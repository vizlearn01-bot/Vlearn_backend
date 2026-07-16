"""
curriculum/generation/engines/chemistry/orchestrator.py

Chemistry-specific Learning Experience Engine Orchestrator.

Execution order
---------------
1.  Load the GenerationJob + related Lesson / LearningUnit.
2.  Update job status -> 'generating'.
3.  RetrievalService.assemble_context()
4.  build_chemistry_prompt()
5.  LLMClient.generate()
6.  Strip markdown fences.
7.  Parse JSON.
8.  validate_learning_experience_schema()
9.  LearningExperienceTranslator.translate()
10. BlueprintPersistenceService.save_blueprint()
11. Update lesson title.
12. Update job status -> 'completed'.
"""

from __future__ import annotations
import json
import re

from curriculum.models import GenerationJob
from curriculum.generation.retrieval import RetrievalService
from curriculum.generation.llm_client import LLMClient
from curriculum.generation.blueprint_persistence import BlueprintPersistenceService
from curriculum.generation.persistence import LessonPersistenceService

from .prompt import build_chemistry_prompt
from .learning_experience import validate_learning_experience_schema, LearningExperienceTranslator


_FENCE_RE = re.compile(r'^```(?:json)?\s*|\s*```$', re.MULTILINE)

def _strip_fences(text: str) -> str:
    """Remove leading/trailing markdown code fences the LLM sometimes adds."""
    return _FENCE_RE.sub('', text).strip()


class ChemistryOrchestrator:
    """
    Learning Experience Engine for Chemistry jobs.
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

            lesson = job.lesson
            learning_unit = lesson.learning_unit

            if not learning_unit:
                raise ValueError(
                    "Lesson has no associated LearningUnit. "
                    "Chemistry Learning Experience generation requires a LearningUnit."
                )

            # 3. Retrieve knowledge chunks
            context_package = RetrievalService.assemble_context(learning_unit.id)

            # 4. Build the instructional-designer prompt
            prompt = build_chemistry_prompt(context_package)

            # 5. Call the LLM
            raw_response = LLMClient.generate(prompt)

            # 6. Strip markdown fences
            clean_response = _strip_fences(raw_response)

            # 7. Parse JSON
            try:
                blueprint = json.loads(clean_response)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"LLM returned non-JSON output. "
                    f"First 300 chars: {clean_response[:300]!r}"
                ) from exc

            # 8. Validate learning experience schema
            errors = validate_learning_experience_schema(blueprint)
            if errors:
                raise ValueError(
                    f"Chemistry Learning Experience validation failed:\n" + "\n".join(errors)
                )

            # 9. Translate blueprint -> block kwargs (Compatibility Layer)
            block_kwargs_list = LearningExperienceTranslator.translate(blueprint)

            if not block_kwargs_list:
                raise ValueError(
                    "LearningExperienceTranslator produced zero blocks. "
                    "The blueprint may be malformed."
                )

            # 10. Persist blocks + pending asset slots
            summary = BlueprintPersistenceService.save_blueprint(lesson, block_kwargs_list)

            # 11. Set lesson title from blueprint
            lesson_title = blueprint.get('lesson_title')
            if lesson_title:
                lesson.title = lesson_title
                lesson.save(update_fields=['title'])
            elif not lesson.title:
                lesson.title = f"{context_package['topic']} — {context_package['learning_unit']}"
                lesson.save(update_fields=['title'])

            # 12. Mark job completed
            LessonPersistenceService.update_job_status(job.id, 'completed')

        except Exception as exc:
            LessonPersistenceService.update_job_status(job.id, 'failed', str(exc))
            raise
