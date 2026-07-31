from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Answer, Quiz, Question, QuestionAttempt, StudentAnswer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, permissions
from .serializers import (
    QuizSerializer,
    QuestionSerializer,
    AnswerSerializer,
    QuestionAttemptSerializer,
    StudentAnswerSerializer,
)


from Resources.permissions import IsPlatformAdmin, CanWriteContent, HasActiveSubscription

class QuizView(APIView):
    permission_classes = [HasActiveSubscription]

    def get(self, request):
        quizzes = Quiz.objects.prefetch_related("questions__answers").all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not user_can(request.user, 'write_content'):
            return Response({"detail": "You do not have permission to create quizzes."}, status=status.HTTP_403_FORBIDDEN)
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizDetailView(APIView):
    permission_classes = [HasActiveSubscription]

    def get(self, request, pk):
        try:
            # Optimize database queries using prefetch_related
            quiz = Quiz.objects.prefetch_related("questions__answers").get(pk=pk)
            serializer = QuizSerializer(quiz)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Quiz.DoesNotExist:
            return Response(
                {"detail": "Quiz not found."}, status=status.HTTP_404_NOT_FOUND
            )


from Resources.policies import user_can

class QuestionView(APIView):
    permission_classes = [HasActiveSubscription]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not user_can(request.user, 'write_content'):
            return Response({"detail": "You do not have permission to create questions."}, status=status.HTTP_403_FORBIDDEN)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Answer API View (For MCQ answers)
class AnswerView(APIView):
    permission_classes = [HasActiveSubscription]

    def get(self, request):
        answer_choices = Answer.objects.all()
        serializer = AnswerSerializer(answer_choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not user_can(request.user, 'write_content'):
            return Response({"detail": "You do not have permission to create answers."}, status=status.HTTP_403_FORBIDDEN)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartQuestionAttempt(APIView):
    permission_classes = [HasActiveSubscription]

    def post(self, request, format=None):
        # Extract quiz_id from request data
        quiz_id = request.data.get("quiz_id")
        try:
            # Get the quiz object or raise 404
            quiz = Quiz.objects.get(id=quiz_id)

            # Check for existing incomplete attempt
            existing_attempt = QuestionAttempt.objects.filter(
                user=request.user, quiz=quiz, is_completed=False
            ).first()
            # if found return the existing attempt so user can resume it
            if existing_attempt:
                serializer = QuestionAttemptSerializer(existing_attempt)
                return Response(serializer.data)

            # otherwise create new attempt
            attempt = QuestionAttempt.objects.create(user=request.user, quiz=quiz)
            serializer = QuestionAttemptSerializer(attempt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # handling missing quiz
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND
            )


class SubmitQuestionAttempt(APIView):
    permission_classes = [HasActiveSubscription]

    def put(self, request, pk, format=None):
        try:
            attempt = QuestionAttempt.objects.get(pk=pk, user=request.user)

            if attempt.is_completed:
                return Response({"error": "Attempt already submitted"}, status=400)

            # Get and validate duration
            try:
                duration = int(request.data.get("duration", 0))
                if duration < 0:
                    raise ValueError
            except (TypeError, ValueError):
                return Response({"error": "Invalid duration value"}, status=400)

            # Get and validate score
            try:
                score = float(request.data.get("score", 0))
                if not (0 <= score <= 100):
                    raise ValueError
            except (TypeError, ValueError):
                return Response(
                    {"error": "Score must be between 0 and 100"}, status=400
                )

            # Update attempt
            attempt.duration = duration
            attempt.score = score
            attempt.is_completed = True
            attempt.save()

            serializer = QuestionAttemptSerializer(attempt)
            return Response(serializer.data)

        except QuestionAttempt.DoesNotExist:
            return Response({"error": "Attempt not found"}, status=404)


class QuestionAttemptList(APIView):
    permission_classes = [HasActiveSubscription]

    def get(self, request, format=None):
        # gets all attempts by the user and returns it
        attempts = QuestionAttempt.objects.filter(user=request.user)
        serializer = QuestionAttemptSerializer(attempts, many=True)
        return Response(serializer.data)


class QuizDetailView(APIView):
    permission_classes = [HasActiveSubscription]

    def get(self, request, pk, format=None):
        try:
            quiz = Quiz.objects.prefetch_related("questions__answers").get(pk=pk)
            serializer = QuizSerializer(quiz)
            return Response(serializer.data)
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND
            )


class SubmitAnswerView(APIView):
    permission_classes = [HasActiveSubscription]

    def post(self, request, format=None):
        try:
            attempt = QuestionAttempt.objects.get(
                pk=request.data.get("attempt_id"), user=request.user, is_completed=False
            )

            question = Question.objects.get(pk=request.data.get("question_id"))
            answer = Answer.objects.get(pk=request.data.get("answer_id"))

            # Check if answer is correct
            is_correct = answer.is_correct
            points_earned = 1 if is_correct else 0
            # Create or update student answer
            student_answer, created = StudentAnswer.objects.update_or_create(
                attempt=attempt,
                question=question,
                defaults={
                    "answer": answer,
                    "is_correct": is_correct,
                    "points_earned": points_earned,
                },
            )
            return Response(StudentAnswerSerializer(student_answer).data)

        except (
            QuestionAttempt.DoesNotExist,
            Question.DoesNotExist,
            Answer.DoesNotExist,
        ) as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
