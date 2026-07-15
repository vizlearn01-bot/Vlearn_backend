import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock
from curriculum.api.serializers import LessonV2Serializer

lesson = Lesson.objects.last()
data = LessonV2Serializer(lesson).data
for block in data.get('blocks', []):
    if block.get('block_type') == 'suggested_diagram':
        print("Diagram block:")
        print("ID:", block.get('id'))
        print("Assets:", block.get('assets'))
