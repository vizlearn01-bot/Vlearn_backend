from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
import logging

if TYPE_CHECKING:
    from billing_payment.models import Invoice, InvoicePaymentTransaction

logger = logging.getLogger(__name__)


class NormalizedPaymentResult:  # Forward declaration for type hints without circular import
    pass


class BasePaymentActionHandler(ABC):
    """
    Abstract base class for domain-specific payment action handlers.
    
    Implementors:
        - SubscriptionActionHandler (subscriptions app)
        - MarketplaceActionHandler (future marketplace app)
        - DigitalResourceHandler (future resources app)
    """

    @abstractmethod
    def handle_payment_completed(
        self,
        invoice: "Invoice",
        transaction: "InvoicePaymentTransaction",
        result: "NormalizedPaymentResult",
    ) -> bool:
        """Execute business fulfilment after payment confirmation. Return True on success."""
        pass

    @abstractmethod
    def handle_payment_failed(
        self,
        invoice: "Invoice",
        transaction: "InvoicePaymentTransaction",
        result: "NormalizedPaymentResult",
    ) -> None:
        """Execute cleanup / cancellation on explicit payment failure."""
        pass


class PaymentActionRegistry:
    """
    Central registry that dispatches payment lifecycle events to registered domain handlers.
    
    Domain handlers are registered during application startup (in AppConfig.ready()).
    The registry itself has no dependency on any business domain.
    
    Usage:
        PaymentActionRegistry.register('SUBSCRIPTION', SubscriptionActionHandler())
        PaymentActionRegistry.dispatch_completed(invoice, transaction, result)
    """

    _handlers: dict = {}

    @classmethod
    def register(cls, action_type: str, handler: BasePaymentActionHandler) -> None:
        """Register a handler for a given action type."""
        cls._handlers[action_type] = handler
        logger.info(f"Registered PaymentActionHandler for action_type='{action_type}': {handler.__class__.__name__}")

    @classmethod
    def _resolve_action_type(cls, invoice: "Invoice") -> str:
        """Determine action type from invoice metadata or related objects."""
        # Prefer explicit action_type in invoice.details metadata
        if invoice.details and isinstance(invoice.details, dict):
            action_type = invoice.details.get("action_type")
            if action_type:
                return action_type
        # Fallback: introspect related subscription objects
        if hasattr(invoice, 'subscription') and invoice.subscription:
            return "SUBSCRIPTION"
        if hasattr(invoice, 'school_subscription') and invoice.school_subscription:
            return "SUBSCRIPTION"
        return "GENERIC"

    @classmethod
    def dispatch_completed(
        cls,
        invoice: "Invoice",
        transaction: "InvoicePaymentTransaction",
        result: "NormalizedPaymentResult",
    ) -> bool:
        """Dispatch a PaymentCompletedEvent to the appropriate domain handler."""
        action_type = cls._resolve_action_type(invoice)
        handler = cls._handlers.get(action_type)
        if not handler:
            logger.warning(
                f"No PaymentActionHandler registered for action_type='{action_type}'. "
                f"Invoice {invoice.invoice_number} payment was confirmed but no business action was dispatched."
            )
            return False
        try:
            return handler.handle_payment_completed(invoice, transaction, result)
        except Exception as exc:
            logger.error(
                f"PaymentActionHandler '{handler.__class__.__name__}' failed for "
                f"invoice {invoice.invoice_number}: {exc}",
                exc_info=True,
            )
            return False

    @classmethod
    def dispatch_failed(
        cls,
        invoice: "Invoice",
        transaction: "InvoicePaymentTransaction",
        result: "NormalizedPaymentResult",
    ) -> None:
        """Dispatch a PaymentFailedEvent to the appropriate domain handler."""
        action_type = cls._resolve_action_type(invoice)
        handler = cls._handlers.get(action_type)
        if not handler:
            return
        try:
            handler.handle_payment_failed(invoice, transaction, result)
        except Exception as exc:
            logger.error(
                f"PaymentActionHandler.handle_payment_failed failed for invoice {invoice.invoice_number}: {exc}",
                exc_info=True,
            )
