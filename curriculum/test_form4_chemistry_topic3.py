"""
Test suite for Form 4 Chemistry Topic 3: Reaction Rates and Reversible Reactions
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def test_form4_chemistry_topic3():
    grade = Grade.objects.get(name="Form 4")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topic = Topic.objects.get(subject=subject, id=14)

    assert topic.name == "Topic 3: Reaction Rates and Reversible Reactions"

    lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
    assert len(lessons) == 14, f"Expected 14 published lessons, found {len(lessons)}"

    banned_meta_labels = [
        "building intuition:",
        "visual representation:",
        "real-world hook",
        "developer note"
    ]

    for lesson in lessons:
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order'))
        assert len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})"

        # Check knowledge checks
        mcq_blocks = [b for b in blocks if b.block_type == "knowledge_check"]
        assert len(mcq_blocks) >= 1, f"Lesson {lesson.id} missing knowledge checks"

        for mcq in mcq_blocks:
            c = mcq.content or {}
            assert "options" in c and len(c["options"]) == 4, f"MCQ in block {mcq.id} must have 4 options"
            assert "answer" in c and c["answer"] in ["A", "B", "C", "D"], f"MCQ in block {mcq.id} has invalid answer: {c.get('answer')}"
            assert "explanation" in c and len(c["explanation"]) > 15, f"MCQ in block {mcq.id} explanation too short"
            assert c.get("check_type") == "multiple_choice", f"MCQ in block {mcq.id} not set to multiple_choice"

        # Check title and content cleanliness
        for b in blocks:
            title_lower = (b.title or "").lower()
            for label in banned_meta_labels:
                assert label not in title_lower, f"Meta-label '{label}' found in block {b.id} title '{b.title}'"
            
            content_str = str(b.content or '')
            assert r'\ \text{}' not in content_str, f"Trailing '\\ \\text{{}}' found in block {b.id}"

    # Verify videos in Lesson 75 and 76
    l75 = Lesson.objects.get(id=75)
    l76 = Lesson.objects.get(id=76)
    assert LessonAsset.objects.filter(lesson=l75, asset_type='youtube').exists(), "Lesson 75 missing video"
    assert LessonAsset.objects.filter(lesson=l76, asset_type='youtube').exists(), "Lesson 76 missing video"

    print("✅ All 14 Form 4 Chemistry Topic 3 lessons passed validation tests!")

if __name__ == "__main__":
    test_form4_chemistry_topic3()
