"""
curriculum/tests.py

Test suite for the VLearn curriculum backend.

Coverage:
  1. Legacy V1 lesson generation still works end-to-end.
  2. Legacy V1 lesson retrieval still works (API contract unchanged).
  3. Legacy V1 API still returns the same response shape.
  4. LessonAssets can be created and updated.
  5. LessonBlocks can reference LessonAssets via the M2M relation.
  6. Repository (KnowledgeChunk) references function correctly on LessonAsset.
  7. Skeleton infrastructure (ComponentType, validate_skeleton,
     SkeletonTranslator) works correctly without touching the DB.

IMPORTANT: These tests do NOT call the live LLM. The generation pipeline
is exercised through the persistence layer directly, mirroring what the
GenerationOrchestrator does after receiving an LLM response.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit,
    Lesson, LessonBlock, LessonAsset,
    KnowledgePack, KnowledgeChunk,
    PedagogyTemplate, GenerationRule, GenerationJob,
)
from curriculum.generation.persistence import LessonPersistenceService
from curriculum.generation.skeleton import (
    ComponentType, SUGGESTED_COMPONENT_TYPES,
    validate_skeleton, SkeletonTranslator,
)

User = get_user_model()


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------

def _build_curriculum_tree():
    """
    Creates the minimal hierarchy required by most tests:
      Curriculum → Grade → Subject → Topic → LearningUnit
    Returns a dict of all created objects.
    """
    curriculum = Curriculum.objects.create(name='Test CBC', description='')
    grade = Grade.objects.create(curriculum=curriculum, name='Grade 10', level=10)
    subject = Subject.objects.create(grade=grade, name='Physics')
    topic = Topic.objects.create(subject=subject, name='Gas Laws', order=1)
    lu = LearningUnit.objects.create(topic=topic, name="Boyle's Law", order=1)
    return {
        'curriculum': curriculum,
        'grade': grade,
        'subject': subject,
        'topic': topic,
        'learning_unit': lu,
    }


def _get_or_create_admin():
    return User.objects.create_superuser(
        username='admin_test', email='admin@test.com', password='testpass123'
    )


# ---------------------------------------------------------------------------
# 1. Legacy V1 lesson generation
# ---------------------------------------------------------------------------

class LegacyLessonGenerationTests(TestCase):
    """Verify the existing V1 persistence pipeline is intact."""

    def setUp(self):
        tree = _build_curriculum_tree()
        self.lu = tree['learning_unit']
        self.topic = tree['topic']

    def test_get_or_create_draft_lesson_creates_new(self):
        lesson = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        self.assertEqual(lesson.status, 'draft')
        self.assertEqual(lesson.learning_unit, self.lu)

    def test_get_or_create_draft_lesson_returns_existing(self):
        lesson1 = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        lesson2 = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        self.assertEqual(lesson1.id, lesson2.id)

    def test_save_block_creates_block(self):
        lesson = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        block = LessonPersistenceService.save_block(
            lesson=lesson,
            block_type='introduction',
            title='Introduction',
            content="## Introduction\n\nBoyle's Law states that...",
            order=0,
        )
        self.assertIsNotNone(block.id)
        self.assertEqual(block.lesson, lesson)
        self.assertEqual(block.block_type, 'introduction')
        self.assertEqual(block.order, 0)

    def test_save_block_update_existing(self):
        lesson = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        block = LessonPersistenceService.save_block(
            lesson=lesson, block_type='summary', title='Summary',
            content='Original', order=1,
        )
        updated = LessonPersistenceService.save_block(
            lesson=lesson, block_type='summary', title='Summary Updated',
            content='Updated content', order=1, block_id=str(block.id),
        )
        self.assertEqual(updated.id, block.id)
        self.assertEqual(updated.content, 'Updated content')

    def test_v1_block_has_null_v2_fields(self):
        """Legacy blocks created by V1 pipeline must have null V2 fields."""
        lesson = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        block = LessonPersistenceService.save_block(
            lesson=lesson, block_type='overview', title='Overview',
            content='...', order=0,
        )
        self.assertIsNone(block.page_number)
        self.assertIsNone(block.page_title)
        self.assertIsNone(block.component_type)
        self.assertIsNone(block.component_order)


# ---------------------------------------------------------------------------
# 2. Legacy V1 API contract
# ---------------------------------------------------------------------------

class LegacyAPIContractTests(TestCase):
    """
    Verify the V1 public API returns the same fields it always has.
    No new mandatory fields should break existing consumers.
    """

    def setUp(self):
        tree = _build_curriculum_tree()
        self.lu = tree['learning_unit']
        self.topic = tree['topic']
        self.admin = _get_or_create_admin()
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)

        self.lesson = LessonPersistenceService.get_or_create_draft_lesson(self.lu.id)
        LessonPersistenceService.save_block(
            lesson=self.lesson, block_type='overview', title='Overview',
            content='Some text', order=0,
        )

    def test_lesson_list_returns_v1_fields(self):
        url = '/api/curriculum/lessons/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # DRF pagination wraps results; fall back to flat list for non-paginated setups
        items = data.get('results', data) if isinstance(data, dict) else data
        lesson_data = next(d for d in items if d['id'] == self.lesson.id)
        # V1 expected fields
        for field in ['id', 'topic', 'learning_unit', 'title', 'status',
                      'version', 'blocks', 'created_at', 'updated_at']:
            self.assertIn(field, lesson_data, msg=f'V1 field "{field}" missing')

    def test_lesson_blocks_v1_fields_present(self):
        url = '/api/curriculum/lessons/'
        response = self.client.get(url)
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        lesson_data = next(d for d in items if d['id'] == self.lesson.id)
        block = lesson_data['blocks'][0]
        for field in ['id', 'lesson', 'block_type', 'title', 'content', 'order']:
            self.assertIn(field, block, msg=f'V1 block field "{field}" missing')

    def test_v2_query_param_returns_assets_key(self):
        url = '/api/curriculum/lessons/?v=2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        lesson_data = next(d for d in items if d['id'] == self.lesson.id)
        self.assertIn('assets', lesson_data)


# ---------------------------------------------------------------------------
# 3. LessonAsset creation and management
# ---------------------------------------------------------------------------

class LessonAssetTests(TestCase):
    """Verify LessonAsset can be created, linked, and retrieved correctly."""

    def setUp(self):
        tree = _build_curriculum_tree()
        self.lesson = LessonPersistenceService.get_or_create_draft_lesson(
            tree['learning_unit'].id
        )
        self.block = LessonPersistenceService.save_block(
            lesson=self.lesson, block_type='concept_explanation',
            title='Concept', content='Some explanation', order=0,
        )

    def test_create_asset_pending(self):
        asset = LessonAsset.objects.create(
            lesson=self.lesson,
            asset_type='diagram',
            source_type='uploaded',
            storage_type='file',
            status='pending',
            description="Diagram showing Boyle's Law.",
        )
        self.assertEqual(asset.status, 'pending')
        self.assertEqual(asset.version, 1)
        self.assertIsNone(asset.url)
        self.assertFalse(bool(asset.file))

    def test_attach_asset_to_block(self):
        asset = LessonAsset.objects.create(
            lesson=self.lesson,
            asset_type='youtube',
            source_type='external',
            storage_type='url',
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            status='attached',
        )
        asset.blocks.add(self.block)
        self.assertIn(self.block, asset.blocks.all())
        self.assertIn(asset, self.block.assets.all())

    def test_asset_version_default_is_one(self):
        asset = LessonAsset.objects.create(
            lesson=self.lesson, asset_type='image',
            source_type='uploaded', storage_type='file',
        )
        self.assertEqual(asset.version, 1)

    def test_asset_lesson_cascade_delete(self):
        asset = LessonAsset.objects.create(
            lesson=self.lesson, asset_type='gif',
            source_type='external', storage_type='url',
            url='https://example.com/loop.gif',
        )
        asset_id = asset.id
        self.lesson.delete()
        self.assertFalse(LessonAsset.objects.filter(id=asset_id).exists())


# ---------------------------------------------------------------------------
# 4. Repository (KnowledgeChunk) references on LessonAsset
# ---------------------------------------------------------------------------

class RepositoryReferenceTests(TestCase):
    """Verify that a LessonAsset can trace back to its source KnowledgeChunk."""

    def setUp(self):
        tree = _build_curriculum_tree()
        self.lesson = LessonPersistenceService.get_or_create_draft_lesson(
            tree['learning_unit'].id
        )
        self.kp = KnowledgePack.objects.create(
            subject=tree['subject'], status='approved',
        )
        self.chunk = KnowledgeChunk.objects.create(
            knowledge_pack=self.kp,
            topic=tree['topic'],
            learning_unit=tree['learning_unit'],
            chunk_type='diagram',
            content_text='',
            order=1,
            section_title='Pressure Diagrams',
        )

    def test_asset_linked_to_chunk(self):
        asset = LessonAsset.objects.create(
            lesson=self.lesson,
            knowledge_chunk=self.chunk,
            asset_type='diagram',
            source_type='knowledge_repository',
            storage_type='file',
            status='attached',
        )
        self.assertEqual(asset.knowledge_chunk, self.chunk)
        self.assertIn(asset, self.chunk.lesson_assets.all())

    def test_chunk_delete_nullifies_asset_reference(self):
        asset = LessonAsset.objects.create(
            lesson=self.lesson,
            knowledge_chunk=self.chunk,
            asset_type='diagram',
            source_type='knowledge_repository',
            storage_type='file',
        )
        self.chunk.delete()
        asset.refresh_from_db()
        self.assertIsNone(asset.knowledge_chunk)


# ---------------------------------------------------------------------------
# 5. Skeleton infrastructure (no DB interaction)
# ---------------------------------------------------------------------------

class SkeletonInfrastructureTests(TestCase):
    """Verify the skeleton helpers work correctly as pure functions."""

    VALID_SKELETON = {
        "pages": [
            {
                "title": "Introduction to Pressure",
                "components": [
                    {"type": "learning_goal",       "content": "Understand pressure."},
                    {"type": "concept_explanation", "content": "Pressure = Force / Area."},
                    {"type": "suggested_diagram",   "admin_instruction": "Boyle's Law diagram."},
                    {"type": "knowledge_check",     "content": "What unit is pressure measured in?"},
                    {"type": "transition",          "content": "Next we look at applications."},
                ],
            }
        ]
    }

    def test_component_type_constants_present(self):
        self.assertIn('learning_goal',        ComponentType.ALL)
        self.assertIn('suggested_diagram',    ComponentType.ALL)
        self.assertIn('knowledge_check',      ComponentType.ALL)

    def test_suggested_types_subset_of_all(self):
        for t in SUGGESTED_COMPONENT_TYPES:
            self.assertIn(t, ComponentType.ALL)

    def test_validate_skeleton_valid(self):
        errors = validate_skeleton(self.VALID_SKELETON)
        self.assertEqual(errors, [])

    def test_validate_skeleton_missing_pages(self):
        errors = validate_skeleton({})
        self.assertTrue(len(errors) > 0)

    def test_validate_skeleton_unknown_type(self):
        bad = {"pages": [{"components": [{"type": "unicorn"}]}]}
        errors = validate_skeleton(bad)
        self.assertTrue(any('unknown component type' in e for e in errors))

    def test_translator_produces_correct_count(self):
        blocks = SkeletonTranslator.translate(self.VALID_SKELETON)
        self.assertEqual(len(blocks), 5)

    def test_translator_page_number_assigned(self):
        blocks = SkeletonTranslator.translate(self.VALID_SKELETON)
        for b in blocks:
            self.assertEqual(b['page_number'], 1)

    def test_translator_page_title_on_first_component_only(self):
        blocks = SkeletonTranslator.translate(self.VALID_SKELETON)
        self.assertEqual(blocks[0]['page_title'], 'Introduction to Pressure')
        for b in blocks[1:]:
            self.assertIsNone(b['page_title'])

    def test_translator_suggested_has_asset_instruction(self):
        blocks = SkeletonTranslator.translate(self.VALID_SKELETON)
        diagram_block = next(b for b in blocks if b['component_type'] == 'suggested_diagram')
        self.assertEqual(diagram_block['_asset_instruction'], "Boyle's Law diagram.")
        self.assertEqual(diagram_block['_asset_type'], 'diagram')

    def test_translator_text_block_has_no_asset_instruction(self):
        blocks = SkeletonTranslator.translate(self.VALID_SKELETON)
        text_block = next(b for b in blocks if b['component_type'] == 'learning_goal')
        self.assertIsNone(text_block['_asset_instruction'])

    def test_translator_global_order_is_sequential(self):
        blocks = SkeletonTranslator.translate(self.VALID_SKELETON)
        orders = [b['order'] for b in blocks]
        self.assertEqual(orders, list(range(len(blocks))))

    def test_translator_multi_page_page_numbers(self):
        skeleton = {
            "pages": [
                {"title": "Page A", "components": [{"type": "learning_goal", "content": "A"}]},
                {"title": "Page B", "components": [{"type": "summary", "content": "B"}]},
            ]
        }
        blocks = SkeletonTranslator.translate(skeleton)
        self.assertEqual(blocks[0]['page_number'], 1)
        self.assertEqual(blocks[1]['page_number'], 2)


# ---------------------------------------------------------------------------
# 6. AI Infrastructure tests
# ---------------------------------------------------------------------------
from unittest.mock import patch, MagicMock
from ai_infrastructure.config import DEFAULT_GEMINI_MODEL
from ai_infrastructure.exceptions import AIError, ProviderError, ValidationError, TimeoutError, RetryError
from ai_infrastructure.di import get_ai_provider, register_provider, reset_registry
from ai_infrastructure.providers.base import AbstractAIProvider
from ai_infrastructure.contracts.base import BaseModel, Field
from ai_infrastructure.contracts.lesson import LessonBlueprintSchema, PageBlueprintSchema, ComponentBlueprintSchema
from ai_infrastructure.providers.gemini import GeminiProvider

class AIInfrastructureTests(TestCase):
    """Verify that the AI Infrastructure foundation behaves correctly."""

    def test_di_registry_resolves_default_provider(self):
        reset_registry()
        # Should resolve to a GeminiProvider by default
        provider = get_ai_provider()
        self.assertIsInstance(provider, GeminiProvider)

    def test_di_registry_override(self):
        reset_registry()
        mock_provider = MagicMock(spec=AbstractAIProvider)
        register_provider(AbstractAIProvider, mock_provider)
        self.assertEqual(get_ai_provider(), mock_provider)

    def test_pydantic_contracts_validation(self):
        # Construct structured schemas
        component = ComponentBlueprintSchema(type="learning_goal", content="Learn biology")
        page = PageBlueprintSchema(title="Intro", components=[component])
        lesson = LessonBlueprintSchema(lesson_title="Cell Structure", pages=[page])
        
        dumped = lesson.model_dump()
        self.assertEqual(dumped["lesson_title"], "Cell Structure")
        self.assertEqual(len(dumped["pages"]), 1)
        self.assertEqual(dumped["pages"][0]["components"][0]["type"], "learning_goal")

    @patch('ai_infrastructure.providers.gemini.GeminiProvider.generate')
    def test_llm_client_delegates_to_provider(self, mock_generate):
        mock_generate.return_value = "Test response"
        from curriculum.generation.llm_client import LLMClient
        res = LLMClient.generate("Test prompt")
        self.assertEqual(res, "Test response")
        mock_generate.assert_called_once_with("Test prompt", model_name=None)

# ---------------------------------------------------------------------------
# 7. Agent 2 Pipeline Tests (Document Ingestion & Semantic Structuring)
# ---------------------------------------------------------------------------
import json
from unittest.mock import patch, MagicMock, mock_open
from curriculum.extraction_pipeline import DocumentIngestionService
from curriculum.semantic_extraction import SemanticStructuringService
from curriculum.models import Concept, ConceptRelationship, LearningObjective, Misconception

class Agent2PipelineTests(TestCase):
    def setUp(self):
        tree = _build_curriculum_tree()
        self.lu = tree['learning_unit']
        self.kp = KnowledgePack.objects.create(
            subject=tree['subject'], status='processing',
        )

    @patch('curriculum.extraction_pipeline.fitz.open')
    @patch('curriculum.extraction_pipeline.os.path.splitext')
    def test_document_ingestion_service_pdf(self, mock_splitext, mock_fitz_open):
        mock_splitext.return_value = ('dummy', '.pdf')
        mock_doc = MagicMock()
        mock_doc.__len__.return_value = 1
        mock_page = MagicMock()
        mock_page.get_text.return_value = [
            (0, 0, 10, 10, "Test chunk content", 0, 0)
        ]
        mock_doc.__getitem__.return_value = mock_page
        mock_doc.get_toc.return_value = []
        mock_fitz_open.return_value = mock_doc
        
        # mock kp.file
        self.kp.file = MagicMock()
        self.kp.file.path = 'dummy.pdf'
        self.kp.save()

        service = DocumentIngestionService(self.kp.id)
        service.process()

        self.assertEqual(self.kp.status, 'review')
        self.assertEqual(self.kp.chunks.count(), 1)
        self.assertEqual(self.kp.chunks.first().content_text, "Test chunk content")

    def test_heuristic_regex_recovery(self):
        mock_doc = MagicMock()
        mock_doc.__len__.return_value = 2
        mock_page = MagicMock()
        mock_page.get_text.return_value = "Table of Contents\nChapter 1: The Mole .... 5\n1.1 Avogadro Constant ... 6"
        mock_doc.__getitem__.return_value = mock_page

        structure = DocumentIngestionService._heuristic_regex_recovery(mock_doc, max_scan_pages=2)
        self.assertTrue(len(structure) > 0)
        self.assertEqual(structure[0]['title'], "Chapter 1: The Mole")
        self.assertEqual(structure[0]['source_type'], "regex_fallback")

    @patch('curriculum.semantic_extraction.LLMClient.generate')
    def test_semantic_structuring_service(self, mock_generate):
        KnowledgeChunk.objects.create(
            knowledge_pack=self.kp,
            learning_unit=self.lu,
            chunk_type='core_text',
            content_text="Photosynthesis is the process by which plants make food. A common misconception is that plants get their food from soil.",
            start_page=1,
            end_page=1,
            order=1
        )
        chunk = KnowledgeChunk.objects.first()

        mock_generate.return_value = json.dumps({
            "concepts": [
                {
                    "name": "Photosynthesis",
                    "description": "Process by which plants make food.",
                    "origin_chunk_id": chunk.id,
                    "page_number": 1
                }
            ],
            "relationships": [],
            "objectives": [
                {
                    "description": "Understand photosynthesis",
                    "related_concept_name": "Photosynthesis",
                    "origin_chunk_id": chunk.id,
                    "page_number": 1
                }
            ],
            "misconceptions": [
                {
                    "description": "Plants get food from soil",
                    "correction": "Plants make their own food",
                    "related_concept_name": "Photosynthesis",
                    "origin_chunk_id": chunk.id,
                    "page_number": 1
                }
            ]
        })

        service = SemanticStructuringService(self.lu.id, self.kp.id)
        service.process_chunks()

        self.assertEqual(Concept.objects.count(), 1)
        self.assertEqual(LearningObjective.objects.count(), 1)
        self.assertEqual(Misconception.objects.count(), 1)

        concept = Concept.objects.first()
        self.assertEqual(concept.name, "Photosynthesis")
        self.assertEqual(concept.learning_unit, self.lu)
        self.assertEqual(concept.origin_chunk, chunk)


# ---------------------------------------------------------------------------
# 8. Interactive Simulation Registry API Tests
# ---------------------------------------------------------------------------
from curriculum.models import Simulation, SubjectDomain, SimulationStatus

class SimulationRegistryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        Simulation.objects.create(
            key="charles_law",
            title="Charles's Law",
            subject=SubjectDomain.CHEMISTRY,
            topic="Gas Laws",
            status=SimulationStatus.ACTIVE,
            description="Interactive gas law simulation",
            archetype="charles_law",
            config={
                "initial_temperature_k": 273,
                "context_spec": {
                    "overview": "Explores the direct relationship between absolute temperature and volume.",
                    "how_to_use": ["Step 1: Adjust slider."],
                    "expected_results": [{"action": "Increasing T", "expected_outcome": "V increases", "key_takeaway": "V ∝ T"}]
                }
            }
        )
        Simulation.objects.create(
            key="reaction_rate",
            title="Reaction Rate",
            subject=SubjectDomain.CHEMISTRY,
            topic="Rates of Reaction",
            status=SimulationStatus.ACTIVE,
            description="Investigate collision theory",
            archetype="reaction_rate",
            config={"initial_concentration_m": 1.0}
        )
        Simulation.objects.create(
            key="electrolysis",
            title="Electrolysis",
            subject=SubjectDomain.CHEMISTRY,
            topic="Electrochemistry",
            status=SimulationStatus.ACTIVE,
            description="Simulate ionic movement",
            archetype="electrolysis",
            config={"electrolyte": "CuSO4"}
        )
        Simulation.objects.create(
            key="chem_acid_base_dissociation",
            title="Acid-Base Strength & Ionization Dynamics",
            subject=SubjectDomain.CHEMISTRY,
            topic="Core Acid-Base Concepts & Strength",
            status=SimulationStatus.ACTIVE,
            description="Explore acid strength and ionization",
            archetype="acid_base_dissociation",
            config={"weak_acid_ka": 0.000018, "initial_acid_type": "weak_acid"}
        )
        Simulation.objects.create(
            key="chemical_equilibrium",
            title="Chemical Equilibrium",
            subject=SubjectDomain.CHEMISTRY,
            topic="Chemical Equilibrium",
            status=SimulationStatus.PLACEHOLDER,
            description="Explore dynamic equilibrium",
            archetype="chemical_equilibrium",
            config={}
        )
        Simulation.objects.create(
            key="freefall",
            title="Freefall Acceleration",
            subject=SubjectDomain.PHYSICS,
            topic="Gravity & Kinematics",
            status=SimulationStatus.PLACEHOLDER,
            description="Analyze freefall motion",
            archetype="freefall",
            config={}
        )

    def test_list_simulations_returns_all(self):
        response = self.client.get('/api/curriculum/simulations/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        self.assertEqual(len(items), 6)

    def test_filter_simulations_by_subject(self):
        response = self.client.get('/api/curriculum/simulations/?subject=CHEMISTRY')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        self.assertEqual(len(items), 5)

    def test_filter_simulations_by_status(self):
        response = self.client.get('/api/curriculum/simulations/?status=ACTIVE')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        self.assertEqual(len(items), 4)

    def test_filter_simulations_by_subject_and_status(self):
        response = self.client.get('/api/curriculum/simulations/?subject=CHEMISTRY&status=ACTIVE')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        self.assertEqual(len(items), 4)

        keys = [item['key'] for item in items]
        self.assertIn('charles_law', keys)
        self.assertIn('reaction_rate', keys)
        self.assertIn('electrolysis', keys)
        self.assertIn('chem_acid_base_dissociation', keys)

    def test_simulation_config_serialization(self):
        response = self.client.get('/api/curriculum/simulations/')
        data = response.json()
        items = data.get('results', data) if isinstance(data, dict) else data
        charles_law = next(item for item in items if item['key'] == 'charles_law')
        self.assertEqual(charles_law['config']['initial_temperature_k'], 273)
        self.assertEqual(charles_law['subject_display'], 'Chemistry')
        self.assertEqual(charles_law['status_display'], 'Active')
        self.assertIn('context_spec', charles_law['config'])
        self.assertEqual(len(charles_law['config']['context_spec']['how_to_use']), 1)



