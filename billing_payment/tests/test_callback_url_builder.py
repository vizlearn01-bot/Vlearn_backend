from django.test import TestCase
from unittest.mock import patch
from billing_payment.utils.config import build_secure_callback_url

class CallbackUrlBuilderTest(TestCase):
    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', 'secret_token')
    def test_appends_token_when_missing(self):
        base_url = "https://example.com/callback/"
        result = build_secure_callback_url(base_url)
        self.assertEqual(result, "https://example.com/callback/?token=secret_token")

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', 'secret_token')
    def test_preserves_existing_query_parameters(self):
        base_url = "https://example.com/callback/?foo=bar"
        result = build_secure_callback_url(base_url)
        self.assertIn("foo=bar", result)
        self.assertIn("token=secret_token", result)
        self.assertTrue(result.startswith("https://example.com/callback/?"))

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', 'secret_token')
    def test_does_not_duplicate_token_if_already_present(self):
        base_url = "https://example.com/callback/?token=existing_token"
        result = build_secure_callback_url(base_url)
        self.assertEqual(result, "https://example.com/callback/?token=existing_token")

    @patch('django.conf.settings.MPESA_CALLBACK_SECRET_TOKEN', '')
    def test_returns_base_url_if_no_token_configured(self):
        base_url = "https://example.com/callback/"
        result = build_secure_callback_url(base_url)
        self.assertEqual(result, base_url)
