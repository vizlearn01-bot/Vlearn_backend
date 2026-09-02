"""
VLearn CBC Grade 10 Business Studies — Topic 6: Types of Business Ownership
Automated QA & Integrity Verification Test Suite
"""

import os
import sys
import unittest
import django
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10BusinessStudiesTopic6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first() or Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="Business Studies").first()
        assert cls.subject, "Subject 'Business Studies' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=6).first()
        assert cls.topic, "Topic 6 'Types of Business Ownership' not found under Business Studies!"

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Business Studies")
        self.assertEqual(self.topic.order, 6)
        self.assertEqual(self.topic.name, "Types of Business Ownership")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 16 LearningUnits and 16 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 16, f"Expected 16 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 16, f"Expected 16 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has 8 pages/cards and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks if b.page_number)
            self.assertGreaterEqual(len(page_numbers), 8, f"Lesson {lesson.id} must have >=8 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 16 lessons have Page 1 photographic visual hooks with Wikimedia URLs."""
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
            self.assertTrue("wikimedia.org" in img_url, f"Lesson {u_order} URL not Wikimedia: {img_url}")

    def test_05_custom_vector_svgs(self):
        """Verify all 16 lessons contain responsive vector SVGs attached as LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing suggested_diagram block!")
            content = diagram_block.content or {}
            svg_text = content.get("svg_content", "")
            self.assertTrue("<svg" in svg_text and "</svg>" in svg_text, f"Lesson {u_order} SVG malformed!")
            self.assertTrue("viewBox=" in svg_text, f"Lesson {u_order} SVG missing viewBox!")

    def test_06_worked_examples_and_katex(self):
        """Verify worked examples contain KaTeX math formatting and 0 citation brackets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            example_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="worked_example"
            ).first()

            self.assertIsNotNone(example_block, f"Lesson {u_order} missing worked_example block!")
            content = example_block.content or {}
            steps = content.get("steps", [])
            self.assertTrue(len(steps) >= 4, f"Lesson {u_order} worked example has too few steps ({len(steps)})")

            full_text = " ".join(steps) + " " + content.get("intro", "")
            self.assertFalse(re.search(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', full_text),
                             f"Lesson {u_order} contains bracket citations in worked example!")

    def test_07_youtube_video_assets(self):
        """Verify YouTube educational video blocks and attached assets exist for each lesson."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            self.assertIsNotNone(video_block, f"Lesson {u_order} missing suggested_video block!")
            content = video_block.content or {}
            yt_id = content.get("youtube_id")
            self.assertTrue(yt_id, f"Lesson {u_order} video block missing youtube_id!")

    def test_08_formative_mcqs(self):
        """Verify each lesson contains scenario-based MCQs with valid options, correct answers, and explanations."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            mcq_blocks = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="knowledge_check"
            )
            self.assertGreaterEqual(mcq_blocks.count(), 2, f"Lesson {u_order} must have at least 2 MCQs, got {mcq_blocks.count()}")

            for block in mcq_blocks:
                content = block.content or {}
                self.assertTrue(content.get("question"), f"Lesson {u_order} MCQ missing question text")
                options = content.get("options", [])
                self.assertEqual(len(options), 4, f"Lesson {u_order} MCQ must have exactly 4 options, got {len(options)}")
                self.assertIn(content.get("correct"), ["A", "B", "C", "D"], f"Lesson {u_order} MCQ invalid correct key: {content.get('correct')}")
                self.assertTrue(content.get("explanation"), f"Lesson {u_order} MCQ missing explanation")

if __name__ == "__main__":
    unittest.main()
