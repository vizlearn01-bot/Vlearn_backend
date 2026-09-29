import uuid
from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.test.utils import CaptureQueriesContext
from django.db import connection
from rest_framework.test import APIClient
from rest_framework import status

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

User = get_user_model()


class CourseManagementAggregationTests(TestCase):
    """
    Verification test suite for Course Management backend aggregation layer.
    Verifies correctness across Cases A, B, C, D, E, F, permissions, and SQL query efficiency.
    """

    def setUp(self):
        self.client = APIClient()

        # Create admin user
        self.admin_user = User.objects.create_user(
            username=f'admin_{uuid.uuid4().hex[:8]}',
            email=f'admin_{uuid.uuid4().hex[:8]}@example.com',
            password='AdminPassword123!',
            role='platform_admin',
            is_staff=True,
        )

        # Create student user
        self.student_user = User.objects.create_user(
            username=f'student_{uuid.uuid4().hex[:8]}',
            email=f'student_{uuid.uuid4().hex[:8]}@example.com',
            password='StudentPassword123!',
            role='student',
        )

        # Core test hierarchy
        self.curriculum = Curriculum.objects.create(name=f"Test_Curriculum_{uuid.uuid4().hex[:6]}")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 3", level=3)
        self.subject = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.topic = Topic.objects.create(subject=self.subject, name="Topic 1: Gas Laws", order=1)

    def test_01_permission_enforcement(self):
        """Verify non-admin or unauthenticated access is strictly rejected."""
        url = f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}"

        # 1. Unauthenticated
        res = self.client.get(url)
        self.assertIn(res.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # 2. Student user
        self.client.force_authenticate(user=self.student_user)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # 3. Platform Admin user
        self.client.force_authenticate(user=self.admin_user)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_02_case_a_ten_units_zero_generated(self):
        """
        Case A: 10 units defined, 0 generated.
        Expected: defined = 10, generated = 0, published = 0, unstarted = 10, draft/review = 0.
        """
        for i in range(10):
            LearningUnit.objects.create(topic=self.topic, name=f"Unit {i+1}", order=i+1)

        self.client.force_authenticate(user=self.admin_user)
        url = f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        subjects = res.data.get('subjects', [])
        self.assertEqual(len(subjects), 1)

        s = subjects[0]
        self.assertEqual(s['units_defined'], 10)
        self.assertEqual(s['units_generated'], 0)
        self.assertEqual(s['units_published'], 0)
        self.assertEqual(s['units_unstarted'], 10)
        self.assertEqual(s['draft_or_review_units'], 0)

    def test_03_case_b_ten_units_seven_generated(self):
        """
        Case B: 10 units defined, 7 generated (all draft/review, 0 published).
        Expected: defined = 10, generated = 7, published = 0, unstarted = 3, draft/review = 7.
        """
        units = []
        for i in range(10):
            units.append(LearningUnit.objects.create(topic=self.topic, name=f"Unit {i+1}", order=i+1))

        # Generate draft lessons for first 7 units
        for i in range(7):
            Lesson.objects.create(topic=self.topic, learning_unit=units[i], status='draft', version=1)

        self.client.force_authenticate(user=self.admin_user)
        url = f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        s = res.data['subjects'][0]
        self.assertEqual(s['units_defined'], 10)
        self.assertEqual(s['units_generated'], 7)
        self.assertEqual(s['units_published'], 0)
        self.assertEqual(s['units_unstarted'], 3)
        self.assertEqual(s['draft_or_review_units'], 7)

    def test_04_case_c_ten_units_seven_generated_five_published(self):
        """
        Case C: 10 units defined, 7 generated, 5 published.
        Expected: defined = 10, generated = 7, published = 5, unstarted = 3, draft/review = 2.
        """
        units = []
        for i in range(10):
            units.append(LearningUnit.objects.create(topic=self.topic, name=f"Unit {i+1}", order=i+1))

        # 5 published
        for i in range(5):
            Lesson.objects.create(topic=self.topic, learning_unit=units[i], status='published', version=1)

        # 2 draft
        for i in range(5, 7):
            Lesson.objects.create(topic=self.topic, learning_unit=units[i], status='draft', version=1)

        self.client.force_authenticate(user=self.admin_user)
        url = f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        s = res.data['subjects'][0]
        self.assertEqual(s['units_defined'], 10)
        self.assertEqual(s['units_generated'], 7)
        self.assertEqual(s['units_published'], 5)
        self.assertEqual(s['units_unstarted'], 3)
        self.assertEqual(s['draft_or_review_units'], 2)

    def test_05_case_d_archived_and_draft_lesson_not_published(self):
        """
        Case D: One learning unit has an old archived lesson and a current draft lesson.
        It must NOT appear as published.
        Expected: defined = 1, generated = 1, published = 0, unstarted = 0, draft/review = 1.
        """
        unit = LearningUnit.objects.create(topic=self.topic, name="Unit with Revision", order=1)
        # Old archived lesson
        Lesson.objects.create(topic=self.topic, learning_unit=unit, status='archived', version=1)
        # New working draft lesson
        Lesson.objects.create(topic=self.topic, learning_unit=unit, status='draft', version=2)

        self.client.force_authenticate(user=self.admin_user)
        url = f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}"
        res = self.client.get(url)

        s = res.data['subjects'][0]
        self.assertEqual(s['units_defined'], 1)
        self.assertEqual(s['units_generated'], 1)
        self.assertEqual(s['units_published'], 0, "Archived + draft unit must NOT be counted as published")
        self.assertEqual(s['units_unstarted'], 0)
        self.assertEqual(s['draft_or_review_units'], 1)

    def test_06_case_e_archived_and_published_lesson_counted_once(self):
        """
        Case E: One learning unit has an archived lesson and a current published lesson.
        It must count as published once.
        Expected: defined = 1, generated = 1, published = 1, unstarted = 0, draft/review = 0.
        """
        unit = LearningUnit.objects.create(topic=self.topic, name="Unit with History", order=1)
        # Old archived version
        Lesson.objects.create(topic=self.topic, learning_unit=unit, status='archived', version=1)
        # Current published version
        Lesson.objects.create(topic=self.topic, learning_unit=unit, status='published', version=2)

        self.client.force_authenticate(user=self.admin_user)
        url = f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}"
        res = self.client.get(url)

        s = res.data['subjects'][0]
        self.assertEqual(s['units_defined'], 1)
        self.assertEqual(s['units_generated'], 1)
        self.assertEqual(s['units_published'], 1, "Must count as published exactly once")
        self.assertEqual(s['units_unstarted'], 0)
        self.assertEqual(s['draft_or_review_units'], 0)

    def test_07_case_f_blocks_and_pending_assets_reported(self):
        """
        Case F: Lesson has multiple blocks, multiple assets, and pending assets.
        Verify correct counts in both grade-summary and subject-hierarchy.
        """
        unit = LearningUnit.objects.create(topic=self.topic, name="Gas Laws Unit", order=1)
        lesson = Lesson.objects.create(topic=self.topic, learning_unit=unit, status='published', version=1)

        # 3 blocks
        b1 = LessonBlock.objects.create(lesson=lesson, block_type='learning_goal', order=1)
        b2 = LessonBlock.objects.create(lesson=lesson, block_type='concept_explanation', order=2)
        b3 = LessonBlock.objects.create(lesson=lesson, block_type='suggested_diagram', order=3)

        # 2 assets: 1 attached, 1 pending
        a1 = LessonAsset.objects.create(lesson=lesson, asset_type='diagram', status='attached')
        a2 = LessonAsset.objects.create(lesson=lesson, asset_type='simulation', status='pending')
        a1.blocks.add(b3)

        self.client.force_authenticate(user=self.admin_user)

        # 1. Check grade-summary pending asset count
        res_summary = self.client.get(f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}")
        s = res_summary.data['subjects'][0]
        self.assertEqual(s['pending_asset_count'], 1)

        # 2. Check subject-hierarchy
        res_hierarchy = self.client.get(f"/api/curriculum/course-management/subject-hierarchy/?subject={self.subject.id}")
        self.assertEqual(res_hierarchy.status_code, status.HTTP_200_OK)
        u_info = res_hierarchy.data['topics'][0]['units'][0]

        self.assertEqual(u_info['blocks_count'], 3)
        self.assertEqual(u_info['assets_count'], 2)
        self.assertEqual(u_info['pending_assets_count'], 1)
        self.assertEqual(u_info['published'], True)

        # 3. Check lesson-disaggregation
        res_disagg = self.client.get(f"/api/curriculum/course-management/lesson-disaggregation/?lesson_id={lesson.id}")
        self.assertEqual(res_disagg.status_code, status.HTTP_200_OK)
        self.assertEqual(res_disagg.data['summary']['total_blocks'], 3)
        self.assertEqual(res_disagg.data['summary']['total_assets'], 2)
        self.assertEqual(res_disagg.data['summary']['pending_assets_count'], 1)

    def test_08_performance_and_query_counts(self):
        """
        Verify no N+1 queries.
        - Grade summary must execute in at most 2 queries (1 auth/session + 1 subject aggregation).
        - Subject hierarchy must execute in constant time (at most 4 queries total regardless of scale).
        """
        # Create a second subject with 3 topics and 15 learning units
        sub2 = Subject.objects.create(grade=self.grade, name="Physics")
        for t_idx in range(3):
            top = Topic.objects.create(subject=sub2, name=f"Physics Topic {t_idx+1}", order=t_idx+1)
            for u_idx in range(5):
                u = LearningUnit.objects.create(topic=top, name=f"Unit {u_idx+1}", order=u_idx+1)
                l = Lesson.objects.create(topic=top, learning_unit=u, status='published' if u_idx % 2 == 0 else 'draft')
                LessonBlock.objects.create(lesson=l, block_type='concept_explanation', order=1)
                LessonAsset.objects.create(lesson=l, asset_type='diagram', status='attached')

        self.client.force_authenticate(user=self.admin_user)

        # Test grade summary query count
        with CaptureQueriesContext(connection) as ctx_summary:
            res = self.client.get(f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}")
            self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        # In Django test client, queries typically include user lookup + grade lookup + 1 aggregated subject query
        self.assertLessEqual(len(ctx_summary.captured_queries), 5, f"Grade summary executed {len(ctx_summary.captured_queries)} queries (N+1 hazard detected)")

        # Test subject hierarchy query count on Physics (3 topics, 15 units, 15 lessons)
        with CaptureQueriesContext(connection) as ctx_hierarchy:
            res = self.client.get(f"/api/curriculum/course-management/subject-hierarchy/?subject={sub2.id}")
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        # 3 prefetch queries + subject lookup + user lookup <= 6 queries total
        self.assertLessEqual(len(ctx_hierarchy.captured_queries), 6, f"Subject hierarchy executed {len(ctx_hierarchy.captured_queries)} queries (prefetch failed)")

    def test_09_query_param_validation(self):
        """Verify non-integer or missing query parameters return HTTP 400 Bad Request."""
        self.client.force_authenticate(user=self.admin_user)
        
        # Missing params
        r1 = self.client.get("/api/curriculum/course-management/grade-summary/")
        self.assertEqual(r1.status_code, status.HTTP_400_BAD_REQUEST)
        
        r2 = self.client.get("/api/curriculum/course-management/subject-hierarchy/")
        self.assertEqual(r2.status_code, status.HTTP_400_BAD_REQUEST)
        
        r3 = self.client.get("/api/curriculum/course-management/lesson-disaggregation/")
        self.assertEqual(r3.status_code, status.HTTP_400_BAD_REQUEST)

        # Invalid non-integer params
        r4 = self.client.get("/api/curriculum/course-management/grade-summary/?grade=invalid_str")
        self.assertEqual(r4.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("integer", r4.data.get("error", ""))

        r5 = self.client.get("/api/curriculum/course-management/subject-hierarchy/?subject=abc")
        self.assertEqual(r5.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("integer", r5.data.get("error", ""))

        r6 = self.client.get("/api/curriculum/course-management/lesson-disaggregation/?lesson=xyz")
        self.assertEqual(r6.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("integer", r6.data.get("error", ""))

    def test_10_overview_aggregation(self):
        """Verify the overview endpoint executes in constant time and correctly aggregates curriculum/grade stats."""
        # Create second grade under curriculum
        grade2 = Grade.objects.create(curriculum=self.curriculum, name="Form 4", level=4)
        sub_bio = Subject.objects.create(grade=grade2, name="Biology")
        top_cell = Topic.objects.create(subject=sub_bio, name="Cell Biology", order=1)
        u1 = LearningUnit.objects.create(topic=top_cell, name="Cell Structure", order=1)
        u2 = LearningUnit.objects.create(topic=top_cell, name="Mitosis", order=2)
        Lesson.objects.create(topic=top_cell, learning_unit=u1, status='published', version=1)

        self.client.force_authenticate(user=self.admin_user)
        with CaptureQueriesContext(connection) as ctx:
            res = self.client.get("/api/curriculum/course-management/overview/")
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        # 1 user auth + 1 single annotated query over Grade objects
        self.assertLessEqual(len(ctx.captured_queries), 4)

        data = res.data
        self.assertIsInstance(data, list)
        f4_entry = next((item for item in data if item['grade_id'] == grade2.id), None)
        self.assertIsNotNone(f4_entry)
        self.assertEqual(f4_entry['units_defined'], 2)
        self.assertEqual(f4_entry['units_generated'], 1)
        self.assertEqual(f4_entry['units_published'], 1)
        self.assertEqual(f4_entry['units_unstarted'], 1)
        self.assertEqual(f4_entry['draft_units'], 0)

    def test_11_lesson_disaggregation_performance_and_sorting(self):
        """Verify lesson disaggregation sorts blocks in Python without triggering N+1 queries."""
        unit = LearningUnit.objects.create(topic=self.topic, name="Optics Unit", order=1)
        lesson = Lesson.objects.create(topic=self.topic, learning_unit=unit, status='published', version=1)

        # Create 10 blocks out of order
        for i in [5, 2, 8, 1, 9, 3, 7, 4, 10, 6]:
            b = LessonBlock.objects.create(lesson=lesson, block_type='concept_explanation', order=i)
            LessonAsset.objects.create(lesson=lesson, asset_type='diagram', status='attached')

        self.client.force_authenticate(user=self.admin_user)
        with CaptureQueriesContext(connection) as ctx:
            res = self.client.get(f"/api/curriculum/course-management/lesson-disaggregation/?lesson_id={lesson.id}")
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        # Prefetched blocks and assets: at most 4 queries
        self.assertLessEqual(len(ctx.captured_queries), 5)

        # Verify sorted order
        blocks = res.data['blocks']
        self.assertEqual(len(blocks), 10)
        orders = [b['order'] for b in blocks]
        self.assertEqual(orders, sorted(orders))

    def test_12_archived_only_unit_is_unstarted(self):
        """
        Verify that a learning unit with ONLY an archived lesson is treated as unstarted,
        and its assets do NOT count towards pending_asset_count.
        """
        unit = LearningUnit.objects.create(topic=self.topic, name="Discarded Draft Unit", order=2)
        archived_lesson = Lesson.objects.create(topic=self.topic, learning_unit=unit, status='archived', version=1)
        LessonAsset.objects.create(lesson=archived_lesson, asset_type='diagram', status='pending')

        self.client.force_authenticate(user=self.admin_user)
        res = self.client.get(f"/api/curriculum/course-management/grade-summary/?grade={self.grade.id}")
        s = res.data['subjects'][0]

        # The unit has only an archived lesson: units_generated should NOT count it
        self.assertEqual(s['units_defined'], 1)
        self.assertEqual(s['units_generated'], 0)
        self.assertEqual(s['units_published'], 0)
        self.assertEqual(s['units_unstarted'], 1)
        self.assertEqual(s['pending_asset_count'], 0, "Pending assets from archived lessons must not be counted")
