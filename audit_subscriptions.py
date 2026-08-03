import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from billing_payment.models import InvoicePaymentTransaction
from subscriptions.models import Subscription
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.filter(email='jasonbitega@gmail.com').first()
if not user:
    user = User.objects.first()

if not user:
    print("No user found.")
else:
    print(f"User: {user.email} (ID: {user.id})")
    print("--- SUBSCRIPTIONS ---")
    subs = Subscription.objects.filter(user=user)
    if not subs.exists():
        print("No subscriptions found in DB.")
    else:
        for sub in subs:
            print(f"Sub ID: {sub.id}, Plan: {sub.plan.name if sub.plan else 'None'}, Status: {sub.status}")
    
    print("--- TRANSACTIONS ---")
    txs = InvoicePaymentTransaction.objects.filter(invoice__user=user)
    if not txs.exists():
        print("No transactions found in DB.")
    else:
        for tx in txs:
            print(f"Tx ID: {tx.transaction_id}, Status: {tx.status}")

