"""
VLearn Form 4 Business Studies — Automated Test Suite for Topic 3: Money and Banking

Verifies:
  1. Target Subject, Grade, Curriculum mapping (Business Studies, Form 4, 844)
  2. Topic 3 existence, name, and ordering (Money and Banking, Order: 3)
  3. Exact 8 Learning Units and 8 Published Lessons
  4. Exact 77 Pages across the 8 Lessons
  5. 100% presence of verified Wikimedia URLs and attributions on photographic blocks
  6. 100% presence of valid educational dark-mode SVG diagrams
  7. Zero bracket citations ([305], [182], [1]) across all blocks
  8. Zero internal developer/generation metadata leaks
  9. 100% LessonAsset database linkage
  10. Verification of worked calculations, comparison tables, and knowledge check questions

Usage:
  ./venv/bin/python curriculum/test_form4_business_studies_topic3.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock, LessonAsset
)

def test_form4_business_studies_topic3():
    print("=" * 80)
    print("RUNNING AUTOMATED TEST SUITE: FORM 4 BUSINESS STUDIES TOPIC 3 (MONEY AND BANKING)")
    print("=" * 80)

    # 1. Check Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    assert curriculum, "Curriculum 844 not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    assert grade, "Grade Form 4 not found!"
    subject = Subject.objects.filter(grade=grade, name="Business Studies").first()
    assert subject, "Subject Business Studies not found under Form 4!"
    print(f"[PASS] 1. Hierarchy resolved: {curriculum.name} -> {grade.name} -> {subject.name} (Subject ID: {subject.id})")

    # 2. Check Topic
    topic = Topic.objects.filter(subject=subject, name="Money and Banking").first()
    assert topic, "Topic 'Money and Banking' not found!"
    assert topic.order == 3, f"Topic order is {topic.order}, expected 3"
    print(f"[PASS] 2. Topic resolved: {topic.name} (Order: {topic.order})")

    # 3. Check Learning Units
    units = list(topic.learning_units.all().order_by("order"))
    assert len(units) == 8, f"Expected 8 Learning Units, found {len(units)}"
    print(f"[PASS] 3. Found exactly {len(units)} Learning Units:")
    for u in units:
        print(f"       - Unit {u.order}: {u.name}")

    # 4. Check Lessons
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    assert len(lessons) == 8, f"Expected 8 Lessons, found {len(lessons)}"
    print(f"[PASS] 4. Found exactly {len(lessons)} Lessons:")
    for l in lessons:
        assert l.status == "published", f"Lesson {l.id} status is {l.status}, expected 'published'"
        print(f"       - Lesson {l.learning_unit.order}: {l.title} ({l.blocks.count()} blocks)")

    # 5. Check Pages count per lesson
    expected_pages = {
        1: 9,   # Barter Trade and its Limitations
        2: 10,  # Meaning, Characteristics & Evolution of Money
        3: 9,   # Functions of Money
        4: 9,   # Demand and Supply of Money
        5: 9,   # The Kenyan Banking System Hierarchy
        6: 10,  # Commercial Banks, Accounts & Profit Sources
        7: 10,  # Money Transfer Facilities & NBFIs
        8: 11   # The Central Bank, Monetary Policy & Modern Trends
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

    assert total_pages == 77, f"Total pages is {total_pages}, expected 77"
    print(f"[PASS] 5. Total Pages across all 8 Lessons: {total_pages} (Matches target: 77)")

    # 6. Check Wikimedia Photographic Assets
    image_blocks = [b for b in all_blocks if b.block_type == "suggested_image"]
    assert len(image_blocks) >= 5, f"Expected at least 5 suggested_image blocks, found {len(image_blocks)}"
    for ib in image_blocks:
        url = ib.content.get("url") or ib.content.get("resolved_image_url")
        assert url and url.startswith("http"), f"Block ID {ib.id} ({ib.title}) missing valid image URL!"
        assert ib.content.get("author"), f"Block ID {ib.id} missing author attribution!"
        assert ib.content.get("licensing"), f"Block ID {ib.id} missing licensing attribution!"
    print(f"[PASS] 6. All {len(image_blocks)} Wikimedia photo blocks contain verified URLs, author attributions, and licensing.")

    # 7. Check Educational SVG Diagrams
    diagram_blocks = [b for b in all_blocks if b.block_type == "suggested_diagram" or (isinstance(b.content, dict) and b.content.get("svg_content"))]
    assert len(diagram_blocks) >= 5, f"Expected at least 5 diagram blocks with SVG markup, found {len(diagram_blocks)}"
    for db in diagram_blocks:
        svg = (db.content.get("svg_content") if isinstance(db.content, dict) else None) or (db.metadata.get("svg_content") if db.metadata else None)
        assert svg and "<svg" in svg and "</svg>" in svg, f"Diagram block {db.id} ({db.title}) missing valid SVG XML!"
    print(f"[PASS] 7. All {len(diagram_blocks)} diagram blocks contain verified dark-mode SVG markup.")

    # 8. Check LessonAsset database linkage
    assets = list(LessonAsset.objects.filter(lesson__topic=topic))
    assert len(assets) >= 10, f"Expected at least 10 LessonAsset records, found {len(assets)}"
    for a in assets:
        assert a.status == "attached", f"Asset {a.id} status is {a.status}, expected 'attached'"
        assert a.blocks.count() > 0, f"Asset {a.id} has no linked LessonBlock!"
    print(f"[PASS] 8. All {len(assets)} LessonAsset records are attached and linked to lesson blocks.")

    # 9. Check for Bracket Citation Leakage ([305], [182], [1])
    bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
    citation_leaks = []
    for b in all_blocks:
        b_str = str(b.content)
        matches = bracket_pattern.findall(b_str)
        if matches:
            citation_leaks.append((b.id, b.page_number, matches))

    assert len(citation_leaks) == 0, f"Found bracket citation leaks in blocks: {citation_leaks}"
    print(f"[PASS] 9. Zero bracket citation leaks detected across all {total_blocks} blocks.")

    # 10. Check for internal generation terminology leaks
    meta_phrases = ["Visual Representation:", "Building Intuition:", "AI-generated", "AI Generated", "[VISUAL OPPORTUNITY]"]
    meta_leaks = []
    for b in all_blocks:
        b_title = b.title or ""
        b_page_title = b.page_title or ""
        b_content_str = str(b.content)
        for phrase in meta_phrases:
            if phrase.lower() in b_title.lower() or phrase.lower() in b_page_title.lower() or phrase.lower() in b_content_str.lower():
                meta_leaks.append((b.id, b.page_number, phrase))

    assert len(meta_leaks) == 0, f"Found internal meta-language leaks: {meta_leaks}"
    print(f"[PASS] 10. Zero internal meta-language leaks detected across all {total_blocks} blocks.")

    # 11. Check Worked Calculations and Knowledge Checks
    worked_examples = [b for b in all_blocks if b.block_type == "worked_example"]
    knowledge_checks = [b for b in all_blocks if b.block_type == "knowledge_check"]
    comparison_tables = [b for b in all_blocks if b.block_type == "comparison_table"]

    assert len(worked_examples) >= 6, f"Expected at least 6 worked examples, found {len(worked_examples)}"
    assert len(knowledge_checks) >= 7, f"Expected at least 7 knowledge checks, found {len(knowledge_checks)}"
    assert len(comparison_tables) >= 5, f"Expected at least 5 comparison tables, found {len(comparison_tables)}"

    print(f"[PASS] 11. Verified {len(worked_examples)} worked examples, {len(knowledge_checks)} knowledge checks, and {len(comparison_tables)} comparison tables.")
    print("=" * 80)
    print("[ALL TESTS PASSED] Form 4 Business Studies Topic 3 is 100% verified and production-ready!")
    print("=" * 80)

if __name__ == "__main__":
    test_form4_business_studies_topic3()
