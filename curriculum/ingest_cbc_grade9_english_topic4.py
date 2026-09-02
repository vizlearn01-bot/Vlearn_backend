"""
VLearn CBC Grade 9 English — Topic 4: The Writing Process and Composition
Production Ingestion Script for Lessons 1 to 7
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

# Set up paths and Django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from django.db import transaction
from curriculum.models import (
    Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.cbc_grade9_english_topic4_data import TOPIC_4_LESSONS


def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()


def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


def ingest_grade9_english_topic4(replace=True):
    print("=" * 80)
    print("INGESTING CBC GRADE 9 ENGLISH — TOPIC 4: THE WRITING PROCESS AND COMPOSITION (LESSONS 1 TO 7)")
    print("=" * 80)

    # 1. Resolve Grade 9 (Grade ID 18)
    grade = Grade.objects.filter(id=18).first()
    if not grade:
        grade = Grade.objects.filter(name="Grade 9", curriculum__name="CBC").first()
    if not grade:
        raise ValueError("Could not resolve Grade 9 (Grade ID 18) in database.")
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id}, Curriculum: {grade.curriculum.name if grade.curriculum else 'None'})")

    # 2. Resolve or Create Subject 'English' in Grade 9
    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="English",
        defaults={
            "description": "Junior Secondary English Language and Literature Curriculum (Grade 9 CBC)"
        }
    )
    if s_created:
        print(f"[+] Created new Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")
    else:
        print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    # 3. Resolve or Create Topic 4 'The Writing Process and Composition' (Order 4)
    topic_description = (
        "Mastering writing mechanics, spelling, punctuation marks, paragraph unity and coherence, "
        "functional writing (formal letters and application forms), professional email etiquette, "
        "the 6-stage writing process pipeline, creative narrative composition (Freytag's plot pyramid), "
        "and enriching creative writing with idiomatic expressions."
    )
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=4,
        defaults={
            "name": "The Writing Process and Composition",
            "description": topic_description
        }
    )
    if not t_created:
        topic.name = "The Writing Process and Composition"
        topic.description = topic_description
        topic.save()
        print(f"[*] Updated Topic 4: {topic.name} (ID: {topic.id})")
    else:
        print(f"[+] Created Topic 4: {topic.name} (ID: {topic.id})")

    # Track metrics
    units_created = 0
    lessons_created = 0
    pages_created = 0
    blocks_created = 0
    assets_created = 0

    with transaction.atomic():
        for item in TOPIC_4_LESSONS:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            if replace:
                # Clean up existing unit/lesson for this order if present
                existing_units = LearningUnit.objects.filter(topic=topic, order=u_order)
                for eu in existing_units:
                    existing_lessons = Lesson.objects.filter(learning_unit=eu)
                    LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
                    existing_lessons.delete()
                existing_units.delete()

            # Create LearningUnit
            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            units_created += 1

            # Create Lesson
            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Grade 9 English Curriculum Specialist",
                    "grade": "Grade 9",
                    "subject": "English",
                    "topic_order": 4,
                    "unit_order": u_order,
                    "lesson_number": u_order
                }
            )
            lessons_created += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, 1):
                pages_created += 1
                for block_data in page_blocks:
                    b_type = block_data.get("type", "concept_explanation")
                    b_title = clean_text(block_data.get("title", f"Page {page_idx} Block"))
                    b_content = clean_dict(block_data.get("content", {}))

                    # Map block type to model block_type & component_type
                    block_type_map = {
                        "suggested_image": ("media", "suggested_image"),
                        "learning_goal": ("core", "learning_goal"),
                        "concept_explanation": ("core", "concept_explanation"),
                        "definition_card": ("core", "definition_card"),
                        "comparison_table": ("core", "comparison_table"),
                        "suggested_diagram": ("diagram", "suggested_diagram"),
                        "worked_example": ("practice", "worked_example"),
                        "suggested_video": ("media", "suggested_video"),
                        "real_world_example": ("practice", "real_world_example"),
                        "common_mistake": ("interactive", "common_mistakes"),
                        "step_process": ("practice", "guided_practice"),
                        "knowledge_check": ("assessment", "knowledge_check"),
                        "summary_card": ("core", "summary_card")
                    }

                    mapped_block_type, mapped_comp_type = block_type_map.get(
                        b_type, ("core", b_type)
                    )

                    # Create LessonBlock
                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_idx,
                        order=block_counter,
                        block_type=mapped_block_type,
                        component_type=mapped_comp_type,
                        title=b_title,
                        content=b_content
                    )
                    blocks_created += 1
                    block_counter += 1

                    # Handle and attach LessonAsset if media/diagram
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="generated",
                            storage_type="embedded",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={
                                "svg_content": b_content["svg_content"],
                                "width": "100%",
                                "height": "100%"
                            }
                        )
                        block.assets.add(asset)
                        assets_created += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA")
                            }
                        )
                        block.assets.add(asset)
                        assets_created += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("description", b_title),
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        assets_created += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print("INGESTION SUMMARY:")
    print(f"  Subject:          {subject.name} (Grade ID: {grade.id})")
    print(f"  Topic:            {topic.name} (Order: {topic.order}, ID: {topic.id})")
    print(f"  Units Ingested:   {units_created} (Units 1 to 7)")
    print(f"  Lessons Ingested: {lessons_created}")
    print(f"  Pages Ingested:   {pages_created}")
    print(f"  Blocks Ingested:  {blocks_created}")
    print(f"  Assets Attached:  {assets_created}")
    print("=" * 80)

    return {
        "subject_id": subject.id,
        "subject_name": subject.name,
        "topic_id": topic.id,
        "topic_name": topic.name,
        "units_created": units_created,
        "lessons_created": lessons_created,
        "pages_created": pages_created,
        "blocks_created": blocks_created,
        "assets_created": assets_created
    }


if __name__ == "__main__":
    ingest_grade9_english_topic4(replace=True)
