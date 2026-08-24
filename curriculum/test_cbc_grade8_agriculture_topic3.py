"""
Automated Quality Assurance Test Suite for CBC Grade 8 Agriculture — Topic 3: Kitchen and Backyard Gardening
(Deep Pedagogical & Multi-Video Edition)

Curriculum: CBC -> Grade 8 -> Agriculture -> Topic 3: Kitchen and Backyard Gardening

Test Coverage:
  1. Hierarchy and Topic Configuration Integrity (Grade 8, Topic Order: 3)
  2. Exactly 7 LearningUnits and 7 Published Lessons
  3. Dynamic Page and Block Counts & Structural Consistency (Deep Pages & Blocks)
  4. Card 1 Photographic Visual Hooks (Verified URLs, Attributions, Attached LessonAssets)
  5. Custom Responsive Vector SVGs (viewBox, sanitization, attached LessonAssets)
  6. Multi-Video Integration (Videos across Lessons 2, 5, and 7 with attached LessonAssets)
  7. Zero Citation Bracket Leaks, Zero Developer Meta-Tags, Zero Raw LaTeX
  8. Formative (7) and Summative (10) MCQ Validation (17 Total Knowledge Checks)

Run:
  ./venv/bin/python curriculum/test_cbc_grade8_agriculture_topic3.py
"""

import os
import sys
import re
import json
import requests
import unittest
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade8AgricultureTopic3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 8").first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Agriculture").first()
        cls.topic_name = "Kitchen and Backyard Gardening"
        cls.topic = Topic.objects.filter(subject=cls.subject, name=cls.topic_name).first()
        if cls.topic:
            cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))
        else:
            cls.lessons = []

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertIsNotNone(self.curriculum, "Curriculum 'CBC' must exist")
        self.assertIsNotNone(self.grade, "Grade 'Grade 8' must exist under CBC")
        self.assertEqual(self.grade.level, 8, "Grade 8 level must be 8")
        self.assertIsNotNone(self.subject, "Subject 'Agriculture' must exist under Grade 8")
        self.assertIsNotNone(self.topic, f"Topic '{self.topic_name}' must exist under Agriculture")
        self.assertEqual(self.topic.order, 3, "Topic 3 order must be 3")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 7 LearningUnits and 7 published Lessons exist in sequential order."""
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        self.assertEqual(units.count(), 7, f"Expected exactly 7 LearningUnits, found {units.count()}")

        for idx, unit in enumerate(units, start=1):
            self.assertEqual(unit.order, idx, f"LearningUnit order must be sequential: expected {idx}, found {unit.order}")
            lesson = Lesson.objects.filter(topic=self.topic, learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"Lesson missing for Unit {idx}: {unit.name}")
            self.assertEqual(lesson.status, "published", f"Lesson {lesson.id} status must be 'published'")

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
        """Verify all 7 lessons have Page 1 photographic visual hooks with HTTP 200 URLs & attached LessonAssets."""
        headers = {'User-Agent': 'VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)'}
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(hook_block, f"Lesson {u_order} Page 1 missing suggested_image hook block")
            content = hook_block.content or {}
            img_url = content.get("resolved_image_url") or content.get("url")
            self.assertTrue(img_url, f"Lesson {u_order} suggested_image missing url")
            self.assertTrue(img_url.startswith("https://upload.wikimedia.org/"), f"Lesson {u_order} URL must be from Wikimedia")
            self.assertTrue(content.get("author"), f"Lesson {u_order} visual hook missing author")
            self.assertTrue(content.get("licensing"), f"Lesson {u_order} visual hook missing licensing")

            asset = hook_block.assets.filter(asset_type="image").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached LessonAsset for visual hook")
            self.assertEqual(asset.url, img_url)

            try:
                resp = requests.head(img_url, headers=headers, timeout=6)
                self.assertIn(resp.status_code, [200, 301, 302, 429], f"Image URL for Lesson {u_order} returned HTTP {resp.status_code}")
            except Exception as e:
                self.fail(f"Failed to connect to image URL for Lesson {u_order}: {e}")

    def test_05_custom_vector_svgs_sanitization(self):
        """Verify all 7 lessons have sanitized responsive vector SVGs attached."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                block_type="suggested_diagram"
            ).first()

            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing suggested_diagram block")
            content = diagram_block.content or {}
            svg_str = content.get("svg_content") or content.get("svg") or ""
            self.assertGreater(len(svg_str), 100, f"Lesson {u_order} SVG content is empty or too short")
            self.assertTrue(svg_str.strip().startswith("<svg"), f"Lesson {u_order} SVG must start with <svg")
            self.assertTrue(svg_str.strip().endswith("</svg>"), f"Lesson {u_order} SVG must end with </svg>")
            self.assertIn('viewBox="0 0 800 450"', svg_str, f"Lesson {u_order} SVG must have standard viewBox='0 0 800 450'")
            self.assertIn('#0f172a', svg_str, f"Lesson {u_order} SVG missing dark-mode background color!")
            self.assertNotIn("<?xml", svg_str, f"Lesson {u_order} SVG contains raw xml header!")
            self.assertNotIn("<!DOCTYPE", svg_str, f"Lesson {u_order} SVG contains DOCTYPE!")
            self.assertNotIn("<script", svg_str.lower(), f"Lesson {u_order} SVG contains dangerous <script tag")

            asset = diagram_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} missing attached LessonAsset for SVG diagram")
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
        """Audit all blocks for citation brackets [55], [58], [117], developer meta-terms, and raw unrendered LaTeX."""
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        meta_pattern = re.compile(r'(?:\[VISUAL:|\[INTERACTION:|Student-facing caption:|Pedagogical reason:|Search concept:)')
        raw_latex_pattern = re.compile(r'(?:\\text\{|\\frac\{|\\rightarrow|\$[^\$]+\$)')

        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for block in blocks:
            content_str = json.dumps(block.content) if isinstance(block.content, (dict, list)) else str(block.content)
            title_str = block.title or ""

            self.assertFalse(citation_pattern.search(title_str), f"Citation bracket leak in Block {block.id} title: {title_str}")
            self.assertFalse(meta_pattern.search(title_str), f"Meta-tag leak in Block {block.id} title: {title_str}")

            clean_content_str = re.sub(r'<svg.*?</svg>', '', content_str, flags=re.DOTALL)
            self.assertFalse(citation_pattern.search(clean_content_str), f"Citation bracket leak in Block {block.id} ({block.block_id})")
            self.assertFalse(meta_pattern.search(clean_content_str), f"Meta-tag leak in Block {block.id} ({block.block_id})")
            self.assertFalse(raw_latex_pattern.search(clean_content_str), f"Raw LaTeX leak in Block {block.id} ({block.block_id})")

    def test_08_formative_and_summative_mcqs_validation(self):
        """Validate all 17 interactive knowledge_check blocks across the 7 lessons."""
        mcq_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="knowledge_check")
        self.assertEqual(mcq_blocks.count(), 17, f"Expected 17 MCQs (7 formative + 10 summative), found {mcq_blocks.count()}")

        for block in mcq_blocks:
            content = block.content or {}
            question = content.get("question", "")
            options = content.get("options", [])
            answer = content.get("answer", "")
            explanation = content.get("explanation", "")

            self.assertGreater(len(question), 10, f"Block {block.id} question is too short: '{question}'")
            self.assertEqual(len(options), 4, f"Block {block.id} must have exactly 4 options, found {len(options)}")
            self.assertIn(answer, ["A", "B", "C", "D"], f"Block {block.id} answer '{answer}' is not A, B, C, or D")
            self.assertGreater(len(explanation), 15, f"Block {block.id} explanation is too short: '{explanation}'")


if __name__ == "__main__":
    unittest.main()
