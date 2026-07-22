"""
RichnessEngine — Lesson Richness Metrics

Computes a structured richness report for a generated lesson after assembly.
Stored in LearningExperienceGraph.quality_report['richness'].
"""
from dataclasses import dataclass, field, asdict
from typing import Optional
import math

from curriculum.models import Lesson, LessonBlock, LessonAsset


@dataclass
class LessonRichnessReport:
    """
    Quantitative description of a lesson's instructional richness.
    Generated after ExperienceAssemblyService completes.
    """
    learning_moments: int = 0       # distinct concept_group values
    pages_estimate: int = 0         # estimated page count (based on cognitive load)
    blocks: int = 0                 # total LessonBlock count
    total_words: int = 0            # approximate word count across all content blocks
    images: int = 0                 # resolved image assets
    simulations: int = 0            # suggested_simulation blocks
    worked_examples: int = 0        # worked_example blocks
    knowledge_checks: int = 0       # knowledge_check blocks
    real_world_examples: int = 0    # real_world_example blocks
    reflections: int = 0            # reflection + summary blocks
    estimated_reading_time_minutes: float = 0.0
    visual_to_text_ratio: float = 0.0   # images / max(1, paragraphs)
    richness_score: float = 0.0         # 0.0-1.0 composite score

    def to_dict(self) -> dict:
        return asdict(self)


# ---------------------------------------------------------------------------
# Scoring weights for richness_score calculation
# ---------------------------------------------------------------------------
_SCORE_WEIGHTS = {
    'blocks':           (0.15, 12),     # (weight, target value for full score)
    'images':           (0.20, 4),
    'simulations':      (0.15, 1),
    'worked_examples':  (0.15, 1),
    'knowledge_checks': (0.15, 1),
    'real_world':       (0.10, 1),
    'reflections':      (0.10, 1),
}

# Cognitive load per block type (matches PageGroupingService.js estimateBlockCognitiveLoad)
_COGNITIVE_LOAD = {
    'suggested_simulation': 5,
    'simulation_placeholder': 5,
    'worked_example': 3,
    'knowledge_check': 3,
    'formula_breakdown': 3,
    'concept_explanation': 2,
    'definitions': 2,
    'experiment': 2,
}
_MAX_COGNITIVE_LOAD = 10  # matches PageGroupingService.js MAX_COGNITIVE_LOAD


class RichnessEngine:
    """
    Calculates lesson richness metrics from the assembled LessonBlocks and LessonAssets.
    """

    @staticmethod
    def calculate(lesson: Lesson) -> LessonRichnessReport:
        report = LessonRichnessReport()

        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by('order'))
        report.blocks = len(blocks)

        if not blocks:
            return report

        # Count learning moments (distinct concept_groups)
        concept_groups = set()
        total_words = 0
        simulations = 0
        worked_examples = 0
        knowledge_checks = 0
        real_world = 0
        reflections = 0
        paragraphs = 0  # text-bearing blocks

        for block in blocks:
            bt = (block.block_type or '').lower()

            # Concept group tracking
            cg = (block.metadata or {}).get('concept_group', '') or ''
            if cg:
                concept_groups.add(cg)

            # Block type tallies
            if bt in ('suggested_simulation', 'simulation_placeholder'):
                simulations += 1
            if bt == 'worked_example':
                worked_examples += 1
            if bt in ('knowledge_check', 'revision_questions', 'multiple_choice', 'true_false'):
                knowledge_checks += 1
            if bt == 'real_world_example':
                real_world += 1
            if bt in ('reflection', 'summary', 'key_takeaway'):
                reflections += 1

            # Word count from content
            content = block.content or {}
            text = ''
            if isinstance(content, dict):
                text = str(content.get('text', '') or '')
            elif isinstance(content, str):
                text = content
            words = len(text.split()) if text else 0
            total_words += words
            if words > 0:
                paragraphs += 1

        report.learning_moments = max(len(concept_groups), 1)
        report.total_words = total_words
        report.simulations = simulations
        report.worked_examples = worked_examples
        report.knowledge_checks = knowledge_checks
        report.real_world_examples = real_world
        report.reflections = reflections

        # Count resolved image assets
        images = LessonAsset.objects.filter(
            lesson=lesson,
            asset_type='image',
            status='attached'
        ).count()
        report.images = images

        # Estimated reading time (200 wpm average)
        text_minutes = (total_words / 200.0)
        media_minutes = (
            simulations * 3.0 +
            knowledge_checks * 2.0 +
            worked_examples * 1.5 +
            images * 0.5
        )
        report.estimated_reading_time_minutes = round(text_minutes + media_minutes, 1)

        # Estimated page count using cognitive load simulation
        estimated_pages = 1
        current_load = 0
        for block in blocks:
            bt = (block.block_type or '').lower()
            block_load = _COGNITIVE_LOAD.get(bt, 1)
            if current_load + block_load > _MAX_COGNITIVE_LOAD and current_load > 0:
                estimated_pages += 1
                current_load = block_load
            else:
                current_load += block_load
        report.pages_estimate = estimated_pages

        # Visual-to-text ratio
        report.visual_to_text_ratio = round(images / max(1, paragraphs), 3)

        # Composite richness score (0.0 - 1.0)
        score = 0.0
        for metric, (weight, target) in _SCORE_WEIGHTS.items():
            value = {
                'blocks': report.blocks,
                'images': report.images,
                'simulations': report.simulations,
                'worked_examples': report.worked_examples,
                'knowledge_checks': report.knowledge_checks,
                'real_world': report.real_world_examples,
                'reflections': report.reflections,
            }.get(metric, 0)
            score += weight * min(1.0, value / max(1, target))

        report.richness_score = round(score, 3)

        return report
