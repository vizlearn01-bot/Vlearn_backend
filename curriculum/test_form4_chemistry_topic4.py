"""
Test suite for Form 4 Chemistry Topic 4: Electrochemistry
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def test_form4_chemistry_topic4():
    grade = Grade.objects.get(name="Form 4")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topic = Topic.objects.get(subject=subject, id=15)

    assert topic.name == "Topic 4: Electrochemistry"

    lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
    assert len(lessons) == 25, f"Expected 25 published lessons, found {len(lessons)}"

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
        assert LessonAsset.objects.filter(lesson=lesson, asset_type='image').exists(), f"Lesson {lesson.id} missing image assets"
        assert LessonAsset.objects.filter(lesson=lesson, asset_type='diagram').exists(), f"Lesson {lesson.id} missing diagram assets"

        # Check knowledge checks
        mcq_blocks = [b for b in blocks if b.block_type == "knowledge_check"]
        assert len(mcq_blocks) >= 2, f"Lesson {lesson.id} missing knowledge checks"

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

    # Verify videos in key lessons
    for lid in [92, 96, 97]:
        l = Lesson.objects.get(id=lid)
        assert LessonAsset.objects.filter(lesson=l, asset_type='youtube').exists(), f"Lesson {lid} missing video"

    print("✅ All 25 Form 4 Chemistry Topic 4 lessons passed validation tests!")

if __name__ == "__main__":
    test_form4_chemistry_topic4()
