from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from billing_payment.models import Invoice, InvoiceItem, InvoicePaymentTransaction
from billing_payment.gateways.base import NormalizedPaymentResult
from billing_payment.services.actions import PaymentActionRegistry, BasePaymentActionHandler
from billing_payment.services.orchestrator import PaymentOrchestrator
from subscriptions.models import Product, ProductVariant, Subscription
from Resources.models import User


def make_test_user():
    return User.objects.create_user(
        username='testbuyer',
        email='buyer@test.com',
        password='TestPass123!'
    )


def make_product_variant():
    product = Product.objects.create(
        name='Test Plan',
        slug='test-plan',
        audience='STUDENT'
    )
    return ProductVariant.objects.create(
        product=product,
        name='Monthly',
        slug='monthly-test',
        duration_type='MONTHLY',
        duration_days=30,
        price=Decimal('500.00')
    )


class SubscriptionActionHandlerTest(TestCase):
    def setUp(self):
        # Ensure the SubscriptionActionHandler is registered
        from subscriptions.services.actions import SubscriptionActionHandler
        PaymentActionRegistry.register('SUBSCRIPTION', SubscriptionActionHandler())

        self.user = make_test_user()
        self.variant = make_product_variant()

        self.invoice = Invoice.objects.create(
            invoice_from={'full_name': 'VizLearn', 'email': 'billing@vlearn.app', 'city': 'Nairobi'},
            invoice_to={'full_name': 'Test User', 'email': 'buyer@test.com', 'city': 'Nairobi'},
            issued_date=timezone.now(),
            due_date=timezone.now(),
        )
        InvoiceItem.objects.create(
            invoice=self.invoice,
            name="Test item",
            description="test",
            unit_price=Decimal('500.00'),
            quantity=1
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            product_variant=self.variant,
            status_state='PENDING_PAYMENT',
            is_active=False,
            invoice=self.invoice,
        )
        self.tx = InvoicePaymentTransaction.objects.create(
            invoice=self.invoice,
            amount=Decimal('500.00'),
            payment_method='MPESA',
            status='PENDING',
            payment_details={'mpesa_phone_number': '254712345678'},
            transaction_details={'checkout_request_id': 'ws_CO_SUB_001'},
        )

    def test_payment_completes_activates_subscription(self):
        """Full end-to-end: payment callback -> orchestrator -> registry -> subscription active."""
        result = NormalizedPaymentResult(
            is_successful=True,
            provider_transaction_id='ws_CO_SUB_001',
            receipt_number='RCPT001',
            amount_paid=Decimal('500.00'),
            phone_number='254712345678',
            paid_at=None,
            result_code='0',
            result_description='Success',
            raw_payload={},
        )
        PaymentOrchestrator.resolve_transaction('ws_CO_SUB_001', result)
        self.subscription.refresh_from_db()
        self.assertEqual(self.subscription.status_state, 'ACTIVE')
        self.assertTrue(self.subscription.is_active)
        self.assertIsNotNone(self.subscription.start_date)
        self.assertIsNotNone(self.subscription.end_date)
        self.assertIsNotNone(self.subscription.activated_at)

    def test_payment_failure_cancels_subscription(self):
        """Payment failure -> subscription cancelled."""
        result = NormalizedPaymentResult(
            is_successful=False,
            provider_transaction_id='ws_CO_SUB_001',
            receipt_number=None,
            amount_paid=None,
            phone_number=None,
            paid_at=None,
            result_code='1032',
            result_description='Request cancelled by user.',
            raw_payload={},
        )
        PaymentOrchestrator.resolve_transaction('ws_CO_SUB_001', result)
        self.subscription.refresh_from_db()
        self.assertEqual(self.subscription.status_state, 'CANCELLED')
        self.assertFalse(self.subscription.is_active)

    def test_no_handler_registered_dispatches_gracefully(self):
        """If no handler is registered for action type, PaymentActionRegistry must not raise."""
        # Temporarily clear handlers
        original_handlers = PaymentActionRegistry._handlers.copy()
        PaymentActionRegistry._handlers.clear()
        try:
            result = NormalizedPaymentResult(
                is_successful=True,
                provider_transaction_id='ws_CO_SUB_001',
                receipt_number='R1',
                amount_paid=Decimal('500.00'),
                phone_number='254712345678',
                paid_at=None,
                result_code='0',
                result_description='Success',
                raw_payload={},
            )
            # Should not raise despite no handler registered
            dispatched = PaymentActionRegistry.dispatch_completed(self.invoice, self.tx, result)
            self.assertFalse(dispatched)
        finally:
            PaymentActionRegistry._handlers = original_handlers
