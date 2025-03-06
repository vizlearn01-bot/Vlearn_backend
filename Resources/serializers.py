from rest_framework import serializers
from .models import  Category, VideoCourse
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
    """
    Serializer for user profile data.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

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


class VideoCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCourse
        fields = '__all__'

