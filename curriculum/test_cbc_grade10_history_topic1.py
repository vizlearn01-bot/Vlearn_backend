"""
Unit and Integration Tests for CBC Grade 10 History Topic 1 (Linguistic Groups in Kenya)
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

import unittest
from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestGrade10HistoryTopic1Ingestion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(name="Grade 10", curriculum__name="CBC").first()
        if not cls.grade:
            cls.grade = Grade.objects.filter(id=5).first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="History").first()
        cls.topic = Topic.objects.filter(subject=cls.subject, order=1).first() if cls.subject else None

    def test_01_subject_and_topic_linkage(self):
        """Test Grade 10 CBC, Subject 'History', and Topic 1 linkage."""
        self.assertIsNotNone(self.grade, "Grade 10 CBC must exist in the database.")
        self.assertIsNotNone(self.subject, "Subject 'History' must exist in Grade 10.")
        self.assertEqual(self.subject.grade.id, self.grade.id)
        self.assertIsNotNone(self.topic, "Topic 1 must exist for Grade 10 History.")
        self.assertEqual(self.topic.order, 1)
        self.assertEqual(self.topic.name, "Topic 1.1: Linguistic Groups in Kenya")

    def test_02_learning_units_and_lessons_structure(self):
        """Test all 5 LearningUnits and Lessons exist with published status."""
        expected_units = [
            (1, "Kenya’s Major Linguistic Families"),
            (2, "Migration, Settlement, and Expansion"),
            (3, "Interaction, Cultural Exchange, and Conflict"),
            (4, "Social Cohesion and Appreciation of Diversity"),
            (5, "Integrated Inquiry: Who Belongs and How Do We Know?")
        ]

        for u_order, expected_name in expected_units:
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            self.assertIsNotNone(unit, f"LearningUnit with order {u_order} must exist.")
            self.assertEqual(unit.name, expected_name)

            lesson = Lesson.objects.filter(learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"Lesson for Unit {u_order} must exist.")
            self.assertEqual(lesson.title, expected_name)
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)

    def test_03_lesson_pages_and_atomic_cards(self):
        """Verify each of the 5 lessons has 6 distinct pages with appropriate component types."""
        for u_order in range(1, 6):
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")

            self.assertGreater(blocks.count(), 0, f"Lesson {u_order} must have blocks.")

            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson {u_order} must contain exactly pages 1 to 6.")

            # Page 1: Must contain learning_goal
            p1_types = [b.component_type for b in blocks if b.page_number == 1]
            self.assertIn("learning_goal", p1_types, f"Lesson {u_order} Page 1 must have learning_goal.")

            # Page 6: Must contain knowledge_check and summary_card
            p6_types = [b.component_type for b in blocks if b.page_number == 6]
            self.assertIn("knowledge_check", p6_types, f"Lesson {u_order} Page 6 must have knowledge_check.")
            self.assertIn("summary_card", p6_types, f"Lesson {u_order} Page 6 must have summary_card.")

    def test_04_svg_diagram_validity_and_responsiveness(self):
        """Test all SVGs in diagram blocks are valid XML and responsive."""
        diagram_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            component_type="suggested_diagram"
        )
        self.assertGreaterEqual(diagram_blocks.count(), 5, "Must have at least 5 diagram blocks across Topic 1.")

        for db in diagram_blocks:
            svg_content = db.content.get("svg_content", "")
            self.assertTrue(svg_content.startswith("<svg"), f"Block {db.block_id} SVG must start with <svg.")
            self.assertIn('viewBox="0 0', svg_content, f"Block {db.block_id} SVG must have viewBox.")
            self.assertIn('width="100%"', svg_content, f"Block {db.block_id} SVG must have width='100%'.")

            try:
                root = ET.fromstring(svg_content)
                self.assertEqual(root.tag.split("}")[-1], "svg", f"Block {db.block_id} root tag must be svg.")
            except ET.ParseError as e:
                self.fail(f"SVG XML parse error in block {db.block_id}: {e}")

    def test_05_verified_wikimedia_images(self):
        """Test all suggested images have valid Wikimedia Commons URLs, captions, authors, and licensing."""
        image_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            component_type="suggested_image"
        )
        self.assertGreaterEqual(image_blocks.count(), 5, "Must have at least 5 image blocks across Topic 1.")

        for ib in image_blocks:
            c = ib.content
            url = c.get("url", "")
            self.assertTrue(url.startswith("https://upload.wikimedia.org/"), f"Block {ib.block_id} image URL must be from Wikimedia.")
            self.assertTrue(bool(c.get("caption")), f"Block {ib.block_id} image must have a caption.")
            self.assertTrue(bool(c.get("author")), f"Block {ib.block_id} image must have an author.")
            self.assertTrue(bool(c.get("licensing")), f"Block {ib.block_id} image must have licensing info.")

    def test_06_youtube_video_assets(self):
        """Test all 5 lessons have a verified educational YouTube video asset."""
        for u_order in range(1, 6):
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            video_blocks = LessonBlock.objects.filter(lesson=lesson, component_type="suggested_video")
            self.assertEqual(video_blocks.count(), 1, f"Lesson {u_order} must have exactly 1 suggested_video block.")

            vb = video_blocks.first()
            c = vb.content
            self.assertTrue(len(c.get("youtube_id", "")) >= 5, f"Lesson {u_order} must have a valid YouTube ID.")
            self.assertTrue(bool(c.get("description")), f"Lesson {u_order} video must have a description.")
            self.assertTrue(c.get("url", "").startswith("https://www.youtube.com/"), f"Lesson {u_order} must have full YouTube URL.")

    def test_07_knowledge_check_mcq_structure(self):
        """Test that all MCQs are properly structured with 4 options, valid answer key, and thorough explanation."""
        kc_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            component_type="knowledge_check"
        )
        self.assertGreaterEqual(kc_blocks.count(), 10, "Topic 1 must have at least 10 MCQs (2 per lesson).")

        for kc in kc_blocks:
            c = kc.content
            self.assertTrue(bool(c.get("question")), f"Block {kc.block_id} MCQ must have question text.")
            self.assertEqual(len(c.get("options", [])), 4, f"Block {kc.block_id} MCQ must have exactly 4 options.")
            self.assertIn(c.get("correct"), ["A", "B", "C", "D"], f"Block {kc.block_id} MCQ correct answer must be A, B, C, or D.")
            self.assertTrue(bool(c.get("explanation")), f"Block {kc.block_id} MCQ must have a pedagogical explanation.")

    def test_08_source_analysis_and_inquiry_activities(self):
        """Test that mini-activities, worked examples, and source analyses are present across lessons."""
        activity_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            component_type__in=["mini_activity", "worked_example"]
        )
        self.assertGreaterEqual(activity_blocks.count(), 5, "Must have at least 5 inquiry/source analysis activities.")

    def test_09_clean_text_no_citations_or_prompt_markers(self):
        """Verify no raw bracket citations [108] or prompt tags remain in content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        import re
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        tag_pattern = re.compile(r'\[(VISUAL|HISTORICAL_CONTEXT|SOURCE ANALYSIS|MISCONCEPTION|MCQ|CRITICAL THINKING|REAL WORLD APPLICATION|SOURCE QUESTION):?[^\]]*\]')

        for b in blocks:
            # Check title
            if b.title:
                self.assertIsNone(citation_pattern.search(b.title), f"Block {b.block_id} title contains bracket citation: {b.title}")
                self.assertIsNone(tag_pattern.search(b.title), f"Block {b.block_id} title contains raw tag: {b.title}")

            # Check content
            content_str = str(b.content)
            self.assertIsNone(citation_pattern.search(content_str), f"Block {b.block_id} content contains bracket citation.")
            self.assertIsNone(tag_pattern.search(content_str), f"Block {b.block_id} content contains raw tag.")


if __name__ == "__main__":
    unittest.main()
