"""
VLearn Form 4 Mathematics — Topic 2: Statistics II
Validation Test Suite

Run with:
  source venv/bin/activate
  python curriculum/test_form4_math_topic2_ingestion.py
"""

import os
import sys
import json
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

DEVELOPER_LEAK_PATTERNS = [
    r"component_type",
    r"block_type",
    r"ai_instruction",
    r"asset_info",
    r"block_id",
    r"internal_page",
    r"TODO",
    r"\bDEBUG\b",
    r"implementation_note",
    r"ingestion_tag",
    r"\braw_prompt\b",
    r"database_metadata",
    r"page_number_override",
]


def get_topic():
    return Topic.objects.filter(
        subject__name="Mathematics",
        subject__grade__name="Form 4",
        name__icontains="Statistics II"
    ).first()


def text_of_content(content):
    """Recursively extract all text strings from a content dict/list/str."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(text_of_content(x) for x in content)
    if isinstance(content, dict):
        return " ".join(text_of_content(v) for v in content.values())
    return ""


def check_developer_leak(text):
    violations = []
    for pattern in DEVELOPER_LEAK_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            violations.append(f"Pattern '{pattern}' found: {matches[:3]}")
    return violations


def check_latex_balance(text):
    """Check that LaTeX delimiters are balanced."""
    issues = []
    display_count = len(re.findall(r"\$\$", text))
    if display_count % 2 != 0:
        issues.append(f"Odd number of $$ delimiters ({display_count})")

    inline_text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    single_dollars = re.findall(r"(?<!\$)\$(?!\$)", inline_text)
    if len(single_dollars) % 2 != 0:
        issues.append(f"Odd number of $ delimiters ({len(single_dollars)} after removing $$)")

    begins = re.findall(r"\\begin\{(\w+)\}", text)
    ends = re.findall(r"\\end\{(\w+)\}", text)
    if sorted(begins) != sorted(ends):
        issues.append(f"\\begin/\\end mismatch: begins={begins}, ends={ends}")

    return issues


# ---------------------------------------------------------------------------
# Test Classes
# ---------------------------------------------------------------------------

class TestHierarchy:

    def test_curriculum_exists(self):
        c = Curriculum.objects.filter(name="844").first()
        assert c is not None, "Curriculum '844' not found"

    def test_grade_exists(self):
        g = Grade.objects.filter(name="Form 4", curriculum__name="844").first()
        assert g is not None, "Grade 'Form 4' not found"

    def test_subject_exists(self):
        s = Subject.objects.filter(name="Mathematics", grade__name="Form 4").first()
        assert s is not None, "Subject 'Mathematics' under Form 4 not found"

    def test_topic_exists(self):
        t = get_topic()
        assert t is not None, "Topic 'Topic 2: Statistics II' not found"

    def test_exactly_4_learning_units(self):
        t = get_topic()
        assert t is not None
        count = LearningUnit.objects.filter(topic=t).count()
        assert count == 4, f"Expected 4 learning units, found {count}"

    def test_exactly_4_lessons(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lesson_count = Lesson.objects.filter(learning_unit__in=units).count()
        assert lesson_count == 4, f"Expected 4 lessons, found {lesson_count}"


class TestLessonPublishStatus:

    def test_all_lessons_published(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        draft_lessons = [l.title for l in lessons if l.status != "published"]
        assert not draft_lessons, f"Lessons not published: {draft_lessons}"


class TestBlockCounts:

    def get_all_blocks(self):
        t = get_topic()
        if not t:
            return []
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        return LessonBlock.objects.filter(lesson__in=lessons)

    def test_minimum_total_blocks(self):
        blocks = self.get_all_blocks()
        assert blocks.count() >= 40, (
            f"Expected at least 40 blocks total, found {blocks.count()}"
        )

    def test_each_lesson_has_minimum_8_pages(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            max_page = blocks.order_by("-page_number").values_list("page_number", flat=True).first()
            assert max_page is not None and max_page >= 8, (
                f"Lesson '{lesson.title}' has only {max_page} pages — minimum is 8"
            )

    def test_each_lesson_has_learning_goal(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            has_goal = LessonBlock.objects.filter(
                lesson=lesson, block_type="learning_goal"
            ).exists()
            assert has_goal, f"Lesson '{lesson.title}' is missing a learning_goal block"

    def test_each_lesson_has_summary(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            has_summary = LessonBlock.objects.filter(
                lesson=lesson, block_type="summary"
            ).exists()
            assert has_summary, f"Lesson '{lesson.title}' is missing a summary block"

    def test_each_lesson_has_at_least_3_worked_examples(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            count = LessonBlock.objects.filter(
                lesson=lesson, block_type="worked_example"
            ).count()
            assert count >= 3, (
                f"Lesson '{lesson.title}' has only {count} worked examples — minimum is 3"
            )

    def test_each_lesson_has_knowledge_check(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            has_check = LessonBlock.objects.filter(
                lesson=lesson,
                block_type__in=["knowledge_check", "multiple_choice", "short_answer"]
            ).exists()
            assert has_check, f"Lesson '{lesson.title}' has no knowledge check or practice block"

    def test_each_lesson_has_misconception_block(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            has_misconception = LessonBlock.objects.filter(
                lesson=lesson,
                block_type__in=["common_misconception", "common_mistake"]
            ).exists()
            assert has_misconception, f"Lesson '{lesson.title}' is missing a misconception block"


class TestBlockOrdering:

    def test_learning_goal_is_on_page_1(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            goal_pages = LessonBlock.objects.filter(
                lesson=lesson, block_type="learning_goal"
            ).values_list("page_number", flat=True)
            for pg in goal_pages:
                assert pg == 1, (
                    f"Lesson '{lesson.title}': learning_goal found on page {pg}, expected page 1"
                )

    def test_summary_is_on_last_page(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            all_blocks = LessonBlock.objects.filter(lesson=lesson)
            max_page = all_blocks.order_by("-page_number").values_list("page_number", flat=True).first()
            summary_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="summary")
            if summary_blocks.exists():
                summary_max_page = summary_blocks.order_by("-page_number").values_list("page_number", flat=True).first()
                assert summary_max_page == max_page, (
                    f"Lesson '{lesson.title}': summary is on page {summary_max_page}, "
                    f"but last page is {max_page}"
                )

    def test_page_numbers_are_sequential(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        for lesson in lessons:
            pages = list(LessonBlock.objects.filter(
                lesson=lesson
            ).values_list("page_number", flat=True).distinct().order_by("page_number"))
            if pages:
                assert pages[0] == 1, f"Lesson '{lesson.title}': pages do not start at 1 (starts at {pages[0]})"
                for i in range(len(pages) - 1):
                    assert pages[i+1] - pages[i] <= 1, (
                        f"Lesson '{lesson.title}': gap in page numbers between {pages[i]} and {pages[i+1]}"
                    )


class TestContentQuality:

    def test_no_developer_leakage_in_content(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        all_violations = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for block in blocks:
                content_text = text_of_content(block.content)
                title_text = block.title or ""
                combined = content_text + " " + title_text
                violations = check_developer_leak(combined)
                if violations:
                    all_violations.append(
                        f"Lesson '{lesson.title}' block {block.page_number}/{block.block_type}: {violations}"
                    )
        assert not all_violations, (
            f"Developer leakage found in {len(all_violations)} blocks:\n" +
            "\n".join(all_violations[:10])
        )

    def test_no_empty_content(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        empty_blocks = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for block in blocks:
                content_text = text_of_content(block.content).strip()
                if len(content_text) < 20:
                    empty_blocks.append(
                        f"Lesson '{lesson.title}' page {block.page_number}/{block.block_type}: "
                        f"content too short ({len(content_text)} chars)"
                    )
        assert not empty_blocks, f"Short/empty content in blocks:\n" + "\n".join(empty_blocks)

    def test_key_statistics_formulas_present(self):
        """Verify essential formulas appear across Statistics II lessons."""
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        all_text = " ".join(text_of_content(b.content) for b in LessonBlock.objects.filter(lesson__in=lessons))
        
        assert "A +" in all_text, "Assumed mean formula not found"
        assert "IQR" in all_text or "Interquartile Range" in all_text, "IQR concept not found"
        assert "s_t^2" in all_text or "s_x" in all_text or "Standard Deviation" in all_text, "Standard deviation not found"


class TestIdempotency:

    def test_rerun_does_not_duplicate_hierarchy(self):
        from curriculum.ingest_form4_math_topic2_statistics import ingest_form4_math_topic2
        ingest_form4_math_topic2()

        t = get_topic()
        assert t is not None

        unit_count = LearningUnit.objects.filter(topic=t).count()
        assert unit_count == 4, f"After re-run: expected 4 units, got {unit_count}"

        units = LearningUnit.objects.filter(topic=t)
        lesson_count = Lesson.objects.filter(learning_unit__in=units).count()
        assert lesson_count == 4, f"After re-run: expected 4 lessons, got {lesson_count}"

    def test_rerun_clears_and_recreates_blocks(self):
        from curriculum.ingest_form4_math_topic2_statistics import ingest_form4_math_topic2
        t = get_topic()
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        count_before = LessonBlock.objects.filter(lesson__in=lessons).count()

        ingest_form4_math_topic2()

        count_after = LessonBlock.objects.filter(lesson__in=lessons).count()
        assert count_before == count_after, (
            f"Block count changed after re-run: {count_before} → {count_after}."
        )


if __name__ == "__main__":
    print("=" * 80)
    print("Form 4 Mathematics Topic 2 — Validation Test Suite")
    print("=" * 80)

    test_classes = [
        TestHierarchy,
        TestLessonPublishStatus,
        TestBlockCounts,
        TestBlockOrdering,
        TestContentQuality,
        TestIdempotency,
    ]

    passed = 0
    failed = 0

    for cls in test_classes:
        instance = cls()
        methods = [m for m in dir(instance) if m.startswith("test_")]
        for method_name in methods:
            method = getattr(instance, method_name)
            try:
                method()
                print(f"  ✓ {cls.__name__}.{method_name}")
                passed += 1
            except AssertionError as e:
                print(f"  ✗ {cls.__name__}.{method_name}")
                print(f"    {e}")
                failed += 1
            except Exception as e:
                print(f"  ✗ {cls.__name__}.{method_name} [ERROR]")
                print(f"    {type(e).__name__}: {e}")
                failed += 1

    print("\n" + "=" * 80)
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("ALL TESTS PASSED ✓")
    else:
        print(f"{failed} TESTS FAILED ✗")
    print("=" * 80)
    sys.exit(0 if failed == 0 else 1)
