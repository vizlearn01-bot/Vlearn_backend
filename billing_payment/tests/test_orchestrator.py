from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from billing_payment.models import Invoice, InvoiceItem, InvoicePaymentTransaction, MpesaPaymentAccount, FinancialLedgerEntry
from billing_payment.gateways.base import NormalizedPaymentResult
from billing_payment.services.orchestrator import PaymentOrchestrator
from billing_payment.services.actions import PaymentActionRegistry, BasePaymentActionHandler


def make_invoice_and_transaction(amount=Decimal('500.00')):
    """Helper to create a minimal Invoice + PENDING InvoicePaymentTransaction."""
    invoice = Invoice.objects.create(
        invoice_from={'full_name': 'VizLearn', 'email': 'billing@vlearn.app', 'city': 'Nairobi'},
        invoice_to={'full_name': 'Test User', 'email': 'user@test.com', 'city': 'Nairobi'},
        issued_date=timezone.now(),
        due_date=timezone.now(),
    )
    InvoiceItem.objects.create(
        invoice=invoice,
        name="Test item",
        description="test",
        unit_price=amount,
        quantity=1
    )
    tx = InvoicePaymentTransaction.objects.create(
        invoice=invoice,
        amount=amount,
        payment_method='MPESA',
        status='PENDING',
        payment_details={'mpesa_phone_number': '254712345678'},
        transaction_details={'checkout_request_id': 'ws_CO_TEST_001'},
    )
    return invoice, tx


def make_successful_result(checkout_request_id='ws_CO_TEST_001', amount=Decimal('500.00')):
    return NormalizedPaymentResult(
        is_successful=True,
        provider_transaction_id=checkout_request_id,
        receipt_number='TESTRECEIPT01',
        amount_paid=amount,
        phone_number='254712345678',
        paid_at=None,
        result_code='0',
        result_description='Success',
        raw_payload={},
    )


def make_failed_result(checkout_request_id='ws_CO_TEST_001'):
    return NormalizedPaymentResult(
        is_successful=False,
        provider_transaction_id=checkout_request_id,
        receipt_number=None,
        amount_paid=None,
        phone_number=None,
        paid_at=None,
        result_code='1032',
        result_description='Request cancelled by user.',
        raw_payload={},
    )


class OrchestratorResolutionTest(TestCase):
    def test_successful_resolution_marks_completed(self):
        invoice, tx = make_invoice_and_transaction()
        result = make_successful_result()
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)
        tx.refresh_from_db()
        invoice.refresh_from_db()
        self.assertEqual(tx.status, 'COMPLETED')
        self.assertEqual(invoice.status, 'PAID')

    def test_successful_resolution_creates_ledger_entry(self):
        invoice, tx = make_invoice_and_transaction()
        result = make_successful_result()
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)
        self.assertTrue(FinancialLedgerEntry.objects.filter(invoice=invoice).exists())
        entry = FinancialLedgerEntry.objects.get(invoice=invoice)
        self.assertEqual(entry.entry_type, 'PAYMENT')
        self.assertEqual(entry.amount, Decimal('500.00'))

    def test_failed_resolution_marks_failed(self):
        invoice, tx = make_invoice_and_transaction()
        result = make_failed_result()
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)
        tx.refresh_from_db()
        invoice.refresh_from_db()
        self.assertEqual(tx.status, 'FAILED')
        self.assertEqual(invoice.status, 'CANCELLED')

    def test_idempotency_duplicate_callback(self):
        """Calling resolve_transaction twice must not create duplicate ledger entries or errors."""
        invoice, tx = make_invoice_and_transaction()
        result = make_successful_result()
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)  # Duplicate
        tx.refresh_from_db()
        self.assertEqual(tx.status, 'COMPLETED')
        self.assertEqual(FinancialLedgerEntry.objects.filter(invoice=invoice).count(), 1)

    def test_ledger_entry_immutability(self):
        invoice, tx = make_invoice_and_transaction()
        result = make_successful_result()
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)
        entry = FinancialLedgerEntry.objects.get(invoice=invoice)
        entry.amount = Decimal('999.00')
        with self.assertRaises(ValueError):
            entry.save()

    def test_no_transaction_found_returns_false(self):
        result = make_successful_result(checkout_request_id='nonexistent')
        resolved = PaymentOrchestrator.resolve_transaction('nonexistent', result)
        self.assertFalse(resolved)


class OrchestratorAmountMismatchTest(TestCase):
    def test_underpayment_fails_transaction(self):
        invoice, tx = make_invoice_and_transaction(amount=Decimal('1000.00'))
        # User only paid 500 but invoice is 1000
        result = NormalizedPaymentResult(
            is_successful=True,
            provider_transaction_id='ws_CO_TEST_001',
            receipt_number='RCP001',
            amount_paid=Decimal('500.00'),
            phone_number='254712345678',
            paid_at=None,
            result_code='0',
            result_description='Success',
            raw_payload={},
        )
        PaymentOrchestrator.resolve_transaction('ws_CO_TEST_001', result)
        tx.refresh_from_db()
        self.assertEqual(tx.status, 'FAILED')
