import logging
from datetime import timedelta
from django.utils import timezone
from billing_payment.services.actions import BasePaymentActionHandler

logger = logging.getLogger(__name__)


class SubscriptionActionHandler(BasePaymentActionHandler):
    """
    Domain action handler for subscription-based payments.
    
    Registered with PaymentActionRegistry under the 'SUBSCRIPTION' action type.
    Activated after PaymentOrchestrator confirms payment via MpesaStkPushCallBackUrl
    or reconcile_pending_payments.
    
    Handles:
        - Individual student/teacher Subscription activation
        - Institutional SchoolSubscription activation
        - Subscription cancellation on payment failure
    """

    def handle_payment_completed(self, invoice, transaction, result) -> bool:
        """
        Activate the subscription linked to this invoice.
        Returns True if a subscription was activated, False otherwise.
        """
        now = timezone.now()
        activated = False

        # --- Individual Subscription (Student or Teacher) ---
        # Note: Subscription has a OneToOneField to Invoice via related_name='subscription'
        try:
            sub = getattr(invoice, 'subscription', None)
            if sub is not None:
                duration_days = (
                    sub.product_variant.duration_days if sub.product_variant
                    else (sub.plan.duration_days if sub.plan else 30)
                )
                sub.status_state = "ACTIVE"
                sub.is_active = True
                sub.activated_at = now
                sub.start_date = now
                sub.end_date = now + timedelta(days=duration_days)
                sub.save(update_fields=['status_state', 'is_active', 'activated_at', 'start_date', 'end_date'])
                logger.info(
                    f"SubscriptionActionHandler: Activated individual subscription {sub.id} "
                    f"for user {sub.user.username} (duration={duration_days}d)"
                )

                # Snapshot StudentSubjectSelection into SubscriptionSubject upon verified payment
                try:
                    from Resources.models import StudentSubjectSelection
                    from subscriptions.models import SubscriptionSubject
                    student_selections = StudentSubjectSelection.objects.filter(user=sub.user)
                    for sel in student_selections:
                        SubscriptionSubject.objects.get_or_create(subscription=sub, subject=sel.subject)
                    logger.info(f"SubscriptionActionHandler: Snapshotted {student_selections.count()} subjects for sub {sub.id}")
                except Exception as e:
                    logger.warning(f"SubscriptionActionHandler: Subject snapshot failed for sub {sub.id}: {e}")

                activated = True
        except Exception as e:
            logger.error(f"SubscriptionActionHandler: Error activating individual subscription for invoice {invoice.invoice_number}: {e}", exc_info=True)

        # --- School Subscription ---
        try:
            school_sub = getattr(invoice, 'school_subscription', None)
            if school_sub is not None:
                duration_days = (
                    school_sub.product_variant.duration_days if school_sub.product_variant
                    else 90
                )
                school_sub.is_active = True
                school_sub.start_date = now
                school_sub.end_date = now + timedelta(days=duration_days)
                school_sub.save(update_fields=['is_active', 'start_date', 'end_date'])
                logger.info(
                    f"SubscriptionActionHandler: Activated SchoolSubscription {school_sub.id} "
                    f"for school {school_sub.school.name} (duration={duration_days}d)"
                )
                activated = True
        except Exception as e:
            logger.error(f"SubscriptionActionHandler: Error activating school subscription for invoice {invoice.invoice_number}: {e}", exc_info=True)

        return activated

    def handle_payment_failed(self, invoice, transaction, result) -> None:
        """
        Cancel pending subscription linked to this invoice on confirmed payment failure.
        """
        # Cancel individual subscription
        try:
            sub = getattr(invoice, 'subscription', None)
            if sub is not None and sub.status_state == "PENDING_PAYMENT":
                sub.status_state = "CANCELLED"
                sub.is_active = False
                sub.cancelled_at = timezone.now()
                sub.save(update_fields=['status_state', 'is_active', 'cancelled_at'])
                logger.info(f"SubscriptionActionHandler: Cancelled pending subscription {sub.id} (payment failed)")
        except Exception as e:
            logger.error(f"SubscriptionActionHandler: Error cancelling subscription for invoice {invoice.invoice_number}: {e}", exc_info=True)

        # Cancel school subscription
        try:
            school_sub = getattr(invoice, 'school_subscription', None)
            if school_sub is not None and not school_sub.is_active:
                # No formal CANCELLED state on SchoolSubscription — just log
                logger.info(f"SubscriptionActionHandler: School subscription {school_sub.id} remains inactive (payment failed)")
        except Exception as e:
            logger.error(f"SubscriptionActionHandler: Error handling failed school subscription for invoice {invoice.invoice_number}: {e}", exc_info=True)
