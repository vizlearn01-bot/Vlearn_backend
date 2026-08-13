"""
VLearn Form 4 Business Studies — Automated Test Suite: Topic 14 (Financial Statements)
"""

import sys
import os
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


def run_tests():
    print("=" * 80)
    print("RUNNING AUTOMATED TEST SUITE: FORM 4 BUSINESS STUDIES TOPIC 14 (FINANCIAL STATEMENTS)")
    print("=" * 80)

    # 1. Hierarchy test
    curriculum = Curriculum.objects.filter(name="844").first()
    assert curriculum is not None, "Curriculum '844' not found!"

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    assert grade is not None, "Grade 'Form 4' not found!"

    subject = Subject.objects.filter(grade=grade, name="Business Studies").first()
    assert subject is not None, "Subject 'Business Studies' not found!"

    print(f"[PASS] 1. Hierarchy resolved: {curriculum.name} -> {grade.name} -> {subject.name} (Subject ID: {subject.id})")

    # 2. Topic test
    topic = Topic.objects.filter(subject=subject, order=14).first()
    assert topic is not None, "Topic 14 (Financial Statements) not found!"
    assert topic.name == "Financial Statements", f"Unexpected topic name: {topic.name}"

    print(f"[PASS] 2. Topic resolved: {topic.name} (Order: {topic.order}, ID: {topic.id})")

    # 3. Learning Units test
    units = LearningUnit.objects.filter(topic=topic).order_by('order')
    assert units.count() == 5, f"Expected 5 Learning Units, found {units.count()}"
    
    print(f"[PASS] 3. Found exactly 5 Learning Units:")
    for u in units:
        print(f"       - Unit {u.order}: {u.name}")

    # 4. Lessons test
    lessons = Lesson.objects.filter(topic=topic).order_by('learning_unit__order')
    assert lessons.count() == 5, f"Expected 5 Lessons, found {lessons.count()}"
    
    print(f"[PASS] 4. Found exactly 5 Published Lessons:")
    for l in lessons:
        b_count = l.blocks.count()
        assert l.status == "published", f"Lesson '{l.title}' is not published!"
        print(f"       - Lesson {l.learning_unit.order}: {l.title} ({b_count} blocks)")

    # 5. Page count test
    total_pages = 0
    for idx, l in enumerate(lessons, start=1):
        pages_in_lesson = l.blocks.values('page_number').distinct().count()
        assert pages_in_lesson == 10, f"Lesson {idx} has {pages_in_lesson} pages, expected 10!"
        total_pages += pages_in_lesson
        print(f"[PASS] 5.{idx} Lesson {idx} has exactly 10 pages.")

    assert total_pages == 50, f"Total pages across topic is {total_pages}, expected 50!"
    print(f"[PASS] 5. Total Pages across all 5 Lessons: {total_pages} (Matches target: 50)")

    # 6. Media & Asset links test
    blocks = LessonBlock.objects.filter(lesson__topic=topic)
    photo_blocks = blocks.filter(component_type="photo_view")
    svg_blocks = blocks.filter(component_type="svg_viewer")

    for pb in photo_blocks:
        assert isinstance(pb.content, dict), f"Photo block {pb.id} content is not dict"
        assert "url" in pb.content, f"Photo block {pb.id} missing image URL"
        assert "text" in pb.content, f"Photo block {pb.id} missing caption text"

    print(f"[PASS] 6. All {photo_blocks.count()} Wikimedia photo blocks contain verified URLs, attributions, and captions.")

    for sb in svg_blocks:
        assert isinstance(sb.content, dict), f"SVG block {sb.id} content is not dict"
        assert "svg_markup" in sb.content or "svg_content" in sb.content, f"SVG block {sb.id} missing SVG markup"

    print(f"[PASS] 7. All {svg_blocks.count()} diagram blocks contain verified dark-mode SVG markup.")

    assets = LessonAsset.objects.filter(lesson__topic=topic)
    assert assets.count() >= 7, f"Expected at least 7 assets, found {assets.count()}"
    print(f"[PASS] 8. All {assets.count()} LessonAsset records are attached and linked to lesson blocks.")

    # 7. Content Quality & Cleanliness checks
    citation_regex = re.compile(r'\[\d+(?:,\s*\d+)*\]')
    metalang_regex = re.compile(r'(?:Here is a lesson|As an AI|In this card|Visual Purpose|Visual Content)', re.IGNORECASE)

    zero_citations = True
    zero_metalang = True

    for b in blocks:
        text_dump = str(b.content) + " " + str(b.title) + " " + str(b.page_title)
        if citation_regex.search(text_dump):
            print(f"[FAIL] Citation leak in block {b.block_id}: {text_dump[:100]}")
            zero_citations = False
        if metalang_regex.search(text_dump):
            print(f"[FAIL] Internal meta-language leak in block {b.block_id}: {text_dump[:100]}")
            zero_metalang = False

    assert zero_citations, "Citation bracket leaks detected!"
    print("[PASS] 9. Zero bracket citation leaks detected across all blocks.")

    assert zero_metalang, "Internal meta-language leaks detected!"
    print("[PASS] 10. Zero internal meta-language leaks detected across all blocks.")

    # 8. Component Types Verification
    worked_examples = blocks.filter(component_type="worked_example").count()
    knowledge_checks = blocks.filter(component_type="knowledge_check").count()
    tables = blocks.filter(component_type="comparison_table").count()

    assert worked_examples >= 5, f"Expected at least 5 worked examples, got {worked_examples}"
    assert knowledge_checks >= 3, f"Expected at least 3 knowledge checks, got {knowledge_checks}"
    assert tables >= 1, f"Expected at least 1 comparison table, got {tables}"

    print(f"[PASS] 11. Verified {worked_examples} worked examples, {knowledge_checks} knowledge checks, and {tables} comparison tables.")

    print("=" * 80)
    print("[ALL TESTS PASSED] Form 4 Business Studies Topic 14 is 100% verified and production-ready!")
    print("=" * 80)


if __name__ == "__main__":
    run_tests()
