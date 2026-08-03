import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from billing_payment.models import InvoicePaymentTransaction, MpesaPaymentAccount
from billing_payment.gateways.daraja import DarajaGateway
from billing_payment.services.orchestrator import PaymentOrchestrator

transaction = InvoicePaymentTransaction.objects.order_by('-created_at').first()

if not transaction:
    print("No transactions found.")
    exit(0)

tx_details = transaction.transaction_details or {}
checkout_request_id = tx_details.get("checkout_request_id")

if checkout_request_id and transaction.status == "PENDING":
    account = MpesaPaymentAccount.objects.filter(is_active=True).first()
    if account:
        gateway = DarajaGateway(account)
        try:
            print(f"Querying Daraja for {checkout_request_id}...")
            result = gateway.query_payment_status(checkout_request_id)
            if result.is_successful:
                print("Payment was successful on Daraja! Reconciling...")
                # We need to manually set amount_paid for Daraja STK Query since it doesn't return it
                result.amount_paid = transaction.invoice.total_amount
                resolved = PaymentOrchestrator.resolve_transaction(checkout_request_id, result)
                print(f"Reconciliation successful: {resolved}")
            else:
                print("Payment failed on Daraja. Reconciling...")
                resolved = PaymentOrchestrator.resolve_transaction(checkout_request_id, result)
                print(f"Reconciliation successful: {resolved}")
        except Exception as e:
            print(f"Error querying Daraja: {e}")

print("Transaction Status is now:")
transaction.refresh_from_db()
print(transaction.status)

