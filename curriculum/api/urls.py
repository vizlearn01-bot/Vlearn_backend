from django.urls import path
from rest_framework.routers import DefaultRouter
from curriculum.api.views import (
    ActiveLessonView,
    CurriculumViewSet,
    GradeViewSet,
    SubjectViewSet,
    TopicViewSet,
    LessonViewSet,
    LessonBlockViewSet,
    KnowledgePackViewSet,
    KnowledgeChunkViewSet,
    LearningUnitViewSet,
    GenerationJobViewSet,
    LessonAssetViewSet,
)

router = DefaultRouter()
router.register(r'curricula', CurriculumViewSet, basename='curriculum')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'lesson-blocks', LessonBlockViewSet, basename='lesson-block')
router.register(r'lesson-assets', LessonAssetViewSet, basename='lesson-asset')  # V2
router.register(r'knowledge-packs', KnowledgePackViewSet, basename='knowledge-pack')
router.register(r'knowledge-chunks', KnowledgeChunkViewSet, basename='knowledge-chunk')
router.register(r'learning-units', LearningUnitViewSet, basename='learning-unit')
router.register(r'generation-jobs', GenerationJobViewSet, basename='generation-job')

urlpatterns = [
    path('topics/<int:topic_id>/lesson/', ActiveLessonView.as_view(), name='active-lesson'),
] + router.urls
