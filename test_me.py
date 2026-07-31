import os, django
from rest_framework.test import APIClient
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()
from Resources.models import User

client = APIClient()
user = User.objects.get(username="school_admin1")
client.force_authenticate(user=user)
resp = client.get("/api/subscriptions/entitlements/me/")
print("Status:", resp.status_code)
print("Data:", resp.json() if resp.status_code == 200 else resp.content)
