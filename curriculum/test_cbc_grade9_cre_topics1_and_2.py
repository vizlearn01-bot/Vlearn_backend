"""
Unit and Integration Tests for CBC Grade 9 CRE — Topics 1 & 2 (All 12 Lessons)
"""

import pytest
import django
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestCBCGrade9CRETopics1And2:

    def test_01_topics_count_and_naming(self):
        g9 = Grade.objects.get(id=18)
        cre = Subject.objects.get(id=50, grade=g9)
        assert cre.topics.count() == 2

        t1 = cre.topics.get(order=1)
        assert t1.name == 'Work'
        assert t1.learning_units.count() == 6

        t2 = cre.topics.get(order=2)
        assert t2.name == 'Christian Moral Values'
        assert t2.learning_units.count() == 6

    def test_02_all_12_lessons_published(self):
        cre = Subject.objects.get(id=50)
        for t_order in (1, 2):
            topic = cre.topics.get(order=t_order)
            for u_order in range(1, 7):
                unit = topic.learning_units.get(order=u_order)
                lessons = unit.lessons.filter(status='published')
                assert lessons.count() == 1, f'Topic {t_order} Unit {u_order} does not have exactly 1 published lesson'
                lesson = lessons.first()
                assert len(lesson.title) > 0

    def test_03_six_cards_per_lesson_all_12(self):
        cre = Subject.objects.get(id=50)
        for t_order in (1, 2):
            topic = cre.topics.get(order=t_order)
            for u_order in range(1, 7):
                unit = topic.learning_units.get(order=u_order)
                lesson = unit.lessons.get(status='published')
                pages = set(lesson.blocks.values_list('page_number', flat=True))
                assert len(pages) == 6, f'Topic {t_order} Lesson {lesson.id} has {len(pages)} pages'
                assert sorted(pages) == [1, 2, 3, 4, 5, 6]

    def test_04_thirteen_blocks_and_correct_types_per_lesson(self):
        cre = Subject.objects.get(id=50)
        expected_types = {
            'suggested_image', 'learning_goal', 'concept_explanation',
            'suggested_diagram', 'step_process', 'suggested_video',
            'summary', 'knowledge_check'
        }
        for t_order in (1, 2):
            topic = cre.topics.get(order=t_order)
            for u_order in range(1, 7):
                unit = topic.learning_units.get(order=u_order)
                lesson = unit.lessons.get(status='published')
                assert lesson.blocks.count() == 13, f'Lesson {lesson.id} has {lesson.blocks.count()} blocks'
                types = set(lesson.blocks.values_list('block_type', flat=True))
                assert types.issubset(expected_types), f'Lesson {lesson.id} contains unmapped types: {types - expected_types}'

    def test_05_three_assets_per_lesson_all_12(self):
        cre = Subject.objects.get(id=50)
        for t_order in (1, 2):
            topic = cre.topics.get(order=t_order)
            for u_order in range(1, 7):
                unit = topic.learning_units.get(order=u_order)
                lesson = unit.lessons.get(status='published')
                assets = lesson.assets.all()
                assert assets.count() == 3, f'Lesson {lesson.id} has {assets.count()} assets'
                types = set(assets.values_list('asset_type', flat=True))
                assert types == {'image', 'diagram', 'youtube'}, f'Lesson {lesson.id} missing assets: {types}'

    def test_06_svg_diagram_xml_validity(self):
        cre = Subject.objects.get(id=50)
        for t_order in (1, 2):
            topic = cre.topics.get(order=t_order)
            for u_order in range(1, 7):
                unit = topic.learning_units.get(order=u_order)
                lesson = unit.lessons.get(status='published')
                diag_asset = lesson.assets.get(asset_type='diagram')
                svg_xml = diag_asset.metadata.get('svg_xml') or ''
                assert '<svg' in svg_xml
                assert '</svg>' in svg_xml
                assert 'viewBox="0 0 800 450"' in svg_xml
                assert '#0f172a' in svg_xml

    def test_07_mcq_structure_validity(self):
        cre = Subject.objects.get(id=50)
        for t_order in (1, 2):
            topic = cre.topics.get(order=t_order)
            for u_order in range(1, 7):
                unit = topic.learning_units.get(order=u_order)
                lesson = unit.lessons.get(status='published')
                mcq_block = lesson.blocks.get(block_type='knowledge_check')
                content = mcq_block.content
                assert 'question' in content
                assert len(content.get('options', [])) == 4
                assert content.get('answer') in {'A', 'B', 'C', 'D'}
                assert len(content.get('explanation', '')) > 0

    def test_08_scope_isolation_verification(self):
        g10_cre = Subject.objects.get(id=46)
        assert g10_cre.topics.count() == 23

        g9_agri = Subject.objects.get(id=31)
        assert g9_agri.topics.count() == 4
