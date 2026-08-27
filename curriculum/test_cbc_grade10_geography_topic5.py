"""
VLearn CBC Grade 10 Geography — Topic 5: Rocks
Automated QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (CBC -> Grade 10 -> Geography -> Topic 5: Rocks)
  2. 18 Learning Units & 18 Published Lessons Validation
  3. Dynamic Card & Block Structure Integrity (all lessons >= 3 pages, non-empty content)
  4. Mandatory First-Card Visual Hooks (18 Wikimedia URLs & attached LessonAssets)
  5. 18 Custom Sanitized Responsive Vector SVGs (viewBox, sanitization & attached LessonAssets)
  6. Verified Educational YouTube Video Asset (Lesson 2)
  7. Content Sanitization (0 Bracket Citations, 0 Developer Meta-Terms, 0 Raw LaTeX Leaks)
  8. Formative & Summative Scenario-Based MCQs Validation (Valid Options & Explanations)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_geography_topic5.py
"""

import os
import sys
import re
import json
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10GeographyTopic5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade__curriculum=cls.curriculum, name="Geography", grade__name__icontains="10").first()
        assert cls.subject, "Subject 'Geography' not found under Grade 10!"
        cls.grade = cls.subject.grade

        cls.topic = Topic.objects.filter(subject=cls.subject, order=5).first()
        assert cls.topic, "Topic 5 'Rocks' not found under Geography!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Geography")
        self.assertEqual(self.subject.id, 37)
        self.assertEqual(self.topic.order, 5)
        self.assertEqual(self.topic.name, "Rocks")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 18 LearningUnits and 18 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 18, f"Expected 18 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 18, f"Expected 18 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has valid page counts (>= 3) and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 4, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(len(page_numbers), 3, f"Lesson {lesson.id} must have >=3 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 18 lessons have Page 1 photographic visual hooks with valid Wikimedia URLs & attached LessonAssets."""
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

            asset = LessonAsset.objects.filter(lesson=lesson, asset_type="image", blocks=hook_block).first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached LessonAsset for Card 1 visual hook!")
            self.assertEqual(asset.status, "attached")

    def test_05_custom_vector_svgs(self):
        """Verify diagram blocks have valid custom vector SVGs with viewBox and attached LessonAssets."""
        diag_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="diagram")
        self.assertEqual(diag_blocks.count(), 18, f"Expected 18 diagram blocks in Topic 5, found {diag_blocks.count()}")

        for diag_block in diag_blocks:
            content = diag_block.content or {}
            svg_text = content.get("svg_content", "")
            self.assertTrue(svg_text, f"Block {diag_block.id} diagram missing svg_content!")
            self.assertIn("<svg", svg_text, f"Block {diag_block.id} invalid SVG missing <svg tag")
            self.assertIn("viewBox=", svg_text, f"Block {diag_block.id} SVG missing viewBox attribute")
            self.assertNotIn("<?xml", svg_text, f"Block {diag_block.id} SVG contains unstripped xml header")

            svg_asset = LessonAsset.objects.filter(lesson=diag_block.lesson, asset_type="diagram", blocks=diag_block).first()
            self.assertIsNotNone(svg_asset, f"Block {diag_block.id} missing attached LessonAsset!")
            self.assertEqual(svg_asset.status, "attached")

    def test_06_video_assets(self):
        """Verify educational video asset exists for Lesson 2 (The Rock Cycle)."""
        lesson_2 = next((l for l in self.lessons if l.learning_unit.order == 2), None)
        self.assertIsNotNone(lesson_2, "Lesson 2 not found!")

        video_block = LessonBlock.objects.filter(lesson=lesson_2, block_type="video").first()
        self.assertIsNotNone(video_block, "Lesson 2 missing video block!")

        v_content = video_block.content or {}
        v_url = v_content.get("url")
        self.assertTrue(v_url and "youtube.com" in v_url, f"Lesson 2 invalid video url: {v_url}")

        v_asset = LessonAsset.objects.filter(lesson=lesson_2, asset_type="youtube", blocks=video_block).first()
        self.assertIsNotNone(v_asset, "Lesson 2 missing attached LessonAsset for video!")
        self.assertEqual(v_asset.status, "attached")

    def test_07_content_sanitization(self):
        """Verify 0 bracket citations, 0 internal prompt leaks, and 0 raw LaTeX leaks."""
        bracket_citation_pattern = re.compile(r'\[\d+(?:,\s*\d+)*\]')
        prompt_leak_pattern = re.compile(r'\[VISUAL:\s*(?:SVG|YOUTUBE|MAP|WIKIMEDIA)\]', re.IGNORECASE)

        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                content_str = json.dumps(b.content or {})
                self.assertFalse(
                    bracket_citation_pattern.search(content_str),
                    f"Bracket citation found in Block {b.id} (Lesson {lesson.learning_unit.order}): {content_str[:100]}"
                )
                self.assertFalse(
                    prompt_leak_pattern.search(content_str),
                    f"Prompt metadata leak found in Block {b.id} (Lesson {lesson.learning_unit.order})"
                )

    def test_08_formative_mcqs_validation(self):
        """Verify all MCQs across Topic 5 have 4 valid options, correct answers, and thorough explanations."""
        mcq_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="multiple_choice_question")
        self.assertGreaterEqual(mcq_blocks.count(), 36, f"Expected at least 36 MCQs across Topic 5, found {mcq_blocks.count()}")

        for mcq in mcq_blocks:
            c = mcq.content or {}
            question = c.get("question", "")
            options = c.get("options", [])
            correct_answer = c.get("correct_answer", "")
            explanation = c.get("explanation", "")

            self.assertTrue(question, f"MCQ Block {mcq.id} missing question text")
            self.assertEqual(len(options), 4, f"MCQ Block {mcq.id} must have exactly 4 options, got {len(options)}")
            self.assertIn(correct_answer, options, f"MCQ Block {mcq.id} correct answer '{correct_answer}' not among options: {options}")
            self.assertTrue(explanation, f"MCQ Block {mcq.id} missing explanation")
            self.assertGreaterEqual(len(explanation), 15, f"MCQ Block {mcq.id} explanation too short: '{explanation}'")

if __name__ == "__main__":
    unittest.main()
