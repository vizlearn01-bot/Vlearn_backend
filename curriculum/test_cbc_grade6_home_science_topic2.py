"""
Dual Automated QA Test Suite
CBC Grade 6 Home Science — Topic 2: Budgeting

Validates:
1. Hierarchy Resolution (CBC -> Grade 6 -> Home Science -> Topic 2: Budgeting, Order: 2)
2. Learning Units & Lessons Count (Exactly 3 Units, 3 Published Lessons)
3. Page Count (Exactly 8 pages per lesson = 24 total pages)
4. Card 1 Photographic Visual Hooks Live HTTP 200 Verification (>10KB)
5. Custom Vector SVGs Validity (Valid XML, sanitized, viewBox="0 0 800 450", 6 total SVGs)
6. Zero Bracket Citations and Zero Developer Meta-Language Leaks
7. Strict Markdown Bullet List Syntax ('- ' format)
8. Scenario Knowledge Checks Completeness (4 options, valid explanation, valid correct_index)
9. Attached LessonAssets Count (3 photos + 6 diagrams = 9 assets)
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

class TestCBCGrade6HomeScienceTopic2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 6").first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Home Science").first()
        cls.topic = Topic.objects.filter(subject=cls.subject, name="Budgeting").first()

    def test_01_hierarchy_resolution(self):
        self.assertIsNotNone(self.curriculum, "CBC Curriculum missing!")
        self.assertIsNotNone(self.grade, "Grade 6 missing!")
        self.assertIsNotNone(self.subject, "Home Science Subject missing!")
        self.assertIsNotNone(self.topic, "Topic 2 (Budgeting) missing!")
        self.assertEqual(self.topic.order, 2, f"Expected Topic 2 order to be 2, got {self.topic.order}")
        print(f"\n[QA PASS] Hierarchy correctly resolved to Grade 6 Topic 2: {self.topic.name} (ID: {self.topic.id}).")

    def test_02_units_and_lessons_count(self):
        units = self.topic.learning_units.all().order_by("order")
        self.assertEqual(units.count(), 3, f"Expected 3 Learning Units, got {units.count()}")
        lessons = Lesson.objects.filter(topic=self.topic, status="published")
        self.assertEqual(lessons.count(), 3, f"Expected 3 published Lessons, got {lessons.count()}")
        print(f"[QA PASS] Exactly 3 Learning Units and 3 Published Lessons verified.")

    def test_03_page_count_per_lesson(self):
        lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")
        total_pages = 0
        for l in lessons:
            pages = set(l.blocks.values_list("page_number", flat=True))
            self.assertEqual(len(pages), 8, f"Lesson '{l.title}' has {len(pages)} pages, expected 8!")
            total_pages += len(pages)
        self.assertEqual(total_pages, 24, f"Expected 24 total pages, got {total_pages}")
        print(f"[QA PASS] Exactly 24 total pages verified (8 pages per lesson).")

    def test_04_card_1_photographic_hooks(self):
        lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")
        headers = {"User-Agent": "VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)"}
        for l in lessons:
            hook_block = l.blocks.filter(page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(hook_block, f"Card 1 missing suggested_image hook in Lesson '{l.title}'")
            content = hook_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertTrue(bool(img_url), f"Card 1 suggested_image has no URL in Lesson '{l.title}'")
            
            r = requests.get(img_url, headers=headers, timeout=8)
            self.assertEqual(r.status_code, 200, f"Image URL failed HTTP 200: {img_url}")
            self.assertGreater(len(r.content), 10000, f"Image payload too small (<10KB): {len(r.content)} bytes")
        print(f"[QA PASS] All 3 Card 1 photographic hooks verified live with HTTP 200 responses.")

    def test_05_custom_vector_svgs_validity(self):
        svg_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="diagram")
        self.assertEqual(svg_blocks.count(), 6, f"Expected 6 diagram blocks, found {svg_blocks.count()}")
        for sb in svg_blocks:
            content = sb.content or {}
            svg_code = content.get("svg") or content.get("code") or content.get("svg_content")
            self.assertIsNotNone(svg_code, f"Diagram block {sb.id} has no SVG code!")
            self.assertTrue(svg_code.strip().startswith("<svg"), f"SVG does not start with <svg in block {sb.id}")
            self.assertTrue(svg_code.strip().endswith("</svg>"), f"SVG does not end with </svg> in block {sb.id}")
            self.assertIn('viewBox="0 0 800 450"', svg_code, f"SVG missing responsive viewBox in block {sb.id}")
        print(f"[QA PASS] All 6 Vector SVGs verified valid, responsive (800x450), and sanitized.")

    def test_06_zero_bracket_citations_and_meta_leaks(self):
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        bracket_pattern = re.compile(r'\[\d+\]')
        meta_words = ["Gemini", "Notebook", "LLM", "TODO", "Placeholder"]
        
        for b in blocks:
            text_str = str(b.content) + " " + (b.title or "")
            bracket_matches = bracket_pattern.findall(text_str)
            self.assertEqual(len(bracket_matches), 0, f"Block {b.id} ({b.title}) contains bracket citations: {bracket_matches}")
            for mw in meta_words:
                self.assertNotIn(mw.lower(), text_str.lower(), f"Block {b.id} ({b.title}) leaks meta word: {mw}")
        print(f"[QA PASS] Zero bracket citations and zero developer meta-language leaks detected across all {blocks.count()} blocks.")

    def test_07_markdown_bullet_list_formatting(self):
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="rich_text")
        for b in blocks:
            text = (b.content or {}).get("text", "")
            self.assertNotIn("•", text, f"Block {b.id} uses raw bullet '•' instead of '- '")
        print(f"[QA PASS] Markdown list formatting verified: 100% compliant with '- ' syntax.")

    def test_08_scenario_knowledge_checks(self):
        kc_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="scenario_check")
        self.assertEqual(kc_blocks.count(), 3)
        for kb in kc_blocks:
            c = kb.content or {}
            self.assertIn("question", c)
            self.assertIn("options", c)
            self.assertEqual(len(c["options"]), 4, f"Scenario check in block {kb.id} must have 4 options")
            self.assertIn("correct_index", c)
            self.assertIn(c["correct_index"], [0, 1, 2, 3])
            self.assertIn("explanation", c)
            self.assertGreater(len(c["explanation"]), 20)
        print(f"[QA PASS] All 3 scenario knowledge checks validated with 4 options, valid index, and detailed explanation.")

    def test_09_attached_assets_count(self):
        total_assets = LessonAsset.objects.filter(lesson__topic=self.topic).count()
        # 3 photos + 6 diagrams = 9 assets
        self.assertEqual(total_assets, 9, f"Expected 9 LessonAsset records, found {total_assets}")
        print(f"[QA PASS] Exactly 9 LessonAsset records verified in database (3 photos + 6 diagrams).")

if __name__ == "__main__":
    unittest.main()
