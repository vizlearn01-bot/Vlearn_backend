from django.test import TestCase
from unittest.mock import patch, MagicMock
from .contracts import (
    MediaRequirement, MediaManifest, ResolvedAsset
)
from curriculum.generation.planner.models import LearningExperiencePlan, StrategyNode, InstructionalIntent, PersonalizationOpportunities
from .planner import MediaPlanner
from .acquisition import MediaAcquisitionEngine
from .adapters import WikimediaAdapter, KnowledgeRepoAdapter, SimulationAdapter
from .assembler import ExperienceAssemblyService
from curriculum.models import Curriculum, Grade, Subject, Topic, Lesson, KnowledgePack, KnowledgeChunk

class TestMediaOrchestration(TestCase):

    def setUp(self):
        # Set up required models for the Assembler
        self.curriculum = Curriculum.objects.create(name="Test Curriculum")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Test Grade")
        self.subject = Subject.objects.create(grade=self.grade, name="Test Subject")
        self.topic = Topic.objects.create(subject=self.subject, name="Test Topic")
        self.lesson = Lesson.objects.create(topic=self.topic, title="Test Lesson")

        self.mock_plan = LearningExperiencePlan(
            title="Test Experience",
            cognitive_analysis={},
            strategy_selected="Predict-Observe-Explain",
            entry_node_id="step-1",
            nodes=[
                StrategyNode(
                    node_id="step-1",
                    node_type="explain",
                    instructional_intent=InstructionalIntent(
                        learning_moment="Introduce Atom",
                        student_goal="Understand basic unit",
                        required_cognitive_change="Know atom",
                        evidence_of_understanding="Can define atom",
                        recommended_learning_support="Text"
                    ),
                    personalization=PersonalizationOpportunities(),
                    content="An atom is the smallest unit of matter.",
                    next_nodes=["step-2"]
                ),
                StrategyNode(
                    node_id="step-2",
                    node_type="observe",
                    instructional_intent=InstructionalIntent(
                        learning_moment="Visualize Atom",
                        student_goal="See atom",
                        required_cognitive_change="Visual model",
                        evidence_of_understanding="Can identify parts",
                        recommended_learning_support="Diagram"
                    ),
                    personalization=PersonalizationOpportunities(),
                    content="Here is a diagram of the Bohr model.",
                    next_nodes=["step-3"]
                ),
                StrategyNode(
                    node_id="step-3",
                    node_type="practice",
                    instructional_intent=InstructionalIntent(
                        learning_moment="Build Atom",
                        student_goal="Interact with atom",
                        required_cognitive_change="Know protons/neutrons",
                        evidence_of_understanding="Can build one",
                        recommended_learning_support="Simulation"
                    ),
                    personalization=PersonalizationOpportunities(),
                    content="Build your own atom.",
                    next_nodes=[]
                )
            ]
        )

    @patch('curriculum.media_orchestration.planner.LLMFactory.get_provider')
    def test_media_planner(self, mock_get_provider):
        # Setup mock provider
        mock_provider = MagicMock()
        mock_get_provider.return_value = mock_provider
        
        # Setup mock response
        mock_manifest = MediaManifest(
            requirements=[
                MediaRequirement(
                    node_id="step-2",
                    is_required=True,
                    preferred_media_type="image",
                    educational_purpose="Visualize the Bohr model.",
                    accessibility_requirements="Diagram of an atom showing a central nucleus and electron orbits.",
                    search_keywords=["atom", "bohr", "diagram"]
                )
            ]
        )
        mock_provider.generate_structured.return_value = mock_manifest
        
        planner = MediaPlanner()
        manifest = planner.generate_manifest(self.mock_plan)
        
        self.assertEqual(len(manifest.requirements), 1)
        self.assertEqual(manifest.requirements[0].node_id, "step-2")
        self.assertEqual(manifest.requirements[0].preferred_media_type, "image")

    def test_wikimedia_adapter(self):
        adapter = WikimediaAdapter()
        req = MediaRequirement(
            node_id="test",
            is_required=True,
            preferred_media_type="image",
            educational_purpose="test",
            accessibility_requirements="test",
            search_keywords=["atom"]
        )
        resolved = adapter.resolve(req)
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved.provenance, 'Wikimedia Commons')
        self.assertEqual(resolved.asset_type, 'image')
        self.assertEqual(resolved.fallback_used, False)
        
        # Test no match
        req_no_match = req.model_copy(update={"search_keywords": ["unrelated_topic"]})
        resolved_none = adapter.resolve(req_no_match)
        self.assertIsNone(resolved_none)

    def test_acquisition_engine_caching(self):
        engine = MediaAcquisitionEngine()
        req = MediaRequirement(
            node_id="step-a",
            is_required=True,
            preferred_media_type="image",
            educational_purpose="test",
            accessibility_requirements="test",
            search_keywords=["atom"]
        )
        
        req_duplicate = req.model_copy(update={"node_id": "step-b"})
        
        manifest = MediaManifest(requirements=[req, req_duplicate])
        resolved_assets = engine.resolve_manifest(manifest)
        
        self.assertEqual(len(resolved_assets), 2)
        # Verify the second asset was pulled from cache (it will have the same URL but different step_id)
        self.assertEqual(resolved_assets[0].url, resolved_assets[1].url)
        self.assertEqual(resolved_assets[0].node_id, "step-a")
        self.assertEqual(resolved_assets[1].node_id, "step-b")

    @patch('curriculum.media_orchestration.providers.youtube.YouTubeProvider._execute_search')
    @patch('curriculum.media_orchestration.assembler.VisualIntelligenceEngine.process_manifest')
    @patch('curriculum.media_orchestration.assembler.MediaAcquisitionEngine.resolve_manifest')
    @patch('curriculum.media_orchestration.assembler.MediaPlanner.generate_manifest')
    def test_experience_assembly(self, mock_generate_manifest, mock_resolve_manifest, mock_process_manifest, mock_yt_search):
        mock_process_manifest.return_value = ([], [])
        mock_yt_search.return_value = []
        # Mock the outputs
        mock_manifest = MediaManifest(requirements=[
            MediaRequirement(
                node_id="step-2",
                is_required=True,
                preferred_media_type="image",
                educational_purpose="Visualize",
                accessibility_requirements="Alt",
                search_keywords=["atom"]
            ),
            MediaRequirement(
                node_id="step-3",
                is_required=True,
                preferred_media_type="simulation",
                educational_purpose="Interactive",
                accessibility_requirements="Sim",
                search_keywords=["build"]
            )
        ])
        mock_generate_manifest.return_value = mock_manifest
        
        mock_resolve_manifest.return_value = [
            ResolvedAsset(
                node_id="step-2",
                asset_type="image",
                url="http://example.com/atom.png",
                provenance="Wikimedia",
                licensing="CC",
                alt_text="Alt atom",
                confidence_score=0.9
            )
            # Notice step-3 is missing, simulating a failure to find the simulation
        ]
        
        assembler = ExperienceAssemblyService()
        package = assembler.compile_experience(self.lesson, self.mock_plan)
        
        # Verify package
        self.assertEqual(package.plan.title, "Test Experience")
        self.assertEqual(len(package.resolved_assets), 1)
        
        # Verify Database Rows (3 text blocks + 2 media blocks: 1 attached image + 1 pending simulation)
        self.assertEqual(self.lesson.blocks.count(), 5)
        self.assertEqual(self.lesson.assets.count(), 2)
        
        # Verify step-2 asset is attached
        asset_2 = self.lesson.assets.get(asset_type='image')
        self.assertEqual(asset_2.status, 'attached')
        self.assertEqual(asset_2.url, "http://example.com/atom.png")
        self.assertEqual(asset_2.metadata['provenance'], 'Wikimedia')
        
        # Verify step-3 asset is pending (graceful degradation)
        asset_3 = self.lesson.assets.get(asset_type='simulation')
        self.assertEqual(asset_3.status, 'pending')
        self.assertEqual(asset_3.asset_type, 'simulation')
        self.assertEqual(asset_3.description, 'Sim')
