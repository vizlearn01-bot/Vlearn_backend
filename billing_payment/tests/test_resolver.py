"""
billing_payment/tests/test_resolver.py

Unit tests for PaymentAccountResolver.
"""
from django.test import TestCase, override_settings
from billing_payment.models import MpesaPaymentAccount
from billing_payment.services.resolver import PaymentAccountResolver, PaymentConfigurationError


VALID_CREDENTIALS = {
    "customer_key": "test_key_1234",
    "customer_secret": "test_secret_5678",
    "pass_key": "test_passkey_abcd",
}


def make_sandbox_account(name="Daraja Sandbox Test", paybill="174379", is_active=True):
    return MpesaPaymentAccount.objects.create(
        name=name,
        type="PAYBILL",
        environment="SANDBOX",
        is_active=is_active,
        paybill_number=paybill,
        authentication_credentials=VALID_CREDENTIALS,
    )


def make_production_account(name="Daraja Production Test", paybill="4165407", is_active=True):
    return MpesaPaymentAccount.objects.create(
        name=name,
        type="PAYBILL",
        environment="PRODUCTION",
        is_active=is_active,
        paybill_number=paybill,
        authentication_credentials=VALID_CREDENTIALS,
    )


class ResolverEnvironmentResolutionTest(TestCase):
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_resolves_sandbox_account_when_env_is_sandbox(self):
        """Resolver returns active SANDBOX account when MPESA_ENVIRONMENT=sandbox."""
        account = make_sandbox_account()
        resolved = PaymentAccountResolver.get_active_account()
        self.assertEqual(resolved.id, account.id)
        self.assertEqual(resolved.environment, "SANDBOX")

    @override_settings(MPESA_ENVIRONMENT="production")
    def test_resolves_production_account_when_env_is_production(self):
        """Resolver returns active PRODUCTION account when MPESA_ENVIRONMENT=production."""
        make_sandbox_account(is_active=False)
        account = make_production_account()
        resolved = PaymentAccountResolver.get_active_account()
        self.assertEqual(resolved.id, account.id)
        self.assertEqual(resolved.environment, "PRODUCTION")

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_environment_mismatch_raises_when_only_production_is_active(self):
        """If MPESA_ENVIRONMENT=sandbox but only a Production account is active, raise."""
        make_production_account(is_active=True)
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("SANDBOX", str(ctx.exception))

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_inactive_sandbox_account_not_returned(self):
        """An inactive account is never resolved."""
        make_sandbox_account(is_active=False)
        with self.assertRaises(PaymentConfigurationError):
            PaymentAccountResolver.get_active_account()


class ResolverMissingAccountTest(TestCase):
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_raises_when_no_account_exists(self):
        """Resolver raises PaymentConfigurationError when DB has no matching account."""
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("No active MpesaPaymentAccount", str(ctx.exception))
        self.assertIn("SANDBOX", str(ctx.exception))

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_error_message_contains_admin_hint(self):
        """Error message guides developer to Django Admin."""
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("Django Admin", str(ctx.exception))


class ResolverDuplicateAccountTest(TestCase):
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_raises_when_multiple_active_sandbox_accounts(self):
        """Resolver raises when two SANDBOX accounts are active."""
        make_sandbox_account(name="Sandbox Account A", paybill="174379")
        make_sandbox_account(name="Sandbox Account B", paybill="600999")
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        error_msg = str(ctx.exception)
        self.assertIn("Multiple active MpesaPaymentAccounts", error_msg)
        self.assertIn("Sandbox Account A", error_msg)
        self.assertIn("Sandbox Account B", error_msg)

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_inactive_duplicate_does_not_trigger_error(self):
        """One active + one inactive: should resolve cleanly."""
        active = make_sandbox_account(name="Active Sandbox", is_active=True)
        make_sandbox_account(name="Inactive Sandbox", is_active=False)
        resolved = PaymentAccountResolver.get_active_account()
        self.assertEqual(resolved.id, active.id)


class ResolverCredentialValidationTest(TestCase):
    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_raises_when_shortcode_missing(self):
        """Resolver raises when paybill_number and till_number are both empty."""
        MpesaPaymentAccount.objects.create(
            name="No Shortcode",
            type="PAYBILL",
            environment="SANDBOX",
            is_active=True,
            paybill_number="",
            till_number="",
            authentication_credentials=VALID_CREDENTIALS,
        )
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("no paybill_number or till_number", str(ctx.exception))

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_raises_when_credentials_missing_entirely(self):
        """Resolver raises when authentication_credentials is empty."""
        MpesaPaymentAccount.objects.create(
            name="No Creds",
            type="PAYBILL",
            environment="SANDBOX",
            is_active=True,
            paybill_number="174379",
            authentication_credentials={},
        )
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("authentication_credentials configured", str(ctx.exception))

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_raises_when_pass_key_missing(self):
        """Resolver raises when pass_key is absent from credentials."""
        MpesaPaymentAccount.objects.create(
            name="Missing Passkey",
            type="PAYBILL",
            environment="SANDBOX",
            is_active=True,
            paybill_number="174379",
            authentication_credentials={
                "customer_key": "some_key",
                "customer_secret": "some_secret",
            },
        )
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("pass_key", str(ctx.exception))

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_raises_for_invalid_account_type(self):
        """Resolver raises when account type is not PAYBILL or BUY_GOODS."""
        MpesaPaymentAccount.objects.create(
            name="Bad Type",
            type="CASH",
            environment="SANDBOX",
            is_active=True,
            paybill_number="174379",
            authentication_credentials=VALID_CREDENTIALS,
        )
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("unsupported type", str(ctx.exception))

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_till_number_accepted_when_paybill_missing(self):
        """BUY_GOODS account with till_number resolves cleanly."""
        MpesaPaymentAccount.objects.create(
            name="Till Account",
            type="BUY_GOODS",
            environment="SANDBOX",
            is_active=True,
            paybill_number="",
            till_number="123456",
            authentication_credentials=VALID_CREDENTIALS,
        )
        account = PaymentAccountResolver.get_active_account()
        self.assertEqual(account.name, "Till Account")

    @override_settings(MPESA_ENVIRONMENT="sandbox")
    def test_valid_account_resolves_and_returns(self):
        """A fully configured account returns without raising."""
        expected = make_sandbox_account()
        resolved = PaymentAccountResolver.get_active_account()
        self.assertEqual(resolved.id, expected.id)


class ResolverInvalidEnvironmentSettingTest(TestCase):
    @override_settings(MPESA_ENVIRONMENT="staging")
    def test_raises_for_unrecognized_environment_value(self):
        """Resolver raises immediately when MPESA_ENVIRONMENT is not sandbox or production."""
        with self.assertRaises(PaymentConfigurationError) as ctx:
            PaymentAccountResolver.get_active_account()
        self.assertIn("staging", str(ctx.exception))
        self.assertIn("invalid", str(ctx.exception).lower())
