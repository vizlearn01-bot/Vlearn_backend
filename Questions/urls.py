from django.urls import path
from .views import (QuizView, QuizDetailView, StartQuestionAttempt,
                    SubmitQuestionAttempt, QuestionAttemptList, SubmitAnswerView)

urlpatterns = [
    #quizzes
    path('quizzes/', QuizView.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>', QuizDetailView.as_view(), name='quiz_detail'),

    #quizattempts
    path('attempts/start/', StartQuestionAttempt.as_view(), name='start-quiz-attempt'),
    path('attempts/<int:pk>/submit/', SubmitQuestionAttempt.as_view(), name='submit-quiz-attempt'),
    path('attempts/', QuestionAttemptList.as_view(), name='quiz-attempt-list'),
    path('quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('answers/', SubmitAnswerView.as_view(), name='submit-answer'),
]
