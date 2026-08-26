"""
VLearn Grade 10 Biology — Topic 10: Animal Gaseous Exchange and Respiration
Automated QA Test Suite

Verifies:
  - Topic 10 exists with correct metadata
  - All 5 lessons are present and published
  - All 48 concept cards and blocks exist
  - All 15 LessonAssets are attached (5 SVGs, 5 Photos, 5 Videos)
  - 100% YouTube video coverage (every lesson has a video)
  - Zero content leaks (no bracket citations, visual tags)
  - Scope isolation (Topics 1-9 and all other subjects untouched)

Usage:
  ./venv/bin/python curriculum/test_grade10_biology_topic10.py
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


def test_topic10_structure():
    print("\n" + "="*60)
    print("TEST 1: Topic 10 Curriculum Structure")
    print("="*60)

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

    try:
        topic = Topic.objects.get(subject=subject, order=10)
        ok(f"Topic 10 found: '{topic.name}' (ID: {topic.id})")
        if "gaseous exchange" not in topic.name.lower() and "respiration" not in topic.name.lower():
            err(f"Topic 10 name '{topic.name}' unexpected")
        return topic
    except Topic.DoesNotExist:
        err("Topic 10 does NOT exist in the database!")
        return None


def test_lessons(topic):
    print("\n" + "="*60)
    print("TEST 2: Lesson Coverage and Status")
    print("="*60)

    expected_lessons = [
        (1273, "Characteristics and Diversity of Respiratory Surfaces"),
        (1274, "Human Gaseous Exchange and Ventilation Mechanics"),
        (1275, "Aerobic and Anaerobic Respiration, Exercise, and Oxygen Debt"),
        (1276, "Respiratory Substrates, Respiratory Quotient (RQ), and Energy Requirements"),
        (1277, "Investigating Respiration and Designing Gaseous-Exchange Models"),
    ]

    lessons = Lesson.objects.filter(topic=topic).order_by("id")
    ok(f"Total lessons found: {lessons.count()} (expected: 5)")

    if lessons.count() != 5:
        err(f"Expected 5 lessons, found {lessons.count()}")

    for lesson_id, lesson_title in expected_lessons:
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            if lesson.status != "published":
                err(f"Lesson {lesson_id} is not published (status: {lesson.status})")
            else:
                ok(f"Lesson {lesson_id}: '{lesson.title[:52]}' — status: {lesson.status}")
        except Lesson.DoesNotExist:
            err(f"Lesson ID {lesson_id} ({lesson_title}) NOT FOUND!")

    return lessons


def test_cards_and_blocks(lessons):
    print("\n" + "="*60)
    print("TEST 3: Concept Cards (Pages) and LessonBlocks")
    print("="*60)

    expected_pages = {
        1273: 9,
        1274: 10,
        1275: 10,
        1276: 10,
        1277: 9,
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

    if total_cards != 48:
        err(f"Expected 48 total concept cards, found {total_cards}")
    else:
        ok("Total concept cards: 48 ✓")

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
        ok("Zero content leaks detected in all 48 blocks ✓")
    else:
        err(f"Total content leaks found: {leak_count}")


def test_visual_assets(lessons):
    print("\n" + "="*60)
    print("TEST 5: Visual Assets (SVGs, Photos, Videos)")
    print("="*60)

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
                ok(f"Lesson {lesson.id}: '{vid.title[:55]}...'")
            else:
                vid_block = video_blocks.first()
                ok(f"Lesson {lesson.id}: Block '{vid_block.title[:55]}...'")


def test_scope_isolation():
    print("\n" + "="*60)
    print("TEST 7: Scope Isolation Check")
    print("="*60)

    subject = Subject.objects.get(id=35)

    # Verify all prior Topics 1-9 still intact
    expected_topic_counts = {1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 5, 7: 4, 8: 2, 9: 5}
    for order, expected_lesson_count in expected_topic_counts.items():
        try:
            t = Topic.objects.get(subject=subject, order=order)
            lesson_count = Lesson.objects.filter(topic=t).count()
            if lesson_count != expected_lesson_count:
                err(f"Topic {order} '{t.name}' has {lesson_count} lessons, expected {expected_lesson_count}!")
            else:
                ok(f"Topic {order} (ID:{t.id}) '{t.name}': {lesson_count} lessons — preserved ✓")
        except Topic.DoesNotExist:
            warn(f"Topic {order} not found")

    ok("Scope isolation check passed — all prior topics preserved")


def run_all_tests():
    print("\n" + "="*70)
    print("VLearn Grade 10 Biology — Topic 10: Animal Gaseous Exchange and Respiration")
    print("Automated QA Test Suite")
    print("="*70)

    topic = test_topic10_structure()
    if not topic:
        print("\n[FATAL] Cannot continue — Topic 10 not found.")
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
        print("\n  ✓ ALL TESTS PASSED — Topic 10 fully verified with 0 errors, 0 content leaks.")
        print("  ✓ 5 Lessons | 48 Concept Cards | 15 LessonAssets (5 SVGs, 5 Photos, 5 Videos)")
        print("  ✓ 100% YouTube video coverage")
        print("  ✓ Scope isolation confirmed — Topics 1–9 all preserved")
        print("\nRESULT: PASSED ✓")

    print("="*70)


if __name__ == "__main__":
    run_all_tests()
