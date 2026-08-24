"""
Test suite for Form 4 Chemistry Topic 2: Energy Changes in Chemical and Physical Processes
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def test_form4_chemistry_topic2():
    grade = Grade.objects.get(name="Form 4")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topic = Topic.objects.get(subject=subject, id=13)

    assert topic.name == "Topic 2: Energy Changes in Chemical and Physical Processes"

    lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
    assert len(lessons) == 12, f"Expected 12 published lessons, found {len(lessons)}"

    banned_meta_labels = [
        "building intuition:",
        "visual representation:",
        "real-world hook",
        "developer note"
    ]

    for lesson in lessons:
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order'))
        assert len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})"

        # Check image and diagram assets
        image_assets = LessonAsset.objects.filter(lesson=lesson, asset_type='image')
        assert image_assets.exists(), f"Lesson {lesson.id} missing image assets"

        diagram_assets = LessonAsset.objects.filter(lesson=lesson, asset_type='diagram')
        assert diagram_assets.exists(), f"Lesson {lesson.id} missing diagram assets"

        # Check title cleanliness
        for b in blocks:
            title_lower = (b.title or "").lower()
            for label in banned_meta_labels:
                assert label not in title_lower, f"Meta-label '{label}' found in block {b.id} title '{b.title}'"
            
            # Check equation cleanliness in content
            content_str = str(b.content or '')
            assert r'\ \text{}' not in content_str, f"Trailing '\\ \\text{{}}' found in block {b.id}"

    # Verify Lesson 42 has video asset
    lesson_42 = Lesson.objects.get(id=42)
    assert LessonAsset.objects.filter(lesson=lesson_42, asset_type='youtube').exists(), "Lesson 42 missing video asset"

    print("✅ All 12 Form 4 Chemistry Topic 2 lessons passed validation tests!")

if __name__ == "__main__":
    test_form4_chemistry_topic2()
