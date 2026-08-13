import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import TestCase
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.ingest_form4_math_topic6_linear_programming import ingest_topic6_linear_programming
from curriculum.enrich_form4_math_topic6_linear import enrich_topic6_linear

class Form4MathTopic6EnrichmentTestCase(TestCase):
    def setUp(self):
        ingest_topic6_linear_programming()
        enrich_topic6_linear()

    def test_topic6_enrichment_blocks_and_assets(self):
        topic = Topic.objects.filter(subject__name='Mathematics', order=6).first()
        self.assertIsNotNone(topic, "Topic 6 Mathematics should exist")

        lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
        self.assertEqual(len(lessons), 4, "Topic 6 should have 4 lessons")

        # Lesson 1: Formulating Linear Inequalities
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

        # Lesson 2: Graphical Representation & KCSE Shading
        l2 = lessons[1]
        p2_b2 = LessonBlock.objects.filter(lesson=l2, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b2, "L2 Page 2 diagram block should exist")

        sim_b2 = LessonBlock.objects.filter(lesson=l2, page_number=8).first()
        self.assertIsNotNone(sim_b2, "L2 Page 8 simulation block should exist")
        self.assertEqual(sim_b2.block_type, 'simulation_placeholder')

        # Lesson 3: Algebraic Corner-Point Evaluation
        l3 = lessons[2]
        p2_b3 = LessonBlock.objects.filter(lesson=l3, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b3, "L3 Page 2 diagram block should exist")

        sim_b3 = LessonBlock.objects.filter(lesson=l3, page_number=8).first()
        self.assertIsNotNone(sim_b3, "L3 Page 8 simulation block should exist")
        self.assertEqual(sim_b3.block_type, 'simulation_placeholder')

        # Lesson 4: Graphical Search-Line Method
        l4 = lessons[3]
        p2_b4 = LessonBlock.objects.filter(lesson=l4, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b4, "L4 Page 2 diagram block should exist")

        sim_b4 = LessonBlock.objects.filter(lesson=l4, page_number=8).first()
        self.assertIsNotNone(sim_b4, "L4 Page 8 simulation block should exist")
        self.assertEqual(sim_b4.block_type, 'simulation_placeholder')

        print("ALL TOPIC 6 LINEAR PROGRAMMING ENRICHMENT ASSERTIONS PASSED PERFECTLY!")
