"""
VLearn CBC Grade 10 English — Topic 2: Reading
Comprehensive Verification & Unit Test Suite
"""

import os
import sys
import unittest
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestCBCGrade10EnglishTopic2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=5).first()
        if not cls.grade:
            cls.grade = Grade.objects.filter(name="Grade 10", curriculum__name="CBC").first()
        assert cls.grade is not None, "Grade 10 (ID 5) must exist."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        assert cls.subject is not None, "Subject 'English' must exist in Grade 10."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=2).first()
        assert cls.topic is not None, "Topic 2 'Reading' must exist in Subject 'English'."

    def test_topic_structure(self):
        """Test topic naming, description, and order."""
        self.assertEqual(self.topic.order, 2)
        self.assertEqual(self.topic.name, "Reading")
        self.assertIn("fluency", self.topic.description.lower())

    def test_all_10_units_exist(self):
        """Test that all 10 learning units exist in correct sequence."""
        units = list(LearningUnit.objects.filter(topic=self.topic).order_by("order"))
        self.assertEqual(len(units), 10, f"Expected 10 units, found {len(units)}")

        expected_titles = [
            "Reading Fluency and Expressive Reading",
            "Extensive Reading and Reading Stamina",
            "Skimming, Scanning, and Locating Information",
            "Main Ideas, Details, Sequence, and Text Organization",
            "Comprehension, Inference, and Conclusions",
            "Vocabulary in Context and Word Relationships",
            "Study Skills: SQ4R, Note-Making, and Summarising",
            "Critical and Close Reading: Purpose, Audience, Attitude, and Argument",
            "Research Beginnings and Reference Materials",
            "Reading-to-Response and Synthesis"
        ]

        for i, (unit, expected_title) in enumerate(zip(units, expected_titles), start=1):
            self.assertEqual(unit.order, i)
            self.assertEqual(unit.name, expected_title)

    def test_lessons_published_and_linked(self):
        """Test that each unit has one published lesson."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lessons = Lesson.objects.filter(learning_unit=unit)
            self.assertEqual(lessons.count(), 1, f"Unit {unit.order} must have exactly 1 lesson.")
            lesson = lessons.first()
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertEqual(lesson.topic, self.topic)

    def test_each_lesson_has_6_atomic_pages(self):
        """Verify each lesson has exactly 6 distinct page numbers (1 to 6)."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson {unit.order} must have pages 1 through 6.")

    def test_pedagogical_block_structure_per_page(self):
        """Verify required component types on each page."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)
            
            # Page 1: Discovery & Objectives
            p1_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by('component_order')]
            self.assertIn("suggested_image", p1_types)
            self.assertIn("learning_goal", p1_types)
            self.assertIn("concept_explanation", p1_types)

            # Page 2: Core Concepts & Terminology
            p2_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=2).order_by('component_order')]
            self.assertIn("definition_card", p2_types)
            self.assertIn("comparison_table", p2_types)

            # Page 3: Model & Structured Analysis / Visual Diagram
            p3_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=3).order_by('component_order')]
            self.assertIn("suggested_diagram", p3_types)
            self.assertIn("worked_example", p3_types)

            # Page 4: Media Integration & Reading Lab
            p4_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=4).order_by('component_order')]
            self.assertIn("suggested_video", p4_types)
            self.assertIn("real_world_example", p4_types)

            # Page 5: Common Mistakes & Guided Practice
            p5_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=5).order_by('component_order')]
            self.assertIn("concept_explanation", p5_types)
            self.assertIn("step_process", p5_types)

            # Page 6: Knowledge Check & Summary (2 MCQs + 1 Summary)
            p6_blocks = list(LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by('component_order'))
            kc_blocks = [b for b in p6_blocks if b.component_type == "knowledge_check"]
            self.assertEqual(len(kc_blocks), 2, f"Lesson {unit.order} Page 6 must have 2 MCQs.")
            
            for kc in kc_blocks:
                content = kc.content
                self.assertIn("question", content)
                self.assertIn("options", content)
                self.assertEqual(len(content["options"]), 4, "MCQ must have 4 options A-D.")
                self.assertIn("correct_answer", content)
                self.assertIn(content["correct_answer"], [0, 1, 2, 3])
                self.assertIn("explanation", content)
                self.assertTrue(len(content["explanation"]) > 20)

    def test_lesson_assets_integrity(self):
        """Verify diagrams, images, and videos attached to each lesson."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)
            assets = LessonAsset.objects.filter(lesson=lesson)
            
            diagram_assets = assets.filter(asset_type="diagram")
            self.assertEqual(diagram_assets.count(), 1, f"Lesson {unit.order} must have 1 diagram asset.")
            diag = diagram_assets.first()
            self.assertIn("<svg", diag.metadata.get("svg_content", ""))
            self.assertIn("</svg>", diag.metadata.get("svg_content", ""))

            image_assets = assets.filter(asset_type="image")
            self.assertEqual(image_assets.count(), 1, f"Lesson {unit.order} must have 1 image asset.")
            img = image_assets.first()
            self.assertTrue(img.url.startswith("https://upload.wikimedia.org/"))

            video_assets = assets.filter(asset_type="youtube")
            self.assertEqual(video_assets.count(), 1, f"Lesson {unit.order} must have 1 YouTube asset.")
            vid = video_assets.first()
            self.assertTrue(len(vid.metadata.get("youtube_id", "")) > 5)

    def test_clean_text_no_raw_bracket_tags(self):
        """Verify no uncleaned bracket tags exist in content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for b in blocks:
            text_str = str(b.content)
            self.assertNotIn("[AUDIO:", text_str)
            self.assertNotIn("[VIDEO LINK:", text_str)


if __name__ == "__main__":
    unittest.main()
