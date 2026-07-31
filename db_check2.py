import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from organizations.models import School, OrganizationMembership
from Resources.models import User

schools = School.objects.all()
for s in schools:
    print(f"School: {s.name}, Owner: {s.owner.username if s.owner else 'None'}")
    members = OrganizationMembership.objects.filter(school=s)
    for m in members:
        print(f"  Member: {m.user.username}, Role: {m.role}, State: {m.state}")
