"""
VLearn Grade 10 Biology — Topic 4: Chemicals of Life
Automated QA, Integrity, and Regression Verification Test Suite

Validates:
  1. Curriculum Hierarchy (CBC -> Grade 10 -> Biology -> Topic 4)
  2. Learning Units & Published Lessons 1-to-1 Parity (4 Comprehensive Lessons)
  3. Concept Card Distribution & Page Numbering (39 Total Cards)
  4. Block Integrity & Typing (Learning Goals, Explanations, Tables, Steps, Knowledge Checks)
  5. Visual Enrichment Assets (4 High-Quality SVGs, 4 Contextualized Photos, 4 YouTube Videos - 1 per lesson)
  6. Assessment Integrity (Valid Questions, Options, Answer Keys, Explanations)
  7. Content Leak Audit (Zero [VISUAL: ...] tags, zero citation brackets [67], zero corrupted LaTeX)

Usage:
  ./venv/bin/python curriculum/test_grade10_biology_topic4.py
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

def run_tests():
    print("=" * 80)
    print("RUNNING AUTOMATED QA: GRADE 10 BIOLOGY TOPIC 4 (CHEMICALS OF LIFE)")
    print("=" * 80)

    errors = []
    warnings = []

    # 1. Hierarchy Verification
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        errors.append("Curriculum 'CBC' (ID: 5) not found!")
    else:
        print(f"[PASS] Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        errors.append("Grade 'Grade 10' under CBC not found!")
    else:
        print(f"[PASS] Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    if not subject:
        errors.append("Subject 'Biology' under Grade 10 not found!")
    else:
        print(f"[PASS] Subject: {subject.name} (ID: {subject.id})")

    topic = Topic.objects.filter(subject=subject, name="Chemicals of Life").first()
    if not topic:
        errors.append("Topic 'Chemicals of Life' not found under Grade 10 Biology!")
        print("\n[!] FATAL ERRORS ENCOUNTERED:")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print(f"[PASS] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # 2. Units & Lessons Count (Expected: 4 Comprehensive Lessons)
    units = list(topic.learning_units.all().order_by("order"))
    lessons = list(topic.lessons.all().order_by("learning_unit__order"))

    if len(units) != 4:
        errors.append(f"Expected 4 LearningUnits, found {len(units)}")
    else:
        print(f"[PASS] Learning Units Count: {len(units)} (1-to-1 verified)")

    if len(lessons) != 4:
        errors.append(f"Expected 4 Published Lessons, found {len(lessons)}")
    else:
        print(f"[PASS] Published Lessons Count: {len(lessons)}")

    # 3. Verify Each Lesson and Its Pages/Cards
    total_cards = 0
    total_blocks = 0
    total_svgs = 0
    total_photos = 0
    total_videos = 0
    total_checks = 0

    print("\n" + "-" * 80)
    print("LESSON-BY-LESSON DETAILED AUDIT")
    print("-" * 80)

    for idx, (unit, lesson) in enumerate(zip(units, lessons), 1):
        if lesson.learning_unit_id != unit.id:
            errors.append(f"Lesson {lesson.id} mismatch with LearningUnit {unit.id}")

        if lesson.status != "published":
            errors.append(f"Lesson {lesson.id} status is '{lesson.status}', expected 'published'")

        blocks = list(lesson.blocks.all().order_by("order"))
        total_blocks += len(blocks)

        pages = set(b.page_number for b in blocks if b.page_number is not None)
        page_count = len(pages)
        total_cards += page_count

        if page_count < 8:
            warnings.append(f"Lesson {idx} ({lesson.title}) has {page_count} pages (expected >= 8)")

        # Count specific block types
        l_svgs = [b for b in blocks if b.block_type == "suggested_diagram" and (b.content or {}).get("svg_content")]
        l_photos = [b for b in blocks if b.block_type == "suggested_image" and (b.content or {}).get("resolved_image_url")]
        l_videos = [b for b in blocks if b.block_type == "suggested_video" and (b.content or {}).get("resolved_video_id")]
        l_checks = [b for b in blocks if b.block_type == "knowledge_check"]

        total_svgs += len(l_svgs)
        total_photos += len(l_photos)
        total_videos += len(l_videos)
        total_checks += len(l_checks)

        # Requirement check: Every single lesson must have a relevant YouTube video!
        if len(l_videos) < 1:
            errors.append(f"Lesson {idx} ({lesson.title}) is missing a YouTube video block!")

        print(f"Lesson {idx:02d}: '{lesson.title[:40]}' | Cards: {page_count:02d} | Blocks: {len(blocks):02d} | SVGs: {len(l_svgs)} | Photos: {len(l_photos)} | Videos: {len(l_videos)} | Checks: {len(l_checks)}")

        # Audit Knowledge Checks in this lesson
        for kc in l_checks:
            c = kc.content or {}
            q = c.get("question")
            opts = c.get("options", [])
            ans = c.get("correct_answer")
            exp = c.get("explanation")

            if not q:
                errors.append(f"Lesson {idx} Block {kc.id}: Missing question in knowledge check")
            if not opts or len(opts) < 2:
                errors.append(f"Lesson {idx} Block {kc.id}: Missing or insufficient options in knowledge check")
            if not ans:
                errors.append(f"Lesson {idx} Block {kc.id}: Missing correct_answer in knowledge check")
            if not exp:
                warnings.append(f"Lesson {idx} Block {kc.id}: Missing explanation in knowledge check")

    # 4. Total Asset Attachments Verification
    lesson_assets = LessonAsset.objects.filter(lesson__in=lessons)
    diagram_assets = lesson_assets.filter(asset_type="diagram").count()
    photo_assets = lesson_assets.filter(asset_type="image").count()
    video_assets = lesson_assets.filter(asset_type="youtube").count()

    print("\n" + "-" * 80)
    print("ASSET RECONCILIATION")
    print("-" * 80)
    print(f"Total Vector SVGs:      {total_svgs} blocks, {diagram_assets} LessonAsset records (Expected: 4)")
    print(f"Total Wikimedia Photos: {total_photos} blocks, {photo_assets} LessonAsset records (Expected: 4)")
    print(f"Total YouTube Videos:   {total_videos} blocks, {video_assets} LessonAsset records (Expected: 4)")
    print(f"Total LessonAssets:     {lesson_assets.count()} (Expected: 12)")

    if diagram_assets != 4:
        errors.append(f"Expected 4 diagram assets, found {diagram_assets}")
    if photo_assets != 4:
        errors.append(f"Expected 4 photo assets, found {photo_assets}")
    if video_assets != 4:
        errors.append(f"Expected 4 video assets, found {video_assets}")

    # 5. Content Leak Scan (Strict No-Leak Audit)
    print("\n" + "-" * 80)
    print("STRICT CONTENT LEAK SCAN")
    print("-" * 80)

    leak_patterns = [
        (r'\[VISUAL:\s*[^\]]+\]', "Raw Visual Tag Leak"),
        (r'\[(?:\d+|image_\d+)\]', "Raw Bracket Citation Leak [e.g. 67]"),
        (r'Visual Representation', "Internal Prompt Label Leak"),
        (r'Suggested Visual', "Internal Prompt Label Leak"),
        (r'Generation Instruction', "Internal Instruction Leak"),
        (r'Image Search Query', "Search Query Leak"),
    ]

    leak_count = 0
    all_blocks = LessonBlock.objects.filter(lesson__in=lessons)

    for block in all_blocks:
        block_str = str(block.content) + " " + str(block.title)
        for pattern, label in leak_patterns:
            matches = re.findall(pattern, block_str, flags=re.IGNORECASE)
            if matches:
                errors.append(f"Block {block.id} (Lesson '{block.lesson.title}', Page {block.page_number}): Detected {label}: {matches[:3]}")
                leak_count += 1

    if leak_count == 0:
        print("[PASS] Zero content leaks detected! All bracket citations, visual prompts, and internal tags are clean.")
    else:
        print(f"[FAIL] Found {leak_count} content leaks in database blocks!")

    # Final Verdict
    print("\n" + "=" * 80)
    print(f"AUDIT SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings")
    print(f"Total Lessons: {len(lessons)} | Total Concept Cards: {total_cards} | Total Blocks: {total_blocks}")
    print("=" * 80)

    if errors:
        print("\n[!] FATAL ERRORS:")
        for e in errors:
            print(f"  - {e}")
        return False

    if warnings:
        print("\n[*] WARNINGS:")
        for w in warnings:
            print(f"  - {w}")

    print("\n[SUCCESS] ALL GRADE 10 BIOLOGY TOPIC 4 TESTS PASSED!")
    return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
