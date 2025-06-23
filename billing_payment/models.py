from django.db import models
from Resources.models import User
from utils.utils import PrettyJSONEncoder
from utils.fields import EncryptedJSONField, EncryptedTextField
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging
import uuid

logger = logging.getLogger(__name__)


class InvoiceManger(models.Manager):
    def create(self, *args, **kwargs):
        invoice_number = Invoice.generate_invoice_number()
        return super().create(invoice_number=invoice_number, *args, **kwargs)


class Invoice(models.Model):
    INVOICE_STATUS_CHOICES = (
        ("DRAFT", "Draft"),
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("CANCELLED", "Cancelled"),
        ("OVERDUE", "Overdue"),
    )
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_from = models.JSONField(default=dict, encoder=PrettyJSONEncoder)
    user_from = models.ForeignKey(
        User,
        related_name="invoices_sent",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    invoice_to = models.JSONField(default=dict, encoder=PrettyJSONEncoder)
    user_to = models.ForeignKey(
        User,
        related_name="invoices_received",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=INVOICE_STATUS_CHOICES,
        default="PENDING",
    )
    details = models.JSONField(
        null=True, blank=True, default=dict, encoder=PrettyJSONEncoder
    )
    issued_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    paid_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InvoiceManger()

    def __str__(self):
        return f"Invoice No: {self.invoice_number} - Status: {self.status}"

    @classmethod
    def generate_invoice_number(cls):
        while True:
            invoice_number = uuid.uuid4().hex[:10].upper()
            if not cls.objects.filter(invoice_number=invoice_number).exists():
                return invoice_number

    @property
    def total_amount(self):
        return sum(item.item_total for item in self.invoice_items.all()) or 0


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="invoice_items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.item_total} (Invoice No: {self.invoice.invoice_number})"

    @property
    def item_total(self):
        return self.unit_price * self.quantity


@receiver(post_delete, sender=Invoice)
def delete_invoice_items(sender, instance, **kwargs):
    try:
        instance.items.all().delete()
    except Exception as e:
        logger.error(
            f"Error deleting invoice items for invoice {instance.invoice_number}: {e}"
        )


class PaymentTransactionManager(models.Manager):
    def create(self, *args, **kwargs):
        transaction_id = InvoicePaymentTransaction.generate_transaction_id()
        return super().create(transaction_id=transaction_id, *args, **kwargs)


class InvoicePaymentTransaction(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    )
    PAYMENT_METHODS = (
        ("CASH", "Cash"),
        ("MPESA", "M-Pesa"),
        ("AIRTEL_MONEY", "Airtel Money"),
        ("CARD", "Card"),
        ("BANK_TRANSFER", "Bank Transfer"),
        ("PAYPAL", "PayPal"),
        ("OTHER", "Other"),
    )
    transaction_id = models.CharField(max_length=50, unique=True)
    invoice = models.ForeignKey(
        Invoice, related_name="payment_transactions", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        default="OTHER",
    )
    payment_details = models.JSONField(default=dict, encoder=PrettyJSONEncoder)
    transaction_details = models.JSONField(default=dict, encoder=PrettyJSONEncoder)
    transaction_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PaymentTransactionManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Invoice Payment Transaction"

    @classmethod
    def generate_transaction_id(cls):
        while True:
            transaction_id = uuid.uuid4().hex[:10].upper()
            if not cls.objects.filter(transaction_id=transaction_id).exists():
                return transaction_id

    def __str__(self):
        return f"Transaction ID: {self.transaction_id} - Amount: {self.amount} - Status: {self.status}"


@receiver(post_save, sender=InvoicePaymentTransaction)
def update_invoice_status(sender, instance, created, **kwargs):
    if instance.status == "COMPLETED":
        instance.invoice.status = "PAID"
        instance.invoice.paid_date = instance.transaction_date or timezone.now()
        instance.invoice.save()


class MpesaPaymentAccount(models.Model):
    PAYMENT_ACCOUNT_TYPE_CHOICES = (
        ("PAYBILL", "Paybill"),
        ("BUY_GOODS", "Buy Goods"),
    )
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(
        max_length=20,
        choices=PAYMENT_ACCOUNT_TYPE_CHOICES,
    )
    paybill_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    account_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    till_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    authentication_credentials = EncryptedJSONField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}: ({self.get_type_display()})"

    def get_access_token(self):
        current_date = timezone.now()
        if self.api_access_tokens.filter(expiry_date__gt=current_date).exists():
            return (
                self.api_access_tokens.filter(expiry_date__gt=current_date)
                .first()
                .access_token
            )
        else:
            # Delete expired tokens
            self.api_access_tokens.filter(expiry_date__lt=current_date).delete()

        return None


class MpesaApiAccessToken(models.Model):
    mpesa_payment_account = models.ForeignKey(
        MpesaPaymentAccount,
        related_name="api_access_tokens",
        on_delete=models.CASCADE,
    )
    access_token = EncryptedTextField(max_length=255, unique=True)
    expiry_date = models.DateTimeField()
