import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson

lessons = Lesson.objects.filter(topic__id__in=[81, 82, 83])
we = LessonBlock.objects.filter(lesson__in=lessons, block_type='worked_example')
for b in we:
    if 'steps' not in b.content:
        print(f"NO STEPS: Lesson {b.lesson.title}, Pg {b.page_number} | Content: {str(b.content)[:200]}")
