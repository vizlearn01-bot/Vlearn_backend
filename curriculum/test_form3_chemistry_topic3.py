"""
Test suite for Form 3 Chemistry Topic 3: Organic Chemistry I
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def test_form3_chemistry_topic3():
    grade = Grade.objects.get(name="Form 3")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topic = Topic.objects.get(subject=subject, id=24)

    assert "Organic Chemistry I" in topic.name

    lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
    assert len(lessons) == 7, f"Expected 7 published lessons, found {len(lessons)}"

    for lesson in lessons:
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order'))
        assert len(blocks) >= 8, f"Lesson {lesson.id} has too few blocks ({len(blocks)})"

        # Check image assets
        image_assets = LessonAsset.objects.filter(lesson=lesson, asset_type='image')
        assert image_assets.exists(), f"Lesson {lesson.id} missing image assets"

        # Check that no generic placeholder URLs exist
        for img in image_assets:
            assert "States_of_matter" not in str(img.url), f"Lesson {lesson.id} still has placeholder image"
            assert "Diffusion_of_ammonia" not in str(img.url), f"Lesson {lesson.id} still has placeholder image"

        # Check knowledge checks
        mcq_blocks = [b for b in blocks if b.block_type == "knowledge_check"]
        assert len(mcq_blocks) >= 1, f"Lesson {lesson.id} missing knowledge checks"

        for mcq in mcq_blocks:
            c = mcq.content or {}
            assert "options" in c and len(c["options"]) == 4, f"MCQ in block {mcq.id} must have 4 options"
            assert "answer" in c and c["answer"] in ["A", "B", "C", "D"], f"MCQ in block {mcq.id} has invalid answer: {c.get('answer')}"
            assert "explanation" in c and len(c["explanation"]) > 10, f"MCQ in block {mcq.id} explanation too short"

    # Verify videos in Lesson 177 and 179
    l177 = Lesson.objects.get(id=177)
    l179 = Lesson.objects.get(id=179)
    assert LessonAsset.objects.filter(lesson=l177, asset_type='youtube').exists(), "Lesson 177 missing video"
    assert LessonAsset.objects.filter(lesson=l179, asset_type='youtube').exists(), "Lesson 179 missing video"

    print("✅ All 7 Form 3 Chemistry Topic 3 lessons passed validation tests!")

if __name__ == "__main__":
    test_form3_chemistry_topic3()
