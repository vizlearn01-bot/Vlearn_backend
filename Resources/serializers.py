from rest_framework import serializers
from .models import  Category, ExperimentVideo, UserProfile, VideoInteraction,  SubscriptionPlan, UserSubscription, UploadedFile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class HomeSerializer(serializers.Serializer):
    message = serializers.CharField()

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    role = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirm', 'role']

    def validate(self, attrs):
        # Compare raw passwords before any hashing occurs
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        attrs.pop('password_confirm')  # Remove confirm field — not needed in create
        return attrs

    def create(self, validated_data):
        # Hash password here, after validation
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone_number', 'school', 'grade', 'enrolled_courses', 'completed_courses', 'average_score', 'total_hours', 'onboarding_complete']

class UserSerializer(serializers.ModelSerializer):
    # Nest the UserProfileSerializer to handle user profile data together with the user
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'account_state', 'organization_id', 'profile', 'is_superuser', 'is_staff']


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
    def get_profile(self, obj):
        if hasattr(obj, 'profile'):
            return UserProfileSerializer(obj.profile).data
        return None


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
    playback_url = serializers.ReadOnlyField()

    class Meta:
        model = ExperimentVideo
        fields = [
            'id', 'title','subtitle', 'image', 'description', 'category',
            'duration', 'difficulty', 'instructor', 'rating',
            'created_at', 'updated_at', 'playback_url', 'cloudflare_video_id'
        ]

class VideoCountSerializer(serializers.Serializer):
        count = serializers.IntegerField()

        
#  Serializer for the VideoInteraction model
class VideoInteractionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Use PrimaryKeyRelatedField
    video_url = serializers.URLField(required=True)

    class Meta:
        model = VideoInteraction
        fields = ['user', 'video_url', 'watched_duration', 'is_completed']

# serializers relating to subscriptions
class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'price', 'duration_days', 'features', 'is_popular']

class UserSubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer(read_only=True)
    
    class Meta:
        model = UserSubscription
        fields = ['id', 'plan', 'start_date', 'end_date', 'is_active']


class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'file_url', 'name', 'uploaded_at', 
                 'size', 'file_type', 'description']
        read_only_fields = ['name', 'uploaded_at', 'size', 'file_type']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and hasattr(obj.file, 'url'):
            return request.build_absolute_uri(obj.file.url)
        return None