"""Curriculum publisher orchestration engine."""

import logging
from datetime import datetime, timezone
from django.apps import apps
from django.db import transaction

from curriculum.publisher.connection import PublishConnection
from curriculum.publisher.constants import SYNCED_MODEL_NAMES
from curriculum.publisher.identity import NATURAL_KEY_MODELS
from curriculum.publisher.media import MediaAuditor, MediaPublisher
from curriculum.publisher.report import PublicationReport
from curriculum.publisher.safety import (
    PublicationLock,
    PreFlightValidator,
    confirm_publication,
    ValidationReport,
)
from curriculum.publisher.syncers import FKRemapper, get_syncer_for_model

logger = logging.getLogger(__name__)


class CurriculumPublisher:
    """Orchestrates validation, dry-run diffing, and one-way publication of curriculum content."""

    def __init__(
        self,
        scope: dict | None = None,
        mode: str = "dry_run",  # 'validate', 'dry_run', 'apply'
        skip_confirmation: bool = False,
        verbosity: int = 1,
        source_db: str = "default",
        target_db: str = "publish_target",
    ):
        self.scope = scope or {}
        self.mode = mode
        self.skip_confirmation = skip_confirmation
        self.verbosity = verbosity
        self.source_db = source_db
        self.target_db = target_db

        self.connection = PublishConnection()
        self.fk_remapper = FKRemapper(self.source_db, self.target_db)

    def run(self) -> tuple[bool, PublicationReport]:
        """Main entrypoint for publisher execution."""
        report = PublicationReport(
            scope=self.scope,
            mode=self.mode,
            started_at=datetime.now(timezone.utc),
        )

        with self.connection:
            report.source_host = self.connection.get_source_display()
            report.target_host = self.connection.get_target_display()

            # 1. Validation Stage
            validator = PreFlightValidator(self.source_db, self.target_db)
            validation_report = validator.validate_all()
            report.validation_passed = validation_report.all_passed

            # Audit Media
            auditor = MediaAuditor(self.source_db)
            media_report = auditor.audit_scope()
            report.media_counts = {
                'external_urls': media_report.external_count,
                'cloudinary_assets': media_report.cloudinary_count,
                'local_files_to_upload': media_report.local_file_count,
                'missing_files': media_report.missing_file_count,
            }

            if media_report.has_missing_files:
                for missing_msg in media_report.get_missing_summary():
                    report.errors.append(f"Missing media: {missing_msg}")
                report.validation_passed = False

            if not report.validation_passed:
                for check in validation_report.checks:
                    if not check.passed:
                        report.errors.append(f"{check.name}: {check.message}")
                        for detail in check.details:
                            report.errors.append(f"  - {detail}")

            if self.mode == "validate" or not report.validation_passed:
                report.completed_at = datetime.now(timezone.utc)
                report.write_json()
                return report.validation_passed, report

            # 2. Build Plan / Diff (for dry_run and apply)
            scoped_source_objects = self._get_scoped_objects()
            self._build_diff(scoped_source_objects, report)

            # 3. Apply Stage (if requested)
            if self.mode == "apply":
                # Require confirmation
                if not confirm_publication(report.target_host, self.scope, self.skip_confirmation):
                    report.warnings.append("Publication canceled by user.")
                    report.completed_at = datetime.now(timezone.utc)
                    return False, report

                self._apply_publication(scoped_source_objects, media_report, report)

            report.completed_at = datetime.now(timezone.utc)
            report.write_json()
            if self.mode == "apply":
                report.save_audit_record(self.source_db)

            return len(report.errors) == 0, report

    def _get_scoped_objects(self) -> dict[str, list]:
        """Calculates the complete dependency closure of objects within the specified scope."""
        scoped: dict[str, list] = {name: [] for name in SYNCED_MODEL_NAMES}

        # 1. Curriculum
        Curriculum = apps.get_model('curriculum', 'Curriculum')
        curr_qs = Curriculum.objects.using(self.source_db).all()
        if 'curriculum' in self.scope:
            currs = [c.strip() for c in str(self.scope['curriculum']).split(',') if c.strip()]
            curr_qs = curr_qs.filter(name__in=currs)
        scoped['Curriculum'] = list(curr_qs)
        curr_ids = [c.pk for c in scoped['Curriculum']]

        # 2. Grade
        Grade = apps.get_model('curriculum', 'Grade')
        grade_qs = Grade.objects.using(self.source_db).filter(curriculum_id__in=curr_ids)
        if 'grade' in self.scope:
            grades = [g.strip() for g in str(self.scope['grade']).split(',') if g.strip()]
            grade_qs = grade_qs.filter(name__in=grades)
        scoped['Grade'] = list(grade_qs)
        grade_ids = [g.pk for g in scoped['Grade']]

        # 3. Subject
        Subject = apps.get_model('curriculum', 'Subject')
        subj_qs = Subject.objects.using(self.source_db).filter(grade_id__in=grade_ids)
        if 'subject' in self.scope:
            subjs = [s.strip() for s in str(self.scope['subject']).split(',') if s.strip()]
            subj_qs = subj_qs.filter(name__in=subjs)
        scoped['Subject'] = list(subj_qs)
        subject_ids = [s.pk for s in scoped['Subject']]

        # 4. PedagogyTemplate & GenerationRule
        PedagogyTemplate = apps.get_model('curriculum', 'PedagogyTemplate')
        scoped['PedagogyTemplate'] = list(
            PedagogyTemplate.objects.using(self.source_db).filter(subject_id__in=subject_ids)
        )
        template_ids = [p.pk for p in scoped['PedagogyTemplate']]

        GenerationRule = apps.get_model('curriculum', 'GenerationRule')
        scoped['GenerationRule'] = list(
            GenerationRule.objects.using(self.source_db).filter(template_id__in=template_ids)
        )

        # 5. KnowledgePack & KnowledgeChunk
        KnowledgePack = apps.get_model('curriculum', 'KnowledgePack')
        scoped['KnowledgePack'] = list(
            KnowledgePack.objects.using(self.source_db).filter(subject_id__in=subject_ids)
        )
        kp_ids = [k.pk for k in scoped['KnowledgePack']]

        KnowledgeChunk = apps.get_model('curriculum', 'KnowledgeChunk')
        scoped['KnowledgeChunk'] = list(
            KnowledgeChunk.objects.using(self.source_db).filter(knowledge_pack_id__in=kp_ids).only('id', 'content_uuid', 'content_hash', 'knowledge_pack_id')
        )

        # 6. Topic & LearningUnit
        Topic = apps.get_model('curriculum', 'Topic')
        scoped['Topic'] = list(
            Topic.objects.using(self.source_db).filter(subject_id__in=subject_ids)
        )
        topic_ids = [t.pk for t in scoped['Topic']]

        LearningUnit = apps.get_model('curriculum', 'LearningUnit')
        scoped['LearningUnit'] = list(
            LearningUnit.objects.using(self.source_db).filter(topic_id__in=topic_ids)
        )
        lu_ids = [u.pk for u in scoped['LearningUnit']]

        # 7. Semantic Concept Layer
        Concept = apps.get_model('curriculum', 'Concept')
        scoped['Concept'] = list(
            Concept.objects.using(self.source_db).filter(learning_unit_id__in=lu_ids)
        )
        concept_ids = [c.pk for c in scoped['Concept']]

        ConceptRelationship = apps.get_model('curriculum', 'ConceptRelationship')
        scoped['ConceptRelationship'] = list(
            ConceptRelationship.objects.using(self.source_db).filter(
                source_id__in=concept_ids, target_id__in=concept_ids
            )
        )

        LearningObjective = apps.get_model('curriculum', 'LearningObjective')
        scoped['LearningObjective'] = list(
            LearningObjective.objects.using(self.source_db).filter(learning_unit_id__in=lu_ids)
        )

        Misconception = apps.get_model('curriculum', 'Misconception')
        scoped['Misconception'] = list(
            Misconception.objects.using(self.source_db).filter(concept_id__in=concept_ids)
        )

        # 8. Lesson, LessonBlock, LessonAsset
        Lesson = apps.get_model('curriculum', 'Lesson')
        scoped['Lesson'] = list(
            Lesson.objects.using(self.source_db).filter(topic_id__in=topic_ids)
        )
        lesson_ids = [l.pk for l in scoped['Lesson']]

        LessonBlock = apps.get_model('curriculum', 'LessonBlock')
        scoped['LessonBlock'] = list(
            LessonBlock.objects.using(self.source_db).filter(lesson_id__in=lesson_ids)
        )

        LessonAsset = apps.get_model('curriculum', 'LessonAsset')
        scoped['LessonAsset'] = list(
            LessonAsset.objects.using(self.source_db).filter(lesson_id__in=lesson_ids)
        )

        # 9. LearningExperienceGraph & Simulation
        LearningExperienceGraph = apps.get_model('curriculum', 'LearningExperienceGraph')
        scoped['LearningExperienceGraph'] = list(
            LearningExperienceGraph.objects.using(self.source_db).filter(learning_unit_id__in=lu_ids)
        )

        Simulation = apps.get_model('curriculum', 'Simulation')
        scoped['Simulation'] = list(Simulation.objects.using(self.source_db).all())

        return scoped

    def _build_diff(self, scoped_source_objects: dict[str, list], report: PublicationReport):
        """Computes the created, updated, unchanged, and production-only records per model."""
        for model_name in SYNCED_MODEL_NAMES:
            source_objects = scoped_source_objects.get(model_name, [])
            syncer = get_syncer_for_model(model_name, self.source_db, self.target_db)
            self.fk_remapper.register_syncer(model_name, syncer)

            created_count = 0
            updated_count = 0
            unchanged_count = 0
            matched_target_pks = set()

            for src_obj in source_objects:
                target_match = syncer.match(src_obj)
                if target_match is None:
                    created_count += 1
                else:
                    matched_target_pks.add(target_match.pk)
                    if syncer.has_changed(src_obj, target_match):
                        updated_count += 1
                    else:
                        unchanged_count += 1

            report.counts[model_name] = {
                'created': created_count,
                'updated': updated_count,
                'unchanged': unchanged_count,
            }

            # Check for production-only content (never deleted, reported only)
            cached_target_objs = (
                syncer._target_cache_by_natural_key.values()
                if model_name in NATURAL_KEY_MODELS
                else syncer._target_cache_by_uuid.values()
            )
            prod_only = [
                f"{model_name} (PK {tgt.pk})"
                for tgt in cached_target_objs
                if tgt.pk not in matched_target_pks
            ]
            if prod_only:
                report.production_only_items[model_name] = prod_only

    def _reset_target_sequences(self):
        """Ensures all PostgreSQL primary key sequences on target DB match or exceed MAX(id)."""
        from django.db import connections
        with connections[self.target_db].cursor() as cursor:
            for model_name in SYNCED_MODEL_NAMES:
                model = apps.get_model('curriculum', model_name)
                table = model._meta.db_table
                sql = f"SELECT setval(pg_get_serial_sequence('{table}', 'id'), COALESCE((SELECT MAX(id) FROM {table}), 1));"
                try:
                    cursor.execute(sql)
                except Exception as e:
                    logger.warning(f"Could not reset sequence for {table}: {e}")

    def _apply_publication(
        self,
        scoped_source_objects: dict[str, list],
        media_report,
        report: PublicationReport,
    ):
        """Executes the publication within an advisory lock and database transaction."""
        lock = PublicationLock()
        with lock:
            # 1. Upload local media if needed
            if media_report.local_file_count > 0:
                media_publisher = MediaPublisher(dry_run=False)
                for item in media_report.items:
                    if item.media_type == 'local_file':
                        try:
                            cloud_url = media_publisher.upload_local_file(item.resolved_url)
                            item.resolved_url = cloud_url
                        except Exception as e:
                            report.errors.append(f"Media upload failed: {e}")
                            return

            # 2. Reset sequences on target DB
            self._reset_target_sequences()

            # 3. Database transaction on target with bootstrap signals disabled
            from curriculum.publisher.signals import disable_curriculum_signals
            import sys

            try:
                with disable_curriculum_signals():
                    with transaction.atomic(using=self.target_db):
                        for model_name in SYNCED_MODEL_NAMES:
                            source_objects = scoped_source_objects.get(model_name, [])
                            syncer = get_syncer_for_model(model_name, self.source_db, self.target_db)
                            self.fk_remapper.register_syncer(model_name, syncer)

                            if self.verbosity >= 1 and source_objects:
                                sys.stdout.write(f"  Publishing {model_name:<26} ({len(source_objects)} source records)... ")
                                sys.stdout.flush()

                            syncer.sync_batch(source_objects, self.fk_remapper, dry_run=False)
                            syncer.sync_m2m_batch(source_objects, self.fk_remapper, dry_run=False)

                            if self.verbosity >= 1 and source_objects:
                                sys.stdout.write("done.\n")
                                sys.stdout.flush()

            except Exception as e:
                logger.exception("Publication transaction failed on target database")
                report.errors.append(f"Transaction failed: {str(e)}")
