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
    ProductSerializer,
    ProductVariantSerializer,
)
from subscriptions.models import Subscription, SubscriptionPlan, Product, ProductVariant
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from Resources.permissions import IsPlatformAdmin

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True).prefetch_related('variants__access_scopes')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsPlatformAdmin()]

class SubscribedUsersCountView(APIView):
    permission_classes = [IsPlatformAdmin]
    def get(self, request):
        active_subs = Subscription.objects.all()
        active_users = {sub.user.id for sub in active_subs if sub.is_active}
        return Response({"subscribed_users": len(active_users)}, status=status.HTTP_200_OK)

class SubscriptionPlanViewSet(ModelViewSet):
    serializer_class = SubscriptionPlanSerializer
    queryset = SubscriptionPlan.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsPlatformAdmin()]
        return [IsAuthenticated()]


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = self.request.user

        if user_id:
            if str(user.id) != str(user_id) and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
                raise NotFound("The requested resource was not found.")
            return Subscription.objects.filter(user__id=user_id)

        if user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin':
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
        user = request.user
        if user_id and str(user.id) != str(user_id) and not (user.is_staff or user.is_superuser or getattr(user, 'role', None) == 'platform_admin'):
            raise NotFound("The requested resource was not found.")

        target_user = user if not user_id else User.objects.get(id=user_id)
        new_subscription = serializer.save(
            user=target_user,
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

class UserEntitlementsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        from organizations.services import EntitlementService
        from curriculum.models import Subject
        from django.db.models import Q

        user = request.user
        full_access = EntitlementService.has_full_curriculum_access(user)
        allowed_subject_ids = EntitlementService.get_allowed_subject_ids(user)

        subjects = Subject.objects.filter(id__in=allowed_subject_ids).select_related('grade')
        
        grades_data = {}
        subjects_data = []
        for s in subjects:
            subjects_data.append({"id": s.id, "name": s.name, "grade_id": s.grade.id, "grade_name": s.grade.name if s.grade else ""})
            if s.grade and s.grade.id not in grades_data:
                grades_data[s.grade.id] = {"id": s.grade.id, "name": s.grade.name}

        features = []
        if full_access:
            features.extend(["access_simulations", "access_premium_curriculum", "lesson_delivery", "teacher_workspace"])
        else:
            now = timezone.now()
            user_subs = Subscription.objects.filter(
                user=user, is_active=True
            ).filter(Q(end_date__isnull=True) | Q(end_date__gte=now)).select_related('product_variant')
            for sub in user_subs:
                if sub.product_variant:
                    for scope in sub.product_variant.access_scopes.filter(scope_type="FEATURE"):
                        if scope.feature_key and scope.feature_key not in features:
                            features.append(scope.feature_key)

        return Response({
            "platform_wide": full_access,
            "curriculum_access": {
                "grades": list(grades_data.values()),
                "subjects": subjects_data
            },
            "features": features,
        }, status=status.HTTP_200_OK)


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


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        from subscriptions.services import CommercialPricingService
        from subscriptions.models import SubscriptionSubject, Promotion, PromotionRedemption
        from billing_payment.models import Invoice, InvoiceItem

        user = request.user
        product_variant_id = request.data.get("product_variant_id")
        promotion_id = request.data.get("promotion_id")
        coupon_code = request.data.get("coupon_code")

        full_name = f"{user.first_name} {user.last_name}".strip() or user.username
        billing_address = request.data.get("billing_address", {
            "full_name": full_name,
            "email": user.email or "billing@vlearn.app",
            "phone_number": getattr(user.profile, 'phone_number', '') if hasattr(user, 'profile') else ""
        })

        if not product_variant_id:
            return Response({"error": "product_variant_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            variant = ProductVariant.objects.get(id=product_variant_id, is_active=True)
        except ProductVariant.DoesNotExist:
            return Response({"error": "ProductVariant not found or inactive."}, status=status.HTTP_404_NOT_FOUND)

        audience = variant.product.audience

        if audience == "STUDENT":
            promo, final_price = CommercialPricingService.evaluate_promotion_eligibility(
                user, variant, promotion_id=promotion_id, coupon_code=coupon_code
            )

            subscription = Subscription.objects.create(
                user=user,
                product_variant=variant,
                status_state="PENDING_PAYMENT",
                is_active=False
            )

            # Snapshot student profile selected subjects into SubscriptionSubject records
            if hasattr(user, 'profile') and user.profile.selected_subjects.exists():
                for subj in user.profile.selected_subjects.all():
                    SubscriptionSubject.objects.get_or_create(subscription=subscription, subject=subj)

            invoice = subscription.generate_invoice(billing_address)
            if promo and invoice.invoice_items.exists():
                inv_item = invoice.invoice_items.first()
                inv_item.unit_price = final_price
                inv_item.save()

            if promo:
                PromotionRedemption.objects.create(
                    promotion=promo,
                    user=user,
                    subscription=subscription,
                    applied_price=final_price
                )

            return Response({
                "subscription_id": str(subscription.id),
                "invoice_id": invoice.id,
                "amount": float(invoice.total_amount),
                "currency": variant.currency,
                "promotion_applied": promo.name if promo else None,
                "status": "PENDING_PAYMENT",
                "message": "Checkout initiated successfully."
            }, status=status.HTTP_201_CREATED)

        elif audience == "SCHOOL":
            school_id = request.data.get("school_id")
            subject_ids = request.data.get("subject_ids", [])
            stream_ids = request.data.get("stream_ids", [])
            academic_year_id = request.data.get("academic_year_id")
            term_name = request.data.get("term_name", "Term 1")

            if not school_id or not subject_ids or not stream_ids:
                return Response({
                    "error": "school_id, subject_ids (list), and stream_ids (list) are required for school checkout."
                }, status=status.HTTP_400_BAD_REQUEST)

            from organizations.models import School, Stream, AcademicYear, SchoolSubscription
            from curriculum.models import Subject

            try:
                school = School.objects.get(id=school_id)
            except School.DoesNotExist:
                return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)

            is_admin = school.owner == user or user.memberships.filter(
                school=school, role='school_admin', state__in=['ACCEPTED', 'ACTIVE']
            ).exists()
            if not is_admin:
                return Response({"error": "Only school administrators can purchase school subscriptions."}, status=status.HTTP_403_FORBIDDEN)

            streams = Stream.objects.filter(id__in=stream_ids, school_class__school=school)
            if streams.count() != len(set(stream_ids)):
                return Response({"error": "One or more streams do not belong to this school or contain duplicates."}, status=status.HTTP_400_BAD_REQUEST)

            subjects = Subject.objects.filter(id__in=subject_ids)
            if subjects.count() != len(set(subject_ids)):
                return Response({"error": "One or more invalid subject_ids provided."}, status=status.HTTP_400_BAD_REQUEST)

            acad_year = None
            if academic_year_id:
                acad_year = AcademicYear.objects.filter(id=academic_year_id, school=school).first()

            pricing = CommercialPricingService.calculate_school_price(
                stream_count=streams.count(),
                subject_count=subjects.count()
            )
            final_price = pricing["total_price"]

            now = timezone.now()
            duration_days = variant.duration_days or 90
            end_date = now + timezone.timedelta(days=duration_days)

            school_sub = SchoolSubscription.objects.create(
                school=school,
                product_variant=variant,
                academic_year=acad_year,
                term_name=term_name,
                stream_count=streams.count(),
                agreed_price=final_price,
                start_date=now,
                end_date=end_date,
                is_active=False
            )
            school_sub.covered_subjects.set(subjects)
            school_sub.covered_streams.set(streams)

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
                issued_date=now,
                due_date=now,
            )
            InvoiceItem.objects.create(
                invoice=invoice,
                name=f"{school.name} - {variant.name} ({subjects.count()} subjects, {streams.count()} streams)",
                description=f"School subscription covering {subjects.count()} subjects across {streams.count()} streams for {term_name}",
                quantity=1,
                unit_price=final_price,
            )
            school_sub.invoice = invoice
            school_sub.save()

            return Response({
                "school_subscription_id": school_sub.id,
                "invoice_id": invoice.id,
                "amount": float(invoice.total_amount),
                "currency": variant.currency,
                "pricing_breakdown": pricing,
                "status": "PENDING_PAYMENT",
                "message": "School checkout initiated successfully."
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({"error": f"Unsupported product audience: {audience}"}, status=status.HTTP_400_BAD_REQUEST)

