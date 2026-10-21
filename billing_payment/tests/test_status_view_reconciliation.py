from decimal import Decimal
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient

from billing_payment.models import Invoice, InvoicePaymentTransaction, InvoiceItem, MpesaPaymentAccount
from billing_payment.gateways.base import NormalizedPaymentResult
from billing_payment.mpesa.utils import StkPushResponseParser
from billing_payment.utils.config import get_mpesa_callback_url

User = get_user_model()


class StkPushResponseParserSuccessLogicTest(TestCase):
    def test_status_query_cancelled_is_not_successful(self):
        # Query response with ResponseCode=0 (API call ok) but ResultCode=1032 (user cancelled)
        response_payload = {
            "ResponseCode": "0",
            "ResponseDescription": "The service request has been accepted successfully",
            "MerchantRequestID": "req-1",
            "CheckoutRequestID": "ws_CO_123",
            "ResultCode": "1032",
            "ResultDesc": "Request Cancelled by user."
        }
        parser = StkPushResponseParser(response_payload, is_status_query_request=True)
        self.assertFalse(parser.is_successful())

    def test_status_query_success_is_successful(self):
        # Query response with ResultCode=0
        response_payload = {
            "ResponseCode": "0",
            "ResponseDescription": "The service request has been accepted successfully",
            "MerchantRequestID": "req-1",
            "CheckoutRequestID": "ws_CO_123",
            "ResultCode": "0",
            "ResultDesc": "The service request is processed successfully."
        }
        parser = StkPushResponseParser(response_payload, is_status_query_request=True)
        self.assertTrue(parser.is_successful())

    def test_initial_stk_push_without_result_code(self):
        # Initial STK push response has only ResponseCode
        response_payload = {
            "MerchantRequestID": "req-1",
            "CheckoutRequestID": "ws_CO_123",
            "ResponseCode": "0",
            "ResponseDescription": "Success. Request accepted for processing",
            "CustomerMessage": "Success. Request accepted for processing"
        }
        parser = StkPushResponseParser(response_payload)
        self.assertTrue(parser.is_successful())


class CallbackUrlResolutionTest(TestCase):
    @patch('django.conf.settings.MPESA_CALLBACK_URL', 'https://api.vizlearn.co/api/billing-and-payments/mpesa/stk-push-callback/')
    @patch('django.conf.settings.LIVE_URL', 'vlearn-backend-4y9z.onrender.com')
    def test_get_mpesa_callback_url_ignores_dead_api_vizlearn_co(self):
        url = get_mpesa_callback_url()
        self.assertNotIn("api.vizlearn.co", url)
        self.assertIn("vlearn-backend-4y9z.onrender.com", url)


class InvoicePaymentStatusActiveReconciliationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_poll_user", password="password123")
        self.client.force_authenticate(user=self.user)

        self.invoice = Invoice.objects.create(
            status="PENDING",
            user_to=self.user
        )
        InvoiceItem.objects.create(
            invoice=self.invoice,
            name="Daily Access",
            description="Testing",
            unit_price=Decimal("2.00"),
            quantity=1
        )
        self.tx = InvoicePaymentTransaction.objects.create(
            invoice=self.invoice,
            amount=Decimal("2.00"),
            status="PENDING",
            payment_method="MPESA",
            transaction_details={"checkout_request_id": "ws_CO_POLL_TEST_123"}
        )
        # Set created_at to 5 seconds ago
        InvoicePaymentTransaction.objects.filter(pk=self.tx.pk).update(
            created_at=timezone.now() - timedelta(seconds=5)
        )
        self.tx.refresh_from_db()

    @patch('billing_payment.gateways.daraja.DarajaGateway.query_payment_status')
    @patch('billing_payment.services.resolver.PaymentAccountResolver.get_active_account')
    def test_status_polling_triggers_active_reconciliation_on_success(self, mock_get_account, mock_query_status):
        mock_account = MagicMock()
        mock_account.paybill_number = "174379"
        mock_account.authentication_credentials = {"pass_key": "dummy"}
        mock_get_account.return_value = mock_account

        mock_query_status.return_value = NormalizedPaymentResult(
            is_successful=True,
            provider_transaction_id="ws_CO_POLL_TEST_123",
            receipt_number="POLL_OK_123",
            amount_paid=Decimal("2.00"),
            phone_number="254757654070",
            paid_at=None,
            result_code="0",
            result_description="The service request is processed successfully.",
            raw_payload={"result_code": "0"}
        )

        resp = self.client.get(f"/api/billing-and-payments/invoices/{self.invoice.invoice_number}/status/")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["invoice_status"], "PAID")
        self.assertEqual(data["transaction_status"], "COMPLETED")

        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.status, "PAID")
        self.tx.refresh_from_db()
        self.assertEqual(self.tx.status, "COMPLETED")

    @patch('billing_payment.gateways.daraja.DarajaGateway.query_payment_status')
    @patch('billing_payment.services.resolver.PaymentAccountResolver.get_active_account')
    def test_status_polling_leaves_pending_when_daraja_code_4999(self, mock_get_account, mock_query_status):
        mock_account = MagicMock()
        mock_account.paybill_number = "174379"
        mock_account.authentication_credentials = {"pass_key": "dummy"}
        mock_get_account.return_value = mock_account

        # Daraja returns code 4999 while the user has prompt on phone awaiting PIN
        mock_query_status.return_value = NormalizedPaymentResult(
            is_successful=False,
            provider_transaction_id="ws_CO_POLL_TEST_123",
            receipt_number=None,
            amount_paid=None,
            phone_number=None,
            paid_at=None,
            result_code="4999",
            result_description="The transaction is still under processing",
            raw_payload={"result_code": "4999", "result_description": "The transaction is still under processing"}
        )

        resp = self.client.get(f"/api/billing-and-payments/invoices/{self.invoice.invoice_number}/status/")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        # Must NOT fail prematurely! Must remain PENDING.
        self.assertEqual(data["invoice_status"], "PENDING")
        self.assertEqual(data["transaction_status"], "PENDING")

        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.status, "PENDING")
        self.tx.refresh_from_db()
        self.assertEqual(self.tx.status, "PENDING")

    def test_failed_transaction_recovers_to_completed_when_paid(self):
        from billing_payment.services.orchestrator import PaymentOrchestrator

        # Manually fail transaction first (simulating premature fail)
        self.tx.status = "FAILED"
        self.tx.save()
        self.invoice.status = "CANCELLED"
        self.invoice.save()

        # Success callback or query arrives with valid payment
        result = NormalizedPaymentResult(
            is_successful=True,
            provider_transaction_id="ws_CO_POLL_TEST_123",
            receipt_number="RECOVERED_123",
            amount_paid=Decimal("2.00"),
            phone_number="254757654070",
            paid_at=None,
            result_code="0",
            result_description="The service request is processed successfully.",
            raw_payload={"result_code": "0"}
        )

        resolved = PaymentOrchestrator.resolve_transaction("ws_CO_POLL_TEST_123", result)
        self.assertTrue(resolved)

        self.tx.refresh_from_db()
        self.assertEqual(self.tx.status, "COMPLETED")
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.status, "PAID")

