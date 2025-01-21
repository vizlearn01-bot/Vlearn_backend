from django.urls import path
from .views import (
    VideoUploadView,
    VideoListView,
    CategoriesView,
    VideoCourseView,
    CourseDetailView,
    Home
)

urlpatterns = [
    path('', Home.as_view(), name='home'),

    # Video URLs
    path('upload/video/', VideoUploadView.as_view(), name='video-upload'),
    path('videos/', VideoListView.as_view(), name='video-list'),

    # Categories
    path('categories/', CategoriesView.as_view(), name='categories'),

    path('video-courses/', VideoCourseView.as_view(), name='video_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail')
]
