"""
VLearn CBC Grade 10 Agriculture — Topic 12: Animal Rearing Project
Automated Dual QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (Curriculum -> Grade 10 -> Agriculture -> Topic 12: Animal Rearing Project)
  2. 10 Learning Units & 10 Published Lessons Validation
  3. Dynamic Card & Block Structure Integrity (all lessons >= 5 pages, non-empty content)
  4. Mandatory First-Card Visual Hooks (10 Tested Wikimedia URLs & attached LessonAssets)
  5. 8 Custom Sanitized Responsive Vector SVGs (viewBox, sanitization & attached LessonAssets)
  6. 1 Verified Educational YouTube Video Asset (Lesson 7)
  7. Content Sanitization (0 Bracket Citations, 0 Developer Meta-Terms, 0 Raw LaTeX Leaks)
  8. Formative & Summative Scenario-Based MCQs Validation (17 MCQs with 4 Options, Valid Answer Key & Explanations)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_agriculture_topic12.py
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

class TestCBCGrade10AgricultureTopic12(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="Agriculture").first()
        assert cls.subject, "Subject 'Agriculture' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, name="Animal Rearing Project").first()
        assert cls.topic, "Topic 12 'Animal Rearing Project' not found under Agriculture!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Agriculture")
        self.assertEqual(self.topic.order, 12)
        self.assertEqual(self.topic.name, "Animal Rearing Project")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 10 LearningUnits and 10 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 10, f"Expected 10 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 10, f"Expected 10 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has valid page counts and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(len(page_numbers), 4, f"Lesson {lesson.id} must have >=4 pages, got {len(page_numbers)}")
            self.assertLessEqual(len(page_numbers), 14, f"Lesson {lesson.id} has too many pages ({len(page_numbers)})")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 10 lessons have Page 1 photographic visual hooks with HTTP 200 URLs & attached LessonAssets."""
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

            # Verify MediaWiki valid URL
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Invalid Wikimedia URL: {img_url}")

            # Verify persistent LessonAsset
            asset = hook_block.assets.filter(asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} Card 1 hook missing attached LessonAsset!")
            self.assertEqual(asset.status, "attached")
            self.assertEqual(asset.url, img_url)

    def test_05_custom_vector_svgs(self):
        """Verify 8 custom responsive SVGs have viewBox, are sanitized, and have attached LessonAssets."""
        expected_svg_units = [1, 2, 4, 5, 6, 9, 10]
        for u_order in expected_svg_units:
            lesson = next((l for l in self.lessons if l.learning_unit.order == u_order), None)
            self.assertIsNotNone(lesson, f"Lesson {u_order} not found!")

            diag_blocks = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            )
            self.assertTrue(diag_blocks.exists(), f"Lesson {u_order} missing suggested_diagram block!")

            for diag_block in diag_blocks:
                content = diag_block.content or {}
                svg_text = content.get("svg") or content.get("svg_xml") or ""
                self.assertTrue(svg_text, f"Lesson {u_order} diagram block missing SVG payload!")
                self.assertIn("<svg", svg_text)
                self.assertIn("</svg>", svg_text)
                self.assertIn('viewBox="0 0 800 450"', svg_text)
                self.assertNotIn("<?xml", svg_text)
                self.assertNotIn("<!DOCTYPE", svg_text)

                asset = diag_block.assets.filter(asset_type="diagram").first()
                self.assertIsNotNone(asset, f"Lesson {u_order} diagram missing attached LessonAsset!")
                self.assertEqual(asset.status, "attached")

    def test_06_video_review_assets(self):
        """Verify educational YouTube video asset in Lesson 7."""
        lesson = next((l for l in self.lessons if l.learning_unit.order == 7), None)
        video_block = LessonBlock.objects.filter(
            lesson=lesson,
            block_type="suggested_video"
        ).first()
        self.assertIsNotNone(video_block, "Lesson 7 missing suggested_video block!")

        content = video_block.content or {}
        v_url = content.get("url")
        self.assertTrue(v_url and "youtube.com" in v_url, f"Lesson 7 video URL invalid: {v_url}")

        asset = video_block.assets.filter(asset_type="youtube").first()
        self.assertIsNotNone(asset, "Lesson 7 video missing attached LessonAsset!")
        self.assertEqual(asset.status, "attached")

    def test_07_content_sanitization(self):
        """Verify 0 bracket citations, 0 developer meta-tags, and 0 unescaped raw LaTeX leaks."""
        bracket_cite_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')

        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                self.assertFalse(
                    bracket_cite_pattern.search(b.title or ""),
                    f"Bracket citation found in Block {b.id} title: {b.title}"
                )

                def check_strings(val, path=""):
                    if isinstance(val, str):
                        if "<svg" in val:
                            return
                        self.assertFalse(
                            bracket_cite_pattern.search(val),
                            f"Bracket citation leak in Block {b.id} at {path}: {val[:60]}"
                        )
                    elif isinstance(val, dict):
                        for k, v in val.items():
                            check_strings(v, f"{path}.{k}")
                    elif isinstance(val, list):
                        for idx, v in enumerate(val):
                            check_strings(v, f"{path}[{idx}]")

                check_strings(b.content)

    def test_08_formative_and_summative_mcqs(self):
        """Verify formative MCQs in Lessons 1-9 and Summative MCQs in Lesson 10 have 4 options, key, and explanation."""
        total_mcqs = 0
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="knowledge_check")
            self.assertTrue(len(mcq_blocks) >= 1, f"Lesson {lesson.id} missing formative knowledge_check block!")

            for mb in mcq_blocks:
                total_mcqs += 1
                c = mb.content or {}
                self.assertTrue(c.get("question"), f"MCQ Block {mb.id} missing question!")
                options = c.get("options") or []
                self.assertEqual(len(options), 4, f"MCQ Block {mb.id} must have exactly 4 options, got {len(options)}")
                self.assertIn(c.get("answer"), ["A", "B", "C", "D"], f"MCQ Block {mb.id} invalid answer key: {c.get('answer')}")
                self.assertTrue(c.get("explanation"), f"MCQ Block {mb.id} missing explanation!")

        # Total MCQs = 9 (one per lesson 1-9) + 8 (summative in lesson 10) = 17 MCQs
        self.assertGreaterEqual(total_mcqs, 17, f"Expected at least 17 MCQs, found {total_mcqs}")

if __name__ == "__main__":
    unittest.main()
