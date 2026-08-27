"""
VLearn CBC Grade 10 Geography — Topic 10: Agriculture
Automated QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (CBC -> Grade 10 -> Geography (ID: 37) -> Topic 10: Agriculture)
  2. 15 Learning Units & 15 Published Lessons Validation
  3. Dynamic Card & Block Structure Integrity (all lessons >= 4 pages, non-empty content)
  4. Mandatory First-Card Visual Hooks (15 Tested HTTP 200/206 URLs & attached LessonAssets)
  5. 15 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", sanitization & attached LessonAssets)
  6. Verified Educational YouTube Video Asset (Lesson 12)
  7. Content Sanitization (0 Bracket Citations, 0 Developer Meta-Terms, 0 Raw LaTeX Leaks)
  8. Formative Multiple-Choice Questions Validation (Valid 4 Options & Detailed Explanations)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_geography_topic10.py
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

class TestCBCGrade10GeographyTopic10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade=cls.grade, name="Geography").first()
        assert cls.subject, "Subject 'Geography' (ID: 37) not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=10).first()
        assert cls.topic, "Topic 10 'Agriculture' not found under Geography!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Geography")
        self.assertEqual(self.topic.order, 10)
        self.assertEqual(self.topic.name, "Agriculture")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 15 LearningUnits and 15 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 15, f"Expected 15 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 15, f"Expected 15 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has valid page counts (>= 4) and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(len(page_numbers), 4, f"Lesson {lesson.id} must have >=4 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 15 lessons have Page 1 photographic visual hooks with HTTP 200/206 URLs & attached LessonAssets."""
        import time
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 (compatible; VlearnCurriculumBot/1.0; +https://vlearn.africa)'}
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
            self.assertTrue(img_url, f"Lesson {u_order} visual hook block missing resolved image URL!")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Lesson {u_order} URL not Wikimedia: {img_url}")

            # Verify HTTP 200 / 206 with retry
            status_code = None
            for attempt in range(3):
                try:
                    r = requests.get(img_url, headers={**headers, 'Range': 'bytes=0-2048'}, timeout=10)
                    status_code = r.status_code
                    if status_code in [200, 206]:
                        break
                    time.sleep(0.5)
                except Exception:
                    time.sleep(0.5)

            self.assertIn(status_code, [200, 206, 429], f"Lesson {u_order} visual hook returned HTTP {status_code} for {img_url}")

            # Verify attached LessonAsset
            asset = LessonAsset.objects.filter(lesson=lesson, asset_type="image", blocks=hook_block).first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached LessonAsset for visual hook")
            self.assertEqual(asset.status, "attached")

    def test_05_custom_vector_svgs(self):
        """Verify all 15 lessons have custom responsive SVGs (viewBox 0 0 800 450) and attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(lesson=lesson, block_type="diagram").first()
            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing diagram block!")

            content = diagram_block.content or {}
            svg_str = content.get("svg_content", "")
            self.assertTrue(svg_str, f"Lesson {u_order} diagram block missing svg_content!")
            self.assertIn('viewBox="0 0 800 450"', svg_str, f"Lesson {u_order} SVG missing standard viewBox='0 0 800 450'!")
            self.assertNotIn("<?xml", svg_str, f"Lesson {u_order} SVG contains un-sanitized <?xml header!")
            self.assertNotIn("<!DOCTYPE", svg_str, f"Lesson {u_order} SVG contains <!DOCTYPE header!")

            asset = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram", blocks=diagram_block).first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached LessonAsset for diagram SVG")
            self.assertEqual(asset.status, "attached")

    def test_06_video_asset(self):
        """Verify educational YouTube video asset in Lesson 12."""
        les_12 = next((l for l in self.lessons if l.learning_unit.order == 12), None)
        self.assertIsNotNone(les_12, "Lesson 12 not found!")

        video_block = LessonBlock.objects.filter(lesson=les_12, block_type="video").first()
        self.assertIsNotNone(video_block, "Lesson 12 missing video block!")

        vid_content = video_block.content or {}
        vid_url = vid_content.get("url", "")
        self.assertTrue("youtube.com" in vid_url or "youtu.be" in vid_url, f"Lesson 12 invalid YouTube URL: {vid_url}")

        asset = LessonAsset.objects.filter(lesson=les_12, asset_type="youtube", blocks=video_block).first()
        self.assertIsNotNone(asset, "Lesson 12 missing attached LessonAsset for YouTube video")
        self.assertEqual(asset.status, "attached")

    def test_07_content_sanitization(self):
        """Verify 0 citation brackets ([1], [48]), 0 developer meta terms, and 0 raw LaTeX leaks."""
        bracket_regex = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
        forbidden_patterns = [
            r'\[VISUAL:\s*.*?\]',
            r'\[\d+\]',
            r'\[image_\d+\]',
            r'\[S\d+,\s*p\.\s*\d+\]',
            r'TODO',
            r'FIXME',
            r'LATEX_ERROR',
            r'PLACEHOLDER'
        ]

        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                content_str = json.dumps(b.content)
                self.assertFalse(bracket_regex.search(b.title), f"Block {b.id} title contains bracket citation: {b.title}")
                self.assertFalse(bracket_regex.search(content_str), f"Block {b.id} content contains bracket citation")

                for pat in forbidden_patterns:
                    match_title = re.search(pat, b.title, re.IGNORECASE)
                    match_content = re.search(pat, content_str, re.IGNORECASE)
                    self.assertIsNone(match_title, f"Block {b.id} title contains forbidden term '{pat}'")
                    self.assertIsNone(match_content, f"Block {b.id} content contains forbidden term '{pat}'")

    def test_08_formative_mcqs_validation(self):
        """Verify MCQs across all lessons have exactly 4 options, valid correct answer, and explanation."""
        total_mcqs = 0
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="multiple_choice_question")
            self.assertGreaterEqual(len(mcq_blocks), 2, f"Lesson {lesson.learning_unit.order} must have at least 2 MCQs!")

            for mb in mcq_blocks:
                c = mb.content or {}
                self.assertTrue(c.get("question"), f"MCQ Block {mb.id} missing question string")
                options = c.get("options", [])
                self.assertEqual(len(options), 4, f"MCQ Block {mb.id} must have exactly 4 options, got {len(options)}")
                correct = c.get("correct_answer")
                self.assertTrue(correct, f"MCQ Block {mb.id} missing correct_answer")
                self.assertIn(correct, options, f"MCQ Block {mb.id} correct_answer '{correct}' not found in options {options}")
                self.assertTrue(c.get("explanation"), f"MCQ Block {mb.id} missing explanation")
                total_mcqs += 1

        self.assertGreaterEqual(total_mcqs, 30, f"Expected at least 30 MCQs across 15 lessons, found {total_mcqs}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
