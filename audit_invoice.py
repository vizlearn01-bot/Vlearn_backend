import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from billing_payment.models import Invoice

inv = Invoice.objects.last()
print(f"Invoice: {inv.invoice_number}")
if hasattr(inv, 'subscription') and inv.subscription:
    sub = inv.subscription
    print(f"Sub ID: {sub.id}")
    print(f"Sub User: {sub.user.id if sub.user else 'None'}")
    print(f"Sub User Email: {sub.user.email if sub.user else 'None'}")
    print(f"Sub Status: {sub.status_state}")
else:
    print(f"No subscription attr")

