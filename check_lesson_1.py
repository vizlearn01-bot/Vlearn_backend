import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson, Topic

t = Topic.objects.get(id=81)
l = Lesson.objects.filter(topic=t).order_by('id').first()
blocks = LessonBlock.objects.filter(lesson=l, page_number=1).order_by('order')
for b in blocks:
    print(f"Order {b.order}: {b.block_type} | {str(b.content)[:100]}")
