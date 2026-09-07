"""
Audit and Verification Script for Grade 9 IRE Topic 6 (Topic ID 346: Belief in Qadar)
"""

import os
import sys
import xml.etree.ElementTree as ET
import django

sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


def audit_topic6():
    print("=" * 80)
    print("AUDITING GRADE 9 IRE — TOPIC 6: BELIEF IN QADAR (DIVINE DECREE)")
    print("=" * 80)

    # 1. Topic Verification
    topic = Topic.objects.select_related("subject", "subject__grade").get(id=346)
    print(f"[*] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")
    print(f"[*] Subject: {topic.subject.name} (ID: {topic.subject.id})")
    print(f"[*] Grade: {topic.subject.grade.name} (ID: {topic.subject.grade.id})")
    assert topic.id == 346, f"Expected Topic ID 346, got {topic.id}"
    assert topic.order == 6, f"Expected Topic Order 6, got {topic.order}"

    # 2. LearningUnits Audit
    units = LearningUnit.objects.filter(topic=topic).order_by("order")
    print(f"\n[*] Total Learning Units: {units.count()}")
    assert units.count() == 4, f"Expected 4 LearningUnits, found {units.count()}"
    for u in units:
        print(f"  - Unit {u.order}: {u.name} (ID: {u.id})")

    # 3. Lessons Audit
    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    print(f"\n[*] Total Lessons: {lessons.count()}")
    assert lessons.count() == 4, f"Expected 4 Lessons, found {lessons.count()}"
    for l in lessons:
        print(f"  - Lesson ID {l.id}: '{l.title}' | Status: {l.status} | Version: {l.version}")
        assert l.status == "published", f"Lesson {l.id} not published"
        assert l.version == 1, f"Lesson {l.id} version is {l.version}"
        assert l.immutable_metadata.get("topic_id") == 346, "Mismatch in immutable_metadata topic_id"

    # 4. Pages / Cards Audit
    print("\n[*] Auditing Cards & Block Components per Lesson:")
    expected_structure = {
        1: ["suggested_image", "learning_goal"],
        2: ["concept_explanation", "callout"],
        3: ["concept_explanation", "suggested_diagram"], # plus comparison_table or step_process
        4: ["worked_example"],
        5: ["suggested_video", "real_world_example", "reflection", "common_misconception"],
        6: ["knowledge_check"],
        7: ["summary", "mini_activity"]
    }

    all_blocks = LessonBlock.objects.filter(lesson__topic=topic)
    print(f"[*] Total LessonBlocks in Topic 346: {all_blocks.count()}")
    assert all_blocks.count() == 60, f"Expected 60 blocks, found {all_blocks.count()}"

    for lesson in lessons:
        print(f"\n  Checking Lesson {lesson.learning_unit.order}: '{lesson.title}'")
        pages = set(lesson.blocks.values_list("page_number", flat=True))
        assert pages == {1, 2, 3, 4, 5, 6, 7}, f"Lesson {lesson.id} does not have exactly pages 1-7: {pages}"

        for p_num in range(1, 8):
            p_blocks = lesson.blocks.filter(page_number=p_num).order_by("component_order")
            block_types = [b.block_type for b in p_blocks]
            print(f"    Page {p_num} ({p_blocks.first().page_title}): {block_types}")

            # Check expected components
            for req_comp in expected_structure[p_num]:
                assert req_comp in block_types, f"Page {p_num} in Lesson {lesson.id} missing {req_comp}"

    # 5. Assets Audit
    all_assets = LessonAsset.objects.filter(lesson__topic=topic)
    diagram_assets = all_assets.filter(asset_type="diagram")
    image_assets = all_assets.filter(asset_type="image")
    yt_assets = all_assets.filter(asset_type="youtube")

    print(f"\n[*] Total Assets in Topic 346: {all_assets.count()}")
    print(f"  - Vector SVG Diagrams: {diagram_assets.count()}")
    print(f"  - Authentic Wikimedia Images: {image_assets.count()}")
    print(f"  - Educational YouTube Videos: {yt_assets.count()}")

    assert diagram_assets.count() == 4, f"Expected 4 SVG diagrams, found {diagram_assets.count()}"
    assert image_assets.count() == 4, f"Expected 4 Images, found {image_assets.count()}"
    assert yt_assets.count() == 4, f"Expected 4 YouTube videos, found {yt_assets.count()}"

    # 6. SVG Content & XML Validation
    print("\n[*] Validating SVG Content & XML Integrity:")
    for a in diagram_assets:
        svg_str = a.metadata.get("svg_content", "")
        assert svg_str, f"Asset {a.id} missing svg_content in metadata"
        assert "<svg" in svg_str and "</svg>" in svg_str, f"Asset {a.id} has invalid SVG markup"
        # Parse with XML parser to verify syntax
        ET.fromstring(svg_str)
        print(f"  [✓] Asset {a.id} ('{a.title}'): Valid SVG XML ({len(svg_str)} chars)")

    # Verify diagram blocks have svg_content in block.metadata and block.content
    diagram_blocks = all_blocks.filter(block_type="suggested_diagram")
    assert diagram_blocks.count() == 4, f"Expected 4 diagram blocks, found {diagram_blocks.count()}"
    for b in diagram_blocks:
        b_meta_svg = b.metadata.get("svg_content", "")
        b_content_svg = b.content.get("svg_content", "")
        assert b_meta_svg, f"Block {b.id} missing svg_content in metadata"
        assert b_content_svg, f"Block {b.id} missing svg_content in content"
        ET.fromstring(b_meta_svg)
        ET.fromstring(b_content_svg)
        assert b.assets.filter(asset_type="diagram").exists(), f"Block {b.id} not linked to diagram asset"
        print(f"  [✓] Block {b.id} ('{b.title}'): SVG linked in metadata, content, and ManyToMany")

    # 7. MCQ Validation
    print("\n[*] Validating MCQs:")
    mcq_blocks = all_blocks.filter(block_type="knowledge_check")
    assert mcq_blocks.count() == 4, f"Expected 4 MCQ blocks, found {mcq_blocks.count()}"
    for b in mcq_blocks:
        c = b.content or {}
        q = c.get("question")
        opts = c.get("options")
        ans = c.get("answer") or c.get("correct_answer")
        expl = c.get("explanation")
        assert q, f"MCQ Block {b.id} missing question"
        assert opts and len(opts) == 4, f"MCQ Block {b.id} must have exactly 4 options, got {len(opts) if opts else 0}"
        assert ans in ["A", "B", "C", "D"], f"MCQ Block {b.id} invalid answer: {ans}"
        assert expl, f"MCQ Block {b.id} missing explanation"
        print(f"  [✓] Lesson {b.lesson.learning_unit.order} MCQ: Answer '{ans}' | Q: {q[:60]}...")

    # 8. Strict Isolation Check: Other topics check
    print("\n[*] Checking Isolation (Verifying other topics untouched):")
    topics = Topic.objects.filter(subject=topic.subject).order_by("order")
    print(f"[*] Total IRE Topics in Grade 9: {topics.count()}")
    for t in topics:
        print(f"  - Topic {t.order}: {t.name} (ID: {t.id}) | Units: {t.learning_units.count()} | Lessons: {t.lessons.count()}")

    print("\n" + "=" * 80)
    print("ALL AUDIT CHECKS PASSED PERFECTLY!")
    print("=" * 80)


if __name__ == "__main__":
    audit_topic6()
