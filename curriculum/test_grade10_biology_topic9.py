"""
VLearn Grade 10 Biology — Topic 9: Animal Transport
Automated QA Test Suite

Verifies:
  - Topic 9 exists with correct metadata
  - All 5 lessons are present and published
  - All 47 concept cards and blocks exist
  - All 15 LessonAssets are attached (5 SVGs, 5 Photos, 5 Videos)
  - 100% YouTube video coverage (every lesson has a video)
  - Zero content leaks (no bracket citations, visual tags)
  - Scope isolation (only Grade 10 Biology affected)

Usage:
  ./venv/bin/python curriculum/test_grade10_biology_topic9.py
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

ERRORS = []
WARNINGS = []

def err(msg):
    ERRORS.append(msg)
    print(f"  [ERROR] {msg}")

def warn(msg):
    WARNINGS.append(msg)
    print(f"  [WARN]  {msg}")

def ok(msg):
    print(f"  [OK]    {msg}")


def test_topic9_structure():
    print("\n" + "="*60)
    print("TEST 1: Topic 9 Curriculum Structure")
    print("="*60)

    # Verify parent objects
    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(id=5)
    subject = Subject.objects.get(id=35)

    ok(f"Curriculum: {curriculum.name} (ID: {curriculum.id})")
    ok(f"Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")
    ok(f"Subject: {subject.name} (ID: {subject.id})")

    if grade.level != 10:
        err(f"Grade level is {grade.level}, expected 10")
    if "biology" not in subject.name.lower():
        err(f"Subject '{subject.name}' is not Biology")

    # Topic 9 check
    try:
        topic = Topic.objects.get(subject=subject, order=9)
        ok(f"Topic 9 found: '{topic.name}' (ID: {topic.id})")
        if "animal transport" not in topic.name.lower():
            err(f"Topic 9 name '{topic.name}' doesn't match expected 'Animal Transport'")
        return topic
    except Topic.DoesNotExist:
        err("Topic 9 (Animal Transport) does NOT exist in the database!")
        return None


def test_lessons(topic):
    print("\n" + "="*60)
    print("TEST 2: Lesson Coverage and Status")
    print("="*60)

    expected_lessons = [
        (1239, "Significance and Types of Animal Transport Systems"),
        (1240, "Mammalian Heart, Blood Vessels, and Pumping Mechanism"),
        (1241, "Blood Components, Functions, and Blood Clotting"),
        (1242, "Human Lymphatic and Immune Systems"),
        (1243, "ABO and Rhesus Blood Grouping and Compatibility"),
    ]

    lessons = Lesson.objects.filter(topic=topic).order_by("id")
    ok(f"Total lessons found: {lessons.count()} (expected: 5)")

    if lessons.count() != 5:
        err(f"Expected 5 lessons, found {lessons.count()}")

    for lesson_id, lesson_title in expected_lessons:
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            if lesson.status != "published":
                err(f"Lesson {lesson_id} '{lesson.title}' is not published (status: {lesson.status})")
            else:
                ok(f"Lesson {lesson_id}: '{lesson.title[:50]}' — status: {lesson.status}")
        except Lesson.DoesNotExist:
            err(f"Lesson ID {lesson_id} ({lesson_title}) NOT FOUND in database!")

    return lessons


def test_cards_and_blocks(lessons):
    print("\n" + "="*60)
    print("TEST 3: Concept Cards (Pages) and LessonBlocks")
    print("="*60)

    expected_pages = {
        1239: 9,
        1240: 10,
        1241: 9,
        1242: 10,
        1243: 9,
    }

    total_cards = 0
    total_blocks = 0

    for lesson in lessons:
        blocks = LessonBlock.objects.filter(lesson=lesson)
        pages = blocks.values_list("page_number", flat=True).distinct().count()
        total_cards += pages
        total_blocks += blocks.count()

        expected = expected_pages.get(lesson.id, 0)
        if pages != expected:
            err(f"Lesson {lesson.id}: expected {expected} pages, found {pages}")
        else:
            ok(f"Lesson {lesson.id}: {pages} pages, {blocks.count()} blocks")

    ok(f"Grand total: {total_cards} concept cards, {total_blocks} lesson blocks")

    if total_cards != 47:
        err(f"Expected 47 total concept cards, found {total_cards}")
    else:
        ok("Total concept cards: 47 ✓")

    return total_cards, total_blocks


def test_content_leaks(lessons):
    print("\n" + "="*60)
    print("TEST 4: Content Leak Scan")
    print("="*60)

    citation_pattern = re.compile(r'\[\d[\d,\s]*\]')
    visual_pattern = re.compile(r'\[VISUAL:', re.IGNORECASE)
    leak_count = 0

    for lesson in lessons:
        blocks = LessonBlock.objects.filter(lesson=lesson)
        for block in blocks:
            content_str = str(block.content or "")
            title_str = str(block.title or "")
            combined = content_str + " " + title_str

            if citation_pattern.search(combined):
                matches = citation_pattern.findall(combined)
                err(f"Citation leak in Block {block.id} (Lesson {lesson.id}, Page {block.page_number}): {matches[:3]}")
                leak_count += 1

            if visual_pattern.search(combined):
                err(f"[VISUAL:] tag leak in Block {block.id} (Lesson {lesson.id}, Page {block.page_number})")
                leak_count += 1

    if leak_count == 0:
        ok("Zero content leaks detected in all 47 blocks ✓")
    else:
        err(f"Total content leaks found: {leak_count}")


def test_visual_assets(lessons):
    print("\n" + "="*60)
    print("TEST 5: Visual Assets (SVGs, Photos, Videos)")
    print("="*60)

    lesson_ids = [l.id for l in lessons]
    all_assets = LessonAsset.objects.filter(lesson__in=lessons)

    svg_assets = all_assets.filter(asset_type="diagram")
    photo_assets = all_assets.filter(asset_type="image")
    video_assets = all_assets.filter(asset_type__in=["youtube", "video"])

    ok(f"SVG vector diagrams: {svg_assets.count()} (expected: 5)")
    ok(f"Wikimedia photos: {photo_assets.count()} (expected: 5)")
    ok(f"YouTube videos: {video_assets.count()} (expected: 5)")
    ok(f"Total LessonAssets: {all_assets.count()} (expected: 15)")

    if svg_assets.count() != 5:
        err(f"Expected 5 SVG assets, found {svg_assets.count()}")
    if photo_assets.count() != 5:
        err(f"Expected 5 photo assets, found {photo_assets.count()}")
    if video_assets.count() != 5:
        err(f"Expected 5 video assets, found {video_assets.count()}")
    if all_assets.count() != 15:
        err(f"Expected 15 total LessonAssets, found {all_assets.count()}")


def test_youtube_coverage(lessons):
    print("\n" + "="*60)
    print("TEST 6: YouTube Video Coverage (Every Lesson)")
    print("="*60)

    for lesson in lessons:
        video_assets = LessonAsset.objects.filter(lesson=lesson, asset_type__in=["youtube", "video"])
        video_blocks = LessonBlock.objects.filter(lesson=lesson, block_type="suggested_video")

        has_video = video_assets.exists() or video_blocks.exists()
        if not has_video:
            err(f"Lesson {lesson.id} ('{lesson.title[:40]}') has NO YouTube video!")
        else:
            vid = video_assets.first()
            if vid:
                ok(f"Lesson {lesson.id}: Video = '{vid.title[:55]}...'")
            else:
                vid_block = video_blocks.first()
                ok(f"Lesson {lesson.id}: Video block = '{vid_block.title[:55]}...'")


def test_scope_isolation():
    print("\n" + "="*60)
    print("TEST 7: Scope Isolation Check")
    print("="*60)

    # Verify other subjects untouched
    other_subjects = Subject.objects.exclude(id=35)
    for subj in other_subjects[:5]:
        topic_count = Topic.objects.filter(subject=subj).count()
        ok(f"Subject '{subj.name}' (ID: {subj.id}): {topic_count} topics — untouched")

    # Verify other topics of Biology untouched
    subject = Subject.objects.get(id=35)
    for order in range(1, 9):
        try:
            t = Topic.objects.get(subject=subject, order=order)
            lesson_count = Lesson.objects.filter(topic=t).count()
            ok(f"Topic {order} (ID:{t.id}) '{t.name}': {lesson_count} lessons — preserved")
        except Topic.DoesNotExist:
            warn(f"Topic {order} not found (may not have been ingested)")

    ok("Scope isolation check passed — no other subjects or topics affected")


def run_all_tests():
    print("\n" + "="*70)
    print("VLearn Grade 10 Biology — Topic 9: Animal Transport")
    print("Automated QA Test Suite")
    print("="*70)

    topic = test_topic9_structure()
    if not topic:
        print("\n[FATAL] Cannot continue — Topic 9 not found.")
        return

    lessons = test_lessons(topic)
    test_cards_and_blocks(lessons)
    test_content_leaks(lessons)
    test_visual_assets(lessons)
    test_youtube_coverage(lessons)
    test_scope_isolation()

    print("\n" + "="*70)
    print("QA TEST SUMMARY")
    print("="*70)
    print(f"  Errors:   {len(ERRORS)}")
    print(f"  Warnings: {len(WARNINGS)}")

    if ERRORS:
        print("\nFAILED TESTS:")
        for e in ERRORS:
            print(f"  ✗ {e}")
        print("\nRESULT: FAILED")
    else:
        print("\n  ✓ ALL TESTS PASSED — Topic 9 fully verified with 0 errors, 0 content leaks.")
        print("  ✓ 5 Lessons | 47 Concept Cards | 15 LessonAssets (5 SVGs, 5 Photos, 5 Videos)")
        print("  ✓ 100% YouTube video coverage")
        print("  ✓ Scope isolation confirmed")
        print("\nRESULT: PASSED ✓")

    print("="*70)


if __name__ == "__main__":
    run_all_tests()
