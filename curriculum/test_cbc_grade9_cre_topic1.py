"""
Unit and Integration Tests for CBC Grade 9 CRE — Topic 1 (Lessons 1-5)
"""

import pytest
import django
import os
import sys

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


@pytest.mark.django_db
class TestCBCGrade9CRETopic1:

    def test_01_subject_and_topic_hierarchy(self):
        grade9 = Grade.objects.get(id=18)
        assert grade9.name == 'Grade 9'

        subject = Subject.objects.get(id=50, grade=grade9)
        assert subject.name == 'CRE'

        topic = Topic.objects.get(subject=subject, order=1)
        assert topic.name == 'Work'

        units = topic.learning_units.all().order_by('order')
        assert units.count() >= 5

    def test_02_first_five_lessons_exist_and_published(self):
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(subject=subject, order=1)

        for u_order in range(1, 6):
            unit = topic.learning_units.get(order=u_order)
            lessons = unit.lessons.filter(status='published')
            assert lessons.exists(), f'Unit {u_order} has no published lesson'
            lesson = lessons.first()
            assert lesson.version >= 1
            assert lesson.title is not None and len(lesson.title) > 0

    def test_03_six_pages_per_lesson(self):
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(subject=subject, order=1)

        for u_order in range(1, 6):
            unit = topic.learning_units.get(order=u_order)
            lesson = unit.lessons.filter(status='published').first()
            pages = set(lesson.blocks.values_list('page_number', flat=True))
            assert len(pages) == 6, f'Lesson {lesson.id} has {len(pages)} pages instead of 6'
            assert sorted(pages) == [1, 2, 3, 4, 5, 6]

    def test_04_lesson_assets_attached(self):
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(subject=subject, order=1)

        for u_order in range(1, 6):
            unit = topic.learning_units.get(order=u_order)
            lesson = unit.lessons.filter(status='published').first()
            assets = lesson.assets.all()
            assert assets.count() >= 3, f'Lesson {lesson.id} has {assets.count()} assets'

            asset_types = set(assets.values_list('asset_type', flat=True))
            assert 'image' in asset_types, f'Lesson {lesson.id} missing image asset'
            assert 'diagram' in asset_types, f'Lesson {lesson.id} missing diagram asset'
            assert 'youtube' in asset_types, f'Lesson {lesson.id} missing youtube asset'

    def test_05_interactive_mcq_structure(self):
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(subject=subject, order=1)

        for u_order in range(1, 6):
            unit = topic.learning_units.get(order=u_order)
            lesson = unit.lessons.filter(status='published').first()
            mcq_blocks = lesson.blocks.filter(block_type='knowledge_check')
            assert mcq_blocks.exists(), f'Lesson {lesson.id} missing knowledge check MCQ'
            
            for b in mcq_blocks:
                content = b.content
                assert 'question' in content or 'text' in content or isinstance(content, dict)
                options = content.get('options') or content.get('options_list') or []
                assert len(options) == 4, f'Lesson {lesson.id} MCQ does not have 4 options'
                assert 'answer' in content or 'correct_answer' in content or 'correct' in content

    def test_06_svg_diagram_integrity(self):
        subject = Subject.objects.get(id=50)
        topic = Topic.objects.get(subject=subject, order=1)

        for u_order in range(1, 6):
            unit = topic.learning_units.get(order=u_order)
            lesson = unit.lessons.filter(status='published').first()
            diagram_blocks = lesson.blocks.filter(block_type='suggested_diagram')
            assert diagram_blocks.exists(), f'Lesson {lesson.id} missing diagram block'
            
            for d in diagram_blocks:
                content = d.content
                svg = content.get('svg') or content.get('svg_xml') or content.get('svg_content') or d.metadata.get('svg_content') or ''
                if not svg and d.assets.filter(asset_type='diagram').exists():
                    diag_asset = d.assets.filter(asset_type='diagram').first()
                    svg = diag_asset.metadata.get('svg_xml') or diag_asset.metadata.get('svg_content') or ''
                assert '<svg' in svg, f'Lesson {lesson.id} diagram block missing valid SVG markup'
                assert '</svg>' in svg, f'Lesson {lesson.id} diagram block has unclosed SVG markup'
                assert 'viewBox' in svg, f'Lesson {lesson.id} SVG missing viewBox attribute'

    def test_07_scope_isolation_preserved(self):
        # Grade 10 CRE must remain untouched (23 topics)
        g10_cre = Subject.objects.get(id=46)
        assert g10_cre.topics.count() == 23

        # Grade 9 Agriculture must remain untouched (4 topics)
        g9_agri = Subject.objects.get(id=31)
        assert g9_agri.topics.count() == 4
