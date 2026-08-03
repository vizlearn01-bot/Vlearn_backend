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


def user_can_access_invoice(user, invoice) -> bool:
    """
    Check if a user is authorized to access an invoice.
    Allowed if:
    - User is staff, superuser, or platform_admin
    - User matches invoice.user_to or invoice.user_from
    - User is the owner of the linked Subscription
    - User is the owner or admin of the school for the linked SchoolSubscription
    - User's email matches the email recorded in invoice.invoice_to
    """
    if not user or not user.is_authenticated:
        return False
    if user.is_staff or user.is_superuser or getattr(user, "role", None) == "platform_admin":
        return True
    if invoice.user_to == user or invoice.user_from == user:
        return True
    if hasattr(invoice, "subscription") and invoice.subscription and invoice.subscription.user == user:
        return True
    if hasattr(invoice, "school_subscription") and invoice.school_subscription:
        school = invoice.school_subscription.school
        if school and (
            school.owner == user
            or user.memberships.filter(
                school=school, role="school_admin", state__in=["ACCEPTED", "ACTIVE"]
            ).exists()
        ):
            return True
    if (
        isinstance(invoice.invoice_to, dict)
        and invoice.invoice_to.get("email")
        and user.email
    ):
        if invoice.invoice_to.get("email").strip().lower() == user.email.strip().lower():
            return True
    return False


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
        if not user_can_access_invoice(user, invoice):
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

        if not user_can_access_invoice(user, item.invoice):
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

        if not user_can_access_invoice(user, invoice):
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

        if not user_can_access_invoice(user, tx.invoice):
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
from billing_payment.gateways.daraja import DarajaGateway
from billing_payment.services.orchestrator import PaymentOrchestrator
from billing_payment.models import MpesaPaymentAccount

class InvoicePaymentStatusView(APIView):
    """
    Lightweight endpoint for frontend payment status polling.
    
    Returns the current payment and subscription activation status for a given invoice.
    Used by the React frontend to show real-time payment confirmation.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, invoice_number):
        user = request.user
        try:
            invoice = Invoice.objects.prefetch_related('payment_transactions').get(
                invoice_number=invoice_number
            )
        except Invoice.DoesNotExist:
            return Response({'error': 'Invoice not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Authorization: invoice owner (user_to/user_from), linked subscription/school owner, or admin
        if not user_can_access_invoice(user, invoice):
            return Response({'error': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)

        latest_tx = invoice.payment_transactions.first()
        tx_status = latest_tx.status if latest_tx else None
        
        # Check subscription activation status
        is_active = False
        if hasattr(invoice, 'subscription') and invoice.subscription:
            is_active = invoice.subscription.is_active
        elif hasattr(invoice, 'school_subscription') and invoice.school_subscription:
            is_active = invoice.school_subscription.is_active

        return Response({
            'invoice_number': invoice.invoice_number,
            'invoice_status': invoice.status,
            'transaction_status': tx_status,
            'is_active': is_active,
        }, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class MpesaStkPushCallBackUrl(APIView):
    """
    Receives M-Pesa STK Push callback notifications from Safaricom Daraja.
    
    Security:
        - Validates request via DarajaGateway.validate_webhook (secret token + IP whitelist)
        - AllowAny permission is intentional: callbacks arrive from Safaricom servers
          without JWT tokens. Security is enforced at the payload/IP level.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            # --- Gateway Validation ---
            from billing_payment.services.resolver import PaymentAccountResolver, PaymentConfigurationError
            try:
                mpesa_account = PaymentAccountResolver.get_active_account()
            except PaymentConfigurationError as config_err:
                logger.error("MpesaStkPushCallBackUrl: Payment account configuration error: %s", config_err)
                return HttpResponse(status=200)  # Always 200 to Safaricom

            gateway = DarajaGateway(mpesa_account)
            
            headers = dict(request.headers)
            raw_body = request.body
            params = request.query_params.dict()
            
            if not gateway.validate_webhook(headers, raw_body, params):
                logger.warning(
                    f"MpesaStkPushCallBackUrl: Webhook validation failed. "
                    f"IP={request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', 'unknown'))}"
                )
                # Return 200 to prevent Safaricom retry flood on validation failures
                return HttpResponse(status=200)

            # --- Parse Payload ---
            raw_payload = json.loads(raw_body)
            result = gateway.parse_webhook_payload(raw_payload)

            checkout_request_id = result.provider_transaction_id
            if not checkout_request_id:
                logger.error("MpesaStkPushCallBackUrl: Missing provider_transaction_id in parsed payload.")
                return HttpResponse(status=200)

            # --- Delegate to Orchestrator ---
            PaymentOrchestrator.resolve_transaction(checkout_request_id, result)

            return HttpResponse(status=200)

        except Exception as exc:
            logger.error(f"MpesaStkPushCallBackUrl: Unhandled exception: {exc}", exc_info=True)
            return HttpResponse(status=200)

