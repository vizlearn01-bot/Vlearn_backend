"""
VLearn CBC Grade 10 English — Topic 4: Writing
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


class TestGrade10EnglishTopic4Ingestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=5).first() or Grade.objects.filter(name="Grade 10").first()
        cls.assertIsNotNone(cls.grade, "Grade 10 (ID 5) must exist in DB.")

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        cls.assertIsNotNone(cls.subject, "Subject 'English' must exist for Grade 10.")

        cls.topic = Topic.objects.filter(subject=cls.subject, order=4).first()
        cls.assertIsNotNone(cls.topic, "Topic 4 'Writing' must exist.")

    def test_topic_details(self):
        """Verify topic name, order, and description."""
        self.assertEqual(self.topic.order, 4)
        self.assertEqual(self.topic.name, "Writing")
        self.assertTrue(len(self.topic.description) > 10)

    def test_learning_units_count_and_order(self):
        """Verify exactly 10 learning units exist in correct sequence (1 to 10)."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        self.assertEqual(units.count(), 10, f"Expected 10 LearningUnits, found {units.count()}")

        expected_titles = [
            "Sentence Fluency and Paragraph Foundations",
            "Spelling, Abbreviations, and Acronyms",
            "Elements of Effective Writing",
            "Punctuation and Capitalization",
            "The Writing Process and Editing",
            "Descriptive and Narrative Essays",
            "Letters of Complaint, Request, and Inquiry",
            "Reports, Memos, and Emails",
            "Meeting Notices, Agendas, and Minutes",
            "Integrated Writing Performance and Publication"
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
            self.assertEqual(lesson.immutable_metadata.get("topic_order"), 4)
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

            # Page 3: Model & Structured Analysis / Visual Diagram (suggested_diagram, worked_example)
            p3_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=3).order_by("order")
            p3_types = [b.block_type for b in p3_blocks]
            self.assertIn("suggested_diagram", p3_types, f"L{u_order} P3 missing suggested_diagram")
            self.assertIn("worked_example", p3_types, f"L{u_order} P3 missing worked_example")

            # Page 4: Media Integration & Writing Lab (suggested_video, real_world_example)
            p4_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=4).order_by("order")
            p4_types = [b.block_type for b in p4_blocks]
            self.assertIn("suggested_video", p4_types, f"L{u_order} P4 missing suggested_video")
            self.assertIn("real_world_example", p4_types, f"L{u_order} P4 missing real_world_example")

            # Page 5: Common Mistakes & Guided Practice (concept_explanation, step_process)
            p5_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=5).order_by("order")
            p5_types = [b.block_type for b in p5_blocks]
            self.assertIn("concept_explanation", p5_types, f"L{u_order} P5 missing concept_explanation")
            self.assertIn("step_process", p5_types, f"L{u_order} P5 missing step_process")

            # Page 6: Knowledge Check & Summary (2 knowledge_checks, 1 concept_explanation summary)
            p6_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=6).order_by("order")
            kc_blocks = [b for b in p6_blocks if b.block_type == "knowledge_check"]
            self.assertEqual(len(kc_blocks), 2, f"L{u_order} P6 must have exactly 2 knowledge checks, found {len(kc_blocks)}")

            for idx, kc in enumerate(kc_blocks, start=1):
                content = kc.content
                self.assertIn("question", content, f"L{u_order} P6 KC{idx} missing question")
                self.assertIn("options", content, f"L{u_order} P6 KC{idx} missing options")
                self.assertEqual(len(content["options"]), 4, f"L{u_order} P6 KC{idx} must have 4 options")
                self.assertIn("correct_answer", content, f"L{u_order} P6 KC{idx} missing correct_answer")
                self.assertIn(content["correct_answer"], [0, 1, 2, 3], f"L{u_order} P6 KC{idx} correct_answer out of range")
                self.assertIn("explanation", content, f"L{u_order} P6 KC{idx} missing explanation")
                self.assertTrue(len(content["explanation"]) > 10, f"L{u_order} P6 KC{idx} explanation too short")

            summary_blocks = [b for b in p6_blocks if b.block_type == "concept_explanation"]
            self.assertTrue(len(summary_blocks) >= 1, f"L{u_order} P6 missing summary concept_explanation")

    def test_diagram_svgs_are_valid_xml(self):
        """Verify that all attached diagram assets contain valid, non-empty XML SVG markup."""
        diagram_assets = LessonAsset.objects.filter(lesson__topic=self.topic, asset_type="diagram")
        self.assertEqual(diagram_assets.count(), 10, f"Expected 10 diagram assets, found {diagram_assets.count()}")
        for asset in diagram_assets:
            svg_text = asset.metadata.get("svg_content", "")
            self.assertTrue(len(svg_text) > 50, f"Asset '{asset.title}' SVG content too short")
            try:
                root = ET.fromstring(svg_text)
                self.assertTrue(root.tag.endswith("svg"), f"Root tag must be SVG, got {root.tag}")
            except ET.ParseError as e:
                self.fail(f"Asset '{asset.title}' SVG is invalid XML: {e}")

    def test_media_assets_urls_and_sources(self):
        """Verify image and video assets are present with valid links."""
        image_assets = LessonAsset.objects.filter(lesson__topic=self.topic, asset_type="image")
        self.assertEqual(image_assets.count(), 10, f"Expected 10 image assets, found {image_assets.count()}")
        for img in image_assets:
            self.assertTrue(img.url.startswith("https://upload.wikimedia.org/"), f"Image URL invalid: {img.url}")
            self.assertIsNotNone(img.metadata.get("licensing"))

        video_assets = LessonAsset.objects.filter(lesson__topic=self.topic, asset_type="youtube")
        self.assertEqual(video_assets.count(), 10, f"Expected 10 youtube assets, found {video_assets.count()}")
        for vid in video_assets:
            self.assertTrue(vid.url.startswith("https://www.youtube.com/watch?v="), f"YouTube URL invalid: {vid.url}")
            self.assertTrue(len(vid.metadata.get("youtube_id", "")) > 5, "YouTube ID too short")

    def test_unique_block_ids_and_ordering(self):
        """Verify block IDs are unique and sequential within each lesson."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        block_ids = list(blocks.values_list("block_id", flat=True))
        self.assertEqual(len(block_ids), len(set(block_ids)), "Block IDs must be globally unique within topic.")

        lessons = Lesson.objects.filter(topic=self.topic)
        for lesson in lessons:
            l_blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")
            orders = [b.order for b in l_blocks]
            expected_orders = list(range(1, len(l_blocks) + 1))
            self.assertEqual(orders, expected_orders, f"Blocks in lesson '{lesson.title}' must be numbered sequentially 1..N.")


if __name__ == "__main__":
    unittest.main()
