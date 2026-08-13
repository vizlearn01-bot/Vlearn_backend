"""
Form 4 Agriculture — Topic 4 Ingestion Engine
Topic: Agricultural Economics III (Production Economics)
Curriculum: 844 (ID: 4) | Grade: Form 4 (ID: 4) | Subject: Agriculture (ID: 19) | Topic ID: 98 (Order: 4)

Usage:
    ./venv/bin/python curriculum/ingest_form4_agriculture_topic4.py [--replace]
"""

import os
import sys
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.topic4_agriculture_data import TOPIC_4_LESSONS

CURRICULUM_ID = 4
GRADE_ID = 4
SUBJECT_ID = 19
TOPIC_ID = 98
TOPIC_TITLE = "Agricultural Economics III (Production Economics)"
TOPIC_ORDER = 4


def ingest_topic4(replace=False):
    print("=" * 80)
    print("STARTING FORM 4 AGRICULTURE TOPIC 4 INGESTION ENGINE")
    print("=" * 80)

    curr = Curriculum.objects.get(id=CURRICULUM_ID)
    grade = Grade.objects.get(id=GRADE_ID)
    subject = Subject.objects.get(id=SUBJECT_ID)

    print(f"[*] Curriculum: {curr.name} (ID: {curr.id})")
    print(f"[*] Grade: {grade.name} (ID: {grade.id})")
    print(f"[*] Subject: {subject.name} (ID: {subject.id})")

    topic, created = Topic.objects.get_or_create(
        id=TOPIC_ID,
        defaults={
            "subject": subject,
            "name": TOPIC_TITLE,
            "order": TOPIC_ORDER,
        }
    )
    if not created:
        topic.subject = subject
        topic.name = TOPIC_TITLE
        topic.order = TOPIC_ORDER
        topic.save()

    print(f"[*] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    if replace:
        print("[!] --replace flag supplied: Cleaning existing units and lessons for Topic 4...")
        LearningUnit.objects.filter(topic=topic).delete()

    total_pages = 0
    total_blocks = 0
    total_assets = 0

    with transaction.atomic():
        for lesson_data in TOPIC_4_LESSONS:
            unit_order = lesson_data["unit_order"]
            unit_name = lesson_data["unit_name"]
            lesson_title = lesson_data["lesson_title"]
            pages = lesson_data["pages"]

            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name}
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
            print(f"\n  [+] Ingesting Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

            # Clean existing blocks for this lesson
            LessonBlock.objects.filter(lesson=lesson).delete()

            block_order = 1
            for page in pages:
                total_pages += 1
                page_num = page["page_number"]
                page_title = page["page_title"]
                blocks = page["blocks"]

                for block_def in blocks:
                    b_type = block_def["block_type"]
                    c_type = block_def["component_type"]
                    b_title = block_def.get("title", "")
                    b_content = block_def.get("content", {})

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_num,
                        order=block_order,
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=b_content
                    )
                    block_order += 1
                    total_blocks += 1

                    # Attach LessonAsset if visual diagram
                    if b_type == "suggested_diagram" and "svg" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            title=b_title,
                            metadata={"svg_content": b_content["svg"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"      - {len(pages)} Pages ingested, {block_order - 1} Blocks created.")

    print("\n" + "=" * 80)
    print("FORM 4 AGRICULTURE TOPIC 4 INGESTION COMPLETE")
    print(f"Total Lessons: {len(TOPIC_4_LESSONS)}")
    print(f"Total Pages: {total_pages}")
    print(f"Total Blocks: {total_blocks}")
    print(f"Total Media Assets Attached: {total_assets}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Form 4 Agriculture Topic 4")
    parser.add_argument("--replace", action="store_true", help="Replace existing units/lessons for Topic 4")
    args = parser.parse_args()

    ingest_topic4(replace=args.replace)
