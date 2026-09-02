"""
VLearn CBC Grade 10 CRE — Topic 2.1: The New Testament Books
Automated Verification and Integrity Test Suite

Verifies:
  1. Hierarchy & Database Integrity (Curriculum CBC -> Grade 10 -> CRE -> Topic 2.1 / Order 11)
  2. 4 Discrete Learning Units & 4 Published Lessons (status='published', version=1)
  3. Dynamic 6-Card Progressive Structure (>= 6 pages per lesson, non-empty blocks)
  4. Mandatory First-Card Photographic Visual Hooks (4 Verified Wikimedia Commons URLs & attached LessonAssets)
  5. 4 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", #0f172a theme, zero raw XML headers)
  6. 4 Curated Educational YouTube Videos (embed IDs & attached LessonAssets)
  7. Content Sanitization (0 Bracket Citations, 0 Internal Visual/Passage Tags)
  8. Formative & Summative MCQs Validation (4 Options, Valid Answer Keys & Explanations)
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

class TestCBCGrade10CRETopic2_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name__icontains="CRE").first()
        assert cls.subject, "Subject 'CRE' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=11).first()
        assert cls.topic, "Topic 2.1 (Order: 11) not found under Grade 10 CRE!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.id, 46)
        self.assertIn("CRE", self.subject.name)
        self.assertEqual(self.topic.order, 11)
        self.assertIn("The New Testament Books", self.topic.name)

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 4 LearningUnits and 4 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 4, f"Expected 4 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 4, f"Expected 4 lessons, found {len(self.lessons)}")

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
        """Verify all 4 lessons have Page 1 photographic visual hooks with Wikimedia URLs & attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 visual hook missing URL!")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Invalid Wikimedia URL: {img_url}")

            asset = hook_block.assets.filter(asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} Card 1 hook missing attached LessonAsset!")
            self.assertEqual(asset.url, img_url)

    def test_05_custom_vector_svgs(self):
        """Verify all 4 lessons have custom sanitized responsive vector SVGs with viewBox and attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()
            self.assertIsNotNone(diag_block, f"Lesson {u_order} missing suggested_diagram block!")

            content = diag_block.content or {}
            svg_text = content.get("svg") or content.get("svg_xml") or ""
            self.assertTrue(svg_text, f"Lesson {u_order} diagram block missing SVG payload!")
            self.assertIn("<svg", svg_text)
            self.assertIn("</svg>", svg_text)
            self.assertIn('viewBox="0 0 800 450"', svg_text)
            self.assertIn("#0f172a", svg_text)
            self.assertNotIn("<?xml", svg_text)
            self.assertNotIn("<!DOCTYPE", svg_text)

            asset = diag_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} diagram missing attached LessonAsset!")

    def test_06_video_assets(self):
        """Verify all 4 lessons have curated educational YouTube video blocks and attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()
            self.assertIsNotNone(video_block, f"Lesson {u_order} missing suggested_video block!")

            content = video_block.content or {}
            v_url = content.get("url")
            self.assertTrue(v_url and "youtube.com" in v_url, f"Lesson {u_order} video URL invalid: {v_url}")

            asset = video_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} video missing attached LessonAsset!")

    def test_07_content_sanitization(self):
        """Verify 0 bracket citations and 0 internal visual/passage tags in block contents."""
        bracket_cite_pattern = re.compile(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        internal_tag_pattern = re.compile(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT)[^\]]*\]', re.IGNORECASE)

        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                content_str = str(b.content)
                # Strip SVG text from check so XML attribute brackets don't trigger
                clean_content_str = re.sub(r'<svg.*?</svg>', '', content_str, flags=re.DOTALL)

                match_cite = bracket_cite_pattern.search(clean_content_str)
                self.assertIsNone(match_cite, f"Block {b.id} contains unsanitized bracket citation: '{match_cite.group(0) if match_cite else ''}'")

                match_tag = internal_tag_pattern.search(clean_content_str)
                self.assertIsNone(match_tag, f"Block {b.id} contains internal pedagogical tag: '{match_tag.group(0) if match_tag else ''}'")

    def test_08_mcq_integrity(self):
        """Verify all knowledge check MCQs have 4 options, a valid answer key, and an explanation."""
        valid_keys = {"A", "B", "C", "D"}
        mcq_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="knowledge_check")
        self.assertEqual(len(mcq_blocks), 4, f"Expected 4 MCQ blocks, found {len(mcq_blocks)}")

        for b in mcq_blocks:
            c = b.content or {}
            self.assertTrue(c.get("question"), f"MCQ Block {b.id} missing question")
            options = c.get("options", [])
            self.assertEqual(len(options), 4, f"MCQ Block {b.id} does not have exactly 4 options")
            ans = c.get("answer") or c.get("correct_answer")
            self.assertIn(ans, valid_keys, f"MCQ Block {b.id} has invalid answer key: {ans}")
            self.assertTrue(c.get("explanation"), f"MCQ Block {b.id} missing explanation")

if __name__ == "__main__":
    unittest.main(verbosity=2)
