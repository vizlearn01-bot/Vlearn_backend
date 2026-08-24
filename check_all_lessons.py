import os, sys, django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock, Lesson, Topic

topics = Topic.objects.filter(id__in=[81, 82, 83]).order_by('id')
for t in topics:
    lessons = Lesson.objects.filter(topic=t).order_by('id')
    for l in lessons:
        page1_blocks = LessonBlock.objects.filter(lesson=l, page_number=1).order_by('order')
        first = page1_blocks.first()
        if not first or first.block_type not in ['photo_view', 'suggested_image']:
            print(f"MISSING IMAGE: {t.name} -> {l.title}")
