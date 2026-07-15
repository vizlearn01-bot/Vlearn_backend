"""
curriculum/generation/blueprint_orchestrator.py

V2 generation engine — Instructional Blueprint pipeline.

Execution order
---------------
1.  Load the GenerationJob + related Lesson / LearningUnit.
2.  Update job status → 'generating'.
3.  RetrievalService.assemble_context()          [reused unchanged]
4.  BlueprintPromptBuilder.build_blueprint_prompt()
5.  LLMClient.generate()                          [reused unchanged]
6.  Strip any markdown fences from the LLM response.
7.  json.loads() the raw response.
8.  validate_skeleton()                           [reused from skeleton.py]
9.  SkeletonTranslator.translate()                [reused from skeleton.py]
10. BlueprintPersistenceService.save_blueprint()
11. Update lesson title from blueprint (first page title or learning-unit name).
12. Update job status → 'completed'.

The legacy V1 orchestrator (orchestrator.py) is NOT touched.
This module is completely self-contained.
"""

from __future__ import annotations
import json
import re

from curriculum.models import GenerationJob, LessonBlock
from curriculum.generation.retrieval import RetrievalService
from curriculum.generation.llm_client import LLMClient
from curriculum.generation.skeleton import validate_skeleton, SkeletonTranslator
from curriculum.generation.blueprint_prompt import build_blueprint_prompt
from curriculum.generation.blueprint_persistence import BlueprintPersistenceService
from curriculum.generation.persistence import LessonPersistenceService  # for job-status helper


# ---------------------------------------------------------------------------
# Markdown fence stripper
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r'^```(?:json)?\s*|\s*```$', re.MULTILINE)


def _strip_fences(text: str) -> str:
    """Remove leading/trailing markdown code fences the LLM sometimes adds."""
    return _FENCE_RE.sub('', text).strip()


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

class BlueprintOrchestrator:
    """
    Replacement generation engine for `generation_mode='blueprint'` jobs.

    Only `execute_job` is public.  All heavy lifting is delegated to the
    specialist modules above.
    """

    @staticmethod
    def execute_job(job_id: int) -> None:
        job = GenerationJob.objects.select_related(
            'lesson',
            'lesson__learning_unit',
            'lesson__learning_unit__topic',
            'lesson__learning_unit__topic__subject',
        ).get(id=job_id)

        try:
            LessonPersistenceService.update_job_status(job.id, 'generating')

            lesson        = job.lesson
            learning_unit = lesson.learning_unit

            if not learning_unit:
                raise ValueError(
                    "Lesson has no associated LearningUnit. "
                    "Blueprint generation requires a LearningUnit."
                )

            # ── Step 3: Retrieve knowledge chunks ─────────────────────────────
            context_package = RetrievalService.assemble_context(learning_unit.id)

            # ── Step 4: Build the instructional-designer prompt ───────────────
            prompt = build_blueprint_prompt(context_package)

            # ── Step 5: Call the LLM ──────────────────────────────────────────
            raw_response = LLMClient.generate(prompt)

            # ── Step 6: Strip markdown fences (LLM sometimes wraps JSON) ──────
            clean_response = _strip_fences(raw_response)

            # ── Step 7: Parse JSON ────────────────────────────────────────────
            try:
                skeleton = json.loads(clean_response)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"LLM returned non-JSON output. "
                    f"First 300 chars: {clean_response[:300]!r}"
                ) from exc

            # ── Step 8: Validate skeleton structure ───────────────────────────
            errors = validate_skeleton(skeleton)
            if errors:
                raise ValueError(
                    f"Blueprint skeleton validation failed:\n" + "\n".join(errors)
                )

            # ── Step 9: Translate blueprint → block kwargs ────────────────────
            block_kwargs_list = SkeletonTranslator.translate(skeleton)

            if not block_kwargs_list:
                raise ValueError(
                    "SkeletonTranslator produced zero blocks. "
                    "The blueprint may be malformed."
                )

            # ── Step 10: Persist blocks + pending asset slots ─────────────────
            summary = BlueprintPersistenceService.save_blueprint(lesson, block_kwargs_list)

            # ── Step 11: Set lesson title from blueprint ──────────────────────
            pages = skeleton.get('pages', [])
            if pages:
                # Use the first page's title as the lesson title if not yet set,
                # or build one from the topic + learning unit names.
                lesson_title = (
                    lesson.title
                    or f"{context_package['topic']} — {context_package['learning_unit']}"
                )
                lesson.title = lesson_title
                lesson.save(update_fields=['title'])

            # ── Step 12: Mark job completed ───────────────────────────────────
            LessonPersistenceService.update_job_status(job.id, 'completed')

        except Exception as exc:
            LessonPersistenceService.update_job_status(job.id, 'failed', str(exc))
            raise
