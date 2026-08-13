"""
Form 4 Agriculture — Topic 4 Automated Verification Suite
Topic: Agricultural Economics III (Production Economics)
Curriculum: 844 (ID: 4) | Grade: Form 4 (ID: 4) | Subject: Agriculture (ID: 19) | Topic ID: 98 (Order: 4)

Usage:
    ./venv/bin/python curriculum/test_form4_agriculture_topic4.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

EXPECTED_CURRICULUM_ID = 4
EXPECTED_GRADE_ID = 4
EXPECTED_SUBJECT_ID = 19
EXPECTED_TOPIC_ID = 98
EXPECTED_LESSON_COUNT = 5
EXPECTED_PAGE_COUNT = 50
EXPECTED_MIN_BLOCK_COUNT = 50
EXPECTED_ASSET_COUNT = 5

EXPECTED_UNITS = [
    "Agriculture, National Income, and Production Resources",
    "Production Functions, Marginal Products, and Production Zones",
    "Substitution, Equimarginal Returns, and Profit Maximisation",
    "Farm Planning and Budgeting",
    "Agricultural Support Services, Credit, and Risk Management"
]


def run_tests():
    print("=" * 80)
    print("RUNNING AUTOMATED TEST SUITE: FORM 4 AGRICULTURE TOPIC 4")
    print("TOPIC: AGRICULTURAL ECONOMICS III (PRODUCTION ECONOMICS)")
    print("=" * 80)

    # Test 1: Hierarchy Verification
    curr = Curriculum.objects.get(id=EXPECTED_CURRICULUM_ID)
    grade = Grade.objects.get(id=EXPECTED_GRADE_ID)
    subject = Subject.objects.get(id=EXPECTED_SUBJECT_ID)
    assert subject.grade == grade and grade.curriculum == curr, "Hierarchy mismatch!"
    print(f"[PASS] 1. Hierarchy resolved: {curr.name} -> {grade.name} -> {subject.name} (Subject ID: {subject.id})")

    # Test 2: Topic Resolution
    topic = Topic.objects.get(id=EXPECTED_TOPIC_ID, subject=subject)
    assert topic.order == 4, f"Expected order 4, got {topic.order}"
    print(f"[PASS] 2. Topic resolved: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Test 3: Units & Lessons Resolution
    units = LearningUnit.objects.filter(topic=topic).order_by("order")
    assert units.count() == EXPECTED_LESSON_COUNT, f"Expected {EXPECTED_LESSON_COUNT} units, got {units.count()}"

    lessons = Lesson.objects.filter(topic=topic, status="published").order_by("learning_unit__order")
    assert lessons.count() == EXPECTED_LESSON_COUNT, f"Expected {EXPECTED_LESSON_COUNT} lessons, got {lessons.count()}"

    print(f"[PASS] 3. Verified {units.count()} Learning Units and {lessons.count()} Published Lessons:")
    for u in units:
        print(f"       - Unit {u.order}: {u.name}")

    # Test 4: Page & Block Counts
    all_blocks = LessonBlock.objects.filter(lesson__topic=topic)
    block_count = all_blocks.count()
    pages_seen = set((b.lesson_id, b.page_number) for b in all_blocks)
    page_count = len(pages_seen)

    assert page_count == EXPECTED_PAGE_COUNT, f"Expected {EXPECTED_PAGE_COUNT} pages, got {page_count}"
    assert block_count >= EXPECTED_MIN_BLOCK_COUNT, f"Expected at least {EXPECTED_MIN_BLOCK_COUNT} blocks, got {block_count}"
    print(f"[PASS] 4. Page & Block Structure verified: {page_count} Pages, {block_count} Blocks across {lessons.count()} Lessons.")

    # Test 5: Citation Bracket Leakage Test
    citation_pattern = re.compile(r"\[\d+\]")
    bracket_leaks = []
    for b in all_blocks:
        text_content = str(b.content)
        matches = citation_pattern.findall(text_content)
        if matches:
            bracket_leaks.append((b.id, b.title, matches))

    assert len(bracket_leaks) == 0, f"Found citation bracket leaks: {bracket_leaks}"
    print("[PASS] 5. Zero citation brackets ([110], [114], [138]) found across all block contents.")

    # Test 6: Raw LaTeX / KaTeX Leakage Test
    latex_pattern = re.compile(r"\\(frac|text|mathrm|begin|end|left|right)|(\$\$|\\[\(\)\[\]])")
    latex_leaks = []
    for b in all_blocks:
        text_content = str(b.content)
        matches = latex_pattern.findall(text_content)
        if matches:
            latex_leaks.append((b.id, b.title, matches))

    assert len(latex_leaks) == 0, f"Found raw LaTeX leaks: {latex_leaks}"
    print("[PASS] 6. Zero raw LaTeX / KaTeX leakage found.")

    # Test 7: Internal Developer Terms & System Captions
    forbidden_terms = ["INSERT_", "PLACEHOLDER", "TODO", "FIXME", "LATEX_ERROR"]
    term_leaks = []
    for b in all_blocks:
        text_content = str(b.content).upper()
        for term in forbidden_terms:
            if term in text_content:
                term_leaks.append((b.id, term))

    assert len(term_leaks) == 0, f"Found forbidden system terms: {term_leaks}"
    print("[PASS] 7. Zero internal developer terms or system captions found.")

    # Test 8: Knowledge Check MCQ Validation
    mcq_blocks = all_blocks.filter(component_type="knowledge_check")
    assert mcq_blocks.count() == 5, f"Expected 5 MCQs, found {mcq_blocks.count()}"

    for mcq in mcq_blocks:
        c = mcq.content
        assert "options" in c and len(c["options"]) >= 3, f"MCQ {mcq.id} missing options"
        assert "correct_answer_index" in c and 0 <= c["correct_answer_index"] < len(c["options"]), f"MCQ {mcq.id} invalid correct answer index"
        assert "explanation" in c and len(c["explanation"]) > 10, f"MCQ {mcq.id} explanation missing or too short"

    print(f"[PASS] 8. Verified {mcq_blocks.count()} Knowledge Check MCQs (options >= 3, valid answer index, non-empty explanation).")

    # Test 9: LessonAsset Database Linkage Test
    diagram_blocks = all_blocks.filter(component_type="suggested_diagram")
    assert diagram_blocks.count() == EXPECTED_ASSET_COUNT, f"Expected {EXPECTED_ASSET_COUNT} diagram blocks, got {diagram_blocks.count()}"

    for db in diagram_blocks:
        assert db.assets.count() > 0, f"Diagram block {db.id} ({db.title}) has no attached LessonAsset!"
        asset = db.assets.first()
        assert "svg_content" in asset.metadata and len(asset.metadata["svg_content"]) > 100, f"Asset {asset.id} missing valid SVG content!"

    print(f"[PASS] 9. Verified 100% LessonAsset database linkage for all {diagram_blocks.count()} visual blocks.")

    print("\n" + "=" * 80)
    print("ALL 9 AUTOMATED TESTS PASSED SUCCESSFULLY!")
    print("FORM 4 AGRICULTURE TOPIC 4 IS 100% VERIFIED & PRODUCTION-READY")
    print("=" * 80)


if __name__ == "__main__":
    run_tests()
