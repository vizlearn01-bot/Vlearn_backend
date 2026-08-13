"""
Validation Test Suite for Form 4 Mathematics Topic 3: Three-Dimensional Geometry

Validates:
  - Complete curriculum hierarchy (Curriculum, Grade, Subject, Topic, Units, Lessons)
  - All lessons published (status='published')
  - Mathematics pedagogical progression (≥8 pages, ≥3 worked examples, learning goal on p1, summary on last page)
  - Required block types present across all lessons
  - Sequential page ordering without gaps
  - Content quality (formula integrity, no developer leakage, humanized explanations)
  - Ingestion idempotency (re-running does not duplicate hierarchy or corrupt blocks)

Run from Vlearn_backend/:
  source venv/bin/activate
  python curriculum/test_form4_math_topic3_geometry.py
"""

import os
import sys
import json
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
from curriculum.ingest_form4_math_topic3_geometry import ingest_topic3_geometry


class TestHierarchy(unittest.TestCase):
    """Test that the full curriculum hierarchy for Topic 3 exists."""

    def test_curriculum_exists(self):
        self.assertTrue(Curriculum.objects.filter(name="844").exists())

    def test_grade_exists(self):
        self.assertTrue(Grade.objects.filter(name="Form 4").exists())

    def test_subject_exists(self):
        grade = Grade.objects.get(name="Form 4")
        self.assertTrue(Subject.objects.filter(name="Mathematics", grade=grade).exists())

    def test_topic_exists(self):
        subject = Subject.objects.get(name="Mathematics", grade__name="Form 4")
        self.assertTrue(Topic.objects.filter(name="Topic 3: Three Dimensional Geometry", subject=subject).exists())

    def test_exactly_4_learning_units(self):
        topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        units = LearningUnit.objects.filter(topic=topic)
        self.assertEqual(units.count(), 4, f"Expected 4 LearningUnits, got {units.count()}")

    def test_exactly_4_lessons(self):
        topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        lessons = Lesson.objects.filter(topic=topic)
        self.assertEqual(lessons.count(), 4, f"Expected 4 Lessons, got {lessons.count()}")


class TestLessonPublishStatus(unittest.TestCase):
    """Test that all Topic 3 lessons have status='published'."""

    def test_all_lessons_published(self):
        topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        lessons = Lesson.objects.filter(topic=topic)
        for lesson in lessons:
            self.assertEqual(
                lesson.status, "published",
                f"Lesson '{lesson.title}' has status '{lesson.status}', expected 'published'"
            )


class TestBlockCounts(unittest.TestCase):
    """Test block counts and presence of required pedagogical components."""

    def setUp(self):
        self.topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        self.lessons = Lesson.objects.filter(topic=self.topic)

    def test_minimum_total_blocks(self):
        total_blocks = LessonBlock.objects.filter(lesson__topic=self.topic).count()
        self.assertGreaterEqual(
            total_blocks, 40,
            f"Expected at least 40 total blocks across 4 lessons, got {total_blocks}"
        )

    def test_each_lesson_has_minimum_8_pages(self):
        for lesson in self.lessons:
            block_count = LessonBlock.objects.filter(lesson=lesson).count()
            self.assertGreaterEqual(
                block_count, 8,
                f"Lesson '{lesson.title}' has {block_count} blocks, expected at least 8"
            )

    def test_each_lesson_has_learning_goal(self):
        for lesson in self.lessons:
            has_goal = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="learning_goal"
            ).exists()
            self.assertTrue(has_goal, f"Lesson '{lesson.title}' missing learning_goal block")

    def test_each_lesson_has_at_least_3_worked_examples(self):
        for lesson in self.lessons:
            example_count = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="worked_example"
            ).count()
            self.assertGreaterEqual(
                example_count, 3,
                f"Lesson '{lesson.title}' has {example_count} worked examples, expected at least 3"
            )

    def test_each_lesson_has_misconception_block(self):
        for lesson in self.lessons:
            has_misconception = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="common_misconception"
            ).exists()
            self.assertTrue(has_misconception, f"Lesson '{lesson.title}' missing common_misconception block")

    def test_each_lesson_has_knowledge_check(self):
        for lesson in self.lessons:
            has_check = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="knowledge_check"
            ).exists()
            self.assertTrue(has_check, f"Lesson '{lesson.title}' missing knowledge_check block")

    def test_each_lesson_has_summary(self):
        for lesson in self.lessons:
            has_summary = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="summary"
            ).exists()
            self.assertTrue(has_summary, f"Lesson '{lesson.title}' missing summary block")


class TestBlockOrdering(unittest.TestCase):
    """Test strict pedagogical page ordering."""

    def setUp(self):
        self.topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        self.lessons = Lesson.objects.filter(topic=self.topic)

    def test_learning_goal_is_on_page_1(self):
        for lesson in self.lessons:
            page1_block = LessonBlock.objects.filter(lesson=lesson, page_number=1).first()
            self.assertIsNotNone(page1_block, f"Lesson '{lesson.title}' has no block on page 1")
            self.assertEqual(
                page1_block.block_type, "learning_goal",
                f"Lesson '{lesson.title}' page 1 is '{page1_block.block_type}', expected 'learning_goal'"
            )

    def test_summary_is_on_last_page(self):
        for lesson in self.lessons:
            last_block = LessonBlock.objects.filter(lesson=lesson).order_by("-page_number").first()
            self.assertIsNotNone(last_block, f"Lesson '{lesson.title}' has no blocks")
            self.assertEqual(
                last_block.block_type, "summary",
                f"Lesson '{lesson.title}' last page is '{last_block.block_type}', expected 'summary'"
            )

    def test_page_numbers_are_sequential(self):
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("page_number")
            unique_pages = sorted(list(set(b.page_number for b in blocks)))
            expected = list(range(1, len(unique_pages) + 1))
            self.assertEqual(
                unique_pages, expected,
                f"Lesson '{lesson.title}' page numbers {unique_pages} not sequential"
            )


class TestContentQuality(unittest.TestCase):
    """Test content quality, formula integrity, and absence of developer leaks."""

    def setUp(self):
        self.topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        self.blocks = LessonBlock.objects.filter(lesson__topic=self.topic)

    def test_no_empty_content(self):
        for block in self.blocks:
            self.assertIsNotNone(block.content, f"Block {block.id} content is None")
            self.assertTrue(len(block.content) > 0, f"Block {block.id} content is empty dict")

    def test_no_developer_leakage_in_content(self):
        import re
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

    def test_key_geometry_concepts_present(self):
        all_text = " ".join([json.dumps(b.content, default=str) for b in self.blocks])
        key_terms = [
            "skew", "projection", "pythagoras", "space diagonal",
            "cosine rule", "dihedral", "perpendicular", "tetrahedron"
        ]
        for term in key_terms:
            self.assertIn(
                term, all_text.lower(),
                f"Key geometry term '{term}' missing from Topic 3 content"
            )


class TestIdempotency(unittest.TestCase):
    """Test that repeated execution of the ingestion script is idempotent."""

    def test_rerun_clears_and_recreates_blocks(self):
        # Re-run ingestion
        ingest_topic3_geometry()

        topic = Topic.objects.get(name="Topic 3: Three Dimensional Geometry")
        lessons = Lesson.objects.filter(topic=topic)
        self.assertEqual(lessons.count(), 4)

        for lesson in lessons:
            self.assertEqual(lesson.status, "published")
            blocks = LessonBlock.objects.filter(lesson=lesson)
            self.assertEqual(blocks.count(), 11, f"Lesson '{lesson.title}' blocks duplicated after rerun")

    def test_rerun_does_not_duplicate_hierarchy(self):
        ingest_topic3_geometry()

        topics = Topic.objects.filter(name="Topic 3: Three Dimensional Geometry")
        self.assertEqual(topics.count(), 1)

        units = LearningUnit.objects.filter(topic=topics.first())
        self.assertEqual(units.count(), 4)


def run_tests():
    """Run all validation tests with formatted console output."""
    print("=" * 80)
    print("Form 4 Mathematics Topic 3 (Three-Dimensional Geometry) — Validation Test Suite")
    print("=" * 80)

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestHierarchy))
    suite.addTests(loader.loadTestsFromTestCase(TestLessonPublishStatus))
    suite.addTests(loader.loadTestsFromTestCase(TestBlockCounts))
    suite.addTests(loader.loadTestsFromTestCase(TestBlockOrdering))
    suite.addTests(loader.loadTestsFromTestCase(TestContentQuality))
    suite.addTests(loader.loadTestsFromTestCase(TestIdempotency))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 80)
    print(f"Results: {result.testsRun - len(result.failures) - len(result.errors)} passed, {len(result.failures) + len(result.errors)} failed")
    if result.wasSuccessful():
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 80)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
