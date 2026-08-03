import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Topic, Lesson
from django.contrib.auth import get_user_model
from curriculum.api.serializers import LessonV2Serializer

User = get_user_model()
user = User.objects.filter(is_superuser=True).first()

topic = Topic.objects.first()
print("Topic:", topic)

try:
    lesson = Lesson.objects.filter(topic=topic, status='published').first()
    if not lesson:
        lesson = Lesson.objects.filter(topic=topic).first()
    
    if lesson:
        print("Found Lesson:", lesson)
        serializer = LessonV2Serializer(lesson, context={'request': type('MockReq', (object,), {'user': user, 'build_absolute_uri': lambda s: s})()})
        print("Serialized keys:", serializer.data.keys())
    else:
        print("No lesson")
except Exception as e:
    import traceback
    traceback.print_exc()

