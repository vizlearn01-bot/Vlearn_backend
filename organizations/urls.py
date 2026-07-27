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
    path("teacher/my-streams/", TeacherMyStreamsView.as_view(), name="teacher-my-streams"),
    path("student/my-school/", StudentMySchoolView.as_view(), name="student-my-school"),
    path("invitations/accept/", InvitationAcceptAPIView.as_view(), name="invitation-accept"),
    path("", include(router.urls)),
]
