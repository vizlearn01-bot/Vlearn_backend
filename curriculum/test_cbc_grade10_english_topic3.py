"""
VLearn CBC Grade 10 English — Topic 3: Grammar in Use
Comprehensive Verification Test Suite
"""

import os
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from dotenv import load_dotenv

# Set up paths and Django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestGrade10EnglishTopic3Ingestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=5).first() or Grade.objects.filter(name="Grade 10").first()
        cls.assertIsNotNone(cls.grade, "Grade 10 (ID 5) must exist in DB.")

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        cls.assertIsNotNone(cls.subject, "Subject 'English' must exist for Grade 10.")

        cls.topic = Topic.objects.filter(subject=cls.subject, order=3).first()
        cls.assertIsNotNone(cls.topic, "Topic 3 'Grammar in Use' must exist.")

    def test_topic_details(self):
        """Verify topic name and description."""
        self.assertEqual(self.topic.order, 3)
        self.assertEqual(self.topic.name, "Grammar in Use")
        self.assertTrue(len(self.topic.description) > 10)

    def test_learning_units_count_and_order(self):
        """Verify exactly 10 learning units exist in correct sequence (1 to 10)."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        self.assertEqual(units.count(), 10, f"Expected 10 LearningUnits, found {units.count()}")

        expected_titles = [
            "Nouns, Pronouns, and Determiners",
            "Verbs and Adverbs",
            "Adjectives, Conjunctions, and Simple Connectors",
            "Noun and Verb Phrases",
            "Adjective, Adverb, and Prepositional Phrases",
            "Relative and Adverbial Clauses",
            "Noun Clauses and Clause Functions",
            "Simple Sentence Structure and Sentence Parts",
            "Sentence Fluency: Fragments, Run-ons, Comma Splices, and Transformation",
            "Active/Passive Sentences and Subject–Verb Agreement"
        ]

        for idx, unit in enumerate(units, start=1):
            self.assertEqual(unit.order, idx)
            self.assertIn(expected_titles[idx - 1].split(":")[0], unit.name)

    def test_lessons_status_and_metadata(self):
        """Verify each learning unit has 1 published lesson with immutable metadata."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        for unit in units:
            lessons = Lesson.objects.filter(learning_unit=unit)
            self.assertEqual(lessons.count(), 1, f"Unit {unit.order} must have exactly 1 lesson.")
            lesson = lessons.first()
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertIsNotNone(lesson.immutable_metadata)
            self.assertEqual(lesson.immutable_metadata.get("grade"), "Grade 10")
            self.assertEqual(lesson.immutable_metadata.get("subject"), "English")
            self.assertEqual(lesson.immutable_metadata.get("topic_order"), 3)
            self.assertEqual(lesson.immutable_metadata.get("unit_order"), unit.order)

    def test_six_pages_per_lesson(self):
        """Verify each lesson has exactly 6 distinct pages."""
        lessons = Lesson.objects.filter(topic=self.topic)
        for lesson in lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            page_numbers = set(blocks.values_list("page_number", flat=True))
            self.assertEqual(page_numbers, {1, 2, 3, 4, 5, 6}, f"Lesson '{lesson.title}' must contain pages 1-6.")

    def test_page_block_composition_and_standards(self):
        """Verify pedagogical standards for each page across all 10 lessons."""
        lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")
        for lesson in lessons:
            u_order = lesson.learning_unit.order

            # Page 1: Discovery & Objectives (suggested_image, learning_goal, concept_explanation)
            p1_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=1).order_by("order")
            p1_types = [b.block_type for b in p1_blocks]
            self.assertIn("suggested_image", p1_types, f"L{u_order} P1 missing suggested_image")
            self.assertIn("learning_goal", p1_types, f"L{u_order} P1 missing learning_goal")
            self.assertIn("concept_explanation", p1_types, f"L{u_order} P1 missing concept_explanation")

            # Page 2: Core Concepts & Terminology (definition_card, comparison_table)
            p2_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=2).order_by("order")
            p2_types = [b.block_type for b in p2_blocks]
            self.assertIn("definition_card", p2_types, f"L{u_order} P2 missing definition_card")
            self.assertIn("comparison_table", p2_types, f"L{u_order} P2 missing comparison_table")

            # Page 3: Model & Structured Analysis (suggested_diagram, worked_example)
            p3_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=3).order_by("order")
            p3_types = [b.block_type for b in p3_blocks]
            self.assertIn("suggested_diagram", p3_types, f"L{u_order} P3 missing suggested_diagram")
            self.assertIn("worked_example", p3_types, f"L{u_order} P3 missing worked_example")

            # Page 4: Media Integration & Grammar Lab (suggested_video, real_world_example)
            p4_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=4).order_by("order")
            p4_types = [b.block_type for b in p4_blocks]
            self.assertIn("suggested_video", p4_types, f"L{u_order} P4 missing suggested_video")
            self.assertIn("real_world_example", p4_types, f"L{u_order} P4 missing real_world_example")

            # Page 5: Common Mistakes & Guided Practice (concept_explanation, step_process)
            p5_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=5).order_by("order")
            p5_types = [b.block_type for b in p5_blocks]
            self.assertIn("concept_explanation", p5_types, f"L{u_order} P5 missing concept_explanation")
            self.assertIn("step_process", p5_types, f"L{u_order} P5 missing step_process")

            # Page 6: Knowledge Check & Summary (2 x knowledge_check)
            p6_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by("order")
            p6_mcqs = [b for b in p6_blocks if b.block_type == "knowledge_check"]
            self.assertEqual(len(p6_mcqs), 2, f"L{u_order} P6 must have exactly 2 knowledge_checks")
            for mcq in p6_mcqs:
                content = mcq.content
                self.assertIn("question", content)
                self.assertIn("options", content)
                self.assertEqual(len(content["options"]), 4, "MCQ must have 4 options A-D")
                self.assertIn("correct_answer", content)
                self.assertIn(content["correct_answer"], [0, 1, 2, 3])
                self.assertIn("explanation", content)
                self.assertTrue(len(content["explanation"]) > 20)

    def test_svg_diagram_validity(self):
        """Verify all 10 custom SVGs are well-formed XML, non-empty, and attached."""
        diagram_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="suggested_diagram")
        self.assertEqual(diagram_blocks.count(), 10)

        for block in diagram_blocks:
            svg_content = block.content.get("svg_content", "")
            self.assertTrue(len(svg_content) > 100, f"Block {block.block_id} has empty/tiny SVG")
            self.assertTrue(svg_content.startswith("<svg"), f"Block {block.block_id} SVG must start with <svg")
            self.assertTrue(svg_content.endswith("</svg>"), f"Block {block.block_id} SVG must end with </svg>")
            # XML parsing validation
            try:
                root = ET.fromstring(svg_content)
                self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
            except Exception as e:
                self.fail(f"Invalid XML in SVG for block {block.block_id}: {e}")

    def test_lesson_assets_attachments(self):
        """Verify diagrams, images, and videos are attached as LessonAsset records."""
        lessons = Lesson.objects.filter(topic=self.topic)
        for lesson in lessons:
            assets = LessonAsset.objects.filter(lesson=lesson)
            types = set(assets.values_list("asset_type", flat=True))
            self.assertIn("diagram", types, f"Lesson '{lesson.title}' missing diagram asset.")
            self.assertIn("image", types, f"Lesson '{lesson.title}' missing image asset.")
            self.assertIn("youtube", types, f"Lesson '{lesson.title}' missing youtube asset.")


def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGrade10EnglishTopic3Ingestion)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
