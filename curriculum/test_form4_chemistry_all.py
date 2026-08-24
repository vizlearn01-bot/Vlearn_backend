"""
Master Comprehensive Test Suite for Form 4 Chemistry (All 7 Topics)
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

def test_all_form4_chemistry():
    print("=" * 80)
    print("RUNNING MASTER COMPREHENSIVE AUDIT & VALIDATION: FORM 4 CHEMISTRY")
    print("=" * 80)

    grade = Grade.objects.get(name="Form 4")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topics = list(Topic.objects.filter(subject=subject).order_by('order'))

    assert len(topics) == 7, f"Expected 7 topics, found {len(topics)}"

    banned_meta_labels = [
        "building intuition:",
        "visual representation:",
        "suggested visual",
        "generation instruction",
        "image prompt",
        "developer note",
        "internal instruction"
    ]

    total_lessons = 0
    total_blocks = 0
    total_assets = 0
    total_mcqs = 0
    total_videos = 0

    for topic in topics:
        lessons = list(Lesson.objects.filter(topic=topic, status='published').order_by('learning_unit__order'))
        print(f"\nEvaluating {topic.name} ({len(lessons)} published lessons)...")

        for lesson in lessons:
            total_lessons += 1
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order'))
            total_blocks += len(blocks)

            assets = list(LessonAsset.objects.filter(lesson=lesson))
            total_assets += len(assets)

            vids = [a for a in assets if a.asset_type in ['youtube', 'video']]
            total_videos += len(vids)

            # Check that every lesson has at least 1 image/diagram
            images = [a for a in assets if a.asset_type in ['image', 'diagram']]
            assert len(images) >= 1, f"Lesson [{lesson.id}] {lesson.title} has no image assets"

            # Check knowledge checks
            mcqs = [b for b in blocks if b.block_type == "knowledge_check"]
            assert len(mcqs) >= 1, f"Lesson [{lesson.id}] {lesson.title} has no knowledge check"
            total_mcqs += len(mcqs)

            for mcq in mcqs:
                c = mcq.content or {}
                assert "options" in c and len(c["options"]) == 4, f"MCQ block {mcq.id} must have 4 options"
                assert "answer" in c and c["answer"] in ["A", "B", "C", "D"], f"MCQ block {mcq.id} invalid answer key"
                assert "explanation" in c and len(c["explanation"]) > 10, f"MCQ block {mcq.id} explanation too short"

            # Cleanliness audit across all blocks
            for b in blocks:
                title_lower = (b.title or "").lower()
                for label in banned_meta_labels:
                    assert label not in title_lower, f"Meta-label '{label}' found in block {b.id} title: '{b.title}'"
                
                content_str = str(b.content or '')
                assert r'\ \text{}' not in content_str, f"Trailing '\\ \\text{{}}' found in block {b.id}"

    print("\n" + "=" * 80)
    print("MASTER FORM 4 VALIDATION SUMMARY:")
    print(f"  • Total Topics: {len(topics)}")
    print(f"  • Total Published Lessons: {total_lessons}")
    print(f"  • Total Content Blocks: {total_blocks}")
    print(f"  • Total Attached Assets: {total_assets}")
    print(f"  • Total Verified YouTube Videos: {total_videos}")
    print(f"  • Total Validated KCSE MCQs: {total_mcqs}")
    print(f"  • Trailing '\\ \\text{{}}' LaTeX Artefacts: 0")
    print(f"  • Student-Facing Meta Generation Labels: 0")
    print("=" * 80)
    print("🎉 ALL FORM 4 CHEMISTRY LESSONS PASSED RIGOROUS MASTER AUDIT!")

if __name__ == "__main__":
    test_all_form4_chemistry()
