import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.filter(email='jasonbitega@gmail.com')
for u in users:
    print(f"ID: {u.id}, Email: {u.email}, Username: {u.username}, Role: {getattr(u, 'role', 'N/A')}")
