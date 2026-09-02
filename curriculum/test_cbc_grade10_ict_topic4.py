"""
VLearn CBC Grade 10 ICT — Topic 4: Word Processing
Automated QA & Integrity Verification Test Suite
"""

import os
import sys
import unittest
import django
import re

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10ICTTopic4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first() or Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="ICT").first()
        assert cls.subject, "Subject 'ICT' not found under Grade 10 CBC!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=4).first()
        assert cls.topic, "Topic 4 'Word Processing' not found under ICT!"

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "ICT")
        self.assertEqual(self.topic.order, 4)
        self.assertEqual(self.topic.name, "Word Processing")
        self.assertTrue(self.topic.description, "Topic 4 missing description")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 10 LearningUnits and 10 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 10, f"Expected 10 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 10, f"Expected 10 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has exactly 5 pages and non-empty block content."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertGreaterEqual(len(blocks), 10, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5], f"Lesson '{lesson.title}' page numbers must be [1, 2, 3, 4, 5], got {page_numbers}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 10 lessons have Page 1 photographic visual hooks with Wikimedia URLs and learning goals."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("url")
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 visual hook missing image URL!")
            self.assertIn("wikimedia.org", img_url, f"Lesson {u_order} URL not Wikimedia: {img_url}")

            goal_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="learning_goal"
            ).first()
            self.assertIsNotNone(goal_block, f"Lesson {u_order} missing Card 1 learning_goal block!")
            self.assertTrue(goal_block.content.get("text"), f"Lesson {u_order} learning_goal missing text!")

    def test_05_custom_vector_svgs(self):
        """Verify all 10 lessons contain sanitized, responsive vector SVGs attached as LessonAssets on Page 3."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=3,
                block_type="suggested_diagram"
            ).first()

            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing page 3 suggested_diagram block!")
            content = diagram_block.content or {}
            svg_text = content.get("svg_content", "")
            self.assertTrue("<svg" in svg_text and "</svg>" in svg_text, f"Lesson {u_order} SVG malformed!")
            self.assertIn("viewBox", svg_text, f"Lesson {u_order} SVG missing viewBox!")

            # Verify LessonAsset attachment
            asset = diagram_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} diagram block missing attached LessonAsset!")

    def test_06_youtube_video_assets(self):
        """Verify 100% YouTube video coverage on Page 5."""
        video_count = 0
        for lesson in self.lessons:
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=5,
                block_type="suggested_video"
            ).first()
            self.assertIsNotNone(video_block, f"Lesson {lesson.learning_unit.order} missing page 5 suggested_video block!")
            content = video_block.content or {}
            yt_id = content.get("youtube_id")
            self.assertTrue(yt_id, f"Lesson {lesson.learning_unit.order} missing youtube_id")
            video_count += 1
            asset = video_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Lesson {lesson.learning_unit.order} video block missing attached LessonAsset!")

        coverage = (video_count / len(self.lessons)) * 100
        print(f"[*] Topic 4 Video Coverage: {video_count}/{len(self.lessons)} ({coverage:.1f}%)")
        self.assertEqual(coverage, 100.0)

    def test_07_content_sanitization(self):
        """Verify zero bracket citations ([36], [258]), zero developer prompt leakage."""
        citation_pattern = re.compile(r'\[\d+\]')
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                text_content = str(b.content) + " " + (b.title or "")
                # Check for raw citation brackets like [36], [258]
                self.assertFalse(bool(citation_pattern.search(text_content)), f"Block {b.id} contains citation brackets: {text_content[:80]}")
                # Check for developer prompt leaks
                for leak in ["Prompt:", "JSON Payload", "block_type:", "component_order:"]:
                    self.assertNotIn(leak, text_content, f"Block {b.id} contains prompt leak '{leak}'")

    def test_08_formative_mcqs(self):
        """Verify MCQs contain 4 options, valid correct answer keys, and explanations."""
        mcq_count = 0
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=5, block_type="knowledge_check")
            self.assertGreaterEqual(len(mcq_blocks), 2, f"Lesson {lesson.learning_unit.order} must have >= 2 MCQs on page 5, got {len(mcq_blocks)}")
            for mb in mcq_blocks:
                mcq_count += 1
                c = mb.content or {}
                self.assertTrue(c.get("question"), f"MCQ Block {mb.id} missing question!")
                options = c.get("options", [])
                self.assertEqual(len(options), 4, f"MCQ Block {mb.id} must have 4 options, got {len(options)}")
                correct = c.get("correct") or c.get("answer")
                self.assertIn(correct, ["A", "B", "C", "D"], f"MCQ Block {mb.id} has invalid correct answer: {correct}")
                self.assertTrue(c.get("explanation"), f"MCQ Block {mb.id} missing explanation!")

        self.assertGreaterEqual(mcq_count, 20, f"Expected >= 20 MCQs across Topic 4, found {mcq_count}")

    def test_09_pedagogical_page_completeness(self):
        """Verify the full 5-page pedagogical card architecture across all 10 lessons."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            # Page 2: definition_card and concept_explanation
            p2_types = list(LessonBlock.objects.filter(lesson=lesson, page_number=2).values_list("block_type", flat=True))
            self.assertIn("definition_card", p2_types, f"Lesson {u_order} Page 2 missing definition_card")
            self.assertIn("concept_explanation", p2_types, f"Lesson {u_order} Page 2 missing concept_explanation")

            # Page 3: suggested_diagram and step_process
            p3_types = list(LessonBlock.objects.filter(lesson=lesson, page_number=3).values_list("block_type", flat=True))
            self.assertIn("suggested_diagram", p3_types, f"Lesson {u_order} Page 3 missing suggested_diagram")
            self.assertIn("step_process", p3_types, f"Lesson {u_order} Page 3 missing step_process")

            # Page 4: real_world_example, common_misconception, common_mistake
            p4_types = list(LessonBlock.objects.filter(lesson=lesson, page_number=4).values_list("block_type", flat=True))
            self.assertIn("real_world_example", p4_types, f"Lesson {u_order} Page 4 missing real_world_example")
            self.assertIn("common_misconception", p4_types, f"Lesson {u_order} Page 4 missing common_misconception")
            self.assertIn("common_mistake", p4_types, f"Lesson {u_order} Page 4 missing common_mistake")

            # Page 5: summary
            p5_types = list(LessonBlock.objects.filter(lesson=lesson, page_number=5).values_list("block_type", flat=True))
            self.assertIn("summary", p5_types, f"Lesson {u_order} Page 5 missing summary")

if __name__ == "__main__":
    unittest.main()
