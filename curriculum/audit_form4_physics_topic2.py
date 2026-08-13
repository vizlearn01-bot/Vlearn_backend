"""
VLearn Form 4 Physics — Topic 2: Uniform Circular Motion
Audit Tool

Inspects and reports curriculum hierarchy, learning units, lessons, page counts,
block type distributions, worked examples, and attached visual assets for Topic 2.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock, LessonAsset

def audit_topic2():
    print("=" * 100)
    print("VLEARN FORM 4 PHYSICS — TOPIC 2 AUDIT REPORT")
    print("=" * 100)

    topic = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        name__icontains="Uniform Circular Motion"
    ).first()

    if not topic:
        print("ERROR: Topic 2 not found.")
        return

    print(f"Topic: '{topic.name}' (ID: {topic.id}) | Order: {topic.order}")
    print(f"Subject: {topic.subject.name} | Grade: {topic.subject.grade.name} | Curriculum: {topic.subject.grade.curriculum.name}")
    units = topic.learning_units.all().order_by("order")
    print(f"Learning Units: {units.count()}\n")

    total_topic_blocks = 0
    total_topic_assets = 0

    for idx, unit in enumerate(units, start=1):
        print(f"  [Unit {idx}] {unit.name} (ID: {unit.id})")
        lesson = unit.lessons.first()
        if not lesson:
            print("    [Warning] No lesson attached to unit.")
            continue

        blocks = lesson.blocks.all().order_by("page_number", "order")
        pages = blocks.values_list("page_number", flat=True).distinct()
        assets = LessonAsset.objects.filter(lesson=lesson)

        total_topic_blocks += blocks.count()
        total_topic_assets += assets.count()

        formula_count = blocks.filter(block_type="formula_breakdown").count()
        example_count = blocks.filter(block_type="worked_example").count()
        kc_count = blocks.filter(block_type="knowledge_check").count()
        visual_count = blocks.filter(block_type__in=["suggested_diagram", "suggested_graph", "suggested_simulation", "suggested_image"]).count()

        print(f"    Lesson ID: {lesson.id} | Title: '{lesson.title}' | Status: {lesson.status}")
        print(f"    Pages ({len(pages)}): {min(pages) if pages else 0} to {max(pages) if pages else 0} | Total Blocks: {blocks.count()} | Total Assets: {assets.count()}")
        print(f"    Formulas: {formula_count} | Worked Examples: {example_count} | Knowledge Checks: {kc_count} | Visual Slots: {visual_count}")

        for b in blocks.filter(block_type__in=["suggested_diagram", "suggested_graph", "suggested_simulation", "suggested_image"]):
            has_svg = bool(b.metadata and "svg_content" in b.metadata) or bool(isinstance(b.content, dict) and "svg_content" in b.content)
            has_img = bool(isinstance(b.content, dict) and "resolved_image_url" in b.content)
            status_tag = "SVG" if has_svg else ("IMG" if has_img else "SLOT")
            print(f"      - [Page {b.page_number:2d}] [{status_tag}] {b.block_type}: '{b.title[:60]}'")
        print()

    print("=" * 100)
    print(f"SUMMARY: {total_topic_blocks} Total Blocks | {total_topic_assets} Total Assets across Topic 2")
    print("=" * 100)

if __name__ == "__main__":
    audit_topic2()
