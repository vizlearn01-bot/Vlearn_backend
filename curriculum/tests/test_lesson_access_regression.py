"""
curriculum/tests/test_lesson_access_regression.py

Regression tests for:
- Student published lesson access vs draft/review protection
- Teacher & Admin preview of draft lessons
- Demo account scoping to designated demo lessons
- Preservation of 404 status on un-entitled lessons (information-disclosure policy)
- Cross-topic draft isolation
"""

from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, LearningUnit
from organizations.services import EntitlementService

User = get_user_model()


class LessonAccessRegressionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Build basic curriculum hierarchy
        self.curriculum = Curriculum.objects.create(name="National Curriculum")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 3", level=3)

        # Subject A: Entitled subject
        self.subject_a = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.topic_a1 = Topic.objects.create(subject=self.subject_a, name="Topic 1: Gas Laws", order=1)
        self.unit_a1 = LearningUnit.objects.create(topic=self.topic_a1, name="Gas Laws Unit", order=1)

        self.lesson_published_a1 = Lesson.objects.create(
            topic=self.topic_a1,
            learning_unit=self.unit_a1,
            title="Graham's Law of Diffusion and Kinetic Theory",
            status="published",
        )
        self.lesson_draft_a1 = Lesson.objects.create(
            topic=self.topic_a1,
            learning_unit=self.unit_a1,
            title="Boyle's Law (Pressure-Volume Relationship)",
            status="draft",
        )
        self.lesson_in_review_a1 = Lesson.objects.create(
            topic=self.topic_a1,
            learning_unit=self.unit_a1,
            title="Charles's Law Draft Review",
            status="review",
        )

        # Topic A2: Topic with ONLY draft lessons
        self.topic_a2 = Topic.objects.create(subject=self.subject_a, name="Topic 2: Only Drafts", order=2)
        self.unit_a2 = LearningUnit.objects.create(topic=self.topic_a2, name="Draft Unit", order=1)
        self.lesson_draft_only = Lesson.objects.create(
            topic=self.topic_a2,
            learning_unit=self.unit_a2,
            title="Draft Only Lesson",
            status="draft",
        )

        # Subject B: Un-entitled subject
        self.grade_cs = Grade.objects.create(curriculum=self.curriculum, name="Grade 10", level=10)
        self.subject_b = Subject.objects.create(grade=self.grade_cs, name="Computer Science")
        self.topic_b = Topic.objects.create(subject=self.subject_b, name="Evolution of Computers", order=1)
        self.unit_b = LearningUnit.objects.create(topic=self.topic_b, name="Origins Unit", order=1)

        self.lesson_published_b1 = Lesson.objects.create(
            topic=self.topic_b,
            learning_unit=self.unit_b,
            title="Early Computing Devices and the Origins of Computation",
            status="published",
        )
        self.lesson_published_b2 = Lesson.objects.create(
            topic=self.topic_b,
            learning_unit=self.unit_b,
            title="Generations of Modern Computers",
            status="published",
        )

        # Users
        self.student = User.objects.create_user(
            username="student_user",
            email="student@example.com",
            password="password123",
            role="student",
        )
        self.unentitled_student = User.objects.create_user(
            username="unentitled_student",
            email="unentitled@example.com",
            password="password123",
            role="student",
        )
        self.teacher = User.objects.create_user(
            username="teacher_user",
            email="teacher@example.com",
            password="password123",
            role="teacher",
        )
        self.admin = User.objects.create_user(
            username="admin_user",
            email="admin@example.com",
            password="password123",
            role="platform_admin",
            is_staff=True,
        )
        self.demo_student = User.objects.create_user(
            username="vizlearn-student-demo",
            email="demo@example.com",
            password="password123",
            role="student",
        )

    # 1. Eligible published lesson retrieval
    def test_eligible_published_lesson_retrieval(self):
        self.client.force_authenticate(user=self.student)
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            url = reverse("lesson-detail", kwargs={"pk": self.lesson_published_a1.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data["id"], self.lesson_published_a1.id)
            self.assertEqual(response.data["title"], self.lesson_published_a1.title)

    # 2. Draft lesson protection by direct ID (both in mixed topic and only-draft topic)
    def test_draft_lesson_protection_direct_id(self):
        self.client.force_authenticate(user=self.student)
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            # Draft in mixed topic
            url = reverse("lesson-detail", kwargs={"pk": self.lesson_draft_a1.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

            # Draft in topic with only draft lessons
            url_draft_only = reverse("lesson-detail", kwargs={"pk": self.lesson_draft_only.id})
            response_draft_only = self.client.get(url_draft_only)
            self.assertEqual(response_draft_only.status_code, 404)

    # 3. In-review lesson protection by direct ID
    def test_in_review_lesson_protection_direct_id(self):
        self.client.force_authenticate(user=self.student)
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            url = reverse("lesson-detail", kwargs={"pk": self.lesson_in_review_a1.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

    # 4. Draft lesson list exclusion
    def test_draft_lesson_list_exclusion(self):
        self.client.force_authenticate(user=self.student)
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            url = reverse("lesson-list") + f"?topic={self.topic_a1.id}"
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            results = response.data.get("results", response.data)
            returned_ids = [l["id"] for l in results]
            self.assertIn(self.lesson_published_a1.id, returned_ids)
            self.assertNotIn(self.lesson_draft_a1.id, returned_ids)
            self.assertNotIn(self.lesson_in_review_a1.id, returned_ids)

    # 5. Topic with only draft lessons returns empty list
    def test_topic_with_only_draft_lessons_returns_empty_list(self):
        self.client.force_authenticate(user=self.student)
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            url = reverse("lesson-list") + f"?topic={self.topic_a2.id}"
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            results = response.data.get("results", response.data)
            self.assertEqual(len(results), 0)

    # 6. Cross-topic draft interference: published lesson in Topic A1 is not hidden when Topic A2 has only draft lessons
    def test_cross_topic_draft_does_not_interfere_with_published_lessons(self):
        self.client.force_authenticate(user=self.student)
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            url = reverse("lesson-detail", kwargs={"pk": self.lesson_published_a1.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

            # Listing all lessons in subject A
            url_list = reverse("lesson-list")
            response_list = self.client.get(url_list)
            self.assertEqual(response_list.status_code, 200)
            results = response_list.data.get("results", response_list.data)
            returned_ids = [l["id"] for l in results]
            self.assertIn(self.lesson_published_a1.id, returned_ids)
            self.assertNotIn(self.lesson_draft_only.id, returned_ids)

    # 7. Teacher draft preview by direct ID
    def test_teacher_draft_preview(self):
        self.client.force_authenticate(user=self.teacher)
        url = reverse("lesson-detail", kwargs={"pk": self.lesson_draft_a1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.lesson_draft_a1.id)

    # 8. Platform admin draft preview by direct ID
    def test_platform_admin_draft_preview(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse("lesson-detail", kwargs={"pk": self.lesson_draft_a1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.lesson_draft_a1.id)

    # 9. Demo account lesson scope: can retrieve designated demo lessons, gets 404 for other lessons
    def test_demo_account_lesson_scope(self):
        self.client.force_authenticate(user=self.demo_student)

        # Designated demo lesson 1 (Graham's Law) -> 200
        url_chem_demo = reverse("lesson-detail", kwargs={"pk": self.lesson_published_a1.id})
        response = self.client.get(url_chem_demo)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.lesson_published_a1.id)

        # Designated demo lesson 2 (Early Computing Devices) -> 200
        url_cs_demo = reverse("lesson-detail", kwargs={"pk": self.lesson_published_b1.id})
        response = self.client.get(url_cs_demo)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.lesson_published_b1.id)

        # Non-demo published lesson in CS (Subject B) -> 404
        url_cs_other = reverse("lesson-detail", kwargs={"pk": self.lesson_published_b2.id})
        response = self.client.get(url_cs_other)
        self.assertEqual(response.status_code, 404)

        # Draft lesson in Chemistry -> 404
        url_chem_draft = reverse("lesson-detail", kwargs={"pk": self.lesson_draft_a1.id})
        response = self.client.get(url_chem_draft)
        self.assertEqual(response.status_code, 404)

    # 10. Un-entitled subject lesson: student without entitlement gets 404 (not 403, no entitlement leak)
    def test_unentitled_subject_lesson_returns_404_no_leak(self):
        self.client.force_authenticate(user=self.unentitled_student)
        # Student has entitlement only to Subject A, requests published lesson in Subject B
        with patch.object(EntitlementService, "get_allowed_subject_ids", return_value=[self.subject_a.id]):
            url = reverse("lesson-detail", kwargs={"pk": self.lesson_published_b1.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)
            # Ensure not 403
            self.assertNotEqual(response.status_code, 403)
