import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson, Topic, Subject

topics = Topic.objects.filter(id__in=[81, 82, 83]).order_by('id')
for t in topics:
    print(f"Topic {t.id}: {t.title}")
    lessons = Lesson.objects.filter(topic=t).order_by('order')
    for l in lessons:
        print(f"  Lesson {l.order}: {l.title}")
        blocks = LessonBlock.objects.filter(lesson=l).order_by('page_number', 'order')
        # print first few blocks
        for b in blocks[:2]:
            print(f"    Pg {b.page_number} Order {b.order}: {b.block_type} | Content: {str(b.content)[:100]}")
