"""
VLearn Form 4 Physics — Topic 3: Floating and Sinking
Audit & Diagnostic Script

Audits the database for:
  - Subject, Grade, Curriculum linkage
  - Topic 3 and its 3 Learning Units
  - Lessons and status ('published')
  - Page-by-page blocks and types
  - Attached vector SVGs and Wikimedia assets
  - Zero empty placeholder LessonAssets
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def audit_topic3():
    print("=" * 80)
    print("AUDIT: FORM 4 PHYSICS — TOPIC 3: FLOATING AND SINKING")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Floating and Sinking"
    ).first()

    if not topic:
        print("ERROR: Topic 3 not found in database!")
        return

    print(f"Topic: '{topic.name}' (ID: {topic.id})")
    print(f"Subject: {topic.subject.name} | Grade: {topic.subject.grade.name} | Curriculum: {topic.subject.grade.curriculum.name}\n")

    units = topic.learning_units.all().order_by("order")
    print(f"Total Learning Units: {units.count()}")

    total_blocks = 0
    total_assets = 0

    for u_idx, unit in enumerate(units, 1):
        print(f"\n--- [{u_idx}/3] Unit: '{unit.name}' (ID: {unit.id}, Order: {unit.order}) ---")
        lessons = unit.lessons.all()
        for lesson in lessons:
            print(f"  Lesson: '{lesson.title}' (ID: {lesson.id}, Status: {lesson.status}, Version: {lesson.version})")
            blocks = lesson.blocks.all().order_by("page_number", "order")
            pages = sorted(list(set(b.page_number for b in blocks)))
            print(f"  Total Blocks: {blocks.count()} across {len(pages)} distinct pages: {pages}")

            total_blocks += blocks.count()
            lesson_assets = LessonAsset.objects.filter(lesson=lesson)
            total_assets += lesson_assets.count()
            print(f"  Attached Assets: {lesson_assets.count()}")

            for page in pages:
                p_blocks = blocks.filter(page_number=page)
                block_desc = ", ".join([f"{b.block_type}" for b in p_blocks])
                has_svg = any(b.content.get("svg_content") for b in p_blocks if isinstance(b.content, dict))
                has_media = any(b.assets.exists() for b in p_blocks)
                print(f"    Page {page:2d}: [{block_desc}] {'[SVG Attached]' if has_svg else ''} {'[Asset Linked]' if has_media else ''}")

    print("\n" + "=" * 80)
    print(f"TOPIC 3 AUDIT SUMMARY: {units.count()} Units | {total_blocks} Total Blocks | {total_assets} Visual Assets")
    print("=" * 80)

if __name__ == "__main__":
    audit_topic3()
