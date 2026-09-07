"""
Automated Verification and Comprehensive Database Audit
Grade 9 IRE — Topic 2: Surah al-Hujurat (Q 49) (Topic ID: 342)
"""

import os
import sys
import unittest
import django

# Setup Django Environment
sys.path.append("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class Grade9IRETopic2AuditTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.topic = Topic.objects.filter(id=342).first()
        assert cls.topic is not None, "Topic 342 not found!"
        cls.units = list(LearningUnit.objects.filter(topic=cls.topic).order_by('order'))
        cls.lessons = list(Lesson.objects.filter(topic=cls.topic).order_by('learning_unit__order'))

    def test_01_topic_metadata(self):
        """Verify Topic 342 matches curriculum hierarchy."""
        self.assertEqual(self.topic.id, 342)
        self.assertEqual(self.topic.name, "Surah al-Hujurat (Q 49)")
        self.assertEqual(self.topic.subject.name, "IRE")
        self.assertEqual(self.topic.subject.grade.name, "Grade 9")
        self.assertEqual(self.topic.subject.grade.curriculum.name, "CBC")

    def test_02_learning_units_and_published_lessons(self):
        """Verify 5 learning units and 5 published v1 lessons in strict order."""
        self.assertEqual(len(self.units), 5, f"Expected 5 units, found {len(self.units)}")
        self.assertEqual(len(self.lessons), 5, f"Expected 5 lessons, found {len(self.lessons)}")

        expected_titles = [
            "Respect, Authority, and Verification (Verses 1-6)",
            "Brotherhood and Conflict Resolution (Verses 9-10)",
            "Respectful Speech and Avoiding Harm (Verses 11-12)",
            "Equality, Sincerity, and Accountability (Verses 13-18)",
            "Surah al-Hujurat in Daily Relationships (Synthesis)"
        ]

        for idx, (unit, lesson) in enumerate(zip(self.units, self.lessons)):
            order = idx + 1
            self.assertEqual(unit.order, order)
            self.assertIn(expected_titles[idx], unit.name)
            self.assertEqual(lesson.learning_unit, unit)
            self.assertEqual(lesson.status, "published")
            self.assertEqual(lesson.version, 1)
            self.assertEqual(lesson.title, expected_titles[idx])

    def test_03_card_atomicity_and_pages(self):
        """Verify each lesson has exactly 7 distinct cards/pages (1-7)."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            pages = set(lesson.blocks.values_list('page_number', flat=True))
            self.assertEqual(pages, {1, 2, 3, 4, 5, 6, 7}, f"Lesson {u_order} pages mismatch: {pages}")

    def test_04_card_structure_and_components(self):
        """Verify each card contains the exact required component structure."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order

            # Card 1: suggested_image + learning_goal
            c1_blocks = lesson.blocks.filter(page_number=1).order_by('component_order')
            self.assertEqual(c1_blocks.count(), 2, f"Lesson {u_order} Card 1 block count")
            self.assertEqual(c1_blocks[0].component_type, 'suggested_image')
            self.assertEqual(c1_blocks[1].component_type, 'learning_goal')

            # Card 2: concept_explanation + callout (Scripture Panel)
            c2_blocks = lesson.blocks.filter(page_number=2).order_by('component_order')
            self.assertEqual(c2_blocks.count(), 2, f"Lesson {u_order} Card 2 block count")
            self.assertEqual(c2_blocks[0].component_type, 'concept_explanation')
            self.assertEqual(c2_blocks[1].component_type, 'callout')

            # Card 3: concept_explanation + suggested_diagram + interactive (comparison/step)
            c3_blocks = lesson.blocks.filter(page_number=3).order_by('component_order')
            self.assertEqual(c3_blocks.count(), 3, f"Lesson {u_order} Card 3 block count")
            self.assertEqual(c3_blocks[0].component_type, 'concept_explanation')
            self.assertEqual(c3_blocks[1].component_type, 'suggested_diagram')
            self.assertIn(c3_blocks[2].component_type, ['comparison_table', 'step_process'])

            # Card 4: worked_example
            c4_blocks = lesson.blocks.filter(page_number=4).order_by('component_order')
            self.assertEqual(c4_blocks.count(), 1, f"Lesson {u_order} Card 4 block count")
            self.assertEqual(c4_blocks[0].component_type, 'worked_example')

            # Card 5: real_world_example + reflection + common_misconception + suggested_video
            c5_blocks = lesson.blocks.filter(page_number=5).order_by('component_order')
            self.assertEqual(c5_blocks.count(), 4, f"Lesson {u_order} Card 5 block count")
            self.assertEqual(c5_blocks[0].component_type, 'real_world_example')
            self.assertEqual(c5_blocks[1].component_type, 'reflection')
            self.assertEqual(c5_blocks[2].component_type, 'common_misconception')
            self.assertEqual(c5_blocks[3].component_type, 'suggested_video')

            # Card 6: knowledge_check
            c6_blocks = lesson.blocks.filter(page_number=6).order_by('component_order')
            self.assertEqual(c6_blocks.count(), 1, f"Lesson {u_order} Card 6 block count")
            self.assertEqual(c6_blocks[0].component_type, 'knowledge_check')

            # Card 7: summary + mini_activity
            c7_blocks = lesson.blocks.filter(page_number=7).order_by('component_order')
            self.assertEqual(c7_blocks.count(), 2, f"Lesson {u_order} Card 7 block count")
            self.assertEqual(c7_blocks[0].component_type, 'summary')
            self.assertEqual(c7_blocks[1].component_type, 'mini_activity')

    def test_05_custom_vector_svgs(self):
        """Verify custom pedagogical SVG diagrams exist, are valid XML, and attached as LessonAsset."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            diag_block = lesson.blocks.filter(block_type='suggested_diagram').first()
            self.assertIsNotNone(diag_block, f"Lesson {u_order} missing suggested_diagram block")
            
            # Check attached asset
            diag_asset = LessonAsset.objects.filter(lesson=lesson, asset_type='diagram').first()
            self.assertIsNotNone(diag_asset, f"Lesson {u_order} missing diagram LessonAsset")
            self.assertEqual(diag_asset.status, 'attached')
            self.assertEqual(diag_asset.source_type, 'ai_generated')
            
            svg_xml = diag_asset.metadata.get('svg_xml') or diag_block.content.get('svg_xml', '')
            self.assertTrue(svg_xml.startswith('<svg') and svg_xml.strip().endswith('</svg>'), f"Lesson {u_order} SVG malformed")
            self.assertIn('viewBox="0 0 880 480"', svg_xml)
            self.assertIn('#0f172a', svg_xml)

    def test_06_authentic_wikimedia_images(self):
        """Verify authentic Wikimedia Commons images are attached with valid metadata."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            img_block = lesson.blocks.filter(block_type='suggested_image').first()
            self.assertIsNotNone(img_block, f"Lesson {u_order} missing suggested_image block")
            
            img_asset = LessonAsset.objects.filter(lesson=lesson, asset_type='image').first()
            self.assertIsNotNone(img_asset, f"Lesson {u_order} missing image LessonAsset")
            self.assertTrue(img_asset.url.startswith('https://upload.wikimedia.org/'), f"Lesson {u_order} URL not Wikimedia: {img_asset.url}")
            self.assertEqual(img_asset.metadata.get('source'), 'Wikimedia Commons')

    def test_07_youtube_video_assets(self):
        """Verify educational YouTube video assets are attached."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            vid_block = lesson.blocks.filter(block_type='suggested_video').first()
            self.assertIsNotNone(vid_block, f"Lesson {u_order} missing suggested_video block")
            
            yt_asset = LessonAsset.objects.filter(lesson=lesson, asset_type='youtube').first()
            self.assertIsNotNone(yt_asset, f"Lesson {u_order} missing youtube LessonAsset")
            self.assertIn('youtube.com/watch?v=', yt_asset.url)
            yid = yt_asset.metadata.get('youtube_id')
            self.assertTrue(len(yid) == 11, f"Lesson {u_order} invalid YouTube ID: {yid}")

    def test_08_mcq_accuracy_and_format(self):
        """Verify Card 6 MCQ has question, 4 options, valid answer, and explanation."""
        for lesson in self.lessons:
            u_order = lesson.learning_unit.order
            mcq_block = lesson.blocks.filter(page_number=6, block_type='knowledge_check').first()
            self.assertIsNotNone(mcq_block, f"Lesson {u_order} missing MCQ block")
            c = mcq_block.content
            self.assertTrue(len(c.get('question', '')) > 20)
            self.assertEqual(len(c.get('options', [])), 4)
            self.assertIn(c.get('answer'), ['A', 'B', 'C', 'D'])
            self.assertIn(c.get('correct_answer'), ['A', 'B', 'C', 'D'])
            self.assertTrue(len(c.get('explanation', '')) > 20)

    def test_09_no_raw_tags_or_citations(self):
        """Verify no raw brackets like [1], [VISUAL: ...], [QURAN REFERENCE: ...] remain in content."""
        blocks = LessonBlock.objects.filter(lesson__topic=self.topic)
        for b in blocks:
            c_str = str(b.content)
            self.assertNotRegex(c_str, r'\[(?:VISUAL|QURAN REFERENCE|Source:)', f"Block {b.id} has uncleaned tags")
            self.assertNotRegex(c_str, r'\[\d+(?:,\s*\d+)*\]', f"Block {b.id} has uncleaned citations")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Grade9IRETopic2AuditTestCase)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
