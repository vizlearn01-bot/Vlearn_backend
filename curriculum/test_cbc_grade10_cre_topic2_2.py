"""
VLearn CBC Grade 10 CRE — Sub-Strand 2.2: Infancy and Early Life of Jesus Christ
Automated Verification and Integrity Test Suite
"""

import os
import sys
import re
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


class TestCBCGrade10CRETopic2_2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name__icontains="CRE").first()
        assert cls.subject, "Subject 'CRE' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=12).first()
        assert cls.topic, "Topic 2.2 (Order: 12) not found under Grade 10 CRE!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.id, 46)
        self.assertIn("CRE", self.subject.name)
        self.assertEqual(self.topic.order, 12)
        self.assertIn("Infancy and Early Life of Jesus Christ", self.topic.name)

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 6 LearningUnits and 6 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 6, f"Expected 6 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 6, f"Expected 6 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has 6 progressive pages and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertGreaterEqual(len(blocks), 11, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertEqual(len(page_numbers), 6, f"Lesson {lesson.id} must have exactly 6 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 6 lessons have Page 1 photographic visual hooks with Wikimedia URLs & attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("url") or content.get("resolved_image_url")
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 visual hook missing URL!")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Invalid Wikimedia URL: {img_url}")

            asset = hook_block.assets.filter(asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} Card 1 hook missing attached LessonAsset!")

    def test_05_pedagogical_vector_svgs(self):
        """Verify all 6 lessons have responsive Vector SVGs with dark theme and attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            svg_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=3,
                block_type="suggested_diagram"
            ).first()

            self.assertIsNotNone(svg_block, f"Lesson {u_order} missing Page 3 suggested_diagram block!")
            content = svg_block.content or {}
            svg_text = content.get("svg", "")
            self.assertTrue(svg_text.startswith("<svg"), f"Lesson {u_order} SVG missing <svg root: {svg_text[:50]}")
            self.assertIn('viewBox="0 0 800 450"', svg_text, f"Lesson {u_order} SVG missing viewBox 800x450")
            self.assertIn("#0f172a", svg_text, f"Lesson {u_order} SVG missing #0f172a theme")

            asset = svg_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} diagram missing attached LessonAsset!")
            self.assertIn("svg_content", asset.metadata, f"Lesson {u_order} asset metadata missing svg_content")

    def test_06_curated_educational_videos(self):
        """Verify all 6 lessons have curated educational YouTube videos with attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=4,
                block_type="suggested_video"
            ).first()

            self.assertIsNotNone(video_block, f"Lesson {u_order} missing Page 4 suggested_video block!")
            content = video_block.content or {}
            yt_id = content.get("youtube_id")
            self.assertTrue(yt_id, f"Lesson {u_order} video block missing youtube_id")

            asset = video_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} video missing attached LessonAsset!")

    def test_07_content_sanitization(self):
        """Verify 0 bracket citations or internal prompt tags exist in block titles and contents."""
        bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        tag_pattern = re.compile(r'\[(?:VISUAL|BIBLE PASSAGE|CRITICAL THINKING|REAL WORLD APPLICATION):?[^\]]*\]')

        for lesson in self.lessons:
            for block in lesson.blocks.all():
                # Check title
                if block.title:
                    self.assertFalse(bracket_pattern.search(block.title), f"Citation found in title of block {block.id}: {block.title}")
                    self.assertFalse(tag_pattern.search(block.title), f"Tag found in title of block {block.id}: {block.title}")

                # Check text content
                content = block.content or {}
                if isinstance(content, dict):
                    markdown = content.get("markdown", "")
                    if markdown:
                        self.assertFalse(bracket_pattern.search(markdown), f"Citation found in markdown of block {block.id}")
                        self.assertFalse(tag_pattern.search(markdown), f"Tag found in markdown of block {block.id}")

    def test_08_formative_mcqs(self):
        """Verify every lesson has a valid 4-option MCQ with valid answer key and explanation on Page 6."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            mcq_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=6,
                block_type="knowledge_check"
            ).first()

            self.assertIsNotNone(mcq_block, f"Lesson {u_order} missing Page 6 knowledge_check block!")
            content = mcq_block.content or {}
            self.assertTrue(content.get("question"), f"Lesson {u_order} MCQ missing question")
            options = content.get("options", [])
            self.assertEqual(len(options), 4, f"Lesson {u_order} MCQ must have 4 options, got {len(options)}")
            ans = content.get("answer")
            self.assertIn(ans, ["A", "B", "C", "D"], f"Lesson {u_order} MCQ answer must be A/B/C/D, got {ans}")
            self.assertTrue(content.get("explanation"), f"Lesson {u_order} MCQ missing explanation")


if __name__ == "__main__":
    unittest.main()
