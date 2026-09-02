"""
VLearn CBC Grade 9 English — Topic 4: The Writing Process and Composition
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


class TestCBCGrade9EnglishTopic4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=18).first()
        if not cls.grade:
            cls.grade = Grade.objects.filter(name="Grade 9", curriculum__name="CBC").first()
        assert cls.grade is not None, "Grade 9 (ID 18) must exist."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        assert cls.subject is not None, "Subject 'English' must exist in Grade 9."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=4).first()
        assert cls.topic is not None, "Topic 4 'The Writing Process and Composition' must exist in Subject 'English'."

    def test_topic_structure(self):
        """Test topic naming, description, and order."""
        self.assertEqual(self.topic.order, 4)
        self.assertEqual(self.topic.name, "The Writing Process and Composition")
        self.assertIn("mechanics", self.topic.description.lower())
        self.assertIn("narrative", self.topic.description.lower())

    def test_all_7_units_exist(self):
        """Test that all 7 learning units exist in correct sequence."""
        units = list(LearningUnit.objects.filter(topic=self.topic).order_by("order"))
        self.assertEqual(len(units), 7, f"Expected 7 units, found {len(units)}")

        expected_titles = [
            "Legibility, Spelling, and Punctuation",
            "Structuring the Perfect Paragraph",
            "Formal Letters and Application Forms",
            "Professional Emails",
            "The Writing Process in Action",
            "Crafting Narrative Compositions",
            "Creative Writing with Idioms"
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
            self.assertEqual(lesson.immutable_metadata["topic_order"], 4)

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
            p1_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by('order')]
            self.assertIn("suggested_image", p1_types, f"Lesson '{lesson.title}' Page 1 missing suggested_image")
            self.assertIn("learning_goal", p1_types, f"Lesson '{lesson.title}' Page 1 missing learning_goal")
            self.assertIn("concept_explanation", p1_types, f"Lesson '{lesson.title}' Page 1 missing concept_explanation")

            # Page 2: Core Concepts & Terminology
            p2_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=2).order_by('order')]
            self.assertIn("definition_card", p2_types, f"Lesson '{lesson.title}' Page 2 missing definition_card")
            self.assertIn("comparison_table", p2_types, f"Lesson '{lesson.title}' Page 2 missing comparison_table")
            self.assertIn("concept_explanation", p2_types, f"Lesson '{lesson.title}' Page 2 missing concept_explanation")

            # Page 3: Model & Structured Analysis
            p3_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=3).order_by('order')]
            self.assertIn("suggested_diagram", p3_types, f"Lesson '{lesson.title}' Page 3 missing suggested_diagram")
            self.assertIn("worked_example", p3_types, f"Lesson '{lesson.title}' Page 3 missing worked_example")

            # Page 4: Media Integration & Active Lab
            p4_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=4).order_by('order')]
            self.assertIn("suggested_video", p4_types, f"Lesson '{lesson.title}' Page 4 missing suggested_video")
            self.assertIn("real_world_example", p4_types, f"Lesson '{lesson.title}' Page 4 missing real_world_example")

            # Page 5: Pitfalls & Guided Practice
            p5_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=5).order_by('order')]
            self.assertIn("common_mistakes", p5_types, f"Lesson '{lesson.title}' Page 5 missing common_mistakes")
            self.assertIn("guided_practice", p5_types, f"Lesson '{lesson.title}' Page 5 missing guided_practice")

            # Page 6: Formative Assessment & Synthesis
            p6_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by('order')]
            self.assertEqual(p6_types.count("knowledge_check"), 2, f"Lesson '{lesson.title}' Page 6 must have 2 knowledge_checks")
            self.assertIn("summary_card", p6_types, f"Lesson '{lesson.title}' Page 6 missing summary_card")

    def test_mcq_data_integrity(self):
        """Verify MCQs have valid questions, 4 options, valid answers (A/B/C/D), and non-empty explanations."""
        mcq_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            component_type="knowledge_check"
        )
        self.assertEqual(mcq_blocks.count(), 14, "Expected exactly 14 MCQs across Topic 4.")

        for b in mcq_blocks:
            c = b.content
            self.assertIn("question", c, f"Block {b.id} missing question")
            self.assertTrue(len(c["question"].strip()) > 10, f"Block {b.id} has too short question")
            self.assertIn("options", c, f"Block {b.id} missing options")
            self.assertEqual(len(c["options"]), 4, f"Block {b.id} must have 4 options")
            self.assertIn("answer", c, f"Block {b.id} missing answer")
            self.assertIn(c["answer"], ["A", "B", "C", "D"], f"Block {b.id} answer must be A/B/C/D")
            self.assertIn("explanation", c, f"Block {b.id} missing explanation")
            self.assertTrue(len(c["explanation"].strip()) > 15, f"Block {b.id} has too short explanation")

    def test_lesson_assets_attachment(self):
        """Verify that SVGs, images, and videos are properly attached as LessonAssets."""
        assets = LessonAsset.objects.filter(lesson__topic=self.topic)
        diagram_assets = assets.filter(asset_type="diagram")
        image_assets = assets.filter(asset_type="image")
        video_assets = assets.filter(asset_type="youtube")

        self.assertEqual(diagram_assets.count(), 7, "Expected 7 diagram assets.")
        self.assertEqual(image_assets.count(), 7, "Expected 7 image assets.")
        self.assertEqual(video_assets.count(), 7, "Expected 7 video assets.")

        for da in diagram_assets:
            self.assertIn("svg_content", da.metadata)
            self.assertTrue(da.metadata["svg_content"].strip().startswith("<svg"))

    def test_no_citation_leakage_or_metadata(self):
        """Verify zero bracket citations (e.g. [21], [367]) in titles or text content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        bracket_regex = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')

        for b in blocks:
            match_title = bracket_regex.search(b.title)
            self.assertIsNone(match_title, f"Block {b.id} title contains citation bracket: {b.title}")

            def check_content(val, path=""):
                if isinstance(val, str):
                    m = bracket_regex.search(val)
                    self.assertIsNone(m, f"Block {b.id} at {path} contains citation bracket: '{m.group(0) if m else ''}'")
                elif isinstance(val, dict):
                    for k, v in val.items():
                        check_content(v, f"{path}.{k}")
                elif isinstance(val, list):
                    for idx, item in enumerate(val):
                        check_content(item, f"{path}[{idx}]")

            check_content(b.content, "content")


if __name__ == "__main__":
    unittest.main()
