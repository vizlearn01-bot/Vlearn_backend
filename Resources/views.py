from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Category, ExperimentVideo, VideoInteraction, Answer, Quiz, Question, QuestionAttempt, StudentAnswer, SubscriptionPlan,UserSubscription
from .serializers import  (
    CategoriesSerializer,HomeSerializer, 
    ExperimentVideoSerializer, UserSerializer, 
    UserRegistrationSerializer, UserLoginSerializer, 
    VideoInteractionSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, QuestionAttemptSerializer, StudentAnswerSerializer, SubscriptionPlanSerializer, UserSubscriptionSerializer)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, permissions
from django.utils import timezone
from datetime import datetime, timedelta



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
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Handles user login.
    """

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
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
        return Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperimentVideoView(APIView):
    def get(self, request):
        courses = ExperimentVideo.objects.all()
        serializer = ExperimentVideoSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperimentVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        data['user'] = request.user.id  # Ensure the user is set to the authenticated user
        serializer = VideoInteractionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            course = ExperimentVideo.objects.get(pk=pk)
        except ExperimentVideo.DoesNotExist:
            return Response({"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExperimentVideoSerializer(course)
        return Response(serializer.data)
# Quiz API View
class QuizView(APIView):
    # permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get(self, request):
        quizzes = Quiz.objects.prefetch_related('questions__answers').all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizDetailView(APIView):
    def get(self, request, pk):
        try:
            # Optimize database queries using prefetch_related
            quiz = Quiz.objects.prefetch_related('questions__answers').get(pk=pk)
            serializer = QuizSerializer(quiz)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Quiz.DoesNotExist:
            return Response({"detail": "Quiz not found."}, status=status.HTTP_404_NOT_FOUND)
# Question API View
class QuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Answer API View (For MCQ answers)
class AnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        answer_choices = Answer.objects.all()
        serializer = AnswerSerializer(answer_choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StartQuestionAttempt(APIView):
    # permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        #Extract quiz_id from request data
        quiz_id = request.data.get('quiz_id')
        try:
            #Get the quiz object or raise 404
            quiz = Quiz.objects.get(id=quiz_id)
            
            # Check for existing incomplete attempt
            existing_attempt = QuestionAttempt.objects.filter(
                user=request.user,
                quiz=quiz,
                is_completed=False
            ).first()
            #if found return the existing attempt so user can resume it
            if existing_attempt:
                serializer = QuestionAttemptSerializer(existing_attempt)
                return Response(serializer.data)
            
            # otherwise create new attempt
            attempt = QuestionAttempt.objects.create(
                user=request.user,
                quiz=quiz
            )
            serializer = QuestionAttemptSerializer(attempt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        #handling missing quiz
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class SubmitQuestionAttempt(APIView):
    # permission_classes = [IsAuthenticated]
    
    def put(self, request, pk, format=None):
        # getting the attempt by id
        try:
            attempt = QuestionAttempt.objects.get(pk=pk)
            
            # Permission check
            if attempt.user != request.user:
                return Response(
                    {"error": "You don't have permission to submit this attempt"},
                    status=status.HTTP_403_FORBIDDEN
                )
                
            # prevent duplicate submissions 
            if attempt.is_completed:
                return Response(
                    {"error": "This attempt is already submitted"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Calculate score
            student_answers = StudentAnswer.objects.filter(attempt=attempt)
            total_points = sum(answer.points_earned for answer in student_answers)
            max_points = sum(question.points for question in attempt.quiz.questions.all())
            
            # Update attempt
            attempt.score = (total_points / max_points) * 100 if max_points > 0 else 0
            attempt.is_completed = True
            attempt.end_time = timezone.now()
            attempt.save()
            
            # return final attempt data
            serializer = QuestionAttemptSerializer(attempt)
            return Response(serializer.data)
            
        except QuestionAttempt.DoesNotExist:
            return Response(
                {"error": "Quiz attempt not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class QuestionAttemptList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        # gets all attempts by the user and returns it
        attempts = QuestionAttempt.objects.filter(user=request.user)
        serializer = QuestionAttemptSerializer(attempts, many=True)
        return Response(serializer.data)

class QuizDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk, format=None):
        try:
            quiz = Quiz.objects.prefetch_related(
                            'questions__answers'
                        ).get(pk=pk)            
            serializer = QuizSerializer(quiz)
            return Response(serializer.data)
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        try:
            attempt = QuestionAttempt.objects.get(
                pk=request.data.get('attempt_id'),
                user=request.user,
                is_completed=False
            )
            
            question = Question.objects.get(pk=request.data.get('question_id'))
            answer = Answer.objects.get(pk=request.data.get('answer_id'))
            
            # Check if answer is correct
            is_correct = answer.is_correct
            points_earned = 1 if is_correct else 0             
            # Create or update student answer
            student_answer, created = StudentAnswer.objects.update_or_create(
                attempt=attempt,
                question=question,
                defaults={
                    'answer': answer,
                    'is_correct': is_correct,
                    'points_earned': points_earned
                }
            )
            
            return Response(StudentAnswerSerializer(student_answer).data)
            
        except (QuestionAttempt.DoesNotExist, Question.DoesNotExist, Answer.DoesNotExist) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
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
            user=request.user,
            is_active=True,
            end_date__gte=now
        ).first()
        
        if active_sub:
            serializer = UserSubscriptionSerializer(active_sub)
            return Response({
                'is_active': True,
                'subscription': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'is_active': False,
            'subscription': None
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create new subscription
        """
        plan_id = request.data.get('plan_id')
        mpesa_number = request.data.get('mpesa_number')
        
        if not plan_id or not mpesa_number:
            return Response(
                {"error": "plan_id and mpesa_number are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            plan = SubscriptionPlan.objects.get(id=plan_id, is_active=True)
        except SubscriptionPlan.DoesNotExist:
            return Response(
                {"error": "Plan not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # Check if user already has active subscription
        now = datetime.now()
        existing_sub = UserSubscription.objects.filter(
            user=request.user,
            end_date__gte=now,
            is_active=True
        ).exists()
        
        if existing_sub:
            return Response(
                {"error": "You already have an active subscription"},
                status=status.HTTP_400_BAD_REQUEST
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
            transaction_id=transaction_id
        )
        
        serializer = UserSubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)