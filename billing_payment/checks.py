"""
billing_payment/checks.py

Django System Check Framework checks for payment configuration.

These checks run automatically on `python manage.py check` and on server startup.
They detect misconfiguration early, before any user attempts a payment.

Test mode:
    Checks that query the database (check_active_payment_account) and checks that
    require infrastructure secrets (check_mpesa_callback_security) are automatically
    silenced during test runs to prevent false failures on an empty test database.
"""
import sys
import logging
from django.conf import settings
from django.core.checks import Error, Warning, register, Tags


def _is_test_run() -> bool:
    """Return True if we are running under the Django test runner."""
    return 'test' in sys.argv or getattr(settings, 'TESTING', False)

logger = logging.getLogger(__name__)

PAYMENT_CHECK_PREFIX = "billing_payment"


@register('configuration')
def check_mpesa_environment(app_configs, **kwargs):
    """Validate MPESA_ENVIRONMENT is set and has a valid value."""
    errors = []
    env = getattr(settings, "MPESA_ENVIRONMENT", None)
    if not env:
        errors.append(
            Error(
                "MPESA_ENVIRONMENT is not configured.",
                hint="Set MPESA_ENVIRONMENT=sandbox or MPESA_ENVIRONMENT=production in your .env file.",
                id=f"{PAYMENT_CHECK_PREFIX}.E001",
            )
        )
    elif env.strip().lower() not in {"sandbox", "production"}:
        errors.append(
            Error(
                f"MPESA_ENVIRONMENT='{env}' is invalid.",
                hint="MPESA_ENVIRONMENT must be 'sandbox' or 'production'.",
                id=f"{PAYMENT_CHECK_PREFIX}.E002",
            )
        )
    return errors


@register('configuration')
def check_mpesa_callback_url(app_configs, **kwargs):
    """Validate that a callback URL can be constructed."""
    warnings = []
    callback_url = getattr(settings, "MPESA_CALLBACK_URL", None)
    live_url = getattr(settings, "LIVE_URL", None)
    if not callback_url and not live_url:
        warnings.append(
            Warning(
                "Neither MPESA_CALLBACK_URL nor LIVE_URL is configured.",
                hint=(
                    "Set MPESA_CALLBACK_URL to your public webhook endpoint "
                    "(e.g. https://<your-ngrok-id>.ngrok-free.app/api/billing-and-payments/mpesa/stk-push-callback/). "
                    "Without this, Safaricom cannot deliver payment callbacks."
                ),
                id=f"{PAYMENT_CHECK_PREFIX}.W001",
            )
        )
    return warnings


@register('configuration')
def check_mpesa_callback_security(app_configs, **kwargs):
    """Warn if callback security token is not configured. Silenced during test runs."""
    if _is_test_run():
        return []
    warnings = []
    token = getattr(settings, "MPESA_CALLBACK_SECRET_TOKEN", None)
    if not token:
        warnings.append(
            Warning(
                "MPESA_CALLBACK_SECRET_TOKEN is not configured.",
                hint=(
                    "Set a strong random token as MPESA_CALLBACK_SECRET_TOKEN in .env. "
                    "Without this, any external party can send fake payment callbacks to your webhook."
                ),
                id=f"{PAYMENT_CHECK_PREFIX}.W002",
            )
        )
    return warnings


@register('database')
def check_active_payment_account(app_configs, **kwargs):
    """
    Validate that exactly one active MpesaPaymentAccount exists for the configured environment.

    This check queries the live database. It is explicitly skipped during test runs
    (detected via sys.argv or settings.TESTING) because the test database is empty
    and seeding it with a MpesaPaymentAccount would be the test's own responsibility.

    Run manually at any time with: python manage.py check --database default
    """  
    if _is_test_run():
        return []
    errors = []
    warnings = []
    try:
        from billing_payment.models import MpesaPaymentAccount
        env = getattr(settings, "MPESA_ENVIRONMENT", "sandbox").strip().upper()
        active_accounts = MpesaPaymentAccount.objects.filter(
            environment=env,
            is_active=True,
        )
        count = active_accounts.count()
        if count == 0:
            errors.append(
                Error(
                    f"No active MpesaPaymentAccount found for environment='{env}'.",
                    hint=(
                        f"Create a MpesaPaymentAccount with environment='{env}' and is_active=True "
                        "via Django Admin, or run: python manage.py seed_mpesa_accounts"
                    ),
                    id=f"{PAYMENT_CHECK_PREFIX}.E003",
                )
            )
        elif count > 1:
            names = ", ".join(a.name for a in active_accounts)
            warnings.append(
                Warning(
                    f"Multiple active MpesaPaymentAccounts found for environment='{env}': [{names}].",
                    hint=(
                        "Exactly one account should be active per environment. "
                        "Deactivate the extras via Django Admin to prevent non-deterministic account resolution."
                    ),
                    id=f"{PAYMENT_CHECK_PREFIX}.W003",
                )
            )
    except Exception as exc:
        # Don't crash the check if DB is unavailable (e.g. during initial migrations)
        warnings.append(
            Warning(
                f"Could not validate MpesaPaymentAccount configuration: {exc}",
                hint="Ensure database migrations are applied.",
                id=f"{PAYMENT_CHECK_PREFIX}.W004",
            )
        )
    return errors + warnings
