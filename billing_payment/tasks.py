from celery import shared_task
from django.utils import timezone
from datetime import timedelta
import logging
from billing_payment.models import InvoicePaymentTransaction, MpesaPaymentAccount
from billing_payment.mpesa.utils import MpesaApi

logger = logging.getLogger(__name__)

@shared_task(name="billing_payment.reconcile_pending_payments")
def reconcile_pending_payments():
    """
    Periodic task to poll status of transactions left PENDING for more than 10 minutes.
    """
    cutoff = timezone.now() - timedelta(minutes=10)
    pending_txs = InvoicePaymentTransaction.objects.filter(
        status="PENDING",
        created_at__lt=cutoff
    ).select_related("invoice")

    if not pending_txs.exists():
        logger.info("No pending payments to reconcile.")
        return "No pending payments to reconcile."

    mpesa_account = MpesaPaymentAccount.objects.first()
    if not mpesa_account:
        logger.warning("No MpesaPaymentAccount found for payment reconciliation.")
        return "No MpesaPaymentAccount configured."

    mpesa_api = MpesaApi(mpesa_payment_account=mpesa_account)
    reconciled_count = 0

    for tx in pending_txs:
        checkout_req_id = tx.transaction_details.get("checkout_request_id")
        if not checkout_req_id:
            logger.warning(f"Transaction {tx.transaction_id} missing checkout_request_id.")
            continue

        try:
            status_res = mpesa_api.query_stk_push_status(checkout_req_id)
            if status_res.get("is_successful"):
                tx.status = "COMPLETED"
                tx.transaction_date = timezone.now()
                tx.invoice.status = "PAID"
                tx.invoice.paid_date = timezone.now()
                tx.invoice.save()
                logger.info(f"Reconciled transaction {tx.transaction_id} -> COMPLETED")
            else:
                result_code = status_res.get("result_code")
                if result_code and str(result_code) != "0":
                    tx.status = "FAILED"
                    logger.info(f"Reconciled transaction {tx.transaction_id} -> FAILED (ResultCode: {result_code})")

            tx.transaction_details["reconciled_at"] = timezone.now().isoformat()
            tx.save()
            reconciled_count += 1
        except Exception as e:
            logger.error(f"Error querying status for transaction {tx.transaction_id}: {e}")

    return f"Reconciled {reconciled_count} pending transactions."
