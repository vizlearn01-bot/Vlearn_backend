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

def detailed_audit():
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    subject = Subject.objects.filter(grade=grade, name="Computer Science").first()

    topics = list(Topic.objects.filter(subject=subject, order__in=[1, 2, 3, 4, 5, 6]).order_by("order"))
    
    bracket_pattern = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')

    print("=" * 80)
    print("DETAILED COMPREHENSIVE PEDAGOGICAL AUDIT (TOPICS 1 - 6)")
    print("=" * 80)

    for topic in topics:
        print(f"\n=======================================================")
        print(f"TOPIC {topic.order}: {topic.name}")
        print("=======================================================")
        
        for unit in topic.learning_units.all().order_by("order"):
            for lesson in unit.lessons.all().order_by("version", "id"):
                print(f"\n--- Lesson: {lesson.title} (ID: {lesson.id}) in Unit {unit.order}: {unit.name} ---")
                blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))
                
                # Check goals
                goals = [b for b in blocks if b.block_type == "learning_goal"]
                print(f"  • Learning Goals: {len(goals)}")
                for g in goals:
                    print(f"      {g.title}: {str(g.content)[:120]}...")

                # Check explanations
                explanations = [b for b in blocks if b.block_type == "concept_explanation"]
                print(f"  • Concept Explanations: {len(explanations)}")
                for exp in explanations:
                    # check for real world analogies
                    raw = json.dumps(exp.content)
                    has_analogy = any(w in raw.lower() for w in ["analogy", "imagine", "like a", "real-world", "metaphor", "kitchen", "traffic", "desk", "library", "factory", "warehouse", "orchestra", "post office", "toll booth", "government"])
                    print(f"      {exp.title} (Analogy detected: {has_analogy})")

                # Check worked examples / traces
                worked = [b for b in blocks if b.block_type in ["worked_example", "step_process"]]
                print(f"  • Worked Examples / Traces: {len(worked)}")
                for w in worked:
                    print(f"      [{w.block_type}] {w.title}")

                # Check MCQs
                mcqs = [b for b in blocks if b.block_type == "knowledge_check"]
                print(f"  • Knowledge Check MCQs: {len(mcqs)}")
                for i, m in enumerate(mcqs, 1):
                    c = m.content or {}
                    q = c.get("question") or c.get("text") or ""
                    opts = c.get("options") or []
                    corr = c.get("correct") or c.get("correct_answer") or c.get("answer")
                    expl = c.get("explanation") or ""
                    print(f"      MCQ {i}: {m.title}")
                    print(f"        Q: {q[:80]}...")
                    print(f"        Opts ({len(opts)}): {opts}")
                    print(f"        Correct: {corr} | Explanation present: {bool(expl)}")

                # Check summaries
                summaries = [b for b in blocks if b.block_type in ["key_takeaway", "summary"]]
                print(f"  • Key Takeaways / Summaries: {len(summaries)}")

                # Check citation leaks
                citation_leaks = []
                for b in blocks:
                    raw_str = str(b.content) + " " + str(b.title)
                    matches = bracket_pattern.findall(raw_str)
                    if matches:
                        citation_leaks.append((b.id, b.block_type, matches))
                if citation_leaks:
                    print(f"  [!] CITATION LEAKS: {citation_leaks}")
                else:
                    print(f"  • Citation Leaks: 0")

if __name__ == "__main__":
    detailed_audit()
