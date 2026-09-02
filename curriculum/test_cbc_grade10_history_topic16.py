"""
VLearn CBC Grade 10 History — Topic 16: Fourth-Generation Technologies and Historical Information
Comprehensive Verification and Unit Test Suite
"""

import os
import sys
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.ingest_cbc_grade10_history_topic16 import ingest_grade10_history_topic16


class TestCBCGrade10HistoryTopic16(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ingest_grade10_history_topic16(replace=True)

        cls.curriculum = Curriculum.objects.filter(name="CBC").first()
        assert cls.curriculum is not None, "Curriculum 'CBC' must exist."

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        assert cls.grade is not None, "Grade 10 must exist in CBC."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="History").first()
        assert cls.subject is not None, "Subject 'History' must exist in Grade 10 CBC."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=16).first()
        assert cls.topic is not None, "Topic 16 must exist in History Grade 10."

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_topic_hierarchy_metadata(self):
        """Verify Topic order, naming, and description."""
        self.assertEqual(self.topic.order, 16)
        self.assertIn("Fourth-Generation Technologies", self.topic.name)
        self.assertTrue(len(self.topic.description) > 20)

    def test_02_learning_units(self):
        """Verify all 3 learning units exist with correct titles and orders."""
        self.assertEqual(len(self.units), 3, f"Expected 3 units, found {len(self.units)}")
        expected_units = [
            (1, "ICT and Fourth-Generation Change"),
            (2, "Opportunities, Risks, and Sustainability"),
            (3, "Technology and Historical Information")
        ]
        for idx, (expected_order, expected_name) in enumerate(expected_units):
            unit = self.units[idx]
            self.assertEqual(unit.order, expected_order)
            self.assertIn(expected_name, unit.name)

    def test_03_lessons_published_and_metadata(self):
        """Verify all 3 lessons are published with version=1 and valid metadata."""
        self.assertEqual(len(self.lessons), 3)
        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertIsNotNone(lesson.immutable_metadata)
            self.assertEqual(lesson.immutable_metadata["grade"], "Grade 10")
            self.assertEqual(lesson.immutable_metadata["subject"], "History")

    def test_04_pages_and_cards_structure(self):
        """Verify each lesson has 5 distinct pages/cards."""
        total_pages = 0
        for unit in self.units:
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(len(page_numbers), 5)
            total_pages += len(page_numbers)
        self.assertEqual(total_pages, 15)

    def test_05_visualizations_and_svg_assets(self):
        """Verify all required SVG vector diagrams are attached with valid markup."""
        lessons = Lesson.objects.filter(topic=self.topic)
        assets = LessonAsset.objects.filter(lesson__in=lessons)
        svg_assets = [a for a in assets if a.asset_type == "diagram" or (a.metadata and "svg_content" in a.metadata)]
        self.assertGreaterEqual(len(svg_assets), 2)
        for sa in svg_assets:
            svg_content = sa.metadata.get("svg_content", "")
            self.assertIn("<svg", svg_content)
            self.assertIn("</svg>", svg_content)

    def test_06_image_and_video_assets(self):
        """Verify Wikimedia images and educational YouTube videos."""
        lessons = Lesson.objects.filter(topic=self.topic)
        assets = LessonAsset.objects.filter(lesson__in=lessons)
        images = [a for a in assets if a.asset_type == "image"]
        videos = [a for a in assets if a.asset_type == "youtube"]
        self.assertEqual(len(images), 3)
        self.assertEqual(len(videos), 3)

    def test_07_knowledge_check_mcqs(self):
        """Verify formative MCQs have 4 options and detailed explanations."""
        lessons = Lesson.objects.filter(topic=self.topic)
        blocks = LessonBlock.objects.filter(lesson__in=lessons, block_type="knowledge_check")
        self.assertGreaterEqual(blocks.count(), 4)
        for b in blocks:
            content = b.content or {}
            self.assertIn("question", content)
            self.assertIn("options", content)
            self.assertEqual(len(content["options"]), 4)
            self.assertIn("correct_answer", content)
            self.assertIn(content["correct_answer"], ["A", "B", "C", "D"])
            self.assertIn("explanation", content)

    def test_08_text_sanitization(self):
        """Verify zero bracket citations or internal visual tags exist in block content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for b in blocks:
            text_str = str(b.content or {})
            self.assertNotRegex(text_str, r'\[VISUAL:', f"Internal visual tag leak in block {b.id}")
            self.assertNotRegex(text_str, r'\[\d+\]', f"Bracket citation leak in block {b.id}")


if __name__ == "__main__":
    unittest.main()
