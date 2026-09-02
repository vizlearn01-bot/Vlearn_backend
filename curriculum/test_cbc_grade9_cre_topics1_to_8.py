"""
Master Test Suite for CBC Grade 9 CRE — Topics 1 to 8 (50 Lessons Total)
"""

import pytest
import django
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestCBCGrade9CRETopics1To8:

    def test_01_topics_and_units_count(self):
        g9 = Grade.objects.get(id=18)
        cre = Subject.objects.get(id=50, grade=g9)
        assert cre.topics.count() == 8

        expected_units = {1: 6, 2: 6, 3: 6, 4: 8, 5: 6, 6: 6, 7: 6, 8: 6}
        for t_order, exp_cnt in expected_units.items():
            topic = cre.topics.get(order=t_order)
            assert topic.learning_units.count() == exp_cnt, f'Topic {t_order} expected {exp_cnt} units, got {topic.learning_units.count()}'

    def test_02_all_fifty_lessons_published(self):
        cre = Subject.objects.get(id=50)
        total_published = 0
        for topic in cre.topics.all().order_by('order'):
            for unit in topic.learning_units.all().order_by('order'):
                lessons = unit.lessons.filter(status='published')
                assert lessons.count() == 1, f'Topic {topic.order} Unit {unit.order} does not have exactly 1 published lesson'
                lesson = lessons.first()
                assert len(lesson.title) > 0
                total_published += 1
        assert total_published == 50

    def test_03_six_cards_per_lesson_all_fifty(self):
        cre = Subject.objects.get(id=50)
        for topic in cre.topics.all().order_by('order'):
            for unit in topic.learning_units.all().order_by('order'):
                lesson = unit.lessons.get(status='published')
                pages = set(lesson.blocks.values_list('page_number', flat=True))
                assert len(pages) == 6, f'Topic {topic.order} Lesson {lesson.id} has {len(pages)} pages'
                assert sorted(pages) == [1, 2, 3, 4, 5, 6]

    def test_04_thirteen_blocks_and_correct_types_all_fifty(self):
        cre = Subject.objects.get(id=50)
        expected_types = {
            'suggested_image', 'learning_goal', 'concept_explanation',
            'suggested_diagram', 'step_process', 'suggested_video',
            'summary', 'knowledge_check'
        }
        for topic in cre.topics.all().order_by('order'):
            for unit in topic.learning_units.all().order_by('order'):
                lesson = unit.lessons.get(status='published')
                assert lesson.blocks.count() == 13, f'Topic {topic.order} Lesson {lesson.id} has {lesson.blocks.count()} blocks'
                types = set(lesson.blocks.values_list('block_type', flat=True))
                assert types.issubset(expected_types), f'Topic {topic.order} Lesson {lesson.id} unmapped types: {types - expected_types}'

    def test_05_three_assets_per_lesson_all_fifty(self):
        cre = Subject.objects.get(id=50)
        for topic in cre.topics.all().order_by('order'):
            for unit in topic.learning_units.all().order_by('order'):
                lesson = unit.lessons.get(status='published')
                assets = lesson.assets.all()
                assert assets.count() == 3, f'Topic {topic.order} Lesson {lesson.id} has {assets.count()} assets'
                types = set(assets.values_list('asset_type', flat=True))
                assert types == {'image', 'diagram', 'youtube'}, f'Topic {topic.order} Lesson {lesson.id} missing types: {types}'

    def test_06_svg_diagram_xml_validity_all_fifty(self):
        cre = Subject.objects.get(id=50)
        for topic in cre.topics.all().order_by('order'):
            for unit in topic.learning_units.all().order_by('order'):
                lesson = unit.lessons.get(status='published')
                diag_asset = lesson.assets.get(asset_type='diagram')
                svg_xml = diag_asset.metadata.get('svg_xml') or ''
                assert '<svg' in svg_xml
                assert '</svg>' in svg_xml
                assert 'viewBox="0 0 800 450"' in svg_xml
                assert '#0f172a' in svg_xml

    def test_07_mcq_structure_validity_all_fifty(self):
        cre = Subject.objects.get(id=50)
        for topic in cre.topics.all().order_by('order'):
            for unit in topic.learning_units.all().order_by('order'):
                lesson = unit.lessons.get(status='published')
                mcq_block = lesson.blocks.get(block_type='knowledge_check')
                content = mcq_block.content
                assert 'question' in content
                options = content.get('options') or content.get('options_list') or []
                assert len(options) == 4, f'Topic {topic.order} Lesson {lesson.id} MCQ options count is {len(options)}'
                answer = content.get('answer') or content.get('correct_answer')
                assert answer in {'A', 'B', 'C', 'D'}, f'Topic {topic.order} Lesson {lesson.id} invalid answer {answer}'
                explanation = content.get('explanation') or content.get('feedback') or ''
                assert len(explanation) > 0

    def test_08_scope_isolation(self):
        g10_cre = Subject.objects.get(id=46)
        assert g10_cre.topics.count() == 23

        g9_agri = Subject.objects.get(id=31)
        assert g9_agri.topics.count() == 4
