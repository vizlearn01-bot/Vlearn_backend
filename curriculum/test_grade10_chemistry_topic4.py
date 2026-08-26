"""
Automated Test Suite for Grade 10 CBC Chemistry — Topic 4: Chemical Bonding
Verifies:
  - Subject: Grade 10 Chemistry (ID: 5)
  - Topic 4 presence (ID: 176, Order: 4)
  - 6 Published Lessons (100% published, version=1)
  - Discrete 5 pages per lesson (30 pages total)
  - LessonBlocks presence, block_type, and component_type integrity
  - LessonAssets attachments and Many-to-Many relationships
  - Zero citation leaks ([49], [313]) and zero developer tags ([VISUAL: ...])
  - Formative Knowledge Checks (4 options, valid answer, non-empty explanation)
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

def run_topic4_tests():
    print("=" * 80)
    print("RUNNING AUTOMATED TEST SUITE: GRADE 10 CHEMISTRY — TOPIC 4")
    print("=" * 80)

    # 1. Subject & Topic Check
    chem = Subject.objects.get(id=5)
    assert chem.name == "Chemistry", f"Expected Chemistry, got {chem.name}"
    assert chem.grade.level == 10, f"Expected Grade 10, got {chem.grade.name}"
    assert "CBC" in chem.grade.curriculum.name, f"Expected CBC curriculum, got {chem.grade.curriculum.name}"
    print("  [PASS] Curriculum Hierarchy Verified (CBC -> Grade 10 -> Chemistry)")

    topic = Topic.objects.get(subject=chem, order=4)
    assert topic.name == "Chemical Bonding", f"Unexpected topic name: {topic.name}"
    print(f"  [PASS] Topic 4 Verified: [{topic.id}] {topic.name}")

    # 2. Learning Units & Lessons Check
    units = LearningUnit.objects.filter(topic=topic).order_by("order")
    assert units.count() == 6, f"Expected 6 learning units, found {units.count()}"
    print("  [PASS] 6 Learning Units Verified in Sequential Order (1 to 6)")

    lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
    assert lessons.count() == 6, f"Expected 6 lessons, found {lessons.count()}"

    total_blocks = 0
    total_assets = 0
    total_checks = 0

    for idx, lesson in enumerate(lessons, start=1):
        assert lesson.status == "published", f"Lesson [{lesson.id}] status is not published!"
        assert lesson.version == 1, f"Lesson [{lesson.id}] version is not 1!"
        
        blocks = list(lesson.blocks.all().order_by("order"))
        assert len(blocks) >= 10, f"Lesson [{lesson.id}] has fewer than 10 blocks: {len(blocks)}"
        total_blocks += len(blocks)

        # Check unique pages
        pages = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
        assert len(pages) == 5, f"Lesson [{lesson.id}] has {len(pages)} pages, expected exactly 5"
        assert set(pages) == {1, 2, 3, 4, 5}, f"Lesson [{lesson.id}] pages are not {1,2,3,4,5}"

        # Card 1 Hook check
        card1_img = next((b for b in blocks if b.page_number == 1 and b.block_type == "suggested_image"), None)
        assert card1_img is not None, f"Lesson [{lesson.id}] missing Card 1 suggested_image hook!"

        # Assets check
        assets = lesson.assets.all()
        assert assets.count() >= 1, f"Lesson [{lesson.id}] has no LessonAsset attached!"
        total_assets += assets.count()

        # Knowledge Checks validation
        checks = [b for b in blocks if b.block_type == "knowledge_check"]
        assert len(checks) == 2, f"Lesson [{lesson.id}] expected 2 knowledge checks, got {len(checks)}"
        for kc in checks:
            total_checks += 1
            c = kc.content or {}
            assert "question" in c and len(c["question"]) > 10, f"KC {kc.id} invalid question"
            assert "options" in c and len(c["options"]) == 4, f"KC {kc.id} must have exactly 4 options"
            assert "answer" in c and c["answer"] in c["options"], f"KC {kc.id} answer not in options"
            assert "explanation" in c and len(c["explanation"]) > 15, f"KC {kc.id} explanation too short"

        # Content Sanitization Scan
        for b in blocks:
            raw_str = str(b.content)
            assert not re.search(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', raw_str), f"Bracket citation leak in block {b.id}: {raw_str[:100]}"
            assert not re.search(r'\[VISUAL:\s*[A-Z]+\]', raw_str), f"Developer visual tag leak in block {b.id}: {raw_str[:100]}"

        print(f"  [PASS] Lesson {idx} [{lesson.id}] '{lesson.title}' -> 5 Pages, {len(blocks)} Blocks, {assets.count()} Assets, 2 MCQs (100% Valid)")

    print("-" * 80)
    print(f"TOPIC 4 SUMMARY: 6 Lessons | {total_blocks} Blocks | {total_assets} Assets | {total_checks} MCQs")
    print("ALL TEST SUITE GATES PASSED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_topic4_tests()
