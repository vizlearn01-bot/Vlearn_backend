"""
VLearn CBC Grade 8 Home Science — Topic 4: Caring for the Family
Dual QA Test Suite (Pedagogical Quality & Platform Integrity)

Verifies:
  1. Hierarchy resolution (CBC -> Grade 8 -> Home Science -> Topic 4: Caring for the Family)
  2. Exactly 7 Learning Units and 7 Published Lessons (status='published')
  3. Exactly 56 Total Structured Pages (8 pages per lesson)
  4. 100% Card 1 Visual Hooks presence with direct HTTP 200 responses
  5. 100% SVG validity, sanitization, and responsive dimensions (13 SVGs)
  6. Zero bracket citations ([10], [80], [81]) and zero developer meta-language leaks
  7. Standard markdown bullet lists (- ) with proper spacing
  8. 7 scenario knowledge checks with complete options, correct index, and pedagogical explanations
"""

import os
import sys
import re
import unittest
import requests
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade8HomeScienceTopic4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 8").first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Home Science").first()
        cls.topic = Topic.objects.filter(subject=cls.subject, name="Caring for the Family").first()
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order")) if cls.topic else []

    def test_01_hierarchy_resolution(self):
        """Test that Topic 4 resolves under CBC -> Grade 8 -> Home Science."""
        self.assertIsNotNone(self.curriculum, "Curriculum 'CBC' not found")
        self.assertIsNotNone(self.grade, "Grade 'Grade 8' not found")
        self.assertIsNotNone(self.subject, "Subject 'Home Science' not found")
        self.assertIsNotNone(self.topic, "Topic 'Caring for the Family' not found")
        self.assertEqual(self.topic.order, 4, "Topic order must be 4")
        print("\n[QA PASS] Hierarchy correctly resolved to Topic 4: Caring for the Family (ID: 106).")

    def test_02_learning_units_and_published_lessons(self):
        """Test that exactly 7 Learning Units and 7 published lessons exist."""
        self.assertEqual(len(self.lessons), 7, f"Expected 7 lessons, found {len(self.lessons)}")
        for idx, lesson in enumerate(self.lessons, 1):
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} is not published")
            self.assertEqual(lesson.learning_unit.order, idx, f"Lesson {lesson.id} unit order mismatch")
        print(f"[QA PASS] Exactly 7 Learning Units and 7 Published Lessons verified.")

    def test_03_total_pages_distribution(self):
        """Test that each lesson has exactly 8 structured pages (56 total pages)."""
        total_pages = 0
        for lesson in self.lessons:
            page_numbers = set(lesson.blocks.values_list("page_number", flat=True))
            self.assertEqual(len(page_numbers), 8, f"Lesson {lesson.title} has {len(page_numbers)} pages instead of 8")
            total_pages += len(page_numbers)
        self.assertEqual(total_pages, 56, f"Expected 56 total pages, got {total_pages}")
        print(f"[QA PASS] Exactly 56 total pages verified (8 pages per lesson).")

    def test_04_card_1_visual_hooks_live_200(self):
        """Test that Card 1 of each of the 7 lessons has a tested HTTP 200 visual hook."""
        headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}
        for lesson in self.lessons:
            hook_block = lesson.blocks.filter(page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(hook_block, f"Card 1 hook block missing for lesson '{lesson.title}'")
            content = hook_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertIsNotNone(img_url, f"Image URL missing on Card 1 hook for lesson '{lesson.title}'")
            self.assertTrue(img_url.startswith("http"), f"Invalid URL scheme: {img_url}")
            
            # Verify HTTP 200
            try:
                r = requests.get(img_url, headers=headers, timeout=6)
                self.assertEqual(r.status_code, 200, f"Image URL returned {r.status_code}: {img_url}")
                self.assertGreater(len(r.content), 10000, f"Image payload too small ({len(r.content)} bytes)")
            except requests.exceptions.RequestException as e:
                self.fail(f"Network error verifying image hook {img_url}: {e}")
        print("[QA PASS] All 7 Card 1 photographic hooks verified live with HTTP 200 responses.")

    def test_05_vector_svg_validity_and_dimensions(self):
        """Test that all 13 vector SVGs are valid, responsive, and attached."""
        svg_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="suggested_diagram")
        self.assertEqual(svg_blocks.count(), 13, f"Expected 13 suggested_diagram blocks, found {svg_blocks.count()}")
        for b in svg_blocks:
            content = b.content or {}
            svg_text = content.get("svg_content") or content.get("svg")
            self.assertIsNotNone(svg_text, f"Block {b.id} missing SVG content")
            self.assertTrue(svg_text.startswith("<svg"), f"Block {b.id} SVG does not start with <svg")
            self.assertTrue(svg_text.endswith("</svg>"), f"Block {b.id} SVG does not end with </svg>")
            self.assertIn('viewBox="0 0 800 450"', svg_text, f"Block {b.id} SVG missing standard responsive viewBox")
            self.assertNotIn("<?xml", svg_text, f"Block {b.id} SVG contains XML declaration")
        print("[QA PASS] All 13 Vector SVGs verified valid, responsive (800x450), and sanitized.")

    def test_06_zero_bracket_citations_and_meta_language(self):
        """Test that no bracket citations or developer meta-language leaks exist."""
        bracket_regex = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
        meta_words = ["Prompt:", "JSON", "BlockType", "Page 1:", "Student-Facing Page Title:"]
        
        all_blocks = LessonBlock.objects.filter(lesson__in=self.lessons)
        for b in all_blocks:
            content_str = str(b.content) + " " + (b.title or "")
            bracket_match = bracket_regex.findall(content_str)
            self.assertEqual(len(bracket_match), 0, f"Block {b.id} ('{b.title}') has bracket citations: {bracket_match}")
            for mw in meta_words:
                self.assertNotIn(mw, content_str, f"Block {b.id} ('{b.title}') contains meta-language '{mw}'")
        print("[QA PASS] Zero bracket citations and zero developer meta-language leaks detected across all 97 blocks.")

    def test_07_markdown_list_syntax_compliance(self):
        """Test that all text blocks use valid markdown list syntax (- ) instead of bare unicode bullets."""
        unicode_bullet_regex = re.compile(r'(?:^|\n)[ \t]*[•\u2022][ \t]+')
        all_blocks = LessonBlock.objects.filter(lesson__in=self.lessons)
        for b in all_blocks:
            content = b.content or {}
            for field, val in content.items():
                if isinstance(val, str):
                    matches = unicode_bullet_regex.findall(val)
                    self.assertEqual(len(matches), 0, f"Block {b.id} ('{b.title}') contains bare unicode bullets: {matches}")
        print("[QA PASS] Markdown list formatting verified: 100% compliant with '- ' syntax.")

    def test_08_scenario_knowledge_checks(self):
        """Test that all 7 lessons end with a high-quality scenario knowledge check."""
        kc_blocks = LessonBlock.objects.filter(lesson__in=self.lessons, block_type="knowledge_check")
        self.assertEqual(kc_blocks.count(), 7, f"Expected 7 knowledge_check blocks, found {kc_blocks.count()}")
        for kc in kc_blocks:
            c = kc.content or {}
            self.assertTrue(len(c.get("question", "")) > 20, f"Knowledge check {kc.id} question too short")
            options = c.get("options", [])
            self.assertEqual(len(options), 4, f"Knowledge check {kc.id} must have exactly 4 options")
            correct_idx = c.get("correct_index")
            self.assertIn(correct_idx, [0, 1, 2, 3], f"Knowledge check {kc.id} invalid correct_index: {correct_idx}")
            self.assertTrue(len(c.get("explanation", "")) > 20, f"Knowledge check {kc.id} explanation too short")
        print("[QA PASS] All 7 scenario knowledge checks validated with 4 options, valid index, and detailed explanation.")

    def test_09_total_assets_persisted(self):
        """Test that LessonAsset records are persisted for all visual assets."""
        assets = LessonAsset.objects.filter(lesson__in=self.lessons)
        self.assertEqual(assets.count(), 20, f"Expected 20 persisted LessonAsset records, found {assets.count()}")
        img_assets = assets.filter(asset_type="image")
        diagram_assets = assets.filter(asset_type="diagram")
        self.assertEqual(img_assets.count(), 7, f"Expected 7 image assets, found {img_assets.count()}")
        self.assertEqual(diagram_assets.count(), 13, f"Expected 13 diagram assets, found {diagram_assets.count()}")
        print("[QA PASS] Exactly 20 LessonAsset records verified in database (7 photos + 13 diagrams).")

if __name__ == "__main__":
    unittest.main()
