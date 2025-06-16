from django.contrib import admin
from .models import (
    Invoice,
    InvoiceItem,
    InvoicePaymentTransaction,
    MpesaPaymentAccount,
    MpesaApiAccessToken,
)


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 0


class PaymentTransactionInline(admin.StackedInline):
    model = InvoicePaymentTransaction
    fields = (
        "transaction_id",
        "amount",
        "status",
        "payment_method",
        "transaction_details",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("transaction_id", "created_at", "updated_at")
    show_change_link = True
    can_delete = False
    extra = 0


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "status", "created_at", "updated_at")
    search_fields = ["invoice_number"]
    inlines = [InvoiceItemInline, PaymentTransactionInline]
    list_filter = ("status",)
    ordering = ("-created_at",)


admin.site.register(InvoicePaymentTransaction)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem)


class MpesaApiAccessTokenInline(admin.StackedInline):
    model = MpesaApiAccessToken
    fields = ("access_token", "expiry_date")
    readonly_fields = ("access_token", "expiry_date")
    can_delete = True
    extra = 0


class MpesaPaymentAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "paybill_number", "account_number", "till_number")
    search_fields = ["name"]
    inlines = [MpesaApiAccessTokenInline]
    list_filter = ("type",)
    ordering = ("name",)


admin.site.register(MpesaPaymentAccount, MpesaPaymentAccountAdmin)
