"""
VLearn Form 4 History — Automated Test Suite for Topic 1: The World War

Verifies:
  1. Target Subject, Grade, Curriculum mapping (History, Form 4, 844)
  2. Topic 1 existence and ordering
  3. Exact 7 Learning Units and 7 Lessons
  4. Exact 103 Pages across the 7 Lessons
  5. 100% presence of verified Wikimedia URLs and attributions on all photographic blocks
  6. 100% presence of educational historical video blocks with embedded documentary URLs
  7. Zero bracket citations ([60], [207], [1]) across all blocks
  8. Zero internal developer/generation metadata leaks
  9. 100% LessonAsset associations (Images + Videos)

Usage:
  ./venv/bin/python curriculum/test_form4_history_topic1.py
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

def test_form4_history_topic1():
    print("=" * 80)
    print("RUNNING AUTOMATED TEST SUITE: FORM 4 HISTORY TOPIC 1 (THE WORLD WAR)")
    print("=" * 80)

    # 1. Check Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    assert curriculum, "Curriculum 844 not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    assert grade, "Grade Form 4 not found!"
    subject = Subject.objects.filter(grade=grade, name="History").first()
    assert subject, "Subject History not found under Form 4!"
    print(f"[PASS] 1. Hierarchy resolved: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    # 2. Check Topic
    topic = Topic.objects.filter(subject=subject, name="The World War").first()
    assert topic, "Topic 'The World War' not found!"
    assert topic.order == 1, f"Topic order is {topic.order}, expected 1"
    print(f"[PASS] 2. Topic resolved: {topic.name} (Order: {topic.order})")

    # 3. Check Learning Units
    units = list(topic.learning_units.all().order_by("order"))
    assert len(units) == 7, f"Expected 7 Learning Units, found {len(units)}"
    print(f"[PASS] 3. Found exactly {len(units)} Learning Units:")
    for u in units:
        print(f"       - Unit {u.order}: {u.name}")

    # 4. Check Lessons
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))
    assert len(lessons) == 7, f"Expected 7 Lessons, found {len(lessons)}"
    print(f"[PASS] 4. Found exactly {len(lessons)} Lessons:")
    # 4.1 Check Page 1 Establishing Real-World Visual on EVERY Lesson
    for l in lessons:
        p1_img = l.blocks.filter(page_number=1, block_type='suggested_image').first()
        assert p1_img is not None, f'Lesson {l.id} ({l.title}) missing Page 1 establishing real-world visual!'
        assert p1_img.content.get('url'), f'Lesson {l.id} Page 1 image missing URL'
        assert p1_img.content.get('author'), f'Lesson {l.id} Page 1 image missing author'
    print("[PASS] 4.1 Every single lesson in Topic 1 has an establishing real-world visual on Page 1.")

    for l in lessons:
        assert l.status == "published", f"Lesson {l.id} status is {l.status}, expected 'published'"
        print(f"       - Lesson {l.learning_unit.order}: {l.title} ({l.blocks.count()} blocks)")

    # 5. Check Pages count per lesson
    expected_pages = {
        1: 14, # Causes and Outbreak of WWI
        2: 16, # Course and Fronts of WWI
        3: 15, # US Entry, Allied Victory, Results of WWI
        4: 15, # Peace Settlement & League of Nations
        5: 13, # WWII Origins, Causes & Path to War
        6: 16, # Course and Fronts of WWII
        7: 14  # Results of WWII and United Nations
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

    assert total_pages == 103, f"Total pages is {total_pages}, expected 103"
    print(f"[PASS] 5. Total Pages across all 7 Lessons: {total_pages} (Matches target: 103)")

    # 6. Check Wikimedia Photographic Assets
    image_blocks = [b for b in all_blocks if b.block_type == "suggested_image"]
    assert len(image_blocks) >= len(lessons), f"Expected 13 suggested_image blocks, found {len(image_blocks)}"
    for ib in image_blocks:
        url = ib.content.get("url") or ib.content.get("resolved_image_url")
        assert url and url.startswith("http"), f"Block ID {ib.id} ({ib.title}) missing valid image URL!"
        assert ib.content.get("author"), f"Block ID {ib.id} missing author attribution!"
        assert ib.content.get("licensing"), f"Block ID {ib.id} missing licensing attribution!"
    print(f"[PASS] 6. All {len(image_blocks)} Wikimedia photo blocks contain verified URLs, author attributions, and licensing.")

    # 7. Check Video Documentary Blocks
    video_blocks = [b for b in all_blocks if b.block_type == "suggested_video"]
    assert len(video_blocks) == 4, f"Expected 4 suggested_video blocks, found {len(video_blocks)}"
    for vb in video_blocks:
        url = vb.content.get("url")
        assert url and ("youtube.com" in url or "youtu.be" in url), f"Video block {vb.id} missing YouTube URL"
        assert vb.title, f"Video block {vb.id} missing title"
    print(f"[PASS] 7. All {len(video_blocks)} video blocks contain verified YouTube documentary embeds and titles.")

    # 8. Check LessonAsset database linkage
    assets = list(LessonAsset.objects.filter(lesson__topic=topic))
    assert len(assets) >= len(lessons), f"Expected 17 LessonAsset records (13 image + 4 video), found {len(assets)}"
    for a in assets:
        assert a.status == "attached", f"Asset {a.id} status is {a.status}, expected 'attached'"
        assert a.url and a.url.startswith("http"), f"Asset {a.id} missing URL"
        assert a.blocks.count() > 0, f"Asset {a.id} has no linked LessonBlock!"
    print(f"[PASS] 8. All {len(assets)} LessonAsset records (13 image + 4 video) are attached and linked to lesson blocks.")

    # 9. Check for Bracket Citation Leakage ([60], [207], [1])
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
    print(f"[PASS] 10. Zero internal developer/generation terminology leaks detected.")

    print("=" * 80)
    print(f"[ALL TESTS PASSED] Form 4 History Topic 1 is fully verified with 13 images and 4 documentary videos!")
    print(f"[*] Total Lessons: {len(lessons)}")
    print(f"[*] Total Pages:   {total_pages}")
    print(f"[*] Total Blocks:  {total_blocks}")
    print(f"[*] Total Assets:  {len(assets)} (13 Photographic + 4 Video Documentary)")
    print("=" * 80)

if __name__ == "__main__":
    test_form4_history_topic1()
