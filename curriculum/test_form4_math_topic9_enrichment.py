import os, sys, django
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import TestCase
from curriculum.models import Topic, Lesson, LessonBlock
from curriculum.ingest_form4_math_topic9_integration import ingest_topic9_integration
from curriculum.enrich_form4_math_topic9_integration import enrich_topic9

class Form4MathTopic9EnrichmentTestCase(TestCase):
    def setUp(self):
        ingest_topic9_integration()
        enrich_topic9()

    def test_topic9_enrichment(self):
        topic = Topic.objects.filter(subject__name='Mathematics', order=9).first()
        self.assertIsNotNone(topic, "Topic 9 Mathematics should exist")

        lessons = list(Lesson.objects.filter(topic=topic).order_by('id'))
        self.assertEqual(len(lessons), 4, "Topic 9 should have 4 lessons")

        for idx, lesson in enumerate(lessons):
            # Pages 2, 3, 4, 9 should have diagram blocks
            for page in [2, 3, 4, 9]:
                b = LessonBlock.objects.filter(lesson=lesson, page_number=page, block_type='suggested_diagram').first()
                self.assertIsNotNone(b, f"Lesson {idx+1} Page {page} diagram block should exist")

            # Page 8 should be simulation_placeholder
            sim = LessonBlock.objects.filter(lesson=lesson, page_number=8).first()
            self.assertIsNotNone(sim, f"Lesson {idx+1} Page 8 sim block should exist")
            self.assertEqual(sim.block_type, 'simulation_placeholder')
            self.assertEqual(sim.metadata.get('simulation_key'), 'math_integration_explorer')

        print("ALL TOPIC 9 INTEGRATION ENRICHMENT ASSERTIONS PASSED PERFECTLY!")
