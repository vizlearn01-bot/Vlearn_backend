from django.test import TestCase
from unittest.mock import patch, MagicMock
from decimal import Decimal
from billing_payment.gateways.daraja import DarajaGateway
from billing_payment.gateways.base import PaymentInitiationRequest, NormalizedPaymentResult
from billing_payment.models import MpesaPaymentAccount

class DarajaGatewayPasswordTest(TestCase):
    def setUp(self):
        self.account = MpesaPaymentAccount.objects.create(
            name="Test BuyGoods Valid",
            type="BUY_GOODS",
            till_number="654321",
            environment="SANDBOX",
            is_active=True,
            authentication_credentials={
                "customer_key": "test_key",
                "customer_secret": "test_secret",
                "pass_key": "test_passkey"
            }
        )
        self.gateway = DarajaGateway(self.account)

    def test_gateway_environment_defaults_to_sandbox(self):
        """DarajaGateway must not default to live unless MPESA_ENVIRONMENT='production'."""
        # By default in tests, MPESA_ENVIRONMENT should not be 'production'
        self.assertFalse(self.gateway.is_live)


class DarajaGatewayWebhookValidationTest(TestCase):
    def setUp(self):
        self.account = MpesaPaymentAccount.objects.create(
            name='Test',
            type='PAYBILL',
            authentication_credentials={
                'consumer_key': 'k', 'consumer_secret': 's',
                'business_shortcode': '174379', 'pass_key': 'pk'
            }
        )
        self.gateway = DarajaGateway(self.account)

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', 'mysecret123')
    @patch('django.conf.settings.MPESA_ALLOWED_SOURCE_IPS', [])
    def test_valid_token_accepted(self):
        result = self.gateway.validate_webhook(
            headers={},
            body=b'{}',
            params={'token': 'mysecret123'}
        )
        self.assertTrue(result)

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', 'mysecret123')
    @patch('django.conf.settings.MPESA_ALLOWED_SOURCE_IPS', [])
    def test_wrong_token_rejected(self):
        result = self.gateway.validate_webhook(
            headers={},
            body=b'{}',
            params={'token': 'forgedtoken'}
        )
        self.assertFalse(result)

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', '')
    @patch('django.conf.settings.MPESA_ALLOWED_SOURCE_IPS', ['196.201.214.200'])
    def test_allowed_ip_accepted(self):
        result = self.gateway.validate_webhook(
            headers={'X-Forwarded-For': '196.201.214.200'},
            body=b'{}',
            params={}
        )
        self.assertTrue(result)

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', '')
    @patch('django.conf.settings.MPESA_ALLOWED_SOURCE_IPS', ['196.201.214.200'])
    def test_unknown_ip_rejected(self):
        result = self.gateway.validate_webhook(
            headers={'X-Forwarded-For': '1.2.3.4'},
            body=b'{}',
            params={}
        )
        self.assertFalse(result)

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', '')
    @patch('django.conf.settings.MPESA_ALLOWED_SOURCE_IPS', [])
    def test_empty_config_allows_all(self):
        """When both token and IP settings are empty, all requests are allowed (with warnings)."""
        result = self.gateway.validate_webhook(headers={}, body=b'{}', params={})
        self.assertTrue(result)


class DarajaGatewayParseWebhookTest(TestCase):
    def setUp(self):
        self.account = MpesaPaymentAccount.objects.create(
            name='Test',
            type='PAYBILL',
            authentication_credentials={
                'consumer_key': 'k', 'consumer_secret': 's',
                'business_shortcode': '174379', 'pass_key': 'pk'
            }
        )
        self.gateway = DarajaGateway(self.account)

    def test_successful_callback_parsed(self):
        payload = {
            'Body': {
                'stkCallback': {
                    'MerchantRequestID': 'mr-001',
                    'CheckoutRequestID': 'ws_CO_001',
                    'ResultCode': 0,
                    'ResultDesc': 'The service request is processed successfully.',
                    'CallbackMetadata': {
                        'Item': [
                            {'Name': 'Amount', 'Value': 100},
                            {'Name': 'MpesaReceiptNumber', 'Value': 'PGF4KBKZ3H'},
                            {'Name': 'TransactionDate', 'Value': 20240101120000},
                            {'Name': 'PhoneNumber', 'Value': 254712345678},
                        ]
                    }
                }
            }
        }
        result = self.gateway.parse_webhook_payload(payload)
        self.assertTrue(result.is_successful)
        self.assertEqual(result.provider_transaction_id, 'ws_CO_001')
        self.assertEqual(result.receipt_number, 'PGF4KBKZ3H')
        self.assertEqual(result.amount_paid, Decimal('100'))
        self.assertEqual(result.result_code, '0')

    def test_failed_callback_parsed(self):
        payload = {
            'Body': {
                'stkCallback': {
                    'MerchantRequestID': 'mr-002',
                    'CheckoutRequestID': 'ws_CO_002',
                    'ResultCode': 1032,
                    'ResultDesc': 'Request cancelled by user.',
                }
            }
        }
        result = self.gateway.parse_webhook_payload(payload)
        self.assertFalse(result.is_successful)
        self.assertEqual(result.provider_transaction_id, 'ws_CO_002')
        self.assertEqual(result.result_code, '1032')
