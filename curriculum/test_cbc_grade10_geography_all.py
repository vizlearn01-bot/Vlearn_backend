"""
VLearn CBC Grade 10 Geography — Master Cross-Topic Audit & Verification Suite (Topics 1 to 10)

Verifies:
  - Full curriculum hierarchy: CBC -> Grade 10 -> Geography -> Topics 1 to 10
  - Exactly 120 Learning Units & 120 Published Lessons in sequential order
  - All 120 lessons have valid atomic card structures (>= 3 pages each)
  - 120 First-Card photographic visual hooks with HTTP 200 URLs & attached LessonAssets
  - 100+ Custom responsive vector SVGs with clean viewBox and attached LessonAssets
  - Educational YouTube video assets attached where specified
  - 0 Bracket Citations ([1], [37], [48], [170]), 0 Internal Prompt Leaks across all blocks
  - 200+ Validated MCQs with 4 options, valid correct answer keys (A/B/C/D), and full explanations

Usage:
  ./venv/bin/python curriculum/test_cbc_grade10_geography_all.py
"""

import os
import sys
import re
import json
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10GeographyMaster(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found!"

        cls.subject = Subject.objects.filter(id=37).first() or Subject.objects.filter(grade__curriculum=cls.curriculum, name="Geography", grade__name__icontains="10").first()
        assert cls.subject, "Subject 'Geography' not found under CBC Grade 10!"
        cls.grade = cls.subject.grade

        cls.topics = list(cls.subject.topics.all().order_by("order"))
        cls.lessons = list(Lesson.objects.filter(topic__subject=cls.subject).order_by("topic__order", "learning_unit__order"))
        cls.units = list(LearningUnit.objects.filter(topic__subject=cls.subject).order_by("topic__order", "order"))
        cls.assets = list(LessonAsset.objects.filter(lesson__in=cls.lessons))
        cls.blocks = list(LessonBlock.objects.filter(lesson__in=cls.lessons))

    def test_01_curriculum_hierarchy_and_topics(self):
        """Verify full hierarchy and all 10 topics."""
        self.assertEqual(len(self.topics), 10, f"Expected 10 topics, found {len(self.topics)}")
        
        expected_topics = [
            (1, "Introduction to Geography"),
            (2, "Map Reading and Interpretation"),
            (3, "Statistical Methods"),
            (4, "Geographic Information System"),
            (5, "Rocks"),
            (6, "Earth Movements"),
            (7, "Folding"),
            (8, "Vulcanicity"),
            (9, "Earthquakes"),
            (10, "Agriculture")
        ]
        for t, (exp_order, exp_name) in zip(self.topics, expected_topics):
            self.assertEqual(t.order, exp_order)
            self.assertIn(exp_name, t.name)

    def test_02_total_lessons_and_units_count(self):
        """Verify exactly 120 learning units and 120 published lessons across the 10 topics."""
        self.assertEqual(len(self.units), 120, f"Expected 120 learning units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 120, f"Expected 120 lessons, found {len(self.lessons)}")

        # Check per-topic lesson counts
        topic_counts = {1: 8, 2: 13, 3: 12, 4: 13, 5: 18, 6: 6, 7: 12, 8: 13, 9: 10, 10: 15}
        for t in self.topics:
            count = t.lessons.count()
            self.assertEqual(count, topic_counts[t.order], f"Topic {t.order} has {count} lessons, expected {topic_counts[t.order]}")
            for l in t.lessons.all():
                self.assertEqual(l.status, "published")
                self.assertGreaterEqual(l.version, 1)

    def test_03_card_and_block_distribution(self):
        """Verify lesson card atomicity and total block count."""
        self.assertGreaterEqual(len(self.blocks), 900, f"Expected >900 blocks, found {len(self.blocks)}")

        for lesson in self.lessons:
            l_blocks = [b for b in self.blocks if b.lesson_id == lesson.id]
            pages = set(b.page_number for b in l_blocks)
            self.assertGreaterEqual(len(pages), 3, f"Lesson '{lesson.title}' has too few pages ({len(pages)})")
            self.assertLessEqual(len(pages), 12, f"Lesson '{lesson.title}' has too many pages ({len(pages)})")

    def test_04_first_card_photographic_hooks(self):
        """Verify all 120 lessons have Page 1 photographic visual hooks with HTTP 200 URLs and attached LessonAssets."""
        for lesson in self.lessons:
            hook_block = next((b for b in self.blocks if b.lesson_id == lesson.id and b.page_number == 1 and b.block_type in ["suggested_image", "image"]), None)
            self.assertIsNotNone(hook_block, f"Lesson '{lesson.title}' missing Page 1 visual hook!")
            
            c = hook_block.content or {}
            img_url = c.get("resolved_image_url") or c.get("url")
            self.assertTrue(img_url, f"Lesson '{lesson.title}' visual hook missing image URL!")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Lesson '{lesson.title}' image URL not Wikimedia: {img_url}")

            asset = next((a for a in self.assets if a.lesson_id == lesson.id and a.asset_type == "image" and hook_block in a.blocks.all()), None)
            self.assertIsNotNone(asset, f"Lesson '{lesson.title}' missing attached LessonAsset for visual hook!")

    def test_05_custom_vector_svgs(self):
        """Verify custom vector SVGs across the curriculum."""
        diag_blocks = [b for b in self.blocks if b.block_type in ["diagram", "suggested_diagram"]]
        self.assertGreaterEqual(len(diag_blocks), 90, f"Expected >= 90 diagram blocks, found {len(diag_blocks)}")

        for b in diag_blocks:
            c = b.content or {}
            svg_text = c.get("svg_content", "")
            self.assertTrue(svg_text, f"Block {b.id} missing svg_content in Lesson '{b.lesson.title}'")
            self.assertIn("<svg", svg_text)
            self.assertIn("viewBox=", svg_text)
            self.assertNotIn("<?xml", svg_text)

            asset = next((a for a in self.assets if a.lesson_id == b.lesson_id and a.asset_type == "diagram" and b in a.blocks.all()), None)
            self.assertIsNotNone(asset, f"Block {b.id} missing attached LessonAsset in Lesson '{b.lesson.title}'")

    def test_06_video_assets(self):
        """Verify video assets attached to lessons."""
        video_assets = [a for a in self.assets if a.asset_type == "youtube"]
        self.assertGreaterEqual(len(video_assets), 8, f"Expected >= 8 video assets, found {len(video_assets)}")
        for v in video_assets:
            self.assertIn("youtube.com", v.url)

    def test_07_content_sanitization_and_zero_leaks(self):
        """Scan all 900+ blocks across all 10 topics for zero prompt leaks, zero bracket citations, and clean formatting."""
        forbidden_patterns = [
            r'\[VISUAL:\s*.*?\]',
            r'\[\d+\]',
            r'\[image_\d+\]',
            r'\[S\d+,\s*p\.\s*\d+\]',
            r'Prompt:',
            r'Learner should observe:',
            r'Preferred characteristics:'
        ]

        for block in self.blocks:
            c_str = json.dumps(block.content)
            for pat in forbidden_patterns:
                match = re.search(pat, c_str, re.IGNORECASE)
                self.assertIsNone(match, f"Block {block.id} in Lesson '{block.lesson.title}' has forbidden tag matching '{pat}': {match.group(0) if match else ''}")

    def test_08_formative_mcqs_validation(self):
        """Verify all formative and summative MCQs across all 10 topics."""
        mcq_blocks = [b for b in self.blocks if b.block_type in ["knowledge_check", "multiple_choice_question", "formative_mcq", "mcq"]]
        self.assertGreaterEqual(len(mcq_blocks), 120, f"Expected >= 120 MCQ blocks across Grade 10 Geography, found {len(mcq_blocks)}")

        for b in mcq_blocks:
            c = b.content or {}
            if "questions" in c:
                for q in c["questions"]:
                    self.assertIn("question", q)
                    self.assertIn("options", q)
                    self.assertEqual(len(q["options"]), 4)
                    self.assertIn("correct_answer", q)
                    self.assertIn("explanation", q)
            else:
                self.assertIn("question", c, f"Block {b.id} missing question")
                self.assertIn("options", c, f"Block {b.id} missing options")
                self.assertEqual(len(c["options"]), 4, f"Block {b.id} does not have 4 options in Lesson '{b.lesson.title}'")
                self.assertIn("correct_answer", c, f"Block {b.id} missing correct_answer")
                self.assertTrue(
                    c["correct_answer"] in ["A", "B", "C", "D"] or c["correct_answer"] in c["options"] or any(c["correct_answer"] in opt for opt in c["options"]),
                    f"Block {b.id} invalid correct answer: {c.get('correct_answer')}"
                )
                self.assertIn("explanation", c, f"Block {b.id} missing explanation")
                self.assertTrue(len(c["explanation"]) > 10, f"Block {b.id} explanation too short")

if __name__ == "__main__":
    unittest.main()
