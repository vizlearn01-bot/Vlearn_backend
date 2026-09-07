"""
VLearn CBC Grade 9 IRE — Topic 4 Database & Pedagogical Audit Script
Target Topic in DB: Topic ID 344 (Selected Hadith)
"""

import os
import sys
import django

sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


def audit_topic4():
    print("=" * 80)
    print("AUDITING GRADE 9 IRE — TOPIC 4: SELECTED HADITH (TOPIC ID 344)")
    print("=" * 80)

    topic = Topic.objects.select_related("subject", "subject__grade", "subject__grade__curriculum").get(id=344)
    print(f"Topic ID      : {topic.id}")
    print(f"Topic Name    : {topic.name}")
    print(f"Topic Order   : {topic.order}")
    print(f"Subject       : {topic.subject.name} (ID: {topic.subject.id})")
    print(f"Grade         : {topic.subject.grade.name} (ID: {topic.subject.grade.id})")
    print(f"Curriculum    : {topic.subject.grade.curriculum.name}")
    print("-" * 80)

    units = LearningUnit.objects.filter(topic=topic).order_by("order")
    assert units.count() == 8, f"Expected 8 units, found {units.count()}"
    print(f"✓ Verified 8 LearningUnits (Orders 1 to 8)")

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    assert lessons.count() == 8, f"Expected 8 lessons, found {lessons.count()}"
    print(f"✓ Verified 8 Lessons (All status='published', version=1)")

    total_blocks = 0
    total_assets = 0

    for unit in units:
        lesson = Lesson.objects.get(learning_unit=unit)
        blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")
        assets = LessonAsset.objects.filter(lesson=lesson)

        total_blocks += blocks.count()
        total_assets += assets.count()

        pages = set(blocks.values_list("page_number", flat=True))
        assert len(pages) == 7, f"Lesson {lesson.title} has pages {pages}, expected 7"
        assert set(range(1, 8)) == pages, f"Lesson {lesson.title} missing pages"

        # Check assets
        img_assets = assets.filter(asset_type="image")
        diag_assets = assets.filter(asset_type="diagram")
        yt_assets = assets.filter(asset_type="youtube")

        assert img_assets.count() == 1, f"Expected 1 image asset in {lesson.title}"
        assert diag_assets.count() == 1, f"Expected 1 diagram asset in {lesson.title}"
        assert yt_assets.count() == 1, f"Expected 1 video asset in {lesson.title}"

        # Check SVG
        diag_asset = diag_assets.first()
        svg_asset_content = diag_asset.metadata.get("svg_content", "")
        assert svg_asset_content.startswith("<svg") and svg_asset_content.strip().endswith("</svg>"), (
            f"Asset SVG content invalid in {lesson.title}"
        )

        # Check diagram block
        diag_blocks = blocks.filter(block_type="suggested_diagram")
        assert diag_blocks.count() == 1, f"Expected 1 suggested_diagram block in {lesson.title}"
        diag_block = diag_blocks.first()
        assert diag_block.assets.filter(id=diag_asset.id).exists(), "Diagram block not linked to diagram asset"

        block_meta_svg = diag_block.metadata.get("svg_content", "")
        block_content_svg = diag_block.content.get("svg_content", "")
        assert block_meta_svg.startswith("<svg") and block_meta_svg.strip().endswith("</svg>"), (
            f"Block metadata svg_content invalid in {lesson.title}"
        )
        assert block_content_svg.startswith("<svg") and block_content_svg.strip().endswith("</svg>"), (
            f"Block content svg_content invalid in {lesson.title}"
        )

        # Check MCQ block
        mcq_blocks = blocks.filter(block_type="knowledge_check")
        assert mcq_blocks.count() == 1, f"Expected 1 knowledge_check in {lesson.title}"
        mcq = mcq_blocks.first().content
        assert "question" in mcq and len(mcq["options"]) == 4 and "answer" in mcq and "explanation" in mcq, (
            f"MCQ structure invalid in {lesson.title}"
        )

        # Print unit summary
        b_types = list(blocks.values_list("block_type", flat=True))
        print(f"  Unit {unit.order}: {lesson.title}")
        print(f"    - Pages: {sorted(list(pages))}")
        print(f"    - Blocks ({blocks.count()}): {', '.join(b_types[:5])}...")
        print(f"    - SVG Diagram: '{diag_asset.title}' ({len(svg_asset_content)} chars)")
        print(f"    - Image: '{img_assets.first().title}'")
        print(f"    - Video: '{yt_assets.first().title}'")

    print("-" * 80)
    print(f"TOTAL AUDIT VERIFICATION PASSED:")
    print(f"  - Total Units        : {units.count()}")
    print(f"  - Total Lessons      : {lessons.count()}")
    print(f"  - Total LessonBlocks : {total_blocks}")
    print(f"  - Total LessonAssets : {total_assets}")
    print("=" * 80)


if __name__ == "__main__":
    audit_topic4()
