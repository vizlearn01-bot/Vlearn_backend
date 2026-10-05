from django.test import TestCase
from unittest.mock import patch, MagicMock
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, Lesson, LessonBlock, LessonAsset,
    VisualizationIssueReport, VisualGenerationJob
)
from curriculum.media_orchestration.contracts import MediaRequirement
from curriculum.media_orchestration.visual_intelligence.engine import VisualIntelligenceEngine
from curriculum.media_orchestration.assembler import ExperienceAssemblyService
from curriculum.ai_ingestion.visual_agent import VisualGeneratorAgent
from curriculum.media_orchestration.contracts import ResolvedAsset

User = get_user_model()


class TestDeploymentRemediation(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.curriculum = Curriculum.objects.create(name="CBC High School")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Grade 10", level=10)
        self.subject = Subject.objects.create(grade=self.grade, name="Physics")
        self.topic = Topic.objects.create(subject=self.subject, name="Mechanics")
        self.lesson = Lesson.objects.create(topic=self.topic, title="Newton's Laws")
        self.block = LessonBlock.objects.create(
            lesson=self.lesson,
            block_id="step_photo_1",
            block_type="suggested_image",
            title="Real-world Example",
            content={"title": "Car on Road", "status": "draft"},
            order=1,
            page_number=1
        )

        self.admin_user = User.objects.create_superuser(
            username="admin_user",
            email="admin@vlearn.co.ke",
            password="adminpassword123"
        )

    def test_unauthenticated_issue_reporting_with_invalid_token(self):
        """
        Verify that learners with expired or corrupted bearer tokens can successfully
        report an issue anonymously without being blocked by HTTP 401.
        """
        self.client.credentials(HTTP_AUTHORIZATION="Bearer corrupted_or_expired_jwt_token_xyz")
        payload = {
            "visualization_title": "Broken Simulation on Friction",
            "visualization_type": "simulation",
            "issue_type": "simulation_broken",
            "description": "Simulation canvas is blank on mobile browser.",
            "lesson": self.lesson.id,
            "lesson_block": self.block.id
        }
        response = self.client.post("/api/curriculum/visualization-issues/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        report = VisualizationIssueReport.objects.get(id=response.data["id"])
        self.assertIsNone(report.user)
        self.assertEqual(report.status, "pending")
        self.assertEqual(report.issue_type, "simulation_broken")

    def test_issue_report_read_only_fields_hardening(self):
        """
        Verify that callers cannot spoof the reporter, force status='resolved',
        or inject resolution notes during issue creation.
        """
        self.client.credentials()  # unauthenticated
        payload = {
            "visualization_title": "Untrusted Submission",
            "visualization_type": "diagram",
            "issue_type": "content_error",
            "description": "Typo in diagram label",
            "user": self.admin_user.id,
            "status": "resolved",
            "resolution_notes": "Illicit resolution notes"
        }
        response = self.client.post("/api/curriculum/visualization-issues/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        report = VisualizationIssueReport.objects.get(id=response.data["id"])
        self.assertIsNone(report.user)
        self.assertEqual(report.status, "pending")
        self.assertEqual(report.resolution_notes, "")

    def test_issue_reporting_summary_endpoint(self):
        """
        Verify that /api/curriculum/visualization-issues/summary/ returns unpaginated,
        accurate database aggregate counts for admin navigation badges.
        """
        VisualizationIssueReport.objects.create(
            visualization_title="Issue 1",
            visualization_type="video",
            issue_type="youtube_unavailable",
            status="pending"
        )
        VisualizationIssueReport.objects.create(
            visualization_title="Issue 2",
            visualization_type="simulation",
            issue_type="simulation_broken",
            status="investigating"
        )
        VisualizationIssueReport.objects.create(
            visualization_title="Issue 3",
            visualization_type="diagram",
            issue_type="content_error",
            status="resolved"
        )

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get("/api/curriculum/visualization-issues/summary/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(data["total_reports"], 3)
        self.assertEqual(data["total_open"], 2)
        self.assertEqual(data["total_resolved"], 1)

    def test_visual_intelligence_engine_image_vs_diagram_classification(self):
        """
        Verify that VisualIntelligenceEngine._is_generatable returns False for
        photographic/concrete/video/simulation media, and True for diagrams.
        """
        engine = VisualIntelligenceEngine()

        # Image requirement -> should NOT be generatable (external retrieval needed)
        image_req = MediaRequirement(
            node_id="n1",
            preferred_media_type="image",
            search_keywords=["microscope", "cell"]
        )
        self.assertFalse(engine._is_generatable(image_req))

        # Photo requirement -> should NOT be generatable
        photo_req = MediaRequirement(
            node_id="n2",
            preferred_media_type="photo",
            search_keywords=["granite", "rock"]
        )
        self.assertFalse(engine._is_generatable(photo_req))

        # Video requirement -> should NOT be generatable
        video_req = MediaRequirement(
            node_id="n3",
            preferred_media_type="video"
        )
        self.assertFalse(engine._is_generatable(video_req))

        # Simulation requirement -> should NOT be generatable
        sim_req = MediaRequirement(
            node_id="n4",
            preferred_media_type="simulation"
        )
        self.assertFalse(engine._is_generatable(sim_req))

        # Diagram requirement -> SHOULD be generatable
        diagram_req = MediaRequirement(
            node_id="n5",
            preferred_media_type="diagram",
            search_keywords=["flowchart", "carbon cycle"]
        )
        self.assertTrue(engine._is_generatable(diagram_req))

    def test_assembler_asset_type_mapping(self):
        """
        Verify that ExperienceAssemblyService maps generated SVG and Mermaid assets
        to suggested_diagram blocks.
        """
        assembler = ExperienceAssemblyService()
        self.assertEqual(assembler._map_asset_type_to_block_type("generated_svg"), "suggested_diagram")
        self.assertEqual(assembler._map_asset_type_to_block_type("generated_mermaid"), "suggested_diagram")
        self.assertEqual(assembler._map_asset_type_to_block_type("diagram"), "suggested_diagram")
        self.assertEqual(assembler._map_asset_type_to_block_type("image"), "image_placeholder")

    @patch("curriculum.media_orchestration.providers.wikimedia.WikimediaProvider.search")
    def test_visual_agent_fetches_wikimedia_for_image_slot(self, mock_wikimedia_search):
        """
        Verify that VisualGeneratorAgent queries WikimediaProvider when the target block
        is an image slot and attaches the resulting Wikimedia asset instead of drawing SVG.
        """
        mock_asset = ResolvedAsset(
            node_id="test_node",
            asset_type="image",
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Newton_Cradle.jpg/800px-Newton_Cradle.jpg",
            provenance="Wikimedia Commons",
            licensing="CC BY-SA 4.0",
            author="Science Photographer",
            attribution="By Science Photographer (CC BY-SA 4.0)",
            alt_text="A high resolution photograph of Newton's Cradle demonstration",
            confidence_score=0.95
        )
        mock_wikimedia_search.return_value = [mock_asset]

        job = VisualGenerationJob.objects.create(
            lesson_block=self.block,
            prompt="Find a photograph of Newton's cradle in action",
            status="pending"
        )

        VisualGeneratorAgent.run(job.id)

        job.refresh_from_db()
        self.assertEqual(job.status, "completed")
        self.assertIsNotNone(job.result_asset)
        self.assertEqual(job.result_asset.source_type, "wikimedia")
        self.assertEqual(job.result_asset.asset_type, "image")
        self.assertIn("Newton_Cradle.jpg", job.result_asset.url)

        self.block.refresh_from_db()
        self.assertEqual(self.block.content.get("status"), "ready")
        self.assertIn("Newton_Cradle.jpg", self.block.content.get("url"))
        self.assertEqual(self.block.content.get("provenance"), "Wikimedia Commons")
