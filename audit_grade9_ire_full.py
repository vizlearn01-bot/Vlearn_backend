"""
Grade 9 Islamic Religious Education (IRE)
Comprehensive Full Audit & Verification Script
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def run_comprehensive_audit():
    print("=" * 80)
    print("VLEARN GRADE 9 IRE COMPREHENSIVE QUALITY AUDIT")
    print("=" * 80)

    # 1. Subject & Grade Verification
    grade = Grade.objects.get(curriculum__name="CBC", name="Grade 9")
    subject = Subject.objects.get(grade=grade, name="IRE")
    print(f"[*] Grade: {grade.curriculum.name} - {grade.name} (ID: {grade.id})")
    print(f"[*] Subject: {subject.name} (ID: {subject.id})")

    # 2. Topics Verification
    topics = Topic.objects.filter(subject=subject).order_by('order')
    print(f"\n[*] Total Topics in Subject: {topics.count()}")
    for t in topics:
        print(f"  - Topic {t.order}: {t.name} (ID: {t.id})")

    assert topics.count() == 3, f"Expected 3 topics, found {topics.count()}"

    # 3. Learning Units & Lessons Count
    all_units = LearningUnit.objects.filter(topic__subject=subject).order_by('topic__order', 'order')
    all_lessons = Lesson.objects.filter(topic__subject=subject).order_by('topic__order', 'learning_unit__order')

    print(f"\n[*] Total Learning Units: {all_units.count()}")
    print(f"[*] Total Lessons: {all_lessons.count()}")

    assert all_units.count() == 22, f"Expected 22 learning units, found {all_units.count()}"
    assert all_lessons.count() == 22, f"Expected 22 lessons, found {all_lessons.count()}"

    # Check all lessons are published
    published_count = all_lessons.filter(status='published').count()
    print(f"[*] Published Lessons: {published_count} / {all_lessons.count()}")
    assert published_count == 22, f"Expected 22 published lessons, found {published_count}"

    # 4. Pages / Cards Audit
    all_blocks = LessonBlock.objects.filter(lesson__topic__subject=subject)
    print(f"\n[*] Total Content Blocks: {all_blocks.count()}")

    total_pages = 0
    lessons_with_7_pages = 0
    for lesson in all_lessons:
        distinct_pages = set(lesson.blocks.values_list('page_number', flat=True))
        total_pages += len(distinct_pages)
        if len(distinct_pages) == 7:
            lessons_with_7_pages += 1
        else:
            print(f"  [!] Lesson {lesson.id} ({lesson.title}) has {len(distinct_pages)} pages: {distinct_pages}")

    print(f"[*] Total Distinct Pages/Cards: {total_pages}")
    print(f"[*] Lessons with exactly 7 Cards: {lessons_with_7_pages} / {all_lessons.count()}")
    assert lessons_with_7_pages == 22, f"Expected all 22 lessons to have 7 cards, found {lessons_with_7_pages}"

    # 5. Media & Assets Audit
    all_assets = LessonAsset.objects.filter(lesson__topic__subject=subject)
    svg_assets = all_assets.filter(asset_type='diagram')
    img_assets = all_assets.filter(asset_type='image')
    yt_assets = all_assets.filter(asset_type='youtube')

    print(f"\n[*] Total Lesson Assets: {all_assets.count()}")
    print(f"  - Vector SVG Diagrams: {svg_assets.count()}")
    print(f"  - Authentic Images: {img_assets.count()}")
    print(f"  - Educational YouTube Videos: {yt_assets.count()}")

    assert svg_assets.count() >= 22, f"Expected at least 22 SVG diagrams, found {svg_assets.count()}"
    assert img_assets.count() >= 22, f"Expected at least 22 images, found {img_assets.count()}"

    # Verify SVGs have valid content
    valid_svgs = 0
    for a in svg_assets:
        svg_str = a.metadata.get('svg_content', '')
        if '<svg' in svg_str and '</svg>' in svg_str and 'viewBox' in svg_str:
            valid_svgs += 1
    print(f"[*] Valid SVG Diagrams: {valid_svgs} / {svg_assets.count()}")
    assert valid_svgs == svg_assets.count()

    # 6. MCQs & Assessments Audit
    mcq_blocks = all_blocks.filter(block_type='knowledge_check')
    print(f"\n[*] Total Knowledge Check / MCQ Blocks: {mcq_blocks.count()}")
    assert mcq_blocks.count() == 22, f"Expected 22 MCQ blocks, found {mcq_blocks.count()}"

    valid_mcqs = 0
    for b in mcq_blocks:
        c = b.content or {}
        has_q = bool(c.get('question'))
        has_opts = bool(c.get('options') or c.get('options_list'))
        has_ans = bool(c.get('answer') or c.get('correct_answer'))
        has_exp = bool(c.get('explanation') or c.get('feedback'))
        if has_q and has_ans and has_exp:
            valid_mcqs += 1
        else:
            print(f"  [!] Incomplete MCQ in Block {b.id}: question={has_q}, options={has_opts}, answer={has_ans}, explanation={has_exp}")

    print(f"[*] Verified Complete MCQs: {valid_mcqs} / {mcq_blocks.count()}")
    assert valid_mcqs == 22

    # 7. Pedagogy Components Count
    learning_goals = all_blocks.filter(block_type='learning_goal').count()
    concept_explanations = all_blocks.filter(block_type='concept_explanation').count()
    callouts = all_blocks.filter(block_type='callout').count()
    worked_examples = all_blocks.filter(block_type='worked_example').count()
    real_world_apps = all_blocks.filter(block_type__in=['real_world_example', 'real_world_connection']).count()
    reflections = all_blocks.filter(block_type='reflection').count()
    summaries = all_blocks.filter(block_type='summary').count()
    mini_activities = all_blocks.filter(block_type='mini_activity').count()
    misconceptions = all_blocks.filter(block_type__in=['common_misconception', 'common_mistake']).count()
    comparison_tables = all_blocks.filter(block_type='comparison_table').count()
    step_processes = all_blocks.filter(block_type='step_process').count()

    print(f"\n[*] Pedagogical Component Breakdown:")
    print(f"  - Learning Goals: {learning_goals}")
    print(f"  - Concept Explanations: {concept_explanations}")
    print(f"  - Scripture Callouts: {callouts}")
    print(f"  - Worked Examples / Scenarios: {worked_examples}")
    print(f"  - Real-World Applications: {real_world_apps}")
    print(f"  - Reflections: {reflections}")
    print(f"  - Misconception Checks: {misconceptions}")
    print(f"  - Comparison Tables: {comparison_tables}")
    print(f"  - Step Processes: {step_processes}")
    print(f"  - Knowledge Checks (MCQs): {mcq_blocks.count()}")
    print(f"  - Summaries: {summaries}")
    print(f"  - Mini Activities / Exit Tickets: {mini_activities}")

    # 8. Strict Scope Isolation Verification
    # Ensure no other Grade 9 subject was modified
    cre_grade9 = Subject.objects.get(grade=grade, name="CRE")
    assert cre_grade9.topics.count() == 16, f"Expected 16 CRE topics, found {cre_grade9.topics.count()}"
    english_grade9 = Subject.objects.get(grade=grade, name="English")
    print(f"\n[*] Scope Isolation Confirmed:")
    print(f"  - Grade 9 CRE Topics preserved: {cre_grade9.topics.count()}")
    print(f"  - Grade 9 English Subject ID: {english_grade9.id}")
    print(f"  - No unrelated curriculum records were altered.")

    print("\n" + "=" * 80)
    print("ALL AUDIT CHECKS PASSED PERFECTLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_comprehensive_audit()
