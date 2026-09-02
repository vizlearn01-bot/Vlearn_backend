"""
Master End-to-End Automated QA & Integrity Verification Test Suite for
CBC Grade 10 English — Topic 1: Listening and Speaking (Lessons 1 to 10)
"""

import os
import sys
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
import django
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)


class TestCBCGrade10EnglishTopic1MasterAll(unittest.TestCase):
    """
    Comprehensive Master Verification Test Suite for CBC Grade 10 English Topic 1.
    Audits all 10 units, 10 lessons, 60 pages, and all associated assets and blocks.
    """

    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.filter(id=5).first()
        if not cls.grade:
            cls.grade = Grade.objects.filter(name="Grade 10").first()
        assert cls.grade is not None, "Grade ID 5 (Grade 10 CBC) must exist in the database."

        cls.subject = Subject.objects.filter(grade=cls.grade, name="English").first()
        assert cls.subject is not None, "Subject 'English' must exist under Grade 10."

        cls.topic = Topic.objects.filter(subject=cls.subject, order=1).first()
        assert cls.topic is not None, "Topic 1 must exist under English."

        cls.expected_lessons = {
            1: "Etiquette in Everyday and Service Encounters",
            2: "Pronunciation: Target Sounds and Minimal Pairs",
            3: "Extensive Listening for Gist and Main Ideas",
            4: "Critical Listening: Fact, Opinion, Evidence, and Bias",
            5: "Intensive Listening and Viewing for Details",
            6: "Non-verbal Communication and Conversational Skills",
            7: "Interactive and Responsive Listening",
            8: "Syllabic and Emphatic Stress",
            9: "Speaking Fluency: Conversation, Presentation, and Interview",
            10: "Meetings, Discussions, Debate, and Oral Decision-making"
        }

    def test_01_curriculum_hierarchy_and_topic_linkage(self):
        """Test Subject 'English' is linked to Grade ID 5, and Topic 1 is 'Listening and Speaking'."""
        self.assertEqual(self.grade.id, 5, "Grade ID must be 5.")
        self.assertEqual(self.subject.name, "English", "Subject name must be 'English'.")
        self.assertEqual(self.topic.order, 1, "Topic order must be 1.")
        self.assertEqual(self.topic.name, "Listening and Speaking", "Topic 1 title must be 'Listening and Speaking'.")

    def test_02_all_10_learning_units_and_published_lessons(self):
        """Verify all 10 Learning Units and Lessons exist, ordered 1-10, with status='published' and version=1."""
        units = list(LearningUnit.objects.filter(topic=self.topic).order_by("order"))
        self.assertEqual(len(units), 10, f"Expected 10 Learning Units, found {len(units)}")

        for u_order, expected_title in self.expected_lessons.items():
            unit = LearningUnit.objects.filter(topic=self.topic, order=u_order).first()
            self.assertIsNotNone(unit, f"LearningUnit {u_order} does not exist!")
            self.assertEqual(unit.name, expected_title, f"Unit {u_order} title mismatch.")

            lesson = Lesson.objects.filter(learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"Lesson for Unit {u_order} does not exist!")
            self.assertEqual(lesson.title, expected_title, f"Lesson {u_order} title mismatch.")
            self.assertEqual(lesson.status, "published", f"Lesson {u_order} must be 'published'.")
            self.assertEqual(lesson.version, 1, f"Lesson {u_order} must be version 1.")

    def test_03_exact_6_page_structure_and_atomic_cards(self):
        """Verify each of the 10 lessons contains exactly 6 sequential pages (60 pages total) with standard components."""
        total_pages = 0
        total_blocks = 0

        for u_order in range(1, 11):
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))

            self.assertGreaterEqual(len(blocks), 13, f"Lesson {u_order} has fewer than 13 blocks ({len(blocks)})")
            total_blocks += len(blocks)

            pages = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            self.assertEqual(pages, [1, 2, 3, 4, 5, 6], f"Lesson {u_order} pages must be exactly [1, 2, 3, 4, 5, 6]")
            total_pages += len(pages)

            # Page 1: Discovery & Objectives (suggested_image, learning_goal)
            p1_types = [b.component_type for b in blocks if b.page_number == 1]
            self.assertIn("suggested_image", p1_types, f"Lesson {u_order} Page 1 missing suggested_image")
            self.assertIn("learning_goal", p1_types, f"Lesson {u_order} Page 1 missing learning_goal")

            # Page 2: Core Concepts & Terminology (definition_card / concept_explanation)
            p2_types = [b.component_type for b in blocks if b.page_number == 2]
            self.assertIn("definition_card", p2_types, f"Lesson {u_order} Page 2 missing definition_card")

            # Page 3: Model & Structured Analysis (suggested_diagram / diagram)
            p3_types = [b.component_type for b in blocks if b.page_number == 3]
            self.assertTrue(
                "suggested_diagram" in p3_types or "diagram" in p3_types,
                f"Lesson {u_order} Page 3 missing diagram component"
            )

            # Page 4: Media Integration & Listening Lab (suggested_video)
            p4_types = [b.component_type for b in blocks if b.page_number == 4]
            self.assertIn("suggested_video", p4_types, f"Lesson {u_order} Page 4 missing suggested_video")

            # Page 5: Common Mistakes & Guided Practice (common_mistakes / common_mistake, guided_practice)
            p5_types = [b.component_type for b in blocks if b.page_number == 5]
            self.assertTrue(
                "common_mistakes" in p5_types or "common_mistake" in p5_types,
                f"Lesson {u_order} Page 5 missing common_mistakes"
            )
            self.assertIn("guided_practice", p5_types, f"Lesson {u_order} Page 5 missing guided_practice")

            # Page 6: Knowledge Check & Summary (knowledge_check, summary_card / key_takeaway)
            p6_types = [b.component_type for b in blocks if b.page_number == 6]
            self.assertIn("knowledge_check", p6_types, f"Lesson {u_order} Page 6 missing knowledge_check")
            self.assertTrue(
                "summary_card" in p6_types or "key_takeaway" in p6_types,
                f"Lesson {u_order} Page 6 missing summary component"
            )

        self.assertEqual(total_pages, 60, f"Expected 60 total pages across Topic 1, found {total_pages}")
        self.assertGreaterEqual(total_blocks, 150, f"Expected >= 150 blocks total, found {total_blocks}")

    def test_04_all_10_custom_svg_vector_diagrams(self):
        """Verify all 10 lessons have attached, responsive XML SVG diagrams in LessonAsset and blocks."""
        for u_order in range(1, 11):
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            diagram_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="diagram").first()
            self.assertIsNotNone(diagram_asset, f"Lesson {u_order} missing diagram LessonAsset!")

            svg_content = diagram_asset.metadata.get("svg_content", "")
            self.assertTrue(svg_content.startswith("<svg"), f"Lesson {u_order} SVG does not start with <svg")
            self.assertTrue(svg_content.endswith("</svg>"), f"Lesson {u_order} SVG does not end with </svg>")

            # Parse XML
            try:
                root = ET.fromstring(svg_content)
                self.assertEqual(root.tag.split("}")[-1], "svg", f"Lesson {u_order} root tag is not svg")
                self.assertIn("viewBox", root.attrib, f"Lesson {u_order} SVG missing viewBox attribute")
            except ET.ParseError as e:
                self.fail(f"Lesson {u_order} SVG XML parse error: {e}")

    def test_05_all_10_wikimedia_photographic_assets(self):
        """Verify all 10 lessons have verified Wikimedia Commons photographic assets with full licensing."""
        for u_order in range(1, 11):
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            image_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="image").first()
            self.assertIsNotNone(image_asset, f"Lesson {u_order} missing image LessonAsset!")
            self.assertTrue(
                image_asset.url.startswith("https://upload.wikimedia.org/"),
                f"Lesson {u_order} image URL '{image_asset.url}' is not a Wikimedia Commons URL!"
            )
            self.assertTrue(bool(image_asset.metadata.get("licensing")), f"Lesson {u_order} image missing licensing")
            self.assertTrue(bool(image_asset.metadata.get("author")), f"Lesson {u_order} image missing author")
            self.assertTrue(bool(image_asset.metadata.get("caption")), f"Lesson {u_order} image missing caption")

    def test_06_all_10_youtube_video_media_assets(self):
        """Verify all 10 lessons have educational YouTube videos with pre-viewing tasks and post-viewing discussions."""
        for u_order in range(1, 11):
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            video_asset = LessonAsset.objects.filter(lesson=lesson, asset_type="youtube").first()
            self.assertIsNotNone(video_asset, f"Lesson {u_order} missing youtube LessonAsset!")
            self.assertTrue(
                video_asset.url.startswith("https://www.youtube.com/watch?v="),
                f"Lesson {u_order} invalid YouTube URL: {video_asset.url}"
            )
            self.assertTrue(
                len(video_asset.metadata.get("youtube_id", "")) >= 8,
                f"Lesson {u_order} invalid youtube_id"
            )

            # Check pre-viewing and post-viewing tasks on Page 4
            p4_blocks = list(LessonBlock.objects.filter(lesson=lesson, page_number=4))
            text_dump = " ".join([json.dumps(b.content) + " " + json.dumps(b.metadata) for b in p4_blocks]).lower()

            has_pre_viewing = any(kw in text_dump for kw in [
                "pre_viewing", "pre-viewing", "before watching", "before viewing", "pre_task", "listening comprehension", "ear tuning", "focus_prompt"
            ])
            has_post_viewing = any(kw in text_dump for kw in [
                "post_viewing", "post-viewing", "after watching", "after viewing", "discussion", "analysis", "reflection", "debate lab", "dialogue model"
            ])

            self.assertTrue(has_pre_viewing, f"Lesson {u_order} Page 4 missing pre-viewing task!")
            self.assertTrue(has_post_viewing, f"Lesson {u_order} Page 4 missing post-viewing discussion!")

    def test_07_knowledge_check_mcq_integrity(self):
        """Verify all 20 MCQs across all 10 lessons have 4 options (A-D), valid correct answer, and rich explanations."""
        total_mcqs = 0
        for u_order in range(1, 11):
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            mcqs = list(LessonBlock.objects.filter(lesson=lesson, component_type="knowledge_check"))
            self.assertGreaterEqual(len(mcqs), 2, f"Lesson {u_order} must have at least 2 MCQs (found {len(mcqs)})")
            total_mcqs += len(mcqs)

            for mcq in mcqs:
                content = mcq.content or {}
                self.assertIn("question", content, f"Lesson {u_order} MCQ missing question")
                self.assertTrue(bool(content["question"]), f"Lesson {u_order} MCQ question cannot be empty")

                options = content.get("options", [])
                self.assertEqual(len(options), 4, f"Lesson {u_order} MCQ must have exactly 4 options (found {len(options)})")

                correct = content.get("correct") or content.get("correct_answer")
                self.assertIn(correct, ["A", "B", "C", "D"], f"Lesson {u_order} MCQ correct answer '{correct}' must be A, B, C, or D")

                explanation = content.get("explanation") or content.get("option_explanations")
                self.assertTrue(bool(explanation), f"Lesson {u_order} MCQ missing explanation")

        self.assertEqual(total_mcqs, 20, f"Expected exactly 20 MCQs across Topic 1 (2 per lesson), found {total_mcqs}")

    def test_08_zero_developer_tag_leakage(self):
        """Verify that zero developer tags ([VISUAL: ...], [AUDIO: ...], citation brackets [1], [2], etc.) leak into content."""
        tag_patterns = [
            re.compile(r'\[VISUAL:', re.IGNORECASE),
            re.compile(r'\[AUDIO:', re.IGNORECASE),
            re.compile(r'\[\d+\]'),
            re.compile(r'\[image_\d+\]', re.IGNORECASE),
            re.compile(r'\[S\d+.*?\]', re.IGNORECASE),
        ]

        leaks = []
        for u_order in range(1, 11):
            unit = LearningUnit.objects.get(topic=self.topic, order=u_order)
            lesson = Lesson.objects.get(learning_unit=unit)

            for b in LessonBlock.objects.filter(lesson=lesson):
                def check_str(s, path):
                    if not isinstance(s, str) or "<svg" in s:
                        return
                    for pat in tag_patterns:
                        if pat.search(s):
                            leaks.append((lesson.title, b.id, b.page_number, b.component_type, path, s[:80]))

                def recurse_check(val, path=""):
                    if isinstance(val, str):
                        check_str(val, path)
                    elif isinstance(val, dict):
                        for k, v in val.items():
                            recurse_check(v, f"{path}.{k}")
                    elif isinstance(val, list):
                        for i, v in enumerate(val):
                            recurse_check(v, f"{path}[{i}]")

                check_str(b.title, "title")
                recurse_check(b.content, "content")

        self.assertEqual(len(leaks), 0, f"Detected developer tag leakage: {leaks}")


if __name__ == "__main__":
    unittest.main()
