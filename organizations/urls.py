from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organizations.views import (
    SchoolViewSet,
    AcademicYearViewSet,
    SchoolClassViewSet,
    StreamViewSet,
    OrganizationMembershipViewSet,
    TeacherAssignmentViewSet,
    StudentEnrollmentViewSet,
    SchoolSubscriptionViewSet,
    SchoolInvitationViewSet,
    TeacherMyStreamsView,
    StudentMySchoolView,
    InvitationAcceptAPIView,
    SchoolRegisterProfileView,
    SchoolSetupStateView,
    SchoolSaveDraftView,
    SchoolUploadBaselineView,
    UnverifiedSchoolMergeView,
    TeacherSpecialtyViewSet,
    TermViewSet,
    ExamConfigurationViewSet,
    SetupWizardView,
    BulkTeacherUploadView,
    BulkStudentUploadView,
    DownloadTemplateView,
)

router = DefaultRouter()
router.register("schools", SchoolViewSet, basename="school")
router.register("academic-years", AcademicYearViewSet, basename="academic-year")
router.register("classes", SchoolClassViewSet, basename="school-class")
router.register("streams", StreamViewSet, basename="stream")
router.register("memberships", OrganizationMembershipViewSet, basename="organization-membership")
router.register("teacher-assignments", TeacherAssignmentViewSet, basename="teacher-assignment")
router.register("enrollments", StudentEnrollmentViewSet, basename="student-enrollment")
router.register("subscriptions", SchoolSubscriptionViewSet, basename="school-subscription")
router.register("invitations", SchoolInvitationViewSet, basename="school-invitation")
router.register(r'teacher-specialties', TeacherSpecialtyViewSet, basename='teacher-specialty')
router.register(r'terms', TermViewSet, basename='term')
router.register(r'exam-configurations', ExamConfigurationViewSet, basename='exam-configuration')

from organizations.teacher_dashboard_views import (
    TeacherDashboardView,
    TeacherTeachingWorkspaceView,
    TeacherTopicWorkspaceView,
    TeacherLessonLogView,
    ClassTeacherDashboardView,
    TeacherPerformanceView,
)
from organizations.year_transition_views import PrepareNewYearView, TransitionPreviewView, HandleExceptionsView, ConfirmTransitionView

urlpatterns = [
    path("schools/register-profile/", SchoolRegisterProfileView.as_view(), name="school-register-profile"),
    path("schools/<int:school_id>/setup-state/", SchoolSetupStateView.as_view(), name="school-setup-state"),
    path("schools/<int:school_id>/save-draft/", SchoolSaveDraftView.as_view(), name="school-save-draft"),
    path("schools/<int:school_id>/upload-baseline/", SchoolUploadBaselineView.as_view(), name="school-upload-baseline"),
    path("suggestions/<int:suggestion_id>/merge/", UnverifiedSchoolMergeView.as_view(), name="unverified-school-merge"),
    
    # Teacher Production Workspace Endpoints
    path("teacher/dashboard/", TeacherDashboardView.as_view(), name="teacher-dashboard"),
    path("teacher/workspace/", TeacherTeachingWorkspaceView.as_view(), name="teacher-workspace"),
    path("teacher/topic-workspace/<int:stream_id>/<int:subject_id>/<int:topic_id>/", TeacherTopicWorkspaceView.as_view(), name="teacher-topic-workspace"),
    path("teacher/teaching-logs/", TeacherLessonLogView.as_view(), name="teacher-teaching-logs"),
    path("teacher/my-class/", ClassTeacherDashboardView.as_view(), name="teacher-my-class"),
    path("teacher/performance/", TeacherPerformanceView.as_view(), name="teacher-performance"),
    path("teacher/my-streams/", TeacherMyStreamsView.as_view(), name="teacher-my-streams"),
    path("student/my-school/", StudentMySchoolView.as_view(), name="student-my-school"),
    
    # Year Transition
    path("year-transition/prepare/", PrepareNewYearView.as_view(), name="year-transition-prepare"),
    path("year-transition/preview/", TransitionPreviewView.as_view(), name="year-transition-preview"),
    path("year-transition/exceptions/", HandleExceptionsView.as_view(), name="year-transition-exceptions"),
    path("year-transition/confirm/", ConfirmTransitionView.as_view(), name="year-transition-confirm"),
    
    path("invitations/accept/", InvitationAcceptAPIView.as_view(), name="invitation-accept"),
    path('setup-wizard/', SetupWizardView.as_view(), name='setup-wizard'),
    path('bulk-upload/teachers/', BulkTeacherUploadView.as_view(), name='bulk-teacher-upload'),
    path('bulk-upload/students/', BulkStudentUploadView.as_view(), name='bulk-student-upload'),
    path('download-template/', DownloadTemplateView.as_view(), name='download-template'),
    path("", include(router.urls)),
]
