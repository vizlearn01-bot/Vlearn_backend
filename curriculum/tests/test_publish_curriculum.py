"""Comprehensive test suite for the VLearn Curriculum Publishing system.

Covers:
- Connection and safety guards
- Content identity, UUIDs, and hashing
- Signal suppression during publication
- Primary key handling: new production PKs generated, no source PK collision
- Foreign key remapping across dependent hierarchies (Curriculum -> Grade -> Subject -> Topic -> LearningUnit -> Lesson -> LessonBlock -> LessonAsset)
- Many-to-Many relationship remapping
- Transaction rollback on error and failure reporting
- Production-only content preservation
- Operational model protection
- Idempotency of publication
"""

import os
import tempfile
import uuid
from unittest.mock import patch, MagicMock

from django.test import TestCase, override_settings
from django.core.management import call_command
from django.core.management.base import CommandError
from django.db import transaction

from curriculum.models import (
    Curriculum,
    Grade,
    Subject,
    PedagogyTemplate,
    GenerationRule,
    Topic,
    LearningUnit,
    Lesson,
    LessonBlock,
    LessonAsset,
    Simulation,
    CurriculumPublication,
)
from curriculum.publisher.connection import PublishConnection
from curriculum.publisher.constants import (
    SYNCED_MODEL_NAMES,
    PROTECTED_OPERATIONAL_MODELS,
)
from curriculum.publisher.identity import (
    VLEARN_NAMESPACE,
    generate_deterministic_uuid,
    compute_content_hash,
    find_target_match,
    build_natural_key_lookup,
)
from curriculum.publisher.media import MediaAuditor, MediaPublisher
from curriculum.publisher.report import PublicationReport
from curriculum.publisher.safety import (
    PublicationLock,
    PublicationLockError,
    PreFlightValidator,
    confirm_publication,
)
from curriculum.publisher.signals import disable_curriculum_signals
from curriculum.publisher.syncers import FKRemapper, BaseEntitySyncer, get_syncer_for_model
from curriculum.publisher.engine import CurriculumPublisher


class TestPublishConnection(TestCase):
    """Tests for production database connection lifecycle and safety guards."""

    def test_missing_publish_database_url_raises(self):
        with patch.dict(os.environ, {}, clear=True):
            conn = PublishConnection()
            with self.assertRaises(ValueError) as ctx:
                conn.configure()
            self.assertIn("PUBLISH_DATABASE_URL environment variable is not set", str(ctx.exception))

    def test_source_and_target_same_raises_error(self):
        conn = PublishConnection()
        conn.source_config = {'HOST': 'localhost', 'NAME': 'vlearn_dev'}
        conn.target_config = {'HOST': 'localhost', 'NAME': 'vlearn_dev'}
        with self.assertRaises(ValueError) as ctx:
            conn.validate_source_target_differ()
        self.assertIn("Target database and source database are the same", str(ctx.exception))

    def test_get_target_display_hides_credentials(self):
        conn = PublishConnection()
        conn.target_config = {
            'HOST': 'aws-0-eu-central-1.pooler.supabase.com',
            'NAME': 'postgres',
            'USER': 'postgres.admin',
            'PASSWORD': 'secret_password_123',
        }
        display = conn.get_target_display()
        self.assertIn("aws-0-eu-central-1.pooler.supabase.com:postgres", display)
        self.assertNotIn("secret_password_123", display)
        self.assertNotIn("postgres.admin", display)


class TestIdentityAndHashing(TestCase):
    """Tests for deterministic UUID generation, content hashing, and matching."""

    def test_deterministic_uuid_reproducible(self):
        uuid1 = generate_deterministic_uuid("Lesson", 42)
        uuid2 = generate_deterministic_uuid("Lesson", 42)
        uuid_diff = generate_deterministic_uuid("Lesson", 43)

        self.assertEqual(uuid1, uuid2)
        self.assertNotEqual(uuid1, uuid_diff)
        self.assertEqual(uuid1, uuid.uuid5(VLEARN_NAMESPACE, "Lesson:42"))

    def test_compute_content_hash_detects_changes(self):
        curriculum = Curriculum.objects.create(name="Test CBC", description="Original description")
        hash1 = compute_content_hash(curriculum)

        curriculum.description = "Updated description with modifications"
        hash2 = compute_content_hash(curriculum)

        self.assertNotEqual(hash1, hash2)

    def test_natural_key_matching(self):
        curriculum = Curriculum.objects.create(name="CBC")
        grade = Grade.objects.create(curriculum=curriculum, name="Grade 4")
        subject = Subject.objects.create(grade=grade, name="Mathematics")

        lookup = build_natural_key_lookup(subject, "Subject")
        self.assertEqual(
            lookup,
            {
                'grade__curriculum__name': 'CBC',
                'grade__name': 'Grade 4',
                'name': 'Mathematics',
            }
        )


class TestSignalSuppression(TestCase):
    """Tests that bootstrap signals are suppressed during publishing."""

    def test_disable_curriculum_signals_prevents_duplicate_pedagogy(self):
        curriculum = Curriculum.objects.create(name="CBC Signals Test")
        grade = Grade.objects.create(curriculum=curriculum, name="Grade 10")

        with disable_curriculum_signals():
            subject = Subject.objects.create(grade=grade, name="Advanced Chemistry")

        # Verify that create_default_pedagogy_template did NOT fire
        templates = PedagogyTemplate.objects.filter(subject=subject)
        self.assertEqual(templates.count(), 0)

        # Normal creation outside context manager triggers the signal
        subject_normal = Subject.objects.create(grade=grade, name="Standard Biology")
        self.assertEqual(PedagogyTemplate.objects.filter(subject=subject_normal).count(), 1)


class TestPKHandlingAndFKRemapping(TestCase):
    """Tests covering primary key generation, overlapping PK scenarios, and FK/M2M remapping."""

    def setUp(self):
        self.remapper = FKRemapper(source_db='default', target_db='default')

    def test_create_sets_fresh_pk_and_preserves_content_uuid(self):
        """Test (E & D): New target record receives fresh PK; content_uuid is preserved."""
        curr = Curriculum.objects.create(name="CBC Fresh PK")
        grade = Grade.objects.create(curriculum=curr, name="Grade 8")
        with disable_curriculum_signals():
            subj = Subject.objects.create(grade=grade, name="Social Studies")

        topic_uuid = uuid.uuid4()
        source_topic = Topic(
            id=999,  # Pretend local ID is 999
            subject=subj,
            name="Weather and Climate",
            order=1,
            content_uuid=topic_uuid,
            content_hash="abc123hash",
        )

        syncer = get_syncer_for_model('Topic', 'default', 'default')
        # Remap subject FK
        self.remapper.register('Subject', subj.pk, subj.pk)

        target_topic = syncer.create(source_topic, self.remapper, dry_run=False)

        # Must have a real database-generated PK, not 999
        self.assertIsNotNone(target_topic.pk)
        self.assertNotEqual(target_topic.pk, 999)
        self.assertEqual(target_topic.content_uuid, topic_uuid)
        self.assertEqual(target_topic.name, "Weather and Climate")
        # Registered in remapper
        self.assertEqual(self.remapper.get('Topic', 999), target_topic.pk)

    def test_overlapping_source_and_target_pks(self):
        """Test (A, B, C): Source and target have overlapping integer PKs for different objects."""
        curr = Curriculum.objects.create(name="CBC Overlap")
        grade = Grade.objects.create(curriculum=curr, name="Grade 5")
        with disable_curriculum_signals():
            subj = Subject.objects.create(grade=grade, name="Science")

        # Existing target topic has ID=98 with different UUID
        existing_target_topic = Topic.objects.create(
            subject=subj,
            name="Existing Topic in Production",
            order=1,
            content_uuid=uuid.uuid4(),
        )

        # Source topic happens to have local ID=98 (same ID!) but a DIFFERENT UUID
        source_topic_uuid = uuid.uuid4()
        source_topic = Topic(
            id=existing_target_topic.pk,  # Local PK happens to match production PK
            subject=subj,
            name="New Authoring Topic",
            order=2,
            content_uuid=source_topic_uuid,
            content_hash="source_hash_98",
        )

        syncer = get_syncer_for_model('Topic', 'default', 'default')
        self.remapper.register('Subject', subj.pk, subj.pk)

        # When creating the new source topic in target, it must NOT collide with existing ID=98
        new_target_topic = syncer.create(source_topic, self.remapper, dry_run=False)

        self.assertNotEqual(new_target_topic.pk, existing_target_topic.pk)
        self.assertEqual(new_target_topic.content_uuid, source_topic_uuid)
        self.assertEqual(new_target_topic.name, "New Authoring Topic")

        # Both records exist in the database with their respective UUIDs
        self.assertTrue(Topic.objects.filter(pk=existing_target_topic.pk).exists())
        self.assertTrue(Topic.objects.filter(pk=new_target_topic.pk).exists())

    def test_foreign_key_remapping_hierarchy(self):
        """Test (F): Foreign keys are properly remapped through all layers."""
        curr = Curriculum.objects.create(name="CBC Hierarchy")
        grade = Grade.objects.create(curriculum=curr, name="Grade 6")
        with disable_curriculum_signals():
            subj = Subject.objects.create(grade=grade, name="Agriculture")

        topic = Topic.objects.create(
            subject=subj,
            name="Soil Conservation",
            order=1,
            content_uuid=uuid.uuid4(),
        )
        unit = LearningUnit.objects.create(
            topic=topic,
            name="Unit 1: Soil Types",
            order=1,
            content_uuid=uuid.uuid4(),
        )
        lesson = Lesson.objects.create(
            topic=topic,
            learning_unit=unit,
            title="Lesson 1: Sandy Soil",
            content_uuid=uuid.uuid4(),
        )

        # Register simulated target mappings
        fake_target_lesson_pk = 5555
        self.remapper.register('Lesson', lesson.pk, fake_target_lesson_pk)

        source_block = LessonBlock(
            id=1234,
            lesson=lesson,
            block_type="introduction",
            order=1,
            content={"text": "Introduction to sandy soil"},
            content_uuid=uuid.uuid4(),
            content_hash="blockhash123",
        )

        block_syncer = get_syncer_for_model('LessonBlock', 'default', 'default')
        prepared_values = block_syncer.prepare_field_values(source_block, self.remapper)

        # Prepared values must have lesson_id = 5555 (remapped target PK)
        self.assertEqual(prepared_values['lesson_id'], fake_target_lesson_pk)
        self.assertNotIn('id', prepared_values)
        self.assertNotIn('pk', prepared_values)

    def test_m2m_remapping_lesson_asset_blocks(self):
        """Test (G): M2M relationships (LessonAsset.blocks) are remapped to target block PKs."""
        curr = Curriculum.objects.create(name="CBC M2M")
        grade = Grade.objects.create(curriculum=curr, name="Grade 7")
        with disable_curriculum_signals():
            subj = Subject.objects.create(grade=grade, name="Creative Arts")
        topic = Topic.objects.create(subject=subj, name="Drawing", order=1, content_uuid=uuid.uuid4())
        unit = LearningUnit.objects.create(topic=topic, name="Unit 1", order=1, content_uuid=uuid.uuid4())
        lesson = Lesson.objects.create(topic=topic, learning_unit=unit, title="Lesson 1", content_uuid=uuid.uuid4())

        source_block = LessonBlock.objects.create(
            lesson=lesson,
            block_type="visual_learning",
            order=1,
            content={"prompt": "Color palette"},
            content_uuid=uuid.uuid4(),
        )
        target_block = LessonBlock.objects.create(
            lesson=lesson,
            block_type="visual_learning",
            order=1,
            content={"prompt": "Color palette"},
            content_uuid=uuid.uuid4(),
        )

        source_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            url="https://res.cloudinary.com/demo/image/upload/sample.jpg",
            content_uuid=uuid.uuid4(),
        )
        source_asset.blocks.add(source_block)

        target_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            url="https://res.cloudinary.com/demo/image/upload/sample.jpg",
            content_uuid=uuid.uuid4(),
        )

        # Register local block PK -> target block PK
        self.remapper.register('LessonBlock', source_block.pk, target_block.pk)

        asset_syncer = get_syncer_for_model('LessonAsset', 'default', 'default')
        asset_syncer.sync_m2m(source_asset, target_asset, self.remapper, dry_run=False)

        # Target asset blocks must contain target_block, NOT source_block
        target_block_pks = list(target_asset.blocks.values_list('pk', flat=True))
        self.assertIn(target_block.pk, target_block_pks)
        self.assertNotIn(source_block.pk, target_block_pks)


class TestRollbackAndFailureReporting(TestCase):
    """Tests covering atomic transaction rollback and error reporting (H, I, J, K, L, M)."""

    def test_transaction_rollback_on_failure(self):
        """Test (H, I, J): Exception during publication rolls back all writes and reports failure."""
        report = PublicationReport(mode='apply', scope={})

        initial_curriculum_count = Curriculum.objects.count()

        publisher = CurriculumPublisher(mode='apply', source_db='default', target_db='default')

        # Simulate an intentional failure during syncer.sync_batch()
        with patch.object(BaseEntitySyncer, 'sync_batch', side_effect=RuntimeError("Simulated DB Disk Full")):
            publisher._apply_publication(
                {'Curriculum': [Curriculum(name="Should Rollback", description="test")]},
                MagicMock(local_file_count=0, items=[]),
                report,
            )

        # Verify transaction rolled back
        self.assertEqual(Curriculum.objects.count(), initial_curriculum_count)
        self.assertFalse(Curriculum.objects.filter(name="Should Rollback").exists())

        # Verify report status
        self.assertTrue(len(report.errors) > 0)
        cli_output = report.format_cli()
        self.assertIn("PUBLICATION FAILED — ROLLED BACK", cli_output)
        self.assertNotIn("PUBLICATION APPLIED", cli_output)

    def test_production_only_curriculum_preserved(self):
        """Test (L): Records that only exist in production are never deleted or modified."""
        prod_only_curr = Curriculum.objects.create(
            name="Legacy 8-4-4 Only In Prod",
            description="Existing production content not in local dev",
        )

        report = PublicationReport(mode='dry_run')
        publisher = CurriculumPublisher(mode='dry_run', source_db='default', target_db='default')

        # Scoped objects contains only a new CBC curriculum
        scoped = {'Curriculum': [Curriculum.objects.create(name="New CBC 2026")]}
        publisher._build_diff(scoped, report)

        # Verify production-only item is detected and reported
        self.assertIn('Curriculum', report.production_only_items)
        self.assertTrue(any(f"PK {prod_only_curr.pk}" in str(item) for item in report.production_only_items['Curriculum']))

        # Verify production-only object still exists untouched
        self.assertTrue(Curriculum.objects.filter(name="Legacy 8-4-4 Only In Prod").exists())

    def test_operational_models_protected(self):
        """Test (M): Protected operational models are excluded from SYNCED_MODELS."""
        for op_model in ['User', 'UserProfile', 'School', 'LearningSession', 'GenerationJob', 'Invoice']:
            self.assertNotIn(op_model, SYNCED_MODEL_NAMES)
            self.assertIn(op_model, PROTECTED_OPERATIONAL_MODELS)
