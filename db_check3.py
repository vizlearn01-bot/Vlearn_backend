import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from organizations.models import SchoolSubscription

subs = SchoolSubscription.objects.all()
for sub in subs:
    plan_name = sub.plan.name if sub.plan else "N/A"
    variant_name = sub.product_variant.name if sub.product_variant else "N/A"
    print(f"School: {sub.school.name} | Active: {sub.is_active} | End: {sub.end_date} | Plan: {plan_name} | Variant: {variant_name}")
