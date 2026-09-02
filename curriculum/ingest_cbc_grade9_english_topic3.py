"""
VLearn CBC Grade 9 English — Topic 3: Grammar in Use
Production Ingestion Script for Grade 9, English, Topic 3 (Order 3)
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
from curriculum.cbc_grade9_english_topic3_data import TOPIC_3_LESSONS


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


def ingest_grade9_english_topic3(replace=True):
    print("=" * 80)
    print("INGESTING CBC GRADE 9 ENGLISH — TOPIC 3: GRAMMAR IN USE")
    print("=" * 80)

    # 1. Resolve Grade 9 (Grade ID 18)
    grade = Grade.objects.filter(id=18).first()
    if not grade:
        grade = Grade.objects.filter(name__icontains="Grade 9", curriculum__name="CBC").first()
    if not grade:
        raise ValueError("Could not resolve Grade 9 (Grade ID 18) in database.")
    print(f"[*] Resolved Grade: {grade.name} (ID: {grade.id}, Curriculum: {grade.curriculum.name if grade.curriculum else 'None'})")

    # 2. Resolve or Create Subject 'English' in Grade 9
    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="English",
        defaults={
            "description": "Kenyan Junior Secondary English Language Curriculum (Grade 9 CBC)"
        }
    )
    if s_created:
        print(f"[+] Created new Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")
    else:
        print(f"[*] Resolved Subject: {subject.name} (ID: {subject.id}) in Grade: {grade.name}")

    # 3. Resolve or Create Topic 3 'Grammar in Use' (Order 3)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=3,
        defaults={
            "name": "Grammar in Use",
            "description": "Applying grammar rules accurately in varied contexts, constructing complex sentences, and using inclusive, gender-neutral language."
        }
    )
    if not t_created:
        topic.name = "Grammar in Use"
        topic.description = "Applying grammar rules accurately in varied contexts, constructing complex sentences, and using inclusive, gender-neutral language."
        topic.save()
        print(f"[*] Updated Topic 3: {topic.name} (ID: {topic.id})")
    else:
        print(f"[+] Created Topic 3: {topic.name} (ID: {topic.id})")

    # Track metrics
    units_created = 0
    lessons_created = 0
    blocks_created = 0
    assets_created = 0

    with transaction.atomic():
        for lesson_data in TOPIC_3_LESSONS:
            unit_order = lesson_data["unit_order"]
            unit_name = clean_text(lesson_data["unit_name"])
            unit_desc = clean_text(lesson_data["unit_description"])
            lesson_title = clean_text(lesson_data["lesson_title"])
            pages = lesson_data["pages"]

            # 4. Create or update LearningUnit
            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={
                    "name": unit_name,
                    "description": unit_desc
                }
            )
            if not u_created:
                unit.name = unit_name
                unit.description = unit_desc
                unit.save()
                print(f"\n[*] Updated Unit {unit_order}: '{unit.name}' (ID: {unit.id})")
            else:
                units_created += 1
                print(f"\n[+] Created Unit {unit_order}: '{unit.name}' (ID: {unit.id})")

            # 5. Create or update Lesson
            lesson, l_created = Lesson.objects.get_or_create(
                learning_unit=unit,
                defaults={
                    "topic": topic,
                    "title": lesson_title,
                    "version": 1,
                    "status": "published"
                }
            )
            if not l_created:
                lesson.title = lesson_title
                lesson.topic = topic
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
                print(f"    [*] Updated Lesson: '{lesson.title}' (ID: {lesson.id})")
            else:
                lessons_created += 1
                print(f"    [+] Created Lesson: '{lesson.title}' (ID: {lesson.id})")

            # Clean existing blocks & assets if replace is requested
            if replace:
                existing_assets = LessonAsset.objects.filter(lesson=lesson)
                count_ass_del = existing_assets.count()
                if count_ass_del > 0:
                    existing_assets.delete()
                
                existing_blocks = LessonBlock.objects.filter(lesson=lesson)
                count_del = existing_blocks.count()
                if count_del > 0:
                    existing_blocks.delete()
                    print(f"    [-] Cleared {count_del} existing blocks for replacement")

            # 6. Ingest Blocks across the 6 pages
            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                for comp_order, block_def in enumerate(page_blocks, start=1):
                    comp_type = block_def["type"]
                    comp_title = clean_text(block_def["title"])
                    raw_content = block_def["content"]
                    cleaned_content = clean_dict(raw_content)

                    # Create LessonBlock
                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_order,
                        component_type=comp_type,
                        block_type=comp_type,
                        title=comp_title,
                        content=cleaned_content
                    )
                    block_counter += 1
                    blocks_created += 1

                    # Attach LessonAsset if media block
                    if comp_type == "suggested_diagram" and "svg_content" in cleaned_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=comp_title,
                            description=cleaned_content.get("caption", comp_title),
                            metadata={"svg_content": cleaned_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        assets_created += 1

                    elif comp_type == "suggested_image" and "url" in cleaned_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=comp_title,
                            description=cleaned_content.get("caption", comp_title),
                            url=cleaned_content["url"],
                            metadata={
                                "author": cleaned_content.get("author", "Wikimedia Commons"),
                                "licensing": cleaned_content.get("licensing", "CC BY-SA 4.0"),
                                "caption": cleaned_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        assets_created += 1

                    elif comp_type == "suggested_video" and "youtube_id" in cleaned_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=comp_title,
                            description=cleaned_content.get("description", comp_title),
                            url=cleaned_content.get("url", f"https://www.youtube.com/watch?v={cleaned_content['youtube_id']}"),
                            metadata={"youtube_id": cleaned_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        assets_created += 1

                print(f"        -> Page {page_idx}: Ingested {len(page_blocks)} blocks")

    print("\n" + "=" * 80)
    print("INGESTION COMPLETE SUMMARY:")
    print(f" • Subject: {subject.name} (Grade ID: {grade.id}, Grade: {grade.name})")
    print(f" • Topic: {topic.order}. {topic.name} (ID: {topic.id})")
    print(f" • Learning Units Processed: {len(TOPIC_3_LESSONS)} (New: {units_created})")
    print(f" • Lessons Processed: {len(TOPIC_3_LESSONS)} (New: {lessons_created})")
    print(f" • Lesson Blocks Created: {blocks_created}")
    print(f" • Lesson Assets Created: {assets_created}")
    print("=" * 80)


if __name__ == "__main__":
    ingest_grade9_english_topic3(replace=True)
