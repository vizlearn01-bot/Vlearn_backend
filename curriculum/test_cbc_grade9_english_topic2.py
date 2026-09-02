"""
VLearn CBC Grade 9 English — Topic 2: Reading and Literature
Comprehensive Verification & Unit Test Suite
"""

import os
import sys
import re
import unittest
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestCBCGrade9EnglishTopic2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=18).first()
        if not cls.grade:
            cls.grade = Grade.objects.filter(name="Grade 9", curriculum__name="CBC").first()
        assert cls.grade is not None, "Grade 9 (ID 18) must exist."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        assert cls.subject is not None, "Subject 'English' must exist in Grade 9."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=2).first()
        assert cls.topic is not None, "Topic 2 'Reading and Literature' must exist in Subject 'English'."

    def test_topic_structure(self):
        """Test topic naming, description, and order."""
        self.assertEqual(self.topic.order, 2)
        self.assertEqual(self.topic.name, "Reading and Literature")
        self.assertIn("fluency", self.topic.description.lower())
        self.assertIn("proverbs", self.topic.description.lower())

    def test_all_7_units_exist(self):
        """Test that all 7 learning units exist in correct sequence."""
        units = list(LearningUnit.objects.filter(topic=self.topic).order_by("order"))
        self.assertEqual(len(units), 7, f"Expected 7 units, found {len(units)}")

        expected_titles = [
            "Reading Fluency and Comprehension Strategies",
            "Visualising, Summarising, and Note-Making",
            "Oral Literature: Riddles, Proverbs, and Tongue Twisters",
            "Analysing Simple and Oral Poems",
            "Play Structure, Setting, and Plot",
            "Characterisation and Conflict",
            "Themes, Style, and Lessons Learnt"
        ]

        for i, (unit, expected_title) in enumerate(zip(units, expected_titles), start=1):
            self.assertEqual(unit.order, i)
            self.assertEqual(unit.name, expected_title)

    def test_lessons_published_and_linked(self):
        """Test that each unit has one published lesson."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lessons = Lesson.objects.filter(learning_unit=unit)
            self.assertEqual(lessons.count(), 1, f"Unit {unit.order} must have exactly 1 lesson.")
            lesson = lessons.first()
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertEqual(lesson.topic, self.topic)
            self.assertEqual(lesson.immutable_metadata["grade"], "Grade 9")
            self.assertEqual(lesson.immutable_metadata["subject"], "English")
            self.assertEqual(lesson.immutable_metadata["topic_order"], 2)

    def test_each_lesson_has_6_atomic_pages(self):
        """Verify each lesson has exactly 6 distinct page numbers (1 to 6)."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson '{lesson.title}' must have pages 1 through 6.")

    def test_pedagogical_block_structure_per_page(self):
        """Verify required component types on each page for all 7 lessons."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)

            # Page 1: Discovery & Objectives
            p1_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by('component_order')]
            self.assertIn("suggested_image", p1_types, f"Lesson '{lesson.title}' Page 1 missing suggested_image")
            self.assertIn("learning_goal", p1_types, f"Lesson '{lesson.title}' Page 1 missing learning_goal")
            self.assertIn("concept_explanation", p1_types, f"Lesson '{lesson.title}' Page 1 missing concept_explanation")

            # Page 2: Core Concepts & Terminology
            p2_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=2).order_by('component_order')]
            self.assertIn("definition_card", p2_types, f"Lesson '{lesson.title}' Page 2 missing definition_card")
            self.assertIn("comparison_table", p2_types, f"Lesson '{lesson.title}' Page 2 missing comparison_table")

            # Page 3: Model & Structured Analysis
            p3_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=3).order_by('component_order')]
            self.assertIn("suggested_diagram", p3_types, f"Lesson '{lesson.title}' Page 3 missing suggested_diagram")
            self.assertIn("worked_example", p3_types, f"Lesson '{lesson.title}' Page 3 missing worked_example")

            # Page 4: Media Integration & Active Lab
            p4_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=4).order_by('component_order')]
            self.assertIn("suggested_video", p4_types, f"Lesson '{lesson.title}' Page 4 missing suggested_video")
            self.assertIn("real_world_example", p4_types, f"Lesson '{lesson.title}' Page 4 missing real_world_example")

            # Page 5: Pitfalls & Guided Practice
            p5_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=5).order_by('component_order')]
            self.assertIn("concept_explanation", p5_types, f"Lesson '{lesson.title}' Page 5 missing concept_explanation")
            self.assertIn("step_process", p5_types, f"Lesson '{lesson.title}' Page 5 missing step_process")

            # Page 6: Formative Assessment & Synthesis
            p6_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by('component_order')
            p6_types = [b.component_type for b in p6_blocks]
            kc_blocks = [b for b in p6_blocks if b.component_type == "knowledge_check"]
            self.assertGreaterEqual(len(kc_blocks), 2, f"Lesson '{lesson.title}' Page 6 must have at least 2 knowledge_checks")
            self.assertIn("summary", p6_types, f"Lesson '{lesson.title}' Page 6 missing summary")

    def test_mcq_data_integrity(self):
        """Verify knowledge check MCQs have valid questions, 4 options, valid correct index, and explanations."""
        kc_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, component_type="knowledge_check")
        self.assertGreaterEqual(kc_blocks.count(), 14, "Expected at least 14 MCQs across 7 lessons")

        for block in kc_blocks:
            content = block.content
            self.assertIn("question", content)
            self.assertTrue(len(content["question"]) > 10)
            self.assertIn("options", content)
            self.assertTrue("answer" in content or "correct_answer" in content)
            ans = content.get("answer") or content.get("correct_answer")
            self.assertIn(ans, ["A", "B", "C", "D", 0, 1, 2, 3])
            self.assertIn("explanation", content)
            self.assertTrue(len(content["explanation"]) > 20)

    def test_lesson_assets_attachment(self):
        """Verify that SVGs, images, and videos are properly attached as LessonAssets."""
        lessons = Lesson.objects.filter(topic=self.topic)
        for lesson in lessons:
            diagram_blocks = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_diagram")
            for db in diagram_blocks:
                self.assertEqual(db.assets.count(), 1, f"Diagram block {db.block_id} must have attached asset")
                asset = db.assets.first()
                self.assertEqual(asset.asset_type, "diagram")
                self.assertEqual(asset.storage_type, "embed")
                self.assertIn("<svg", asset.metadata.get("svg_content", ""))

            image_blocks = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_image")
            for ib in image_blocks:
                self.assertEqual(ib.assets.count(), 1, f"Image block {ib.block_id} must have attached asset")
                asset = ib.assets.first()
                self.assertEqual(asset.asset_type, "image")
                self.assertTrue(asset.url.startswith("https://"))

            video_blocks = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_video")
            for vb in video_blocks:
                self.assertEqual(vb.assets.count(), 1, f"Video block {vb.block_id} must have attached asset")
                asset = vb.assets.first()
                self.assertEqual(asset.asset_type, "youtube")
                self.assertTrue(len(asset.metadata.get("youtube_id", "")) > 4)

    def test_no_citation_leakage_or_metadata(self):
        """Verify no citation brackets like [21] or [367] exist in block text."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')

        for block in blocks:
            text_rep = str(block.content)
            matches = bracket_pattern.findall(text_rep)
            self.assertEqual(len(matches), 0, f"Found uncleaned citation brackets in block {block.block_id}: {matches}")


if __name__ == "__main__":
    unittest.main()
