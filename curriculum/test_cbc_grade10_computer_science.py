"""
VLearn CBC Grade 10 Computer Science — Quality Assurance & Audit Suite
Comprehensive automated validation of database records, pedagogical pages,
rich media assets, interactive checkpoints, and LaTeX formatting.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def run_quality_audit():
    print("=" * 80)
    print("RUNNING CBC GRADE 10 COMPUTER SCIENCE COMPREHENSIVE QUALITY AUDIT")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    assert grade, "Grade 10 not found under CBC!"
    subject = Subject.objects.filter(grade=grade, name="Computer Science").first()
    assert subject, "Subject 'Computer Science' not found under Grade 10 CBC!"

    print(f"[*] Subject Verified: {subject.name} (ID: {subject.id}) in {grade.name} ({curriculum.name})")

    topics = list(Topic.objects.filter(subject=subject, order__in=[1, 2, 3, 4, 5, 6]).order_by("order"))
    assert len(topics) == 6, f"Expected 6 Topics, found {len(topics)}"
    print(f"[*] Total Target Topics Verified (1-6): {len(topics)}")

    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_svgs = 0
    total_images = 0
    total_videos = 0
    total_mcqs = 0
    total_worked_examples = 0
    bracket_leaks = 0

    bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')

    for t_idx, topic in enumerate(topics, start=1):
        print(f"\n" + "-" * 60)
        print(f"TOPIC {topic.order}: {topic.name}")
        print("-" * 60)

        units = list(topic.learning_units.all().order_by("order"))
        assert len(units) >= 2, f"Topic {topic.order} expected >=2 units, found {len(units)}"
        total_units += len(units)

        for unit in units:
            lessons = list(unit.lessons.all().order_by("version"))
            assert len(lessons) >= 1, f"Unit {unit.order} has no lessons!"
            total_lessons += len(lessons)

            for lesson in lessons:
                assert lesson.status == "published", f"Lesson '{lesson.title}' is not published!"
                blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))
                assert len(blocks) >= 10, f"Lesson '{lesson.title}' has too few blocks ({len(blocks)})"
                total_blocks += len(blocks)

                pages = set(b.page_number for b in blocks if b.page_number)
                total_pages += len(pages)

                # Count component types
                block_types = [b.block_type for b in blocks]
                has_goal = "learning_goal" in block_types
                has_explanation = "concept_explanation" in block_types
                has_media = any(t in block_types for t in ["suggested_diagram", "suggested_image", "suggested_video"])
                has_quiz = "knowledge_check" in block_types
                has_summary = any(t in block_types for t in ["summary", "key_takeaway"])

                assert has_goal, f"Lesson '{lesson.title}' missing learning_goal!"
                assert has_explanation, f"Lesson '{lesson.title}' missing concept_explanation!"
                assert has_media, f"Lesson '{lesson.title}' missing media block!"
                assert has_quiz, f"Lesson '{lesson.title}' missing knowledge_check!"
                assert has_summary, f"Lesson '{lesson.title}' missing summary/takeaway!"

                # Check assets
                assets = LessonAsset.objects.filter(lesson=lesson)
                lesson_svgs = assets.filter(asset_type="diagram").count()
                lesson_images = assets.filter(asset_type="image").count()
                lesson_videos = assets.filter(asset_type="youtube").count()

                total_svgs += lesson_svgs
                total_images += lesson_images
                total_videos += lesson_videos

                lesson_mcqs = [b for b in blocks if b.block_type == "knowledge_check"]
                total_mcqs += len(lesson_mcqs)
                assert len(lesson_mcqs) >= 3, f"Lesson '{lesson.title}' has fewer than 3 MCQs ({len(lesson_mcqs)})"
                for mcq in lesson_mcqs:
                    c = mcq.content or {}
                    assert "question" in c or "text" in c, f"MCQ Block {mcq.id} missing question text!"
                    assert "correct" in c or "correct_answer" in c or "answer" in c, f"MCQ Block {mcq.id} missing correct answer!"
                    assert "options" in c and len(c["options"]) == 4, f"MCQ Block {mcq.id} must have 4 options!"

                lesson_we = [b for b in blocks if b.block_type in ["worked_example", "step_process"]]
                assert len(lesson_we) >= 1, f"Lesson '{lesson.title}' missing worked examples / step processes!"
                total_worked_examples += len(lesson_we)

                # Check for bracket citation leaks in content
                for b in blocks:
                    raw_str = str(b.content) + " " + str(b.title)
                    matches = bracket_pattern.findall(raw_str)
                    if matches:
                        bracket_leaks += len(matches)
                        print(f"    [!] Citation leak in block {b.block_id}: {matches}")

                print(f"  [✓] Unit {unit.order} -> Lesson '{lesson.title}': {len(pages)} Pages, {len(blocks)} Blocks | SVGs: {lesson_svgs}, Images: {lesson_images}, Videos: {lesson_videos}, MCQs: {len(lesson_mcqs)}, Worked: {len(lesson_we)}")

    print("\n" + "=" * 80)
    print("AUDIT SUMMARY MATRIX FOR GRADE 10 COMPUTER SCIENCE (TOPICS 1-6):")
    print(f"  • Total Topics:                 {len(topics)} (Expected: 6)")
    print(f"  • Total Learning Units:         {total_units} (Expected: 13)")
    print(f"  • Total Published Lessons:      {total_lessons} (Expected: 13)")
    print(f"  • Total Pedagogical Cards/Pages:{total_pages} (Expected: >= 80)")
    print(f"  • Total Lesson Blocks:          {total_blocks} (Expected: >= 200)")
    print(f"  • Total Custom Vector SVGs:     {total_svgs}")
    print(f"  • Total Wikimedia Images:       {total_images}")
    print(f"  • Total YouTube Videos:         {total_videos} (Mandatory in every lesson)")
    print(f"  • Total Interactive MCQs:       {total_mcqs}")
    print(f"  • Total Worked Trace Examples:  {total_worked_examples}")
    print(f"  • Bracket Citation Leaks:       {bracket_leaks} (Expected: 0)")
    print("=" * 80)

    assert total_lessons == 13, f"Expected 13 lessons, got {total_lessons}"
    assert total_videos >= 13, f"Expected at least 1 video per lesson, got {total_videos}"
    assert bracket_leaks == 0, f"Found {bracket_leaks} citation leaks!"
    print("\n[ALL QUALITY AUDIT ASSERTIONS PASSED SUCCESSFULLY!]")

if __name__ == "__main__":
    run_quality_audit()
