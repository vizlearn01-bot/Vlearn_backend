import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from organizations.models import SchoolSubscription, OrganizationMembership
from django.utils import timezone

now = timezone.now()
print(f"Current Time: {now}")

subs = SchoolSubscription.objects.all()
for sub in subs:
    print(f"School: {sub.school.name} | Active: {sub.is_active} | End: {sub.end_date} | Plan: {sub.product_variant.name if sub.product_variant else 'N/A'}")
    
    # Check members
    members = OrganizationMembership.objects.filter(school=sub.school, role='school_admin')
    for m in members:
        print(f"  Admin: {m.user.username} | State: {m.state}")

        # Check has_full_curriculum_access logic
        is_admin = m.user.memberships.filter(
            state__in=['ACCEPTED', 'ACTIVE'],
            role='school_admin',
            school__subscriptions__is_active=True,
            school__subscriptions__end_date__gte=now
        ).exists()
        print(f"  -> has_full_curriculum_access evaluates to: {is_admin}")
