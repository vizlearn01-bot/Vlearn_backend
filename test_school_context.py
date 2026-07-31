import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from organizations.models import Stream, Subject
from curriculum.models import Subject as CurriculumSubject

print(Stream.objects.first().__dict__ if Stream.objects.first() else "No streams")
print(CurriculumSubject.objects.first().__dict__ if CurriculumSubject.objects.first() else "No subjects")
