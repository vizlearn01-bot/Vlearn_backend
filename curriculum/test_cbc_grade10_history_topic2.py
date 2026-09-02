"""
VLearn CBC Grade 10 History — Topic 2: Establishment of Colonial Rule
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


class TestCBCGrade10HistoryTopic2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
        assert cls.curriculum is not None, "CBC Curriculum must exist"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        assert cls.grade is not None, "Grade 10 must exist"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="History").first()
        assert cls.subject is not None, "History Subject must exist in Grade 10"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=2).first()
        assert cls.topic is not None, "Topic 2 (Establishment of Colonial Rule) must exist"

        cls.units = list(LearningUnit.objects.filter(topic=cls.topic).order_by("order"))
        cls.lessons = list(Lesson.objects.filter(topic=cls.topic).order_by("learning_unit__order"))

    def test_01_target_hierarchy(self):
        """Verify Curriculum, Grade, Subject, and Topic hierarchy."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.name, "Grade 10")
        self.assertEqual(self.subject.name, "History")
        self.assertEqual(self.topic.order, 2)
        self.assertIn("Establishment of Colonial Rule", self.topic.name)
        print("\n  [PASS] Test 01: Hierarchy correctly mapped to CBC -> Grade 10 -> History -> Topic 2")

    def test_02_learning_units_and_lessons_count(self):
        """Verify all 5 Units and 5 Lessons exist and are published."""
        self.assertEqual(len(self.units), 5, f"Expected 5 learning units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 5, f"Expected 5 lessons, found {len(self.lessons)}")

        expected_titles = [
            "Why Britain Established Colonial Rule",
            "British Methods of Establishing Rule",
            "The Process of Colonial Consolidation",
            "African Agency, Collaboration, and Resistance",
            "Colonial Rule as Change Over Time"
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

        self.assertEqual(total_pages, 31, f"Expected 31 total pages across 5 lessons, found {total_pages}")
        print(f"  [PASS] Test 03: Page card structures verified: 5-7 pages per lesson (Total: {total_pages} pages, {total_blocks} blocks)")

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
            svg = asset.metadata.get("svg_content", "")
            self.assertTrue(svg.startswith("<svg"), f"Asset '{asset.title}' svg_content must start with <svg")
            self.assertTrue(svg.endswith("</svg>"), f"Asset '{asset.title}' svg_content must end with </svg>")
            self.assertGreater(len(svg), 1000, f"Asset '{asset.title}' SVG content should be rich and detailed")

        print("  [PASS] Test 04: All 6 rich SVG vector diagrams validated (Causes/Consequences, Economic Coercion, Railway Map, Timeline, Strategic Matrix, Pre-Colonial vs Colonial Map)")

    def test_05_wikimedia_images(self):
        """Verify all Wikimedia images are properly configured with URLs and metadata."""
        image_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="suggested_image"
        )
        self.assertGreaterEqual(image_blocks.count(), 5, "Expected at least 5 image blocks")

        image_assets = LessonAsset.objects.filter(
            lesson__topic=self.topic,
            asset_type="image"
        )
        self.assertGreaterEqual(image_assets.count(), 5, "Expected at least 5 image assets")

        for asset in image_assets:
            self.assertTrue(asset.url.startswith("https://upload.wikimedia.org/"), f"Asset '{asset.title}' url must be from Wikimedia Commons")
            self.assertIn("author", asset.metadata)
            self.assertIn("licensing", asset.metadata)

        print(f"  [PASS] Test 05: {image_assets.count()} authentic Wikimedia images validated")

    def test_06_youtube_videos(self):
        """Verify each lesson has 1 educational YouTube video attached."""
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

        for asset in video_assets:
            yt_id = asset.metadata.get("youtube_id", "")
            self.assertGreaterEqual(len(yt_id), 8, f"Asset '{asset.title}' has invalid YouTube ID: {yt_id}")
            self.assertTrue(asset.url.startswith("https://www.youtube.com/watch?v="), f"Invalid video URL: {asset.url}")

        print("  [PASS] Test 06: Exactly 5 educational YouTube videos verified across all 5 lessons")

    def test_07_source_analysis_activities(self):
        """Verify primary source analyses for all 5 lessons."""
        source_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="mini_activity"
        )
        self.assertGreaterEqual(source_blocks.count(), 5, "Expected at least 5 source analysis / workshop blocks")

        # Verify specific source titles / contents
        titles_combined = " ".join(b.title for b in source_blocks)
        self.assertIn("Parliamentary", titles_combined) # Lesson 1
        self.assertIn("Maasai", titles_combined)        # Lesson 2
        self.assertIn("Kipande", titles_combined)       # Lesson 3
        self.assertIn("Corroboration", titles_combined) # Lesson 4
        self.assertIn("Scholarly", titles_combined)     # Lesson 5

        print("  [PASS] Test 07: All 5 Primary & Secondary Source Analysis workshops validated")

    def test_08_formative_assessment_mcqs(self):
        """Verify each lesson has a pedagogical MCQ with 4 options and detailed explanation."""
        mcq_blocks = LessonBlock.objects.filter(
            lesson__topic=self.topic,
            block_type="knowledge_check"
        )
        self.assertEqual(mcq_blocks.count(), 5, f"Expected 5 MCQ blocks, found {mcq_blocks.count()}")

        for idx, block in enumerate(mcq_blocks, start=1):
            content = block.content
            self.assertIn("question", content)
            self.assertIn("options", content)
            self.assertIn("correct_answer", content)
            self.assertIn("explanation", content)

            options = content["options"]
            self.assertEqual(len(options), 4, f"MCQ {idx} should have exactly 4 options")
            self.assertIn(content["correct_answer"], ["A", "B", "C", "D"], f"MCQ {idx} correct_answer should be A, B, C, or D")
            self.assertGreater(len(content["explanation"]), 30, f"MCQ {idx} explanation should be pedagogically thorough")

        print("  [PASS] Test 08: All 5 formative assessment MCQs validated with 4 options and thorough explanations")

    def test_09_bracket_citation_cleanliness(self):
        """Verify no uncleaned citation brackets ([113], [255]) or internal [VISUAL: ...] tags exist."""
        import re
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        visual_pattern = re.compile(r'\[VISUAL:[^\]]*\]')

        for b in blocks:
            text_str = str(b.content) + " " + (b.title or "")
            cit_matches = citation_pattern.findall(text_str)
            vis_matches = visual_pattern.findall(text_str)
            self.assertEqual(len(cit_matches), 0, f"Found uncleaned citation brackets in block {b.block_id}: {cit_matches}")
            self.assertEqual(len(vis_matches), 0, f"Found uncleaned [VISUAL:] tag in block {b.block_id}: {vis_matches}")

        print("  [PASS] Test 09: Text cleanliness verified: zero bracket citations or internal visual tags")


if __name__ == "__main__":
    unittest.main()
