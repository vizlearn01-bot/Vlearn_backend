"""
VLearn Form 4 Agriculture — Topic 3: Farm Power and Machinery
Authoritative High-Structure Ingestion Engine

Subject: Agriculture (Subject ID: 19)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)
Topic 3: Farm Power and Machinery

Architecture:
  5 Learning Units / Lessons:
  - Lesson 1: Sources and Uses of Farm Power (10 Pages)
  - Lesson 2: Four-Stroke and Two-Stroke Internal Combustion Engines (10 Pages)
  - Lesson 3: Tractor Systems, Lubrication, and Servicing (10 Pages)
  - Lesson 4: Tractor-Drawn Implements (10 Pages)
  - Lesson 5: Animal-Drawn Implements (10 Pages)
  Total: 50 Pages, ~180 Granular Lesson Blocks

Usage:
  ./venv/bin/python curriculum/ingest_form4_agriculture_topic3.py [--replace]
"""

import os
import sys
import re
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

from curriculum.topic3_agriculture_data import ALL_LESSONS

def clean_text(raw_str):
    """Remove source citation brackets like [56], [61], [107] and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    """Recursively clean text within content dicts or lists."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data

def run_ingestion(replace=False):
    print("=" * 80)
    print("STARTING FORM 4 AGRICULTURE TOPIC 3 INGESTION ENGINE")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Hierarchy
        curriculum, _ = Curriculum.objects.get_or_create(
            name="844",
            defaults={"description": "Kenyan 8-4-4 National Curriculum"}
        )
        print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")

        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Form 4",
            defaults={"level": 4, "description": "Form 4 Secondary"}
        )
        print(f"[*] Grade: {grade.name} (ID: {grade.id})")

        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Agriculture",
            defaults={"description": "Secondary Agriculture Form 4"}
        )
        print(f"[*] Subject: {subject.name} (ID: {subject.id})")

        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            name="Farm Power and Machinery",
            defaults={
                "order": 3,
                "description": (
                    "Covers farm power sources, 2-stroke/4-stroke IC engines, tractor systems, "
                    "servicing, tractor-drawn implements, and animal-drawn implements."
                )
            }
        )
        topic.order = 3
        topic.save()
        print(f"[*] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

        if replace:
            print("[!] --replace flag supplied: Cleaning existing units and lessons for Topic 3...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()

        total_pages = 0
        total_blocks = 0
        total_assets = 0

        # Ingest Lessons
        for lesson_data in ALL_LESSONS:
            unit_order = lesson_data["unit_order"]
            unit_name = lesson_data["unit_name"]
            lesson_title = lesson_data["lesson_title"]
            pages = lesson_data["pages"]

            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": f"Learning Unit {unit_order}: {unit_name}"}
            )
            unit.name = unit_name
            unit.save()

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=lesson_title,
                status="published",
                version=1
            )
            print(f"\n  [+] Ingesting Lesson {unit_order}: {lesson_title} (ID: {lesson.id})")

            block_global_order = 1

            for page_idx, page in enumerate(pages, 1):
                page_num = page["page_number"]
                page_title = page["page_title"]
                blocks = page["blocks"]

                total_pages += 1

                for comp_idx, block_info in enumerate(blocks, 1):
                    b_type = block_info["block_type"]
                    c_type = block_info.get("component_type", b_type)
                    b_title = block_info.get("title", f"Page {page_num} - {c_type}")
                    raw_content = block_info.get("content", {})

                    cleaned_content = clean_content_dict(raw_content)

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"ag4_t3_l{unit_order}_p{page_num}_b{comp_idx}",
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=cleaned_content,
                        page_number=page_num,
                        page_title=page_title,
                        component_order=comp_idx,
                        order=block_global_order
                    )
                    block_global_order += 1
                    total_blocks += 1

                    # Process Media Assets
                    if c_type in ["suggested_image", "suggested_diagram", "suggested_video"]:
                        asset_type_map = {
                            "suggested_image": "image",
                            "suggested_diagram": "diagram",
                            "suggested_video": "youtube"
                        }
                        a_type = asset_type_map.get(c_type, "image")
                        asset_url = cleaned_content.get("url", "")
                        asset_desc = cleaned_content.get("text", b_title)

                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type=a_type,
                            source_type="external" if a_type != "diagram" else "ai_generated",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=asset_desc,
                            url=asset_url if asset_url else None,
                            metadata=cleaned_content
                        )
                        asset.blocks.add(block)
                        total_assets += 1

            print(f"      - {len(pages)} Pages ingested, {block_global_order - 1} Blocks created.")

        print("\n" + "=" * 80)
        print(f"FORM 4 AGRICULTURE TOPIC 3 INGESTION COMPLETE")
        print(f"Total Lessons: {len(ALL_LESSONS)}")
        print(f"Total Pages: {total_pages}")
        print(f"Total Blocks: {total_blocks}")
        print(f"Total Media Assets Attached: {total_assets}")
        print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 Agriculture Topic 3")
    parser.add_argument("--replace", action="store_true", help="Replace existing Topic 3 data")
    args = parser.parse_args()

    run_ingestion(replace=args.replace)
