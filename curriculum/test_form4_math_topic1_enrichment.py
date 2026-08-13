import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import TestCase
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.ingest_form4_math_topic1_matrices import ingest_form4_math_topic1
from curriculum.enrich_form4_math_topic1_matrices import enrich_topic1_matrices

class Form4MathTopic1EnrichmentTestCase(TestCase):
    def setUp(self):
        ingest_form4_math_topic1()
        enrich_topic1_matrices()

    def test_topic1_enrichment_blocks_and_assets(self):
        topic = Topic.objects.filter(subject__name='Mathematics', order=1).first()
        self.assertIsNotNone(topic, "Topic 1 Mathematics should exist")

        lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
        self.assertEqual(len(lessons), 4, "Topic 1 should have 4 lessons")

        # Lesson 1: Matrix Action on Coordinate Vectors
        l1 = lessons[0]
        p2_b = LessonBlock.objects.filter(lesson=l1, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b, "L1 Page 2 diagram block should exist")
        self.assertIn('svg_content', p2_b.metadata)

        p3_b = LessonBlock.objects.filter(lesson=l1, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b, "L1 Page 3 diagram block should exist")
        self.assertIn('svg_content', p3_b.metadata)

        # Lesson 2: Finding and Interpreting Transformation Matrices
        l2 = lessons[1]
        p2_b_l2 = LessonBlock.objects.filter(lesson=l2, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b_l2, "L2 Page 2 diagram block should exist")

        p3_b_l2 = LessonBlock.objects.filter(lesson=l2, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b_l2, "L2 Page 3 diagram block should exist")

        # Lesson 3: Successive Transformations & Simulation Fix
        l3 = lessons[2]
        p2_b_l3 = LessonBlock.objects.filter(lesson=l3, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b_l3, "L3 Page 2 diagram block should exist")

        sim_b = LessonBlock.objects.filter(lesson=l3, page_number=8).first()
        self.assertIsNotNone(sim_b, "L3 Page 8 simulation block should exist")
        self.assertEqual(sim_b.block_type, 'simulation_placeholder', "Block 13263 should be simulation_placeholder")
        self.assertEqual(sim_b.metadata.get('simulation_key'), 'math_matrix_transformation')

        # Lesson 4: Determinant, Area Scale Factor, Shear and Stretch
        l4 = lessons[3]
        p2_b_l4 = LessonBlock.objects.filter(lesson=l4, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b_l4, "L4 Page 2 diagram block should exist")

        p3_b_l4 = LessonBlock.objects.filter(lesson=l4, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b_l4, "L4 Page 3 diagram block should exist")

        print("ALL TOPIC 1 ENRICHMENT ASSERTIONS PASSED PERFECTLY!")
