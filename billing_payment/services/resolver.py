"""
billing_payment/services/resolver.py

Centralized payment account resolver.

This is the ONLY entry point for obtaining a configured MpesaPaymentAccount
at runtime. No serializer, view, task, gateway or other service should
query MpesaPaymentAccount directly for payment purposes.
"""
import logging
from django.conf import settings
from billing_payment.models import MpesaPaymentAccount

logger = logging.getLogger(__name__)


class PaymentConfigurationError(Exception):
    """
    Raised when the payment configuration is missing, incomplete, or inconsistent.
    Fail-fast: this error surfaces immediately rather than producing a runtime
    payment failure that the user sees as a generic error.
    """
    pass


class PaymentAccountResolver:
    """
    Centralized resolver for MpesaPaymentAccount selection.

    Responsibilities:
        - Selects the correct payment account for the current MPESA_ENVIRONMENT.
        - Validates that exactly one active, correctly-configured account exists.
        - Validates required credentials are present.
        - Raises PaymentConfigurationError immediately if configuration is invalid.

    This class must be the sole gateway into payment account resolution.
    Every payment execution path — serializers, views, tasks, webhooks —
    must call PaymentAccountResolver.get_active_account() rather than
    querying MpesaPaymentAccount directly.
    """

    # Required credential keys inside authentication_credentials JSON
    REQUIRED_CREDENTIAL_KEYS = {"customer_key", "customer_secret", "pass_key"}

    # Valid account types
    VALID_ACCOUNT_TYPES = {"PAYBILL", "BUY_GOODS"}

    @classmethod
    def get_active_account(cls) -> MpesaPaymentAccount:
        """
        Returns the single active MpesaPaymentAccount for the current environment.

        Resolution rules:
            1. Reads MPESA_ENVIRONMENT from Django settings.
            2. Queries MpesaPaymentAccount where environment matches and is_active=True.
            3. Validates exactly one account is active.
            4. Validates required credentials are present.
            5. Validates account type is supported.

        Returns:
            MpesaPaymentAccount: The validated, active payment account.

        Raises:
            PaymentConfigurationError: If any validation step fails.
        """
        environment = cls._get_environment()
        accounts = cls._query_active_accounts(environment)
        account = cls._assert_single_account(accounts, environment)
        cls._validate_account(account)
        logger.debug(
            "PaymentAccountResolver: Resolved account '%s' (env=%s, type=%s, shortcode=%s)",
            account.name,
            account.environment,
            account.type,
            account.paybill_number or account.till_number or "N/A",
        )
        return account

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @classmethod
    def _get_environment(cls) -> str:
        """Return the configured MPESA_ENVIRONMENT in uppercase."""
        env_raw = getattr(settings, "MPESA_ENVIRONMENT", "sandbox")
        env = env_raw.strip().upper()
        valid_envs = {"SANDBOX", "PRODUCTION"}
        if env not in valid_envs:
            raise PaymentConfigurationError(
                f"MPESA_ENVIRONMENT='{env_raw}' is invalid. "
                f"Must be one of: {sorted(valid_envs)}."
            )
        return env

    @classmethod
    def _query_active_accounts(
        cls, environment: str
    ) -> list:
        """Return all active accounts for the given environment."""
        return list(
            MpesaPaymentAccount.objects.filter(
                environment=environment,
                is_active=True,
            )
        )

    @classmethod
    def _assert_single_account(
        cls, accounts: list, environment: str
    ) -> MpesaPaymentAccount:
        """Assert exactly one active account exists; raise otherwise."""
        count = len(accounts)
        if count == 0:
            raise PaymentConfigurationError(
                f"No active MpesaPaymentAccount found for environment='{environment}'. "
                "Create one via Django Admin and set is_active=True and "
                f"environment='{environment}'."
            )
        if count > 1:
            names = ", ".join(a.name for a in accounts)
            raise PaymentConfigurationError(
                f"Multiple active MpesaPaymentAccounts found for environment='{environment}': "
                f"[{names}]. Exactly one account may be active per environment. "
                "Deactivate the others via Django Admin."
            )
        return accounts[0]

    @classmethod
    def _validate_account(cls, account: MpesaPaymentAccount) -> None:
        """Validate that the account has all required fields and credentials."""
        # Validate account type
        if account.type not in cls.VALID_ACCOUNT_TYPES:
            raise PaymentConfigurationError(
                f"MpesaPaymentAccount '{account.name}' has unsupported type='{account.type}'. "
                f"Supported types: {sorted(cls.VALID_ACCOUNT_TYPES)}."
            )

        # Validate shortcode is present
        shortcode = account.paybill_number or account.till_number
        if not shortcode:
            raise PaymentConfigurationError(
                f"MpesaPaymentAccount '{account.name}' has no paybill_number or till_number configured."
            )

        # Validate credentials dictionary exists
        creds = account.authentication_credentials
        if not creds or not isinstance(creds, dict):
            raise PaymentConfigurationError(
                f"MpesaPaymentAccount '{account.name}' has no authentication_credentials configured."
            )

        # Validate all required credential keys are present and non-empty
        missing = [
            key for key in cls.REQUIRED_CREDENTIAL_KEYS
            if not creds.get(key)
        ]
        if missing:
            raise PaymentConfigurationError(
                f"MpesaPaymentAccount '{account.name}' is missing required credentials: "
                f"{sorted(missing)}. Set these values via Django Admin."
            )

        logger.debug(
            "PaymentAccountResolver: Account '%s' passed validation.",
            account.name,
        )
