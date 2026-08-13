import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import TestCase
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.ingest_form4_math_topic7_loci import ingest_topic7_loci
from curriculum.enrich_form4_math_topic7_loci import enrich_topic7_loci

class Form4MathTopic7EnrichmentTestCase(TestCase):
    def setUp(self):
        ingest_topic7_loci()
        enrich_topic7_loci()

    def test_topic7_enrichment_blocks_and_assets(self):
        topic = Topic.objects.filter(subject__name='Mathematics', order=7).first()
        self.assertIsNotNone(topic, "Topic 7 Mathematics should exist")

        lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
        self.assertEqual(len(lessons), 4, "Topic 7 should have 4 lessons")

        # Lesson 1: Foundational 2D and 3D Loci
        l1 = lessons[0]
        p2_b1 = LessonBlock.objects.filter(lesson=l1, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b1, "L1 Page 2 diagram block should exist")

        p3_b1 = LessonBlock.objects.filter(lesson=l1, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b1, "L1 Page 3 diagram block should exist")

        p4_b1 = LessonBlock.objects.filter(lesson=l1, page_number=4, block_type='suggested_diagram').first()
        self.assertIsNotNone(p4_b1, "L1 Page 4 diagram block should exist")

        p9_b1 = LessonBlock.objects.filter(lesson=l1, page_number=9, block_type='suggested_diagram').first()
        self.assertIsNotNone(p9_b1, "L1 Page 9 diagram block should exist")

        sim_b1 = LessonBlock.objects.filter(lesson=l1, page_number=8).first()
        self.assertIsNotNone(sim_b1, "L1 Page 8 simulation block should exist")
        self.assertEqual(sim_b1.block_type, 'simulation_placeholder')

        # Lesson 2: Conditional Loci & Geometric Inequalities
        l2 = lessons[1]
        p2_b2 = LessonBlock.objects.filter(lesson=l2, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b2, "L2 Page 2 diagram block should exist")

        sim_b2 = LessonBlock.objects.filter(lesson=l2, page_number=8).first()
        self.assertIsNotNone(sim_b2, "L2 Page 8 simulation block should exist")
        self.assertEqual(sim_b2.block_type, 'simulation_placeholder')

        # Lesson 3: Constant Angle Loci
        l3 = lessons[2]
        p2_b3 = LessonBlock.objects.filter(lesson=l3, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b3, "L3 Page 2 diagram block should exist")

        sim_b3 = LessonBlock.objects.filter(lesson=l3, page_number=8).first()
        self.assertIsNotNone(sim_b3, "L3 Page 8 simulation block should exist")
        self.assertEqual(sim_b3.block_type, 'simulation_placeholder')

        # Lesson 4: Intersecting Loci & Chords Theorem
        l4 = lessons[3]
        p2_b4 = LessonBlock.objects.filter(lesson=l4, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b4, "L4 Page 2 diagram block should exist")

        sim_b4 = LessonBlock.objects.filter(lesson=l4, page_number=8).first()
        self.assertIsNotNone(sim_b4, "L4 Page 8 simulation block should exist")
        self.assertEqual(sim_b4.block_type, 'simulation_placeholder')

        print("ALL TOPIC 7 LOCI ENRICHMENT ASSERTIONS PASSED PERFECTLY!")
