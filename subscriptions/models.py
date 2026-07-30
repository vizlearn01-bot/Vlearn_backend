import uuid
from django.db import models
from billing_payment.models import Invoice, InvoiceItem
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Product(models.Model):
    AUDIENCE_CHOICES = (
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
        ("SCHOOL", "School"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    audience = models.CharField(max_length=20, choices=AUDIENCE_CHOICES)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.get_audience_display()})"


class ProductVariant(models.Model):
    DURATION_CHOICES = (
        ("MONTHLY", "Monthly"),
        ("TERM", "Term"),
        ("ANNUAL", "Annual"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="variants")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    duration_type = models.CharField(max_length=20, choices=DURATION_CHOICES)
    duration_days = models.PositiveIntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in KES")
    currency = models.CharField(max_length=3, default="KES")
    is_active = models.BooleanField(default=True)
    effective_from = models.DateTimeField(default=timezone.now)
    effective_until = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.name} ({self.price} KES)"


class AccessScope(models.Model):
    SCOPE_TYPE_CHOICES = (
        ("PLATFORM", "Platform Wide"),
        ("GRADE", "Grade / Form Specific"),
        ("SUBJECT", "Subject Specific"),
        ("FEATURE", "Feature Specific"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="access_scopes")
    scope_type = models.CharField(max_length=20, choices=SCOPE_TYPE_CHOICES)
    grade = models.ForeignKey("curriculum.Grade", on_delete=models.PROTECT, null=True, blank=True, related_name="access_scopes")
    subject = models.ForeignKey("curriculum.Subject", on_delete=models.PROTECT, null=True, blank=True, related_name="access_scopes")
    feature_key = models.CharField(max_length=100, null=True, blank=True, help_text="Feature flag key e.g. premium_simulations")

    def __str__(self):
        if self.scope_type == "PLATFORM":
            return f"{self.product_variant.name} -> Platform Wide"
        elif self.scope_type == "GRADE":
            return f"{self.product_variant.name} -> Grade: {self.grade}"
        elif self.scope_type == "SUBJECT":
            return f"{self.product_variant.name} -> Subject: {self.subject}"
        else:
            return f"{self.product_variant.name} -> Feature: {self.feature_key}"


class SubscriptionPlan(models.Model):
    plan_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField(help_text="Duration in days")
    details = models.JSONField(
        default=dict,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Subscription(models.Model):
    STATUS_STATE_CHOICES = (
        ("PENDING_PAYMENT", "Pending Payment"),
        ("ACTIVE", "Active"),
        ("EXPIRED", "Expired"),
        ("CANCELLED", "Cancelled"),
    )
    user = models.ForeignKey(
        "Resources.User", on_delete=models.PROTECT, related_name="subscriptions"
    )
    plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.CASCADE, related_name="subscriptions", null=True, blank=True
    )
    product_variant = models.ForeignKey(
        ProductVariant, on_delete=models.PROTECT, related_name="user_subscriptions", null=True, blank=True
    )
    status_state = models.CharField(
        max_length=20, choices=STATUS_STATE_CHOICES, default="PENDING_PAYMENT"
    )
    start_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    invoice = models.OneToOneField(
        "billing_payment.Invoice",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subscription",
    )
    is_active = models.BooleanField(default=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        plan_name = self.product_variant.name if self.product_variant else (self.plan.name if self.plan else "Unknown")
        return f"{self.user} - {plan_name}"

    @property
    def get_start_date(self):
        if self.start_date:
            return self.start_date.date()
        else:
            if self.invoice and self.invoice.paid_date:
                self.start_date = self.invoice.paid_date
                self.save()
                return self.start_date.date()
        return None

    @property
    def get_end_date(self):
        if self.end_date:
            return self.end_date.date()
        else:
            duration = self.product_variant.duration_days if self.product_variant else (self.plan.duration_days if self.plan else 30)
            if self.start_date and duration:
                self.end_date = self.start_date + timezone.timedelta(days=duration)
                self.save()
                return self.end_date.date()
        return None

    @property
    def is_currently_active(self):
        if self.get_start_date and self.get_end_date:
            return self.start_date <= timezone.now() <= self.end_date
        return False

    @property
    def status(self):
        if self.is_currently_active:
            return "Active"
        elif self.end_date and timezone.now() > self.end_date:
            return "Expired"
        else:
            if self.invoice and self.invoice.status == "PENDING":
                return "Pending"
            return "Inactive"

    def generate_invoice(self, billing_address):
        invoice_from = {
            "full_name": "Vizlearn Limited",
            "phone_number": "+254794771949",
            "email": "vizlearn01@gmail.com",
            "street_address": "Westlands, Nairobi",
            "city": "Nairobi",
            "postal_code": "00100",
            "country": "Kenya",
        }
        invoice = Invoice.objects.create(
            invoice_from=invoice_from,
            invoice_to=billing_address,
            issued_date=timezone.now(),
            due_date=timezone.now(),
        )
        plan_name = self.product_variant.name if self.product_variant else self.plan.name
        plan_desc = self.product_variant.product.description if self.product_variant else self.plan.description
        plan_price = self.product_variant.price if self.product_variant else self.plan.price
        InvoiceItem.objects.create(
            invoice=invoice,
            name=plan_name,
            description=plan_desc or "",
            quantity=1,
            unit_price=plan_price,
        )
        self.invoice = invoice
        self.save()
        return invoice


class SubscriptionSubject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="entitled_subjects")
    subject = models.ForeignKey("curriculum.Subject", on_delete=models.PROTECT, related_name="subscription_entitlements")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscription', 'subject')

    def __str__(self):
        return f"{self.subscription} -> {self.subject.name}"


class Promotion(models.Model):
    RULE_TYPE_CHOICES = (
        ("FIRST_PURCHASE", "First Purchase Only"),
        ("DATE_WINDOW", "Active Date Window"),
        ("COUPON_CODE", "Coupon / Promo Code"),
        ("AUDIENCE", "Target Audience Only"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="promotions")
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2)
    rule_type = models.CharField(max_length=30, choices=RULE_TYPE_CHOICES, default="FIRST_PURCHASE")
    max_redemptions_per_user = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Promotion: {self.name} ({self.promotional_price} KES)"


class PromotionRedemption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT, related_name="redemptions")
    user = models.ForeignKey("Resources.User", on_delete=models.PROTECT, related_name="promotion_redemptions")
    subscription = models.OneToOneField(Subscription, on_delete=models.PROTECT, related_name="promotion_redemption")
    applied_price = models.DecimalField(max_digits=10, decimal_places=2)
    redeemed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} redeemed {self.promotion.name}"



