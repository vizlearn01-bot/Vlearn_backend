import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from subscriptions.models import Subscription

subs = Subscription.objects.filter(user_id=20, status_state="ACTIVE").order_by('-end_date')
for sub in subs:
    print(f"Subscription ID: {sub.id}")
    print(f"Status: {sub.status_state}")
    print(f"Start Date: {sub.start_date}")
    print(f"End Date: {sub.end_date}")

