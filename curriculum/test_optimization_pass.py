import uuid
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.utils import CaptureQueriesContext
from django.db import connection
from rest_framework.test import APIClient
from rest_framework import status

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset, VisualGenerationJob, VisualizationIssueReport
)
from curriculum.ai_ingestion.visual_agent import VisualGeneratorAgent

User = get_user_model()


class OptimizationPassTests(TestCase):
    """
    Test suite verifying the Admin Portal Optimization Pass:
    1. Curriculum Builder progress annotations on SubjectViewSet and TopicViewSet.
    2. LessonViewSet.generate_visual targeted visual generation API endpoint (replace vs insert).
    3. VisualGeneratorAgent execution, contextual prompting, and transactional fallback resilience.
    """

    def setUp(self):
        self.client = APIClient()

        # Admin user
        self.admin_user = User.objects.create_user(
            username=f'admin_{uuid.uuid4().hex[:8]}',
            email=f'admin_{uuid.uuid4().hex[:8]}@example.com',
            password='AdminPassword123!',
            role='platform_admin',
            is_staff=True,
        )

        # Student user
        self.student_user = User.objects.create_user(
            username=f'student_{uuid.uuid4().hex[:8]}',
            email=f'student_{uuid.uuid4().hex[:8]}@example.com',
            password='StudentPassword123!',
            role='student',
        )

        # Base curriculum structure
        self.curriculum = Curriculum.objects.create(name=f"Curriculum_{uuid.uuid4().hex[:6]}")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 2", level=2)
        self.subject = Subject.objects.create(grade=self.grade, name="Physics")

        # Two topics
        self.topic1 = Topic.objects.create(subject=self.subject, name="Topic 1: Mechanics", order=1)
        self.topic2 = Topic.objects.create(subject=self.subject, name="Topic 2: Waves", order=2)

        # Units for topic 1: 3 units
        self.u1 = LearningUnit.objects.create(topic=self.topic1, name="Unit 1: Force", order=1)
        self.u2 = LearningUnit.objects.create(topic=self.topic1, name="Unit 2: Work", order=2)
        self.u3 = LearningUnit.objects.create(topic=self.topic1, name="Unit 3: Energy", order=3)

        # Units for topic 2: 2 units
        self.u4 = LearningUnit.objects.create(topic=self.topic2, name="Unit 4: Wave Properties", order=1)
        self.u5 = LearningUnit.objects.create(topic=self.topic2, name="Unit 5: Sound Waves", order=2)

        # Lessons:
        # u1 -> published
        self.l1 = Lesson.objects.create(topic=self.topic1, learning_unit=self.u1, title="Lesson on Force", status='published', version=1)
        # u2 -> draft (generated, not published)
        self.l2 = Lesson.objects.create(topic=self.topic1, learning_unit=self.u2, title="Lesson on Work", status='draft', version=1)
        # u3 -> unstarted (no lesson)
        # u4 -> published
        self.l4 = Lesson.objects.create(topic=self.topic2, learning_unit=self.u4, title="Lesson on Waves", status='published', version=1)
        # u5 -> unstarted (no lesson)

    # ──────────────────────────────────────────────────────────────────────────
    # 1. CURRICULUM BUILDER PROGRESS ANNOTATIONS
    # ──────────────────────────────────────────────────────────────────────────

    def test_01_subject_progress_annotations(self):
        """
        Verify SubjectViewSet.get_queryset() returns accurate aggregate annotations
        without requiring N+1 subqueries:
        - topics_count = 2
        - units_count = 5
        - lessons_generated_count = 3 (l1, l2, l4)
        - lessons_published_count = 2 (l1, l4)
        """
        self.client.force_authenticate(user=self.admin_user)
        with CaptureQueriesContext(connection) as ctx:
            res = self.client.get(f"/api/curriculum/subjects/?grade={self.grade.id}")
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        # Constant queries (no N+1 per subject)
        self.assertLessEqual(len(ctx.captured_queries), 5)

        data = res.data if isinstance(res.data, list) else res.data.get('results', [])
        subject_data = next((s for s in data if s['id'] == self.subject.id), None)
        self.assertIsNotNone(subject_data)
        self.assertEqual(subject_data['topics_count'], 2)
        self.assertEqual(subject_data['units_count'], 5)
        self.assertEqual(subject_data['lessons_generated_count'], 3)
        self.assertEqual(subject_data['lessons_published_count'], 2)

    def test_02_topic_progress_annotations(self):
        """
        Verify TopicViewSet.get_queryset() returns units_count and published_lessons_count:
        - Topic 1: units_count = 3, published_lessons_count = 1
        - Topic 2: units_count = 2, published_lessons_count = 1
        """
        self.client.force_authenticate(user=self.admin_user)
        with CaptureQueriesContext(connection) as ctx:
            res = self.client.get(f"/api/curriculum/topics/?subject={self.subject.id}")
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertLessEqual(len(ctx.captured_queries), 5)

        data = res.data if isinstance(res.data, list) else res.data.get('results', [])
        t1_data = next((t for t in data if t['id'] == self.topic1.id), None)
        t2_data = next((t for t in data if t['id'] == self.topic2.id), None)

        self.assertIsNotNone(t1_data)
        self.assertEqual(t1_data['units_count'], 3)
        self.assertEqual(t1_data['published_lessons_count'], 1)

        self.assertIsNotNone(t2_data)
        self.assertEqual(t2_data['units_count'], 2)
        self.assertEqual(t2_data['published_lessons_count'], 1)

    # ──────────────────────────────────────────────────────────────────────────
    # 2. TARGETED VISUAL GENERATION API (LessonViewSet.generate_visual)
    # ──────────────────────────────────────────────────────────────────────────

    def test_03_generate_visual_permission_and_validation(self):
        """Verify endpoint rejects unauthenticated/unauthorized users and empty prompt."""
        url = f"/api/curriculum/lessons/{self.l1.id}/generate-visual/"

        # 1. Unauthenticated
        res = self.client.post(url, {"prompt": "Diagram"})
        self.assertIn(res.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

        # 2. Student user
        self.client.force_authenticate(user=self.student_user)
        res = self.client.post(url, {"prompt": "Diagram"})
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

        # 3. Platform Admin with empty prompt
        self.client.force_authenticate(user=self.admin_user)
        res = self.client.post(url, {"prompt": "   "})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('curriculum.tasks.dispatch_background_task')
    def test_04_generate_visual_replace_existing_block(self, mock_dispatch):
        """
        Verify that calling generate-visual with placement='replace' and target_block_id:
        - Updates the existing block's metadata and title directly.
        - Does NOT create a redundant extra LessonBlock.
        - Creates a VisualGenerationJob for that block with status='pending'.
        - Does NOT fail with NameError (models import fix verified).
        """
        self.client.force_authenticate(user=self.admin_user)

        # Existing block on lesson
        block = LessonBlock.objects.create(
            lesson=self.l1,
            block_type='suggested_diagram',
            title='Initial Diagram',
            content={'description': 'Original rough description'},
            order=1,
            page_number=1,
        )

        initial_block_count = self.l1.blocks.count()

        url = f"/api/curriculum/lessons/{self.l1.id}/generate-visual/"
        payload = {
            "prompt": "Show detailed vectors for resultant force",
            "target_block_id": block.id,
            "placement": "replace",
            "visual_type": "suggested_diagram"
        }

        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn('visual_job_id', res.data)
        self.assertEqual(res.data['block_id'], block.id)

        # Block count unchanged (no duplicate block created)
        self.assertEqual(self.l1.blocks.count(), initial_block_count)

        # Verify block was updated
        block.refresh_from_db()
        self.assertIn("AI Visual: Show detailed vectors", block.title)
        self.assertEqual(block.metadata.get('user_prompt'), "Show detailed vectors for resultant force")
        self.assertEqual(block.metadata.get('last_updated_via'), 'targeted_ai_prompt')

        # Verify job was created
        job = VisualGenerationJob.objects.get(id=res.data['visual_job_id'])
        self.assertEqual(job.lesson_block, block)
        self.assertEqual(job.status, 'pending')
        self.assertEqual(job.prompt, "Show detailed vectors for resultant force")

        # Verify task was dispatched
        mock_dispatch.assert_called_once()

    @patch('curriculum.tasks.dispatch_background_task')
    def test_05_generate_visual_insert_after(self, mock_dispatch):
        """
        Verify that calling generate-visual with placement='after':
        - Shifts subsequent block orders without NameError on models.F.
        - Inserts a new block with order = target.order + 1.
        - Creates VisualGenerationJob.
        """
        self.client.force_authenticate(user=self.admin_user)

        b1 = LessonBlock.objects.create(lesson=self.l1, block_type='concept_explanation', order=1, page_number=1)
        b2 = LessonBlock.objects.create(lesson=self.l1, block_type='summary', order=2, page_number=1)

        url = f"/api/curriculum/lessons/{self.l1.id}/generate-visual/"
        payload = {
            "prompt": "Diagram between explanation and summary",
            "target_block_id": b1.id,
            "placement": "after",
            "visual_type": "suggested_diagram"
        }

        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

        new_block = LessonBlock.objects.get(id=res.data['block_id'])
        self.assertEqual(new_block.order, 2)

        # b2 order should have shifted from 2 to 3
        b2.refresh_from_db()
        self.assertEqual(b2.order, 3)

    # ──────────────────────────────────────────────────────────────────────────
    # 3. VISUAL GENERATOR AGENT RESILIENCE & TRANSACTIONAL REPLACEMENT
    # ──────────────────────────────────────────────────────────────────────────

    @patch('curriculum.media_orchestration.visual_intelligence.reasoner.VisualReasoner.evaluate_requirement')
    def test_06_agent_success_safely_replaces_asset(self, mock_evaluate):
        """
        When VisualReasoner returns a valid visual specification:
        - New LessonAsset is created with status='attached' and generated SVG code in metadata.
        - Old LessonAsset is detached and marked 'archived'.
        - Job is completed.
        """
        block = LessonBlock.objects.create(lesson=self.l1, block_type='suggested_diagram', order=1, page_number=1)
        old_asset = LessonAsset.objects.create(
            lesson=self.l1, asset_type='diagram', status='attached', title='Old Diagram'
        )
        old_asset.blocks.add(block)

        job = VisualGenerationJob.objects.create(
            lesson_block=block,
            prompt="Free body diagram with normal and gravitational forces",
        )

        # Mock reasoner returning success
        mock_spec = MagicMock()
        mock_spec.code = "<svg><rect width='100' height='100'/></svg>"
        mock_spec.format = "svg"
        mock_spec.alt_text = "Free body diagram showing balanced vertical forces"
        mock_evaluate.return_value = (mock_spec, None)

        VisualGeneratorAgent.run(job.id)

        job.refresh_from_db()
        self.assertEqual(job.status, 'completed')
        self.assertIsNotNone(job.result_asset)

        # New asset is attached to block
        new_asset = job.result_asset
        self.assertEqual(new_asset.status, 'attached')
        self.assertEqual(new_asset.metadata.get('generated_code'), mock_spec.code)
        self.assertIn(block, new_asset.blocks.all())

        # Old asset is detached and archived
        old_asset.refresh_from_db()
        self.assertEqual(old_asset.status, 'archived')
        self.assertNotIn(block, old_asset.blocks.all())

    @patch('curriculum.media_orchestration.visual_intelligence.reasoner.VisualReasoner.evaluate_requirement')
    def test_07_agent_failure_preserves_existing_asset(self, mock_evaluate):
        """
        When VisualReasoner fails:
        - Existing working LessonAsset is NOT destroyed, remains attached and untouched.
        - Job status is set to 'failed' with error_message.
        """
        block = LessonBlock.objects.create(lesson=self.l1, block_type='suggested_diagram', order=1, page_number=1)
        existing_asset = LessonAsset.objects.create(
            lesson=self.l1, asset_type='diagram', status='attached', title='Working Diagram v1'
        )
        existing_asset.blocks.add(block)

        job = VisualGenerationJob.objects.create(
            lesson_block=block,
            prompt="Make an overly complex interactive 3D simulation",
        )

        # Mock reasoner returning failure
        mock_failure = MagicMock()
        mock_failure.reason = "VisualReasoner unable to satisfy constraints for requested 3D simulation."
        mock_evaluate.return_value = (None, mock_failure)

        VisualGeneratorAgent.run(job.id)

        job.refresh_from_db()
        self.assertEqual(job.status, 'failed')
        self.assertIn("unable to satisfy constraints", job.error_message)

        # CRITICAL: Existing working asset is preserved
        existing_asset.refresh_from_db()
        self.assertEqual(existing_asset.status, 'attached')
        self.assertIn(block, existing_asset.blocks.all())

    # ──────────────────────────────────────────────────────────────────────────
    # 4. USER COUNTS BREAKDOWN & VISUALIZATION ISSUE REPORTS
    # ──────────────────────────────────────────────────────────────────────────

    def test_08_user_count_breakdown_metrics(self):
        """
        Verify /users-count/ returns:
        - enrolled_learners (students)
        - other_users (total_users - enrolled_learners)
        - teachers
        - school_admins
        - platform_admins
        - backward-compatible user_count
        """
        # Create an additional teacher and school admin
        User.objects.create_user(
            username=f'teacher_{uuid.uuid4().hex[:8]}',
            email=f'teacher_{uuid.uuid4().hex[:8]}@example.com',
            password='Password123!',
            role='teacher',
        )
        User.objects.create_user(
            username=f'admin_school_{uuid.uuid4().hex[:8]}',
            email=f'school_{uuid.uuid4().hex[:8]}@example.com',
            password='Password123!',
            role='school_admin',
        )

        self.client.force_authenticate(user=self.admin_user)
        res = self.client.get('/users-count/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data

        self.assertIn('enrolled_learners', data)
        self.assertIn('other_users', data)
        self.assertIn('teachers', data)
        self.assertIn('school_admins', data)
        self.assertIn('platform_admins', data)
        self.assertIn('total_users', data)
        self.assertIn('user_count', data)

        self.assertEqual(data['enrolled_learners'], 1)  # self.student_user
        self.assertEqual(data['teachers'], 1)
        self.assertEqual(data['school_admins'], 1)
        self.assertEqual(data['platform_admins'], 1)   # self.admin_user
        self.assertEqual(data['other_users'], data['total_users'] - data['enrolled_learners'])

    def test_09_visualization_issue_pedagogical_coordinates_and_resolve(self):
        """
        Verify /api/curriculum/visualization-issues/ returns full pedagogical coordinates:
        - learning_unit_id and learning_unit_title
        - subject_name, topic_name, grade_name
        - block_title, block_type, block_page_number
        - user_email, user_role
        And verify the resolve action works with custom resolution notes.
        """
        block = LessonBlock.objects.create(
            lesson=self.l1,
            block_type='simulation',
            order=2,
            page_number=3,
            content={'title': 'Newton Third Law Sim', 'narrative': 'Test simulation block'}
        )

        issue = VisualizationIssueReport.objects.create(
            user=self.student_user,
            lesson=self.l1,
            lesson_block=block,
            visualization_title="Action Reaction Simulation",
            visualization_type="simulation",
            issue_type="simulation_broken",
            description="The slider for mass does not update acceleration in real-time.",
            status="pending"
        )

        self.client.force_authenticate(user=self.admin_user)
        res = self.client.get('/api/curriculum/visualization-issues/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        issues = res.data if isinstance(res.data, list) else res.data.get('results', [])
        found = next((i for i in issues if i['id'] == issue.id), None)
        self.assertIsNotNone(found)

        # Verify pedagogical coordinates
        self.assertEqual(found['learning_unit_id'], self.u1.id)
        self.assertEqual(found['learning_unit_title'], self.u1.name)
        self.assertEqual(found['subject_name'], "Physics")
        self.assertEqual(found['grade_name'], "Form 2")
        self.assertEqual(found['topic_name'], "Topic 1: Mechanics")
        self.assertEqual(found['lesson_title'], "Lesson on Force")
        self.assertEqual(found['block_page_number'], 3)
        self.assertEqual(found['block_type'], 'simulation')
        self.assertEqual(found['user_email'], self.student_user.email)
        self.assertEqual(found['user_role'], 'student')

        # Test resolve endpoint
        resolve_res = self.client.post(f'/api/curriculum/visualization-issues/{issue.id}/resolve/', {
            'resolution_notes': 'Fixed slider state synchronization in Content Studio.'
        })
        self.assertEqual(resolve_res.status_code, status.HTTP_200_OK)
        self.assertEqual(resolve_res.data['status'], 'resolved')
        self.assertEqual(resolve_res.data['resolution_notes'], 'Fixed slider state synchronization in Content Studio.')

        issue.refresh_from_db()
        self.assertEqual(issue.status, 'resolved')
        self.assertIsNotNone(issue.resolved_at)

