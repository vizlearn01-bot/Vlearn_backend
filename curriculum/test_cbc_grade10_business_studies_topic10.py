"""
VLearn CBC Grade 10 Business Studies — Topic 10: Consumer Satisfaction
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

class TestCBCGrade10BusinessStudiesTopic10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first() or Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="Business Studies").first()
        assert cls.subject, "Subject 'Business Studies' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=10).first()
        assert cls.topic, "Topic 10 'Consumer Satisfaction' not found under Business Studies!"

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Business Studies")
        self.assertEqual(self.topic.order, 10)
        self.assertEqual(self.topic.name, "Consumer Satisfaction")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 8 LearningUnits and 8 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 8, f"Expected 8 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 8, f"Expected 8 lessons, found {len(self.lessons)}")

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
            self.assertEqual(len(page_numbers), 8, f"Lesson {lesson.id} must have exactly 8 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 8 lessons have Page 1 photographic visual hooks with Wikimedia URLs."""
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
        """Verify all 8 lessons contain responsive vector SVGs attached as LessonAssets."""
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

            # Verify asset attachment
            assets = list(diagram_block.assets.filter(asset_type="diagram"))
            self.assertTrue(len(assets) >= 1, f"Lesson {u_order} diagram block has no attached diagram asset!")

    def test_06_worked_examples_katex_math(self):
        """Verify Card 5 worked examples have step-by-step structure and KaTeX math formatting."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            math_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=5,
                block_type="worked_example"
            ).first()

            self.assertIsNotNone(math_block, f"Lesson {u_order} Card 5 missing worked_example block!")
            content = math_block.content or {}
            steps = content.get("steps", [])
            self.assertEqual(len(steps), 6, f"Lesson {u_order} Card 5 must have 6 steps, got {len(steps)}")

            # Check math delimiter formatting
            full_math_text = " ".join(steps)
            self.assertTrue("$" in full_math_text, f"Lesson {u_order} math steps missing KaTeX math formatting!")

    def test_07_youtube_video_assets(self):
        """Verify all 8 lessons contain attached educational YouTube video assets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            self.assertIsNotNone(video_block, f"Lesson {u_order} missing suggested_video block!")
            content = video_block.content or {}
            yt_id = content.get("youtube_id")
            self.assertTrue(yt_id and len(yt_id) >= 8, f"Lesson {u_order} invalid youtube_id: {yt_id}")

            assets = list(video_block.assets.filter(asset_type="youtube"))
            self.assertTrue(len(assets) >= 1, f"Lesson {u_order} video block has no attached youtube asset!")

    def test_08_formative_scenario_mcqs(self):
        """Verify Card 7 contains 2 scenario-based MCQs with valid keys (A/B/C/D) and explanations."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            mcq_blocks = list(LessonBlock.objects.filter(
                lesson=lesson,
                page_number=7,
                block_type="knowledge_check"
            ))

            self.assertEqual(len(mcq_blocks), 2, f"Lesson {u_order} Card 7 must have exactly 2 MCQs, got {len(mcq_blocks)}")

            for idx, mcq in enumerate(mcq_blocks, start=1):
                content = mcq.content or {}
                self.assertIn(content.get("correct"), ["A", "B", "C", "D"], f"Lesson {u_order} MCQ {idx} invalid correct key")
                self.assertEqual(len(content.get("options", [])), 4, f"Lesson {u_order} MCQ {idx} must have 4 options")
                self.assertTrue(content.get("explanation"), f"Lesson {u_order} MCQ {idx} missing explanation")

    def test_09_zero_bracket_citations(self):
        """Verify zero bracket citations remain in block titles or content strings."""
        bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                self.assertFalse(bracket_pattern.search(b.title), f"Lesson {u_order} Block {b.id} title has citation: {b.title}")
                # Recursively check content
                def check_no_brackets(val, path=""):
                    if isinstance(val, str):
                        self.assertFalse(bracket_pattern.search(val), f"Lesson {u_order} Block {b.id} content at '{path}' has citation: {val}")
                    elif isinstance(val, dict):
                        for k, v in val.items():
                            check_no_brackets(v, f"{path}.{k}")
                    elif isinstance(val, list):
                        for i, v in enumerate(val):
                            check_no_brackets(v, f"{path}[{i}]")
                check_no_brackets(b.content)

if __name__ == "__main__":
    unittest.main()
