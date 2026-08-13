from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.db.models import Q
from .models import (
    User,
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
    VideoCountSerializer,
    ChangePasswordSerializer,
    SetPasswordSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status, permissions
from .permissions import IsPlatformAdmin, IsStudent, IsTeacher, IsSchoolAdmin, CanCreateInvitation, CanWriteContent
from django.utils import timezone
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
import requests
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.db import IntegrityError
import logging

security_logger = logging.getLogger('security')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def log_security(request, action, message=""):
    user_id = request.user.id if hasattr(request, 'user') and request.user and request.user.is_authenticated else 'anonymous'
    ip = get_client_ip(request)
    security_logger.info(message, extra={'user_id': user_id, 'ip': ip, 'action': action})


class LoginThrottle(AnonRateThrottle):
    rate = '5/min'

class ForgotPasswordThrottle(AnonRateThrottle):
    rate = '3/min'

class ResetPasswordThrottle(AnonRateThrottle):
    rate = '3/min'

class InvitationThrottle(UserRateThrottle):
    rate = '10/min'


# Home view
class Home(APIView):
    permission_classes = [IsAuthenticated]
    
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
            user = serializer.save()
            if hasattr(user, 'profile') and user.profile.onboarding_complete:
                user.account_state = User.ACCOUNT_ACTIVE
                user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    permission_classes = [IsPlatformAdmin]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserCountView(APIView):
    permission_classes = [IsPlatformAdmin]

    def get(self, request, format=None):
        count = User.objects.count()
        return Response({'user_count': count})
    
from .services import AuthService, OnboardingService

def get_tokens_for_user(user):
    return AuthService.get_tokens_for_user(user)

class RegisterView(APIView):
    """
    Handles user registration.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.validated_data.get('role', '')
            try:
                user = AuthService.register_user(serializer.validated_data, role=role)
                tokens = AuthService.get_tokens_for_user(user)
                return Response(tokens, status=status.HTTP_201_CREATED)
            except IntegrityError:
                # A concurrent request slipped past serializer validation and
                # hit the database unique constraint on username.  Return a
                # structured 400 so the client receives the same field-level
                # error format as normal serializer validation — never a 500.
                return Response(
                    {"username": ["A user with that username already exists."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Handles user login.
    """
    permission_classes = [AllowAny]
    throttle_classes = [LoginThrottle]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            
            # Check if user exists and is active before authenticate
            user_check = User.objects.filter(username=username).first()
            if user_check and not user_check.is_active:
                log_security(request, 'login_failed_inactive', f"Failed login for disabled user {username}")
                return Response({"detail": "Account disabled"}, status=status.HTTP_403_FORBIDDEN)

            tokens = AuthService.authenticate_user(username=username, password=password)
            if tokens:
                # To log with correct user_id, we might just pass the user_check id or extract from tokens
                log_security(request, 'login_success', f"Successful login for user {username}")
                return Response(tokens, status=status.HTTP_200_OK)
                
            log_security(request, 'login_failed', f"Failed login for user {username}")
            if not user_check:
                return Response(
                    {"detail": "Account not found. Please sign up instead."}, status=status.HTTP_401_UNAUTHORIZED
                )
            else:
                return Response(
                    {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
                )
        log_security(request, 'login_failed_invalid', "Failed login due to invalid request format")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .policies import user_can

class CategoriesView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not user_can(request.user, 'write_content'):
            log_security(request, 'permission_denied', "Denied write_content permission for CategoriesView")
            return Response({"detail": "You do not have permission to create categories."}, status=status.HTTP_403_FORBIDDEN)
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
        params = getattr(request, "query_params", request.GET)
        
        subject = params.get("subject")
        if subject:
            # All recorded experiment videos belong to Chemistry
            if "chem" not in subject.lower():
                return Response([])

        category = params.get("category")
        if category:
            videos = videos.filter(category__icontains=category)

        topic = params.get("topic")
        if topic:
            # Match against category or title
            topic_lower = topic.lower()
            if "gas law" in topic_lower:
                videos = videos.filter(category__icontains="Gas Laws")
            elif "mole" in topic_lower:
                videos = videos.filter(category__icontains="The Mole")
            elif "organic" in topic_lower:
                videos = videos.filter(category__icontains="Organic")
            elif "nitrogen" in topic_lower:
                videos = videos.filter(category__icontains="Nitrogen")
            elif "sulphur" in topic_lower or "sulfur" in topic_lower:
                videos = videos.filter(category__icontains="Sulphur")
            elif "chlorine" in topic_lower:
                videos = videos.filter(category__icontains="Chlorine")
            else:
                videos = videos.filter(Q(category__icontains=topic) | Q(title__icontains=topic))

        serializer = ExperimentVideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not user_can(request.user, 'write_content'):
            log_security(request, 'permission_denied', "Denied write_content permission for ExperimentVideoView")
            return Response({"detail": "You do not have permission to upload experiment videos."}, status=status.HTTP_403_FORBIDDEN)
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

class VideoCountAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        available_videos_count = ExperimentVideo.objects.filter(is_available=True).count()
        serializer = VideoCountSerializer({"count": available_videos_count})
        return Response(serializer.data)


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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [AllowAny]


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
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        files = UploadedFile.objects.all().order_by("-uploaded_at")
        serializer = FileSerializer(files, many=True, context={"request": request})
        return Response(serializer.data)


class FileDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
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

        # Check ownership or admin status
        if hasattr(file_instance, 'user') and file_instance.user and file_instance.user != request.user and not (request.user.is_staff or request.user.is_superuser or getattr(request.user, 'role', None) == 'platform_admin'):
            log_security(request, 'permission_denied', f"Denied file delete for file {pk}")
            return Response(
                {"error": "You do not have permission to delete this file."}, status=status.HTTP_403_FORBIDDEN
            )

        file_instance.delete()
        return Response(
            {"message": "File deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class FileDownloadAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, *args, **kwargs):
        file_instance = UploadedFile.objects.get(pk=pk)
        if not file_instance.file:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )

        response = FileResponse(file_instance.file)
        response["Content-Disposition"] = f'attachment; filename="{file_instance.name}"'
        return response

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        if AuthService.logout(refresh_token):
            return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        if int(pk) != request.user.id:
            return Response(
                {"error": "You can only change your own password."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        if not user.check_password(serializer.validated_data['old_password']):
            return Response(
                {"errors": {"old_password": ["Old password is incorrect."]}},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        log_security(request, 'password_change', f"Password changed for user {user.id}")
        
        return Response(
            {"message": "Password changed successfully.", "responseCode": 200},
            status=status.HTTP_200_OK
        )

class SetPasswordView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = SetPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        log_security(request, 'password_set', f"Password set by admin {request.user.id} for user {user.id}")
        
        return Response(
            {"message": f"Password set successfully.", "responseCode": 200},
            status=status.HTTP_200_OK
        )

class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [ForgotPasswordThrottle]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        raw_token, token_obj = AuthService.request_password_reset(email)
        log_security(request, 'password_reset_request', f"Password reset requested for {email}")
        
        response_data = {"detail": "If the email is registered, a password reset link has been sent."}
        if settings.DEBUG and raw_token:
            frontend_url = getattr(settings, 'FRONTEND_URL', 'http://localhost:5173')
            response_data["reset_url"] = f"{frontend_url}/reset-password/{raw_token}"
            
        return Response(response_data, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [ResetPasswordThrottle]

    def post(self, request, token):
        new_password = request.data.get("password")
        if not new_password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        success = AuthService.reset_password(token, new_password)
        if success:
            log_security(request, 'password_reset_completion', "Password reset successful")
            return Response({"detail": "Password successfully reset"}, status=status.HTTP_200_OK)
        log_security(request, 'password_reset_failed', "Password reset failed")
        return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

class InvitationView(APIView):
    permission_classes = [CanCreateInvitation]
    throttle_classes = [InvitationThrottle]

    def post(self, request):
        email = request.data.get("email")
        role = request.data.get("role", "student")
        organization_id = request.data.get("organization_id")
        
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        raw_token, invitation = AuthService.create_invitation(
            email=email, role=role, organization_id=organization_id, created_by=request.user
        )
        
        log_security(request, 'invitation_created', f"Invitation created for {email} with role {role}")
        
        response_data = {"detail": f"Invitation created for {email}"}
        if settings.DEBUG:
            response_data["debug_token"] = raw_token
            
        return Response(response_data, status=status.HTTP_201_CREATED)

class InvitationValidateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        invitation = AuthService.validate_invitation(token)
        if not invitation:
            return Response({"error": "Invalid or expired invitation"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "email": invitation.email,
            "role": invitation.role,
            "organization_id": invitation.organization_id
        }, status=status.HTTP_200_OK)

class InvitationAcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, token):
        required_fields = ['username', 'password']
        for field in required_fields:
            if field not in request.data:
                return Response({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
                
        tokens = AuthService.accept_invitation(token, request.data)
        if not tokens:
            log_security(request, 'invitation_accept_failed', "Failed to accept invitation")
            return Response({"error": "Invalid or expired invitation"}, status=status.HTTP_400_BAD_REQUEST)
            
        log_security(request, 'invitation_accepted', "Invitation accepted successfully")
        return Response(tokens, status=status.HTTP_200_OK)

class UserRoleUpdateView(APIView):
    permission_classes = [IsPlatformAdmin]

    def patch(self, request, pk):
        role = request.data.get("role")
        if not role:
            return Response({"error": "role is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
        if user.role != role:
            user.role = role
            user.save()
            AuthService.blacklist_user_tokens(user)
        log_security(request, 'role_change', f"Changed role of user {pk} to {role}")
        return Response({"detail": "User role updated successfully"}, status=status.HTTP_200_OK)

class UserStatusUpdateView(APIView):
    permission_classes = [IsPlatformAdmin]

    def patch(self, request, pk):
        is_active = request.data.get("is_active")
        if is_active is None:
            return Response({"error": "is_active is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
        new_status = bool(is_active)
        if user.is_active != new_status:
            user.is_active = new_status
            user.save()
            if not new_status:
                AuthService.blacklist_user_tokens(user)
        log_security(request, 'account_status_change', f"Changed account status of user {pk} to {is_active}")
        return Response({"detail": "User status updated successfully"}, status=status.HTTP_200_OK)

class SelectRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        role = request.data.get("role")
        if role not in ['student', 'teacher', 'school_admin']:
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)
            
        user = request.user
        if user.role and user.role in ['student', 'teacher', 'school_admin', 'platform_admin']:
            return Response({"error": "Role already set"}, status=status.HTTP_400_BAD_REQUEST)
            
        user.role = role
        user.save()
        AuthService.blacklist_user_tokens(user)
        tokens = AuthService.get_tokens_for_user(user)
        log_security(request, 'role_selected', f"User {user.id} selected role {role}")
        return Response(tokens, status=status.HTTP_200_OK)


class StudentOnboardingStateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = OnboardingService.get_student_onboarding_state(request.user)
        return Response(data, status=status.HTTP_200_OK)


class StudentSaveStepView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        step = request.data.get("step")
        if not step:
            return Response({"error": "Step number is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            profile = OnboardingService.save_student_onboarding_step(request.user, int(step), request.data)
            return Response({
                "message": f"Step {step} saved.",
                "onboarding_status": profile.onboarding_status
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class StudentCompleteMinimumView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            profile = OnboardingService.complete_minimum_student_onboarding(request.user, request.data)
            return Response({
                "message": "Minimum onboarding completed successfully.",
                "onboarding_status": profile.onboarding_status,
                "onboarding_version": profile.onboarding_version,
                "completed_at": profile.completed_at
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": getattr(e, 'message_dict', str(e))}, status=status.HTTP_400_BAD_REQUEST)


class StudentCompleteProgressiveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            profile = OnboardingService.complete_progressive_student_onboarding(request.user, request.data)
            return Response({
                "message": "Progressive profile updated successfully.",
                "onboarding_status": profile.onboarding_status
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": getattr(e, 'message_dict', str(e))}, status=status.HTTP_400_BAD_REQUEST)

