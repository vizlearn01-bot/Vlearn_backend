"""
VLearn CBC Grade 10 History — Topic 6: National Integration
Comprehensive Verification and Unit Test Suite
"""

import os
import sys
import unittest
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10HistoryTopic6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name="CBC").first()
        assert cls.curriculum is not None, "Curriculum 'CBC' must exist."

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        assert cls.grade is not None, "Grade 10 must exist in CBC."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="History").first()
        assert cls.subject is not None, "Subject 'History' must exist in Grade 10 CBC."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=6).first()
        assert cls.topic is not None, "Topic 6 must exist in History Grade 10."

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_topic_hierarchy_metadata(self):
        """Verify Topic order, naming, and description."""
        self.assertEqual(self.topic.order, 6)
        self.assertIn("National Integration", self.topic.name)
        self.assertTrue(len(self.topic.description) > 20)

    def test_02_learning_units(self):
        """Verify all 4 learning units exist with correct titles and orders."""
        self.assertEqual(len(self.units), 4, f"Expected 4 units, found {len(self.units)}")

        expected_units = [
            (1, "Meaning and Dimensions of National Integration"),
            (2, "Barriers to National Integration"),
            (3, "Strategies and Institutions for Integration"),
            (4, "Citizenship Integration Project")
        ]

        for unit, (expected_order, expected_name) in zip(self.units, expected_units):
            self.assertEqual(unit.order, expected_order)
            self.assertEqual(unit.name, expected_name)

    def test_03_lessons_published_and_metadata(self):
        """Verify all 4 lessons are published, versioned, and have valid metadata."""
        self.assertEqual(len(self.lessons), 4, f"Expected 4 lessons, found {len(self.lessons)}")

        for idx, lesson in enumerate(self.lessons, start=1):
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertIsNotNone(lesson.learning_unit)
            self.assertEqual(lesson.learning_unit.order, idx)
            self.assertIn("grade", lesson.immutable_metadata)
            self.assertEqual(lesson.immutable_metadata["grade"], "Grade 10")
            self.assertEqual(lesson.immutable_metadata["subject"], "History")
            self.assertEqual(lesson.immutable_metadata["topic_order"], 6)

    def test_04_pages_and_cards_structure(self):
        """Verify each of the 4 lessons has exactly 7 distinct pages/cards (28 total)."""
        total_pages = 0
        for unit in self.units:
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, list(range(1, 8)), f"Lesson '{lesson.title}' must have 7 pages (1-7).")
            total_pages += len(page_numbers)

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

        self.assertEqual(total_pages, 28, "Total pages across topic 6 must be 28.")

    def test_05_visual_hooks_and_wikimedia_images(self):
        """Verify all 4 lessons have Page 1 photographic/vector visual hooks with Wikimedia URLs."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("url")
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 visual hook missing image URL!")
            self.assertIn("wikimedia.org", img_url, f"Lesson {u_order} URL not Wikimedia: {img_url}")

            # Check attached asset
            asset = LessonAsset.objects.filter(lesson=lesson, asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached image LessonAsset!")
            self.assertIn("wikimedia.org", asset.url)

    def test_06_custom_vector_svgs(self):
        """Verify all 4 lessons contain valid, responsive vector SVGs attached as LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=5,
                block_type="suggested_diagram"
            ).first()

            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing Card 5 suggested_diagram block!")
            content = diagram_block.content or {}
            svg_text = content.get("svg_content", "")
            self.assertTrue("<svg" in svg_text and "</svg>" in svg_text, f"Lesson {u_order} SVG malformed!")
            self.assertIn("viewBox", svg_text, f"Lesson {u_order} SVG missing viewBox!")

            # Check attached asset
            asset = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached diagram LessonAsset!")
            self.assertIn("<svg", asset.metadata.get("svg_content", ""))

    def test_07_youtube_video_assets(self):
        """Verify all 4 lessons have educational YouTube video assets attached."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=6,
                block_type="suggested_video"
            ).first()

            self.assertIsNotNone(video_block, f"Lesson {u_order} missing Card 6 suggested_video block!")
            content = video_block.content or {}
            yt_id = content.get("youtube_id")
            self.assertTrue(yt_id and len(yt_id) >= 11, f"Lesson {u_order} invalid YouTube ID: {yt_id}")

            video_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube").first()
            self.assertIsNotNone(video_asset, f"Lesson {u_order} missing attached YouTube LessonAsset!")
            self.assertIn(yt_id, video_asset.url)

    def test_08_assessment_mcqs_and_misconceptions(self):
        """Verify all lessons have Page 7 assessment quizzes with at least 3 MCQs and a misconception."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            quiz_blocks = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=7,
                block_type="knowledge_check"
            )
            self.assertGreaterEqual(quiz_blocks.count(), 3, f"Lesson {u_order} has fewer than 3 MCQs!")

            for qb in quiz_blocks:
                content = qb.content or {}
                self.assertIn("question", content)
                self.assertIn("options", content)
                self.assertEqual(len(content["options"]), 4, "Must have exactly 4 options A, B, C, D")
                self.assertIn("correct_answer", content)
                self.assertIn(content["correct_answer"], ["A", "B", "C", "D"])
                self.assertIn("explanation", content)
                self.assertGreater(len(content["explanation"]), 20)

            misc_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=7,
                block_type="common_misconception"
            ).first()
            self.assertIsNotNone(misc_block, f"Lesson {u_order} missing Card 7 common_misconception block!")
            content = misc_block.content or {}
            self.assertIn("misconception", content)
            self.assertIn("correction", content)

    def test_09_pedagogical_components_coverage(self):
        """Verify presence of comparison tables, step processes, and mini activities across lessons."""
        tables = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="comparison_table")
        self.assertGreaterEqual(tables.count(), 4, "Expected at least 4 comparison tables across topic 6.")

        processes = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="step_process")
        self.assertGreaterEqual(processes.count(), 4, "Expected at least 4 step processes across topic 6.")

        activities = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="mini_activity")
        self.assertGreaterEqual(activities.count(), 4, "Expected at least 4 mini activities across topic 6.")

    def test_10_clean_content_no_brackets_or_visual_tags(self):
        """Verify no lingering citation brackets [17] or [VISUAL: ...] tags exist in any text content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for b in blocks:
            text_str = str(b.content) + " " + str(b.title)
            self.assertNotRegex(text_str, r'\[VISUAL:', f"Block {b.id} contains uncleaned [VISUAL:] tag")
            self.assertNotRegex(text_str, r'\[\d+\]', f"Block {b.id} contains uncleaned bracket citation like [17]")

if __name__ == "__main__":
    unittest.main()
