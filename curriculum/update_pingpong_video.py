import os, sys, django, json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

b28264 = LessonBlock.objects.get(id=28264)
b28264.content['url'] = "https://www.youtube.com/watch?v=ywjOdG8fOWk"
b28264.content['title'] = "Video Demonstration: Restoring a Dented Ping-Pong Ball with Hot Water"
b28264.content['description'] = "Watch how submerging a dented ping-pong ball into hot water causes the trapped gas molecules inside to heat up and expand, increasing pressure and popping the plastic shell back into a sphere—a vivid demonstration of Charles's Law."
b28264.save()

print("Successfully updated Ping Pong video block (ID 28264) to https://www.youtube.com/watch?v=ywjOdG8fOWk")
