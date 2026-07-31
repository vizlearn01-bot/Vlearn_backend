from rest_framework import serializers
from billing_payment.models import (
    Invoice,
    InvoiceItem,
    InvoicePaymentTransaction,
    MpesaPaymentAccount,
)
from rest_framework.exceptions import ValidationError
from billing_payment.mpesa.serializers import MpesaPaymentDetailsSerializer
from billing_payment.mpesa.utils import MpesaApi
from django.conf import settings


class InvoiceItemSerializer(serializers.ModelSerializer):
    item_total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = InvoiceItem
        fields = "__all__"


class BillingAddressSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone_number = serializers.CharField(
        max_length=20, required=False, allow_blank=True
    )
    city = serializers.CharField(max_length=100)
    street_address = serializers.CharField(
        max_length=100, required=False, allow_blank=True
    )
    postal_code = serializers.CharField(max_length=20, required=False, allow_blank=True)
    country = serializers.CharField(max_length=100, required=False, allow_blank=True)


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_from = serializers.JSONField()
    invoice_to = serializers.JSONField()
    invoice_items = InvoiceItemSerializer(many=True, read_only=True)
    total_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    status_display = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Invoice
        fields = "__all__"
        read_only_fields = ("invoice_number", "created_at", "updated_at")

    def validate_invoice_from(self, value):
        serializer = BillingAddressSerializer(data=value)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def validate_invoice_to(self, value):
        serializer = BillingAddressSerializer(data=value)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class InvoicePaymentTransactionSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_details = serializers.JSONField()

    class Meta:
        model = InvoicePaymentTransaction
        fields = "__all__"
        read_only_fields = ("transaction_id", "created_at", "updated_at", "invoice")

    def validate_amount(self, value):
        if value <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return value

    def validate(self, attrs):
        payment_method = attrs.get("payment_method")
        payment_details = attrs.get("payment_details")
        if payment_method == "MPESA":
            payment_details_serializer = MpesaPaymentDetailsSerializer(
                data=payment_details
            )
            if not payment_details_serializer.is_valid():
                raise ValidationError(
                    {"payment_details": payment_details_serializer.errors}
                )

        return super().validate(attrs)

    def create(self, validated_data):
        transaction = super().create(validated_data)
        if transaction.payment_method == "MPESA":
            mpesa_payment_account = MpesaPaymentAccount.objects.first()
            mpesa_api = MpesaApi(mpesa_payment_account, is_live=True)
            stk_amount = transaction.invoice.total_amount if transaction.invoice else transaction.amount
            transaction.amount = stk_amount
            account_ref = getattr(settings, 'MPESA_ACCOUNT_REFERENCE', 'VizLearn')
            stk_response = mpesa_api.initiate_stk_push(
                amount=stk_amount,
                phone_number=transaction.payment_details.get("mpesa_phone_number"),
                account_reference=account_ref,
                transaction_description="Payment for Invoice "
                + transaction.invoice.invoice_number,
            )
            print("STK Push Response:", stk_response)
            transaction_details = transaction.transaction_details or {}
            transaction_details.update(stk_response)
            transaction.transaction_details = transaction_details
            transaction.save()
            is_successful = stk_response.get("is_successful", False)
            if is_successful == False:
                transaction.status = "FAILED"
                if stk_response.get("error_code") == "400.002.02":
                    raise ValidationError(
                        {
                            "payment_details": {
                                "mpesa_phone_number": "Invalid phone number"
                            }
                        }
                    )

        return transaction
