"""
VLearn Automated QA Suite: Grade 10 Aviation — Topic 3 (ID: 249)
Aircraft Components and Construction
"""

import os
import sys
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

class TestGrade10AviationTopic249(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subject = Subject.objects.get(id=44)
        cls.topic = Topic.objects.get(id=249, subject=cls.subject)
        cls.lessons = Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order")
        cls.expected_lessons = [
            (0, "Aircraft Anatomy — Fuselage, Wings, Empennage, and Landing Gear"),
            (1, "Power Plant, Control Surfaces, and Aircraft Systems"),
            (2, "Component Identification and Aircraft Comparison")
        ]

    def test_topic_hierarchy(self):
        """Verify Topic 249 exists with correct attributes and lessons."""
        self.assertEqual(self.topic.name, "Aircraft Components and Construction")
        self.assertEqual(self.topic.order, 2)
        self.assertEqual(self.topic.subject.id, 44)
        self.assertEqual(self.topic.subject.grade.level, 10)
        self.assertEqual(self.lessons.count(), 3, f"Expected 3 Lessons under Topic 249, found {self.lessons.count()}")

        for (exp_order, exp_title), lesson in zip(self.expected_lessons, self.lessons):
            self.assertEqual(lesson.learning_unit.order, exp_order)
            self.assertEqual(lesson.title, exp_title)

    def test_lesson_published_status(self):
        """All lessons must be published with version 1."""
        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} is not published")
            self.assertEqual(lesson.version, 1, f"Lesson {lesson.id} version is not 1")

    def test_card_atomicity_and_blocks(self):
        """Each lesson must have at least 8 concept cards and required block types."""
        expected_images = [
            "https://upload.wikimedia.org/wikipedia/commons/5/51/Cessna_172_Skyhawk%2C_S2-AFH.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/6/6e/C-141C_Glass_Cockpit_Upgrade.JPEG",
            "https://upload.wikimedia.org/wikipedia/commons/7/78/Bell_206L-4_LongRanger_IV_over_Botafogo_Bay%2C_Rio_de_Janeiro.jpg"
        ]
        expected_videos = [
            "https://www.youtube.com/watch?v=_x5RhNQZrrg",
            "https://www.youtube.com/watch?v=CAl3PayUW0M",
            "https://www.youtube.com/watch?v=g9oVFRG1PGQ"
        ]

        for idx, lesson in enumerate(self.lessons):
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = set(blocks.values_list("page_number", flat=True))
            self.assertGreaterEqual(len(page_numbers), 8, f"Lesson {lesson.id} must have >= 8 cards")
            self.assertEqual(len(page_numbers), 10, f"Lesson {lesson.id} expected 10 cards")

            # Check for photographic hook on Card 1
            photo_block = blocks.filter(page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(photo_block, f"Lesson {lesson.id} Card 1 must have suggested_image")
            resolved_url = photo_block.content.get("resolved_image_url") or photo_block.content.get("url")
            self.assertEqual(resolved_url, expected_images[idx], f"Lesson {lesson.id} photo URL mismatch")
            self.assertTrue(photo_block.assets.filter(asset_type="image").exists(), f"Lesson {lesson.id} Photo Asset missing")

            # Check for custom SVG diagram
            diag_block = blocks.filter(block_type="suggested_diagram").first()
            self.assertIsNotNone(diag_block, f"Lesson {lesson.id} must have suggested_diagram")
            svg_content = diag_block.content.get("svg", "")
            self.assertIn("<svg", svg_content, f"Lesson {lesson.id} SVG XML missing")
            self.assertIn('viewBox="0 0 800 450"', svg_content, f"Lesson {lesson.id} SVG viewBox incorrect")
            self.assertIn("#0f172a", svg_content, f"Lesson {lesson.id} SVG dark slate theme missing")
            self.assertTrue(diag_block.assets.filter(asset_type="diagram").exists(), f"Lesson {lesson.id} Diagram Asset missing")

            # Check for YouTube video
            video_block = blocks.filter(block_type="suggested_video").first()
            self.assertIsNotNone(video_block, f"Lesson {lesson.id} must have suggested_video")
            vid_url = video_block.content.get("url", "")
            self.assertEqual(vid_url, expected_videos[idx], f"Lesson {lesson.id} YouTube URL mismatch")
            self.assertTrue(video_block.assets.filter(asset_type="youtube").exists(), f"Lesson {lesson.id} Video Asset missing")

            # Check for Knowledge Checks (MCQs)
            mcq_blocks = blocks.filter(block_type="knowledge_check")
            self.assertGreaterEqual(mcq_blocks.count(), 2, f"Lesson {lesson.id} must have at least 2 MCQs")
            for mcq in mcq_blocks:
                content = mcq.content or {}
                options = content.get("options", [])
                self.assertEqual(len(options), 4, f"MCQ in Lesson {lesson.id} must have exactly 4 options")
                self.assertIn(content.get("answer"), ["A", "B", "C", "D"], f"Invalid MCQ answer key in Lesson {lesson.id}")
                self.assertTrue(len(content.get("explanation", "").strip()) > 20, f"MCQ explanation too short in Lesson {lesson.id}")

    def test_sanitization(self):
        """Zero bracket citations or internal prompt tags in student-facing blocks."""
        for lesson in self.lessons:
            for b in lesson.blocks.all():
                text_content = str(b.content)
                self.assertNotRegex(text_content, r'\[\d+\]', f"Bracket citation leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[VISUAL:", text_content, f"Visual tag leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[REAL WORLD APPLICATION]", text_content, f"Real-world tag leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[PRACTICAL TASK]", text_content, f"Practical tag leak in Lesson {lesson.id} Block {b.id}")
                self.assertNotIn("[SCENARIO]", text_content, f"Scenario tag leak in Lesson {lesson.id} Block {b.id}")

    def test_lesson_assets_integrity(self):
        """Verify all LessonAssets for Topic 249 are valid and bound."""
        assets = LessonAsset.objects.filter(lesson__topic=self.topic)
        self.assertEqual(assets.count(), 9, f"Expected 9 LessonAssets (3 photos, 3 svgs, 3 videos), found {assets.count()}")
        self.assertEqual(assets.filter(asset_type="image").count(), 3)
        self.assertEqual(assets.filter(asset_type="diagram").count(), 3)
        self.assertEqual(assets.filter(asset_type="youtube").count(), 3)
        for asset in assets:
            self.assertEqual(asset.status, "attached")
            self.assertGreater(asset.blocks.count(), 0, f"Asset {asset.id} not bound to any block")

if __name__ == "__main__":
    unittest.main()
