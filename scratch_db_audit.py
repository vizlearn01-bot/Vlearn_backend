import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.apps import apps
from django.db import connection

print("--- Database Record Counts ---")
for model in apps.get_models():
    try:
        count = model.objects.count()
        if count > 0:
            print(f"{model._meta.label}: {count}")
    except Exception as e:
        pass
