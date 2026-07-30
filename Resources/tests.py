from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from Resources.models import UserProfile, StudentSubjectSelection, StudentAcademicBaseline
from curriculum.models import Curriculum, Grade, Subject
from organizations.models import School, AcademicYear

User = get_user_model()

class StudentOnboardingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="student_test",
            email="student@test.com",
            password="Password123!",
            role="student"
        )
        self.client.force_authenticate(user=self.user)

        self.curriculum = Curriculum.objects.create(name="CBC", max_selectable_subjects=4, max_priority_subjects=2)
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Grade 10", level=10)
        self.subject1 = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.subject2 = Subject.objects.create(grade=self.grade, name="Physics")
        self.subject3 = Subject.objects.create(grade=self.grade, name="Biology")
        self.subject4 = Subject.objects.create(grade=self.grade, name="Mathematics")
        self.subject5 = Subject.objects.create(grade=self.grade, name="English")

    def test_student_minimum_onboarding_success(self):
        payload = {
            "curriculum_id": self.curriculum.id,
            "grade_id": self.grade.id,
            "selected_subject_ids": [self.subject1.id, self.subject2.id, self.subject3.id],
            "priority_subject_ids": [self.subject1.id],
            "unverified_school_name": "Nairobi Academy"
        }
        response = self.client.post("/student/complete-minimum-onboarding/", payload, format="json")
        if response.status_code != 200:
            print("MINIMUM ONBOARDING ERROR RESPONSE:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.onboarding_status, "MINIMUM_COMPLETE")
        self.assertEqual(profile.onboarding_version, 1)
        self.assertIsNotNone(profile.completed_at)
        
        selections = StudentSubjectSelection.objects.filter(user=self.user)
        self.assertEqual(selections.count(), 3)
        self.assertTrue(selections.get(subject=self.subject1).is_priority)

    def test_student_onboarding_exceed_subject_limit_rejected(self):
        payload = {
            "curriculum_id": self.curriculum.id,
            "grade_id": self.grade.id,
            "selected_subject_ids": [self.subject1.id, self.subject2.id, self.subject3.id, self.subject4.id, self.subject5.id],
            "priority_subject_ids": [self.subject1.id]
        }
        response = self.client.post("/student/complete-minimum-onboarding/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_priority_subject_not_in_selected_list_rejected(self):
        payload = {
            "curriculum_id": self.curriculum.id,
            "grade_id": self.grade.id,
            "selected_subject_ids": [self.subject1.id, self.subject2.id],
            "priority_subject_ids": [self.subject3.id]
        }
        response = self.client.post("/student/complete-minimum-onboarding/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_progressive_onboarding_baseline_save(self):
        payload = {
            "location_county": "Nairobi",
            "primary_device": "LAPTOP",
            "career_aspiration": "Software Engineer",
            "baselines": [
                {
                    "subject_id": self.subject1.id,
                    "raw_previous_grade": "A-",
                    "target_grade": "A",
                    "grading_scheme": "LETTER_GRADE"
                }
            ]
        }
        response = self.client.post("/student/complete-progressive-onboarding/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.onboarding_status, "FULLY_COMPLETE")
        self.assertEqual(profile.location_county, "Nairobi")
        
        baseline = StudentAcademicBaseline.objects.get(user=self.user, subject=self.subject1)
        self.assertEqual(baseline.raw_previous_grade, "A-")

