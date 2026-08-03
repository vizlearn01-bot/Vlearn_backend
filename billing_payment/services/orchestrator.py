import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from billing_payment.models import Invoice, InvoicePaymentTransaction, FinancialLedgerEntry
from billing_payment.services.actions import PaymentActionRegistry

logger = logging.getLogger(__name__)


class PaymentOrchestrator:
    """
    Single source of truth for all payment lifecycle transitions.
    
    Responsibilities:
        - Atomically transitions InvoicePaymentTransaction and Invoice states
        - Posts immutable FinancialLedgerEntry records on successful payment
        - Dispatches PaymentCompletedEvent or PaymentFailedEvent to PaymentActionRegistry
        - Enforces idempotency: safe to call multiple times for the same transaction
    
    This class is intentionally domain-agnostic. It has no knowledge of
    subscriptions, school licenses, marketplace orders, or any other business domain.
    Business fulfilment is delegated entirely to PaymentActionRegistry.
    """

    @classmethod
    def resolve_transaction(
        cls,
        checkout_request_id: str,
        result,  # NormalizedPaymentResult from gateways.base
    ) -> bool:
        """
        Resolve a payment transaction based on a gateway result.
        
        Handles both successful and failed payment outcomes.
        Idempotent: safe to call multiple times for the same checkout_request_id.
        
        Args:
            checkout_request_id: The provider's unique transaction identifier
            result: NormalizedPaymentResult from the gateway
            
        Returns:
            True if resolution was applied, False if already resolved (idempotent skip)
        """
        if result.is_successful:
            return cls._complete_transaction(checkout_request_id, result)
        else:
            return cls._fail_transaction(checkout_request_id, result)

    @classmethod
    def _complete_transaction(cls, checkout_request_id: str, result) -> bool:
        """Mark transaction as COMPLETED and trigger business fulfilment."""
        with transaction.atomic():
            # Row-level lock to prevent concurrent processing
            tx = (
                InvoicePaymentTransaction.objects
                .select_for_update()
                .filter(transaction_details__checkout_request_id=checkout_request_id)
                .select_related("invoice")
                .first()
            )

            if not tx:
                logger.error(
                    f"PaymentOrchestrator: No transaction found for CheckoutRequestID={checkout_request_id}"
                )
                return False

            # Idempotency guard
            if tx.status in ("COMPLETED", "FAILED"):
                logger.info(
                    f"PaymentOrchestrator: Transaction {tx.transaction_id} already in terminal state "
                    f"'{tx.status}'. Skipping resolution."
                )
                return False

            # Amount validation
            invoice_total = tx.invoice.total_amount
            amount_paid = result.amount_paid
            if amount_paid is not None and float(amount_paid) < float(invoice_total):
                logger.error(
                    f"PaymentOrchestrator: Amount mismatch for tx {tx.transaction_id}. "
                    f"Paid={amount_paid}, Expected={invoice_total}. Marking FAILED."
                )
                tx.status = "FAILED"
                tx.transaction_details.update({"orchestrator_fail_reason": "amount_mismatch"})
                tx.save(update_fields=["status", "transaction_details", "updated_at"])
                return False

            # Mark transaction COMPLETED
            tx.status = "COMPLETED"
            if result.paid_at:
                tx.transaction_date = timezone.datetime.strptime(result.paid_at, "%Y-%m-%d %H:%M:%S") if isinstance(result.paid_at, str) else result.paid_at
            else:
                tx.transaction_date = timezone.now()
            
            # Store receipt metadata
            details = tx.transaction_details or {}
            details.update(result.raw_payload or {})
            tx.transaction_details = details
            tx.save(update_fields=["status", "transaction_date", "transaction_details", "updated_at"])

            # Mark invoice PAID
            inv = Invoice.objects.select_for_update().get(pk=tx.invoice.pk)
            inv.status = "PAID"
            inv.paid_date = tx.transaction_date
            inv.save(update_fields=["status", "paid_date", "updated_at"])

            # Write immutable ledger entry
            FinancialLedgerEntry.objects.create(
                invoice=inv,
                transaction=tx,
                entry_type="PAYMENT",
                amount=amount_paid or invoice_total,
                currency="KES",
                description=f"M-Pesa payment received. Receipt: {result.receipt_number or 'N/A'}",
                metadata={
                    "receipt_number": result.receipt_number,
                    "phone_number": result.phone_number,
                    "provider_transaction_id": result.provider_transaction_id,
                    "result_code": result.result_code,
                },
            )

            logger.info(
                f"PaymentOrchestrator: Transaction {tx.transaction_id} COMPLETED. "
                f"Invoice {inv.invoice_number} marked PAID. Dispatching action registry."
            )

        # Dispatch outside the atomic block to avoid holding the row lock during
        # potentially slow domain handler operations
        PaymentActionRegistry.dispatch_completed(inv, tx, result)
        return True

    @classmethod
    def _fail_transaction(cls, checkout_request_id: str, result) -> bool:
        """Mark transaction as FAILED and trigger domain cleanup."""
        with transaction.atomic():
            tx = (
                InvoicePaymentTransaction.objects
                .select_for_update()
                .filter(transaction_details__checkout_request_id=checkout_request_id)
                .select_related("invoice")
                .first()
            )

            if not tx:
                logger.error(
                    f"PaymentOrchestrator: No transaction found for CheckoutRequestID={checkout_request_id} during failure handling."
                )
                return False

            if tx.status in ("COMPLETED", "FAILED"):
                logger.info(
                    f"PaymentOrchestrator: Transaction {tx.transaction_id} already terminal. Skipping."
                )
                return False

            tx.status = "FAILED"
            details = tx.transaction_details or {}
            details.update(result.raw_payload or {})
            tx.transaction_details = details
            tx.save(update_fields=["status", "transaction_details", "updated_at"])

            inv = Invoice.objects.select_for_update().get(pk=tx.invoice.pk)
            inv.status = "CANCELLED"
            inv.save(update_fields=["status", "updated_at"])

            logger.info(
                f"PaymentOrchestrator: Transaction {tx.transaction_id} FAILED (code={result.result_code}). "
                f"Invoice {inv.invoice_number} marked CANCELLED."
            )

        PaymentActionRegistry.dispatch_failed(inv, tx, result)
        return True
