"""
VLearn Form 4 Mathematics — Topic 1: Matrix and Transformation
Validation Test

Run with pytest from Vlearn_backend/:
  python -m pytest curriculum/test_form4_math_topic1_ingestion.py -v

Or run directly:
  python curriculum/test_form4_math_topic1_ingestion.py
"""

import os
import sys
import json
import re
import django
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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

LEGITIMATE_MATH_TERMS = [
    "transformation matrix", "solution", "Step 1", "Step 2", "Step 3", "Step 4",
    "matrix", "determinant", "isometric", "shear", "stretch", "composite",
    "rotation", "reflection", "column vector", "identity"
]

REQUIRED_STANDARD_MATRICES = {
    "reflection in x-axis": r"\\begin\{pmatrix\}\s*1\s*&\s*0\s*\\\\\s*0\s*&\s*-1\s*\\end\{pmatrix\}",
    "reflection in y-axis": r"\\begin\{pmatrix\}\s*-1\s*&\s*0\s*\\\\\s*0\s*&\s*1\s*\\end\{pmatrix\}",
    "90 degree rotation":   r"\\begin\{pmatrix\}\s*0\s*&\s*[-]?1\s*\\\\\s*[-]?1\s*&\s*0\s*\\end\{pmatrix\}",
    "determinant formula":  r"ad\s*-\s*bc",
}


def get_topic():
    return Topic.objects.filter(
        subject__name="Mathematics",
        subject__grade__name="Form 4",
        name__icontains="Matrix and Transformation"
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

    # Count display math ($$)
    display_count = len(re.findall(r"\$\$", text))
    if display_count % 2 != 0:
        issues.append(f"Odd number of $$ delimiters ({display_count})")

    # Count inline math ($) excluding $$
    inline_text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    single_dollars = re.findall(r"(?<!\$)\$(?!\$)", inline_text)
    if len(single_dollars) % 2 != 0:
        issues.append(f"Odd number of $ delimiters ({len(single_dollars)} after removing $$)")

    # Check \begin{...} and \end{...} are paired
    begins = re.findall(r"\\begin\{(\w+)\}", text)
    ends = re.findall(r"\\end\{(\w+)\}", text)
    if sorted(begins) != sorted(ends):
        issues.append(f"\\begin/\\end mismatch: begins={begins}, ends={ends}")

    return issues


def check_pmatrix_structure(text):
    """Verify pmatrix environments have row separators where needed.
    
    A single-row matrix like $\\begin{pmatrix} a & b \\end{pmatrix}$ is VALID
    and does NOT need a row separator.
    
    Only flag matrices that have & (columns) AND a newline or are clearly
    intended to be multi-row (have entries on two separate lines).
    
    In the stored Python string:
    - LaTeX \\ (row separator) appears as \\\\ (two backslashes)
    - & (column separator) appears as & (ampersand)
    """
    issues = []
    pmatrix_blocks = re.findall(r"\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}", text, re.DOTALL)
    for i, block in enumerate(pmatrix_blocks, 1):
        entries = block.strip()
        # Only flag if there are MULTIPLE ROWS indicated by a newline in the content.
        # A single-row matrix (like \begin{pmatrix} a & b \end{pmatrix}) is valid.
        has_columns = "&" in entries
        # Multi-row indicator: the block contains a newline (i.e., the source was
        # written with entries on separate lines) OR has more than one & per logical row.
        # We conservatively: only flag if it looks like a 2x2 matrix with 4 distinct entries
        # but no row separator. Specifically: &-count >= 2 suggests at least 2 columns × 2 rows.
        ampersand_count = entries.count("&")
        has_row_sep = "\\\\" in entries  # two literal backslashes = LaTeX row separator
        
        # Flag only if: multiple ampersands (suggesting 2+ rows) AND no row separator
        if ampersand_count >= 2 and not has_row_sep:
            issues.append(
                f"pmatrix block {i} may be a 2-row matrix with {ampersand_count} "
                f"column-separators (&) but no row separator (\\\\): '{entries[:60]}'"
            )
    return issues


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestHierarchy:

    def test_curriculum_exists(self):
        c = Curriculum.objects.filter(name="844").first()
        assert c is not None, "Curriculum '844' not found"

    def test_grade_exists(self):
        g = Grade.objects.filter(name="Form 4", curriculum__name="844").first()
        assert g is not None, "Grade 'Form 4' not found"
        # Note: Form 4 has level=1 in the existing DB — this is the pre-existing convention.
        # We do not override the existing grade level on ingestion.

    def test_subject_exists(self):
        s = Subject.objects.filter(name="Mathematics", grade__name="Form 4").first()
        assert s is not None, "Subject 'Mathematics' under Form 4 not found"

    def test_topic_exists(self):
        t = get_topic()
        assert t is not None, "Topic 'Matrix and Transformation' not found"

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
            pages = LessonBlock.objects.filter(
                lesson=lesson
            ).values_list("page_number", flat=True).distinct().order_by("page_number")
            pages = list(pages)
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

    def test_page_titles_are_student_facing(self):
        """Page titles must not expose internal labels."""
        internal_label_patterns = [
            r"component_type", r"block_type", r"ai_instruction",
            r"PLACEHOLDER", r"TODO", r"page_\d+_title"
        ]
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        violations = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for block in blocks:
                title = block.page_title or ""
                for pattern in internal_label_patterns:
                    if re.search(pattern, title, re.IGNORECASE):
                        violations.append(
                            f"Lesson '{lesson.title}' page {block.page_number}: "
                            f"title '{title}' matches internal pattern '{pattern}'"
                        )
        assert not violations, "Internal labels in page titles:\n" + "\n".join(violations)


class TestLatexIntegrity:

    def test_latex_delimiters_balanced(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        latex_errors = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for block in blocks:
                text = text_of_content(block.content)
                issues = check_latex_balance(text)
                if issues:
                    latex_errors.append(
                        f"Lesson '{lesson.title}' page {block.page_number}/{block.block_type}: {issues}"
                    )
        assert not latex_errors, (
            f"LaTeX delimiter issues in {len(latex_errors)} blocks:\n" +
            "\n".join(latex_errors[:10])
        )

    def test_pmatrix_has_row_separators(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        pmatrix_errors = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for block in blocks:
                text = text_of_content(block.content)
                issues = check_pmatrix_structure(text)
                if issues:
                    pmatrix_errors.append(
                        f"Lesson '{lesson.title}' page {block.page_number}: {issues}"
                    )
        assert not pmatrix_errors, (
            f"pmatrix structure issues:\n" + "\n".join(pmatrix_errors[:10])
        )

    def test_determinant_formula_present(self):
        """The determinant formula ad-bc must appear in Topic 1.4."""
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t, name__icontains="Determinant")
        lessons = Lesson.objects.filter(learning_unit__in=units)
        found = False
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for block in blocks:
                text = text_of_content(block.content)
                if re.search(r"ad\s*-\s*bc", text):
                    found = True
                    break
        assert found, "Determinant formula 'ad - bc' not found in any determinant lesson block"


class TestWorkedExampleIntegrity:

    def test_worked_examples_have_problem_and_steps(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        failures = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson, block_type="worked_example")
            for block in blocks:
                content = block.content
                if isinstance(content, dict):
                    has_problem = "problem" in content and content["problem"]
                    has_steps = "steps" in content and isinstance(content["steps"], list) and len(content["steps"]) >= 2
                else:
                    has_problem = has_steps = bool(text_of_content(content).strip())
                if not has_problem:
                    failures.append(
                        f"Lesson '{lesson.title}' page {block.page_number}: worked_example missing 'problem'"
                    )
                if not has_steps:
                    failures.append(
                        f"Lesson '{lesson.title}' page {block.page_number}: worked_example missing 'steps' (or fewer than 2)"
                    )
        assert not failures, "\n".join(failures)

    def test_mcq_blocks_have_4_options_and_answer(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        failures = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(
                lesson=lesson,
                block_type__in=["knowledge_check", "multiple_choice"]
            )
            for block in blocks:
                content = block.content
                if isinstance(content, dict):
                    check_type = content.get("check_type", "")
                    if check_type == "multiple_choice" or "options" in content:
                        options = content.get("options", [])
                        answer = content.get("answer", "")
                        if len(options) < 4:
                            failures.append(
                                f"Lesson '{lesson.title}' page {block.page_number}: MCQ has {len(options)} options, expected 4"
                            )
                        if not answer:
                            failures.append(
                                f"Lesson '{lesson.title}' page {block.page_number}: MCQ missing 'answer'"
                            )
                        if answer not in ["A", "B", "C", "D"]:
                            failures.append(
                                f"Lesson '{lesson.title}' page {block.page_number}: MCQ answer '{answer}' not in A-D"
                            )
        assert not failures, "\n".join(failures)

    def test_short_answer_blocks_have_hint_and_answer(self):
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        failures = []
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson, component_type="short_answer")
            for block in blocks:
                content = block.content
                if isinstance(content, dict):
                    if not content.get("hint"):
                        failures.append(
                            f"Lesson '{lesson.title}' page {block.page_number}: short_answer missing 'hint'"
                        )
                    if not content.get("answer"):
                        failures.append(
                            f"Lesson '{lesson.title}' page {block.page_number}: short_answer missing 'answer'"
                        )
        assert not failures, "\n".join(failures)


class TestSimulationPlaceholder:

    def test_simulation_placeholder_exists(self):
        """The math_matrix_transformation simulation placeholder should exist in Topic 1.3."""
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t, name__icontains="Successive")
        lessons = Lesson.objects.filter(learning_unit__in=units)
        found = False
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(
                lesson=lesson,
                block_type__in=["suggested_simulation", "simulation_placeholder"]
            )
            for block in blocks:
                content_text = text_of_content(block.content)
                if "math_matrix_transformation" in content_text:
                    found = True
                    break
        assert found, (
            "No suggested_simulation with archetype 'math_matrix_transformation' found in "
            "Lesson 1.3 (Successive Transformations)"
        )

    def test_simulation_asset_created(self):
        """A LessonAsset of type 'simulation' should exist for the lesson with the placeholder."""
        t = get_topic()
        assert t is not None
        units = LearningUnit.objects.filter(topic=t, name__icontains="Successive")
        lessons = Lesson.objects.filter(learning_unit__in=units)
        found = False
        for lesson in lessons:
            if LessonAsset.objects.filter(lesson=lesson, asset_type="simulation").exists():
                found = True
                break
        assert found, "No LessonAsset of type 'simulation' found for Module 1.3"


class TestIdempotency:

    def test_rerun_does_not_duplicate_hierarchy(self):
        """Running the ingestion a second time should not create duplicate topics/units/lessons."""
        # Import and re-run ingestion
        from curriculum.ingest_form4_math_topic1_matrices import ingest_form4_math_topic1
        ingest_form4_math_topic1()

        t = get_topic()
        assert t is not None

        # Should still be exactly 4 units and 4 lessons
        unit_count = LearningUnit.objects.filter(topic=t).count()
        assert unit_count == 4, f"After re-run: expected 4 units, got {unit_count}"

        units = LearningUnit.objects.filter(topic=t)
        lesson_count = Lesson.objects.filter(learning_unit__in=units).count()
        assert lesson_count == 4, f"After re-run: expected 4 lessons, got {lesson_count}"

    def test_rerun_clears_and_recreates_blocks(self):
        """After a second run, block count should be identical, not doubled."""
        from curriculum.ingest_form4_math_topic1_matrices import ingest_form4_math_topic1
        t = get_topic()
        units = LearningUnit.objects.filter(topic=t)
        lessons = Lesson.objects.filter(learning_unit__in=units)
        count_before = LessonBlock.objects.filter(lesson__in=lessons).count()

        ingest_form4_math_topic1()

        count_after = LessonBlock.objects.filter(lesson__in=lessons).count()
        assert count_before == count_after, (
            f"Block count changed after re-run: {count_before} → {count_after}. "
            "Idempotency broken — blocks may be duplicated."
        )


# ---------------------------------------------------------------------------
# Direct-run mode (no pytest required)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("Form 4 Mathematics Topic 1 — Validation Test Suite")
    print("=" * 80)

    test_classes = [
        TestHierarchy,
        TestLessonPublishStatus,
        TestBlockCounts,
        TestBlockOrdering,
        TestContentQuality,
        TestLatexIntegrity,
        TestWorkedExampleIntegrity,
        TestSimulationPlaceholder,
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
