import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.conf import settings
from billing_payment.models import MpesaPaymentAccount
from billing_payment.gateways.daraja import DarajaGateway
from billing_payment.gateways.base import PaymentInitiationRequest
from billing_payment.utils.config import get_mpesa_callback_url, build_secure_callback_url
import logging

logging.basicConfig(level=logging.INFO)

# Fetch the active account
account = MpesaPaymentAccount.objects.filter(is_active=True).first()
if not account:
    print("No active account found")
    exit(1)

gateway = DarajaGateway(account)

base_callback_url = get_mpesa_callback_url()
secure_callback_url = build_secure_callback_url(base_callback_url)

req = PaymentInitiationRequest(
    amount=1,
    phone_number="254700000000",
    account_reference="TestRef",
    transaction_description="Test Desc",
    callback_url=secure_callback_url,
)

print("--- Running Test STK Push ---")
try:
    gateway.initiate_payment(req)
except Exception as e:
    print("Exception:", e)
