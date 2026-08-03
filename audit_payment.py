import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from billing_payment.models import InvoicePaymentTransaction, MpesaPaymentAccount
from billing_payment.gateways.daraja import DarajaGateway
import json

print("--- Payment Audit ---")
transaction = InvoicePaymentTransaction.objects.order_by('-created_at').first()

if not transaction:
    print("No transactions found.")
    exit(0)

print(f"Latest Transaction ID: {transaction.id}")
print(f"Status: {transaction.status}")
print(f"Amount: {transaction.amount}")

tx_details = transaction.transaction_details or {}
checkout_request_id = tx_details.get("checkout_request_id")
merchant_request_id = tx_details.get("merchant_request_id")

print(f"CheckoutRequestID: {checkout_request_id}")
print(f"MerchantRequestID: {merchant_request_id}")

if checkout_request_id:
    # Get active account
    account = MpesaPaymentAccount.objects.filter(is_active=True).first()
    if account:
        gateway = DarajaGateway(account)
        try:
            print(f"\nQuerying Daraja STK Query API for {checkout_request_id}...")
            result = gateway.query_payment_status(checkout_request_id)
            print(f"Daraja Status: {'SUCCESS' if result.is_successful else 'FAILED'}")
            print(f"Result Code: {result.result_code}")
            print(f"Result Desc: {result.result_description}")
            print(f"Raw Payload: {json.dumps(result.raw_payload, indent=2)}")
        except Exception as e:
            print(f"Error querying Daraja: {e}")
    else:
        print("No active MpesaPaymentAccount found to query Daraja.")

