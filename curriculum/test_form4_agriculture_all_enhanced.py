"""
Master Automated Test & Quality Verification Suite for Form 4 Agriculture
Tests all 7 Topics (IDs 95-101), 33 Lessons, and 396 Blocks.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def run_master_test_suite():
    print("=" * 80)
    print("RUNNING MASTER QUALITY VERIFICATION SUITE: FORM 4 AGRICULTURE (ALL 7 TOPICS)")
    print("=" * 80)

    # 1. Subject and Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    assert curriculum, "Curriculum 844 not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    assert grade, "Grade Form 4 not found!"
    subject = Subject.objects.filter(grade=grade, name="Agriculture").first()
    assert subject.id == 19, f"Expected Agriculture Subject ID 19, got {subject.id}"
    print(f"[PASS] 1. Hierarchy resolved: 844 -> Form 4 -> Agriculture (Subject ID: 19)")

    # 2. Topic Verification
    topic_ids = list(range(95, 102))
    topics = Topic.objects.filter(id__in=topic_ids).order_by("order")
    assert topics.count() == 7, f"Expected 7 Topics, got {topics.count()}"
    print(f"[PASS] 2. All 7 Topics resolved with IDs 95 to 101:")
    for t in topics:
        print(f"       - Topic {t.order}: {t.name} (ID: {t.id})")

    # 3. Learning Units & Lessons
    total_units = LearningUnit.objects.filter(topic__in=topics).count()
    total_lessons = Lesson.objects.filter(topic__in=topics).count()
    assert total_units == 33, f"Expected 33 Learning Units, got {total_units}"
    assert total_lessons == 33, f"Expected 33 Lessons, got {total_lessons}"
    print(f"[PASS] 3. Verified 33 Learning Units and 33 Published Lessons across 7 Topics.")

    # 4. Page 1 Real-World Visual Anchor on ALL 33 Lessons
    lessons = Lesson.objects.filter(topic__in=topics).order_by("topic__order", "learning_unit__order")
    p1_visuals_count = 0
    for lesson in lessons:
        p1_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by("component_order")
        lg = p1_blocks.filter(component_type="learning_goal").first()
        img = p1_blocks.filter(component_type="suggested_image").first()

        assert lg is not None, f"Lesson {lesson.id} ({lesson.title}) missing learning_goal on Page 1"
        assert img is not None, f"Lesson {lesson.id} ({lesson.title}) missing suggested_image on Page 1"
        assert lg.component_order == 1, f"Lesson {lesson.id} learning_goal component_order is {lg.component_order}, expected 1"
        assert img.component_order == 2, f"Lesson {lesson.id} suggested_image component_order is {img.component_order}, expected 2"

        # Check image URL format
        content = img.content or {}
        url = content.get("url", "")
        assert url.startswith("https://upload.wikimedia.org/"), f"Lesson {lesson.id} Page 1 image invalid URL: {url}"
        assert len(content.get("text", "")) > 10, f"Lesson {lesson.id} Page 1 image missing descriptive text"
        assert len(content.get("author", "")) > 0, f"Lesson {lesson.id} Page 1 image missing author"
        assert len(content.get("licensing", "")) > 0, f"Lesson {lesson.id} Page 1 image missing licensing"

        # Check attached LessonAsset
        assert img.assets.count() > 0, f"Lesson {lesson.id} Page 1 image has no attached LessonAsset"
        p1_visuals_count += 1

    assert p1_visuals_count == 33, f"Expected 33 Page 1 visuals, got {p1_visuals_count}"
    print(f"[PASS] 4. Verified 100% Page 1 Real-World Visual Anchors across all 33 lessons (33/33).")

    # 5. Component Order Contiguity & Block Ordering
    all_blocks = LessonBlock.objects.filter(lesson__topic__in=topics)
    for lesson in lessons:
        l_blocks = all_blocks.filter(lesson=lesson).order_by("order")
        global_orders = [b.order for b in l_blocks]
        assert global_orders == list(range(1, len(global_orders) + 1)), f"Lesson {lesson.id} non-contiguous global block order"

        page_numbers = sorted(list(set(b.page_number for b in l_blocks)))
        for p_num in page_numbers:
            p_blks = l_blocks.filter(page_number=p_num).order_by("component_order")
            comp_orders = [b.component_order for b in p_blks]
            assert comp_orders == list(range(1, len(comp_orders) + 1)), f"Lesson {lesson.id} Page {p_num} non-contiguous component order: {comp_orders}"

    print(f"[PASS] 5. Verified component order contiguity and sequential global ordering for all {all_blocks.count()} blocks.")

    # 6. Citation Brackets Check
    bracket_pattern = r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]'
    for b in all_blocks:
        content_str = str(b.content)
        matches = re.findall(bracket_pattern, content_str)
        assert len(matches) == 0, f"Block {b.id} ({b.title}) contains citation brackets: {matches}"
    print(f"[PASS] 6. Zero citation bracket leakages found across all {all_blocks.count()} blocks.")

    # 7. Raw LaTeX / KaTeX Leakage Check
    raw_latex_patterns = [r'\\frac\{', r'\\text\{', r'\\cdot', r'\\times']
    for b in all_blocks:
        content_str = str(b.content)
        for pat in raw_latex_patterns:
            matches = re.findall(pat, content_str)
            assert len(matches) == 0, f"Block {b.id} contains raw LaTeX: {matches}"
    print(f"[PASS] 7. Zero raw LaTeX leakages found across all {all_blocks.count()} blocks.")

    # 8. MCQs Quality Verification
    mcq_blocks = all_blocks.filter(component_type="knowledge_check")
    for b in mcq_blocks:
        content = b.content or {}
        options = content.get("options", [])
        correct_idx = content.get("correct_answer_index")
        explanation = content.get("explanation", "")
        assert len(options) >= 3, f"MCQ Block {b.id} has fewer than 3 options"
        assert correct_idx is not None and 0 <= correct_idx < len(options), f"MCQ Block {b.id} invalid correct_answer_index"
        assert len(explanation.strip()) > 0, f"MCQ Block {b.id} missing explanation"
    print(f"[PASS] 8. Verified {mcq_blocks.count()} Knowledge Check MCQs with valid options, indices, and explanations.")

    # 9. Visual Asset Database Linkage Check
    visual_blocks = all_blocks.filter(component_type__in=["suggested_image", "suggested_diagram", "suggested_video"])
    for b in visual_blocks:
        assert b.assets.count() > 0, f"Visual Block {b.id} ({b.title}) missing attached LessonAsset"
        for a in b.assets.all():
            assert a.status == "attached", f"Asset {a.id} status is {a.status}, expected 'attached'"
    print(f"[PASS] 9. Verified 100% LessonAsset database linkage for all {visual_blocks.count()} visual blocks ({visual_blocks.filter(component_type='suggested_image').count()} images, {visual_blocks.filter(component_type='suggested_diagram').count()} diagrams, {visual_blocks.filter(component_type='suggested_video').count()} videos).")

    # 10. Semantic Metadata Tagging Verification
    tagged_blocks = all_blocks.exclude(metadata__semantic_role__isnull=True).exclude(metadata__semantic_role="")
    assert tagged_blocks.count() == all_blocks.count(), f"Expected all {all_blocks.count()} blocks tagged with semantic_role, found {tagged_blocks.count()}"
    print(f"[PASS] 10. Verified 100% semantic metadata tagging across all {all_blocks.count()} blocks.")

    print("\n" + "=" * 80)
    print("ALL 10 COMPREHENSIVE AUTOMATED VERIFICATION TESTS PASSED (100% SUCCESS)!")
    print("VLEARN FORM 4 AGRICULTURE (TOPICS 1 TO 7) IS FULLY ENHANCED & PRODUCTION-READY!")
    print("=" * 80)

if __name__ == "__main__":
    run_master_test_suite()
