"""
VLearn CBC Grade 10 CRE — Topic 4.2: Human Rights (Non-discrimination)
Automated Verification and Integrity Test Suite
"""

import os
import sys
import re
import unittest
import django

sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


class TestCBCGrade10CRETopic4_2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name__icontains="CRE").first()
        assert cls.subject, "Subject 'CRE' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=20).first()
        assert cls.topic, "Topic 4.2 (Order: 20) not found under Grade 10 CRE!"

        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertIn("10", self.grade.name)
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.id, 46)
        self.assertIn("CRE", self.subject.name)
        self.assertEqual(self.topic.order, 20)
        self.assertIn("Human Rights (Non-discrimination)", self.topic.name)

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 8 LearningUnits and 8 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 8, f"Expected 8 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 8, f"Expected 8 lessons, found {len(self.lessons)}")

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
            self.assertEqual(len(blocks), 13, f"Lesson {lesson.id} expected 13 blocks, got ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertEqual(len(page_numbers), 6, f"Lesson {lesson.id} must have exactly 6 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 8 lessons have Page 1 photographic visual hooks with Wikimedia URLs & attached LessonAssets."""
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
        """Verify all 8 lessons have custom sanitized responsive vector SVGs with viewBox and attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diag_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=3,
                block_type="suggested_diagram"
            ).first()
            self.assertIsNotNone(diag_block, f"Lesson {u_order} missing suggested_diagram block on Card 3!")

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
        """Verify all 8 lessons have curated educational YouTube video blocks and attached LessonAssets."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=5,
                block_type="suggested_video"
            ).first()
            self.assertIsNotNone(video_block, f"Lesson {u_order} missing suggested_video block on Card 5!")

            content = video_block.content or {}
            v_url = content.get("url")
            self.assertTrue(v_url and "youtube.com" in v_url, f"Lesson {u_order} video URL invalid: {v_url}")

            asset = video_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} video missing attached LessonAsset!")

    def test_07_content_sanitization(self):
        """Verify 0 bracket citations and 0 internal visual/passage tags in block contents."""
        bracket_cite_pattern = re.compile(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        internal_tag_pattern = re.compile(r'\[(VISUAL|BIBLE PASSAGE|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|REAL WORLD APPLICATION|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE)[^\]]*\]', re.IGNORECASE)

        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                content_str = str(b.content)
                # Ignore SVG content for bracket checks
                if b.block_type == "suggested_diagram":
                    continue
                match_c = bracket_cite_pattern.search(content_str)
                self.assertIsNone(match_c, f"Lesson {lesson.id} Block {b.id} contains citation: {match_c.group(0) if match_c else ''}")
                match_t = internal_tag_pattern.search(content_str)
                self.assertIsNone(match_t, f"Lesson {lesson.id} Block {b.id} contains internal tag: {match_t.group(0) if match_t else ''}")

    def test_08_mcq_structure_and_validity(self):
        """Verify all 8 lessons have valid 4-option MCQs with valid answer keys and explanations."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            mcq_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=6,
                block_type="knowledge_check"
            ).first()
            self.assertIsNotNone(mcq_block, f"Lesson {u_order} missing Card 6 MCQ block!")

            content = mcq_block.content or {}
            question = content.get("question")
            options = content.get("options")
            answer = content.get("answer")
            explanation = content.get("explanation")

            self.assertTrue(question, f"Lesson {u_order} MCQ missing question")
            self.assertEqual(len(options), 4, f"Lesson {u_order} MCQ must have 4 options, got {len(options) if options else 0}")
            self.assertIn(answer, ["A", "B", "C", "D"], f"Lesson {u_order} MCQ answer key invalid: {answer}")
            self.assertTrue(explanation, f"Lesson {u_order} MCQ missing explanation")


if __name__ == "__main__":
    unittest.main()
