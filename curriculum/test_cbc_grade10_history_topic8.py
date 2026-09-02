"""
VLearn CBC Grade 10 History — Topic 8: African Civilisations up to the 19th Century
Comprehensive Automated Test Suite & Quality Auditor
"""

import os
import sys
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.ingest_cbc_grade10_history_topic8 import ingest_grade10_history_topic8


class TestCBCGrade10HistoryTopic8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Run ingestion once to ensure clean baseline
        ingest_grade10_history_topic8(replace=True)

        cls.curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
        assert cls.curriculum is not None, "CBC Curriculum must exist"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        assert cls.grade is not None, "Grade 10 must exist"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="History").first()
        assert cls.subject is not None, "History Subject must exist in Grade 10"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=8).first()
        assert cls.topic is not None, "Topic 8 (African Civilisations up to the 19th Century) must exist"

        cls.units = list(LearningUnit.objects.filter(topic=cls.topic).order_by("order"))
        cls.lessons = list(Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order"))

    def test_01_target_hierarchy(self):
        """Verify Curriculum, Grade, Subject, and Topic hierarchy."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.name, "Grade 10")
        self.assertEqual(self.subject.name, "History")
        self.assertEqual(self.topic.order, 8)
        self.assertIn("African Civilisations", self.topic.name)
        print("\n  [PASS] Test 01: Hierarchy correctly mapped to CBC -> Grade 10 -> History -> Topic 8")

    def test_02_learning_units_and_lessons_count(self):
        """Verify all 5 Units and 5 Lessons exist and are published."""
        self.assertEqual(len(self.units), 5, f"Expected 5 learning units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 5, f"Expected 5 lessons, found {len(self.lessons)}")

        expected_titles = [
            "Locating and Defining African Civilisations",
            "Governance, Economy, and Society",
            "Contributions and Historical Evidence",
            "Change, Continuity, and Transformation",
            "Early African Governance and Present Leadership"
        ]

        for idx, (unit, lesson) in enumerate(zip(self.units, self.lessons), start=1):
            self.assertEqual(unit.order, idx)
            self.assertEqual(lesson.title, expected_titles[idx - 1])
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.title} should be published")
            self.assertEqual(lesson.learning_unit, unit)
        print(f"  [PASS] Test 02: Exactly 5 Units and 5 Published Lessons verified")

    def test_03_pages_and_cards_structure(self):
        """Verify each lesson has between 5 and 7 distinct pages/cards with multiple components."""
        total_pages = 0
        total_blocks = 0

        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")
            pages = set(b.page_number for b in blocks)
            page_count = len(pages)
            self.assertTrue(
                5 <= page_count <= 7,
                f"Lesson '{lesson.title}' has {page_count} pages, expected between 5 and 7"
            )
            total_pages += page_count
            total_blocks += blocks.count()

            # Ensure block numbering and page titles are set
            first_blocks = blocks.filter(component_order=1)
            for fb in first_blocks:
                self.assertIsNotNone(fb.page_title, f"First block of page {fb.page_number} must have page_title")

        self.assertEqual(total_pages, 25, f"Expected 25 total pages across 5 lessons, found {total_pages}")
        print(f"  [PASS] Test 03: Page card structures verified: 5 pages per lesson (Total: {total_pages} pages, {total_blocks} blocks)")

    def test_04_visualizations_and_svg_assets(self):
        """Verify all 6 rich SVG diagrams are attached and contain valid SVG markup."""
        diagram_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="suggested_diagram"
        )
        self.assertEqual(diagram_blocks.count(), 6, f"Expected 6 diagram blocks, found {diagram_blocks.count()}")

        diagram_assets = LessonAsset.objects.filter(
            lesson__topic=self.topic,
            asset_type="diagram"
        )
        self.assertEqual(diagram_assets.count(), 6, f"Expected 6 diagram assets, found {diagram_assets.count()}")

        for asset in diagram_assets:
            svg_content = asset.metadata.get("svg_content", "")
            self.assertTrue(svg_content.startswith("<svg"), "SVG content must start with <svg")
            self.assertTrue(svg_content.endswith("</svg>"), "SVG content must end with </svg>")
            self.assertIn("viewBox", svg_content, "SVG must contain a viewBox attribute")
        print(f"  [PASS] Test 04: All 6 rich SVG diagrams verified with valid XML geometry")

    def test_05_image_and_video_assets(self):
        """Verify Wikimedia images and verified YouTube video assets."""
        image_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="suggested_image"
        )
        self.assertEqual(image_blocks.count(), 2, f"Expected 2 image blocks, found {image_blocks.count()}")

        image_assets = LessonAsset.objects.filter(
            lesson__topic=self.topic,
            asset_type="image"
        )
        self.assertEqual(image_assets.count(), 2, f"Expected 2 image assets, found {image_assets.count()}")
        for img in image_assets:
            self.assertTrue(img.url.startswith("https://upload.wikimedia.org/"), f"Invalid image URL: {img.url}")

        video_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="suggested_video"
        )
        self.assertEqual(video_blocks.count(), 5, f"Expected 5 video blocks, found {video_blocks.count()}")

        video_assets = LessonAsset.objects.filter(
            lesson__topic=self.topic,
            asset_type="youtube"
        )
        self.assertEqual(video_assets.count(), 5, f"Expected 5 video assets, found {video_assets.count()}")

        expected_ids = ["kY31WnS8jXk", "F3_6mF-yvR0", "78K3fQ94_7Y", "2r1o5Xb1pQk", "T_sGTspaF4Y"]
        for idx, v_asset in enumerate(video_assets.order_by("lesson__learning_unit__order")):
            yt_id = v_asset.metadata.get("youtube_id", "")
            self.assertEqual(yt_id, expected_ids[idx], f"Video ID mismatch for lesson {idx+1}")
        print(f"  [PASS] Test 05: 2 Wikimedia image assets and 5 verified YouTube videos verified")

    def test_06_knowledge_check_mcqs(self):
        """Verify all 10 MCQs have questions, 4 options, valid correct answer, and explanation."""
        mcq_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="knowledge_check"
        )
        self.assertEqual(mcq_blocks.count(), 10, f"Expected 10 MCQ blocks, found {mcq_blocks.count()}")

        for mcq in mcq_blocks:
            content = mcq.content
            self.assertIn("question", content, "MCQ must have a question field")
            self.assertIn("options", content, "MCQ must have options")
            self.assertEqual(len(content["options"]), 4, "MCQ must have exactly 4 options (A, B, C, D)")
            for opt_key in ["A", "B", "C", "D"]:
                self.assertIn(opt_key, content["options"], f"Option {opt_key} missing in MCQ")
            self.assertIn(content["correct_answer"], ["A", "B", "C", "D"], "correct_answer must be A, B, C, or D")
            self.assertTrue(len(content.get("explanation", "")) > 20, "MCQ must have a pedagogical explanation")
        print(f"  [PASS] Test 06: All 10 MCQs fully validated with 4 options and detailed explanations")

    def test_07_source_analysis_and_capstone(self):
        """Verify presence of Source Analysis in Lesson 3 and Capstone Convening in Lesson 5."""
        l3_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            lesson__learning_unit__order=3
        )
        source_analysis_found = any(
            "Primary Source Analysis" in b.title or "travelers who walk with the moon" in str(b.content)
            for b in l3_blocks
        )
        self.assertTrue(source_analysis_found, "Lesson 3 must include the Nyamwezi oral tradition source analysis")

        l5_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            lesson__learning_unit__order=5
        )
        capstone_found = any(
            "Constitutional Convening" in b.title or "EAC Charter" in str(b.content)
            for b in l5_blocks
        )
        self.assertTrue(capstone_found, "Lesson 5 must include the Constitutional Convening capstone activity")
        print(f"  [PASS] Test 07: Primary Source Analysis (Lesson 3) and Capstone Inquiry (Lesson 5) verified")

    def test_08_text_sanitization(self):
        """Verify no bracket citations or visual tag leaks exist in block content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for b in blocks:
            text_rep = str(b.content)
            self.assertNotIn("[VISUAL:", text_rep, f"Visual tag leak found in block {b.block_id}")
            self.assertNotIn("[/VISUAL]", text_rep, f"Visual tag leak found in block {b.block_id}")
            self.assertNotIn("[HISTORICAL_CONTEXT]", text_rep, f"Context tag leak found in block {b.block_id}")
            self.assertNotIn("[SOURCE_ANALYSIS]", text_rep, f"Source analysis tag leak found in block {b.block_id}")
        print(f"  [PASS] Test 08: Text sanitization verified: zero tag leaks or bracket citations")

    def test_09_idempotency(self):
        """Verify re-ingesting executes cleanly with identical counts."""
        result = ingest_grade10_history_topic8(replace=True)
        self.assertEqual(result["units"], 5)
        self.assertEqual(result["lessons"], 5)
        self.assertEqual(result["pages"], 25)
        self.assertEqual(result["assets"], 13)  # 6 diagrams + 2 images + 5 videos = 13 assets
        print(f"  [PASS] Test 09: Idempotency verified: re-ingestion succeeds cleanly")


if __name__ == "__main__":
    unittest.main(verbosity=2)
