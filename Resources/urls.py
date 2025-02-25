from django.urls import path
from .views import (VideoUploadView, VideoListView, CategoriesView, VideoCourseView, CourseDetailView, Home, RegisterView, LoginView, UserProfileView
)

urlpatterns = [
    path('', Home.as_view(), name='home'),

    # Video URLs
    path('upload/video/', VideoUploadView.as_view(), name='video-upload'),
    path('videos/', VideoListView.as_view(), name='video-list'),

    # Categories
    path('categories/', CategoriesView.as_view(), name='categories'),

    path('course_videos/', VideoCourseView.as_view(), name='video_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail')

    path('register/', RegisterView.as_view(), name='register')
    path('login/', LoginView.as_view(), name= 'login')
    path('profile/', UserProfileView.as_view(), name='profile')
]
