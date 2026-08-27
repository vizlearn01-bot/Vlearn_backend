import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

def inspect_all():
    print("=" * 80)
    print("AUDITING TOPICS 1 TO 6 IN DATABASE")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        print("ERROR: CBC Curriculum not found!")
        return

    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        print("ERROR: Grade 10 not found!")
        return

    subject = Subject.objects.filter(grade=grade, name="Computer Science").first()
    if not subject:
        print("ERROR: Computer Science subject not found!")
        return

    print(f"Subject: {subject.name} (ID: {subject.id}), Grade: {grade.name}, Curriculum: {curriculum.name}")

    topics = list(Topic.objects.filter(subject=subject, order__in=[1, 2, 3, 4, 5, 6]).order_by("order"))
    print(f"Found {len(topics)} topics for orders 1-6:")
    for t in topics:
        print(f"  Topic {t.order}: {t.name} (ID: {t.id})")

    bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')

    report = []

    for topic in topics:
        print("\n" + "=" * 60)
        print(f"TOPIC {topic.order}: {topic.name}")
        print("=" * 60)

        units = list(topic.learning_units.all().order_by("order"))
        print(f"Learning Units ({len(units)}):")
        for unit in units:
            lessons = list(unit.lessons.all().order_by("version", "id"))
            print(f"\n  Unit {unit.order}: {unit.name} ({len(lessons)} lessons)")
            for lesson in lessons:
                blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))
                block_types = [b.block_type for b in blocks]
                
                has_learning_goal = "learning_goal" in block_types
                has_concept_explanation = "concept_explanation" in block_types
                worked_examples = [b for b in blocks if b.block_type in ["worked_example", "step_process"]]
                mcqs = [b for b in blocks if b.block_type == "knowledge_check"]
                has_key_takeaway = any(t in block_types for t in ["key_takeaway", "summary"])
                
                # Check MCQs
                mcq_issues = []
                for i, mcq in enumerate(mcqs, 1):
                    c = mcq.content or {}
                    q_text = c.get("question") or c.get("text") or ""
                    options = c.get("options") or []
                    correct = c.get("correct") or c.get("correct_answer") or c.get("answer")
                    explanation = c.get("explanation") or ""

                    if not q_text:
                        mcq_issues.append(f"MCQ {i} missing question text")
                    if len(options) != 4:
                        mcq_issues.append(f"MCQ {i} has {len(options)} options (expected 4)")
                    if not correct:
                        mcq_issues.append(f"MCQ {i} missing correct answer")
                    if not explanation:
                        mcq_issues.append(f"MCQ {i} missing explanation")

                # Check citation leaks
                citation_leaks = []
                for b in blocks:
                    raw_str = str(b.content) + " " + str(b.title)
                    matches = bracket_pattern.findall(raw_str)
                    if matches:
                        citation_leaks.append(f"Block {b.block_id} ({b.block_type}): {matches}")

                lesson_report = {
                    "topic_order": topic.order,
                    "topic_name": topic.name,
                    "unit_order": unit.order,
                    "unit_name": unit.name,
                    "lesson_id": lesson.id,
                    "lesson_title": lesson.title,
                    "status": lesson.status,
                    "total_blocks": len(blocks),
                    "has_learning_goal": has_learning_goal,
                    "has_concept_explanation": has_concept_explanation,
                    "worked_examples_count": len(worked_examples),
                    "mcqs_count": len(mcqs),
                    "has_key_takeaway": has_key_takeaway,
                    "mcq_issues": mcq_issues,
                    "citation_leaks": citation_leaks,
                }
                report.append(lesson_report)

                status_mark = "✓" if (
                    has_learning_goal and 
                    has_concept_explanation and 
                    len(worked_examples) >= 1 and 
                    len(mcqs) >= 3 and 
                    has_key_takeaway and 
                    len(mcq_issues) == 0 and 
                    len(citation_leaks) == 0
                ) else "✗"

                print(f"    [{status_mark}] Lesson: {lesson.title} (ID: {lesson.id})")
                print(f"        Blocks: {len(blocks)} | Goal: {has_learning_goal} | Concept Expl: {has_concept_explanation}")
                print(f"        Worked Ex: {len(worked_examples)} | MCQs: {len(mcqs)} | Key Takeaway: {has_key_takeaway}")
                if mcq_issues:
                    print(f"        MCQ ISSUES: {mcq_issues}")
                if citation_leaks:
                    print(f"        CITATION LEAKS: {citation_leaks}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Lessons Audited: {len(report)}")
    failing = [r for r in report if not (
        r["has_learning_goal"] and 
        r["has_concept_explanation"] and 
        r["worked_examples_count"] >= 1 and 
        r["mcqs_count"] >= 3 and 
        r["has_key_takeaway"] and 
        len(r["mcq_issues"]) == 0 and 
        len(r["citation_leaks"]) == 0
    )]
    print(f"Compliant: {len(report) - len(failing)}")
    print(f"Failing / Non-compliant: {len(failing)}")
    if failing:
        print("\nFailing Lessons:")
        for f in failing:
            print(f"  - Topic {f['topic_order']}, Unit {f['unit_order']}: '{f['lesson_title']}'")
            if not f['has_learning_goal']: print("      Missing learning_goal")
            if not f['has_concept_explanation']: print("      Missing concept_explanation")
            if f['worked_examples_count'] < 1: print(f"      Lacks worked examples ({f['worked_examples_count']})")
            if f['mcqs_count'] < 3: print(f"      Fewer than 3 MCQs ({f['mcqs_count']})")
            if not f['has_key_takeaway']: print("      Missing key_takeaway/summary")
            if f['mcq_issues']: print(f"      MCQ issues: {f['mcq_issues']}")
            if f['citation_leaks']: print(f"      Citation leaks: {f['citation_leaks']}")

if __name__ == "__main__":
    inspect_all()
