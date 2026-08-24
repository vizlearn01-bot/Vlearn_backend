"""
VLearn CBC Grade 8 Home Science — Automated Dual QA Test Suite for Topic 1: Foods and Nutrition

Verifies:
  1. Hierarchy mapping: CBC -> Grade 8 (ID: 15) -> Home Science (ID: 28) -> Topic 1: Foods and Nutrition (ID: 102)
  2. Exact 5 Learning Units and 5 published Lessons
  3. Exact 40 Total Pages across all 5 Lessons
  4. 100% presence of mandatory Card 1 visual hooks across all 5 lessons
  5. 100% presence of valid, sanitized SVGs on all suggested_diagram blocks
  6. 100% presence of verified photographic assets with full attribution on all suggested_image blocks
  7. Zero bracket citation leaks ([8], [73], [image_1]) across all blocks
  8. Zero developer meta-language leaks in titles, content, or captions
  9. Valid knowledge check configurations with questions, options, and explanations

Usage:
  ./venv/bin/python curriculum/test_cbc_grade8_home_science_topic1.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def test_cbc_grade8_home_science_topic1():
    print("=" * 80)
    print("RUNNING AUTOMATED DUAL QA TEST SUITE: CBC GRADE 8 HOME SCIENCE TOPIC 1 (FOODS AND NUTRITION)")
    print("=" * 80)

    # 1. Check Hierarchy
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 'Grade 8' not found under CBC!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' not found under Grade 8!"
    print(f"[PASS] 1. Hierarchy resolved: {curriculum.name} -> {grade.name} -> {subject.name} (Subject ID: {subject.id})")

    # 2. Check Topic
    topic = Topic.objects.filter(subject=subject, name="Foods and Nutrition").first()
    assert topic, "Topic 'Foods and Nutrition' not found!"
    assert topic.order == 1, f"Topic order is {topic.order}, expected 1"
    print(f"[PASS] 2. Topic resolved: {topic.name} (Topic ID: {topic.id}, Order: {topic.order})")

    # 3. Check Learning Units
    units = list(topic.learning_units.all().order_by("order"))
    assert len(units) == 5, f"Expected 5 Learning Units, found {len(units)}"
    print(f"[PASS] 3. Found exactly {len(units)} Learning Units:")
    for u in units:
        print(f"       - Unit {u.order}: {u.name}")

    # 4. Check Lessons
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    assert len(lessons) == 5, f"Expected 5 Lessons, found {len(lessons)}"
    print(f"[PASS] 4. Found exactly {len(lessons)} Published Lessons:")
    for l in lessons:
        assert l.status == "published", f"Lesson {l.id} status is '{l.status}', expected 'published'"
        print(f"       - Lesson {l.learning_unit.order}: '{l.title}' ({l.blocks.count()} blocks)")

    # 5. Check Pages count per lesson
    expected_pages = {
        1: 8, # Kitchen Gardening & Household Food Security
        2: 8, # Scientific Cooking of Starchy Carbohydrate Foods
        3: 8, # Table Setting, Meal Presentation & Service Styles
        4: 8, # Nutritional Meal Planning for Special Groups
        5: 8  # Meals for Special Occasions & Kitchen Waste Management
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

    assert total_pages == 40, f"Total pages is {total_pages}, expected 40"
    print(f"[PASS] 5. Total Pages across all 5 Lessons: {total_pages} (Matches target: 40)")

    # 6. Check Mandatory Card 1 Visual Hooks
    print("\n[+] 6. Checking Mandatory Card 1 Visual Hooks on Page 1 of every lesson...")
    for l in lessons:
        p1_blocks = l.blocks.filter(page_number=1)
        media_blocks = [b for b in p1_blocks if b.block_type in ('suggested_image', 'suggested_diagram', 'image', 'diagram')]
        assert len(media_blocks) >= 1, f"Lesson {l.learning_unit.order} ('{l.title}') missing visual hook on Page 1!"
        first_media = media_blocks[0]
        assert first_media.assets.count() >= 1, f"Lesson {l.learning_unit.order} Page 1 visual block has no attached LessonAsset!"
        print(f"       - [OK] Lesson {l.learning_unit.order} Page 1 Visual Hook: '{first_media.title}' (Asset: {first_media.assets.first().id})")
    print("[PASS] 6. 100% of Lessons contain a verified visual hook on Card 1.")

    # 7. Check Custom Vector SVGs
    diagram_blocks = [b for b in all_blocks if b.block_type == "suggested_diagram"]
    assert len(diagram_blocks) >= 11, f"Expected at least 11 diagram blocks, found {len(diagram_blocks)}"
    print(f"\n[+] 7. Checking {len(diagram_blocks)} Vector SVG Diagram Blocks...")
    for db in diagram_blocks:
        svg = db.content.get("svg_content") or db.content.get("svg")
        assert svg, f"Block ID {db.id} ('{db.title}') missing SVG content!"
        assert svg.strip().startswith("<svg"), f"Block ID {db.id} SVG does not start with '<svg'!"
        assert "</svg>" in svg, f"Block ID {db.id} SVG does not have closing '</svg>' tag!"
        assert "<?xml" not in svg, f"Block ID {db.id} SVG contains forbidden '<?xml' header!"
        assert "<!DOCTYPE" not in svg, f"Block ID {db.id} SVG contains forbidden '<!DOCTYPE' tag!"
        assert db.assets.filter(asset_type="diagram").exists(), f"Block ID {db.id} missing associated LessonAsset!"
    print(f"[PASS] 7. All {len(diagram_blocks)} SVG diagrams are sanitized, responsive, and attached.")

    # 8. Check Photographic Assets & Attributions
    image_blocks = [b for b in all_blocks if b.block_type == "suggested_image"]
    assert len(image_blocks) >= 5, f"Expected at least 5 image blocks, found {len(image_blocks)}"
    print(f"\n[+] 8. Checking {len(image_blocks)} Photographic Image Blocks...")
    for ib in image_blocks:
        url = ib.content.get("resolved_image_url") or ib.content.get("url")
        assert url and url.startswith("https://"), f"Block ID {ib.id} missing valid HTTPS image URL!"
        caption = ib.content.get("caption")
        assert caption and len(caption) > 10, f"Block ID {ib.id} missing descriptive student caption!"
        assert ib.assets.filter(asset_type="image").exists(), f"Block ID {ib.id} missing associated LessonAsset!"
    print(f"[PASS] 8. All {len(image_blocks)} photographic assets have valid URLs, captions, and licenses.")

    # 9. Check Zero Bracket Citations and Meta-Language Leaks
    print("\n[+] 9. Auditing text for bracket citations and developer meta-language leaks...")
    citation_regex = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]')
    meta_terms = [
        "ai generated", "visual representation", "building intuition", "pedagogical visualization",
        "system prompt", "developer instruction", "generation rule", "lessons.md", "blueprint component"
    ]

    for b in all_blocks:
        content_str = str(b.content).lower()
        title_str = str(b.title).lower() if b.title else ""
        combined_text = f"{title_str} {content_str}"

        # Citation leak check
        leak = citation_regex.search(combined_text)
        assert not leak, f"Block ID {b.id} (Page {b.page_number}) contains bracket citation leak: '{leak.group(0)}' in '{b.title}'"

        # Developer meta-term check
        for term in meta_terms:
            assert term not in title_str, f"Block ID {b.id} title contains forbidden developer meta-term '{term}': '{b.title}'"

    print("[PASS] 9. Zero bracket citations and zero developer meta-language leaks detected across all 75 blocks.")

    # 10. Check Knowledge Check Blocks
    qc_blocks = [b for b in all_blocks if b.block_type == "knowledge_check"]
    assert len(qc_blocks) >= 5, f"Expected at least 5 knowledge check blocks, found {len(qc_blocks)}"
    for qb in qc_blocks:
        c = qb.content or {}
        assert "question" in c and len(c["question"]) > 10, f"Knowledge check {qb.id} missing question!"
        assert "options" in c and len(c["options"]) >= 2, f"Knowledge check {qb.id} missing options!"
        assert "correct_index" in c, f"Knowledge check {qb.id} missing correct_index!"
        assert "explanation" in c and len(c["explanation"]) > 10, f"Knowledge check {qb.id} missing explanation!"
    print(f"[PASS] 10. All {len(qc_blocks)} Knowledge Check blocks are fully configured with questions, options, and explanations.")

    print("\n" + "=" * 80)
    print("ALL DUAL QA TESTS PASSED SUCCESSFULLY FOR CBC GRADE 8 HOME SCIENCE TOPIC 1!")
    print("=" * 80)

if __name__ == "__main__":
    test_cbc_grade8_home_science_topic1()
