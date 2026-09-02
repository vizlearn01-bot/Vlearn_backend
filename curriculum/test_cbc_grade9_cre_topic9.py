"""
Master Test Suite for CBC Grade 9 CRE — Topic 9: Jesus' Ministry in Jerusalem (8 Lessons Total)
"""

import pytest
import django
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


class TestCBCGrade9CRETopic9:

    def test_01_topic_and_units_count(self):
        g9 = Grade.objects.get(id=18)
        cre = Subject.objects.get(id=50, grade=g9)
        topic = cre.topics.get(order=9)
        assert topic.name == "Jesus' Ministry in Jerusalem"
        assert topic.learning_units.count() == 8, f"Expected 8 units, got {topic.learning_units.count()}"

    def test_02_all_eight_lessons_published(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        assert topic.lessons.filter(status='published').count() == 8
        for unit in topic.learning_units.all().order_by('order'):
            lessons = unit.lessons.filter(status='published')
            assert lessons.count() == 1, f"Unit {unit.order} does not have exactly 1 published lesson"
            lesson = lessons.first()
            assert len(lesson.title) > 0

    def test_03_six_cards_per_lesson(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        for unit in topic.learning_units.all().order_by('order'):
            lesson = unit.lessons.get(status='published')
            pages = set(lesson.blocks.values_list('page_number', flat=True))
            assert len(pages) == 6, f"Lesson {lesson.id} has {len(pages)} pages"
            assert sorted(pages) == [1, 2, 3, 4, 5, 6]

    def test_04_thirteen_blocks_and_correct_types(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        expected_types = {
            'suggested_image', 'learning_goal', 'concept_explanation',
            'suggested_diagram', 'step_process', 'suggested_video',
            'summary', 'knowledge_check'
        }
        for unit in topic.learning_units.all().order_by('order'):
            lesson = unit.lessons.get(status='published')
            assert lesson.blocks.count() == 13, f"Lesson {lesson.id} has {lesson.blocks.count()} blocks"
            types = set(lesson.blocks.values_list('block_type', flat=True))
            assert types.issubset(expected_types), f"Lesson {lesson.id} unmapped types: {types - expected_types}"

    def test_05_three_assets_per_lesson(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        for unit in topic.learning_units.all().order_by('order'):
            lesson = unit.lessons.get(status='published')
            assets = lesson.assets.all()
            assert assets.count() == 3, f"Lesson {lesson.id} has {assets.count()} assets"
            types = set(assets.values_list('asset_type', flat=True))
            assert types == {'image', 'diagram', 'youtube'}, f"Lesson {lesson.id} missing types: {types}"

    def test_06_svg_diagram_xml_validity(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        for unit in topic.learning_units.all().order_by('order'):
            lesson = unit.lessons.get(status='published')
            diag_asset = lesson.assets.get(asset_type='diagram')
            svg_xml = diag_asset.metadata.get('svg_xml') or ''
            assert '<svg' in svg_xml
            assert '</svg>' in svg_xml
            assert 'viewBox="0 0 800 450"' in svg_xml
            assert '#0f172a' in svg_xml

    def test_07_mcq_structure_validity(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        for unit in topic.learning_units.all().order_by('order'):
            lesson = unit.lessons.get(status='published')
            mcq_block = lesson.blocks.get(block_type='knowledge_check')
            content = mcq_block.content
            assert 'question' in content
            options = content.get('options') or []
            assert len(options) == 4, f"Lesson {lesson.id} MCQ options count is {len(options)}"
            answer = content.get('answer')
            assert answer in {'A', 'B', 'C', 'D'}, f"Lesson {lesson.id} invalid answer {answer}"
            explanation = content.get('explanation') or ''
            assert len(explanation) > 0

    def test_08_no_bracket_citations(self):
        cre = Subject.objects.get(id=50)
        topic = cre.topics.get(order=9)
        import re
        bracket_pattern = re.compile(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
        for unit in topic.learning_units.all():
            assert not bracket_pattern.search(unit.name)
            assert not bracket_pattern.search(unit.description)
            for lesson in unit.lessons.all():
                assert not bracket_pattern.search(lesson.title)
                for block in lesson.blocks.all():
                    content_str = str(block.content)
                    assert not bracket_pattern.search(content_str), f"Found bracket citation in block {block.id}"
