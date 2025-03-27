from rest_framework import serializers
from .models import  Category, ExperimentVideo, UserProfile, VideoInteraction, Answer, Question , Quiz, QuestionAttempt, StudentAnswer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class HomeSerializer(serializers.Serializer):
    message = serializers.CharField()

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email',  'password']

    def validate_password(self, value):
        return make_password(value)  # Hash the password

    def create(self, validated_data):
            return User.objects.create(**validated_data)

    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone_number', 'enrolled_courses', 'completed_courses', 'average_score', 'total_hours']

class UserSerializer(serializers.ModelSerializer):
    # Nest the UserProfileSerializer to handle user profile data together with the user
    profile = UserProfileSerializer()  

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

    def update(self, instance, validated_data):
        # Extract profile data from the validated data
        profile_data = validated_data.pop('profile', {})

        # Update user fields (username, email, etc.)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update profile fields if profile data exists
        profile = instance.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class CategoriesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()  # Absolute URL for the category image

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'image_url')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class ExperimentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentVideo
        fields = '__all__'

#  Serializer for the VideoInteraction model
class VideoInteractionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Use PrimaryKeyRelatedField
    video_url = serializers.URLField(required=True)

    class Meta:
        model = VideoInteraction
        fields = ['user', 'video_url', 'watched_duration', 'is_completed']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct'] 
    

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)  # Nested answers
    
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'answers']  # Add 'answers' to fields

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)  # Nested questions with answers
    
    class Meta:
        model = Quiz
        fields = ['id', 'video', 'title', 'description', 'time_limit', 
                 'difficulty', 'question_count', 'questions']

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['id', 'question', 'answer', 'text_answer', 'is_correct', 'points_earned']

class QuizAttemptSerializer(serializers.ModelSerializer):
    student_answers = StudentAnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = QuestionAttempt
        fields = ['id', 'student', 'quiz', 'start_time', 'end_time', 'score', 'is_completed', 'student_answers']