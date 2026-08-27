r"""
VLearn CBC Grade 10 Home Science — Comprehensive Automated QA & Integrity Verification Test Suite
Audits ALL Ingested Topics and Units under Subject 'Home Science':
  - Topic 1: Foods and Nutrition (Units 1.1 [2], 1.2 [14], 1.3 [8], 1.4 [14], 1.5 [12] -> 50 lessons total)
  - Topic 2: Home Management (Units 2.1 [4], 2.2 [4], 2.3 [4], 2.4 [8], 2.5 [6] -> 26 lessons total)
  - Grand Total: 76 Published Lessons across 2 Topics and 10 Learning Units

Tests:
  1. Hierarchy & Database Integrity (CBC -> Grade 10 -> Home Science -> Topics 1 & 2)
  2. Topic Integrity (Topic 1: Foods and Nutrition, Topic 2: Home Management)
  3. Learning Units Count & Structure (Exactly 10 Learning Units: 5 in Topic 1, 5 in Topic 2)
  4. Published Lessons Count & Status (Exactly 76 Lessons: all status='published', version=1)
  5. Page Counts (each lesson must have >= 5 discrete concept pages)
  6. Block Counts & Typed Coverage (each lesson >= 10 blocks: learning_goal, concept_explanation, step_process, suggested_image, suggested_diagram, suggested_video, knowledge_check, summary/key_takeaway)
  7. 100% YouTube Video Coverage (exactly 76 / 76 lessons have attached YouTube LessonAsset and valid 11-char ID)
  8. SVG XML Tag Validity & Responsive viewBox check on all 76 custom diagrams
  9. Regex scan for bracket citation leaks (r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
  10. Formative MCQ Integrity (4 options, valid correct_answer index 0-3, explanatory feedback)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_home_science.py
"""

import os
import sys
import re
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_svg_structure


class TestCBCGrade10HomeScience(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__icontains="CBC").first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name__icontains="Home Science").first()
        cls.topics = list(Topic.objects.filter(subject=cls.subject).order_by("order"))
        cls.learning_units = list(LearningUnit.objects.filter(topic__subject=cls.subject).order_by("topic__order", "order"))
        cls.lessons = list(Lesson.objects.filter(learning_unit__topic__subject=cls.subject).order_by("learning_unit__topic__order", "learning_unit__order", "id"))

    def test_01_hierarchy_integrity(self):
        """Verify Curriculum CBC -> Grade 10 -> Subject Home Science hierarchy."""
        self.assertIsNotNone(self.curriculum, "Curriculum 'CBC' not found")
        self.assertIsNotNone(self.grade, "Grade 10 not found under CBC")
        self.assertEqual(self.grade.level, 10, "Grade level is not 10")
        self.assertIsNotNone(self.subject, "Subject 'Home Science' not found under Grade 10")
        print(f"\n[PASS] Hierarchy Verified: CBC -> Grade 10 (Level 10) -> Home Science (ID: {self.subject.id})")

    def test_02_topic_integrity(self):
        """Verify Topic 1 (Foods and Nutrition) and Topic 2 (Home Management)."""
        self.assertGreaterEqual(len(self.topics), 2, "Expected at least 2 topics")
        t1 = self.topics[0]
        self.assertEqual(t1.order, 1)
        self.assertIn("Foods and Nutrition", t1.name)

        t2 = self.topics[1]
        self.assertEqual(t2.order, 2)
        self.assertIn("Home Management", t2.name)

        print(f"[PASS] Topics Verified (2 Topics):")
        print(f"       - Topic 1: '{t1.name}' (ID: {t1.id})")
        print(f"       - Topic 2: '{t2.name}' (ID: {t2.id})")

    def test_03_learning_units(self):
        """Verify exactly 10 Learning Units (5 in Topic 1, 5 in Topic 2)."""
        self.assertEqual(len(self.learning_units), 10, f"Expected exactly 10 learning units, found {len(self.learning_units)}")
        
        expected_units = [
            ("Foods and Nutrition", 1, "1.1 Overview of Foods and Nutrition"),
            ("Foods and Nutrition", 2, "1.2 Kitchen Layouts and Equipment"),
            ("Foods and Nutrition", 3, "1.3 Food Hygiene and Safety"),
            ("Foods and Nutrition", 4, "1.4 Methods of Cooking"),
            ("Foods and Nutrition", 5, "1.5 Nutritive Value of Foods"),
            ("Home Management", 1, "2.1 Hygiene During Puberty"),
            ("Home Management", 2, "2.2 Safety in the Home"),
            ("Home Management", 3, "2.3 Housing the Family"),
            ("Home Management", 4, "2.4 Care of the Home"),
            ("Home Management", 5, "2.5 Laundry Work")
        ]

        print(f"[PASS] 10 Learning Units Verified:")
        for idx, (exp_topic, exp_order, exp_name) in enumerate(expected_units):
            u = self.learning_units[idx]
            self.assertEqual(u.topic.name, exp_topic)
            self.assertEqual(u.order, exp_order)
            self.assertIn(exp_name, u.name)
            l_count = u.lessons.count()
            print(f"       - {exp_topic} | Unit {u.order}: {u.name} ({l_count} lessons)")

    def test_04_published_lessons_count_and_status(self):
        """Verify exactly 76 Published Lessons (all status='published', version=1: 50 in Topic 1, 26 in Topic 2)."""
        self.assertEqual(len(self.lessons), 76, f"Expected exactly 76 lessons, found {len(self.lessons)}")
        for l in self.lessons:
            self.assertEqual(l.status, "published", f"Lesson '{l.title}' is not published ({l.status})")
            self.assertEqual(l.version, 1, f"Lesson '{l.title}' has invalid version ({l.version})")
            self.assertTrue(l.title, f"Lesson ID {l.id} has empty title")
        print(f"[PASS] 76 Published Lessons Verified across 10 Units (All status='published', version=1)")

    def test_05_page_counts(self):
        """Verify each lesson has >= 5 discrete concept pages."""
        total_pages = 0
        for l in self.lessons:
            distinct_pages = l.blocks.values_list("page_number", flat=True).distinct()
            page_count = len(distinct_pages)
            total_pages += page_count
            self.assertGreaterEqual(
                page_count, 5,
                f"Lesson '{l.title}' has only {page_count} pages, expected >= 5"
            )
        avg_pages = total_pages / len(self.lessons)
        print(f"[PASS] Page Counts Verified: Total {total_pages} Pages across 76 Lessons (Avg: {avg_pages:.1f} pages/lesson, all >= 5)")

    def test_06_block_counts_and_types(self):
        """Verify each lesson has >= 10 typed blocks covering required pedagogical types."""
        required_types = [
            'learning_goal',
            'concept_explanation',
            'step_process',
            'suggested_image',
            'suggested_diagram',
            'suggested_video',
            'knowledge_check'
        ]

        total_blocks = 0
        for idx, lesson in enumerate(self.lessons, start=1):
            blocks = list(lesson.blocks.all().order_by("order"))
            block_count = len(blocks)
            total_blocks += block_count
            self.assertGreaterEqual(
                block_count, 10,
                f"Lesson {idx} ('{lesson.title}') has {block_count} blocks, expected >= 10"
            )

            block_types = set(b.block_type for b in blocks)
            for req_type in required_types:
                self.assertIn(
                    req_type, block_types,
                    f"Lesson {idx} ('{lesson.title}') missing required block_type '{req_type}'"
                )

            # Accept summary or key_takeaway
            self.assertTrue(
                'summary' in block_types or 'key_takeaway' in block_types,
                f"Lesson {idx} ('{lesson.title}') missing summary or key_takeaway block"
            )

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} in '{lesson.title}' has empty title")
                self.assertTrue(b.content, f"Block {b.id} in '{lesson.title}' has empty content")

        avg_blocks = total_blocks / len(self.lessons)
        print(f"[PASS] Block Counts & Typed Coverage Verified: Total {total_blocks} Blocks (Avg: {avg_blocks:.1f} blocks/lesson, all >= 10 with 100% required types)")

    def test_07_youtube_video_coverage(self):
        """Verify 100% YouTube video coverage: assert exactly 76 / 76 lessons have an attached YouTube video asset."""
        video_lessons_count = 0
        for lesson in self.lessons:
            yt_assets = lesson.assets.filter(asset_type="youtube")
            self.assertGreaterEqual(
                yt_assets.count(), 1,
                f"Lesson '{lesson.title}' has no attached YouTube video asset"
            )
            for asset in yt_assets:
                yt_id = asset.metadata.get("youtube_id") or ""
                if not yt_id and "v=" in (asset.url or ""):
                    yt_id = asset.url.split("v=")[-1][:11]
                self.assertTrue(
                    len(yt_id) >= 11,
                    f"Asset {asset.id} in '{lesson.title}' has invalid YouTube ID: '{yt_id}'"
                )
            video_lessons_count += 1

        self.assertEqual(video_lessons_count, 76, "Not all 76 lessons have verified YouTube videos")
        print(f"[PASS] 100% YouTube Video Coverage Verified: Exactly {video_lessons_count}/76 Lessons have valid YouTube video assets")

    def test_08_svg_xml_validity_and_viewbox(self):
        """Verify SVG XML tag validity and viewBox check on all 76 custom diagrams."""
        svg_diagram_count = 0
        for lesson in self.lessons:
            diagram_assets = lesson.assets.filter(asset_type="diagram")
            self.assertGreaterEqual(
                diagram_assets.count(), 1,
                f"Lesson '{lesson.title}' has no attached diagram asset"
            )
            for asset in diagram_assets:
                svg_content = asset.metadata.get("svg_content", "")
                self.assertTrue(
                    svg_content.startswith("<svg") and svg_content.endswith("</svg>"),
                    f"Diagram asset {asset.id} in '{lesson.title}' has invalid SVG content format"
                )
                self.assertTrue(
                    re.search(r'viewBox="0 0 \d+ \d+"', svg_content),
                    f"Diagram asset {asset.id} in '{lesson.title}' missing responsive viewBox"
                )
                is_valid, err = validate_svg_structure(svg_content)
                self.assertTrue(
                    is_valid,
                    f"Diagram asset {asset.id} in '{lesson.title}' SVG XML invalid: {err}"
                )
                svg_diagram_count += 1

        self.assertEqual(svg_diagram_count, 76, f"Expected 76 SVG diagrams, found {svg_diagram_count}")
        print(f"[PASS] SVG XML Validity & Responsive viewBox Verified: Exactly {svg_diagram_count}/76 Valid Vector SVGs attached")

    def test_09_regex_scan_bracket_citations(self):
        """Scan all blocks and metadata for bracket citation leaks (e.g. [123], [image_1], [S12])."""
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        leaks = []

        for lesson in self.lessons:
            for block in lesson.blocks.all():
                content_str = str(block.content)
                found = citation_pattern.findall(content_str)
                if found:
                    leaks.append((lesson.title, block.id, block.block_type, found))

        self.assertEqual(
            len(leaks), 0,
            f"Found {len(leaks)} bracket citation leaks in blocks: {leaks[:5]}"
        )
        print(f"[PASS] Regex Bracket Citation Scan: 0 Bracket Citation Leaks Detected across all {len(self.lessons)} lessons")

    def test_10_mcq_integrity(self):
        """Verify MCQ integrity: 4 options, valid correct_answer index (0-3), and detailed explanations."""
        mcq_count = 0
        for lesson in self.lessons:
            mcq_blocks = lesson.blocks.filter(block_type="knowledge_check")
            self.assertGreaterEqual(
                mcq_blocks.count(), 1,
                f"Lesson '{lesson.title}' has no knowledge_check MCQ block"
            )
            for mcq in mcq_blocks:
                content = mcq.content or {}
                question = content.get("question") or ""
                self.assertGreaterEqual(
                    len(question), 15,
                    f"MCQ {mcq.id} in '{lesson.title}' has too short question: '{question}'"
                )

                options = content.get("options") or []
                self.assertEqual(
                    len(options), 4,
                    f"MCQ {mcq.id} in '{lesson.title}' must have exactly 4 options, got {len(options)}"
                )

                for opt_idx, opt in enumerate(options):
                    self.assertTrue(opt, f"MCQ {mcq.id} option {opt_idx} is empty")

                ca = content.get("correct_answer")
                self.assertIsNotNone(ca, f"MCQ {mcq.id} in '{lesson.title}' missing correct_answer")
                self.assertIn(
                    ca, [0, 1, 2, 3, "0", "1", "2", "3"],
                    f"MCQ {mcq.id} in '{lesson.title}' invalid correct_answer index: {ca}"
                )

                exp = content.get("explanation") or ""
                self.assertGreaterEqual(
                    len(exp), 25,
                    f"MCQ {mcq.id} in '{lesson.title}' explanation too brief ({len(exp)} chars): '{exp}'"
                )
                mcq_count += 1

        self.assertEqual(mcq_count, 76, f"Expected 76 MCQs, found {mcq_count}")
        print(f"[PASS] MCQ Integrity Verified: Exactly {mcq_count}/76 MCQs with 4 options, valid answer index (0-3), and comprehensive feedback")


if __name__ == "__main__":
    print("=" * 80)
    print("CBC GRADE 10 HOME SCIENCE QA AUDITOR: COMPREHENSIVE TEST SUITE")
    print("=" * 80)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCBCGrade10HomeScience)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
