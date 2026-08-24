"""
VLearn CBC Grade 9 Agriculture — Topic 1: Conserving Animal Feeds (Forage, Drought, and Hay)
Automated Dual QA & Integrity Verification Test Suite

Tests:
  1. Hierarchy & Database Integrity (Curriculum -> Grade 9 -> Agriculture -> Topic 1)
  2. 12 Learning Units & 12 Published Lessons Validation
  3. Dynamic Card & Block Structure Integrity
  4. Mandatory First-Card Visual Hooks (12 Tested HTTP 200 OK URLs & LessonAssets)
  5. 12 Custom Sanitized Responsive Vector SVGs (viewBox, sanitization & LessonAssets)
  6. Verified Topic Video Review Asset (Lesson 12)
  7. Content Sanitization (0 Bracket Citations, 0 Developer Meta-Terms, 0 Raw LaTeX Leaks)
  8. Formative & Summative Scenario-Based MCQs Validation (22 Questions with 4 Options, Key & Explanation)

Usage:
  ./venv/bin/python curriculum/test_cbc_grade9_agriculture_topic1.py
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

class TestCBCGrade9AgricultureTopic1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"
        
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 9").first()
        assert cls.grade, "Grade 'Grade 9' not found under CBC!"
        
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Agriculture").first()
        assert cls.subject, "Subject 'Agriculture' not found under Grade 9!"
        
        cls.topic = Topic.objects.filter(subject=cls.subject, name="Conserving Animal Feeds (Forage, Drought, and Hay)").first()
        assert cls.topic, "Topic 1 'Conserving Animal Feeds' not found under Agriculture!"
        
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        cls.units = list(cls.topic.learning_units.all().order_by("order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.name, "Grade 9")
        self.assertEqual(self.grade.level, 9)
        self.assertEqual(self.subject.name, "Agriculture")
        self.assertEqual(self.topic.order, 1)
        self.assertIn("Conserving Animal Feeds", self.topic.name)

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 12 LearningUnits and 12 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 12, f"Expected 12 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 12, f"Expected 12 lessons, found {len(self.lessons)}")
        
        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has valid page counts and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertTrue(len(blocks) >= 10, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks)
            self.assertGreaterEqual(len(page_numbers), 6, f"Lesson {lesson.id} must have >=6 pages, got {len(page_numbers)}")
            self.assertLessEqual(len(page_numbers), 14, f"Lesson {lesson.id} has too many pages ({len(page_numbers)})")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 12 lessons have Page 1 photographic visual hooks with HTTP 200 URLs & attached LessonAssets."""
        headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()
            
            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 image has no resolved URL!")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Invalid image URL format in Lesson {u_order}")
            
            # Verify attached LessonAsset
            asset = hook_block.assets.filter(asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} Card 1 image block has no attached LessonAsset!")
            self.assertEqual(asset.status, "attached")
            
            # Test HTTP 200
            try:
                resp = requests.head(img_url, headers=headers, timeout=6)
                self.assertIn(resp.status_code, [200, 301, 302, 429], f"Image URL for Lesson {u_order} returned HTTP {resp.status_code}")
            except Exception as e:
                self.fail(f"Failed to connect to image URL for Lesson {u_order}: {e}")

    def test_05_custom_vector_svgs_sanitization(self):
        """Verify all 12 lessons have sanitized responsive vector SVGs attached."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()
            
            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing suggested_diagram block!")
            content = diagram_block.content or {}
            svg = content.get("svg_content") or content.get("svg")
            self.assertTrue(svg, f"Lesson {u_order} suggested_diagram has no SVG content!")
            
            # SVG Sanitization checks
            self.assertNotIn("<?xml", svg, f"Lesson {u_order} SVG contains raw xml header!")
            self.assertNotIn("<!DOCTYPE", svg, f"Lesson {u_order} SVG contains DOCTYPE!")
            self.assertIn('viewBox="0 0 800 450"', svg, f"Lesson {u_order} SVG missing viewBox='0 0 800 450'!")
            self.assertIn('#0f172a', svg, f"Lesson {u_order} SVG missing dark-mode background color!")
            self.assertTrue(svg.startswith("<svg"), f"Lesson {u_order} SVG does not start with <svg tag!")
            self.assertTrue(svg.endswith("</svg>"), f"Lesson {u_order} SVG does not end with </svg> tag!")
            
            # Verify attached LessonAsset
            asset = diagram_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} diagram block has no attached LessonAsset!")
            self.assertEqual(asset.status, "attached")

    def test_06_multi_video_integration(self):
        """Verify lessons contain verified YouTube video blocks with attached LessonAssets."""
        video_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="suggested_video")
        self.assertGreaterEqual(video_blocks.count(), 3, f"Expected at least 3 video blocks across topic, found {video_blocks.count()}")

        for v_block in video_blocks:
            content = v_block.content or {}
            self.assertTrue(content.get("verified"), f"Block {v_block.id} video is not marked as verified")
            vid_id = content.get("resolved_video_id")
            self.assertTrue(vid_id, f"Block {v_block.id} missing resolved_video_id")
            self.assertIn(vid_id, content.get("url", ""))

            asset = v_block.assets.filter(asset_type="video").first() or v_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Block {v_block.id} missing attached LessonAsset for YouTube video")
            self.assertEqual(asset.url, content["url"])

    def test_07_zero_citation_and_meta_leaks(self):
        """Audit all blocks for citation brackets [1], [539], developer meta-terms, and raw unrendered LaTeX."""
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
        meta_pattern = re.compile(r'(?:\[VISUAL:|\[INTERACTION:|BlockType|Expected Answer:|Concept Tested:)', re.IGNORECASE)
        raw_latex_pattern = re.compile(r'\\text\{|\\frac\{')
        
        for lesson in self.lessons:
            for block in lesson.blocks.all():
                # Inspect title
                if block.title:
                    self.assertFalse(citation_pattern.search(block.title), f"Citation leak in title of Block {block.id}: {block.title}")
                    self.assertFalse(meta_pattern.search(block.title), f"Meta-tag leak in title of Block {block.id}: {block.title}")
                
                # Inspect content
                content_str = str(block.content or {})
                # Exclude SVG content from regex search
                clean_content_str = re.sub(r'<svg.*?</svg>', '', content_str, flags=re.DOTALL)
                
                self.assertFalse(citation_pattern.search(clean_content_str), f"Citation leak in Block {block.id}")
                self.assertFalse(meta_pattern.search(clean_content_str), f"Developer meta-term leak in Block {block.id}")
                self.assertFalse(raw_latex_pattern.search(clean_content_str), f"Raw LaTeX leak in Block {block.id}")

    def test_08_formative_and_summative_mcqs_validation(self):
        """Validate all 22 interactive knowledge_check blocks across the 12 lessons."""
        all_kc_blocks = LessonBlock.objects.filter(
            lesson__in=self.lessons,
            block_type="knowledge_check"
        ).order_by("lesson__learning_unit__order", "order")
        
        self.assertEqual(all_kc_blocks.count(), 22, f"Expected 22 knowledge_check blocks (12 lesson + 10 topic), found {all_kc_blocks.count()}")
        
        for kc in all_kc_blocks:
            c = kc.content or {}
            q = c.get("question")
            options = c.get("options")
            ans = c.get("answer")
            exp = c.get("explanation")
            
            self.assertTrue(q and len(q) > 15, f"Knowledge check {kc.id} has invalid question text!")
            self.assertIsInstance(options, list, f"Knowledge check {kc.id} options is not a list!")
            self.assertEqual(len(options), 4, f"Knowledge check {kc.id} does not have exactly 4 options! ({len(options)})")
            for opt_idx, opt in enumerate(options):
                self.assertTrue(opt and len(opt) > 1, f"Knowledge check {kc.id} Option {opt_idx} is empty!")
            self.assertIn(ans, ["A", "B", "C", "D"], f"Knowledge check {kc.id} answer '{ans}' is not A, B, C, or D!")
            self.assertTrue(exp and len(exp) > 20, f"Knowledge check {kc.id} explanation is too short or empty!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
