"""
VLearn CBC Grade 10 Business Studies — Topic 4: Banking
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

class TestCBCGrade10BusinessStudiesTopic4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first() or Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="Business Studies").first()
        assert cls.subject, "Subject 'Business Studies' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=4).first()
        assert cls.topic, "Topic 4 'Banking' not found under Business Studies!"

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "Business Studies")
        self.assertEqual(self.topic.order, 4)
        self.assertEqual(self.topic.name, "Banking")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 5 LearningUnits and 5 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 5, f"Expected 5 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 5, f"Expected 5 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has exactly 8 pedagogical cards (pages) and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 10, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number)))
            self.assertEqual(len(page_numbers), 8, f"Lesson {lesson.id} must have exactly 8 pages, got {len(page_numbers)}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 5 lessons have Page 1 photographic visual hooks with valid Wikimedia URLs."""
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
        """Verify all 5 lessons contain sanitized, responsive vector SVGs attached as LessonAssets."""
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
            self.assertIn("viewBox", svg_text, f"Lesson {u_order} SVG missing viewBox!")

            # Verify LessonAsset attachment
            asset = diagram_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} diagram block missing attached LessonAsset!")

    def test_06_youtube_video_assets(self):
        """Verify high YouTube video coverage (100% across all 5 lessons)."""
        video_count = 0
        for lesson in self.lessons:
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_video"
            ).first()
            if video_block:
                content = video_block.content or {}
                yt_id = content.get("youtube_id")
                if yt_id:
                    video_count += 1
                    asset = video_block.assets.filter(asset_type="youtube").first()
                    self.assertIsNotNone(asset, f"Lesson {lesson.learning_unit.order} video block missing attached LessonAsset!")

        coverage = (video_count / len(self.lessons)) * 100
        print(f"[*] Topic 4 Video Coverage: {video_count}/{len(self.lessons)} ({coverage:.1f}%)")
        self.assertEqual(coverage, 100.0, f"Topic 4 video coverage below 100%: {coverage}%")

    def test_07_content_sanitization(self):
        """Verify zero bracket citations ([37], [119]), zero developer prompt leakage, and clean math."""
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                text_content = str(b.content) + " " + (b.title or "")
                # Check for raw citation brackets like [37], [119]
                self.assertFalse(bool(re.search(r'\[\d+\]', text_content)), f"Block {b.id} contains citation brackets: {text_content[:80]}")
                # Check for developer prompt leaks
                for leak in ["Prompt:", "JSON Payload", "block_type:", "component_order:"]:
                    self.assertNotIn(leak, text_content, f"Block {b.id} contains prompt leak '{leak}'")

    def test_08_formative_mcqs(self):
        """Verify MCQs contain 4 options, valid correct answer keys, and explanations."""
        mcq_count = 0
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="knowledge_check")
            for mb in mcq_blocks:
                mcq_count += 1
                c = mb.content or {}
                self.assertTrue(c.get("question"), f"MCQ Block {mb.id} missing question!")
                options = c.get("options", [])
                self.assertEqual(len(options), 4, f"MCQ Block {mb.id} must have 4 options, got {len(options)}")
                correct = c.get("correct") or c.get("answer")
                self.assertIn(correct, ["A", "B", "C", "D"], f"MCQ Block {mb.id} has invalid correct answer: {correct}")
                self.assertTrue(c.get("explanation"), f"MCQ Block {mb.id} missing explanation!")

        self.assertGreaterEqual(mcq_count, 10, f"Expected >= 10 MCQs in Topic 4, found {mcq_count}")

if __name__ == "__main__":
    unittest.main()
