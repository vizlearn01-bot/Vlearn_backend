"""
VLearn CBC Grade 10 Computer Science — Topic 6: Operating Systems Quality Assurance Test
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

def test_grade10_topic6():
    print("=" * 80)
    print("RUNNING QUALITY AUDIT: GRADE 10 COMPUTER SCIENCE — TOPIC 6: OPERATING SYSTEMS")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    assert grade, "Grade 10 not found!"
    subject = Subject.objects.filter(grade=grade, name="Computer Science").first()
    assert subject, "Subject 'Computer Science' not found!"

    topic = Topic.objects.filter(subject=subject, order=6).first()
    assert topic, "Topic 6 not found in database!"
    assert topic.name == "Operating Systems (OS)", f"Unexpected topic name: {topic.name}"

    print(f"[*] Topic 6 Verified: {topic.name} (ID: {topic.id})")

    units = list(topic.learning_units.all().order_by("order"))
    assert len(units) == 3, f"Expected 3 units, found {len(units)}"

    bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
    total_blocks = 0
    total_assets = 0
    total_mcqs = 0
    citation_leaks = 0

    for unit in units:
        print(f"\n[+] Unit {unit.order}: {unit.name}")
        lessons = list(unit.lessons.all())
        assert len(lessons) == 1, f"Unit {unit.order} expected 1 lesson, found {len(lessons)}"
        lesson = lessons[0]
        assert lesson.status == "published", f"Lesson {lesson.title} is not published!"

        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))
        assert len(blocks) >= 15, f"Lesson {lesson.title} has only {len(blocks)} blocks"
        total_blocks += len(blocks)

        pages = sorted(list(set(b.page_number for b in blocks if b.page_number)))
        print(f"    Lesson: '{lesson.title}' -> {len(pages)} Pages, {len(blocks)} Blocks")

        for p in pages:
            p_blocks = [b for b in blocks if b.page_number == p]
            b_types = [b.block_type for b in p_blocks]
            print(f"      Page {p}: {b_types}")

        assets = LessonAsset.objects.filter(lesson=lesson)
        total_assets += assets.count()

        for b in blocks:
            raw_str = str(b.content) + " " + str(b.title)
            matches = bracket_pattern.findall(raw_str)
            if matches:
                citation_leaks += len(matches)
                print(f"    [!] Citation leak in block {b.block_id}: {matches}")

            if b.block_type == "knowledge_check":
                total_mcqs += 1
                c = b.content or {}
                assert "question" in c, f"Block {b.block_id} missing question!"
                assert "options" in c and len(c["options"]) >= 2, f"Block {b.block_id} invalid options!"
                assert "correct_answer" in c, f"Block {b.block_id} missing correct_answer!"

    print("\n" + "=" * 80)
    print("AUDIT SUMMARY FOR TOPIC 6:")
    print(f"  • Total Units:             {len(units)} (Expected: 3)")
    print(f"  • Total Lessons:           {len(units)} (Expected: 3)")
    print(f"  • Total Blocks:            {total_blocks} (Expected: >= 45)")
    print(f"  • Total Attached Assets:   {total_assets} (Expected: >= 6)")
    print(f"  • Total Knowledge MCQs:    {total_mcqs} (Expected: >= 8)")
    print(f"  • Citation Leaks Found:    {citation_leaks} (Expected: 0)")
    print("=" * 80)

    assert citation_leaks == 0, f"Found {citation_leaks} citation leaks in content!"
    print("\n[✓] ALL TOPIC 6 QUALITY AUDIT TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_grade10_topic6()
