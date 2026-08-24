"""
Test suite for Form 3 Chemistry Topic 4: Nitrogen and its Compounds
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def test_form3_chemistry_topic4():
    grade = Grade.objects.get(name="Form 3")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topic = Topic.objects.get(subject=subject, id=25)

    assert "Nitrogen" in topic.name

    lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
    assert len(lessons) == 6, f"Expected 6 published lessons, found {len(lessons)}"

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

    # Verify videos in Lesson 182 and 184
    l182 = Lesson.objects.get(id=182)
    l184 = Lesson.objects.get(id=184)
    assert LessonAsset.objects.filter(lesson=l182, asset_type='youtube').exists(), "Lesson 182 missing video"
    assert LessonAsset.objects.filter(lesson=l184, asset_type='youtube').exists(), "Lesson 184 missing video"

    print("✅ All 6 Form 3 Chemistry Topic 4 lessons passed validation tests!")

if __name__ == "__main__":
    test_form3_chemistry_topic4()
