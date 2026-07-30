from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework import status

from organizations.models import (
    School,
    OrganizationMembership,
    AcademicYear,
    SchoolSubscription,
    SchoolClass,
    Stream,
    StudentEnrollment,
    TeacherSubjectAssignment,
    TeacherStreamAssignment,
    SchoolInvitation,
)
from curriculum.models import Curriculum, Grade, Subject
from subscriptions.models import SubscriptionPlan
from organizations.services import EntitlementService
from Resources.policies import user_can

User = get_user_model()


class EntitlementServiceTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="admin_user",
            email="admin@school.com",
            role="school_admin"
        )
        self.teacher_user = User.objects.create_user(
            username="teacher_user",
            email="teacher@school.com",
            role="teacher"
        )
        self.student_user = User.objects.create_user(
            username="student_user",
            email="student@school.com",
            role="student"
        )

        self.school = School.objects.create(
            name="VizLearn Test Academy",
            code="VIZ-TEST-001",
            owner=self.admin_user,
            contact_email="admin@school.com"
        )

        self.plan = SubscriptionPlan.objects.create(
            plan_id="school_plan_basic",
            name="Basic School Plan",
            price=100.00,
            duration_days=365
        )

        self.subscription = SchoolSubscription.objects.create(
            school=self.school,
            plan=self.plan,
            max_teachers=2,
            max_students=10,
            start_date=timezone.now() - timedelta(days=1),
            end_date=timezone.now() + timedelta(days=364),
            is_active=True
        )

        self.membership_admin = OrganizationMembership.objects.create(
            user=self.admin_user,
            school=self.school,
            role="school_admin",
            state="ACTIVE"
        )
        self.membership_teacher = OrganizationMembership.objects.create(
            user=self.teacher_user,
            school=self.school,
            role="teacher",
            state="PENDING"
        )
        self.membership_student = OrganizationMembership.objects.create(
            user=self.student_user,
            school=self.school,
            role="student",
            state="PENDING"
        )

    def test_membership_state_transition(self):
        # Pending -> Accepted
        EntitlementService.transition_membership_state(
            self.membership_teacher, "ACCEPTED", self.admin_user
        )
        self.assertEqual(self.membership_teacher.state, "ACCEPTED")

        # Accepted -> Active
        EntitlementService.transition_membership_state(
            self.membership_teacher, "ACTIVE", self.admin_user
        )
        self.assertEqual(self.membership_teacher.state, "ACTIVE")

        # Invalid transition ACTIVE -> PENDING should fail
        with self.assertRaises(ValidationError):
            EntitlementService.transition_membership_state(
                self.membership_teacher, "PENDING", self.admin_user
            )

    def test_teacher_capacity_enforcement(self):
        # 1 active teacher (self.membership_teacher after activation)
        EntitlementService.transition_membership_state(
            self.membership_teacher, "ACCEPTED", self.admin_user
        )
        EntitlementService.transition_membership_state(
            self.membership_teacher, "ACTIVE", self.admin_user
        )

        # Create 1 invitation (total capacity = 2)
        invitation = EntitlementService.create_school_invitation(
            school=self.school,
            email="teacher2@school.com",
            role="teacher",
            created_by=self.admin_user
        )
        self.assertIsNotNone(invitation)

        # 3rd teacher invitation/activation should raise ValidationError
        with self.assertRaises(ValidationError):
            EntitlementService.create_school_invitation(
                school=self.school,
                email="teacher3@school.com",
                role="teacher",
                created_by=self.admin_user
            )

    def test_policies_institutional_actions(self):
        self.assertTrue(user_can(self.admin_user, 'manage_school'))
        self.assertTrue(user_can(self.admin_user, 'invite_teacher'))
        self.assertTrue(user_can(self.admin_user, 'invite_student'))
        self.assertTrue(user_can(self.admin_user, 'assign_teacher'))
        self.assertTrue(user_can(self.admin_user, 'enroll_student'))
        self.assertFalse(user_can(self.student_user, 'manage_school'))


class OrganizationsAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="school_admin_api",
            email="admin_api@school.com",
            password="password123",
            role="school_admin"
        )
        self.teacher_user = User.objects.create_user(
            username="teacher_api",
            email="teacher_api@school.com",
            password="password123",
            role="teacher"
        )
        self.student_user = User.objects.create_user(
            username="student_api",
            email="student_api@school.com",
            password="password123",
            role="student"
        )

        self.school = School.objects.create(
            name="VizLearn API Academy",
            code="VIZ-API-001",
            owner=self.admin_user,
            contact_email="admin_api@school.com"
        )

        self.plan = SubscriptionPlan.objects.create(
            plan_id="school_plan_api",
            name="API School Plan",
            price=150.00,
            duration_days=365
        )

        self.subscription = SchoolSubscription.objects.create(
            school=self.school,
            plan=self.plan,
            max_teachers=3,
            max_students=10,
            start_date=timezone.now() - timedelta(days=1),
            end_date=timezone.now() + timedelta(days=364),
            is_active=True
        )

        self.academic_year = AcademicYear.objects.create(
            school=self.school,
            name="2026 Academic Year",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timedelta(days=365)).date(),
            is_current=True
        )

        self.curriculum = Curriculum.objects.create(name="8-4-4 / CBC")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 4", level=4)
        self.subject = Subject.objects.create(grade=self.grade, name="Chemistry")

        self.school_class = SchoolClass.objects.create(
            school=self.school,
            curriculum_grade=self.grade,
            name="Form 4",
            code="F4"
        )

        self.stream = Stream.objects.create(
            school_class=self.school_class,
            name="North"
        )

        # Admin membership
        OrganizationMembership.objects.create(
            user=self.admin_user,
            school=self.school,
            role="school_admin",
            state="ACTIVE"
        )
        # Teacher membership
        self.teacher_membership = OrganizationMembership.objects.create(
            user=self.teacher_user,
            school=self.school,
            role="teacher",
            state="ACTIVE"
        )
        # Student membership
        self.student_membership = OrganizationMembership.objects.create(
            user=self.student_user,
            school=self.school,
            role="student",
            state="ACTIVE"
        )

    def test_school_crud_endpoints(self):
        self.client.force_authenticate(user=self.admin_user)

        # List schools
        response = self.client.get("/api/organizations/schools/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        # Create new school
        payload = {
            "name": "New Secondary School",
            "code": "NEW-SEC-001",
            "contact_email": "new@school.com"
        }
        response = self.client.post("/api/organizations/schools/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Secondary School")

    def test_class_and_stream_endpoints(self):
        self.client.force_authenticate(user=self.admin_user)

        # Create class
        class_payload = {
            "school": self.school.id,
            "curriculum_grade": self.grade.id,
            "name": "Form 3",
            "code": "F3"
        }
        response = self.client.post("/api/organizations/classes/", class_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        class_id = response.data["id"]

        # Create stream
        stream_payload = {
            "school_class": class_id,
            "name": "South"
        }
        response = self.client.post("/api/organizations/streams/", stream_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_membership_state_transition_endpoint(self):
        self.client.force_authenticate(user=self.admin_user)

        # Create pending membership
        new_user = User.objects.create_user(username="pending_user", email="pending@school.com")
        membership = OrganizationMembership.objects.create(
            user=new_user,
            school=self.school,
            role="teacher",
            state="PENDING"
        )

        url = f"/api/organizations/memberships/{membership.id}/transition-state/"
        response = self.client.post(url, {"state": "ACCEPTED"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["state"], "ACCEPTED")

    def test_invitation_creation_and_acceptance_flow(self):
        self.client.force_authenticate(user=self.admin_user)

        # Create invitation
        invite_payload = {
            "school": self.school.id,
            "email": "invited_teacher@school.com",
            "role": "teacher",
            "intended_class": self.school_class.id,
            "intended_stream": self.stream.id,
            "intended_subject": self.subject.id
        }
        response = self.client.post("/api/organizations/invitations/", invite_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        raw_token = response.data.get("raw_token")
        self.assertIsNotNone(raw_token)

        # Accept invitation with a new authenticated user
        invited_user = User.objects.create_user(
            username="invited_teacher",
            email="invited_teacher@school.com"
        )
        self.client.force_authenticate(user=invited_user)

        accept_payload = {"token": raw_token}
        response = self.client.post("/api/organizations/invitations/accept/", accept_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["membership"]["state"], "ACCEPTED")

    def test_teacher_assignment_endpoints(self):
        self.client.force_authenticate(user=self.admin_user)

        # Assign subject
        assign_sub_payload = {
            "teacher": self.teacher_user.id,
            "school": self.school.id,
            "subject": self.subject.id,
            "academic_year": self.academic_year.id
        }
        response = self.client.post("/api/organizations/teacher-assignments/assign-subject/", assign_sub_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assign stream
        assign_stream_payload = {
            "teacher": self.teacher_user.id,
            "stream": self.stream.id,
            "subject": self.subject.id,
            "academic_year": self.academic_year.id
        }
        response = self.client.post("/api/organizations/teacher-assignments/assign-stream/", assign_stream_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_enrollment_and_batch_enrollment(self):
        self.client.force_authenticate(user=self.admin_user)

        # Single enrollment
        enroll_payload = {
            "student": self.student_user.id,
            "stream": self.stream.id,
            "academic_year": self.academic_year.id
        }
        response = self.client.post("/api/organizations/enrollments/", enroll_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Batch enrollment
        student2 = User.objects.create_user(username="student2", email="student2@school.com")
        batch_payload = {
            "stream": self.stream.id,
            "academic_year": self.academic_year.id,
            "student_ids": [student2.id]
        }
        response = self.client.post("/api/organizations/enrollments/batch-enroll/", batch_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_teacher_my_streams_view(self):
        # Assign teacher to stream
        TeacherStreamAssignment.objects.create(
            teacher=self.teacher_user,
            stream=self.stream,
            subject=self.subject,
            academic_year=self.academic_year
        )
        # Enroll student in stream
        StudentEnrollment.objects.create(
            student=self.student_user,
            stream=self.stream,
            academic_year=self.academic_year,
            status="active"
        )

        self.client.force_authenticate(user=self.teacher_user)
        response = self.client.get("/api/organizations/teacher/my-streams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["stream_name"], "North")
        self.assertEqual(len(response.data[0]["students"]), 1)

    def test_student_my_school_view(self):
        StudentEnrollment.objects.create(
            student=self.student_user,
            stream=self.stream,
            academic_year=self.academic_year,
            status="active"
        )

        self.client.force_authenticate(user=self.student_user)
        response = self.client.get("/api/organizations/student/my-school/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["school_name"], "VizLearn API Academy")
        self.assertTrue(response.data[0]["has_active_subscription"])

    def test_school_register_profile_and_setup_state(self):
        self.client.force_authenticate(user=self.admin_user)
        payload = {
            "name": "St. Andrew High School",
            "code": "ST-ANDREW-001",
            "school_type": "PRIVATE",
            "ownership_type": "PRIVATE",
            "curricula_offered": "CBC",
            "estimated_students": 500
        }
        response = self.client.post("/api/organizations/schools/register-profile/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        school_id = response.data["school"]["id"]

        state_resp = self.client.get(f"/api/organizations/schools/{school_id}/setup-state/")
        self.assertEqual(state_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(state_resp.data["setup_status"], "PROFILE_COMPLETE")
        self.assertEqual(len(state_resp.data["checklist"]), 6)

    def test_cross_school_isolation_setup_state_denied(self):
        other_user = User.objects.create_user(username="other_admin", email="other@school.com")
        self.client.force_authenticate(user=other_user)
        response = self.client.get(f"/api/organizations/schools/{self.school.id}/setup-state/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

