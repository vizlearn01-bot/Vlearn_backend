import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import TestCase
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.ingest_form4_math_topic2_statistics import ingest_form4_math_topic2
from curriculum.enrich_form4_math_topic2_statistics import enrich_topic2_statistics

class Form4MathTopic2EnrichmentTestCase(TestCase):
    def setUp(self):
        ingest_form4_math_topic2()
        enrich_topic2_statistics()

    def test_topic2_enrichment_blocks_and_assets(self):
        topic = Topic.objects.filter(subject__name='Mathematics', order=2).first()
        self.assertIsNotNone(topic, "Topic 2 Mathematics should exist")

        lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
        self.assertEqual(len(lessons), 4, "Topic 2 should have 4 lessons")

        # Lesson 1: Assumed Mean & Step-Deviation
        l1 = lessons[0]
        p2_b1 = LessonBlock.objects.filter(lesson=l1, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b1, "L1 Page 2 diagram block should exist")
        self.assertIn('svg_content', p2_b1.metadata)

        p3_b1 = LessonBlock.objects.filter(lesson=l1, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b1, "L1 Page 3 diagram block should exist")
        self.assertIn('svg_content', p3_b1.metadata)

        sim_b1 = LessonBlock.objects.filter(lesson=l1, page_number=8).first()
        self.assertIsNotNone(sim_b1, "L1 Page 8 simulation block should exist")
        self.assertEqual(sim_b1.block_type, 'simulation_placeholder')

        # Lesson 2: Cumulative Frequency Tables and Ogives
        l2 = lessons[1]
        p2_b2 = LessonBlock.objects.filter(lesson=l2, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b2, "L2 Page 2 diagram block should exist")

        p3_b2 = LessonBlock.objects.filter(lesson=l2, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b2, "L2 Page 3 diagram block should exist")

        sim_b2 = LessonBlock.objects.filter(lesson=l2, page_number=8).first()
        self.assertIsNotNone(sim_b2, "L2 Page 8 simulation block should exist")
        self.assertEqual(sim_b2.block_type, 'simulation_placeholder')

        # Lesson 3: Median, Quartiles, and Percentiles by Calculation
        l3 = lessons[2]
        p2_b3 = LessonBlock.objects.filter(lesson=l3, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b3, "L3 Page 2 diagram block should exist")

        p3_b3 = LessonBlock.objects.filter(lesson=l3, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b3, "L3 Page 3 diagram block should exist")

        # Lesson 4: Measures of Dispersion & Moving Averages
        l4 = lessons[3]
        p2_b4 = LessonBlock.objects.filter(lesson=l4, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b4, "L4 Page 2 diagram block should exist")

        p7_b4 = LessonBlock.objects.filter(lesson=l4, page_number=7, block_type='suggested_diagram').first()
        self.assertIsNotNone(p7_b4, "L4 Page 7 diagram block should exist")

        sim_b4 = LessonBlock.objects.filter(lesson=l4, page_number=8).first()
        self.assertIsNotNone(sim_b4, "L4 Page 8 simulation block should exist")
        self.assertEqual(sim_b4.block_type, 'simulation_placeholder')

        print("ALL TOPIC 2 STATISTICS II ENRICHMENT ASSERTIONS PASSED PERFECTLY!")
