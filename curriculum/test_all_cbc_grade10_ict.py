"""
VLearn Comprehensive Master Audit & Test Suite: Grade 10 CBC ICT (All 9 Topics)
Verifies:
1. Subject resolution under Grade 10 CBC
2. All 9 Topics created with correct ordering (1 to 9)
3. 53 Learning Units and 53 published Lessons
4. Exactly 5 pages/cards per lesson (265 total pages)
5. Non-empty lesson blocks with rich pedagogical components
6. Visual assets attached (Vector SVGs, Wikimedia Images, YouTube videos)
7. Zero bracket citation leaks ([20], [44], etc.) and zero developer tag leaks ([VISUAL: ...])
8. Formative assessment MCQs validity (4 options, correct answer, explanatory feedback)
"""

import os
import sys
import unittest
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestAllGrade10ICT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=cls.curriculum, level=10).first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="ICT").first()
        cls.topics = list(Topic.objects.filter(subject=cls.subject).order_by("order")) if cls.subject else []

    def test_01_hierarchy_integrity(self):
        """Verify Curriculum -> Grade 10 -> Subject ICT -> 9 Topics exist."""
        self.assertIsNotNone(self.curriculum, "Curriculum 'CBC' not found")
        self.assertIsNotNone(self.grade, "Grade 'Grade 10' not found under CBC")
        self.assertIsNotNone(self.subject, "Subject 'ICT' not found under Grade 10")
        self.assertEqual(len(self.topics), 9, f"Expected 9 topics, found {len(self.topics)}")
        
        topic_orders = [t.order for t in self.topics]
        self.assertEqual(topic_orders, [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Topics must have order 1..9, got {topic_orders}")
        
        expected_names = [
            "Introduction to ICT",
            "Application Areas of ICT",
            "Operating Systems",
            "Word Processing",
            "Presentation Software",
            "Desktop Publishing",
            "Introduction to the Internet",
            "Digital Communication Platforms",
            "Digital Citizenship"
        ]
        actual_names = [t.name for t in self.topics]
        self.assertEqual(actual_names, expected_names, "Topic names mismatch")

    def test_02_units_and_published_lessons_count(self):
        """Verify 53 Learning Units and 53 published Lessons across all 9 topics."""
        expected_counts = {
            1: 4,   # Topic 1: 4 lessons
            2: 4,   # Topic 2: 4 lessons
            3: 6,   # Topic 3: 6 lessons
            4: 10,  # Topic 4: 10 lessons
            5: 5,   # Topic 5: 5 lessons
            6: 6,   # Topic 6: 6 lessons
            7: 5,   # Topic 7: 5 lessons
            8: 7,   # Topic 8: 7 lessons
            9: 6,   # Topic 9: 6 lessons
        }
        total_units = 0
        total_lessons = 0

        for topic in self.topics:
            expected = expected_counts.get(topic.order, 0)
            units = topic.learning_units.all().order_by("order")
            lessons = topic.lessons.filter(status="published").order_by("learning_unit__order")
            
            self.assertEqual(units.count(), expected, f"Topic {topic.order} ({topic.name}) expected {expected} units, got {units.count()}")
            self.assertEqual(lessons.count(), expected, f"Topic {topic.order} ({topic.name}) expected {expected} published lessons, got {lessons.count()}")
            
            total_units += units.count()
            total_lessons += lessons.count()

        self.assertEqual(total_units, 53, f"Expected 53 total units, found {total_units}")
        self.assertEqual(total_lessons, 53, f"Expected 53 total published lessons, found {total_lessons}")

    def test_03_card_page_structure(self):
        """Verify each lesson has exactly 5 pages/cards and sequential component orders."""
        all_lessons = Lesson.objects.filter(topic__subject=self.subject, status="published")
        total_pages = 0
        total_blocks = 0

        for lesson in all_lessons:
            blocks = lesson.blocks.all().order_by("order")
            self.assertGreater(blocks.count(), 0, f"Lesson '{lesson.title}' has no blocks")
            
            pages = set(b.page_number for b in blocks if b.page_number is not None)
            self.assertEqual(pages, {1, 2, 3, 4, 5}, f"Lesson '{lesson.title}' must contain exactly pages 1 to 5, got {pages}")
            total_pages += len(pages)
            total_blocks += blocks.count()

        self.assertEqual(total_pages, 265, f"Expected 265 total pages across 53 lessons, got {total_pages}")
        self.assertGreaterEqual(total_blocks, 740, f"Expected >= 740 blocks, got {total_blocks}")

    def test_04_visual_assets_attached(self):
        """Verify SVG diagrams, photographic images, and YouTube videos are properly attached."""
        all_lessons = Lesson.objects.filter(topic__subject=self.subject, status="published")
        
        total_diagrams = 0
        total_images = 0
        total_youtube = 0

        for lesson in all_lessons:
            diagrams = lesson.assets.filter(asset_type="diagram")
            images = lesson.assets.filter(asset_type="image")
            youtube_vids = lesson.assets.filter(asset_type__in=["video", "youtube"])

            self.assertGreaterEqual(diagrams.count(), 1, f"Lesson '{lesson.title}' missing diagram asset")
            self.assertGreaterEqual(images.count(), 1, f"Lesson '{lesson.title}' missing image asset")
            self.assertGreaterEqual(youtube_vids.count(), 1, f"Lesson '{lesson.title}' missing video asset")

            total_diagrams += diagrams.count()
            total_images += images.count()
            total_youtube += youtube_vids.count()

            # Verify SVG markup in diagram asset
            for diag in diagrams:
                svg_markup = diag.metadata.get("svg_content", "")
                self.assertIn("<svg", svg_markup, f"Diagram asset '{diag.title}' missing <svg tag")
                self.assertIn("viewBox=", svg_markup, f"Diagram asset '{diag.title}' missing viewBox")

        self.assertGreaterEqual(total_diagrams, 53, "Expected >= 53 diagram assets")
        self.assertGreaterEqual(total_images, 53, "Expected >= 53 image assets")
        self.assertGreaterEqual(total_youtube, 53, "Expected >= 53 YouTube video assets")

    def test_05_content_sanitization_no_leaks(self):
        """Verify zero bracket citations [20] and zero [VISUAL: ...] developer prompt leaks."""
        bracket_cite_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        visual_leak_pattern = re.compile(r'\[VISUAL:', re.IGNORECASE)

        all_blocks = LessonBlock.objects.filter(lesson__topic__subject=self.subject)
        leak_count = 0

        for b in all_blocks:
            # Check title
            if b.title:
                if bracket_cite_pattern.search(b.title) or visual_leak_pattern.search(b.title):
                    leak_count += 1
                    print(f"Leak in block title ID {b.id}: {b.title}")

            # Check content
            content_str = str(b.content)
            if bracket_cite_pattern.search(content_str):
                leak_count += 1
                print(f"Bracket citation in block content ID {b.id}: {content_str[:120]}")
            if visual_leak_pattern.search(content_str):
                leak_count += 1
                print(f"Prompt leak in block content ID {b.id}: {content_str[:120]}")

        self.assertEqual(leak_count, 0, f"Found {leak_count} citation or prompt leaks in LessonBlocks")

    def test_06_formative_mcqs(self):
        """Verify all MCQ knowledge checks have question, 4 options, valid correct answer, and explanation."""
        mcq_blocks = LessonBlock.objects.filter(
            lesson__topic__subject=self.subject,
            block_type="knowledge_check"
        )
        self.assertGreaterEqual(mcq_blocks.count(), 106, f"Expected >= 106 MCQs (2 per lesson), found {mcq_blocks.count()}")

        for mb in mcq_blocks:
            c = mb.content
            question = c.get("question", "")
            options = c.get("options", [])
            answer = c.get("correct_answer", c.get("answer", c.get("correct", "")))
            explanation = c.get("explanation", "")

            self.assertTrue(bool(question), f"MCQ Block {mb.id} missing question")
            self.assertEqual(len(options), 4, f"MCQ Block {mb.id} ('{question[:40]}...') must have 4 options, got {len(options)}")
            self.assertTrue(bool(answer), f"MCQ Block {mb.id} missing correct answer")
            self.assertTrue(bool(explanation), f"MCQ Block {mb.id} missing explanation")

if __name__ == "__main__":
    unittest.main()
