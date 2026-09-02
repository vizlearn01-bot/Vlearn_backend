"""
VLearn CBC Grade 10 Business Studies — Topic 15: Source Documents and Books of Original Entry
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

class TestCBCGrade10BusinessStudiesTopic15(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first() or Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="Business Studies").first()
        assert cls.subject, "Subject 'Business Studies' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=15).first()
        assert cls.topic, "Topic 15 'Source Documents and Books of Original Entry' not found under Business Studies!"

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Business Studies")
        self.assertEqual(self.topic.order, 15)
        self.assertEqual(self.topic.name, "Source Documents and Books of Original Entry")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 6 LearningUnits and 6 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 6, f"Expected 6 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 6, f"Expected 6 lessons, found {len(self.lessons)}")

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
        """Verify all 6 lessons have Page 1 photographic visual hooks with Wikimedia URLs."""
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
        """Verify all 6 lessons contain responsive vector SVGs attached as LessonAssets."""
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

            # Verify LessonAsset attachment
            assets = diagram_block.assets.all()
            self.assertGreaterEqual(assets.count(), 1, f"Lesson {u_order} diagram block missing attached Asset!")
            asset = assets.first()
            self.assertEqual(asset.asset_type, "diagram")
            self.assertEqual(asset.status, "attached")

    def test_06_worked_examples_katex_steps(self):
        """Verify Card 5 worked examples contain complete 6-step KaTeX mathematical breakdowns."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            example_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=5,
                block_type="worked_example"
            ).first()

            self.assertIsNotNone(example_block, f"Lesson {u_order} missing Card 5 worked_example block!")
            content = example_block.content or {}
            steps = content.get("steps", [])
            self.assertEqual(len(steps), 6, f"Lesson {u_order} worked example must have 6 steps, found {len(steps)}")
            
            # Check presence of math delimiters
            full_text = " ".join(steps)
            self.assertTrue("$" in full_text, f"Lesson {u_order} worked example missing KaTeX math expressions!")

    def test_07_youtube_video_assets(self):
        """Verify Card 6 real-world examples contain valid educational YouTube video embeds."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=6,
                block_type="suggested_video"
            ).first()

            self.assertIsNotNone(video_block, f"Lesson {u_order} missing Card 6 suggested_video block!")
            content = video_block.content or {}
            youtube_id = content.get("youtube_id")
            self.assertTrue(youtube_id, f"Lesson {u_order} video block missing youtube_id!")

            # Verify LessonAsset attachment
            assets = video_block.assets.all()
            self.assertGreaterEqual(assets.count(), 1, f"Lesson {u_order} video block missing attached Asset!")
            asset = assets.first()
            self.assertEqual(asset.asset_type, "youtube")

    def test_08_formative_mcqs(self):
        """Verify Card 7 contains 2 scenario-based MCQs with 4 options and complete explanations."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            mcq_blocks = list(LessonBlock.objects.filter(
                lesson=lesson,
                page_number=7,
                block_type="knowledge_check"
            ))

            self.assertEqual(len(mcq_blocks), 2, f"Lesson {u_order} Card 7 must have exactly 2 MCQs, found {len(mcq_blocks)}")
            for mcq in mcq_blocks:
                content = mcq.content or {}
                self.assertTrue(content.get("question"), f"Lesson {u_order} MCQ missing question text")
                options = content.get("options", [])
                self.assertEqual(len(options), 4, f"Lesson {u_order} MCQ must have 4 options, found {len(options)}")
                self.assertIn(content.get("correct"), ["A", "B", "C", "D"], f"Lesson {u_order} MCQ correct key invalid")
                self.assertTrue(content.get("explanation"), f"Lesson {u_order} MCQ missing explanation")

    def test_09_no_bracket_citations(self):
        """Verify 0 bracket citations exist across all titles, descriptions, and block contents."""
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                # Check title
                self.assertFalse(citation_pattern.search(b.title or ""), f"Citation found in block title: {b.title}")
                # Check content stringified
                content_str = str(b.content)
                self.assertFalse(citation_pattern.search(content_str), f"Citation found in block content for {b.block_id}: {citation_pattern.findall(content_str)}")

if __name__ == "__main__":
    unittest.main()
