"""
VLearn Automated QA Suite: Grade 10 Aviation — Topic 367 (ID: 367)
The Airport: Structure and Operations
"""

import os
import sys
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

class TestGrade10AviationTopic367(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subject = Subject.objects.get(id=44)
        cls.topic = Topic.objects.get(id=367, subject=cls.subject)
        cls.lessons = Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order")
        cls.expected_lessons = [
            (0, "Categories of Airports (Kenya & International)"),
            (1, "Functions of Major Areas of an Airport"),
            (2, "Runway Designation and Numbering"),
            (3, "Runway Visual Markings and Signs"),
            (4, "Airport Operations & Air Traffic Control")
        ]

    def test_topic_hierarchy(self):
        """Verify Topic 367 exists with correct attributes and lessons."""
        self.assertEqual(self.topic.name, "The Airport: Structure and Operations")
        self.assertEqual(self.topic.order, 9)
        self.assertEqual(self.topic.subject.id, 44)
        self.assertEqual(self.topic.subject.grade.level, 10)
        self.assertEqual(self.lessons.count(), 5, f"Expected 5 Lessons under Topic 367, found {self.lessons.count()}")

        for (exp_order, exp_title), lesson in zip(self.expected_lessons, self.lessons):
            self.assertEqual(lesson.learning_unit.order, exp_order)
            self.assertEqual(lesson.title, exp_title)

    def test_lesson_published_status(self):
        """All lessons must be published with version 1."""
        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} is not published")
            self.assertEqual(lesson.version, 1, f"Lesson {lesson.id} version is not 1")

    def test_card_atomicity_and_blocks(self):
        """Each lesson must have exactly 10 concept cards and required block types."""
        expected_images = [
            "https://upload.wikimedia.org/wikipedia/commons/8/87/Jomo_Kenyatta_International_Airport_%28JKIA%29.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/0/07/Qatar_Airways_Airbus_A380-800_at_Heathrow_Airport_Terminal_4_before_Flying_to_Doha%2C_6_Jan_2015.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/7/78/15R-33L_-_Aeropuerto_de_Madrid-Barajas_-_detail.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/0/03/ATL_TWY_B_-_RWY_Crossing_%2813534655025%29.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/0/09/Air_traffic_heathrow.JPG"
        ]
        expected_videos = [
            "https://www.youtube.com/watch?v=B0Ar5WsUhWs",
            "https://www.youtube.com/watch?v=YmlfheAGx0E",
            "https://www.youtube.com/watch?v=Yacx4jNQlgo",
            "https://www.youtube.com/watch?v=eZuutXV7fqY",
            "https://www.youtube.com/watch?v=0t8tL6Mtp4E"
        ]

        for idx, lesson in enumerate(self.lessons):
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = set(blocks.values_list("page_number", flat=True))
            self.assertEqual(len(page_numbers), 10, f"Lesson {lesson.id} must have exactly 10 cards")

            # Check for photographic hook on Card 1
            photo_block = blocks.filter(page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(photo_block, f"Lesson {lesson.id} Card 1 must have suggested_image")
            resolved_url = photo_block.content.get("resolved_image_url") or photo_block.content.get("url")
            self.assertEqual(resolved_url, expected_images[idx], f"Lesson {lesson.id} photo URL mismatch")
            self.assertTrue(photo_block.assets.filter(asset_type="image").exists(), f"Lesson {lesson.id} Photo Asset missing")

            # Check for learning goal on Card 1
            goal_block = blocks.filter(page_number=1, block_type="learning_goal").first()
            self.assertIsNotNone(goal_block, f"Lesson {lesson.id} Card 1 must have learning_goal")

            # Check for definition card on Card 2
            def_block = blocks.filter(page_number=2, block_type="definition_card").first()
            self.assertIsNotNone(def_block, f"Lesson {lesson.id} Card 2 must have definition_card")

            # Check for custom SVG diagram on Card 4
            diag_block = blocks.filter(block_type="suggested_diagram").first()
            self.assertIsNotNone(diag_block, f"Lesson {lesson.id} must have suggested_diagram")
            svg_content = diag_block.content.get("svg", "")
            self.assertIn("<svg", svg_content, f"Lesson {lesson.id} SVG XML missing")
            self.assertIn('viewBox="0 0 800 450"', svg_content, f"Lesson {lesson.id} SVG viewBox incorrect")
            self.assertIn("#0f172a", svg_content, f"Lesson {lesson.id} SVG dark slate theme missing")
            self.assertTrue(diag_block.assets.filter(asset_type="diagram").exists(), f"Lesson {lesson.id} Diagram Asset missing")

            # Check for YouTube video on Card 9
            video_block = blocks.filter(block_type="suggested_video").first()
            self.assertIsNotNone(video_block, f"Lesson {lesson.id} must have suggested_video")
            vid_url = video_block.content.get("url", "")
            self.assertEqual(vid_url, expected_videos[idx], f"Lesson {lesson.id} YouTube URL mismatch")
            self.assertTrue(video_block.assets.filter(asset_type="youtube").exists(), f"Lesson {lesson.id} Video Asset missing")

            # Check for Knowledge Checks (MCQs) on Card 10
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
        forbidden_patterns = [
            r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]',
            r'\[VISUAL:\s*[^\]]+\]',
            r'\[(?:REAL WORLD APPLICATION|PRACTICAL TASK|SAFETY SCENARIO|SCENARIO)[^\]]*\]',
        ]
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for b in blocks:
            text_to_check = f"{b.title} {b.page_title} {str(b.content)}"
            for pat in forbidden_patterns:
                self.assertNotRegex(
                    text_to_check,
                    pat,
                    f"Forbidden pattern '{pat}' found in LessonBlock {b.id} (Lesson {b.lesson_id}, Page {b.page_number})"
                )

    def test_lesson_assets_count(self):
        """Verify 15 LessonAssets exist and are bound to Topic 367 lessons."""
        assets = LessonAsset.objects.filter(lesson__topic=self.topic)
        self.assertEqual(assets.count(), 15, f"Expected 15 LessonAssets, found {assets.count()}")
        self.assertEqual(assets.filter(asset_type="image").count(), 5)
        self.assertEqual(assets.filter(asset_type="diagram").count(), 5)
        self.assertEqual(assets.filter(asset_type="youtube").count(), 5)

if __name__ == "__main__":
    unittest.main()
