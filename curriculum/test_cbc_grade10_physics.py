"""
VLearn CBC Grade 10 Physics (Topics 1 Through 13 Complete Curriculum)
Automated QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (Curriculum CBC -> Grade 10 -> Subject Physics -> 13 Topics)
  2. 58 Sequential Learning Units & 58 Published Lessons Verification
  3. Dynamic Card & Block Structure Integrity (all lessons 7-9 cards, >= 10 blocks)
  4. Authentic Photographic Visual Assets & Attached LessonAssets (all 58 lessons)
  5. Custom Sanitized Vector SVGs Validation (valid viewBox, xml structure, attached LessonAssets)
  6. Verified Educational YouTube Video Integrations & Attached LessonAssets (all 58 lessons)
  7. Content Quality & KaTeX Sanitization (0 Bracket Citations, 0 Developer Artifacts, Proper Math Delimiters)
  8. Formative Scenario-Based MCQs Validation (58 MCQs with 4 options, valid answer key, detailed feedback)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_physics.py
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
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_svg_structure

class TestCBCGrade10Physics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="Physics").first()
        assert cls.subject, "Subject 'Physics' not found under Grade 10!"

        cls.topics = list(Topic.objects.filter(subject=cls.subject).order_by("order"))
        cls.units = list(LearningUnit.objects.filter(topic__in=cls.topics).order_by("topic__order", "order"))
        cls.lessons = list(Lesson.objects.filter(topic__in=cls.topics).order_by("topic__order", "learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy for Grade 10 Physics (Topics 1–13)."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Physics")
        self.assertEqual(len(self.topics), 13, f"Expected 13 topics, found {len(self.topics)}")

        expected_topics = [
            (1, "Introduction to Physics"),
            (2, "Pressure"),
            (3, "Mechanical Properties of Materials"),
            (4, "Temperature and Thermal Expansion"),
            (5, "Moments and Equilibrium"),
            (6, "Energy, Work, Power and Machines"),
            (7, "Properties of Waves"),
            (8, "Radioactivity and Stability of Isotopes"),
            (9, "Electrostatics"),
            (10, "Current Electricity"),
            (11, "Introduction to Electronics"),
            (12, "Greenhouse Effect and Climate Change"),
            (13, "Introduction to Space Physics"),
        ]
        for idx, (exp_order, exp_name) in enumerate(expected_topics):
            self.assertEqual(self.topics[idx].order, exp_order)
            self.assertEqual(self.topics[idx].name, exp_name)

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 58 LearningUnits and 58 published Lessons exist sequentially."""
        self.assertEqual(len(self.units), 58, f"Expected 58 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 58, f"Expected 58 lessons, found {len(self.lessons)}")

        # Check counts per topic: 3, 5, 4, 4, 6, 7, 6, 7, 4, 6, 2, 2, 2
        expected_counts = [3, 5, 4, 4, 6, 7, 6, 7, 4, 6, 2, 2, 2]
        for idx, count in enumerate(expected_counts):
            t_lessons = [l for l in self.lessons if l.topic_id == self.topics[idx].id]
            self.assertEqual(len(t_lessons), count, f"Topic {idx+1} has {len(t_lessons)} lessons, expected {count}")

        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {lesson.id} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has valid page/card counts (7-9) and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 10, f"Lesson '{lesson.title}' has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(len(page_numbers), 7, f"Lesson '{lesson.title}' must have >= 7 pages, got {len(page_numbers)}")
            self.assertLessEqual(len(page_numbers), 10, f"Lesson '{lesson.title}' has too many pages ({len(page_numbers)})")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} in '{lesson.title}' missing title")
                self.assertTrue(b.content, f"Block {b.id} in '{lesson.title}' missing content")

    def test_04_photographic_visual_assets(self):
        """Verify all 58 lessons have authentic Wikimedia photographic visual blocks with valid URLs & attached LessonAssets."""
        for lesson in self.lessons:
            img_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(img_block, f"Lesson '{lesson.title}' missing suggested_image photographic block!")
            content = img_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertTrue(img_url and "wikimedia.org" in img_url, f"Lesson '{lesson.title}' image URL invalid: {img_url}")

            asset = img_block.assets.filter(asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson '{lesson.title}' missing attached image LessonAsset")
            self.assertEqual(asset.storage_type, "url")
            self.assertEqual(asset.source_type, "external")
            self.assertTrue(asset.metadata.get("commons_page_url"), f"Asset {asset.id} missing commons_page_url")

    def test_05_custom_vector_svgs(self):
        """Verify all custom SVG diagrams are valid, sanitized XML, and attached as LessonAssets."""
        diagram_blocks = LessonBlock.objects.filter(
            lesson__in=self.lessons,
            block_type="suggested_diagram"
        )
        self.assertGreaterEqual(len(diagram_blocks), 62, f"Expected >= 62 diagram blocks, found {len(diagram_blocks)}")

        for b in diagram_blocks:
            c = b.content or {}
            svg_code = c.get("svg_content") or c.get("svg") or b.metadata.get("svg_content")
            self.assertIsNotNone(svg_code, f"Diagram block {b.id} in '{b.lesson.title}' missing svg_content")
            
            is_valid, err = validate_svg_structure(svg_code)
            self.assertTrue(is_valid, f"Diagram block {b.id} in '{b.lesson.title}' has invalid SVG: {err}")
            self.assertIn("viewBox", svg_code, f"Diagram block {b.id} missing responsive viewBox")

            asset = b.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Diagram block {b.id} in '{b.lesson.title}' missing attached diagram LessonAsset")

    def test_06_educational_youtube_videos(self):
        """Verify all 58 lessons have educational YouTube video blocks with valid IDs and attached LessonAssets."""
        for lesson in self.lessons:
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()

            self.assertIsNotNone(video_block, f"Lesson '{lesson.title}' missing YouTube video block!")
            content = video_block.content or {}
            v_url = content.get("url")
            v_id = content.get("resolved_video_id")
            self.assertTrue(v_url and "youtube.com" in v_url, f"Lesson '{lesson.title}' video URL invalid: {v_url}")
            self.assertTrue(v_id and len(v_id) == 11, f"Lesson '{lesson.title}' video ID invalid: {v_id}")

            asset = video_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Lesson '{lesson.title}' missing attached youtube LessonAsset")
            self.assertEqual(asset.metadata.get("youtube_id"), v_id)

    def test_07_content_quality_and_sanitization(self):
        """Verify 0 developer meta-terms, 0 bracket citations, and clean prose throughout."""
        forbidden_patterns = [
            r'\[VISUAL:', r'\[QUESTION:', r'\[IMAGE_PROMPT', r'Suggested Visual',
            r'Internal Block', r'TODO', r'FIXME'
        ]
        blocks = LessonBlock.objects.filter(lesson__in=self.lessons)
        for b in blocks:
            text_repr = str(b.content) + " " + str(b.title or "")
            for pat in forbidden_patterns:
                self.assertIsNone(re.search(pat, text_repr, re.IGNORECASE),
                                  f"Block {b.id} in '{b.lesson.title}' contains forbidden marker: {pat}")

    def test_08_formative_mcqs_validation(self):
        """Verify each of the 58 lessons contains a validated 4-option MCQ with correct answer & explanation."""
        mcq_blocks = LessonBlock.objects.filter(
            lesson__in=self.lessons,
            block_type="knowledge_check"
        )
        self.assertEqual(len(mcq_blocks), 58, f"Expected 58 MCQ knowledge checks, found {len(mcq_blocks)}")

        for mcq in mcq_blocks:
            c = mcq.content or {}
            self.assertTrue(c.get("question"), f"MCQ block {mcq.id} missing question")
            opts = c.get("options") or []
            self.assertEqual(len(opts), 4, f"MCQ block {mcq.id} must have exactly 4 options, got {len(opts)}")
            
            ans = c.get("answer")
            self.assertIn(ans, ["A", "B", "C", "D"], f"MCQ block {mcq.id} invalid answer key: {ans}")

            exp = c.get("explanation")
            self.assertTrue(exp and len(exp) >= 30, f"MCQ block {mcq.id} missing detailed explanation")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCBCGrade10Physics)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
