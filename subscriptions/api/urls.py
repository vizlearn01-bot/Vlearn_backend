from django.urls import path
from . import views

urlpatterns = [
    path(
        "plans/",
        views.SubscriptionPlanViewSet.as_view({"get": "list"}),
        name="subscription_plan_list",
    ),
    path(
        "users/<str:user_id>/subscriptions/",
        views.SubscriptionViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="subscription_list_by_account",
    ),
    path(
        "users/<str:user_id>/subscriptions/active/",
        views.SubscriptionViewSet.as_view({"get": "active_subscriptions"}),
        name="active_subscriptions_by_account",
    ),
    path(
        "users/<str:user_id>/subscriptions/<str:subscription_id>/",
        views.SubscriptionViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="subscription_detail",
    ),
]
