"""
VisualGeneratorAgent
--------------------
Takes a free-text admin prompt and a LessonBlock, builds focused curriculum
context, calls the VisualReasoner, and safely attaches the result as a LessonAsset.
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

        1. Fetches the VisualGenerationJob from the DB with full curriculum hierarchy.
        2. Builds focused pedagogical context combining:
           - Curriculum / Grade / Subject / Topic / LearningUnit
           - LessonBlock type and content snippet
           - Existing visual metadata if updating
           - Administrator's explicit instruction
        3. Calls VisualReasoner.evaluate_requirement().
        4. On success:
           - Creates a LessonAsset with generated code.
           - Attaches it to the block.
           - Safely archives/detaches previous visual assets (safe non-destructive replacement).
           - Marks job completed.
        5. On failure:
           - Preserves existing assets completely intact.
           - Marks job failed with the specific failure reason.
        """
        from curriculum.models import VisualGenerationJob, LessonAsset
        from curriculum.media_orchestration.contracts import MediaRequirement
        from curriculum.media_orchestration.visual_intelligence.reasoner import VisualReasoner

        job = VisualGenerationJob.objects.select_related(
            'lesson_block',
            'lesson_block__lesson',
            'lesson_block__lesson__topic',
            'lesson_block__lesson__topic__subject',
            'lesson_block__lesson__topic__subject__grade',
            'lesson_block__lesson__topic__subject__grade__curriculum',
            'lesson_block__lesson__learning_unit',
        ).get(id=visual_job_id)

        job.status = 'generating'
        job.save(update_fields=['status'])

        block = job.lesson_block
        lesson = block.lesson
        topic = lesson.topic if lesson else None
        subject = topic.subject if topic else None
        grade = subject.grade if subject else None
        curriculum = grade.curriculum if grade else None
        learning_unit = lesson.learning_unit if lesson else None

        # Existing visual info (if updating)
        existing_assets = list(block.assets.all())
        existing_visual_summary = None
        if existing_assets:
            primary_asset = existing_assets[0]
            existing_visual_summary = {
                "id": primary_asset.id,
                "asset_type": primary_asset.asset_type,
                "title": primary_asset.title,
                "description": primary_asset.description,
                "format": (primary_asset.metadata or {}).get('visual_format', ''),
            }

        # Content preview (up to 250 chars)
        content_preview = ""
        if isinstance(block.content, dict):
            content_preview = (
                block.content.get('text')
                or block.content.get('question')
                or block.content.get('prompt')
                or str(block.content)
            )[:250]
        elif isinstance(block.content, str):
            content_preview = block.content[:250]

        pedagogical_context = {
            "curriculum": curriculum.name if curriculum else "General Curriculum",
            "grade_level": grade.name if grade else "",
            "subject": subject.name if subject else "",
            "topic": topic.name if topic else "",
            "learning_unit": learning_unit.name if learning_unit else (topic.name if topic else ""),
            "lesson_title": lesson.title or "",
            "component_type": block.component_type or block.block_type,
            "block_title": block.title or "",
            "relevant_block_content": content_preview,
            "existing_visual": existing_visual_summary,
            "administrator_instruction": job.prompt,
        }

        try:
            req_desc = (
                f"Subject: {pedagogical_context['subject']} ({pedagogical_context['grade_level']}). "
                f"Topic: {pedagogical_context['topic']} - Unit: {pedagogical_context['learning_unit']}. "
                f"Requested visual: {job.prompt}"
            )

            req = MediaRequirement(
                node_id=f"visual_job_{job.pk}",
                requirement_type="visual",
                description=req_desc,
                search_keywords=job.prompt.split()[:8],
                entity_name=pedagogical_context['topic'] or pedagogical_context['subject'],
            )

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
            new_asset = LessonAsset.objects.create(
                lesson=lesson,
                asset_type='generated',
                source_type='ai_generated',
                storage_type='url',
                status='attached',
                title=f"AI Visual: {job.prompt[:40]}",
                description=job.prompt,
                metadata={
                    'visual_format': fmt,
                    'generated_code': code,
                    'alt_text': getattr(visual_spec, 'alt_text', '') or '',
                    'visual_job_id': job.pk,
                    'component_tag': block.component_type or block.block_type,
                    'admin_instruction': job.prompt,
                },
            )
            new_asset.blocks.add(block)

            # Safe replacement: only detach/archive previous assets after the new one succeeded
            for old_a in existing_assets:
                old_a.blocks.remove(block)
                if old_a.blocks.count() == 0:
                    old_a.status = 'archived'
                    old_a.save(update_fields=['status'])

            # Update lesson block content to ready status
            if isinstance(block.content, dict):
                block.content['status'] = 'ready'
                block.content['visual_format'] = fmt
                block.content['alt_text'] = getattr(visual_spec, 'alt_text', '') or ''
                block.save(update_fields=['content'])

            job.result_asset = new_asset
            job.status = 'completed'
            job.save(update_fields=['result_asset', 'status', 'updated_at'])
            logger.info("[VisualAgent] Job %d completed — asset #%d created.", job.pk, new_asset.pk)

        except Exception as exc:
            logger.error("[VisualAgent] Job %d errored: %s", job.pk, exc, exc_info=True)
            job.status = 'failed'
            job.error_message = str(exc)
            job.save(update_fields=['status', 'error_message', 'updated_at'])
            raise
