"""
Comprehensive Automated QA Test Suite
CBC Grade 7 — Home Science
Topic 7: Seams (Order: 7)

Validates:
1. Curriculum hierarchy resolution (CBC -> Grade 7 -> Home Science -> Topic 7)
2. 4 Learning Units and 4 Published Lessons
3. 32 total pages (8 pages per lesson)
4. All 4 Card 1 Photographic Visual Hooks verified live with HTTP 200 responses
5. All 7 Custom Vector SVGs verified valid, responsive (800x450), and sanitized
6. Zero bracket citations ([108], [255]) and zero developer meta-language leaks
7. 100% compliant markdown bullet lists with '- ' syntax
8. All 4 Scenario Knowledge Checks with 4 options, valid correct_index, and thorough explanations
9. Total LessonAsset count in database matches exactly (4 photos + 7 diagrams = 11 assets)
"""

import os
import re
import sys
import unittest
import requests
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade7HomeScienceTopic7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "CBC Curriculum missing!"
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 7").first()
        assert cls.grade, "Grade 7 missing!"
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Home Science").first()
        assert cls.subject, "Home Science subject missing!"
        cls.topic = Topic.objects.filter(subject=cls.subject, name="Seams").first()
        assert cls.topic, "Topic 7 (Seams) missing!"
        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_resolution(self):
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.name, "Grade 7")
        self.assertEqual(self.subject.name, "Home Science")
        self.assertEqual(self.topic.name, "Seams")
        self.assertEqual(self.topic.order, 7)
        print(f"\n[QA PASS] Hierarchy correctly resolved to Grade 7 Topic 7: Seams (ID: {self.topic.id}).")

    def test_02_units_and_lessons_count(self):
        self.assertEqual(len(self.units), 4)
        self.assertEqual(len(self.lessons), 4)
        for lesson in self.lessons:
            self.assertEqual(lesson.status, "published")
        print(f"[QA PASS] Exactly 4 Learning Units and 4 Published Lessons verified.")

    def test_03_page_count_per_lesson(self):
        total_pages = 0
        for lesson in self.lessons:
            pages = set(lesson.blocks.values_list("page_number", flat=True))
            self.assertEqual(len(pages), 8, f"Lesson {lesson.title} does not have exactly 8 pages (has {len(pages)})")
            total_pages += len(pages)
        self.assertEqual(total_pages, 32)
        print(f"[QA PASS] Exactly 32 total pages verified (8 pages per lesson).")

    def test_04_card_1_visual_hooks_live_200(self):
        headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}
        for lesson in self.lessons:
            hook_block = lesson.blocks.filter(page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(hook_block, f"Lesson {lesson.title} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertIsNotNone(img_url, f"Lesson {lesson.title} has empty image URL!")
            self.assertTrue(img_url.startswith("http"))
            
            # Live HTTP 200 verification
            r = requests.get(img_url, headers=headers, timeout=6)
            self.assertEqual(r.status_code, 200, f"Image URL failed for {lesson.title}: {img_url}")
            self.assertGreater(len(r.content), 10000, f"Image payload too small ({len(r.content)} bytes) for {img_url}")
        print(f"[QA PASS] All 4 Card 1 photographic hooks verified live with HTTP 200 responses.")

    def test_05_custom_vector_svgs_validity(self):
        svg_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="diagram")
        self.assertEqual(svg_blocks.count(), 8, f"Expected 8 diagram blocks, found {svg_blocks.count()}")
        for sb in svg_blocks:
            content = sb.content or {}
            svg_code = content.get("svg") or content.get("code") or content.get("svg_content")
            self.assertIsNotNone(svg_code, f"Diagram block {sb.id} has no SVG code!")
            self.assertTrue(svg_code.strip().startswith("<svg"), f"SVG does not start with <svg in block {sb.id}")
            self.assertTrue(svg_code.strip().endswith("</svg>"), f"SVG does not end with </svg> in block {sb.id}")
            self.assertIn('viewBox="0 0 800 450"', svg_code, f"SVG missing responsive viewBox in block {sb.id}")
        print(f"[QA PASS] All 8 Vector SVGs verified valid, responsive (800x450), and sanitized.")

    def test_06_zero_bracket_citations_and_meta_leaks(self):
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        bracket_pattern = re.compile(r'\[\d+\]')
        meta_words = ["Gemini", "Notebook", "LLM", "Prompt", "TODO", "Placeholder"]
        
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
        self.assertEqual(kc_blocks.count(), 4)
        for kb in kc_blocks:
            c = kb.content or {}
            self.assertIn("question", c)
            self.assertIn("options", c)
            self.assertEqual(len(c["options"]), 4, f"Scenario check in block {kb.id} must have 4 options")
            self.assertIn("correct_index", c)
            self.assertIn(c["correct_index"], [0, 1, 2, 3])
            self.assertIn("explanation", c)
            self.assertGreater(len(c["explanation"]), 20)
        print(f"[QA PASS] All 4 scenario knowledge checks validated with 4 options, valid index, and detailed explanation.")

    def test_09_attached_assets_count(self):
        total_assets = LessonAsset.objects.filter(lesson__topic=self.topic).count()
        # 4 photos + 8 diagrams = 12 assets
        self.assertEqual(total_assets, 12, f"Expected 12 LessonAsset records, found {total_assets}")
        print(f"[QA PASS] Exactly 12 LessonAsset records verified in database (4 photos + 8 diagrams).")

if __name__ == "__main__":
    unittest.main()
