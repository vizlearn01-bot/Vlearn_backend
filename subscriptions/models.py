from django.db import models
from billing_payment.models import Invoice, InvoiceItem
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)


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
    user = models.ForeignKey(
        "Resources.User", on_delete=models.CASCADE, related_name="subscriptions"
    )
    plan = models.ForeignKey(
        SubscriptionPlan, on_delete=models.CASCADE, related_name="subscriptions"
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

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.user} - {self.plan.name}"

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
            if self.start_date and self.plan.duration_days:
                self.end_date = self.start_date + timezone.timedelta(
                    days=self.plan.duration_days
                )
                self.save()
                return self.end_date.date()
        return None

    @property
    def is_active(self):
        if self.get_start_date and self.get_end_date:
            return self.start_date <= timezone.now() <= self.end_date
        return False

    @property
    def status(self):
        if self.is_active:
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
        InvoiceItem.objects.create(
            invoice=invoice,
            name=self.plan.name,
            description=self.plan.description,
            quantity=1,
            unit_price=self.plan.price,
        )
        self.invoice = invoice
        self.save()

        return invoice


@receiver(post_delete, sender=Subscription)
def delete_subscription_invoice(sender, instance, **kwargs):
    try:
        if instance.invoice:
            instance.invoice.delete()
    except Exception as e:
        logger.error(f"Error deleting invoice for subscription {instance.id}: {e}")
