import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from utils.utils import handle_server_error
from django.utils import timezone
from .serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoicePaymentTransactionSerializer,
)

from billing_payment.models import (
    Invoice,
    InvoiceItem,
    InvoicePaymentTransaction,
    MpesaPaymentAccount,
)
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from billing_payment.mpesa.utils import StkPushCallbackResponseParser

import logging

logger = logging.getLogger(__name__)


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        account_id = self.kwargs.get("account_id")
        user = self.request.user

        if account_id:
            return Invoice.objects.filter(account__account_id=account_id)

        if user.is_staff or user.is_superuser:
            return Invoice.objects.all()

        raise NotFound("The requested resource was not found.")

    def get_object(self):
        account_id = self.kwargs.get("account_id")
        invoice_number = self.kwargs.get("invoice_number")

        if not account_id or not invoice_number:
            raise NotFound("The requested resource was not found.")

        return Invoice.objects.get(
            account__account_id=account_id, invoice_number=invoice_number
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
        account_id = self.kwargs.get("account_id")
        invoice_number = self.kwargs.get("invoice_number")

        if account_id and invoice_number:
            return InvoiceItem.objects.filter(
                invoice__account__account_id=account_id,
                invoice__invoice_number=invoice_number,
            )

        raise NotFound("The requested resource was not found.")

    def get_object(self):
        account_id = self.kwargs.get("account_id")
        invoice_number = self.kwargs.get("invoice_number")
        item_id = self.kwargs.get("item_id")

        if not account_id or not invoice_number or not item_id:
            raise NotFound("The requested resource was not found.")

        return InvoiceItem.objects.get(
            invoice__account__account_id=account_id,
            invoice__invoice_number=invoice_number,
            id=item_id,
        )

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
        account_id = self.kwargs.get("account_id")
        invoice_number = self.kwargs.get("invoice_number")

        if account_id and invoice_number:
            return InvoicePaymentTransaction.objects.filter(
                invoice__account__account_id=account_id,
                invoice__invoice_number=invoice_number,
            )

        raise NotFound("The requested resource was not found.")

    def get_object(self):
        account_id = self.kwargs.get("account_id")
        invoice_number = self.kwargs.get("invoice_number")
        transaction_id = self.kwargs.get("transaction_id")

        if not account_id or not invoice_number or not transaction_id:
            raise NotFound("The requested resource was not found.")

        return InvoicePaymentTransaction.objects.get(
            invoice__account__account_id=account_id,
            invoice__invoice_number=invoice_number,
            id=transaction_id,
        )

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


@method_decorator(csrf_exempt, name="dispatch")
class MpesaStkPushCallBackUrl(APIView):

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

            if result_parser.is_successful():
                invoice_payment_transaction.status = "COMPLETED"
                invoice_payment_transaction.transaction_date = (
                    result_parser.get_transaction_date()
                )
                invoice_payment_transaction.invoice.status = "PAID"
                invoice_payment_transaction.invoice.paid_date = (
                    result_parser.get_transaction_date()
                )
                invoice_payment_transaction.invoice.save()
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

