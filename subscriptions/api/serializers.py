from rest_framework import serializers
from subscriptions.models import Subscription, SubscriptionPlan
from billing_payment.api.serializers import (
    BillingAddressSerializer,
    InvoiceSerializer,
    InvoicePaymentTransactionSerializer,
)
from rest_framework.exceptions import ValidationError


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"
        read_only_fields = ("id", "plan_id")


class SubscriptionSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source="plan.name", read_only=True)
    plan_id = serializers.CharField(source="plan.plan_id", read_only=True)
    invoice_details = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(source='is_currently_active', read_only=True)
    status = serializers.CharField(read_only=True)
    start_date = serializers.DateField(source="get_start_date", read_only=True)
    end_date = serializers.DateField(source="get_end_date", read_only=True)

    class Meta:
        model = Subscription
        fields = "__all__"
        read_only_fields = (
            "id",
            "user",
            "invoice",
            "start_date",
            "end_date",
            "is_active",
        )

    def get_invoice_details(self, obj):
        if obj.invoice:
            return InvoiceSerializer(obj.invoice).data
        return None


class AddSubscriptionSerializer(serializers.Serializer):
    subscription_details = serializers.JSONField()
    billing_address = serializers.JSONField()
    invoice_payment_transaction = serializers.JSONField()

    def validate_subscription_details(self, value):
        serializer = SubscriptionSerializer(data=value)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def validate_billing_address(self, value):
        serializer = BillingAddressSerializer(data=value)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def validate_invoice_payment_transaction(self, value):
        serializer = InvoicePaymentTransactionSerializer(data=value)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def create(self, validated_data):
        subscription_details = validated_data.pop("subscription_details")
        billing_address = validated_data.pop("billing_address")

        new_subscription = Subscription.objects.create(
            user=validated_data.get("user"),
            **subscription_details,
        )
        invoice = new_subscription.generate_invoice(billing_address=billing_address)

        invoice_payment_transaction = validated_data.pop("invoice_payment_transaction")
        invoice_payment_transaction_serializer = InvoicePaymentTransactionSerializer(
            data=invoice_payment_transaction
        )
        if not invoice_payment_transaction_serializer.is_valid():
            raise serializers.ValidationError(
                {
                    "invoice_payment_transaction": invoice_payment_transaction_serializer.errors
                }
            )
        else:
            try:
                invoice_payment_transaction = (
                    invoice_payment_transaction_serializer.save(invoice=invoice)
                )
            except ValidationError as e:
                raise serializers.ValidationError(
                    {"invoice_payment_transaction": e.detail}
                )
            except Exception as e:
                raise serializers.ValidationError(
                    {"invoice_payment_transaction": str(e)}
                )

        return new_subscription
