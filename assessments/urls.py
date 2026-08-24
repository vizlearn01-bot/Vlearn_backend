from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExaminationViewSet, StudentMarkViewSet, MarkTemplateDownloadView, KCSEResultViewSet
from .performance_views import (
    StudentPerformanceView, StreamPerformanceView, 
    FormPerformanceView, SchoolPerformanceView, ClassTeacherStreamView
)

router = DefaultRouter()
router.register(r'examinations', ExaminationViewSet)
router.register(r'marks', StudentMarkViewSet)
router.register(r'kcse', KCSEResultViewSet, basename='kcse')

urlpatterns = [
    path('', include(router.urls)),
    path('marks/template/download/', MarkTemplateDownloadView.as_view(), name='mark-template-download'),
    
    # Direct and performance endpoints
    path('student/<int:id>/', StudentPerformanceView.as_view(), name='student-performance-direct'),
    path('stream/<int:id>/', StreamPerformanceView.as_view(), name='stream-performance-direct'),
    path('form/<int:id>/', FormPerformanceView.as_view(), name='form-performance-direct'),
    path('school/<int:id>/', SchoolPerformanceView.as_view(), name='school-performance-direct'),
    path('class-teacher/stream/<int:id>/', ClassTeacherStreamView.as_view(), name='class-teacher-stream-performance-direct'),
    
    # Aliased under /performance/... for backwards compatibility
    path('performance/student/<int:id>/', StudentPerformanceView.as_view(), name='student-performance'),
    path('performance/stream/<int:id>/', StreamPerformanceView.as_view(), name='stream-performance'),
    path('performance/form/<int:id>/', FormPerformanceView.as_view(), name='form-performance'),
    path('performance/school/<int:id>/', SchoolPerformanceView.as_view(), name='school-performance'),
    path('performance/class-teacher/stream/<int:id>/', ClassTeacherStreamView.as_view(), name='class-teacher-stream-performance'),
]
