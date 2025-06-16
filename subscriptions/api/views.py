from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from Resources.models import User
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from utils.utils import handle_server_error
from .serializers import (
    SubscriptionSerializer,
    SubscriptionPlanSerializer,
    AddSubscriptionSerializer,
)
from subscriptions.models import Subscription, SubscriptionPlan
from django.utils import timezone


class SubscriptionPlanViewSet(ModelViewSet):
    serializer_class = SubscriptionPlanSerializer
    queryset = SubscriptionPlan.objects.all()


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = self.request.user

        if user_id:
            return Subscription.objects.filter(user__id=user_id)

        if user.is_staff or user.is_superuser:
            return Subscription.objects.all()

        raise NotFound("The requested resource was not found.")

    def get_object(self):
        user_id = self.kwargs.get("user_id")
        subscription_id = self.kwargs.get("subscription_id")

        if not user_id or not subscription_id:
            raise NotFound("The requested resource was not found.")

        return Subscription.objects.get(
            user__id=user_id, id=subscription_id
        )

    def list(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_results = paginator.paginate_queryset(
            self.get_queryset(), request, view=self
        )
        if paginated_results is not None:
            serializer = self.get_serializer(paginated_results, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "data": serializer.data,
                    "pagination": {
                        "total_pages": paginator.page.paginator.num_pages,
                        "current_page": paginator.page.number,
                        "has_previous": paginator.page.has_previous(),
                        "has_next": paginator.page.has_next(),
                    },
                },
            )

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data},
        )

    def active_subscriptions(self, request, *args, **kwargs):
        subscriptions = self.get_queryset().filter(end_date__gt=timezone.now())
        serializer = self.get_serializer(subscriptions, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data},
        )

    def create(self, request, *args, **kwargs):
        serializer = AddSubscriptionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"errors": serializer.errors},
            )

        user_id = self.kwargs.get("user_id")
        user = User.objects.get(id=user_id)
        new_subscription = serializer.save(
            user=user,
            **serializer.validated_data,
        )
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "data": SubscriptionSerializer(new_subscription).data,
                "message": "Subscription added successfully.",
            },
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            status=status.HTTP_200_OK,
            data={"data": serializer.data},
        )

    def handle_exception(self, exc):
        if isinstance(exc, Subscription.DoesNotExist):
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "data": None,
                    "errors": {"detail": "Subscription not found."},
                },
            )

        # Handle other exceptions
        return handle_server_error(
            request=self.request, error=exc, debug=settings.DEBUG
        )
