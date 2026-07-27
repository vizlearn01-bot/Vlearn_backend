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

User = get_user_model()


class GoldenFlowTestCase(APITestCase):
    """
    Automated Testing for Phase 5: Sprint 1 Golden Flow Integration.
    Verifies the complete end-to-end institutional workflow:
      Step 1: Create School ("VizLearn Academy")
      Step 2: Purchase/Attach School Subscription (max_teachers=2, max_students=5)
      Step 3: Invite Teacher (teacher@vizlearn.co)
      Step 4: Verify capacity limit exception when attempting 3rd teacher invitation (above max_teachers=2)
      Step 5: Teacher accepts invitation token -> Membership state becomes ACCEPTED / ACTIVE
      Step 6: Create Class ("Form 4") & Stream ("Form 4 North")
      Step 7: Assign Teacher to Subject ("Chemistry") & Stream ("Form 4 North")
      Step 8: Enroll Student (student@vizlearn.co) in "Form 4 North"
      Step 9: Verify Teacher API GET /api/organizations/teacher/my-streams/ returns Form 4 North and enrolled student roster
      Step 10: Verify Student API GET /api/organizations/student/my-school/ returns VizLearn Academy and Form 4 North
      Step 11: Verify EntitlementService.check_curriculum_access(student, chemistry_subject.id) evaluates True unlocked by school subscription!
    """

    def setUp(self):
        # Admin User (School Owner / School Admin)
        self.admin_user = User.objects.create_user(
            username="admin_golden",
            email="admin@vizlearn.co",
            password="password123",
            role="school_admin"
        )

        # Teacher Users
        self.teacher_user = User.objects.create_user(
            username="teacher_golden",
            email="teacher@vizlearn.co",
            password="password123",
            role="teacher"
        )
        self.teacher2_user = User.objects.create_user(
            username="teacher2_golden",
            email="teacher2@vizlearn.co",
            password="password123",
            role="teacher"
        )
        self.teacher3_user = User.objects.create_user(
            username="teacher3_golden",
            email="teacher3@vizlearn.co",
            password="password123",
            role="teacher"
        )

        # Student User
        self.student_user = User.objects.create_user(
            username="student_golden",
            email="student@vizlearn.co",
            password="password123",
            role="student"
        )

        # Subscription Plan
        self.plan = SubscriptionPlan.objects.create(
            plan_id="school_plan_gold",
            name="Gold School Plan",
            price=500.00,
            duration_days=365
        )

        # Curriculum Hierarchy: Curriculum -> Grade ("Form 4") -> Subject ("Chemistry")
        self.curriculum = Curriculum.objects.create(name="KCSE Curriculum")
        self.grade = Grade.objects.create(
            curriculum=self.curriculum,
            name="Form 4",
            level=4
        )
        self.subject = Subject.objects.create(
            grade=self.grade,
            name="Chemistry"
        )

    def test_sprint1_golden_flow(self):
        """
        Executes the complete 11-step Sprint 1 Golden Flow sequentially.
        """
        # =========================================================================
        # Step 1: Create School ("VizLearn Academy")
        # =========================================================================
        self.client.force_authenticate(user=self.admin_user)
        school_payload = {
            "name": "VizLearn Academy",
            "code": "VIZ-ACADEMY-001",
            "contact_email": "admin@vizlearn.co",
            "phone_number": "+254700000000",
            "address": "Nairobi, Kenya"
        }
        response = self.client.post("/api/organizations/schools/", school_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        school_id = response.data["id"]
        school = School.objects.get(pk=school_id)
        self.assertEqual(school.name, "VizLearn Academy")
        self.assertEqual(school.owner, self.admin_user)

        # Verify admin auto-membership creation
        admin_membership = OrganizationMembership.objects.filter(
            user=self.admin_user, school=school
        ).first()
        self.assertIsNotNone(admin_membership)
        self.assertEqual(admin_membership.role, "school_admin")
        self.assertEqual(admin_membership.state, "ACTIVE")

        # Create active Academic Year for school
        academic_year = AcademicYear.objects.create(
            school=school,
            name="2026 Academic Year",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timedelta(days=365)).date(),
            is_current=True
        )

        # =========================================================================
        # Step 2: Purchase/Attach School Subscription (max_teachers=2, max_students=5)
        # =========================================================================
        subscription_payload = {
            "school": school.id,
            "plan": self.plan.id,
            "max_teachers": 2,
            "max_students": 5,
            "start_date": timezone.now().isoformat(),
            "end_date": (timezone.now() + timedelta(days=364)).isoformat(),
            "is_active": True
        }
        response = self.client.post("/api/organizations/subscriptions/", subscription_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(school.active_subscription.max_teachers, 2)
        self.assertEqual(school.active_subscription.max_students, 5)

        # =========================================================================
        # Step 3: Invite Teacher (teacher@vizlearn.co)
        # =========================================================================
        invite1_payload = {
            "school": school.id,
            "email": "teacher@vizlearn.co",
            "role": "teacher"
        }
        response = self.client.post("/api/organizations/invitations/", invite1_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        raw_token_1 = response.data.get("raw_token")
        self.assertIsNotNone(raw_token_1)
        self.assertEqual(response.data["state"], "PENDING")

        # =========================================================================
        # Step 4: Verify capacity limit exception when attempting 3rd teacher invitation
        # =========================================================================
        # Invite 2nd teacher (filling capacity max_teachers=2: 2 pending invites)
        invite2_payload = {
            "school": school.id,
            "email": "teacher2@vizlearn.co",
            "role": "teacher"
        }
        response = self.client.post("/api/organizations/invitations/", invite2_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 3rd teacher invitation attempt should fail with capacity limit error (HTTP 400 Bad Request)
        invite3_payload = {
            "school": school.id,
            "email": "teacher3@vizlearn.co",
            "role": "teacher"
        }
        response = self.client.post("/api/organizations/invitations/", invite3_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Teacher capacity limit reached", response.data.get("detail", ""))

        # Also verify EntitlementService direct exception call
        with self.assertRaises(ValidationError) as cm:
            EntitlementService.create_school_invitation(
                school=school,
                email="teacher3@vizlearn.co",
                role="teacher",
                created_by=self.admin_user
            )
        self.assertIn("Teacher capacity limit reached", str(cm.exception))

        # =========================================================================
        # Step 5: Teacher accepts invitation token -> Membership state becomes ACCEPTED / ACTIVE
        # =========================================================================
        self.client.force_authenticate(user=self.teacher_user)
        accept_payload = {"token": raw_token_1}
        response = self.client.post("/api/organizations/invitations/accept/", accept_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        membership_data = response.data.get("membership", {})
        self.assertIn(membership_data.get("state"), ["ACCEPTED", "ACTIVE"])

        # Fetch and ensure membership state is ACTIVE
        teacher_membership = OrganizationMembership.objects.get(
            user=self.teacher_user, school=school
        )
        if teacher_membership.state == "ACCEPTED":
            teacher_membership = EntitlementService.transition_membership_state(
                membership=teacher_membership,
                new_state="ACTIVE",
                actor=self.admin_user
            )
        self.assertEqual(teacher_membership.state, "ACTIVE")

        # =========================================================================
        # Step 6: Create Class ("Form 4") & Stream ("Form 4 North")
        # =========================================================================
        self.client.force_authenticate(user=self.admin_user)
        class_payload = {
            "school": school.id,
            "curriculum_grade": self.grade.id,
            "name": "Form 4",
            "code": "F4"
        }
        response = self.client.post("/api/organizations/classes/", class_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        class_id = response.data["id"]

        stream_payload = {
            "school_class": class_id,
            "name": "Form 4 North"
        }
        response = self.client.post("/api/organizations/streams/", stream_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        stream_id = response.data["id"]
        stream = Stream.objects.get(pk=stream_id)
        self.assertEqual(stream.name, "Form 4 North")

        # =========================================================================
        # Step 7: Assign Teacher to Subject ("Chemistry") & Stream ("Form 4 North")
        # =========================================================================
        assign_subject_payload = {
            "teacher": self.teacher_user.id,
            "school": school.id,
            "subject": self.subject.id,
            "academic_year": academic_year.id
        }
        response = self.client.post(
            "/api/organizations/teacher-assignments/assign-subject/", assign_subject_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        assign_stream_payload = {
            "teacher": self.teacher_user.id,
            "stream": stream.id,
            "subject": self.subject.id,
            "academic_year": academic_year.id
        }
        response = self.client.post(
            "/api/organizations/teacher-assignments/assign-stream/", assign_stream_payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # =========================================================================
        # Step 8: Enroll Student (student@vizlearn.co) in "Form 4 North"
        # =========================================================================
        enroll_payload = {
            "student": self.student_user.id,
            "stream": stream.id,
            "academic_year": academic_year.id
        }
        response = self.client.post("/api/organizations/enrollments/", enroll_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            StudentEnrollment.objects.filter(
                student=self.student_user, stream=stream, status="active"
            ).exists()
        )

        # =========================================================================
        # Step 9: Verify Teacher API GET /api/organizations/teacher/my-streams/
        # returns Form 4 North and enrolled student roster
        # =========================================================================
        self.client.force_authenticate(user=self.teacher_user)
        response = self.client.get("/api/organizations/teacher/my-streams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        teacher_stream_data = response.data[0]
        self.assertEqual(teacher_stream_data["stream_name"], "Form 4 North")
        self.assertEqual(teacher_stream_data["school_class_name"], "Form 4")
        self.assertEqual(teacher_stream_data["school_name"], "VizLearn Academy")

        # Verify subject list contains Chemistry
        subject_names = [sub["name"] for sub in teacher_stream_data["subjects"]]
        self.assertIn("Chemistry", subject_names)

        # Verify student roster contains student@vizlearn.co
        student_emails = [st["email"] for st in teacher_stream_data["students"]]
        self.assertIn("student@vizlearn.co", student_emails)

        # =========================================================================
        # Step 10: Verify Student API GET /api/organizations/student/my-school/
        # returns VizLearn Academy and Form 4 North
        # =========================================================================
        self.client.force_authenticate(user=self.student_user)
        response = self.client.get("/api/organizations/student/my-school/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        student_school_data = response.data[0]
        self.assertEqual(student_school_data["school_name"], "VizLearn Academy")
        self.assertEqual(student_school_data["class_name"], "Form 4")
        self.assertEqual(student_school_data["stream_name"], "Form 4 North")
        self.assertTrue(student_school_data["has_active_subscription"])

        # =========================================================================
        # Step 11: Verify EntitlementService.check_curriculum_access(student, chemistry_subject.id)
        # evaluates True unlocked by school subscription!
        # =========================================================================
        has_access = EntitlementService.check_curriculum_access(
            user=self.student_user,
            subject_id=self.subject.id
        )
        self.assertTrue(
            has_access,
            "EntitlementService should grant access to student for Chemistry unlocked by school subscription!"
        )
