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
    VisualGenerationJobViewSet,
    LessonAssetViewSet,
    ConceptViewSet,
    ConceptRelationshipViewSet,
    LearningObjectiveViewSet,
    MisconceptionViewSet,
    LearningExperienceGraphViewSet,
    SimulationViewSet,
    MediaProxyView,
)
from curriculum.api.runtime_views import RuntimeSessionViewSet

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
router.register(r'visual-generation-jobs', VisualGenerationJobViewSet, basename='visual-generation-job')
router.register(r'concepts', ConceptViewSet, basename='concept')
router.register(r'concept-relationships', ConceptRelationshipViewSet, basename='concept-relationship')
router.register(r'learning-objectives', LearningObjectiveViewSet, basename='learning-objective')
router.register(r'misconceptions', MisconceptionViewSet, basename='misconception')
router.register(r'learning-experience-graphs', LearningExperienceGraphViewSet, basename='learning-experience-graph')
router.register(r'simulations', SimulationViewSet, basename='simulation')
router.register(r'runtime/session', RuntimeSessionViewSet, basename='runtime-session')

urlpatterns = [
    path('topics/<int:topic_id>/lesson/', ActiveLessonView.as_view(), name='active-lesson'),
    path('media-proxy/', MediaProxyView.as_view(), name='media-proxy'),
] + router.urls
