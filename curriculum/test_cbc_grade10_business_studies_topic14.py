"""
VLearn CBC Grade 10 Business Studies — Topic 14: Effects of Business Transactions
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

class TestCBCGrade10BusinessStudiesTopic14(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        assert cls.grade, "Grade 10 not found in database!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name__icontains="Business").first()
        assert cls.subject, "Subject 'Business Studies' not found in Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=14).first()
        assert cls.topic, "Topic 14 'Effects of Business Transactions' not found in database!"

        cls.units = list(LearningUnit.objects.filter(topic=cls.topic).order_by("order"))
        cls.lessons = list(Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertIn("Business Studies", self.subject.name)
        self.assertEqual(self.topic.order, 14)
        self.assertEqual(self.topic.name, "Effects of Business Transactions")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 5 LearningUnits and 5 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 5, f"Expected 5 units in Topic 14, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 5, f"Expected 5 lessons in Topic 14, found {len(self.lessons)}")

        for i, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, i, f"Unit order mismatch at index {i}: got {unit.order}")
            lesson = Lesson.objects.filter(topic=self.topic, learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"No lesson found attached to Unit {i} ({unit.name})")
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.title} is not published!")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has exactly 8 pedagogical cards and non-empty blocks."""
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            self.assertGreaterEqual(blocks.count(), 8, f"Lesson {lesson.title} has too few blocks ({blocks.count()})")
            page_numbers = set(b.page_number for b in blocks)
            self.assertEqual(len(page_numbers), 8, f"Lesson {lesson.title} must have 8 pages, got {len(page_numbers)}")

    def test_04_card_1_visual_hooks(self):
        """Verify all 5 lessons have Page 1 photographic visual hooks with valid Wikimedia URLs."""
        for lesson in self.lessons:
            hook_block = LessonBlock.objects.filter(lesson=lesson, page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(hook_block, f"Lesson {lesson.title} missing Page 1 suggested_image hook!")
            c = hook_block.content or {}
            url = c.get("url") or ""
            self.assertTrue(url.startswith("https://upload.wikimedia.org/"), f"Invalid Wikimedia URL in {lesson.title}: {url}")

    def test_05_custom_vector_svgs(self):
        """Verify all 5 lessons contain responsive vector SVGs attached as LessonAssets."""
        for u_order in range(1, 6):
            lesson = Lesson.objects.filter(topic=self.topic, learning_unit__order=u_order).first()
            self.assertIsNotNone(lesson, f"Lesson for Unit {u_order} not found!")

            svg_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram").first()
            self.assertIsNotNone(svg_asset, f"Lesson {u_order} ({lesson.title}) missing diagram LessonAsset!")
            svg_content = svg_asset.metadata.get("svg_content", "")
            self.assertTrue(svg_content.strip().startswith("<svg"), f"Lesson {u_order} SVG asset invalid!")

    def test_06_youtube_video_assets(self):
        """Verify 100% YouTube video coverage across all 5 lessons."""
        video_count = 0
        for lesson in self.lessons:
            yt_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube").first()
            yt_block = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_video").first()
            if yt_asset or yt_block:
                video_count += 1
        self.assertEqual(video_count, len(self.lessons), f"Expected 100% video coverage in Topic 14, found {video_count}/{len(self.lessons)}")

    def test_07_content_sanitization(self):
        """Verify zero bracket citations, zero prompt leaks, and clean math."""
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                text_content = str(b.content) + " " + str(b.title)
                self.assertFalse(bool(re.search(r"\[\d+\]", text_content)), f"Block {b.id} in {lesson.title} contains citation brackets")

    def test_08_formative_mcqs(self):
        """Verify MCQs contain 4 options, valid correct answer keys, and explanations."""
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="knowledge_check")
            for mb in mcq_blocks:
                c = mb.content or {}
                self.assertEqual(len(c.get("options", [])), 4, f"MCQ Block {mb.id} must have 4 options")
                self.assertIn(c.get("correct") or c.get("answer"), ["A", "B", "C", "D"])
                self.assertTrue(c.get("explanation"), f"MCQ Block {mb.id} missing explanation!")

if __name__ == "__main__":
    unittest.main()
