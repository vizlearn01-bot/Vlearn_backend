"""
Automated QA & Integrity Verification Test Suite for
CBC Grade 10 English — Topic 1 (Lessons 4, 5, 6, and 7)
"""

import os
import sys
import unittest
import xml.etree.ElementTree as ET
import django

# Setup django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10EnglishTopic1Lessons4To7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=5).first()
        assert cls.grade, "Grade ID 5 (Grade 10 CBC) not found!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        assert cls.subject, "Subject 'English' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=1).first()
        assert cls.topic, "Topic 1 'Listening and Speaking' not found under English!"

        cls.expected_lessons = {
            4: "Critical Listening: Fact, Opinion, Evidence, and Bias",
            5: "Intensive Listening and Viewing for Details",
            6: "Non-verbal Communication and Conversational Skills",
            7: "Interactive and Responsive Listening"
        }

    def test_01_curriculum_hierarchy_linkage(self):
        """Verify Grade 10 English subject and Topic 1 linkage."""
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "English")
        self.assertEqual(self.topic.order, 1)
        self.assertEqual(self.topic.name, "Listening and Speaking")

    def test_02_units_and_published_lessons(self):
        """Verify Units 4, 5, 6, and 7 are created, correctly ordered, and published."""
        for u_order, expected_title in self.expected_lessons.items():
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            self.assertIsNotNone(unit, f"LearningUnit {u_order} does not exist!")
            self.assertEqual(unit.name, expected_title)

            lesson = Lesson.objects.filter(topic=self.topic, learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"Lesson for Unit {u_order} does not exist!")
            self.assertEqual(lesson.title, expected_title)
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)

    def test_03_atomic_page_architecture(self):
        """Verify each lesson has exactly 6 sequential pages with standard components."""
        for u_order in self.expected_lessons.keys():
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))

            self.assertGreaterEqual(len(blocks), 15, f"Lesson {u_order} has fewer than 15 blocks ({len(blocks)})")

            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson {u_order} pages must be exactly [1, 2, 3, 4, 5, 6]")

            # Page 1: Discovery & Objectives (suggested_image, learning_goal)
            p1_types = [b.component_type for b in blocks if b.page_number == 1]
            self.assertIn("suggested_image", p1_types, f"Lesson {u_order} Page 1 missing suggested_image")
            self.assertIn("learning_goal", p1_types, f"Lesson {u_order} Page 1 missing learning_goal")

            # Page 2: Core Concepts & Terminology (definition_card, comparison_table)
            p2_types = [b.component_type for b in blocks if b.page_number == 2]
            self.assertIn("definition_card", p2_types, f"Lesson {u_order} Page 2 missing definition_card")
            self.assertIn("comparison_table", p2_types, f"Lesson {u_order} Page 2 missing comparison_table")

            # Page 3: Model & Structured Analysis (diagram/suggested_diagram, model_dialogue)
            p3_types = [b.component_type for b in blocks if b.page_number == 3]
            self.assertTrue("suggested_diagram" in p3_types or "diagram" in p3_types, f"Lesson {u_order} Page 3 missing diagram")
            self.assertIn("model_dialogue", p3_types, f"Lesson {u_order} Page 3 missing model_dialogue")

            # Page 4: Media Integration & Listening Lab (suggested_video, listening_lab)
            p4_types = [b.component_type for b in blocks if b.page_number == 4]
            self.assertIn("suggested_video", p4_types, f"Lesson {u_order} Page 4 missing suggested_video")
            self.assertIn("listening_lab", p4_types, f"Lesson {u_order} Page 4 missing listening_lab")

            # Page 5: Common Mistakes & Guided Practice (common_mistakes, guided_practice)
            p5_types = [b.component_type for b in blocks if b.page_number == 5]
            self.assertIn("common_mistakes", p5_types, f"Lesson {u_order} Page 5 missing common_mistakes")
            self.assertIn("guided_practice", p5_types, f"Lesson {u_order} Page 5 missing guided_practice")

            # Page 6: Knowledge Check & Summary (knowledge_check, key_takeaway)
            p6_types = [b.component_type for b in blocks if b.page_number == 6]
            self.assertIn("knowledge_check", p6_types, f"Lesson {u_order} Page 6 missing knowledge_check")
            self.assertIn("key_takeaway", p6_types, f"Lesson {u_order} Page 6 missing key_takeaway")

    def test_04_svg_diagram_assets(self):
        """Verify all 4 lessons have valid, responsive XML SVGs embedded in LessonAssets."""
        for u_order in self.expected_lessons.keys():
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            diagram_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram").first()
            self.assertIsNotNone(diagram_asset, f"Lesson {u_order} missing diagram LessonAsset!")
            
            svg_content = diagram_asset.metadata.get("svg_content", "")
            self.assertTrue(svg_content.startswith("<svg"), f"Lesson {u_order} SVG does not start with <svg")
            self.assertTrue(svg_content.endswith("</svg>"), f"Lesson {u_order} SVG does not end with </svg>")
            
            # Check XML syntax
            root = ET.fromstring(svg_content)
            self.assertIn("viewBox", root.attrib, f"Lesson {u_order} SVG missing viewBox attribute!")

    def test_05_verified_wikimedia_images(self):
        """Verify all 4 lessons have attached Wikimedia Commons photographic assets with full attribution."""
        for u_order in self.expected_lessons.keys():
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            image_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="image").first()
            self.assertIsNotNone(image_asset, f"Lesson {u_order} missing image LessonAsset!")
            self.assertTrue(image_asset.url.startswith("https://upload.wikimedia.org/"), f"Lesson {u_order} URL not Wikimedia!")
            self.assertIn("licensing", image_asset.metadata)
            self.assertIn("caption", image_asset.metadata)

    def test_06_video_assets(self):
        """Verify all 4 lessons have valid YouTube media assets attached."""
        for u_order in self.expected_lessons.keys():
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            video_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube").first()
            self.assertIsNotNone(video_asset, f"Lesson {u_order} missing youtube LessonAsset!")
            self.assertTrue(video_asset.url.startswith("https://www.youtube.com/watch?v="))
            self.assertTrue(len(video_asset.metadata.get("youtube_id", "")) >= 8)

    def test_07_mcq_assessment_integrity(self):
        """Verify all knowledge check blocks have questions, options, and explanations."""
        for u_order in self.expected_lessons.keys():
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            mcqs = LessonBlock.objects.filter(lesson=lesson, component_type="knowledge_check")
            self.assertGreaterEqual(mcqs.count(), 1, f"Lesson {u_order} must have at least 1 MCQ")

            for mcq in mcqs:
                content = mcq.content or {}
                self.assertIn("question", content)
                self.assertIn("options", content)
                self.assertIn("correct_answer", content)
                self.assertIn("explanation", content)
                self.assertGreaterEqual(len(content["options"]), 4)

if __name__ == "__main__":
    unittest.main()
