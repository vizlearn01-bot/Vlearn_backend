import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.contrib.auth import get_user_model, authenticate
User = get_user_model()

print("ALL USERS AND PASSWORD HASH PREFIXES:")
for u in User.objects.all():
    print(f"Username: {u.username}, Password prefix: {u.password[:45]}, Is Superuser: {u.is_superuser}")

# Try to authenticate a test user
print("\nAttempting to authenticate 'jason' with 'password':")
try:
    user = authenticate(username="jason", password="password")
    print(f"Auth result: {user}")
except Exception as e:
    print(f"Auth exception: {e}")
