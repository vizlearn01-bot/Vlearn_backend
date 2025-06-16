from django.urls import path
from . import views

urlpatterns = [
    path(
        "users/<str:user_id>/invoices/",
        views.InvoiceViewSet.as_view({"get": "list", "post": "create"}),
        name="invoice-list-create",
    ),
    path(
        "users/<str:user_id>/invoices/<str:invoice_number>/",
        views.InvoiceViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="invoice-detail",
    ),
    path(
        "users/<str:user_id>/invoices/<str:invoice_number>/invoice-items/",
        views.InvoiceItemViewSet.as_view({"get": "list", "post": "create"}),
        name="invoice-item-list-create",
    ),
    path(
        "users/<str:user_id>/invoices/<str:invoice_number>/invoice-items/<int:item_id>/",
        views.InvoiceItemViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="invoice-item-detail",
    ),
    path(
        "users/<str:user_id>/invoices/<str:invoice_number>/payment-transactions/",
        views.InvoicePaymentTransactionViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="invoice-payment-transaction-list-create",
    ),
    path(
        "users/<str:user_id>/invoices/<str:invoice_number>/payment-transactions/<str:transaction_id>/",
        views.InvoicePaymentTransactionViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="invoice-payment-transaction-detail",
    ),
    # MPESA API URLS
    path(
        "mpesa/stk-push-callback/",
        views.MpesaStkPushCallBackUrl.as_view(),
        name="mpesa-stk-push-callback",
    )
]
