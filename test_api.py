import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from curriculum.models import Topic

User = get_user_model()
user = User.objects.filter(email='jasonbitega@gmail.com', is_superuser=True).first()

client = Client()
client.force_login(user)

topic = Topic.objects.first()
print("Fetching lesson for topic:", topic.id)
response = client.get(f'/api/curriculum/topics/{topic.id}/lesson/')
print("Status Code:", response.status_code)
if response.status_code != 200:
    print("Content:", response.content)

print("Fetching simulations:")
sim_res = client.get('/api/curriculum/simulations/')
print("Simulations Status:", sim_res.status_code)
if sim_res.status_code != 200:
    print("Sim Content:", sim_res.content)
