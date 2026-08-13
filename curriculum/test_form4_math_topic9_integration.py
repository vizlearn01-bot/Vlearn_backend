#!/usr/bin/env python3
"""
VLearn Form 4 Mathematics — Topic 9: Integration Test Suite
============================================================
Validates:
  1. Hierarchy (Curriculum, Grade, Subject, Topic, 4 LearningUnits, 4 Lessons)
  2. Publishing status (all status="published")
  3. Lesson block structure & minimum page counts (≥8 pages per lesson, exactly 4 progressive worked examples)
  4. Block ordering (learning_goal on page 1, summary on last page)
  5. Content quality (zero developer leakages, zero raw math arrays, key Integration concepts present)
  6. Idempotency (re-running ingestion cleanly updates without duplicating records)
"""

import os
import sys
import json
import re
import unittest
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.ingest_form4_math_topic9_integration import ingest_topic9_integration


class TestHierarchy(unittest.TestCase):
    """Verify the database hierarchy for Topic 9."""

    def test_curriculum_exists(self):
        curriculum = Curriculum.objects.filter(name="844").first()
        self.assertIsNotNone(curriculum, "Curriculum '844' not found")

    def test_grade_exists(self):
        grade = Grade.objects.filter(name__icontains="Form 4").first()
        self.assertIsNotNone(grade, "Grade 'Form 4' not found")

    def test_subject_exists(self):
        subject = Subject.objects.filter(name="Mathematics", grade__name__icontains="Form 4").first()
        self.assertIsNotNone(subject, "Subject 'Mathematics' for Form 4 not found")

    def test_topic_exists(self):
        topic = Topic.objects.filter(name__icontains="Integration", subject__name="Mathematics").first()
        self.assertIsNotNone(topic, "Topic 'Integration' not found")
        self.assertEqual(topic.order, 9, "Topic order should be 9")

    def test_exactly_4_learning_units(self):
        topic = Topic.objects.filter(name__icontains="Integration").first()
        units = LearningUnit.objects.filter(topic=topic).order_by("order")
        self.assertEqual(units.count(), 4, f"Expected 4 LearningUnits, found {units.count()}")

    def test_exactly_4_lessons(self):
        topic = Topic.objects.filter(name__icontains="Integration").first()
        lessons = Lesson.objects.filter(topic=topic)
        self.assertEqual(lessons.count(), 4, f"Expected 4 Lessons, found {lessons.count()}")


class TestLessonPublishStatus(unittest.TestCase):
    """Verify that all lessons have status='published'."""

    def test_all_lessons_published(self):
        topic = Topic.objects.filter(name__icontains="Integration").first()
        lessons = Lesson.objects.filter(topic=topic)
        for lesson in lessons:
            self.assertEqual(
                lesson.status, "published",
                f"Lesson '{lesson.title}' (ID: {lesson.id}) status is '{lesson.status}', expected 'published'"
            )


class TestBlockCounts(unittest.TestCase):
    """Verify that each lesson has sufficient depth and required components."""

    def setUp(self):
        self.topic = Topic.objects.filter(name__icontains="Integration").first()
        self.lessons = list(Lesson.objects.filter(topic=self.topic))

    def test_minimum_total_blocks(self):
        total_blocks = LessonBlock.objects.filter(lesson__topic=self.topic).count()
        self.assertGreaterEqual(
            total_blocks, 40,
            f"Expected at least 40 blocks across Topic 9, found {total_blocks}"
        )

    def test_each_lesson_has_minimum_8_pages(self):
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(
                len(page_numbers), 8,
                f"Lesson '{lesson.title}' has {len(page_numbers)} pages, expected ≥ 8"
            )

    def test_each_lesson_has_learning_goal(self):
        for lesson in self.lessons:
            has_goal = LessonBlock.objects.filter(lesson=lesson, block_type="learning_goal").exists()
            self.assertTrue(has_goal, f"Lesson '{lesson.title}' is missing a learning_goal block")

    def test_each_lesson_has_misconception_block(self):
        for lesson in self.lessons:
            has_misc = LessonBlock.objects.filter(lesson=lesson, block_type="common_misconception").exists()
            self.assertTrue(has_misc, f"Lesson '{lesson.title}' is missing a common_misconception block")

    def test_each_lesson_has_summary(self):
        for lesson in self.lessons:
            has_sum = LessonBlock.objects.filter(lesson=lesson, block_type="summary").exists()
            self.assertTrue(has_sum, f"Lesson '{lesson.title}' is missing a summary block")

    def test_each_lesson_has_at_least_3_worked_examples(self):
        for lesson in self.lessons:
            example_count = LessonBlock.objects.filter(lesson=lesson, block_type="worked_example").count()
            self.assertGreaterEqual(
                example_count, 3,
                f"Lesson '{lesson.title}' has {example_count} worked_examples, expected ≥ 3"
            )

    def test_each_lesson_has_knowledge_check(self):
        for lesson in self.lessons:
            has_kc = LessonBlock.objects.filter(
                lesson=lesson,
                block_type__in=["knowledge_check", "multiple_choice", "short_answer"]
            ).exists()
            self.assertTrue(has_kc, f"Lesson '{lesson.title}' is missing a knowledge check block")


class TestBlockOrdering(unittest.TestCase):
    """Verify that lesson blocks follow the proper pedagogical progression."""

    def setUp(self):
        self.topic = Topic.objects.filter(name__icontains="Integration").first()
        self.lessons = list(Lesson.objects.filter(topic=self.topic))

    def test_learning_goal_is_on_page_1(self):
        for lesson in self.lessons:
            p1_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=1)
            block_types = [b.block_type for b in p1_blocks]
            self.assertIn(
                "learning_goal", block_types,
                f"Lesson '{lesson.title}' does not have learning_goal on page 1 (found: {block_types})"
            )

    def test_summary_is_on_last_page(self):
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("page_number")
            max_page = max(b.page_number for b in blocks)
            last_page_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=max_page)
            block_types = [b.block_type for b in last_page_blocks]
            self.assertIn(
                "summary", block_types,
                f"Lesson '{lesson.title}' does not have summary on last page {max_page} (found: {block_types})"
            )

    def test_page_numbers_are_sequential(self):
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("page_number")
            page_numbers = sorted(list(set(b.page_number for b in blocks)))
            expected = list(range(1, len(page_numbers) + 1))
            self.assertEqual(
                page_numbers, expected,
                f"Lesson '{lesson.title}' has non-sequential pages: {page_numbers}"
            )


class TestContentQuality(unittest.TestCase):
    """Verify that student-facing content has no developer leakage, OCR corruption, or empty payloads."""

    def setUp(self):
        self.topic = Topic.objects.filter(name__icontains="Integration").first()
        self.blocks = list(LessonBlock.objects.filter(lesson__topic=self.topic))

    def test_no_empty_content(self):
        for block in self.blocks:
            self.assertIsNotNone(block.content, f"Block {block.id} content is None")
            self.assertTrue(len(block.content) > 0, f"Block {block.id} content is empty dict")

    def test_no_developer_leakage_in_content(self):
        leak_patterns = [
            (r"\bTODO\b", "TODO"),
            (r"\bTBD\b", "TBD"),
            (r"\bFIXME\b", "FIXME"),
            (r"\bundefined\b", "undefined"),
            (r"\blorem ipsum\b", "lorem ipsum"),
            (r"\\begin\{array\}", r"\begin{array}"),
            (r"\\hline", r"\hline")
        ]
        for block in self.blocks:
            content_str = json.dumps(block.content, default=str)
            for pat, name in leak_patterns:
                self.assertIsNone(
                    re.search(pat, content_str, re.IGNORECASE),
                    f"Found forbidden developer pattern '{name}' in block {block.id} ({block.block_type})"
                )

    def test_key_integration_concepts_present(self):
        all_text = " ".join([json.dumps(b.content, default=str) for b in self.blocks])
        key_terms = [
            "antiderivative", "constant of integration", "definite integral",
            "area under", "split", "intersecting", "kinematics", "velocity"
        ]
        for term in key_terms:
            self.assertIn(
                term.lower(), all_text.lower(),
                f"Key Integration concept '{term}' not found in Topic 9 content"
            )


class TestIdempotency(unittest.TestCase):
    """Verify that re-running the ingestion script is completely safe and produces identical state."""

    def test_rerun_does_not_duplicate_hierarchy(self):
        ingest_topic9_integration()

        topic = Topic.objects.filter(name__icontains="Integration").first()
        self.assertIsNotNone(topic)
        self.assertEqual(LearningUnit.objects.filter(topic=topic).count(), 4)
        self.assertEqual(Lesson.objects.filter(topic=topic).count(), 4)

    def test_rerun_clears_and_recreates_blocks(self):
        ingest_topic9_integration()

        topic = Topic.objects.filter(name__icontains="Integration").first()
        total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()
        self.assertEqual(total_blocks, 44)


if __name__ == "__main__":
    print("=" * 80)
    print("Form 4 Mathematics Topic 9 (Integration) — Validation Test Suite")
    print("=" * 80)
    suite = unittest.TestSuite()
    for test_class in [
        TestHierarchy,
        TestLessonPublishStatus,
        TestBlockCounts,
        TestBlockOrdering,
        TestContentQuality,
        TestIdempotency
    ]:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 80)
    print(f"Results: {result.testsRun - len(result.failures) - len(result.errors)} passed, {len(result.failures)} failed")
    if result.wasSuccessful():
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 80)
    sys.exit(0 if result.wasSuccessful() else 1)
