"""
Test Suite for Grade 9 IRE — Topic 1: Ulum al-Qur'an (The Sciences of the Qur'an)
Topic ID: 341
"""

import os
import sys
import unittest
import xml.etree.ElementTree as ET
import django

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestGrade9IRETopic1Ingestion(unittest.TestCase):

    def setUp(self):
        self.topic = Topic.objects.filter(id=341).first()
        self.assertIsNotNone(self.topic, "Topic ID 341 must exist in the database.")
        self.units = LearningUnit.objects.filter(topic=self.topic).order_by("order")
        self.lessons = Lesson.objects.filter(topic=self.topic).order_by("learning_unit__order")

    def test_01_topic_isolation_and_metadata(self):
        """Verify Topic 341 isolation, subject, grade, and metadata."""
        self.assertEqual(self.topic.id, 341)
        self.assertEqual(self.topic.subject.name, "IRE")
        self.assertEqual(self.topic.subject.grade.name, "Grade 9")
        self.assertEqual(self.topic.name, "Ulum al-Qur'an (The Sciences of the Qur'an)")
        self.assertEqual(self.topic.order, 1)

    def test_02_unit_and_lesson_counts(self):
        """Verify exactly 7 LearningUnits and 7 published Lessons."""
        self.assertEqual(self.units.count(), 7, "Must have exactly 7 LearningUnits.")
        self.assertEqual(self.lessons.count(), 7, "Must have exactly 7 Lessons.")

        for i, unit in enumerate(self.units, start=1):
            self.assertEqual(unit.order, i, f"Unit {unit.name} must have order {i}.")
            lesson = Lesson.objects.filter(learning_unit=unit).first()
            self.assertIsNotNone(lesson, f"Unit {unit.id} must have an associated Lesson.")
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)

    def test_03_seven_cards_per_lesson(self):
        """Verify each lesson has 7 pages (Cards 1 to 7)."""
        for lesson in self.lessons:
            pages = set(lesson.blocks.values_list("page_number", flat=True))
            self.assertEqual(pages, {1, 2, 3, 4, 5, 6, 7}, f"Lesson {lesson.title} must have pages 1 through 7.")

    def test_04_card_block_composition(self):
        """Verify required component types on each card."""
        for lesson in self.lessons:
            # Card 1: learning_goal
            card1_types = set(lesson.blocks.filter(page_number=1).values_list("block_type", flat=True))
            self.assertIn("learning_goal", card1_types)

            # Card 2: concept_explanation and callout
            card2_types = set(lesson.blocks.filter(page_number=2).values_list("block_type", flat=True))
            self.assertIn("concept_explanation", card2_types)
            self.assertIn("callout", card2_types)

            # Card 3: concept_explanation and suggested_diagram and (comparison_table or step_process)
            card3_types = set(lesson.blocks.filter(page_number=3).values_list("block_type", flat=True))
            self.assertIn("concept_explanation", card3_types)
            self.assertIn("suggested_diagram", card3_types)
            has_table_or_step = ("comparison_table" in card3_types) or ("step_process" in card3_types)
            self.assertTrue(has_table_or_step, f"Lesson {lesson.title} Card 3 must have comparison_table or step_process.")

            # Card 4: worked_example
            card4_types = set(lesson.blocks.filter(page_number=4).values_list("block_type", flat=True))
            self.assertIn("worked_example", card4_types)

            # Card 5: real_world_example, reflection, and common_misconception
            card5_types = set(lesson.blocks.filter(page_number=5).values_list("block_type", flat=True))
            self.assertIn("real_world_example", card5_types)
            self.assertIn("reflection", card5_types)
            self.assertIn("common_misconception", card5_types)

            # Card 6: knowledge_check
            card6_types = set(lesson.blocks.filter(page_number=6).values_list("block_type", flat=True))
            self.assertIn("knowledge_check", card6_types)

            # Card 7: summary and mini_activity
            card7_types = set(lesson.blocks.filter(page_number=7).values_list("block_type", flat=True))
            self.assertIn("summary", card7_types)
            self.assertIn("mini_activity", card7_types)

    def test_05_svg_validity_and_assets(self):
        """Verify all 7 diagrams are valid SVG XML and linked to LessonAsset and LessonBlock."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diag_asset = lesson.assets.filter(asset_type="diagram").first()
            self.assertIsNotNone(diag_asset, f"Lesson {u_order} must have a diagram LessonAsset.")
            
            svg_xml = diag_asset.metadata.get("svg_xml")
            self.assertTrue(svg_xml, f"Lesson {u_order} diagram asset must contain svg_xml.")

            # Check valid XML
            try:
                root = ET.fromstring(svg_xml)
                self.assertIn("svg", root.tag)
            except Exception as e:
                self.fail(f"Lesson {u_order} SVG XML parse error: {e}")

            # Verify diagram block has asset attached
            diag_block = lesson.blocks.filter(page_number=3, block_type="suggested_diagram").first()
            self.assertIsNotNone(diag_block, f"Lesson {u_order} Card 3 must have suggested_diagram block.")
            self.assertIn(diag_asset, diag_block.assets.all(), f"Lesson {u_order} diagram block must be linked to diagram asset.")

    def test_06_authentic_image_assets(self):
        """Verify each lesson has an authentic Wikimedia image asset attached."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            img_asset = lesson.assets.filter(asset_type="image").first()
            self.assertIsNotNone(img_asset, f"Lesson {u_order} must have an image LessonAsset.")
            self.assertTrue(img_asset.url.startswith("https://upload.wikimedia.org/"), f"Lesson {u_order} image URL must be from Wikimedia.")
            self.assertTrue(img_asset.metadata.get("licensing"))

    def test_07_knowledge_check_mcq_structure(self):
        """Verify all MCQs on Card 6 have valid structure with 4 options and explanation."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            kc_block = lesson.blocks.filter(page_number=6, block_type="knowledge_check").first()
            self.assertIsNotNone(kc_block)
            content = kc_block.content or {}
            self.assertTrue(content.get("question"), f"Lesson {u_order} MCQ missing question.")
            options = content.get("options")
            self.assertIsInstance(options, list)
            self.assertEqual(len(options), 4, f"Lesson {u_order} MCQ must have 4 options.")
            self.assertIn(content.get("answer"), ["A", "B", "C", "D"])
            self.assertEqual(content.get("answer"), content.get("correct_answer"))
            self.assertTrue(content.get("explanation"), f"Lesson {u_order} MCQ missing explanation.")

    def test_08_no_bracket_citations_leakage(self):
        """Verify no raw bracket citations or prompt tags remain in block contents."""
        for lesson in self.lessons:
            for b in lesson.blocks.all():
                content_str = str(b.content)
                self.assertNotIn("[VISUAL:", content_str)
                self.assertNotIn("[QURAN REFERENCE:", content_str)
                self.assertNotIn("[MISCONCEPTION CHECK]", content_str)
                self.assertNotIn("[REAL WORLD APPLICATION]", content_str)


if __name__ == "__main__":
    unittest.main()
