import uuid
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset, GenerationJob
)

User = get_user_model()


class ContentStudioRemediationTests(TestCase):
    """
    Automated verification suite for Content Studio UX remediation fixes:
    1. Lesson context fields (breadcrumbs) in serializers.
    2. Zero pagination truncation on LessonBlockViewSet (>20 blocks returned).
    3. Zero pagination truncation on LessonAssetViewSet.
    4. Atomic synchronization of `order` and `component_order` on reorder.
    5. Block update with page_title and content persistence.
    6. GenerationJobSerializer null learning_unit safety.
    """

    def setUp(self):
        self.client = APIClient()

        # Admin user
        self.admin = User.objects.create_user(
            username=f'cs_admin_{uuid.uuid4().hex[:6]}',
            email=f'cs_admin_{uuid.uuid4().hex[:6]}@test.com',
            password='TestPassword123!',
            role='platform_admin',
            is_staff=True,
        )
        self.client.force_authenticate(user=self.admin)

        # Hierarchy
        self.curriculum = Curriculum.objects.create(name=f"CBC_Test_{uuid.uuid4().hex[:4]}")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Grade 10", level=10)
        self.subject = Subject.objects.create(grade=self.grade, name="Physics")
        self.topic = Topic.objects.create(subject=self.subject, name="Topic 1: Introduction to Mechanics", order=1)
        self.learning_unit = LearningUnit.objects.create(
            topic=self.topic,
            name="LU 1.1: Motion and Forces",
            order=1,
        )
        self.lesson = Lesson.objects.create(
            topic=self.topic,
            learning_unit=self.learning_unit,
            title="Newton's Laws of Motion",
            status='draft',
            version=1,
        )

    def test_01_lesson_serializer_context_breadcrumbs(self):
        """Verify lesson detail endpoint returns curriculum hierarchy breadcrumbs."""
        res_v1 = self.client.get(f"/api/curriculum/lessons/{self.lesson.id}/")
        self.assertEqual(res_v1.status_code, status.HTTP_200_OK)
        data_v1 = res_v1.data
        self.assertEqual(data_v1['topic_name'], "Topic 1: Introduction to Mechanics")
        self.assertEqual(data_v1['subject_id'], self.subject.id)
        self.assertEqual(data_v1['subject_name'], "Physics")
        self.assertEqual(data_v1['grade_name'], "Grade 10")
        self.assertEqual(data_v1['learning_unit_name'], "LU 1.1: Motion and Forces")

        # Test V2 serializer
        res_v2 = self.client.get(f"/api/curriculum/lessons/{self.lesson.id}/?v=2")
        self.assertEqual(res_v2.status_code, status.HTTP_200_OK)
        data_v2 = res_v2.data
        self.assertEqual(data_v2['topic_name'], "Topic 1: Introduction to Mechanics")
        self.assertEqual(data_v2['subject_name'], "Physics")
        self.assertEqual(data_v2['learning_unit_name'], "LU 1.1: Motion and Forces")

    def test_02_lesson_blocks_pagination_disabled(self):
        """Verify lesson blocks viewset returns ALL blocks (>20 blocks) without truncation."""
        # Create 28 blocks (exceeding default page size of 20)
        blocks = []
        for i in range(28):
            blocks.append(
                LessonBlock(
                    lesson=self.lesson,
                    block_type='concept_explanation',
                    title=f"Block {i+1}",
                    content={"text": f"Content for block {i+1}"},
                    order=i,
                    component_order=i,
                    page_number=(i // 4) + 1,
                    page_title=f"Card {(i // 4) + 1}",
                )
            )
        LessonBlock.objects.bulk_create(blocks)

        res = self.client.get(f"/api/curriculum/lesson-blocks/?lesson={self.lesson.id}")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Should be a flat list of 28 blocks, not a paginated dict {count: 28, results: [...20 items...]}
        self.assertIsInstance(res.data, list, "LessonBlockViewSet response must be a flat list (pagination_class = None)")
        self.assertEqual(len(res.data), 28, "All 28 blocks must be returned without truncation")

    def test_03_lesson_assets_pagination_disabled(self):
        """Verify lesson assets viewset returns ALL assets without pagination truncation."""
        assets = []
        for i in range(25):
            assets.append(
                LessonAsset(
                    lesson=self.lesson,
                    asset_type='diagram',
                    title=f"Diagram {i+1}",
                    url=f"https://example.com/asset_{i+1}.svg",
                    status='attached',
                )
            )
        LessonAsset.objects.bulk_create(assets)

        res = self.client.get(f"/api/curriculum/lesson-assets/?lesson={self.lesson.id}")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.data, list, "LessonAssetViewSet response must be a flat list (pagination_class = None)")
        self.assertEqual(len(res.data), 25, "All 25 assets must be returned")

    def test_04_reorder_synchronizes_order_and_component_order(self):
        """Verify reordering updates both order and component_order simultaneously."""
        b1 = LessonBlock.objects.create(
            lesson=self.lesson,
            block_type='hook',
            title="Hook Block",
            content={"text": "Engage"},
            order=0,
            component_order=0,
        )
        b2 = LessonBlock.objects.create(
            lesson=self.lesson,
            block_type='concept_explanation',
            title="Concept Block",
            content={"text": "Explain"},
            order=1,
            component_order=1,
        )

        # Reverse the order via reorder endpoint
        reorder_payload = {
            "ordering": [
                {"id": b1.id, "order": 1},
                {"id": b2.id, "order": 0},
            ]
        }
        res = self.client.post("/api/curriculum/lesson-blocks/reorder/", reorder_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        b1.refresh_from_db()
        b2.refresh_from_db()

        self.assertEqual(b1.order, 1)
        self.assertEqual(b1.component_order, 1, "component_order must be synchronized with order")
        self.assertEqual(b2.order, 0)
        self.assertEqual(b2.component_order, 0, "component_order must be synchronized with order")

    def test_05_block_update_page_title_and_content(self):
        """Verify partial update of block preserves page_title and content."""
        block = LessonBlock.objects.create(
            lesson=self.lesson,
            block_type='concept_explanation',
            title="Original Title",
            content={"text": "Original text"},
            order=0,
            component_order=0,
            page_number=1,
            page_title="Card 1: Introduction",
        )

        patch_data = {
            "page_title": "Card 1: Renamed Title",
            "content": {"text": "Updated **bold** content with $E=mc^2$"},
        }
        res = self.client.patch(f"/api/curriculum/lesson-blocks/{block.id}/", patch_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        block.refresh_from_db()
        self.assertEqual(block.page_title, "Card 1: Renamed Title")
        self.assertEqual(block.content['text'], "Updated **bold** content with $E=mc^2$")

    def test_06_generation_job_serializer_null_learning_unit(self):
        """Verify GenerationJobSerializer handles lessons without a learning unit safely."""
        lesson_no_lu = Lesson.objects.create(
            topic=self.topic,
            learning_unit=None,
            title="Orphan Lesson",
            status='draft',
        )
        job = GenerationJob.objects.create(
            lesson=lesson_no_lu,
            status='completed',
        )
        from curriculum.api.serializers import GenerationJobSerializer
        serializer = GenerationJobSerializer(job)
        self.assertIsNone(serializer.data['learning_unit_id'], "Null learning_unit should serialize as None without error")
