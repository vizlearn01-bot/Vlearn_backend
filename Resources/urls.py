from django.urls import path
from .views import (
    CategoriesView,
    ExperimentVideoView,
    CourseDetailView,
    Home,
    RegisterView,
    LoginView,
    UserProfileView,
    VideoInteractionView,
    SubscriptionPlansAPIView,
    UserSubscriptionAPIView,
    FileDetailAPIView,
    FileDownloadAPIView,
    FileUploadAPIView,
    FileListAPIView,
    VideoCountAPIView,
    UserCountView,
    UserDetails,
)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
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
