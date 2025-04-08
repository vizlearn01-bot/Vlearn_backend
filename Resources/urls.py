from django.urls import path
from .views import ( CategoriesView, ExperimentVideoView, CourseDetailView, 
                    Home, RegisterView, LoginView, UserProfileView, 
                    VideoInteractionView, QuizView, QuizDetailView, StartQuestionAttempt,
                    SubmitQuestionAttempt, QuestionAttemptList, SubmitAnswerView, SubscriptionPlansAPIView, UserSubscriptionAPIView)


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    # Categories
    path('categories/', CategoriesView.as_view(), name='categories'),

    path('experiment_videos/', ExperimentVideoView.as_view(), name='experiment_videos'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # video interactions
    path('video_interactions/', VideoInteractionView.as_view(), name='video_interactions'),

    #quizzes
    path('quizzes/', QuizView.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>', QuizDetailView.as_view(), name='quiz_detail'),

    #quizattempts
    path('attempts/start/', StartQuestionAttempt.as_view(), name='start-quiz-attempt'),
    path('attempts/<int:pk>/submit/', SubmitQuestionAttempt.as_view(), name='submit-quiz-attempt'),
    path('attempts/', QuestionAttemptList.as_view(), name='quiz-attempt-list'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('answers/', SubmitAnswerView.as_view(), name='submit-answer'),

    # urls for subscription plans
    path('plans/', SubscriptionPlansAPIView.as_view(), name='subscription-plans'),
    path('subscriptions/', UserSubscriptionAPIView.as_view(), name='user-subscriptions'),
]
