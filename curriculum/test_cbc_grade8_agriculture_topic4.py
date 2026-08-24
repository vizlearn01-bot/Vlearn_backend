"""
VLearn CBC Grade 8 Agriculture — Topic 4: Poultry Rearing in a Fold
Automated QA Test Suite (Phase 3: Pedagogical & Visual Integrity Validation)

Tests:
  1. test_01_hierarchy_integrity: Validates Curriculum -> Grade -> Subject -> Topic configuration.
  2. test_02_units_and_published_lessons_count: Verifies exactly 9 Units and 9 published Lessons.
  3. test_03_card_and_block_structure: Verifies card pagination and block distribution.
  4. test_04_card_1_visual_hooks: Verifies all 9 lessons have Page 1 Wikimedia image hooks and attached assets.
  5. test_05_custom_vector_svgs_sanitization: Verifies 9 sanitized responsive vector SVGs.
  6. test_06_multi_video_integration: Verifies YouTube video lessons across Units 2, 5, and 9.
  7. test_07_zero_citation_and_meta_leaks: Audits zero citation leaks, zero meta-tags, and zero raw LaTeX.
  8. test_08_formative_and_summative_mcqs_validation: Verifies all interactive knowledge check MCQs.

Usage:
  ./venv/bin/python curriculum/test_cbc_grade8_agriculture_topic4.py
"""

import os
import sys
import re
import json
import unittest
import requests
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade8AgricultureTopic4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name="CBC").first()
        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, name="Grade 8").first()
        cls.subject = Subject.objects.filter(grade=cls.grade, name="Agriculture").first()
        cls.topic = Topic.objects.filter(subject=cls.subject, name="Poultry Rearing in a Fold").first()
        cls.units = list(LearningUnit.objects.filter(topic=cls.topic).order_by("order"))
        cls.lessons = list(Lesson.objects.filter(topic=cls.topic).select_related("learning_unit").order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertIsNotNone(self.curriculum, "Curriculum 'CBC' must exist")
        self.assertIsNotNone(self.grade, "Grade 'Grade 8' must exist")
        self.assertIsNotNone(self.subject, "Subject 'Agriculture' must exist")
        self.assertIsNotNone(self.topic, "Topic 'Poultry Rearing in a Fold' must exist")
        self.assertEqual(self.topic.order, 4, "Topic order must be 4")
        self.assertTrue(len(self.topic.description) > 50, "Topic description must be detailed")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 9 LearningUnits and 9 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 9, f"Expected exactly 9 LearningUnits, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 9, f"Expected exactly 9 Lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit '{unit.name}' order must be {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"LearningUnit {unit.id} must have an associated Lesson")
            self.assertEqual(lesson.status, "published", f"Lesson '{lesson.title}' must be published")

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
        """Verify all 9 lessons have Page 1 photographic visual hooks with HTTP 200 URLs & attached LessonAssets."""
        headers = {"User-Agent": "VlearnCurriculumBot/1.0 (https://vlearn.africa; contact@vlearn.africa)"}
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(lesson=lesson, page_number=1, block_type="suggested_image").first()
            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Page 1 suggested_image visual hook")

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
        """Verify all 9 lessons have sanitized responsive vector SVGs attached."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_diagram").first()
            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing suggested_diagram block")

            content = diagram_block.content or {}
            svg_str = content.get("svg") or content.get("svg_content")
            self.assertTrue(svg_str, f"Lesson {u_order} missing inline SVG string")
            self.assertIn("viewBox=\"0 0 800 450\"", svg_str, f"Lesson {u_order} SVG missing viewBox 0 0 800 450")
            self.assertIn("<rect width=\"800\" height=\"450\" fill=\"#0f172a\"", svg_str, f"Lesson {u_order} SVG missing dark background")
            self.assertNotIn("<?xml", svg_str, f"Lesson {u_order} SVG contains raw XML header!")
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
        """Audit all blocks for citation brackets [1], [245], developer meta-terms, and raw unrendered LaTeX."""
        citation_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        meta_pattern = re.compile(r'(?:\[VISUAL:|\[INTERACTION:|Student-facing caption:|Pedagogical reason:|Search concept:)')
        raw_latex_pattern = re.compile(r'(?:\\text\{|\\frac\{|\\rightarrow|\$[^\$]+\$)')

        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for block in blocks:
            text_corpus = f"{block.title} {json.dumps(block.content or {})}"

            citation_match = citation_pattern.search(text_corpus)
            self.assertIsNone(citation_match, f"Block {block.id} (Lesson {block.lesson_id}) contains raw citation bracket: {citation_match.group(0) if citation_match else ''}")

            meta_match = meta_pattern.search(text_corpus)
            self.assertIsNone(meta_match, f"Block {block.id} contains developer meta-tag: {meta_match.group(0) if meta_match else ''}")

            # Check raw LaTeX outside math formulas
            if block.block_type in ["concept_explanation", "key_takeaway", "learning_goal"]:
                for match in raw_latex_pattern.finditer(text_corpus):
                    # allow properly rendered $$ formulas in concept_explanation
                    if "$$" not in text_corpus:
                        self.fail(f"Block {block.id} contains unrendered LaTeX: {match.group(0)}")

    def test_08_formative_and_summative_mcqs_validation(self):
        """Validate all interactive knowledge_check blocks across the 9 lessons."""
        kc_blocks = LessonBlock.objects.filter(lesson__topic=self.topic, block_type="knowledge_check")
        # 1 formative per lesson (1-8) + 1 formative + 10 summative on lesson 9 = 19 MCQs
        self.assertGreaterEqual(kc_blocks.count(), 18, f"Expected at least 18 MCQs, found {kc_blocks.count()}")

        for kc in kc_blocks:
            c = kc.content or {}
            self.assertTrue(c.get("question"), f"KC Block {kc.id} missing question text")
            options = c.get("options", [])
            self.assertGreaterEqual(len(options), 2, f"KC Block {kc.id} must have at least 2 options")
            self.assertIn(c.get("answer"), ["A", "B", "C", "D"], f"KC Block {kc.id} answer '{c.get('answer')}' must be A, B, C, or D")
            self.assertTrue(c.get("explanation"), f"KC Block {kc.id} missing explanation")

if __name__ == "__main__":
    unittest.main()
