"""
VLearn Ingestion Script for CBC Grade 10 Business Studies — Topic 12: International Trade
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.cbc_grade10_business_studies_topic12_data import TOPIC_12_LESSONS

def ingest_topic_12():
    print("=" * 80)
    print("INGESTING CBC GRADE 10 BUSINESS STUDIES — TOPIC 12: INTERNATIONAL TRADE")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' not found!")

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC!")

    subject = Subject.objects.filter(grade=grade, name__icontains="Business").first()
    if not subject:
        raise ValueError("Subject 'Business Studies' not found under Grade 10!")

    topic, _ = Topic.objects.update_or_create(
        subject=subject,
        order=12,
        defaults={
            "name": "International Trade",
            "description": "Cross-border commerce, visible and invisible trade, Balance of Payments, Incoterms, international payment methods, protectionism, and currency exchange math."
        }
    )
    print(f"Topic configured: ID {topic.id} - {topic.name}")

    total_units = 0
    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    for lesson_def in TOPIC_12_LESSONS:
        u_order = lesson_def["unit_order"]
        u_name = lesson_def["unit_name"]
        u_desc = lesson_def["unit_description"]
        l_title = lesson_def["lesson_title"]
        pages = lesson_def["pages"]

        unit, _ = LearningUnit.objects.update_or_create(
            topic=topic,
            order=u_order,
            defaults={
                "name": u_name,
                "description": u_desc
            }
        )
        total_units += 1

        lesson, _ = Lesson.objects.update_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": l_title,
                "status": "published",
                "version": 1
            }
        )
        total_lessons += 1

        # Clear existing blocks and assets for idempotency
        LessonBlock.objects.filter(lesson=lesson).delete()
        LessonAsset.objects.filter(lesson=lesson).delete()

        block_order = 1
        for page_idx, page_blocks in enumerate(pages, start=1):
            for b in page_blocks:
                b_type = b["type"]
                b_title = b.get("title", "")
                b_content = b.get("content", {})

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    title=b_title,
                    content=b_content,
                    page_number=page_idx,
                    order=block_order
                )
                block_order += 1
                total_blocks += 1

                # If block is suggested_image, create LessonAsset
                if b_type == "suggested_image":
                    LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="image",
                        title=b_title,
                        url=b_content.get("url", ""),
                        metadata=b_content
                    )
                    total_assets += 1
                elif b_type == "suggested_diagram":
                    LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        title=b_title,
                        url="",
                        metadata=b_content
                    )
                    total_assets += 1
                elif b_type == "suggested_video":
                    LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="youtube",
                        title=b_title,
                        url=f"https://www.youtube.com/watch?v={b_content.get('youtube_id', '')}",
                        metadata=b_content
                    )
                    total_assets += 1

        print(f"  -> Ingested Unit {u_order}: {l_title} (Pages: {len(pages)}, Blocks: {block_order - 1})")

    print("=" * 80)
    print(f"TOPIC 12 INGESTION COMPLETE:")
    print(f"  Learning Units:  {total_units}")
    print(f"  Lessons:         {total_lessons}")
    print(f"  Blocks:          {total_blocks}")
    print(f"  Lesson Assets:   {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_topic_12()
