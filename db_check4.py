import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from subscriptions.models import Product, ProductVariant

products = Product.objects.filter(audience='SCHOOL')
for p in products:
    print(f"Product: {p.name}")
    for v in p.variants.all():
        print(f"  Variant: {v.name} | Price: {v.price}")
