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

urlpatterns = [
    path("schools/register-profile/", SchoolRegisterProfileView.as_view(), name="school-register-profile"),
    path("schools/<int:school_id>/setup-state/", SchoolSetupStateView.as_view(), name="school-setup-state"),
    path("schools/<int:school_id>/save-draft/", SchoolSaveDraftView.as_view(), name="school-save-draft"),
    path("schools/<int:school_id>/upload-baseline/", SchoolUploadBaselineView.as_view(), name="school-upload-baseline"),
    path("suggestions/<int:suggestion_id>/merge/", UnverifiedSchoolMergeView.as_view(), name="unverified-school-merge"),
    path("teacher/my-streams/", TeacherMyStreamsView.as_view(), name="teacher-my-streams"),
    path("student/my-school/", StudentMySchoolView.as_view(), name="student-my-school"),
    path("invitations/accept/", InvitationAcceptAPIView.as_view(), name="invitation-accept"),
    path("", include(router.urls)),
]
