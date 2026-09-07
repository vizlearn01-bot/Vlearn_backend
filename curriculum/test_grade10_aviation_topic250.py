"""
VLearn Automated QA Suite: Grade 10 Aviation — Topic 250 (ID: 250)
Flight Operations: Aviation Weather
"""

import os
import sys
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

class TestGrade10AviationTopic250(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subject = Subject.objects.get(id=44)
        cls.topic = Topic.objects.get(id=250, subject=cls.subject)
        cls.lessons = Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order")
        cls.expected_lessons = [
            (0, "Elements of Weather in the Atmosphere"),
            (1, "Structure of the Lower Atmosphere: Troposphere and Stratosphere"),
            (2, "Clouds in Flight Operations: Low, Middle, and High Altitude"),
            (3, "Aviation Weather Measurements and Instruments"),
            (4, "Effects of Weather on Flight Operations and Planning Roles")
        ]

    def test_topic_hierarchy(self):
        """Verify Topic 250 exists with correct attributes and lessons."""
        self.assertEqual(self.topic.name, "Flight Operations: Aviation Weather")
        self.assertEqual(self.topic.order, 3)
        self.assertEqual(self.topic.subject.id, 44)
        self.assertEqual(self.topic.subject.grade.level, 10)
        self.assertEqual(self.lessons.count(), 5, f"Expected 5 Lessons under Topic 250, found {self.lessons.count()}")

        for (exp_order, exp_title), lesson in zip(self.expected_lessons, self.lessons):
            self.assertEqual(lesson.learning_unit.order, exp_order)
            self.assertEqual(lesson.title, exp_title)

    def test_lesson_published_status(self):
        """All lessons must be published with version 1."""
        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} is not published")
            self.assertEqual(lesson.version, 1, f"Lesson {lesson.id} version is {lesson.version}")

    def test_card_atomicity_and_blocks(self):
        """Verify each lesson has at least 8-10 cards, image, diagram, video, and MCQs."""
        for lesson in self.lessons:
            blocks = lesson.blocks.all()
            pages = set(blocks.values_list("page_number", flat=True))
            self.assertGreaterEqual(len(pages), 8, f"Lesson {lesson.id} has {len(pages)} cards, expected >= 8")
            
            p1_img = blocks.filter(page_number=1, block_type="suggested_image")
            self.assertTrue(p1_img.exists(), f"Lesson {lesson.id} missing Card 1 suggested_image")

            diag = blocks.filter(block_type="suggested_diagram")
            self.assertTrue(diag.exists(), f"Lesson {lesson.id} missing suggested_diagram")
            for d in diag:
                if isinstance(d.content, dict):
                    svg_str = d.content.get("svg", "") or d.content.get("svg_xml", "")
                else:
                    svg_str = str(d.content)
                self.assertIn("viewBox", svg_str)

            vid = blocks.filter(block_type="suggested_video")
            self.assertTrue(vid.exists(), f"Lesson {lesson.id} missing suggested_video")

            mcqs = blocks.filter(block_type="knowledge_check")
            self.assertGreaterEqual(mcqs.count(), 2, f"Lesson {lesson.id} has {mcqs.count()} MCQs, expected >= 2")
            for mcq in mcqs:
                data = mcq.content if isinstance(mcq.content, dict) else (mcq.metadata or {})
                opts = data.get("options", [])
                self.assertEqual(len(opts), 4, f"Lesson {lesson.id} MCQ has {len(opts)} options, expected 4")
                self.assertIn("answer", data)
                self.assertIn("explanation", data)

    def test_lesson_assets_count(self):
        """Verify 15 LessonAssets attached (3 per lesson)."""
        for lesson in self.lessons:
            assets = LessonAsset.objects.filter(lesson=lesson)
            self.assertEqual(assets.count(), 3, f"Lesson {lesson.id} has {assets.count()} assets, expected 3")
            self.assertTrue(assets.filter(asset_type="image").exists())
            self.assertTrue(assets.filter(asset_type="diagram").exists())
            self.assertTrue(assets.filter(asset_type="youtube").exists())

    def test_sanitization(self):
        """Ensure no bracket citations or prompt leaks remain."""
        for lesson in self.lessons:
            for b in lesson.blocks.all():
                content = b.content or ""
                if isinstance(content, dict):
                    content = str(content)
                self.assertNotIn("[VISUAL:", content)
                self.assertNotIn("[REAL WORLD APPLICATION]", content)
                self.assertNotIn("[PRACTICAL TASK]", content)

if __name__ == "__main__":
    unittest.main()
