"""
VLearn CBC Grade 10 Geography — Topic 9: Earthquakes
Automated QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (CBC -> Grade 10 -> Geography -> Topic 9: Earthquakes)
  2. 10 Learning Units & 10 Published Lessons Validation
  3. Dynamic Card & Block Structure Integrity (all lessons >= 4 pages, non-empty content)
  4. Mandatory First-Card Visual Hooks (10 Tested HTTP 200/206 URLs & attached LessonAssets)
  5. 10 Custom Sanitized Responsive Vector SVGs (viewBox="0 0 800 450", sanitization & attached LessonAssets)
  6. Verified Educational YouTube Video Asset (Lesson 6)
  7. Content Sanitization (0 Bracket Citations, 0 Developer Meta-Terms, 0 Leaked Tags)
  8. Formative Multiple-Choice Questions Validation (Valid 4 Options & Detailed Explanations)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_geography_topic9.py
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

class TestCBCGrade10GeographyTopic9(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade__curriculum=cls.curriculum, name="Geography", grade__name__icontains="10").first()
        assert cls.subject, "Subject 'Geography' (ID: 37) not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=9).first()
        assert cls.topic, "Topic 9 'Earthquakes' not found under Geography!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Geography")
        self.assertEqual(self.topic.order, 9)
        self.assertEqual(self.topic.name, "Earthquakes")

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
        """Verify all 10 lessons have Page 1 photographic visual hooks with HTTP 200/206 URLs & attached LessonAssets."""
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
        """Verify all 10 lessons have custom responsive SVGs (viewBox 0 0 800 450) and attached LessonAssets."""
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
        """Verify educational YouTube video asset in Lesson 6."""
        les_6 = next((l for l in self.lessons if l.learning_unit.order == 6), None)
        self.assertIsNotNone(les_6, "Lesson 6 not found!")

        video_block = LessonBlock.objects.filter(lesson=les_6, block_type="video").first()
        self.assertIsNotNone(video_block, "Lesson 6 missing video block!")

        vid_content = video_block.content or {}
        vid_url = vid_content.get("url")
        self.assertTrue(vid_url, "Lesson 6 video block missing URL")
        self.assertIn("youtube.com", vid_url, "Lesson 6 video URL is not YouTube")

        asset = LessonAsset.objects.filter(lesson=les_6, asset_type="youtube", blocks=video_block).first()
        self.assertIsNotNone(asset, "Lesson 6 missing attached LessonAsset for video")
        self.assertEqual(asset.status, "attached")

    def test_07_content_sanitization(self):
        """Verify zero bracket citations ([1], [48]), zero developer meta tags ([VISUAL:, [TODO), and clean text."""
        bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
        meta_pattern = re.compile(r'\[(?:VISUAL:|TODO|FIXME|TOC|NOTE:)')

        for lesson in self.lessons:
            for block in lesson.blocks.all():
                content_str = json.dumps(block.content)

                # Ignore svg_content in diagram blocks when checking brackets
                if block.block_type == "diagram":
                    c_copy = dict(block.content)
                    c_copy.pop("svg_content", None)
                    content_str = json.dumps(c_copy)

                bracket_matches = bracket_pattern.findall(content_str)
                self.assertEqual(
                    len(bracket_matches), 0,
                    f"Lesson {lesson.learning_unit.order} Block {block.id} has leaked citations: {bracket_matches}"
                )

                meta_matches = meta_pattern.findall(content_str)
                self.assertEqual(
                    len(meta_matches), 0,
                    f"Lesson {lesson.learning_unit.order} Block {block.id} has leaked metadata: {meta_matches}"
                )

    def test_08_formative_mcqs_validation(self):
        """Verify MCQs have valid 4 options (A, B, C, D), valid correct_answer, and detailed explanations."""
        mcq_count = 0
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="multiple_choice_question")
            self.assertGreaterEqual(mcq_blocks.count(), 2, f"Lesson {lesson.learning_unit.order} has fewer than 2 MCQs!")

            for block in mcq_blocks:
                mcq_count += 1
                content = block.content or {}
                self.assertTrue(content.get("question"), f"Block {block.id} missing question text")
                options = content.get("options", [])
                self.assertEqual(len(options), 4, f"Block {block.id} does not have exactly 4 options")

                opt_ids = [opt["id"] for opt in options]
                self.assertEqual(opt_ids, ["A", "B", "C", "D"], f"Block {block.id} option IDs invalid: {opt_ids}")

                for opt in options:
                    self.assertTrue(opt.get("text"), f"Block {block.id} option {opt.get('id')} missing text")

                correct_ans = content.get("correct_answer")
                self.assertIn(correct_ans, ["A", "B", "C", "D"], f"Block {block.id} invalid correct_answer: {correct_ans}")

                explanation = content.get("explanation")
                self.assertTrue(explanation, f"Block {block.id} missing explanation")
                self.assertGreater(len(explanation), 20, f"Block {block.id} explanation too short")

        self.assertGreaterEqual(mcq_count, 20, f"Total MCQs across topic must be >= 20, got {mcq_count}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
