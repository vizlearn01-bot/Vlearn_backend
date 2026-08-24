import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson, Topic, Subject

topics = Topic.objects.filter(id__in=[81, 82, 83]).order_by('id')
for t in topics:
    print(f"Topic {t.id}: {t.name}")
    lessons = Lesson.objects.filter(topic=t).order_by('id')
    for idx, l in enumerate(lessons):
        print(f"  Lesson {idx+1}: {l.title}")
        blocks = LessonBlock.objects.filter(lesson=l).order_by('page_number', 'order')
        # print first few blocks
        for b in blocks[:2]:
            print(f"    Pg {b.page_number} Order {b.order}: {b.block_type} | Content: {str(b.content)[:100]}")
