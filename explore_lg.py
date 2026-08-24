import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson

lessons = Lesson.objects.filter(topic__id__in=[81, 82, 83])
lg = LessonBlock.objects.filter(lesson__in=lessons, block_type='learning_goal')
count_no_goals = 0
for b in lg:
    if 'goals' not in b.content:
        count_no_goals += 1
print(f"Total learning goals without 'goals' array: {count_no_goals}")
