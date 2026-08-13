import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock

def deep_scan():
    grade = Grade.objects.get(name="Form 3")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topics = Topic.objects.filter(subject=subject).order_by("order")

    print(f"Scanning all topics in {grade.name} {subject.name}...\n")

    for topic in topics:
        print(f"================================================================================")
        print(f"{topic.name}")
        print(f"================================================================================")
        lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
        for lesson in lessons:
            unit = lesson.learning_unit
            print(f"\n--- Lesson ID {lesson.id}: {lesson.title} ({unit.name}) ---")
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")
            for b in blocks:
                # Print summary of block
                content_preview = json.dumps(b.content, ensure_ascii=False)
                if len(content_preview) > 160:
                    content_preview = content_preview[:160] + "..."
                print(f"  P{b.page_number} [{b.component_type}] Title: '{b.title}' | PageTitle: '{b.page_title}'")
                if b.component_type == "learning_goal":
                    print(f"     Text: {b.content.get('text', '')}")

if __name__ == "__main__":
    deep_scan()
