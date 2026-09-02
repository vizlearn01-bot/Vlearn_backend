"""
Unit and Integration Tests for CBC Grade 10 English Topic 1 (Lessons 8, 9, and 10)
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

import unittest
from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestGrade10EnglishTopic1Ingestion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=5).first()
        cls.subject = Subject.objects.filter(grade_id=5, name="English").first()
        cls.topic = Topic.objects.filter(subject=cls.subject, order=1).first() if cls.subject else None

    def test_01_subject_and_topic_linkage(self):
        """Test Subject 'English' is linked to Grade ID 5, and Topic 1 is 'Listening and Speaking'."""
        self.assertIsNotNone(self.grade, "Grade ID 5 (Grade 10 CBC) must exist.")
        self.assertIsNotNone(self.subject, "Subject 'English' must exist in Grade ID 5.")
        self.assertEqual(self.subject.grade.id, 5)
        self.assertIsNotNone(self.topic, "Topic 1 must exist for English.")
        self.assertEqual(self.topic.order, 1)
        self.assertEqual(self.topic.name, "Listening and Speaking")

    def test_02_learning_units_8_9_10(self):
        """Test Units 8, 9, and 10 exist under Topic 1."""
        for u_order, expected_title in [
            (8, "Syllabic and Emphatic Stress"),
            (9, "Speaking Fluency: Conversation, Presentation, and Interview"),
            (10, "Meetings, Discussions, Debate, and Oral Decision-making")
        ]:
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            self.assertIsNotNone(unit, f"LearningUnit with order {u_order} must exist.")
            self.assertEqual(unit.name, expected_title)
            
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"Lesson for Unit {u_order} must exist.")
            self.assertEqual(lesson.title, expected_title)
            self.assertEqual(lesson.status, "published")

    def test_03_lesson_pages_and_atomic_card_structure(self):
        """Verify each lesson has 6 atomic pages with proper page_number and component_type."""
        for u_order in [8, 9, 10]:
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")

            # Must have blocks
            self.assertGreater(blocks.count(), 0)

            # Check distinct page numbers (1 to 6)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson {u_order} must contain exactly pages 1 to 6.")

            # Page 1: Must contain suggested_image and learning_goal
            p1_types = [b.component_type for b in blocks if b.page_number == 1]
            self.assertIn("suggested_image", p1_types, f"Lesson {u_order} Page 1 must have suggested_image.")
            self.assertIn("learning_goal", p1_types, f"Lesson {u_order} Page 1 must have learning_goal.")

            # Page 2: Must contain definition_card and concept_explanation
            p2_types = [b.component_type for b in blocks if b.page_number == 2]
            self.assertIn("definition_card", p2_types, f"Lesson {u_order} Page 2 must have definition_card.")
            self.assertIn("concept_explanation", p2_types, f"Lesson {u_order} Page 2 must have concept_explanation.")

            # Page 3: Must contain suggested_diagram
            p3_types = [b.component_type for b in blocks if b.page_number == 3]
            self.assertIn("suggested_diagram", p3_types, f"Lesson {u_order} Page 3 must have suggested_diagram.")

            # Page 4: Must contain suggested_video
            p4_types = [b.component_type for b in blocks if b.page_number == 4]
            self.assertIn("suggested_video", p4_types, f"Lesson {u_order} Page 4 must have suggested_video.")

            # Page 5: Must contain common_mistakes and guided_practice
            p5_types = [b.component_type for b in blocks if b.page_number == 5]
            self.assertIn("common_mistakes", p5_types, f"Lesson {u_order} Page 5 must have common_mistakes.")
            self.assertIn("guided_practice", p5_types, f"Lesson {u_order} Page 5 must have guided_practice.")

            # Page 6: Must contain knowledge_check and summary_card
            p6_types = [b.component_type for b in blocks if b.page_number == 6]
            self.assertIn("knowledge_check", p6_types, f"Lesson {u_order} Page 6 must have knowledge_check.")
            self.assertIn("summary_card", p6_types, f"Lesson {u_order} Page 6 must have summary_card.")

    def test_04_svg_diagram_validity(self):
        """Test all Lesson 8, 9, 10 SVGs are valid XML and have responsive attributes."""
        for u_order in [8, 9, 10]:
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            diagram_block = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_diagram").first()
            self.assertIsNotNone(diagram_block, f"Lesson {u_order} must have a diagram block.")
            
            svg_content = diagram_block.content.get("svg_content", "")
            self.assertTrue(svg_content.startswith("<svg"), f"Lesson {u_order} SVG must start with <svg.")
            self.assertIn('viewBox="0 0', svg_content, f"Lesson {u_order} SVG must have viewBox.")
            self.assertIn('width="100%"', svg_content, f"Lesson {u_order} SVG must be responsive.")
            
            # Verify valid XML parsing
            try:
                root = ET.fromstring(svg_content)
                self.assertEqual(root.tag.split("}")[-1], "svg", f"Lesson {u_order} SVG root tag must be svg.")
            except ET.ParseError as e:
                self.fail(f"Lesson {u_order} SVG XML parse error: {e}")

    def test_05_verified_wikimedia_images(self):
        """Test that images are valid Wikimedia Commons URLs with author and licensing."""
        for u_order in [8, 9, 10]:
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            img_block = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_image").first()
            self.assertIsNotNone(img_block, f"Lesson {u_order} must have an image block.")
            
            content = img_block.content
            url = content.get("url", "")
            self.assertTrue(url.startswith("https://upload.wikimedia.org/"), f"Lesson {u_order} image URL must be from Wikimedia Commons.")
            self.assertTrue(bool(content.get("caption")), f"Lesson {u_order} image must have a caption.")
            self.assertTrue(bool(content.get("author")), f"Lesson {u_order} image must have an author.")
            self.assertTrue(bool(content.get("licensing")), f"Lesson {u_order} image must have licensing info.")

    def test_06_knowledge_check_integrity(self):
        """Test Knowledge Check blocks have well-formed MCQ structures."""
        for u_order in [8, 9, 10]:
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            kc_blocks = LessonBlock.objects.filter(lesson=lesson, component_type="knowledge_check")
            self.assertGreaterEqual(kc_blocks.count(), 1, f"Lesson {u_order} must have at least 1 MCQ.")
            
            for kc in kc_blocks:
                c = kc.content
                self.assertTrue(bool(c.get("question")), "MCQ must have question text.")
                self.assertEqual(len(c.get("options", [])), 4, "MCQ must have exactly 4 options.")
                self.assertIn(c.get("correct"), ["A", "B", "C", "D"], "MCQ correct answer must be A, B, C, or D.")
                self.assertTrue(bool(c.get("explanation")), "MCQ must have explanation.")


if __name__ == "__main__":
    unittest.main()
