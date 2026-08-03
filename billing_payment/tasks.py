from celery import shared_task
from django.utils import timezone
from datetime import timedelta
import logging

from billing_payment.models import InvoicePaymentTransaction, MpesaPaymentAccount
from billing_payment.gateways.daraja import DarajaGateway
from billing_payment.services.orchestrator import PaymentOrchestrator

logger = logging.getLogger(__name__)


@shared_task(name="billing_payment.reconcile_pending_payments")
def reconcile_pending_payments():
    """
    Periodic Celery task to reconcile InvoicePaymentTransactions stuck in PENDING state.
    
    This serves as a fallback when Safaricom's STK Push callback is delayed or dropped.
    For each PENDING transaction older than 10 minutes, the task queries Daraja's
    STK Push status API and delegates resolution to PaymentOrchestrator.
    
    PaymentOrchestrator handles all state transitions including subscription activation.
    """
    cutoff = timezone.now() - timedelta(minutes=10)
    pending_txs = (
        InvoicePaymentTransaction.objects
        .filter(status="PENDING", created_at__lt=cutoff)
        .select_related("invoice")
    )

    if not pending_txs.exists():
        logger.info("reconcile_pending_payments: No pending transactions to reconcile.")
        return "No pending payments to reconcile."

    from billing_payment.services.resolver import PaymentAccountResolver, PaymentConfigurationError
    try:
        mpesa_account = PaymentAccountResolver.get_active_account()
    except PaymentConfigurationError as config_err:
        logger.warning("reconcile_pending_payments: Configuration error: %s", config_err)
        return f"Configuration error: {config_err}"

    # DarajaGateway resolves is_live from settings.MPESA_ENVIRONMENT automatically
    gateway = DarajaGateway(mpesa_account)
    reconciled_count = 0

    for tx in pending_txs:
        checkout_req_id = tx.transaction_details.get("checkout_request_id")
        if not checkout_req_id:
            logger.warning(
                f"reconcile_pending_payments: Transaction {tx.transaction_id} has no checkout_request_id. Skipping."
            )
            continue

        try:
            result = gateway.query_payment_status(checkout_req_id)
            PaymentOrchestrator.resolve_transaction(checkout_req_id, result)
            reconciled_count += 1
            logger.info(
                f"reconcile_pending_payments: Resolved transaction {tx.transaction_id} "
                f"-> is_successful={result.is_successful}, code={result.result_code}"
            )
        except Exception as exc:
            logger.error(
                f"reconcile_pending_payments: Error processing transaction {tx.transaction_id}: {exc}",
                exc_info=True,
            )

    return f"Reconciled {reconciled_count} of {pending_txs.count()} pending transactions."
