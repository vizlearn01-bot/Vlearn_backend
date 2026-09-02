"""
VLearn CBC Grade 10 History — Topic 11: Global Governance and the Role of the UN
Authoritative Ingestion & Enrichment Engine

Subject: History
Grade: Grade 10
Curriculum: CBC
Topic Order: 11
Topic Name: "Topic 3.2B: Global Governance and the Role of the UN"
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.cbc_grade10_history_topic11_data import TOPIC_11_LESSONS

def clean_text(text: str) -> str:
    """Removes bracket citations, [VISUAL: ...] tags, and normalizes formatting."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[VISUAL:[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[/VISUAL\]', '', text, flags=re.IGNORECASE)
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

def ingest_grade10_history_topic11(replace=True):
    print("=" * 80)
    print("INGESTING TOPIC 11: Global Governance and the Role of the UN (Grade 10 History)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first()
    if not curriculum:
        curriculum, _ = Curriculum.objects.get_or_create(
            name="CBC",
            defaults={"description": "Competency-Based Curriculum (Kenya)"}
        )
    print(f"[*] Resolved Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            level=10,
            defaults={"name": "Grade 10"}
        )
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    subject = Subject.objects.filter(grade=grade, name="History").first()
    if not subject:
        subject = Subject.objects.create(
            grade=grade,
            name="History",
            description="Grade 10 CBC History and Citizenship Curriculum"
        )
    print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    topic_name = "Topic 3.2B: Global Governance and the Role of the UN"
    topic_desc = "Meaning and principles of global governance, borderless challenges, Montreal Protocol success, UN Security Council veto mechanics, and responsible global citizenship."

    topic = Topic.objects.filter(subject=subject, order=11).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            order=11,
            name=topic_name,
            description=topic_desc
        )
        print(f"[*] Created Topic 11: {topic.name} (ID: {topic.id})")
    else:
        topic.name = topic_name
        topic.description = topic_desc
        topic.save()
        print(f"[*] Resolved & Updated Topic 11: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Replacing existing Topic 11 units, lessons, blocks, and assets...")
        existing_lessons = Lesson.objects.filter(topic=topic)
        LessonAsset.objects.filter(lesson__in=existing_lessons).delete()
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for item in TOPIC_11_LESSONS:
            u_order = item["unit_order"]
            u_name = item["unit_name"]
            u_desc = item["unit_description"]
            l_title = item["lesson_title"]
            pages = item["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Senior History Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "History",
                    "topic_order": 11,
                    "unit_order": u_order,
                    "strand": "3.0: World History and Global Citizenship"
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    if b_type == "interactive_quiz":
                        b_type = "knowledge_check"
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_hist_t11_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 11, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAsset if applicable
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="knowledge_repository",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA 4.0 / Public Domain"),
                                "caption": b_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

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
                        total_assets += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print("TOPIC 11 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_history_topic11(replace=True)
