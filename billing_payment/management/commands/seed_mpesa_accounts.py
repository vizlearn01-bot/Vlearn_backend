"""
Management command: seed_mpesa_accounts

Creates or updates MpesaPaymentAccount records from environment variables.

Usage:
    python manage.py seed_mpesa_accounts
    python manage.py seed_mpesa_accounts --env sandbox
    python manage.py seed_mpesa_accounts --env production

This command reads M-Pesa credentials from Django settings (loaded from .env)
and writes them to the database, making the database the authoritative runtime
source and .env the bootstrap source for credential entry.

Development usage:
    1. Set MPESA_ENVIRONMENT=sandbox in .env
    2. Set sandbox credentials in .env (MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET, MPESA_PASSKEY, MPESA_SHORTCODE)
    3. Run: python manage.py seed_mpesa_accounts
    4. A Sandbox MpesaPaymentAccount will be created/updated in the database.

Production usage:
    Add production credentials to .env (or environment variables), run the command, then
    manually set is_active=True via Django Admin for the Production account.
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from billing_payment.models import MpesaPaymentAccount


class Command(BaseCommand):
    help = "Seed MpesaPaymentAccount records from environment variables (.env)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--env",
            type=str,
            default=None,
            help="Environment to seed: 'sandbox' or 'production'. Defaults to MPESA_ENVIRONMENT from settings.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print what would be created/updated without saving.",
        )

    def handle(self, *args, **options):
        env_arg = options.get("env")
        dry_run = options.get("dry_run", False)

        env_raw = env_arg or getattr(settings, "MPESA_ENVIRONMENT", "sandbox")
        environment = env_raw.strip().upper()

        if environment not in {"SANDBOX", "PRODUCTION"}:
            self.stderr.write(
                self.style.ERROR(
                    f"Invalid environment '{env_raw}'. Must be 'sandbox' or 'production'."
                )
            )
            return

        consumer_key = getattr(settings, "MPESA_CONSUMER_KEY", None)
        consumer_secret = getattr(settings, "MPESA_CONSUMER_SECRET", None)
        passkey = getattr(settings, "MPESA_PASSKEY", None)
        shortcode = getattr(settings, "MPESA_SHORTCODE", None)
        shortcode_type = getattr(settings, "MPESA_SHORTCODE_TYPE", "paybill").upper()
        account_type = "PAYBILL" if shortcode_type == "PAYBILL" else "BUY_GOODS"

        missing_settings = []
        if not consumer_key:
            missing_settings.append("MPESA_CONSUMER_KEY")
        if not consumer_secret:
            missing_settings.append("MPESA_CONSUMER_SECRET")
        if not passkey:
            missing_settings.append("MPESA_PASSKEY")
        if not shortcode:
            missing_settings.append("MPESA_SHORTCODE")

        if missing_settings:
            self.stderr.write(
                self.style.ERROR(
                    f"Missing required settings: {', '.join(missing_settings)}. "
                    "Set these in your .env file and try again."
                )
            )
            return

        account_name = f"Daraja {environment.capitalize()}"
        defaults = {
            "environment": environment,
            "type": account_type,
            "paybill_number": shortcode if account_type == "PAYBILL" else None,
            "till_number": shortcode if account_type == "BUY_GOODS" else None,
            "is_active": environment == "SANDBOX",  # Sandbox active by default; Production requires manual activation
            "authentication_credentials": {
                "customer_key": consumer_key,
                "customer_secret": consumer_secret,
                "pass_key": passkey,
            },
        }

        if dry_run:
            self.stdout.write(self.style.WARNING("[DRY RUN] Would create/update:"))
            self.stdout.write(f"  Name: {account_name}")
            for k, v in defaults.items():
                if k == "authentication_credentials":
                    self.stdout.write(f"  {k}: {{customer_key: *****, customer_secret: *****, pass_key: *****}}")
                else:
                    self.stdout.write(f"  {k}: {v}")
            return

        account, created = MpesaPaymentAccount.objects.update_or_create(
            name=account_name,
            defaults=defaults,
        )

        action = "Created" if created else "Updated"
        self.stdout.write(
            self.style.SUCCESS(
                f"{action} MpesaPaymentAccount: '{account.name}' "
                f"(env={account.environment}, is_active={account.is_active}, "
                f"shortcode={account.paybill_number or account.till_number})"
            )
        )

        if environment == "PRODUCTION":
            self.stdout.write(
                self.style.WARNING(
                    "Production account created with is_active=False. "
                    "Manually set is_active=True via Django Admin to enable live payments."
                )
            )
