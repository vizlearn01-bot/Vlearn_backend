"""
billing_payment/tests/test_checks.py

Unit tests for the Django System Check Framework checks in billing_payment/checks.py.

These tests validate that:
- Valid configuration produces no errors
- Missing MPESA account produces an Error (but is silenced in test mode via _is_test_run())
- Multiple active accounts produce a Warning (but silenced in test mode)
- MPESA_ENVIRONMENT validation works correctly
- Callback URL warning fires when both MPESA_CALLBACK_URL and LIVE_URL are absent

NOTE: The DB check (check_active_payment_account) and security token check
(check_mpesa_callback_security) are explicitly silenced during test runs
via _is_test_run() in checks.py. This test file validates the pure logic
by calling the check functions directly and temporarily spoofing sys.argv.
"""
from django.test import TestCase, override_settings
from unittest.mock import patch
from billing_payment.checks import (
    check_mpesa_environment,
    check_mpesa_callback_url,
    check_mpesa_callback_security,
    check_active_payment_account,
)
from billing_payment.models import MpesaPaymentAccount


VALID_CREDENTIALS = {
    "customer_key": "key",
    "customer_secret": "secret",
    "pass_key": "passkey",
}


class CheckMpesaEnvironmentTest(TestCase):
    """Tests for check_mpesa_environment."""

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_valid_sandbox_passes(self):
        errors = check_mpesa_environment(None)
        self.assertEqual(errors, [])

    @override_settings(MPESA_ENVIRONMENT="production")
    def test_valid_production_passes(self):
        errors = check_mpesa_environment(None)
        self.assertEqual(errors, [])

    @override_settings(MPESA_ENVIRONMENT="staging")
    def test_invalid_environment_produces_error(self):
        errors = check_mpesa_environment(None)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].id, "billing_payment.E002")
        self.assertIn("staging", errors[0].msg)

    def test_missing_environment_produces_error(self):
        with self.settings(MPESA_ENVIRONMENT=None):
            errors = check_mpesa_environment(None)
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0].id, "billing_payment.E001")


class CheckMpesaCallbackUrlTest(TestCase):
    """Tests for check_mpesa_callback_url."""

    @override_settings(MPESA_CALLBACK_URL="https://example.ngrok.io/callback/")
    def test_explicit_callback_url_passes(self):
        warnings = check_mpesa_callback_url(None)
        self.assertEqual(warnings, [])

    @override_settings(LIVE_URL="api.vizlearn.co", MPESA_CALLBACK_URL="")
    def test_live_url_fallback_passes(self):
        warnings = check_mpesa_callback_url(None)
        self.assertEqual(warnings, [])

    def test_neither_url_set_produces_warning(self):
        with self.settings(MPESA_CALLBACK_URL="", LIVE_URL=""):
            warnings = check_mpesa_callback_url(None)
            self.assertEqual(len(warnings), 1)
            self.assertEqual(warnings[0].id, "billing_payment.W001")


class CheckMpesaCallbackSecurityTest(TestCase):
    """Tests for check_mpesa_callback_security (silenced during tests by default)."""

    def test_silenced_during_test_run(self):
        """This check is silenced when 'test' is in sys.argv."""
        # In the test environment, sys.argv contains 'test', so this returns []
        result = check_mpesa_callback_security(None)
        self.assertEqual(result, [])

    @patch("billing_payment.checks._is_test_run", return_value=False)
    @override_settings(MPESA_CALLBACK_SECRET_TOKEN="")
    def test_missing_token_produces_warning_in_non_test_mode(self, mock_is_test):
        """When not in test mode, missing token produces a Warning."""
        warnings = check_mpesa_callback_security(None)
        self.assertEqual(len(warnings), 1)
        self.assertEqual(warnings[0].id, "billing_payment.W002")

    @patch("billing_payment.checks._is_test_run", return_value=False)
    @override_settings(MPESA_CALLBACK_SECRET_TOKEN="strong-random-token-xyz")
    def test_configured_token_passes_in_non_test_mode(self, mock_is_test):
        """When not in test mode, configured token produces no warning."""
        warnings = check_mpesa_callback_security(None)
        self.assertEqual(warnings, [])


class CheckActivePaymentAccountTest(TestCase):
    """Tests for check_active_payment_account (silenced during tests by default)."""

    def test_silenced_during_test_run(self):
        """DB check is silenced when running under test runner."""
        result = check_active_payment_account(None)
        self.assertEqual(result, [])

    @patch("billing_payment.checks._is_test_run", return_value=False)
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_no_account_produces_error_in_non_test_mode(self, mock_is_test):
        """In non-test mode, no matching account produces an Error."""
        errors = check_active_payment_account(None)
        error_ids = [e.id for e in errors]
        self.assertIn("billing_payment.E003", error_ids)

    @patch("billing_payment.checks._is_test_run", return_value=False)
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_single_active_account_passes_in_non_test_mode(self, mock_is_test):
        """In non-test mode, one active sandbox account produces no issues."""
        MpesaPaymentAccount.objects.create(
            name="Check Test Sandbox",
            type="PAYBILL",
            environment="SANDBOX",
            is_active=True,
            paybill_number="174379",
            authentication_credentials=VALID_CREDENTIALS,
        )
        issues = check_active_payment_account(None)
        self.assertEqual(issues, [])

    @patch("billing_payment.checks._is_test_run", return_value=False)
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_multiple_active_accounts_produce_warning_in_non_test_mode(self, mock_is_test):
        """In non-test mode, two active sandbox accounts produce a Warning."""
        MpesaPaymentAccount.objects.create(
            name="Check Sandbox A",
            type="PAYBILL",
            environment="SANDBOX",
            is_active=True,
            paybill_number="174379",
            authentication_credentials=VALID_CREDENTIALS,
        )
        MpesaPaymentAccount.objects.create(
            name="Check Sandbox B",
            type="PAYBILL",
            environment="SANDBOX",
            is_active=True,
            paybill_number="600999",
            authentication_credentials=VALID_CREDENTIALS,
        )
        warnings = check_active_payment_account(None)
        warning_ids = [w.id for w in warnings]
        self.assertIn("billing_payment.W003", warning_ids)
