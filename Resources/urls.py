from django.urls import path
from .views import ( CategoriesView, ExperimentVideoView, CourseDetailView, Home, RegisterView, LoginView, UserProfileView)


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    # Categories
    path('categories/', CategoriesView.as_view(), name='categories'),

    path('course_videos/', ExperimentVideoView.as_view(), name='video_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

  
]
