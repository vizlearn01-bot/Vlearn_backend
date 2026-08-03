from django.apps import AppConfig


class SubscriptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscriptions'

    def ready(self):
        """Register domain action handlers with the PaymentActionRegistry on app startup."""
        from billing_payment.services.actions import PaymentActionRegistry
        from subscriptions.services.actions import SubscriptionActionHandler
        PaymentActionRegistry.register('SUBSCRIPTION', SubscriptionActionHandler())
