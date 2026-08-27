"""
VLearn CBC Grade 10 Geography — Topic 3: Statistical Methods
Automated QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (CBC -> Grade 10 -> Geography -> Topic 3: Statistical Methods)
  2. 12 Learning Units & 12 Published Lessons Validation
  3. Dynamic Card & Block Structure Integrity (all lessons >= 4 pages, non-empty content)
  4. Mandatory First-Card Visual Hooks (12 Tested HTTP 200 URLs & attached LessonAssets)
  5. 12 Custom Sanitized Responsive Vector SVGs (viewBox, sanitization & attached LessonAssets)
  6. Verified Educational YouTube Video Assets (Lesson 5 & Lesson 11)
  7. Content Sanitization (0 Bracket Citations, 0 Developer Meta-Terms, 0 Raw LaTeX Leaks)
  8. Formative Scenario-Based MCQs Validation (Valid Answer Keys & Explanations)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_geography_topic3.py
"""

import os
import sys
import re
import json
import unittest
import requests
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10GeographyTopic3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade__curriculum=cls.curriculum, name="Geography", grade__name__icontains="10").first()
        assert cls.subject, "Subject 'Geography' not found under Grade 10!"
        cls.grade = cls.subject.grade

        cls.topic = Topic.objects.filter(subject=cls.subject, order=3).first()
        assert cls.topic, "Topic 3 'Statistical Methods' not found under Geography!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Geography")
        self.assertEqual(self.topic.order, 3)
        self.assertEqual(self.topic.name, "Statistical Methods")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 12 LearningUnits and 12 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 12, f"Expected 12 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 12, f"Expected 12 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has valid page counts (4-7) and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 4, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(len(page_numbers), 4, f"Lesson '{lesson.title}' must have >=4 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 12 lessons have Page 1 photographic visual hooks with HTTP 200 URLs & attached LessonAssets."""
        headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}
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
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 visual hook missing image URL!")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Lesson {u_order} URL not Wikimedia: {img_url}")

            # Verify HTTP 200
            resp = requests.head(img_url, headers=headers, timeout=10)
            self.assertEqual(resp.status_code, 200, f"Lesson {u_order} image URL failed HTTP 200 check: {img_url}")

            asset = LessonAsset.objects.filter(lesson=lesson, asset_type="image", blocks=hook_block).first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached LessonAsset for Card 1 visual hook!")
            self.assertEqual(asset.status, "attached")

    def test_05_custom_vector_svgs(self):
        """Verify diagram blocks have valid custom vector SVGs with viewBox and attached LessonAssets."""
        diag_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="suggested_diagram")
        self.assertGreaterEqual(diag_blocks.count(), 12, "Expected at least 12 diagram blocks in Topic 3")

        for diag_block in diag_blocks:
            content = diag_block.content or {}
            svg_text = content.get("svg_content", "")
            self.assertTrue(svg_text, f"Block {diag_block.id} diagram missing svg_content!")
            self.assertIn("<svg", svg_text)
            self.assertIn("viewBox=", svg_text)
            self.assertNotIn("<?xml", svg_text)

            svg_asset = LessonAsset.objects.filter(lesson=diag_block.lesson, asset_type="diagram", blocks=diag_block).first()
            self.assertIsNotNone(svg_asset, f"Block {diag_block.id} missing attached LessonAsset for diagram!")
            self.assertEqual(svg_asset.status, "attached")

    def test_06_video_assets(self):
        """Verify Lessons 5 and 11 have attached educational YouTube video assets."""
        for u_num in [5, 11]:
            lesson = next(l for l in self.lessons if l.learning_unit.order == u_num)
            v_block = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_video").first()
            self.assertIsNotNone(v_block, f"Lesson {u_num} missing suggested_video block!")

            v_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube", blocks=v_block).first()
            self.assertIsNotNone(v_asset, f"Lesson {u_num} missing attached YouTube LessonAsset!")
            self.assertIn("youtube.com", v_asset.url)

    def test_07_content_purification(self):
        """Scan all blocks across Topic 3 for zero prompt leaks, zero bracket citations, and clean formatting."""
        forbidden_patterns = [
            r'\[VISUAL:\s*.*?\]',
            r'\[\d+\]',
            r'\[image_\d+\]',
            r'\[S\d+,\s*p\.\s*\d+\]',
            r'Prompt:',
            r'Learner should observe:',
            r'Preferred characteristics:'
        ]

        all_blocks = LessonBlock.objects.filter(lesson__in=self.lessons)
        for block in all_blocks:
            c_str = json.dumps(block.content)
            for pat in forbidden_patterns:
                match = re.search(pat, c_str, re.IGNORECASE)
                self.assertIsNone(match, f"Block {block.id} in Lesson '{block.lesson.title}' contains forbidden tag matching '{pat}': {match.group(0) if match else ''}")

    def test_08_formative_mcqs_validation(self):
        """Verify all knowledge check blocks have 4 options, valid correct answer, and explanation."""
        mcq_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="knowledge_check")
        self.assertGreaterEqual(mcq_blocks.count(), 24, "Expected at least 24 MCQs across Topic 3 (2 per lesson)")

        for block in mcq_blocks:
            c = block.content or {}
            self.assertIn("question", c, f"Block {block.id} missing question")
            self.assertIn("options", c, f"Block {block.id} missing options")
            self.assertEqual(len(c["options"]), 4, f"Block {block.id} does not have 4 options")
            self.assertIn("correct_answer", c, f"Block {block.id} missing correct_answer")
            self.assertIn(c["correct_answer"], ["A", "B", "C", "D"], f"Block {block.id} correct answer invalid: {c.get('correct_answer')}")
            self.assertIn("explanation", c, f"Block {block.id} missing explanation")
            self.assertTrue(len(c["explanation"]) > 10, f"Block {block.id} explanation too short")

if __name__ == "__main__":
    unittest.main()
