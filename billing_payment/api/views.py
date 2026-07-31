from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from utils.utils import handle_server_error
from .serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoicePaymentTransactionSerializer,
)
from billing_payment.models import (
    Invoice,
    InvoiceItem,
    InvoicePaymentTransaction,
)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.utils import timezone

from billing_payment.mpesa.utils import StkPushCallbackResponseParser

import logging
import json
from Resources.models import User

logger = logging.getLogger(__name__)


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = self.request.user

        if user_id:
            if str(user.id) != str(user_id) and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
                raise NotFound("The requested resource was not found.")
            return Invoice.objects.filter(
                user_from__id=user_id
            ) | Invoice.objects.filter(user_to__id=user_id)

        if user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin':
            return Invoice.objects.all()

        raise NotFound("The requested resource was not found.")

    def get_object(self):
        invoice_number = self.kwargs.get("invoice_number")

        if not invoice_number:
            raise NotFound("The requested resource was not found.")

        return self.get_queryset().get(
            invoice_number=invoice_number,
        )

    def list(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_results = paginator.paginate_queryset(
            self.get_queryset(), request, view=self
        )
        if paginated_results is not None:
            serializer = self.get_serializer(paginated_results, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data,
            )

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )

    def retrieve(self, request, *args, **kwargs):
        invoice = self.get_object()
        serializer = self.get_serializer(invoice)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = kwargs.get("user_id")
        if user_id:
            user = User.objects.get(id=user_id)
            invoice = serializer.save(
                from_user=user,
            )
        else:
            invoice = serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data=self.get_serializer(invoice).data,
        )

    def update(self, request, *args, **kwargs):
        invoice = self.get_object()
        serializer = self.get_serializer(invoice, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_invoice = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data=self.get_serializer(updated_invoice).data,
        )

    def partial_update(self, request, *args, **kwargs):
        invoice = self.get_object()
        serializer = self.get_serializer(invoice, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_invoice = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data=self.get_serializer(updated_invoice).data,
        )

    def destroy(self, request, *args, **kwargs):
        invoice = self.get_object()
        invoice.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={"message": "Invoice deleted successfully."},
        )

    def handle_exception(self, exc):
        if isinstance(exc, Invoice.DoesNotExist):
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "data": None,
                    "errors": {"detail": "Invoice not found."},
                },
            )

        # Handle other exceptions
        return handle_server_error(self.request, exc, settings.DEBUG)


class InvoiceItemViewSet(ModelViewSet):
    serializer_class = InvoiceItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        invoice_number = self.kwargs.get("invoice_number")
        user = self.request.user

        if not invoice_number:
            raise NotFound("The requested resource was not found.")

        try:
            invoice = Invoice.objects.get(invoice_number=invoice_number)
        except Invoice.DoesNotExist:
            raise NotFound("Invoice not found.")

        # Check ownership or admin status
        if invoice.user_from != user and invoice.user_to != user and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
            raise NotFound("The requested resource was not found.")

        return InvoiceItem.objects.filter(invoice__invoice_number=invoice_number)

    def get_object(self):
        invoice_number = self.kwargs.get("invoice_number")
        item_id = self.kwargs.get("item_id")
        user = self.request.user

        if not invoice_number or not item_id:
            raise NotFound("The requested resource was not found.")

        try:
            item = InvoiceItem.objects.get(invoice__invoice_number=invoice_number, id=item_id)
        except InvoiceItem.DoesNotExist:
            raise NotFound("Invoice item not found.")

        if item.invoice.user_from != user and item.invoice.user_to != user and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
            raise NotFound("The requested resource was not found.")

        return item

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )

    def retrieve(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data=self.get_serializer(item).data,
        )

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_item = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data=self.get_serializer(updated_item).data,
        )

    def partial_update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_item = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data=self.get_serializer(updated_item).data,
        )

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={"message": "Invoice item deleted successfully."},
        )

    def handle_exception(self, exc):
        if isinstance(exc, InvoiceItem.DoesNotExist):
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "data": None,
                    "errors": {"detail": "Invoice item not found."},
                },
            )

        if isinstance(exc, Invoice.DoesNotExist):
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "data": None,
                    "errors": {"detail": "Invoice not found."},
                },
            )

        # Handle other exceptions
        return handle_server_error(self.request, exc, settings.DEBUG)


class InvoicePaymentTransactionViewSet(ModelViewSet):
    serializer_class = InvoicePaymentTransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        invoice_number = self.kwargs.get("invoice_number")
        user = self.request.user

        if not invoice_number:
            raise NotFound("The requested resource was not found.")

        try:
            invoice = Invoice.objects.get(invoice_number=invoice_number)
        except Invoice.DoesNotExist:
            raise NotFound("Invoice not found.")

        if invoice.user_from != user and invoice.user_to != user and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
            raise NotFound("The requested resource was not found.")

        return InvoicePaymentTransaction.objects.filter(
            invoice__invoice_number=invoice_number
        )

    def get_object(self):
        invoice_number = self.kwargs.get("invoice_number")
        transaction_id = self.kwargs.get("transaction_id")
        user = self.request.user

        if not invoice_number or not transaction_id:
            raise NotFound("The requested resource was not found.")

        try:
            tx = InvoicePaymentTransaction.objects.get(
                invoice__invoice_number=invoice_number,
                transaction_id=transaction_id,
            )
        except InvoicePaymentTransaction.DoesNotExist:
            raise NotFound("Transaction not found.")

        if tx.invoice.user_from != user and tx.invoice.user_to != user and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
            raise NotFound("The requested resource was not found.")

        return tx

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )

    def retrieve(self, request, *args, **kwargs):
        transaction = self.get_object()
        serializer = self.get_serializer(transaction)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice_number = self.kwargs.get("invoice_number")
        invoice = Invoice.objects.get(invoice_number=invoice_number)
        transaction = serializer.save(invoice=invoice)

        return Response(
            status=status.HTTP_201_CREATED,
            data=self.get_serializer(transaction).data,
        )

    def update(self, request, *args, **kwargs):
        transaction = self.get_object()
        serializer = self.get_serializer(transaction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_transaction = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data=self.get_serializer(updated_transaction).data,
        )

    def partial_update(self, request, *args, **kwargs):
        transaction = self.get_object()
        serializer = self.get_serializer(transaction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_transaction = serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            data=self.get_serializer(updated_transaction).data,
        )

    def destroy(self, request, *args, **kwargs):
        transaction = self.get_object()
        transaction.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={"message": "Payment transaction deleted successfully."},
        )

    def handle_exception(self, exc):
        if isinstance(exc, InvoicePaymentTransaction.DoesNotExist):
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "data": None,
                    "errors": {"detail": "Payment transaction not found."},
                },
            )

        if isinstance(exc, Invoice.DoesNotExist):
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "data": None,
                    "errors": {"detail": "Invoice not found."},
                },
            )

        # Handle other exceptions
        return handle_server_error(self.request, exc, settings.DEBUG)


from rest_framework.permissions import AllowAny

@method_decorator(csrf_exempt, name="dispatch")
class MpesaStkPushCallBackUrl(APIView):
    # AllowAny is intentional: M-Pesa STK Push callbacks are server-to-server
    # webhook calls from Safaricom that do not carry JWT tokens. Authentication
    # relies on payload validation (CheckoutRequestID matching a known transaction).
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            print("STK Push Callback Data:", request.body)
            result = json.loads(request.body)
            result_parser = StkPushCallbackResponseParser(result)
            checkout_request_id = result_parser.get_checkout_request_id()
            invoice_payment_transaction = InvoicePaymentTransaction.objects.filter(
                transaction_details__checkout_request_id=checkout_request_id
            ).first()

            if not invoice_payment_transaction:
                logger.error(
                    f"Transaction not found for CheckoutRequestID: {checkout_request_id}"
                )
                return HttpResponse(status=200)

            # Idempotency check: Skip if transaction has already been processed
            if invoice_payment_transaction.status in ["COMPLETED", "FAILED"]:
                logger.info(
                    f"Transaction {checkout_request_id} already processed with status: {invoice_payment_transaction.status}"
                )
                return HttpResponse(status=200)

            if result_parser.is_successful():
                callback_amount = result_parser.get_amount()
                invoice_total = invoice_payment_transaction.invoice.total_amount

                # Payment amount validation
                if callback_amount is None or float(callback_amount) < float(invoice_total):
                    logger.error(
                        f"Payment validation failed for CheckoutRequestID {checkout_request_id}: "
                        f"Received {callback_amount}, expected {invoice_total}"
                    )
                    invoice_payment_transaction.status = "FAILED"
                else:
                    invoice_payment_transaction.status = "COMPLETED"
                    invoice_payment_transaction.transaction_date = (
                        result_parser.get_transaction_date()
                    )
                    invoice_payment_transaction.invoice.status = "PAID"
                    invoice_payment_transaction.invoice.paid_date = (
                        result_parser.get_transaction_date()
                    )
                    invoice_payment_transaction.invoice.save()

                    # Activate linked Subscription or SchoolSubscription
                    inv = invoice_payment_transaction.invoice
                    if hasattr(inv, 'subscription') and inv.subscription:
                        sub = inv.subscription
                        sub.status_state = "ACTIVE"
                        sub.is_active = True
                        sub.activated_at = timezone.now()
                        sub.start_date = timezone.now()
                        duration = sub.product_variant.duration_days if sub.product_variant else 30
                        sub.end_date = sub.start_date + timezone.timedelta(days=duration)
                        sub.save()

                        # Idempotently snapshot StudentSubjectSelection into SubscriptionSubject upon verified payment
                        from Resources.models import StudentSubjectSelection
                        from subscriptions.models import SubscriptionSubject
                        student_selections = StudentSubjectSelection.objects.filter(user=sub.user)
                        for sel in student_selections:
                            SubscriptionSubject.objects.get_or_create(subscription=sub, subject=sel.subject)

                    if hasattr(inv, 'school_subscription') and inv.school_subscription:
                        school_sub = inv.school_subscription
                        school_sub.is_active = True
                        school_sub.start_date = timezone.now()
                        duration = school_sub.product_variant.duration_days if school_sub.product_variant else 90
                        school_sub.end_date = school_sub.start_date + timezone.timedelta(days=duration)
                        school_sub.save()
            else:
                invoice_payment_transaction.status = "FAILED"

            transaction_details = invoice_payment_transaction.transaction_details or {}
            transaction_details.update(result_parser.get_result_data())
            invoice_payment_transaction.transaction_details = transaction_details
            invoice_payment_transaction.save()

            return HttpResponse(status=200)

        except Exception as e:
            logger.error(f"Error parsing STK Push callback data: {e}")
            return HttpResponse(status=200)

