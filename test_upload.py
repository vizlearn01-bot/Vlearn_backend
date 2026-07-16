import os
import django
from io import BytesIO

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test.client import RequestFactory
from curriculum.api.views import LessonAssetViewSet
from curriculum.models import Lesson, LessonBlock

lesson = Lesson.objects.first()
block = LessonBlock.objects.first()

factory = RequestFactory(SERVER_NAME='localhost')

file_data = BytesIO(b"dummy image content")
file_data.name = "test.jpg"

request = factory.post('/api/curriculum/lesson-assets/', {
    'lesson': lesson.id,
    'blocks': block.id,
    'asset_type': 'image',
    'storage_type': 'file',
    'status': 'attached',
    'title': 'Test Image',
    'description': '',
    'file': file_data,
})

# Bypass auth for test
view = LessonAssetViewSet.as_view({'post': 'create'})
request.user = None
response = view(request)

print("POST Response Status:", response.status_code)
print("POST Response Content:", response.content.decode() if hasattr(response, 'content') else response.data)

