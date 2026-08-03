from django.urls import path
from .views import (
    CategoriesView,
    ExperimentVideoView,
    CourseDetailView,
    Home,
    RegisterView,
    LoginView,
    UserProfileView,
    UserDetails,
    UserCountView,
    VideoInteractionView,
    SubscriptionPlansAPIView,
    UserSubscriptionAPIView,
    FileDetailAPIView,
    FileDownloadAPIView,
    FileUploadAPIView,
    FileListAPIView,
    VideoCountAPIView,
    LogoutView,
    ForgotPasswordView,
    ResetPasswordView,
    ChangePasswordView,
    SetPasswordView,
    InvitationView,
    InvitationValidateView,
    InvitationAcceptView,
    UserRoleUpdateView,
    UserStatusUpdateView,
    SelectRoleView,
    StudentOnboardingStateView,
    StudentSaveStepView,
    StudentCompleteMinimumView,
    StudentCompleteProgressiveView,
)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("reset-password/<str:token>/", ResetPasswordView.as_view(), name="reset-password"),
    # Compatibility aliases for API accounts namespace
    path("api/accounts/register/", RegisterView.as_view(), name="api-accounts-register"),
    path("api/accounts/auth-tokens/generate/", LoginView.as_view(), name="api-accounts-login"),
    path("api/accounts/users/reset-password/", ForgotPasswordView.as_view(), name="api-accounts-forgot-password"),
    path("api/accounts/users/<int:pk>/change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("api/accounts/users/<int:pk>/set-password/", SetPasswordView.as_view(), name="set-password"),

    path("invitations/", InvitationView.as_view(), name="invitations"),
    path("invitations/<str:token>/validate/", InvitationValidateView.as_view(), name="invitation-validate"),
    path("invitations/<str:token>/accept/", InvitationAcceptView.as_view(), name="invitation-accept"),
    path("users/<int:pk>/role/", UserRoleUpdateView.as_view(), name="user-role-update"),
    path("users/<int:pk>/status/", UserStatusUpdateView.as_view(), name="user-status-update"),
    path("users/select-role/", SelectRoleView.as_view(), name="select-role"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("student/onboarding-state/", StudentOnboardingStateView.as_view(), name="student-onboarding-state"),
    path("student/save-onboarding-step/", StudentSaveStepView.as_view(), name="student-save-onboarding-step"),
    path("student/complete-minimum-onboarding/", StudentCompleteMinimumView.as_view(), name="student-complete-minimum-onboarding"),
    path("student/complete-progressive-onboarding/", StudentCompleteProgressiveView.as_view(), name="student-complete-progressive-onboarding"),
    path("users-count/", UserCountView.as_view(), name="user-count"),
    path("user-details/", UserDetails.as_view(), name="user-details"),
    # Categories
    path("categories/", CategoriesView.as_view(), name="categories"),
    path("experiment_videos/", ExperimentVideoView.as_view(), name="experiment_videos"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("video-count/", VideoCountAPIView.as_view(), name="video-count"),
    # video interactions
    path(
        "video_interactions/", VideoInteractionView.as_view(), name="video_interactions"
    ),
    # urls for subscription plans
    path("plans/", SubscriptionPlansAPIView.as_view(), name="subscription-plans"),
    path(
        "subscriptions/", UserSubscriptionAPIView.as_view(), name="user-subscriptions"
    ),
    # url paths for handling files
    path("upload/", FileUploadAPIView.as_view(), name="file-upload"),
    path("files/", FileListAPIView.as_view(), name="file-list"),
    path("files/<int:pk>/", FileDetailAPIView.as_view(), name="file-detail"),
    path(
        "files/<int:pk>/download/", FileDownloadAPIView.as_view(), name="file-download"
    ),
]
