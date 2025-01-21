from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Video, Category, VideoCourse
from .serializers import VideoSerializer, CategoriesSerializer, HomeSerializer


# Home view
class Home(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Welcome to the home page!"}
        serializer = HomeSerializer(data)
        return Response(serializer.data)


# Video upload view
class VideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        video_serializer = VideoSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Video list view
class VideoListView(APIView):
    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        video_serializer = VideoSerializer(videos, many=True, context={'request': request})
        return Response(video_serializer.data)


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


from .serializers import VideoCourseSerializer

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
