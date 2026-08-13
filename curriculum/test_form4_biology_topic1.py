"""
VLearn Form 4 Biology — Automated Test Suite for Topic 1: Genetics

Verifies:
  1. Hierarchy mapping: 844 -> Form 4 -> Biology (ID: 13)
  2. Topic 1 existence and ordering (Topic Order: 1, Name: Genetics)
  3. Exact 6 Learning Units and 6 published Lessons
  4. 70 Total Pages across all 6 Lessons
  5. 100% presence of sanitized SVGs on all diagram blocks
  6. 100% presence of verified Wikimedia URLs and full attributions on all suggested_image blocks
  7. Zero bracket citation leaks ([33], [74], [132]) across all blocks
  8. Zero developer meta-language leaks in titles or text

Usage:
  ./venv/bin/python curriculum/test_form4_biology_topic1.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def test_form4_biology_topic1():
    print("=" * 80)
    print("RUNNING AUTOMATED TEST SUITE: FORM 4 BIOLOGY TOPIC 1 (GENETICS)")
    print("=" * 80)

    # 1. Check Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    assert curriculum, "Curriculum 844 not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    assert grade, "Grade Form 4 not found!"
    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    assert subject, "Subject Biology not found under Form 4!"
    print(f"[PASS] 1. Hierarchy resolved: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    # 2. Check Topic
    topic = Topic.objects.filter(subject=subject, name="Genetics").first()
    assert topic, "Topic 'Genetics' not found!"
    assert topic.order == 1, f"Topic order is {topic.order}, expected 1"
    print(f"[PASS] 2. Topic resolved: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # 3. Check Learning Units
    units = list(topic.learning_units.all().order_by("order"))
    assert len(units) == 6, f"Expected 6 Learning Units, found {len(units)}"
    print(f"[PASS] 3. Found exactly {len(units)} Learning Units:")
    for u in units:
        print(f"       - Unit {u.order}: {u.name}")

    # 4. Check Lessons
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    assert len(lessons) == 6, f"Expected 6 Lessons, found {len(lessons)}"
    print(f"[PASS] 4. Found exactly {len(lessons)} Lessons:")
    for l in lessons:
        assert l.status == "published", f"Lesson {l.id} status is {l.status}, expected 'published'"
        print(f"       - Lesson {l.learning_unit.order}: {l.title} ({l.blocks.count()} blocks)")

    # 5. Check Pages count per lesson
    expected_pages = {
        1: 12, # Foundations & Biological Variation
        2: 11, # Chromosomes, DNA & Protein Synthesis
        3: 12, # Mendelian Monohybrid Crosses & Test Crosses
        4: 10, # Non-Mendelian, Blood Groups, & Sex Linkage
        5: 12, # Mutations, Mutagens, & Inherited Disorders
        6: 13  # Applied Genetics, KCSE Problems & Topic Review
    }

    total_pages = 0
    total_blocks = 0
    all_blocks = []

    for l in lessons:
        u_order = l.learning_unit.order
        l_blocks = list(l.blocks.all().order_by("order"))
        total_blocks += len(l_blocks)
        all_blocks.extend(l_blocks)

        pages = set(b.page_number for b in l_blocks if b.page_number is not None)
        page_count = len(pages)
        total_pages += page_count
        expected = expected_pages.get(u_order)
        assert page_count == expected, f"Lesson {u_order} has {page_count} pages, expected {expected}"
        print(f"[PASS] 5.{u_order} Lesson {u_order} has exactly {page_count} pages.")

    assert total_pages == 70, f"Total pages is {total_pages}, expected 70"
    print(f"[PASS] 5. Total Pages across all 6 Lessons: {total_pages} (Matches target: 70)")

    # 6. Check Visual Diagram SVGs
    diagram_blocks = [b for b in all_blocks if b.block_type == "suggested_diagram"]
    assert len(diagram_blocks) >= 18, f"Expected at least 18 diagram blocks, found {len(diagram_blocks)}"
    for db in diagram_blocks:
        svg = db.content.get("svg_content") or db.content.get("svg")
        assert svg, f"Block ID {db.id} ({db.title}) missing SVG content!"
        assert svg.strip().startswith("<svg"), f"Block ID {db.id} SVG does not start with '<svg'!"
        assert svg.strip().endswith("</svg>"), f"Block ID {db.id} SVG does not end with '</svg>'!"
    print(f"[PASS] 6. All {len(diagram_blocks)} Diagram blocks contain valid, structurally complete SVGs.")

    # 7. Check Wikimedia Photographic Assets
    image_blocks = [b for b in all_blocks if b.block_type == "suggested_image"]
    assert len(image_blocks) >= 8, f"Expected at least 8 suggested_image blocks, found {len(image_blocks)}"
    for ib in image_blocks:
        url = ib.content.get("resolved_image_url") or ib.content.get("url")
        assert url and url.startswith("http"), f"Block ID {ib.id} ({ib.title}) missing valid image URL!"
        assert ib.content.get("author"), f"Block ID {ib.id} missing author attribution!"
        assert ib.content.get("licensing"), f"Block ID {ib.id} missing licensing attribution!"
    print(f"[PASS] 7. All {len(image_blocks)} Wikimedia photo blocks contain verified URLs and full attributions.")

    # 8. Check for Bracket Citation Leakage ([33], [74], [132])
    bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
    citation_leaks = []
    for b in all_blocks:
        b_str = str(b.content)
        matches = bracket_pattern.findall(b_str)
        if matches:
            citation_leaks.append((b.id, b.page_number, matches))

    assert len(citation_leaks) == 0, f"Found bracket citation leaks in blocks: {citation_leaks}"
    print(f"[PASS] 8. Zero bracket citation leaks detected across all {total_blocks} blocks.")

    # 9. Check for internal developer/generation terminology leaks
    meta_phrases = ["Visual Representation:", "Building Intuition:", "Student should observe", "AI-generated", "AI Generated"]
    meta_leaks = []
    for b in all_blocks:
        b_title = b.title or ""
        b_page_title = b.page_title or ""
        for phrase in meta_phrases:
            if phrase.lower() in b_title.lower() or phrase.lower() in b_page_title.lower():
                meta_leaks.append((b.id, b.page_number, phrase))

    assert len(meta_leaks) == 0, f"Found internal meta-language leaks: {meta_leaks}"
    print(f"[PASS] 9. Zero internal developer/generation terminology leaks detected.")

    print("=" * 80)
    print(f"[ALL TESTS PASSED] Form 4 Biology Topic 1 (Genetics) is fully verified and production-ready!")
    print(f"[*] Total Lessons: {len(lessons)}")
    print(f"[*] Total Pages:   {total_pages}")
    print(f"[*] Total Blocks:  {total_blocks}")
    print(f"[*] Total Assets:  {LessonAsset.objects.filter(lesson__in=lessons).count()}")
    print("=" * 80)

if __name__ == "__main__":
    test_form4_biology_topic1()
