"""Curriculum services package."""
from curriculum.services.legacy_generator import LessonGeneratorService
from curriculum.services.quiz_generation_service import (
    generate_revision_quiz_for_topic,
    grade_kcse_answer_with_llm,
    grade_full_exam_paper,
)

__all__ = [
    "LessonGeneratorService",
    "generate_revision_quiz_for_topic",
    "grade_kcse_answer_with_llm",
    "grade_full_exam_paper",
]
