"""
Verification Test Suite for Grade 9 CRE Topic 11: The Early Church
"""

import os
import sys
import unittest
import django

sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestGrade9CRETopic11Ingestion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.grade = Grade.objects.get(id=18)
        cls.subject = Subject.objects.get(id=50, grade=cls.grade)
        cls.topic = Topic.objects.get(subject=cls.subject, order=11)

    def test_topic_hierarchy(self):
        self.assertEqual(self.grade.id, 18)
        self.assertEqual(self.subject.id, 50)
        self.assertEqual(self.topic.order, 11)
        self.assertEqual(self.topic.name, "The Early Church")

    def test_units_and_lessons_count(self):
        units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        self.assertEqual(units.count(), 8)

        lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")
        self.assertEqual(lessons.count(), 8)

        expected_titles = [
            "The Day of Pentecost: Birth of the Church",
            "Characteristics of the Early Church",
            "Miracles in the Early Church",
            "Paul and Silas: The Prison Context",
            "Paul and Silas: Praise in the Prison",
            "The Conversion of the Jailer",
            "Characteristics of the Modern Church",
            "The Call to Salvation Today"
        ]

        for idx, lesson in enumerate(lessons):
            self.assertEqual(lesson.title, expected_titles[idx])
            self.assertEqual(lesson.status, "published")

    def test_lesson_structure_and_blocks(self):
        lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")

        for lesson in lessons:
            blocks = list(lesson.blocks.all().order_by("page_number", "component_order"))
            self.assertEqual(len(blocks), 13, f"Lesson '{lesson.title}' must have exactly 13 blocks")

            # Check 6 distinct pages
            page_numbers = sorted(list(set(b.page_number for b in blocks)))
            self.assertEqual(page_numbers, [1, 2, 3, 4, 5, 6], f"Lesson '{lesson.title}' must have 6 pages (1-6)")

            # Check block types
            block_types = [b.block_type for b in blocks]
            expected_block_types = [
                "suggested_image", "learning_goal", "concept_explanation", # Page 1 (3 blocks)
                "concept_explanation", "concept_explanation",              # Page 2 (2 blocks)
                "suggested_diagram", "concept_explanation",                # Page 3 (2 blocks)
                "step_process", "concept_explanation",                     # Page 4 (2 blocks)
                "suggested_video", "concept_explanation",                  # Page 5 (2 blocks)
                "summary", "knowledge_check"                               # Page 6 (2 blocks)
            ]
            self.assertEqual(block_types, expected_block_types, f"Block types mismatch in '{lesson.title}'")

            # Check assets attached
            assets = list(lesson.assets.all())
            self.assertEqual(len(assets), 3, f"Lesson '{lesson.title}' must have exactly 3 assets")
            asset_types = sorted([a.asset_type for a in assets])
            self.assertEqual(asset_types, ["diagram", "image", "youtube"])

            # Verify diagram SVG content
            diag_block = next(b for b in blocks if b.block_type == "suggested_diagram")
            self.assertIn("svg", diag_block.content)
            self.assertIn('viewBox="0 0 800 450"', diag_block.content["svg"])
            self.assertIn("#0f172a", diag_block.content["svg"])

            # Verify knowledge check MCQ
            mcq_block = next(b for b in blocks if b.block_type == "knowledge_check")
            self.assertIn("question", mcq_block.content)
            self.assertEqual(len(mcq_block.content["options"]), 4)
            self.assertIn(mcq_block.content["correct_answer"], ["A", "B", "C", "D"])
            self.assertTrue(len(mcq_block.content["explanation"]) > 10)


if __name__ == "__main__":
    unittest.main()
