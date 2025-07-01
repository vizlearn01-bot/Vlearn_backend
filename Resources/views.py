from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import (
    Category,
    ExperimentVideo,
    VideoInteraction,
    SubscriptionPlan,
    UserSubscription,
    UploadedFile,
)
from .serializers import (
    CategoriesSerializer,
    HomeSerializer,
    ExperimentVideoSerializer,
    UserSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    VideoInteractionSerializer,
    SubscriptionPlanSerializer,
    UserSubscriptionSerializer,
    FileSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, permissions
from django.utils import timezone
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
import requests


# Home view
class Home(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Welcome to the home page!"}
        serializer = HomeSerializer(data)
        return Response(serializer.data)


class UserProfileView(APIView):
    # Restrict access to authenticated users only
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Retrieve the authenticated user's profile
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        # Fully update the user's profile
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        # Partially update the user's profile
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    """
    Handles user registration.
    """

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Handles user login.
    """

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        categories_serializer = CategoriesSerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(categories_serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ExperimentVideoView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        videos = ExperimentVideo.objects.all().order_by("-created_at")
        serializer = ExperimentVideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        required_fields = [
            "title",
            "description",
            "category",
            "difficulty",
            "instructor",
        ]
        for field in required_fields:
            if field not in request.data:
                return Response(
                    {"error": f"{field} is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        video_file = request.FILES.get("file")
        if not video_file:
            return Response(
                {"error": "Video file is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        headers = {
            "Authorization": f"Bearer {settings.CLOUDFLARE_STREAM_AUTH_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "maxDurationSeconds": 3600,
            "requireSignedURLs": False,
            "meta": {
                "name": request.data["title"],
                "description": request.data["description"],
            },
        }

        try:
            # Step 1: Get upload URL
            response = requests.post(
                settings.CLOUDFLARE_STREAM_UPLOAD_URL, headers=headers, json=payload
            )

            if response.status_code != 200:
                return Response(
                    {"error": "Failed to get upload URL"}, status=response.status_code
                )

            upload_data = response.json()["result"]
            upload_url = upload_data["uploadURL"]
            video_uid = upload_data["uid"]

            # Step 2: Upload to that URL
            files = {"file": (video_file.name, video_file)}
            upload_response = requests.post(upload_url, files=files)
            if upload_response.status_code not in [200, 201]:
                return Response(
                    {"error": "Failed to upload video"},
                    status=upload_response.status_code,
                )

            # Step 3: Save to DB
            video = ExperimentVideo.objects.create(
                title=request.data["title"],
                description=request.data["description"],
                category=request.data["category"],
                difficulty=request.data["difficulty"],
                instructor=request.data["instructor"],
                cloudflare_video_id=video_uid,
                image=request.data.get("image", ""),
            )

            serializer = ExperimentVideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class VideoInteractionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Retrieve video interactions for the authenticated user.
        """
        interactions = VideoInteraction.objects.filter(user=request.user)
        serializer = VideoInteractionSerializer(interactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new video interaction for the authenticated user.
        """
        data = request.data
        data["user"] = (
            request.user.id
        )  # Ensure the user is set to the authenticated user
        serializer = VideoInteractionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            course = ExperimentVideo.objects.get(pk=pk)
        except ExperimentVideo.DoesNotExist:
            return Response(
                {"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ExperimentVideoSerializer(course)
        return Response(serializer.data)


# views relating to the subscription plan
class SubscriptionPlansAPIView(APIView):
    """
    Get all active subscription plans
    """

    def get(self, request):
        plans = SubscriptionPlan.objects.filter(is_active=True)
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSubscriptionAPIView(APIView):
    """
    Handle user subscriptions
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get user's active subscription
        """
        now = datetime.now()
        active_sub = UserSubscription.objects.filter(
            user=request.user, is_active=True, end_date__gte=now
        ).first()

        if active_sub:
            serializer = UserSubscriptionSerializer(active_sub)
            return Response(
                {"is_active": True, "subscription": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"is_active": False, "subscription": None}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Create new subscription
        """
        plan_id = request.data.get("plan_id")
        mpesa_number = request.data.get("mpesa_number")

        if not plan_id or not mpesa_number:
            return Response(
                {"error": "plan_id and mpesa_number are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            plan = SubscriptionPlan.objects.get(id=plan_id, is_active=True)
        except SubscriptionPlan.DoesNotExist:
            return Response(
                {"error": "Plan not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Check if user already has active subscription
        now = datetime.now()
        existing_sub = UserSubscription.objects.filter(
            user=request.user, end_date__gte=now, is_active=True
        ).exists()

        if existing_sub:
            return Response(
                {"error": "You already have an active subscription"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # In production: Call M-Pesa API here
        transaction_id = f"MPESA{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Calculate end date based on plan duration
        end_date = datetime.now() + timedelta(days=plan.duration_days)

        subscription = UserSubscription.objects.create(
            user=request.user,
            plan=plan,
            start_date=datetime.now(),
            end_date=end_date,
            is_active=True,
            mpesa_number=mpesa_number,
            transaction_id=transaction_id,
        )

        serializer = UserSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        files = UploadedFile.objects.all().order_by("-uploaded_at")
        serializer = FileSerializer(files, many=True, context={"request": request})
        return Response(serializer.data)


class FileDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return UploadedFile.objects.get(pk=pk)
        except UploadedFile.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        file_instance = self.get_object(pk)
        if not file_instance:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = FileSerializer(file_instance, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        file_instance = self.get_object(pk)
        if not file_instance:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        file_instance.delete()
        return Response(
            {"message": "File deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class FileDownloadAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        file_instance = UploadedFile.objects.get(pk=pk)
        if not file_instance.file:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        response = FileResponse(file_instance.file)
        response["Content-Disposition"] = f'attachment; filename="{file_instance.name}"'
        return response
