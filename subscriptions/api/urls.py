from django.urls import path
from .views import SubscribedUsersCountView, SubscriptionViewSet, SubscriptionPlanViewSet

urlpatterns = [
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
