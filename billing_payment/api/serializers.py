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
        from billing_payment.gateways.daraja import DarajaGateway
        from billing_payment.gateways.base import PaymentInitiationRequest
        from billing_payment.utils.phone import normalize_phone_number
        from billing_payment.models import MpesaPaymentAccount
        
        transaction = super().create(validated_data)
        
        if transaction.payment_method == "MPESA":
            from billing_payment.services.resolver import PaymentAccountResolver, PaymentConfigurationError
            try:
                mpesa_account = PaymentAccountResolver.get_active_account()
            except PaymentConfigurationError as config_err:
                transaction.status = "FAILED"
                transaction.save(update_fields=["status", "updated_at"])
                raise ValidationError({"non_field_errors": str(config_err)})
            
            gateway = DarajaGateway(mpesa_account)
            raw_amount = transaction.invoice.total_amount if transaction.invoice else transaction.amount
            transaction.amount = raw_amount
            
            raw_phone = transaction.payment_details.get("mpesa_phone_number", "")
            try:
                normalized_phone = normalize_phone_number(raw_phone)
            except ValueError as e:
                raise ValidationError({"payment_details": {"mpesa_phone_number": str(e)}})
            
            from billing_payment.utils.config import get_mpesa_callback_url, build_secure_callback_url
            account_ref = getattr(settings, 'MPESA_ACCOUNT_REFERENCE', 'VizLearn')
            base_callback_url = get_mpesa_callback_url()
            callback_url = build_secure_callback_url(base_callback_url)
            
            pay_request = PaymentInitiationRequest(
                amount=raw_amount,
                phone_number=normalized_phone,
                account_reference=account_ref,
                transaction_description=f"Payment for Invoice {transaction.invoice.invoice_number}",
                callback_url=callback_url,
            )
            
            gateway_response = gateway.initiate_payment(pay_request)
            
            tx_details = transaction.transaction_details or {}
            tx_details.update(gateway_response.raw_response)
            if gateway_response.is_successful:
                tx_details['checkout_request_id'] = gateway_response.provider_transaction_id
                tx_details['merchant_request_id'] = gateway_response.provider_reference
            transaction.transaction_details = tx_details
            
            if not gateway_response.is_successful:
                transaction.status = "FAILED"
                error_code = gateway_response.raw_response.get("error_code", "")
                transaction.save(update_fields=["status", "amount", "transaction_details", "updated_at"])
                if error_code == "400.002.02":
                    raise ValidationError(
                        {"payment_details": {"mpesa_phone_number": "Invalid phone number"}}
                    )
            else:
                transaction.save(update_fields=["amount", "transaction_details", "updated_at"])
        
        return transaction
