import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.get(id=20)

client = Client()
client.force_login(user)

response = client.get(f'/api/subscriptions/users/{user.id}/subscriptions/')
print(f"Status Code: {response.status_code}")
print("Response Data:")
print(response.json() if response.status_code == 200 else response.content)

