import logging
import gc
from celery import shared_task
from django.db import close_old_connections
from django.utils import timezone

logger = logging.getLogger('curriculum')


@shared_task(
    bind=True,
    name='curriculum.tasks.process_textbook_pipeline',
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=3,
    retry_jitter=True,
    queue='heavy_ops',
)
def process_textbook_pipeline_task(self, knowledge_pack_id: int):
    """
    Celery task for Document Ingestion and Knowledge Repository Construction.
    Accepts primitive ID argument, fetches fresh KnowledgePack from DB, manages connection cleanup,
    and performs garbage collection after heavy PDF/OCR processing.
    """
    from curriculum.models import KnowledgePack
    from curriculum.extraction_pipeline import DocumentIngestionService

    close_old_connections()
    kp = KnowledgePack.objects.filter(id=knowledge_pack_id).first()
    if not kp:
        logger.error(f"[Task {self.request.id}] KnowledgePack ID {knowledge_pack_id} not found.")
        return

    logger.info(f"[Task {self.request.id}] Starting textbook extraction for KnowledgePack ID {knowledge_pack_id}")
    try:
        service = DocumentIngestionService(knowledge_pack_id)
        service.process()
        logger.info(f"[Task {self.request.id}] Completed textbook extraction for KnowledgePack ID {knowledge_pack_id}")
    except Exception as exc:
        logger.error(f"[Task {self.request.id}] Ingestion failed for KnowledgePack ID {knowledge_pack_id}: {exc}")
        try:
            kp.refresh_from_db()
            kp.status = 'failed'
            kp.save()
        except Exception as save_err:
            logger.error(f"[Task {self.request.id}] Failed to set failure status on KP {knowledge_pack_id}: {save_err}")
        raise exc
    finally:
        gc.collect()
        close_old_connections()


@shared_task(
    bind=True,
    name='curriculum.tasks.regenerate_lesson_block',
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=3,
    retry_jitter=True,
    queue='default',
)
def regenerate_lesson_block_task(self, job_id: int):
    """
    Celery task for Single Block AI Regeneration.
    Updates GenerationJob status, executes GenerationOrchestrator, and handles failure recording.
    """
    from curriculum.models import GenerationJob
    from curriculum.generation.orchestrator import GenerationOrchestrator

    close_old_connections()
    job = GenerationJob.objects.filter(id=job_id).first()
    if not job:
        logger.error(f"[Task {self.request.id}] GenerationJob ID {job_id} not found.")
        return

    logger.info(f"[Task {self.request.id}] Starting block regeneration for GenerationJob ID {job_id}")
    try:
        GenerationOrchestrator.execute_job(job_id)
        logger.info(f"[Task {self.request.id}] Completed block regeneration for GenerationJob ID {job_id}")
    except Exception as exc:
        logger.error(f"[Task {self.request.id}] Block regeneration failed for Job ID {job_id}: {exc}")
        try:
            job.refresh_from_db()
            job.status = 'failed'
            job.error_message = str(exc)
            job.completed_at = timezone.now()
            job.save()
        except Exception as save_err:
            logger.error(f"[Task {self.request.id}] Failed to set failure status on Job {job_id}: {save_err}")
        raise exc
    finally:
        close_old_connections()


@shared_task(
    bind=True,
    name='curriculum.tasks.execute_generation_job',
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=3,
    retry_jitter=True,
    queue='heavy_ops',
)
def execute_generation_job_task(self, job_id: int):
    """
    Celery task for Full Lesson AI Generation.
    Selects target orchestrator engine based on generation_mode and executes job asynchronously.
    """
    from curriculum.models import GenerationJob
    from curriculum.generation.orchestrator import GenerationOrchestrator
    from curriculum.generation.blueprint_orchestrator import BlueprintOrchestrator

    close_old_connections()
    job = GenerationJob.objects.select_related('lesson', 'lesson__learning_unit', 'lesson__learning_unit__topic', 'lesson__learning_unit__topic__subject').filter(id=job_id).first()
    if not job:
        logger.error(f"[Task {self.request.id}] GenerationJob ID {job_id} not found.")
        return

    mode = job.generation_mode
    logger.info(f"[Task {self.request.id}] Executing generation job ID {job_id} (mode: {mode})")

    try:
        if mode == 'blueprint':
            learning_unit = job.lesson.learning_unit
            subject_name = learning_unit.topic.subject.name.lower() if (learning_unit and learning_unit.topic and learning_unit.topic.subject) else ''
            if subject_name == 'chemistry':
                from curriculum.generation.engines.chemistry.orchestrator import ChemistryOrchestrator
                orchestrator_fn = ChemistryOrchestrator.execute_job
            else:
                orchestrator_fn = BlueprintOrchestrator.execute_job
        elif mode == 'learning_experience_planner':
            from curriculum.generation.planner.engine import PedagogicalEngine
            orchestrator_fn = PedagogicalEngine.execute_job
        else:
            orchestrator_fn = GenerationOrchestrator.execute_job

        orchestrator_fn(job_id)
        logger.info(f"[Task {self.request.id}] Successfully completed generation job ID {job_id}")
    except Exception as exc:
        logger.error(f"[Task {self.request.id}] Generation job ID {job_id} failed: {exc}")
        try:
            job.refresh_from_db()
            job.status = 'failed'
            job.error_message = str(exc)
            job.completed_at = timezone.now()
            job.save()
        except Exception as save_err:
            logger.error(f"[Task {self.request.id}] Failed to set failure status on Job {job_id}: {save_err}")
        raise exc
    finally:
        gc.collect()
        close_old_connections()


@shared_task(
    bind=True,
    name='curriculum.tasks.semantic_structure_extraction',
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=3,
    retry_jitter=True,
    queue='heavy_ops',
)
def semantic_structure_extraction_task(self, knowledge_pack_id: int, unit_ids: list):
    """
    Celery task for Semantic Structure Graph Extraction post KnowledgePack approval.
    """
    from curriculum.semantic_extraction import SemanticStructuringService

    close_old_connections()
    logger.info(f"[Task {self.request.id}] Starting semantic extraction for KP ID {knowledge_pack_id} across {len(unit_ids)} units")
    try:
        for unit_id in unit_ids:
            try:
                service = SemanticStructuringService(unit_id, knowledge_pack_id)
                service.process()
            except Exception as e:
                logger.error(f"[Task {self.request.id}] Semantic extraction failed for LU {unit_id}: {e}")
        logger.info(f"[Task {self.request.id}] Completed semantic extraction for KP ID {knowledge_pack_id}")
    finally:
        close_old_connections()
