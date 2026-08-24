"""
Test suite for Form 4 Chemistry Topic 1: Acids, Bases and Salts
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def test_form4_chemistry_topic1():
    grade = Grade.objects.get(name="Form 4")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topic = Topic.objects.get(subject=subject, id=12)

    assert topic.name == "Topic 1: Acids, Bases and Salts"

    lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
    assert len(lessons) == 14, f"Expected 14 published lessons, found {len(lessons)}"

    banned_meta_labels = [
        "building intuition:",
        "visual representation:",
        "real-world hook",
        "developer note",
        "image prompt"
    ]

    for lesson in lessons:
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order'))
        assert len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})"

        # Check that each lesson has at least 1 image asset
        image_assets = LessonAsset.objects.filter(lesson=lesson, asset_type='image')
        assert image_assets.exists(), f"Lesson {lesson.id} missing image assets"

        # Check that each lesson has at least 1 diagram asset
        diagram_assets = LessonAsset.objects.filter(lesson=lesson, asset_type='diagram')
        assert diagram_assets.exists(), f"Lesson {lesson.id} missing diagram assets"

        # Check knowledge checks
        mcq_blocks = [b for b in blocks if b.block_type == "knowledge_check"]
        assert len(mcq_blocks) >= 2, f"Lesson {lesson.id} expected >=2 knowledge checks, got {len(mcq_blocks)}"

        for mcq in mcq_blocks:
            c = mcq.content or {}
            assert "options" in c and len(c["options"]) == 4, f"MCQ in block {mcq.id} must have 4 options"
            assert "answer" in c and c["answer"] in ["A", "B", "C", "D"], f"MCQ in block {mcq.id} has invalid answer: {c.get('answer')}"
            assert "explanation" in c and len(c["explanation"]) > 10, f"MCQ in block {mcq.id} explanation too short"

        # Check title cleanliness
        for b in blocks:
            title_lower = (b.title or "").lower()
            for label in banned_meta_labels:
                assert label not in title_lower, f"Meta-label '{label}' found in block {b.id} title '{b.title}'"
            
            # Check equation cleanliness in content
            content_str = str(b.content or '')
            assert r'\ \text{}' not in content_str, f"Trailing '\\ \\text{{}}' found in block {b.id}"

    print("✅ All 14 Form 4 Chemistry Topic 1 lessons passed validation tests!")

if __name__ == "__main__":
    test_form4_chemistry_topic1()
