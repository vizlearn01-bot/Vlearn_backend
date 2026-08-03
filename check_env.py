import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.conf import settings
from billing_payment.models import MpesaPaymentAccount

print(f"MPESA_ENVIRONMENT: {getattr(settings, 'MPESA_ENVIRONMENT', 'Not set')}")
accounts = MpesaPaymentAccount.objects.all()
for acc in accounts:
    print(f"Account: {acc.name}, Active: {acc.is_active}, Environment: {acc.environment}, Paybill: {acc.paybill_number}, Till: {acc.till_number}")

