from rest_framework import serializers
from .models import Video, Category, VideoCourse
from django.contrib.auth.models import User



class HomeSerializer(serializers.Serializer):
    message = serializers.CharField()


class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()  # Absolute URL for the video file
    cover_image_url = serializers.SerializerMethodField()  # Absolute URL for the cover image

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file', 'cover_image', 'category', 'uploaded_at', 'video_url', 'cover_image_url')

    def get_video_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.video_file.url)
        return None

    def get_cover_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url)
        return None


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model:User
        fields =['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password' ]
        extra_kwargs = { 'password': {'write_only': True}} ## password is not included when sending user data in API responses

        def create(self, validated_data):
            user = User.objects.create-user(**validated_data)
            return user