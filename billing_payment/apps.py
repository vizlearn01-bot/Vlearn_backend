from django.apps import AppConfig


class BillingPaymentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing_payment'

    def ready(self):
        """Register Django system checks for payment configuration validation."""
        import billing_payment.checks  # noqa: F401 — registers check functions via @register decorator
