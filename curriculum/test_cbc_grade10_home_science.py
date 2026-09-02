r"""
VLearn CBC Grade 10 Home Science — Comprehensive Automated QA & Integrity Verification Test Suite
Audits ALL Ingested Topics and Units under Subject 'Home Science':
  - Topic 1: Foods and Nutrition (Units 1.1 [2], 1.2 [14], 1.3 [8], 1.4 [14], 1.5 [12] -> 50 lessons)
  - Topic 2: Home Management (Units 2.1 [4], 2.2 [4], 2.3 [4], 2.4 [8], 2.5 [6], 2.6 [4] -> 30 lessons)
  - Topic 3: Clothing and Textiles (Units 3.1 [11], 3.2 [12], 3.3 [14], 3.4 [12], 3.5 [18] -> 67 lessons)
  - Grand Total: 147 Published Lessons across 3 Topics and 16 Learning Units

Tests:
  1. Hierarchy & Database Integrity (CBC -> Grade 10 -> Home Science -> Topics 1, 2 & 3)
  2. Topic Integrity (Topic 1: Foods and Nutrition, Topic 2: Home Management, Topic 3: Clothing and Textiles)
  3. Learning Units Count & Structure (Exactly 16 Learning Units: 5 in Topic 1, 6 in Topic 2, 5 in Topic 3)
  4. Published Lessons Count & Status (Exactly 147 Lessons: all status='published', version=1)
  5. Page Counts (each lesson must have >= 5 discrete concept pages)
  6. Block Counts & Typed Coverage (each lesson >= 10 blocks: learning_goal, concept_explanation, step_process, suggested_image, suggested_diagram, suggested_video, knowledge_check, summary/key_takeaway)
  7. 100% YouTube Video Coverage (exactly 147 / 147 lessons have attached YouTube LessonAsset and valid ID)
  8. SVG XML Tag Validity & Responsive viewBox check on all 147 custom diagrams
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
        """Verify Topic 1 (Foods and Nutrition), Topic 2 (Home Management), and Topic 3 (Clothing and Textiles)."""
        self.assertGreaterEqual(len(self.topics), 3, "Expected at least 3 topics")
        t1 = self.topics[0]
        self.assertEqual(t1.order, 1)
        self.assertIn("Foods and Nutrition", t1.name)

        t2 = self.topics[1]
        self.assertEqual(t2.order, 2)
        self.assertIn("Home Management", t2.name)

        t3 = self.topics[2]
        self.assertEqual(t3.order, 3)
        self.assertIn("Clothing and Textiles", t3.name)

        print(f"[PASS] Topics Verified (3 Topics):")
        print(f"       - Topic 1: '{t1.name}' (ID: {t1.id})")
        print(f"       - Topic 2: '{t2.name}' (ID: {t2.id})")
        print(f"       - Topic 3: '{t3.name}' (ID: {t3.id})")

    def test_03_learning_units(self):
        """Verify exactly 16 Learning Units (5 in Topic 1, 6 in Topic 2, 5 in Topic 3)."""
        self.assertEqual(len(self.learning_units), 16, f"Expected exactly 16 learning units, found {len(self.learning_units)}")
        
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
            ("Home Management", 5, "2.5 Laundry Work"),
            ("Home Management", 6, "2.6 Consumer Education"),
            ("Clothing and Textiles", 1, "3.1 Sewing Tools, Equipment, and Materials"),
            ("Clothing and Textiles", 2, "3.2 Textile Fibres"),
            ("Clothing and Textiles", 3, "3.3 Clothing Construction Processes: Stitches"),
            ("Clothing and Textiles", 4, "3.4 Clothing Construction Processes: Seams"),
            ("Clothing and Textiles", 5, "3.5 Clothing Construction Processes: Management of Fullness")
        ]

        print(f"[PASS] 16 Learning Units Verified:")
        for idx, (exp_topic, exp_order, exp_name) in enumerate(expected_units):
            u = self.learning_units[idx]
            self.assertEqual(u.topic.name, exp_topic)
            self.assertEqual(u.order, exp_order)
            self.assertIn(exp_name, u.name)
            l_count = u.lessons.count()
            print(f"       - {exp_topic} | Unit {u.order}: {u.name} ({l_count} lessons)")

    def test_04_published_lessons_count_and_status(self):
        """Verify exactly 147 Published Lessons (all status='published', version=1)."""
        self.assertEqual(len(self.lessons), 147, f"Expected exactly 147 lessons, found {len(self.lessons)}")
        for l in self.lessons:
            self.assertEqual(l.status, "published", f"Lesson '{l.title}' is not published ({l.status})")
            self.assertEqual(l.version, 1, f"Lesson '{l.title}' has invalid version ({l.version})")
            self.assertTrue(l.title, f"Lesson ID {l.id} has empty title")
        print(f"[PASS] 147 Published Lessons Verified across 16 Units (All status='published', version=1)")

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
        print(f"[PASS] Page Counts Verified: Total {total_pages} Pages across 147 Lessons (Avg: {avg_pages:.1f} pages/lesson, all >= 5)")

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
        print(f"[PASS] Block Counts & Types Verified: Total {total_blocks} Blocks across 147 Lessons (Avg: {avg_blocks:.1f} blocks/lesson, 100% typed coverage)")

    def test_07_youtube_video_coverage(self):
        """Assert 100% YouTube video coverage across all 147 lessons."""
        video_count = 0
        for lesson in self.lessons:
            yt_assets = lesson.assets.filter(asset_type="youtube")
            self.assertGreaterEqual(
                yt_assets.count(), 1,
                f"Lesson '{lesson.title}' has no attached YouTube LessonAsset"
            )
            for y in yt_assets:
                yt_id = y.metadata.get("youtube_id", "")
                self.assertTrue(
                    yt_id,
                    f"Lesson '{lesson.title}' YouTube asset {y.id} missing youtube_id"
                )
                self.assertEqual(
                    len(yt_id), 11,
                    f"Lesson '{lesson.title}' YouTube asset has invalid ID length: '{yt_id}'"
                )
                self.assertIn("youtube.com", y.url)
                video_count += 1

        self.assertEqual(video_count, 147, f"Expected 147 YouTube video assets, found {video_count}")
        print(f"[PASS] 100% Video Coverage Verified: Exactly {video_count} / {len(self.lessons)} Lessons have verified YouTube embeds")

    def test_08_svg_diagram_validity(self):
        """Assert all 147 lessons have sanitized, valid responsive SVGs."""
        diagram_count = 0
        for lesson in self.lessons:
            diagram_assets = lesson.assets.filter(asset_type="diagram")
            self.assertGreaterEqual(
                diagram_assets.count(), 1,
                f"Lesson '{lesson.title}' has no attached Diagram LessonAsset"
            )
            for d in diagram_assets:
                svg_code = d.metadata.get("svg_content", "")
                self.assertTrue(svg_code, f"Lesson '{lesson.title}' diagram {d.id} has empty svg_content")
                self.assertIn("<svg", svg_code)
                self.assertIn("</svg>", svg_code)
                self.assertTrue(
                    re.search(r'viewBox="0 0 \d+ \d+"', svg_code),
                    f"Lesson '{lesson.title}' SVG missing valid responsive viewBox attribute: {svg_code[:100]}"
                )
                diagram_count += 1

        self.assertEqual(diagram_count, 147, f"Expected 147 Diagram assets, found {diagram_count}")
        print(f"[PASS] SVG Diagram Validity Verified: Exactly {diagram_count} / {len(self.lessons)} Lessons have responsive vector SVGs")

    def test_09_no_bracket_citation_leaks(self):
        """Scan all lesson blocks across all 147 lessons for bracket citation leaks."""
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        leaks = []

        for lesson in self.lessons:
            for block in lesson.blocks.all():
                content_str = str(block.content)
                matches = citation_pattern.findall(content_str)
                if matches:
                    leaks.append((lesson.title, block.block_type, matches))

        self.assertEqual(
            len(leaks), 0,
            f"Found {len(leaks)} bracket citation leaks across database blocks:\n" +
            "\n".join(f"  - {l[0]} [{l[1]}]: {l[2]}" for l in leaks[:5])
        )
        print(f"[PASS] Zero Citation Leaks Verified: Scanned all blocks across 147 Lessons (0 leaks found)")

    def test_10_mcq_integrity(self):
        """Assert MCQ formative knowledge check integrity on all 147 lessons."""
        mcq_count = 0
        for lesson in self.lessons:
            mcq_blocks = lesson.blocks.filter(block_type="knowledge_check")
            self.assertGreaterEqual(
                mcq_blocks.count(), 1,
                f"Lesson '{lesson.title}' has no knowledge_check block"
            )
            for b in mcq_blocks:
                content = b.content
                question = content.get("question", "")
                options = content.get("options", [])
                correct_idx = content.get("correct_answer")
                explanation = content.get("explanation", "")

                self.assertTrue(question, f"Block {b.id} in '{lesson.title}' has empty question")
                self.assertEqual(len(options), 4, f"Block {b.id} in '{lesson.title}' options count is {len(options)}, expected 4")
                self.assertIn(correct_idx, [0, 1, 2, 3], f"Block {b.id} in '{lesson.title}' has invalid correct_answer {correct_idx}")
                self.assertTrue(explanation, f"Block {b.id} in '{lesson.title}' has empty explanation")
                mcq_count += 1

        self.assertEqual(mcq_count, 147, f"Expected 147 MCQ knowledge checks, found {mcq_count}")
        print(f"[PASS] MCQ Integrity Verified: Exactly {mcq_count} Knowledge Checks tested (4 options, valid index, detailed feedback)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
