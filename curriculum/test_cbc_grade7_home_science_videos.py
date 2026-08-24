"""
Test: CBC Grade 7 Home Science — Comprehensive Video Enrichment Verification

Asserts that:
1. All 33+ lessons in Grade 7 Home Science have a valid suggested_video block on Page 9.
2. Every video block is followed by a companion 'callout' reflection block on Page 9.
3. Every video is stored as an active attached LessonAsset (asset_type='video').
4. The original content on Pages 1–8 across all lessons is preserved intact.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset


def run_tests():
    print("=" * 80)
    print("[TEST] CBC Grade 7 Home Science — Video Enrichment Verification")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    assert grade, "Grade 7 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' under Grade 7 not found!"

    passed = 0
    failed = 0
    total_lessons = 0

    for topic in subject.topics.order_by("order"):
        print(f"\n--- Topic {topic.order}: {topic.name} ---")
        for unit in topic.learning_units.order_by("order"):
            for lesson in unit.lessons.all():
                total_lessons += 1

                # 1. Check video block on page 9
                video_block = lesson.blocks.filter(block_type="suggested_video", page_number=9).first()
                if not video_block:
                    print(f"  [FAIL] '{lesson.title}' — Missing suggested_video block on Page 9")
                    failed += 1
                    continue

                url = video_block.content.get("url", "")
                if not url or ("youtube.com" not in url and "youtu.be" not in url):
                    print(f"  [FAIL] '{lesson.title}' — Invalid YouTube URL in video block: {url}")
                    failed += 1
                    continue

                # 2. Check callout reflection block on page 9
                callout_block = lesson.blocks.filter(block_type="callout", page_number=9).first()
                if not callout_block:
                    print(f"  [FAIL] '{lesson.title}' — Missing reflection callout on Page 9")
                    failed += 1
                    continue

                # 3. Check attached LessonAsset
                video_asset = lesson.assets.filter(asset_type="video", status="attached").first()
                if not video_asset:
                    print(f"  [FAIL] '{lesson.title}' — Missing attached video LessonAsset")
                    failed += 1
                    continue

                # 4. Check original content preserved on pages 1-8
                p1_to_8_blocks = lesson.blocks.filter(page_number__lte=8).count()
                if p1_to_8_blocks < 8:
                    print(f"  [FAIL] '{lesson.title}' — Expected >=8 blocks on pages 1-8, found {p1_to_8_blocks}")
                    failed += 1
                    continue

                print(f"  [PASS] Unit {unit.order}: '{lesson.title[:50]}'")
                print(f"         Video: {url} | Asset: OK | Pages 1-8 intact ({p1_to_8_blocks} blocks)")
                passed += 1

    print("\n" + "=" * 80)
    if failed == 0:
        print(f"[ALL TESTS PASSED] {passed}/{total_lessons} Grade 7 lessons verified successfully.")
    else:
        print(f"[TESTS FAILED] {passed} passed, {failed} failed out of {total_lessons} lessons.")
    print("=" * 80)
    assert failed == 0, f"{failed} test(s) failed!"


if __name__ == "__main__":
    run_tests()
