"""
Form 4 Physics — Topic 6 Ingestion Audit Tool
Prints comprehensive summary of Topic 6 database persistence, modular hierarchy, page structure, block types, and attached visual assets.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def audit_topic6():
    print("=" * 80)
    print("AUDIT: FORM 4 PHYSICS — TOPIC 6: MAINS ELECTRICITY")
    print("=" * 80)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Mains Electricity"
    ).first()

    if not topic:
        print("ERROR: Topic 6: Mains Electricity not found in database!")
        return

    print(f"Topic: '{topic.name}' (ID: {topic.id})")
    print(f"Subject: {topic.subject.name} | Grade: {topic.subject.grade.name} | Curriculum: {topic.subject.grade.curriculum.name}\n")

    units = topic.learning_units.all().order_by("order")
    print(f"Total Learning Units: {units.count()}\n")

    total_blocks_all = 0
    total_assets_all = 0

    for u_idx, unit in enumerate(units, start=1):
        lesson = unit.lessons.first()
        blocks = lesson.blocks.all().order_by("page_number", "order") if lesson else []
        pages = sorted(list(set(b.page_number for b in blocks)))
        assets = LessonAsset.objects.filter(lesson=lesson) if lesson else []

        total_blocks_all += len(blocks)
        total_assets_all += assets.count()

        print(f"--- [{u_idx}/{units.count()}] Unit: '{unit.name}' (ID: {unit.id}, Order: {unit.order}) ---")
        if lesson:
            print(f"  Lesson: '{lesson.title}' (ID: {lesson.id}, Status: {lesson.status}, Version: {lesson.version})")
            print(f"  Total Blocks: {len(blocks)} across {len(pages)} distinct pages: {pages}")
            print(f"  Attached Assets: {assets.count()}")

            for page in pages:
                page_blocks = [b for b in blocks if b.page_number == page]
                types = [b.block_type for b in page_blocks]
                has_svg = any(
                    (isinstance(b.content, dict) and bool(b.content.get("svg_content"))) or
                    (bool(b.metadata) and bool(b.metadata.get("svg_content")))
                    for b in page_blocks
                )
                has_asset = any(b.assets.exists() for b in page_blocks)
                status_str = ""
                if has_svg:
                    status_str += " [SVG Attached]"
                if has_asset:
                    status_str += " [Asset Linked]"

                print(f"    Page {page:2d}: {types}{status_str}")
        print()

    print("=" * 80)
    print(f"TOPIC 6 AUDIT SUMMARY: {units.count()} Units | {total_blocks_all} Total Blocks | {total_assets_all} Visual Assets")
    print("=" * 80)

if __name__ == "__main__":
    audit_topic6()
