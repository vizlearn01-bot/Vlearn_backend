from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InvoiceViewSet,
    InvoiceItemViewSet,
    InvoicePaymentTransactionViewSet,
    MpesaStkPushCallBackUrl,
    InvoicePaymentStatusView,
)

router = DefaultRouter()

urlpatterns = [
    # Invoice CRUD
    path(
        "invoices/",
        InvoiceViewSet.as_view({"get": "list", "post": "create"}),
        name="invoice-list",
    ),

    # Invoice Status (for frontend polling)
    path(
        "invoices/<str:invoice_number>/status/",
        InvoicePaymentStatusView.as_view(),
        name="invoice-payment-status",
    ),
    # Invoice Items
    path(
        "invoices/<str:invoice_number>/invoice-items/",
        InvoiceItemViewSet.as_view({"get": "list", "post": "create"}),
        name="invoice-item-list",
    ),
    path(
        "invoices/<str:invoice_number>/invoice-items/<int:item_id>/",
        InvoiceItemViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="invoice-item-detail",
    ),
    # Payment Transactions
    path(
        "invoices/<str:invoice_number>/payment-transactions/",
        InvoicePaymentTransactionViewSet.as_view({"get": "list", "post": "create"}),
        name="payment-transaction-list",
    ),
    path(
        "invoices/<str:invoice_number>/payment-transactions/<str:transaction_id>/",
        InvoicePaymentTransactionViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="payment-transaction-detail",
    ),
    path(
        "invoices/<str:invoice_number>/",
        InvoiceViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="invoice-detail",
    ),
    # M-Pesa Webhook Callback
    path(
        "mpesa/stk-push-callback/",
        MpesaStkPushCallBackUrl.as_view(),
        name="mpesa-stk-push-callback",
    ),
]
