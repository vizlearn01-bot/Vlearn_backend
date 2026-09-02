"""
VLearn CBC Grade 9 English — Topic 3: Grammar in Use
Comprehensive Verification & Unit Test Suite
"""

import os
import sys
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


class TestCBCGrade9EnglishTopic3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=18).first()
        if not cls.grade:
            cls.grade = Grade.objects.filter(name__icontains="Grade 9", curriculum__name="CBC").first()
        assert cls.grade is not None, "Grade 9 (ID 18) must exist in database."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        assert cls.subject is not None, "Subject 'English' must exist in Grade 9."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=3).first()
        assert cls.topic is not None, "Topic 3 'Grammar in Use' must exist in Grade 9 English."

    def test_topic_metadata(self):
        """Test topic order, naming, and description."""
        self.assertEqual(self.topic.order, 3)
        self.assertEqual(self.topic.name, "Grammar in Use")
        self.assertIn("grammar", self.topic.description.lower())

    def test_all_8_units_exist_in_sequence(self):
        """Test that all 8 learning units exist in correct sequence."""
        units = list(LearningUnit.objects.filter(topic=self.topic).order_by("order"))
        self.assertEqual(len(units), 8, f"Expected 8 units, found {len(units)}")

        expected_titles = [
            "Gender-Neutral Language",
            "Nouns (Formation) and Quantifiers",
            "Relative and Interrogative Pronouns",
            "The Order of Adjectives and Comparison of Adverbs",
            "Complex Prepositions and Correlative Conjunctions",
            "Modal Auxiliaries",
            "Present and Past Perfect Aspects",
            "Complex Sentences and Reported Speech"
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

    def test_each_lesson_has_6_atomic_pages(self):
        """Verify each lesson has exactly 6 distinct page numbers (1 to 6)."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson '{lesson.title}' must have pages 1 through 6.")

    def test_pedagogical_block_structure_per_page(self):
        """Verify required component types on each page for all 8 lessons."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lesson = Lesson.objects.get(learning_unit=unit)

            # Page 1: Discovery & Objectives
            p1_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by('component_order')]
            self.assertIn("suggested_image", p1_types, f"Lesson '{lesson.title}' missing suggested_image on page 1")
            self.assertIn("learning_goal", p1_types, f"Lesson '{lesson.title}' missing learning_goal on page 1")
            self.assertIn("concept_explanation", p1_types, f"Lesson '{lesson.title}' missing concept_explanation on page 1")

            # Page 2: Core Concepts & Terminology
            p2_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=2).order_by('component_order')]
            self.assertIn("definition_card", p2_types, f"Lesson '{lesson.title}' missing definition_card on page 2")
            self.assertIn("comparison_table", p2_types, f"Lesson '{lesson.title}' missing comparison_table on page 2")

            # Page 3: Model & Structured Analysis
            p3_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=3).order_by('component_order')]
            self.assertIn("suggested_diagram", p3_types, f"Lesson '{lesson.title}' missing suggested_diagram on page 3")
            self.assertIn("worked_example", p3_types, f"Lesson '{lesson.title}' missing worked_example on page 3")

            # Page 4: Media Integration & Active Lab
            p4_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=4).order_by('component_order')]
            self.assertIn("suggested_video", p4_types, f"Lesson '{lesson.title}' missing suggested_video on page 4")
            self.assertIn("real_world_example", p4_types, f"Lesson '{lesson.title}' missing real_world_example on page 4")

            # Page 5: Pitfalls & Guided Practice
            p5_types = [b.component_type for b in LessonBlock.objects.filter(lesson=lesson, page_number=5).order_by('component_order')]
            self.assertIn("common_mistake", p5_types, f"Lesson '{lesson.title}' missing common_mistake on page 5")
            self.assertIn("step_process", p5_types, f"Lesson '{lesson.title}' missing step_process on page 5")

            # Page 6: Formative Assessment & Synthesis
            p6_blocks = list(LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by('component_order'))
            p6_types = [b.component_type for b in p6_blocks]
            mcq_count = sum(1 for t in p6_types if t == "knowledge_check")
            self.assertGreaterEqual(mcq_count, 2, f"Lesson '{lesson.title}' must have at least 2 knowledge_checks on page 6")
            self.assertIn("summary", p6_types, f"Lesson '{lesson.title}' missing summary on page 6")

    def test_mcq_data_integrity(self):
        """Verify knowledge check MCQs have question, 4 options, correct answer, and explanation."""
        mcqs = LessonBlock.objects.filter(lesson__topic=self.topic, component_type="knowledge_check")
        self.assertEqual(mcqs.count(), 16, f"Expected 16 MCQs (2 per lesson * 8 lessons), found {mcqs.count()}")
        for mcq in mcqs:
            content = mcq.content
            self.assertIn("question", content)
            self.assertIn("options", content)
            self.assertTrue("answer" in content or "correct_answer" in content)
            ans = content.get("answer") or content.get("correct_answer")
            self.assertIn(ans, ["A", "B", "C", "D", 0, 1, 2, 3] + content["options"])
            self.assertIn("explanation", content)
            self.assertGreater(len(content["explanation"]), 20)

    def test_media_assets_linked_and_valid(self):
        """Verify images, videos, and SVGs are correctly created and attached as assets."""
        lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")
        for lesson in lessons:
            assets = LessonAsset.objects.filter(lesson=lesson)
            # Each lesson must have at least 1 image, 1 video, and 1 diagram
            asset_types = [a.asset_type for a in assets]
            self.assertIn("image", asset_types, f"Lesson '{lesson.title}' missing image asset")
            self.assertIn("youtube", asset_types, f"Lesson '{lesson.title}' missing youtube video asset")
            self.assertIn("diagram", asset_types, f"Lesson '{lesson.title}' missing diagram SVG asset")

            # Check SVG diagram content integrity
            diag_asset = assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(diag_asset)
            self.assertIn("svg_content", diag_asset.metadata)
            self.assertTrue(diag_asset.metadata["svg_content"].strip().startswith("<svg"))
            self.assertTrue(diag_asset.metadata["svg_content"].strip().endswith("</svg>"))

            # Check Video YouTube ID
            vid_asset = assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(vid_asset)
            self.assertIn("youtube_id", vid_asset.metadata)
            self.assertGreater(len(vid_asset.metadata["youtube_id"]), 3)

            # Check Image URL
            img_asset = assets.filter(asset_type="image").first()
            self.assertIsNotNone(img_asset)
            self.assertTrue(img_asset.url.startswith("https://"))

    def test_no_raw_bracket_citations_in_content(self):
        """Verify no citation tags like [37], [483] leaked into ingested block content."""
        import re
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        for block in blocks:
            text_repr = str(block.content)
            matches = citation_pattern.findall(text_repr)
            self.assertEqual(len(matches), 0, f"Found citation tags in block ID {block.id}: {matches}")


if __name__ == "__main__":
    unittest.main()
