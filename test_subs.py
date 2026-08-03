import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from organizations.services import EntitlementService
User = get_user_model()

print(f"Total Users: {User.objects.count()}")
for user in User.objects.all()[:10]:
    has_access = EntitlementService.has_full_curriculum_access(user)
    allowed = EntitlementService.get_allowed_subject_ids(user)
    print(f"User {user.id} ({user.email}) - Superuser: {user.is_superuser} - Role: {getattr(user, 'role', 'None')} - Access: {has_access} - Allowed: {allowed}")

