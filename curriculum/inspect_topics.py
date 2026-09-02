import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")

import django
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
print("Curriculum:", curriculum)

grade = Grade.objects.filter(curriculum=curriculum, level=10).first() or Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
print("Grade:", grade)

subject = Subject.objects.filter(grade=grade, name="Business Studies").first()
print("Subject:", subject)

if subject:
    topics = Topic.objects.filter(subject=subject).order_by("order")
    print(f"Found {topics.count()} topics for Business Studies:")
    for t in topics:
        units = t.learning_units.count()
        lessons = t.lessons.count()
        blocks = LessonBlock.objects.filter(lesson__topic=t).count()
        print(f"  Topic {t.order}: '{t.name}' (id={t.id}) -> {units} units, {lessons} lessons, {blocks} blocks")
