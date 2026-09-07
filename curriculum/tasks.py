import logging
import gc
from celery import shared_task
from django.db import close_old_connections
from django.utils import timezone

logger = logging.getLogger('curriculum')


def dispatch_background_task(task, *args, **kwargs):
    """
    Dispatches a background task.
    If CELERY_TASK_ALWAYS_EAGER is True (local dev without Redis),
    runs the task in a detached daemon thread so the HTTP request
    returns immediately and the UI can poll progress asynchronously.
    Otherwise, enqueues to Celery on transaction commit.
    """
    from django.conf import settings
    if getattr(settings, 'CELERY_TASK_ALWAYS_EAGER', False):
        import threading
        def _runner():
            from django.db import connection
            connection.close()
            try:
                task.delay(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in background task daemon thread: {e}", exc_info=True)
            finally:
                connection.close()

        thread = threading.Thread(target=_runner, daemon=True)
        thread.start()
    else:
        from django.db import transaction
        transaction.on_commit(lambda: task.delay(*args, **kwargs))


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
    name='curriculum.tasks.ai_ingestion_pipeline',
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=2,
    retry_jitter=True,
    queue='heavy_ops',
)
def ai_ingestion_pipeline_task(self, knowledge_pack_id: int):
    """
    Celery task for AI Ingestion — runs TopicModuleGenerationAgent after
    document extraction to auto-generate the Topic/LearningUnit hierarchy.

    This task is chained after process_textbook_pipeline_task when the
    upload mode is 'ai_ingestion'.  It runs after extraction has finished
    (KP status == 'review'), so the LLM has textbook chunks to work with.

    Human approval of the KP is still required before lesson generation.
    """
    from curriculum.models import KnowledgePack
    from curriculum.ai_ingestion.agent import TopicModuleGenerationAgent

    close_old_connections()
    kp = KnowledgePack.objects.filter(id=knowledge_pack_id).first()
    if not kp:
        logger.error(f"[Task {self.request.id}] AI Ingestion: KnowledgePack ID {knowledge_pack_id} not found.")
        return

    if kp.status not in ('review', 'approved'):
        logger.warning(
            f"[Task {self.request.id}] AI Ingestion: KP {knowledge_pack_id} not in 'review' status "
            f"(current: {kp.status}). Skipping hierarchy generation."
        )
        return

    logger.info(f"[Task {self.request.id}] AI Ingestion starting for KP {knowledge_pack_id}")
    try:
        TopicModuleGenerationAgent.run(knowledge_pack_id)
        logger.info(f"[Task {self.request.id}] AI Ingestion completed for KP {knowledge_pack_id}")
    except Exception as exc:
        logger.error(f"[Task {self.request.id}] AI Ingestion failed for KP {knowledge_pack_id}: {exc}")
        raise exc
    finally:
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
    Routes through the V3 PedagogicalEngine (execute_generation_job_task)
    rather than the legacy V1 GenerationOrchestrator.

    This fixes the defect where block regeneration used the V1 pipeline
    instead of the active V3 engine.
    """
    from curriculum.models import GenerationJob
    from curriculum.generation.planner.engine import PedagogicalEngine

    close_old_connections()
    job = GenerationJob.objects.filter(id=job_id).first()
    if not job:
        logger.error(f"[Task {self.request.id}] GenerationJob ID {job_id} not found.")
        return

    logger.info(f"[Task {self.request.id}] Starting block regeneration (V3) for GenerationJob ID {job_id}")
    try:
        PedagogicalEngine.execute_job(job_id)
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


@shared_task(
    bind=True,
    name='curriculum.tasks.generate_visual',
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=2,
    retry_jitter=True,
    queue='default',
)
def generate_visual_task(self, visual_job_id: int):
    """
    Celery task for on-demand visual generation from an admin-provided prompt.
    Delegates to VisualGeneratorAgent which calls the existing VisualReasoner.
    """
    from curriculum.ai_ingestion.visual_agent import VisualGeneratorAgent

    close_old_connections()
    logger.info(f"[Task {self.request.id}] Starting visual generation for VisualGenerationJob ID {visual_job_id}")
    try:
        VisualGeneratorAgent.run(visual_job_id)
        logger.info(f"[Task {self.request.id}] Completed visual generation for VisualGenerationJob ID {visual_job_id}")
    except Exception as exc:
        logger.error(f"[Task {self.request.id}] Visual generation failed for Job ID {visual_job_id}: {exc}")
        raise exc
    finally:
        close_old_connections()
