from rest_framework import serializers
from .models import  Category, VideoCourse
from django.contrib.auth.models import User



class HomeSerializer(serializers.Serializer):
    message = serializers.CharField()




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
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user