import os
import sys
import django

# Setup Django environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import TestCase
from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset
from curriculum.ingest_form4_math_topic3_geometry import ingest_topic3_geometry
from curriculum.enrich_form4_math_topic3_geometry import enrich_topic3_geometry

class Form4MathTopic3EnrichmentTestCase(TestCase):
    def setUp(self):
        ingest_topic3_geometry()
        enrich_topic3_geometry()

    def test_topic3_enrichment_blocks_and_assets(self):
        topic = Topic.objects.filter(subject__name='Mathematics', order=3).first()
        self.assertIsNotNone(topic, "Topic 3 Mathematics should exist")

        lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
        self.assertEqual(len(lessons), 4, "Topic 3 should have 4 lessons")

        # Lesson 1: 3D Solids, Skew Lines, and Projections
        l1 = lessons[0]
        p2_b1 = LessonBlock.objects.filter(lesson=l1, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b1, "L1 Page 2 diagram block should exist")

        p3_b1 = LessonBlock.objects.filter(lesson=l1, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b1, "L1 Page 3 diagram block should exist")

        sim_b1 = LessonBlock.objects.filter(lesson=l1, page_number=8).first()
        self.assertIsNotNone(sim_b1, "L1 Page 8 simulation block should exist")
        self.assertEqual(sim_b1.block_type, 'simulation_placeholder')

        # Lesson 2: 3D Lengths and Angles Between Lines
        l2 = lessons[1]
        p2_b2 = LessonBlock.objects.filter(lesson=l2, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b2, "L2 Page 2 diagram block should exist")

        p3_b2 = LessonBlock.objects.filter(lesson=l2, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b2, "L2 Page 3 diagram block should exist")

        sim_b2 = LessonBlock.objects.filter(lesson=l2, page_number=8).first()
        self.assertIsNotNone(sim_b2, "L2 Page 8 simulation block should exist")
        self.assertEqual(sim_b2.block_type, 'simulation_placeholder')

        # Lesson 3: Angle Between a Line and a Plane
        l3 = lessons[2]
        p2_b3 = LessonBlock.objects.filter(lesson=l3, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b3, "L3 Page 2 diagram block should exist")

        p3_b3 = LessonBlock.objects.filter(lesson=l3, page_number=3, block_type='suggested_diagram').first()
        self.assertIsNotNone(p3_b3, "L3 Page 3 diagram block should exist")

        sim_b3 = LessonBlock.objects.filter(lesson=l3, page_number=8).first()
        self.assertIsNotNone(sim_b3, "L3 Page 8 simulation block should exist")
        self.assertEqual(sim_b3.block_type, 'simulation_placeholder')

        # Lesson 4: Angle Between Two Planes (Dihedral Angle)
        l4 = lessons[3]
        p2_b4 = LessonBlock.objects.filter(lesson=l4, page_number=2, block_type='suggested_diagram').first()
        self.assertIsNotNone(p2_b4, "L4 Page 2 diagram block should exist")

        sim_b4 = LessonBlock.objects.filter(lesson=l4, page_number=8).first()
        self.assertIsNotNone(sim_b4, "L4 Page 8 simulation block should exist")
        self.assertEqual(sim_b4.block_type, 'simulation_placeholder')

        print("ALL TOPIC 3 THREE-DIMENSIONAL GEOMETRY ENRICHMENT ASSERTIONS PASSED PERFECTLY!")
