from rest_framework import serializers
from subscriptions.models import Subscription, SubscriptionPlan, Product, ProductVariant, AccessScope
from billing_payment.api.serializers import (
    BillingAddressSerializer,
    InvoiceSerializer,
    InvoicePaymentTransactionSerializer,
)
from rest_framework.exceptions import ValidationError


class AccessScopeSerializer(serializers.ModelSerializer):
    grade_name = serializers.CharField(source="grade.name", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)

    class Meta:
        model = AccessScope
        fields = "__all__"


class ProductVariantSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_audience = serializers.CharField(source="product.audience", read_only=True)
    access_scopes = AccessScopeSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"
        read_only_fields = ("id", "plan_id")


class SubscriptionSerializer(serializers.ModelSerializer):
    plan_name = serializers.SerializerMethodField()
    plan_id = serializers.SerializerMethodField()
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

    def get_plan_name(self, obj):
        if obj.product_variant:
            return obj.product_variant.name
        if obj.plan:
            return obj.plan.name
        return "Unknown"

    def get_plan_id(self, obj):
        if obj.product_variant:
            return obj.product_variant.slug
        if obj.plan:
            return obj.plan.plan_id
        return "unknown"

    def get_invoice_details(self, obj):
        if obj.invoice:
            return InvoiceSerializer(obj.invoice).data
        return None


class AddSubscriptionSerializer(serializers.Serializer):
    subscription_details = serializers.JSONField()
    billing_address = serializers.JSONField()
    invoice_payment_transaction = serializers.JSONField()

    def validate_subscription_details(self, value):
        return value

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

        plan_id = subscription_details.get("plan")
        product_variant_id = subscription_details.get("product_variant") or subscription_details.get("product_variant_id")
        plan_obj = None
        variant_obj = None

        if product_variant_id:
            try:
                variant_obj = ProductVariant.objects.get(id=product_variant_id)
            except (ProductVariant.DoesNotExist, ValidationError):
                variant_obj = ProductVariant.objects.filter(slug=product_variant_id).first()

        if not variant_obj and plan_id:
            try:
                plan_obj = SubscriptionPlan.objects.get(id=plan_id)
            except (SubscriptionPlan.DoesNotExist, ValueError):
                plan_obj = SubscriptionPlan.objects.filter(plan_id=plan_id).first()

        new_subscription = Subscription.objects.create(
            user=validated_data.get("user"),
            plan=plan_obj,
            product_variant=variant_obj,
            status_state="PENDING_PAYMENT",
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

