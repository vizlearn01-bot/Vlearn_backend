"""
VLearn CBC Grade 10 ICT — Topic 1: Introduction to ICT
Automated QA & Integrity Verification Test Suite
"""

import os
import sys
import unittest
import django
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

class TestCBCGrade10ICTTopic1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        assert cls.curriculum, "Curriculum 'CBC' not found in database!"

        cls.grade = Grade.objects.filter(curriculum=cls.curriculum, level=10).first() or Grade.objects.filter(curriculum=cls.curriculum, name__icontains="10").first()
        assert cls.grade, "Grade 10 not found under CBC!"

        cls.subject = Subject.objects.filter(grade=cls.grade, name="ICT").first()
        assert cls.subject, "Subject 'ICT' not found under Grade 10!"

        cls.topic = Topic.objects.filter(subject=cls.subject, order=1).first()
        assert cls.topic, "Topic 1 'Introduction to ICT' not found under ICT!"

        cls.units = list(cls.topic.learning_units.all().order_by("order"))
        cls.lessons = list(cls.topic.lessons.all().order_by("learning_unit__order"))

    def test_01_hierarchy_integrity(self):
        """Verify the full curriculum hierarchy and Topic 1 configuration."""
        self.assertEqual(self.curriculum.name, "CBC")
        self.assertEqual(self.grade.level, 10)
        self.assertEqual(self.subject.name, "ICT")
        self.assertEqual(self.topic.order, 1)
        self.assertEqual(self.topic.name, "Introduction to ICT")

    def test_02_units_and_published_lessons_count(self):
        """Verify exactly 4 LearningUnits and 4 published Lessons exist in sequential order."""
        self.assertEqual(len(self.units), 4, f"Expected 4 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 4, f"Expected 4 lessons, found {len(self.lessons)}")

        for idx, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, idx, f"Unit order mismatch at index {idx}")
            lesson = next((l for l in self.lessons if l.learning_unit_id == unit.id), None)
            self.assertIsNotNone(lesson, f"No lesson found for Unit {idx}")
            self.assertEqual(lesson.status, "published", f"Lesson {idx} is not published!")
            self.assertGreaterEqual(lesson.version, 1, f"Lesson {idx} version invalid")

    def test_03_card_and_block_structure(self):
        """Verify every lesson has exactly 5 pages and non-empty blocks."""
        for lesson in self.lessons:
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            self.assertGreaterEqual(len(blocks), 5, f"Lesson {lesson.id} has too few blocks ({len(blocks)})")

            page_numbers = set(b.page_number for b in blocks if b.page_number)
            self.assertEqual(page_numbers, {1, 2, 3, 4, 5}, f"Lesson {lesson.id} must have exactly 5 pages, got {page_numbers}")

            for b in blocks:
                self.assertTrue(b.title, f"Block {b.id} missing title")
                self.assertTrue(b.content, f"Block {b.id} missing content")

    def test_04_card_1_visual_hooks(self):
        """Verify all 4 lessons have Page 1 photographic visual hooks with Wikimedia URLs and learning goals."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            hook_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="suggested_image"
            ).first()

            self.assertIsNotNone(hook_block, f"Lesson {u_order} missing Card 1 suggested_image block!")
            content = hook_block.content or {}
            img_url = content.get("url", "")
            self.assertTrue(img_url, f"Lesson {u_order} Card 1 visual hook missing image URL!")
            self.assertTrue("wikimedia.org" in img_url, f"Lesson {u_order} URL not Wikimedia: {img_url}")

            # Verify learning_goal exists on page 1
            lg_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=1,
                block_type="learning_goal"
            ).first()
            self.assertIsNotNone(lg_block, f"Lesson {u_order} missing learning_goal on Page 1")

    def test_05_custom_vector_svgs(self):
        """Verify all 4 lessons contain responsive vector SVGs attached as LessonAssets on Page 3."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diagram_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=3,
                block_type="suggested_diagram"
            ).first()

            self.assertIsNotNone(diagram_block, f"Lesson {u_order} missing Page 3 suggested_diagram block!")
            content = diagram_block.content or {}
            svg_text = content.get("svg_content", "")
            self.assertTrue("<svg" in svg_text and "</svg>" in svg_text, f"Lesson {u_order} SVG malformed!")
            self.assertIn("viewBox", svg_text, f"Lesson {u_order} SVG missing viewBox!")

            # Verify LessonAsset attachment
            asset = diagram_block.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(asset, f"Lesson {u_order} diagram block missing attached LessonAsset!")

    def test_06_youtube_video_assets(self):
        """Verify 100% YouTube video coverage on Page 5 with attached LessonAssets."""
        video_count = 0
        for lesson in self.lessons:
            video_block = LessonBlock.objects.filter(
                lesson=lesson,
                page_number=5,
                block_type="suggested_video"
            ).first()
            self.assertIsNotNone(video_block, f"Lesson {lesson.learning_unit.order} missing Page 5 suggested_video block!")
            content = video_block.content or {}
            yt_id = content.get("youtube_id")
            self.assertTrue(yt_id, f"Lesson {lesson.learning_unit.order} missing youtube_id")
            video_count += 1
            asset = video_block.assets.filter(asset_type="youtube").first()
            self.assertIsNotNone(asset, f"Lesson {lesson.learning_unit.order} video block missing attached LessonAsset!")

        coverage = (video_count / len(self.lessons)) * 100
        print(f"[*] Topic 1 Video Coverage: {video_count}/{len(self.lessons)} ({coverage:.1f}%)")
        self.assertEqual(coverage, 100.0, f"Topic 1 video coverage below 100%: {coverage}%")

    def test_07_content_sanitization(self):
        """Verify zero bracket citations ([568], [1]), zero developer prompt leakage, and clean markdown."""
        for lesson in self.lessons:
            blocks = LessonBlock.objects.filter(lesson=lesson)
            for b in blocks:
                text_content = str(b.content) + " " + (b.title or "")
                # Check for raw citation brackets like [568], [12]
                self.assertFalse(bool(re.search(r'\[\d+\]', text_content)), f"Block {b.id} contains citation brackets: {text_content[:80]}")
                # Check for developer prompt leaks and tags
                for leak in ["Prompt:", "JSON Payload", "[VISUAL:", "[MISCONCEPTION]", "[PRACTICAL TASK]"]:
                    self.assertNotIn(leak, text_content, f"Block {b.id} contains prompt leak/tag '{leak}'")

    def test_08_formative_mcqs(self):
        """Verify MCQs contain 4 options, valid correct answer keys, and non-empty explanations."""
        mcq_count = 0
        for lesson in self.lessons:
            mcq_blocks = LessonBlock.objects.filter(lesson=lesson, page_number=5, block_type="knowledge_check")
            self.assertGreaterEqual(len(mcq_blocks), 2, f"Lesson {lesson.learning_unit.order} must have at least 2 MCQs on Page 5")
            for mb in mcq_blocks:
                mcq_count += 1
                c = mb.content or {}
                self.assertTrue(c.get("question"), f"MCQ Block {mb.id} missing question!")
                options = c.get("options", [])
                self.assertEqual(len(options), 4, f"MCQ Block {mb.id} must have 4 options, got {len(options)}")
                correct = c.get("correct") or c.get("answer")
                self.assertIn(correct, ["A", "B", "C", "D"], f"MCQ Block {mb.id} has invalid correct answer: {correct}")
                self.assertTrue(c.get("explanation"), f"MCQ Block {mb.id} missing explanation!")

        self.assertGreaterEqual(mcq_count, 8, f"Expected >= 8 MCQs in Topic 1, found {mcq_count}")

    def test_09_pedagogical_card_architecture(self):
        """Verify the strict 5-page pedagogical card architecture across all 4 lessons."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order

            # Page 1: suggested_image & learning_goal
            p1_types = set(LessonBlock.objects.filter(lesson=lesson, page_number=1).values_list("block_type", flat=True))
            self.assertIn("suggested_image", p1_types, f"Lesson {u_order} Page 1 missing suggested_image")
            self.assertIn("learning_goal", p1_types, f"Lesson {u_order} Page 1 missing learning_goal")

            # Page 2: definition_card & concept_explanation
            p2_types = set(LessonBlock.objects.filter(lesson=lesson, page_number=2).values_list("block_type", flat=True))
            self.assertIn("definition_card", p2_types, f"Lesson {u_order} Page 2 missing definition_card")
            self.assertIn("concept_explanation", p2_types, f"Lesson {u_order} Page 2 missing concept_explanation")

            # Page 3: suggested_diagram & step_process
            p3_types = set(LessonBlock.objects.filter(lesson=lesson, page_number=3).values_list("block_type", flat=True))
            self.assertIn("suggested_diagram", p3_types, f"Lesson {u_order} Page 3 missing suggested_diagram")
            self.assertIn("step_process", p3_types, f"Lesson {u_order} Page 3 missing step_process")

            # Page 4: real_world_example, common_misconception, common_mistake
            p4_types = set(LessonBlock.objects.filter(lesson=lesson, page_number=4).values_list("block_type", flat=True))
            self.assertIn("real_world_example", p4_types, f"Lesson {u_order} Page 4 missing real_world_example")
            self.assertIn("common_misconception", p4_types, f"Lesson {u_order} Page 4 missing common_misconception")
            self.assertIn("common_mistake", p4_types, f"Lesson {u_order} Page 4 missing common_mistake")

            # Page 5: knowledge_check, suggested_video, summary
            p5_types = set(LessonBlock.objects.filter(lesson=lesson, page_number=5).values_list("block_type", flat=True))
            self.assertIn("knowledge_check", p5_types, f"Lesson {u_order} Page 5 missing knowledge_check")
            self.assertIn("suggested_video", p5_types, f"Lesson {u_order} Page 5 missing suggested_video")
            self.assertIn("summary", p5_types, f"Lesson {u_order} Page 5 missing summary")

if __name__ == "__main__":
    unittest.main()
