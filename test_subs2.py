import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from organizations.services import EntitlementService
User = get_user_model()

access_count = 0
for user in User.objects.all():
    has_access = EntitlementService.has_full_curriculum_access(user)
    if has_access:
        access_count += 1
        print(f"User {user.id} ({user.email}) has full access.")

print(f"Total users with access: {access_count}")

