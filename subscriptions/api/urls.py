from django.urls import path
from .views import SubscribedUsersCountView, SubscriptionViewSet, SubscriptionPlanViewSet, UserEntitlementsView, ProductViewSet, CheckoutView

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="subscription_checkout"),
    path("products/", ProductViewSet.as_view({"get": "list"}), name="product_list"),
    path("products/<str:pk>/", ProductViewSet.as_view({"get": "retrieve"}), name="product_detail"),
    path("entitlements/me/", UserEntitlementsView.as_view(), name="user_entitlements"),
    path("plans/", SubscriptionPlanViewSet.as_view({"get": "list"}),
        name="subscription_plan_list",
    ),
    path(
        "users/<str:user_id>/subscriptions/",
        SubscriptionViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="subscription_list_by_account",
    ),
    path(
        "users/<str:user_id>/subscriptions/active/",
        SubscriptionViewSet.as_view({"get": "active_subscriptions"}),
        name="active_subscriptions_by_account",
    ),
    path(
        "users/<str:user_id>/subscriptions/<str:subscription_id>/",
    SubscriptionViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="subscription_detail",
    ),
        path('subscribed-users/count/', SubscribedUsersCountView.as_view(), name='subscribed-users-count'),

]
