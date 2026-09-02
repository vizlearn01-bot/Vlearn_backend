"""
VLearn CBC Grade 10 History — Topic 3: The Constitution of Kenya (2010) — Public Resources
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

class TestCBCGrade10HistoryTopic3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name="CBC").first()
        assert cls.curriculum is not None, "Curriculum 'CBC' must exist."

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        assert cls.grade is not None, "Grade 10 must exist in CBC."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="History").first()
        assert cls.subject is not None, "Subject 'History' must exist in Grade 10 CBC."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=3).first()
        assert cls.topic is not None, "Topic 3 must exist in History Grade 10."

    def test_01_topic_metadata(self):
        """Verify Topic order, naming, and description."""
        self.assertEqual(self.topic.order, 3)
        self.assertIn("Constitution of Kenya (2010)", self.topic.name)
        self.assertIn("Public Resources", self.topic.name)
        self.assertTrue(len(self.topic.description) > 20)

    def test_02_learning_units(self):
        """Verify all 4 learning units exist with correct titles and orders."""
        units = list(LearningUnit.objects.filter(topic=self.topic).order_by("order"))
        self.assertEqual(len(units), 4, f"Expected 4 units, found {len(units)}")

        expected_units = [
            (1, "Public Resources and Constitutional Stewardship"),
            (2, "Challenges in Efficient Utilisation"),
            (3, "Sustainable Utilisation and Ethical Advocacy"),
            (4, "Applied Constitutional Inquiry")
        ]

        for unit, (expected_order, expected_name) in zip(units, expected_units):
            self.assertEqual(unit.order, expected_order)
            self.assertEqual(unit.name, expected_name)

    def test_03_lessons_published_and_metadata(self):
        """Verify all 4 lessons are published, versioned, and have valid metadata."""
        lessons = list(Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order"))
        self.assertEqual(len(lessons), 4, f"Expected 4 lessons, found {len(lessons)}")

        for idx, lesson in enumerate(lessons, start=1):
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertIsNotNone(lesson.learning_unit)
            self.assertEqual(lesson.learning_unit.order, idx)
            self.assertIn("grade", lesson.immutable_metadata)
            self.assertEqual(lesson.immutable_metadata["grade"], "Grade 10")
            self.assertEqual(lesson.immutable_metadata["subject"], "History")

    def test_04_pages_and_cards_structure(self):
        """Verify each of the 4 lessons has 8 distinct pages/cards (32 total)."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        total_pages = 0

        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, list(range(1, 9)), f"Lesson '{lesson.title}' must have 8 pages.")
            total_pages += len(page_numbers)

        self.assertEqual(total_pages, 32, "Total pages across topic 3 must be 32.")

    def test_05_visualizations_and_assets(self):
        """Verify all required SVG diagrams, images, and YouTube videos are attached."""
        lessons = Lesson.objects.filter(topic=self.topic)
        total_assets = LessonAsset.objects.filter(lesson__in=lessons).count()
        self.assertGreaterEqual(total_assets, 14, f"Expected at least 14 assets, found {total_assets}")

        # Lesson 1 Assets: Timeline, 3 Pillars SVG, Image, YouTube Video
        l1 = Lesson.objects.get(topic=self.topic, learning_unit__order=1)
        l1_assets = LessonAsset.objects.filter(lesson=l1)
        l1_types = [a.asset_type for a in l1_assets]
        self.assertIn("diagram", l1_types)
        self.assertIn("image", l1_types)
        self.assertIn("youtube", l1_types)
        self.assertEqual(l1_assets.filter(asset_type="diagram").count(), 2)  # Timeline + 3 Pillars

        # Lesson 2 Assets: Causal Chain SVG, Image, YouTube Video
        l2 = Lesson.objects.get(topic=self.topic, learning_unit__order=2)
        l2_assets = LessonAsset.objects.filter(lesson=l2)
        l2_types = [a.asset_type for a in l2_assets]
        self.assertIn("diagram", l2_types)
        self.assertIn("image", l2_types)
        self.assertIn("youtube", l2_types)

        # Lesson 3 Assets: Sustainability Loop SVG, Mali ya Umma Poster SVG, Image, YouTube Video
        l3 = Lesson.objects.get(topic=self.topic, learning_unit__order=3)
        l3_assets = LessonAsset.objects.filter(lesson=l3)
        l3_types = [a.asset_type for a in l3_assets]
        self.assertIn("diagram", l3_types)
        self.assertIn("image", l3_types)
        self.assertIn("youtube", l3_types)
        self.assertEqual(l3_assets.filter(asset_type="diagram").count(), 2)  # Loop + Poster

        # Lesson 4 Assets: Inquiry Framework SVG, Image, YouTube Video
        l4 = Lesson.objects.get(topic=self.topic, learning_unit__order=4)
        l4_assets = LessonAsset.objects.filter(lesson=l4)
        l4_types = [a.asset_type for a in l4_assets]
        self.assertIn("diagram", l4_types)
        self.assertIn("image", l4_types)
        self.assertIn("youtube", l4_types)

    def test_06_youtube_videos_verified(self):
        """Verify each lesson has a dedicated valid educational YouTube video."""
        for u_order in range(1, 5):
            lesson = Lesson.objects.get(topic=self.topic, learning_unit__order=u_order)
            yt_assets = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube")
            self.assertEqual(yt_assets.count(), 1, f"Lesson {u_order} must have exactly 1 YouTube asset.")
            yt = yt_assets.first()
            self.assertTrue(yt.url.startswith("https://www.youtube.com/watch?v="))
            self.assertIn("youtube_id", yt.metadata)
            self.assertTrue(len(yt.metadata["youtube_id"]) > 5)

    def test_07_source_analyses_present(self):
        """Verify Source Analysis blocks exist in Lessons with complete prompt breakdown."""
        lessons = Lesson.objects.filter(topic=self.topic)
        sa_blocks = LessonBlock.objects.filter(lesson__in=lessons, component_type="source_analysis")
        self.assertGreaterEqual(sa_blocks.count(), 4, "Must have source analysis blocks across lessons.")

        for sa in sa_blocks:
            content = sa.content
            self.assertIn("source_title", content)
            self.assertIn("source_text", content)
            self.assertIn("prompts", content)
            self.assertTrue(len(content["prompts"]) >= 1)
            for p in content["prompts"]:
                self.assertIn("prompt", p)
                self.assertIn("analysis", p)
                self.assertTrue(len(p["analysis"]) > 10)

    def test_08_assessment_mcqs_and_misconceptions(self):
        """Verify all lessons have MCQs with 4 options and detailed explanations, plus misconceptions."""
        lessons = Lesson.objects.filter(topic=self.topic)

        for lesson in lessons:
            # Check MCQs (knowledge_check)
            mcqs = LessonBlock.objects.filter(lesson=lesson, component_type="knowledge_check")
            self.assertGreaterEqual(mcqs.count(), 2, f"Lesson '{lesson.title}' must have at least 2 MCQs.")
            for mcq in mcqs:
                content = mcq.content
                self.assertIn("question", content)
                self.assertIn("options", content)
                self.assertEqual(len(content["options"]), 4, "Each MCQ must have exactly 4 options.")
                self.assertIn("correct", content)
                self.assertIn(content["correct"], ["A", "B", "C", "D"])
                self.assertIn("explanation", content)
                self.assertTrue(len(content["explanation"]) > 20)

            # Check Misconception blocks
            misconceptions = LessonBlock.objects.filter(lesson=lesson, component_type="remedial_misconception")
            self.assertGreaterEqual(misconceptions.count(), 1, f"Lesson '{lesson.title}' must have at least 1 misconception block.")
            for misc in misconceptions:
                content = misc.content
                self.assertIn("misconception", content)
                self.assertIn("correction", content)
                self.assertTrue(len(content["correction"]) > 30)

    def test_09_no_bracket_citations_or_internal_tags(self):
        """Verify no uncleaned [1], [60], [image_1], or [VISUAL: ...] tags exist in any block."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for block in blocks:
            # Check title
            if block.title:
                self.assertNotRegex(block.title, r'\[(?:\d+|image_\d+|S\d+.*?)\]')
                self.assertNotRegex(block.title, r'\[VISUAL:[^\]]*\]')

            # Check content string representations
            content_str = str(block.content)
            self.assertNotRegex(content_str, r'\[(?:\d+|image_\d+|S\d+.*?)\]')
            self.assertNotRegex(content_str, r'\[VISUAL:[^\]]*\]')


if __name__ == "__main__":
    unittest.main()
