"""
VisualGeneratorAgent
--------------------
Takes a free-text admin prompt and a LessonBlock, calls the existing
VisualReasoner (which already produces SVG/Mermaid), and attaches the
result as a LessonAsset to the block.
"""
import logging
from typing import Tuple, Optional

logger = logging.getLogger("curriculum.ai_ingestion.visual")


class VisualGeneratorAgent:
    """
    Wraps the existing VisualReasoner for on-demand visual generation.
    Used by the generate_visual Celery task to fulfil VisualGenerationJob requests.
    """

    @staticmethod
    def run(visual_job_id: int) -> None:
        """
        Execute a VisualGenerationJob.

        1. Fetches the VisualGenerationJob from the DB.
        2. Builds a synthetic MediaRequirement from the admin's prompt.
        3. Calls VisualReasoner.evaluate_requirement().
        4. On success: creates a LessonAsset, attaches it to the block, marks job completed.
        5. On failure: marks job failed with the reason.
        """
        from curriculum.models import VisualGenerationJob, LessonAsset
        from curriculum.media_orchestration.contracts import MediaRequirement
        from curriculum.media_orchestration.visual_intelligence.reasoner import VisualReasoner

        job = VisualGenerationJob.objects.select_related(
            'lesson_block', 'lesson_block__lesson'
        ).get(id=visual_job_id)

        job.status = 'generating'
        job.save(update_fields=['status'])

        try:
            # Build a MediaRequirement from the admin's prompt
            req = MediaRequirement(
                node_id=f"visual_job_{job.pk}",
                requirement_type="visual",
                description=job.prompt,
                search_keywords=job.prompt.split()[:8],
                entity_name="",
            )

            pedagogical_context = {
                "block_type": job.lesson_block.block_type,
                "block_title": job.lesson_block.title or "",
                "admin_prompt": job.prompt,
            }

            reasoner = VisualReasoner()
            visual_spec, failure = reasoner.evaluate_requirement(req, pedagogical_context)

            if failure or visual_spec is None:
                reason = failure.reason if failure else "Visual reasoner returned no result."
                job.status = 'failed'
                job.error_message = reason
                job.save(update_fields=['status', 'error_message', 'updated_at'])
                logger.warning("[VisualAgent] Job %d failed: %s", job.pk, reason)
                return

            # Determine format
            code = visual_spec.code or ""
            fmt = getattr(visual_spec, 'format', 'svg') or 'svg'

            # Create LessonAsset with the generated code stored in metadata
            asset = LessonAsset.objects.create(
                lesson=job.lesson_block.lesson,
                asset_type='generated',
                source_type='ai_generated',
                storage_type='url',
                status='attached',
                title=job.lesson_block.title or f"Generated Visual #{job.pk}",
                description=job.prompt,
                metadata={
                    'visual_format': fmt,
                    'generated_code': code,
                    'alt_text': getattr(visual_spec, 'alt_text', '') or '',
                    'visual_job_id': job.pk,
                },
            )
            asset.blocks.add(job.lesson_block)

            job.result_asset = asset
            job.status = 'completed'
            job.save(update_fields=['result_asset', 'status', 'updated_at'])
            logger.info("[VisualAgent] Job %d completed — asset #%d created.", job.pk, asset.pk)

        except Exception as exc:
            logger.error("[VisualAgent] Job %d errored: %s", job.pk, exc)
            job.status = 'failed'
            job.error_message = str(exc)
            job.save(update_fields=['status', 'error_message', 'updated_at'])
            raise
