"""
Test: CBC Grade 6 Home Science — YouTube Video Enrichment Verification
Asserts that all 8 video blocks are correctly attached to the right lessons,
that each video is followed by a reflection callout on the same page,
and that every LessonAsset record is correctly stored.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset

EXPECTED_VIDEOS = [
    {"topic_order": 1, "lesson_contains": "Grooming",    "url_fragment": "y4gburcET5I"},
    {"topic_order": 1, "lesson_contains": "Exercise",    "url_fragment": "vSnRdmR6xcE"},
    {"topic_order": 2, "lesson_contains": "Needs, Wants","url_fragment": "NkY3KuahkqY"},
    {"topic_order": 3, "lesson_contains": "Minerals",    "url_fragment": "uZousR_FfEE"},
    {"topic_order": 3, "lesson_contains": "Preservation","url_fragment": "rBJ3njZwaik"},
    {"topic_order": 3, "lesson_contains": "Cookery",     "url_fragment": "UYsAW2FeGDg"},
    {"topic_order": 4, "lesson_contains": "Weaving",     "url_fragment": "AWLIy-Um7_0"},
    {"topic_order": 4, "lesson_contains": "Knitting",    "url_fragment": "WRhJeCnTmEo"},
]

def run_tests():
    print("=" * 80)
    print("[TEST] CBC Grade 6 Home Science — Video Enrichment Verification")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade      = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    subject    = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert curriculum and grade and subject, "Hierarchy broken!"

    passed = 0
    failed = 0

    for ev in EXPECTED_VIDEOS:
        topic = Topic.objects.filter(subject=subject, order=ev["topic_order"]).first()
        assert topic, f"Topic {ev['topic_order']} not found!"

        lesson = None
        for unit in topic.learning_units.all():
            candidate = unit.lessons.filter(title__icontains=ev["lesson_contains"]).first()
            if candidate:
                lesson = candidate
                break

        if not lesson:
            print(f"  [FAIL] Topic {ev['topic_order']} — Lesson '{ev['lesson_contains']}' not found")
            failed += 1
            continue

        # 1. Check suggested_video block with correct URL
        video_blocks = lesson.blocks.filter(block_type="suggested_video")
        url_match = [b for b in video_blocks if ev["url_fragment"] in str(b.content)]
        if not url_match:
            print(f"  [FAIL] '{lesson.title}' — No suggested_video block with URL fragment '{ev['url_fragment']}'")
            failed += 1
            continue
        vb = url_match[0]

        # 2. Check companion callout block on the same page
        callout_on_page = lesson.blocks.filter(block_type="callout", page_number=vb.page_number)
        if not callout_on_page.exists():
            print(f"  [FAIL] '{lesson.title}' — No callout reflection block on page {vb.page_number}")
            failed += 1
            continue

        # 3. Check LessonAsset exists
        asset = LessonAsset.objects.filter(lesson=lesson, url__icontains=ev["url_fragment"]).first()
        if not asset:
            print(f"  [FAIL] '{lesson.title}' — LessonAsset not found for URL '{ev['url_fragment']}'")
            failed += 1
            continue

        assert asset.asset_type == "video", f"Asset type should be 'video', got '{asset.asset_type}'"
        assert asset.status == "attached", f"Asset status should be 'attached', got '{asset.status}'"

        # 4. Confirm existing lesson pages are unmodified (pages 1-8 still exist)
        original_pages = lesson.blocks.filter(page_number__lte=8).count()
        assert original_pages >= 8, (
            f"'{lesson.title}' — Expected ≥8 blocks on pages 1–8, found {original_pages}. "
            "Original content may have been modified!"
        )

        print(f"  [PASS] Topic {ev['topic_order']}: '{lesson.title}'")
        print(f"         → Video on page {vb.page_number}: {ev['url_fragment']}")
        print(f"         → Reflection callout: ✓  |  LessonAsset: ✓  |  Original pages 1-8: ✓")
        passed += 1

    print("\n" + "=" * 80)
    if failed == 0:
        print(f"[ALL TESTS PASSED] {passed}/{passed + failed} videos verified successfully.")
    else:
        print(f"[PARTIAL] {passed} passed, {failed} FAILED.")
    print("=" * 80)
    assert failed == 0, f"{failed} test(s) failed!"

if __name__ == "__main__":
    run_tests()
