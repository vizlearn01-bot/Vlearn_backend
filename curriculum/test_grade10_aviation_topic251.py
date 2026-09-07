"""
VLearn Automated QA Suite: Grade 10 Aviation — Topic 251
Airport Safety and Operations
"""

import os
import sys
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

class TestGrade10AviationTopic251(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subject = Subject.objects.get(id=44)
        cls.topic = Topic.objects.get(id=251, subject=cls.subject)
        cls.units = LearningUnit.objects.filter(topic=cls.topic).order_by("order")
        cls.lessons = Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order")

    def test_topic_hierarchy(self):
        """Verify Topic 251 exists with correct attributes."""
        self.assertEqual(self.topic.name, "Airport Safety and Operations")
        self.assertEqual(self.topic.order, 4)
        self.assertEqual(self.units.count(), 5, "Expected 5 LearningUnits under Topic 251")
        self.assertEqual(self.lessons.count(), 5, "Expected 5 Lessons under Topic 251")

    def test_lesson_published_status(self):
        """All lessons must be published with version 1."""
        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} is not published")
            self.assertEqual(lesson.version, 1, f"Lesson {lesson.id} version is not 1")

    def test_card_atomicity_and_blocks(self):
        """Each lesson must have at least 8 concept cards and required block types."""
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = blocks.values_list("page_number", flat=True).distinct()
            self.assertGreaterEqual(len(page_numbers), 8, f"Lesson {lesson.id} must have >= 8 cards")

            # Check for photographic hook on Card 1
            photo_block = blocks.filter(page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(photo_block, f"Lesson {lesson.id} Card 1 must have suggested_image")
            self.assertTrue(photo_block.assets.filter(asset_type="image").exists(), f"Lesson {lesson.id} Photo Asset missing")

            # Check for custom SVG diagram
            diag_block = blocks.filter(block_type="suggested_diagram").first()
            self.assertIsNotNone(diag_block, f"Lesson {lesson.id} must have suggested_diagram")
            svg_content = diag_block.content.get("svg", "")
            self.assertIn("<svg", svg_content, f"Lesson {lesson.id} SVG XML missing")
            self.assertIn('viewBox="0 0 800 450"', svg_content, f"Lesson {lesson.id} SVG viewBox invalid")
            self.assertIn("#0f172a", svg_content, f"Lesson {lesson.id} SVG background color theme missing")
            self.assertTrue(diag_block.assets.filter(asset_type="diagram").exists(), f"Lesson {lesson.id} Diagram Asset missing")

            # Check for YouTube video
            video_block = blocks.filter(block_type="suggested_video").first()
            self.assertIsNotNone(video_block, f"Lesson {lesson.id} must have suggested_video")
            self.assertIn("youtube.com", video_block.content.get("url", ""), f"Lesson {lesson.id} YouTube URL invalid")
            self.assertTrue(video_block.assets.filter(asset_type="youtube").exists(), f"Lesson {lesson.id} Video Asset missing")

            # Check for Knowledge Checks (MCQs)
            mcq_blocks = blocks.filter(block_type="knowledge_check")
            self.assertGreaterEqual(mcq_blocks.count(), 2, f"Lesson {lesson.id} must have at least 2 MCQs")
            for mcq in mcq_blocks:
                content = mcq.content or {}
                options = content.get("options", [])
                self.assertEqual(len(options), 4, f"MCQ in Lesson {lesson.id} must have exactly 4 options")
                self.assertIn(content.get("answer"), ["A", "B", "C", "D"], f"Invalid MCQ answer key in Lesson {lesson.id}")
                self.assertTrue(len(content.get("explanation", "").strip()) > 10, f"MCQ explanation empty in Lesson {lesson.id}")

    def test_sanitization(self):
        """Zero bracket citations or internal prompt tags in student-facing blocks."""
        for lesson in self.lessons:
            for b in lesson.blocks.all():
                text_content = str(b.content)
                self.assertNotRegex(text_content, r'\[\d+\]', f"Bracket citation leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[VISUAL:", text_content, f"Visual tag leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[PRACTICAL TASK]", text_content, f"Practical tag leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[REAL WORLD APPLICATION]", text_content, f"Real world tag leak in Lesson {lesson.id} Block {b.id}")

if __name__ == "__main__":
    unittest.main()
