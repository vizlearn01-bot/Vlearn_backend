from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Category, VideoCourse
from .serializers import  CategoriesSerializer, HomeSerializer, VideoCourseSerializer, UserSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated


# Home view
class Home(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Welcome to the home page!"}
        serializer = HomeSerializer(data)
        return Response(serializer.data)

# Category views
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

class VideoCourseView(APIView):
    def get(self, request):
        courses = VideoCourse.objects.all()
        serializer = VideoCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            course = VideoCourse.objects.get(pk=pk)
        except VideoCourse.DoesNotExist:
            return Response({"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = VideoCourseSerializer(course)
        return Response(serializer.data)

# generate JWT token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

# register view
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'User': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login view
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token = get_tokens_for_user(user)
            return Response({"User":UserSerializer(user).data, 'token':token}, status=status.HTTP_200_OK)
        return Response({'error':"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
# protected user data view
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'user':UserSerializer(user).data})