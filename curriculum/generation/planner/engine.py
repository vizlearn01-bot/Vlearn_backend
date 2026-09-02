import logging
from dataclasses import dataclass, field
from typing import List

from curriculum.models import GenerationJob, LearningExperienceGraph
from curriculum.generation.llm_client import LLMClient
from curriculum.generation.persistence import LessonPersistenceService

from .knowledge_assembler import KnowledgeAssembler
from .prompt import build_planner_prompt
from .models import LearningExperiencePlan
from .graph_validator import GraphValidator
from curriculum.media_orchestration.assembler import ExperienceAssemblyService
from curriculum.generation.optimizer.validator import CompilerValidator
from curriculum.generation.optimizer.engine import OptimizerEngine
from curriculum.generation.optimizer.quality import QualityEngine
from curriculum.generation.optimizer.media_validator import MediaValidator
from curriculum.generation.optimizer.models import EngineReport
from curriculum.generation.optimizer.richness import RichnessEngine
from curriculum.generation.intelligence.selection import FrameworkSelectionEngine

logger = logging.getLogger("curriculum.generation")

# ---------------------------------------------------------------------------
# Adaptive complexity targets — scales expected lesson depth by topic type
# ---------------------------------------------------------------------------
COMPLEXITY_TARGETS = {
    'simple':   {'min_nodes': 8,  'min_diversity_types': 5},
    'standard': {'min_nodes': 9, 'min_diversity_types': 6},
    'complex':  {'min_nodes': 11, 'min_diversity_types': 6},
}

# Diversity buckets: each maps a bucket name to a list of node_type substrings
# At least one node from each required bucket must be present for the lesson to pass.
REQUIRED_DIVERSITY_BUCKETS = {
    'explanation':    ['explain', 'concept', 'core', 'present', 'teach', 'introduction', 'hook'],
    'visualization':  ['visual', 'diagram', 'observe', 'illustrat', 'chart', 'graph'],
    'worked_example': ['worked', 'example', 'demonstrat', 'guided_practice'],
    'assessment':     ['assess', 'quiz', 'check', 'predict', 'practice', 'knowledge_check', 'question'],
    'real_world':     ['real_world', 'application', 'context', 'case', 'scenario', 'impact'],
    'summary':        ['summary', 'reflect', 'recap', 'consolidat', 'reflection', 'conclusion'],
}


# ---------------------------------------------------------------------------
# Compiler Trace — telemetry collected during one generation job
# ---------------------------------------------------------------------------
@dataclass
class CompilerTrace:
    job_id: int
    knowledge_chunks_retrieved: int = 0
    nodes_generated: int = 0
    nodes_after_repair: int = 0
    media_requests: int = 0
    media_acquired: int = 0
    blocks_created: int = 0
    simulations_attached: int = 0
    quality_gate_passed: bool = False
    quality_warnings: List[str] = field(default_factory=list)
    repair_triggered: bool = False
    complexity_tier: str = 'standard'

    def log(self):
        logger.info(
            "\n[COMPILER TRACE] Job #%d\n"
            "  Complexity tier            : %s\n"
            "  Knowledge chunks retrieved : %d\n"
            "  Nodes generated            : %d\n"
            "  Nodes after repair         : %d\n"
            "  Repair triggered           : %s\n"
            "  Media requests             : %d\n"
            "  Media acquired             : %d\n"
            "  Blocks created             : %d\n"
            "  Simulations attached       : %d\n"
            "  Quality gate               : %s\n"
            "  Quality warnings           : %s",
            self.job_id,
            self.complexity_tier,
            self.knowledge_chunks_retrieved,
            self.nodes_generated,
            self.nodes_after_repair,
            "YES" if self.repair_triggered else "NO",
            self.media_requests,
            self.media_acquired,
            self.blocks_created,
            self.simulations_attached,
            "PASSED" if self.quality_gate_passed else "FAILED",
            self.quality_warnings or "none",
        )

    def to_dict(self) -> dict:
        return {
            'job_id': self.job_id,
            'complexity_tier': self.complexity_tier,
            'knowledge_chunks_retrieved': self.knowledge_chunks_retrieved,
            'nodes_generated': self.nodes_generated,
            'nodes_after_repair': self.nodes_after_repair,
            'repair_triggered': self.repair_triggered,
            'media_requests': self.media_requests,
            'media_acquired': self.media_acquired,
            'blocks_created': self.blocks_created,
            'simulations_attached': self.simulations_attached,
            'quality_gate_passed': self.quality_gate_passed,
            'quality_warnings': self.quality_warnings,
        }


# ---------------------------------------------------------------------------
# Sequential Graph Repair — replaces destructive DFS pruning
# ---------------------------------------------------------------------------

def _repair_sequential_graph(validated_plan: LearningExperiencePlan) -> tuple[LearningExperiencePlan, bool]:
    """
    Ensures all nodes are reachable by wiring them sequentially via execution_order.
    
    Strategy:
    1. Sort all nodes by execution_order (then by list position as tiebreaker).
    2. Rebuild next_nodes for each node to point to the next in sorted sequence.
    3. Set entry_node_id to the first node.
    4. This replaces destructive DFS pruning — NO nodes are ever deleted.
    
    Returns: (repaired_plan, was_repair_needed)
    """
    nodes = validated_plan.nodes
    if not nodes:
        return validated_plan, False

    # Sort by execution_order. If not set, fall back to list index.
    for i, node in enumerate(nodes):
        if node.execution_order is None or node.execution_order < 1:
            node.execution_order = i + 1

    sorted_nodes = sorted(nodes, key=lambda n: n.execution_order)

    # Check whether all next_nodes are already correct (no repair needed for clean plans)
    was_repair_needed = False
    for i, node in enumerate(sorted_nodes):
        expected_next = [sorted_nodes[i + 1].node_id] if i < len(sorted_nodes) - 1 else []
        # Only auto-wire if this is NOT a genuine branch point
        if not node.is_branch_point:
            if node.next_nodes != expected_next:
                was_repair_needed = True
            node.next_nodes = expected_next

    validated_plan.nodes = sorted_nodes
    validated_plan.entry_node_id = sorted_nodes[0].node_id

    return validated_plan, was_repair_needed


# ---------------------------------------------------------------------------
# Instructional Diversity Check
# ---------------------------------------------------------------------------

def _check_diversity(plan: LearningExperiencePlan, complexity: str) -> List[str]:
    """
    Validates instructional diversity across the lesson.
    Returns a list of warnings for missing diversity buckets.
    """
    targets = COMPLEXITY_TARGETS.get(complexity, COMPLEXITY_TARGETS['standard'])
    warnings = []

    # 1. Node count
    if len(plan.nodes) < targets['min_nodes']:
        warnings.append(
            f"Only {len(plan.nodes)} nodes generated; "
            f"complexity='{complexity}' requires minimum {targets['min_nodes']}."
        )

    # 2. Diversity buckets
    covered = set()
    for node in plan.nodes:
        nt = (node.node_type or '').lower()
        for bucket, keywords in REQUIRED_DIVERSITY_BUCKETS.items():
            if any(k in nt for k in keywords):
                covered.add(bucket)

    missing_buckets = set(REQUIRED_DIVERSITY_BUCKETS.keys()) - covered
    # Only require up to min_diversity_types buckets
    if len(missing_buckets) > (len(REQUIRED_DIVERSITY_BUCKETS) - targets['min_diversity_types']):
        for bucket in missing_buckets:
            warnings.append(f"Missing instructional diversity type: '{bucket}'.")

    return warnings


# ---------------------------------------------------------------------------
# Media Coverage Check
# ---------------------------------------------------------------------------

def _check_media_coverage(manifest, acquired_assets: list, trace: CompilerTrace) -> List[str]:
    """
    Validates that media acquisition met expectations.
    Returns warnings for unresolved required media.
    """
    warnings = []
    required = [r for r in manifest.requirements if r.is_required]
    trace.media_requests = len(manifest.requirements)
    trace.media_acquired = len(acquired_assets)

    if required and not acquired_assets:
        warnings.append(
            f"Zero visual assets acquired despite {len(required)} required media requests. "
            "Lesson will ship without images."
        )
    elif len(acquired_assets) < len(required) // 2:
        warnings.append(
            f"Low media coverage: {len(acquired_assets)}/{len(required)} media requirements resolved."
        )

    return warnings


# ---------------------------------------------------------------------------
# Repair Prompt Builder
# ---------------------------------------------------------------------------

def _build_repair_prompt(original_prompt: str, missing_types: List[str]) -> str:
    """Appends a targeted repair instruction to the original prompt."""
    repair_instruction = (
        "\n\n[COMPILER REPAIR REQUEST]\n"
        "Your previous response was incomplete. The lesson is missing the following required instructional types:\n"
        + "\n".join(f"  - {t}" for t in missing_types)
        + "\n\nYou MUST regenerate the complete lesson, ensuring ALL required node types are present. "
        "Do not omit any previously correct nodes. Output the full JSON plan."
    )
    return original_prompt + repair_instruction


# ---------------------------------------------------------------------------
# PedagogicalEngine
# ---------------------------------------------------------------------------

class PedagogicalEngine:
    """
    Agent 3 Orchestrator.
    Consumes Knowledge Repository -> Generates pure pedagogy -> Persists to LearningExperienceGraph.

    Pipeline:
      1. Assemble Knowledge (Agent 2 output)
      2. Framework Selection (Deterministic)
      3. Build Planner Prompt
      4. LLM Generation (Structured)
      5. Sequential Graph Repair (replaces destructive DFS pruning)
      6. Graph Validation (warnings only for orphans)
      7. Diversity Quality Gate (with optional repair pass)
      8. Agent 5: Validation & Optimization
      9. Persist to LearningExperienceGraph
     10. Agent 4: Experience Assembly (Media Orchestration)
     11. Media Coverage Check
     12. Richness Metrics
     13. Emit Compiler Trace
    """

    @staticmethod
    def execute_job(job_id: int) -> None:
        job = GenerationJob.objects.select_related(
            'lesson',
            'lesson__learning_unit',
        ).get(id=job_id)

        trace = CompilerTrace(job_id=job_id)

        try:
            LessonPersistenceService.update_job_status(job.id, 'generating')

            lesson = job.lesson
            learning_unit = lesson.learning_unit

            if not learning_unit:
                raise ValueError(
                    "Lesson has no associated LearningUnit. "
                    "Pedagogical Engine requires a LearningUnit."
                )

            # 1. Assemble Knowledge (Agent 2 output)
            context_package = KnowledgeAssembler.assemble(learning_unit.id)
            knowledge = context_package.get('knowledge', {})
            trace.knowledge_chunks_retrieved = sum(len(v) for v in knowledge.values())

            # 2. Framework Selection (Deterministic)
            selected_framework = FrameworkSelectionEngine.select(learning_unit)
            context_package['framework'] = selected_framework

            # 3. Build Planner Prompt
            prompt = build_planner_prompt(context_package)

            # 4. Call LLM with Structured Generation
            logger.info("[PEDAGOGICAL ENGINE] Job #%d — Calling LLM for plan generation...", job_id)
            validated_plan = LLMClient.generate_structured(prompt, LearningExperiencePlan)
            trace.nodes_generated = len(validated_plan.nodes)
            logger.info("[PEDAGOGICAL ENGINE] Job #%d — LLM returned %d nodes.", job_id, trace.nodes_generated)

            # 5. Sequential Graph Repair (replaces destructive DFS pruning)
            validated_plan, was_repaired = _repair_sequential_graph(validated_plan)
            trace.nodes_after_repair = len(validated_plan.nodes)
            trace.repair_triggered = was_repaired
            if was_repaired:
                logger.info(
                    "[SEQUENTIAL REPAIR] Job #%d — Graph repaired. All %d nodes linked sequentially.",
                    job_id, trace.nodes_after_repair
                )

            # Determine complexity tier from cognitive analysis
            complexity = getattr(validated_plan.cognitive_analysis, 'complexity', 'standard') or 'standard'
            if complexity not in COMPLEXITY_TARGETS:
                complexity = 'standard'
            trace.complexity_tier = complexity

            # 6. Graph Validation (warnings only — no content deletion)
            plan_dict = validated_plan.model_dump()
            graph_warnings = GraphValidator.validate(plan_dict)
            for w in graph_warnings:
                logger.warning("[GRAPH VALIDATOR] Job #%d: %s", job_id, w)

            # 7. Diversity Quality Gate
            diversity_warnings = _check_diversity(validated_plan, complexity)
            targets = COMPLEXITY_TARGETS.get(complexity, COMPLEXITY_TARGETS['standard'])

            if diversity_warnings and len(validated_plan.nodes) < targets['min_nodes']:
                # Attempt a single repair pass
                missing_types = [
                    bucket for bucket in REQUIRED_DIVERSITY_BUCKETS
                    if not any(
                        any(k in (n.node_type or '').lower() for k in REQUIRED_DIVERSITY_BUCKETS[bucket])
                        for n in validated_plan.nodes
                    )
                ]
                logger.warning(
                    "[QUALITY GATE] Job #%d — Insufficient lesson depth (%d nodes, complexity=%s). "
                    "Missing: %s. Triggering repair pass.",
                    job_id, len(validated_plan.nodes), complexity, missing_types
                )
                repair_prompt = _build_repair_prompt(prompt, missing_types)
                try:
                    repaired_plan = LLMClient.generate_structured(repair_prompt, LearningExperiencePlan)
                    repaired_plan, _ = _repair_sequential_graph(repaired_plan)
                    repaired_diversity = _check_diversity(repaired_plan, complexity)
                    if len(repaired_diversity) < len(diversity_warnings):
                        logger.info("[QUALITY GATE] Repair improved lesson from %d to %d nodes.", len(validated_plan.nodes), len(repaired_plan.nodes))
                        validated_plan = repaired_plan
                        trace.nodes_after_repair = len(validated_plan.nodes)
                        diversity_warnings = repaired_diversity
                    else:
                        logger.warning("[QUALITY GATE] Repair did not improve lesson. Proceeding with original.")
                except Exception as repair_exc:
                    logger.warning("[QUALITY GATE] Repair pass failed: %s. Proceeding with original.", repair_exc)

            trace.quality_warnings = diversity_warnings
            trace.quality_gate_passed = len(diversity_warnings) == 0

            plan_dict = validated_plan.model_dump()

            # 8. Agent 5: Validation & Optimization Engine

            # 8.1 Pre-Optimization Deterministic Validation
            validation_report = CompilerValidator.validate_plan(validated_plan)
            if validation_report.has_errors:
                error_msgs = [c.detail for c in validation_report.checks if c.severity == 'error']
                raise ValueError(f"Pedagogical validation failed:\n" + "\n".join(error_msgs))

            # 8.2 Optional LLM Optimization Pass
            optimized_plan, recommendations = OptimizerEngine.optimize(validated_plan)

            # 8.3 Post-Optimization re-repair (ensure structure is still intact after optimizer)
            optimized_plan, _ = _repair_sequential_graph(optimized_plan)

            # 8.4 Quality Scoring
            quality_score = QualityEngine.calculate_score(optimized_plan)
            quality_score.recommendations = recommendations

            engine_report = EngineReport(
                validation=validation_report,
                quality=quality_score,
                optimized=True
            )

            # 9. Persist to LearningExperienceGraph
            provenance = {
                'knowledge_chunk_ids': context_package.get('provenance_chunk_ids', []),
                'compiler_trace': trace.to_dict(),  # Store trace in provenance
            }

            graph_instance = LearningExperienceGraph.objects.create(
                learning_unit=learning_unit,
                generation_job=job,
                status='published',
                graph_data=optimized_plan.model_dump(),
                quality_report=engine_report.model_dump(),
                provenance=provenance
            )

            # 10. Agent 4: Experience Assembly Service (Media Orchestration)
            assembler = ExperienceAssemblyService()
            experience_package = assembler.compile_experience(lesson, optimized_plan)

            # 11. Media Coverage Check & Telemetry
            # Count blocks and simulations from assembled lesson
            from curriculum.models import LessonBlock, LessonAsset
            blocks_qs = LessonBlock.objects.filter(lesson=lesson)
            trace.blocks_created = blocks_qs.count()
            trace.simulations_attached = blocks_qs.filter(block_type='suggested_simulation').count()
            acquired_assets = experience_package.resolved_assets if experience_package else []
            trace.media_acquired = len(acquired_assets)

            # Estimate media requests from block count (each node may have had one requirement)
            # Use the optimized_plan node count as proxy since assembler consumed it
            trace.media_requests = len(optimized_plan.nodes)

            if not acquired_assets and trace.media_requests > 0:
                logger.warning(
                    "[MEDIA COVERAGE] Job #%d: Zero visual assets acquired despite %d nodes. "
                    "Lesson may ship without images.",
                    job_id, trace.media_requests
                )

            # 12. Agent 5: Post-Orchestration Media Validation
            media_report = MediaValidator.validate_media(lesson)

            # Merge checks into quality report
            final_report = engine_report.model_dump()
            final_report['validation']['checks'].extend([c.model_dump() for c in media_report.checks])

            # 13. Lesson Richness Metrics
            try:
                richness_report = RichnessEngine.calculate(lesson)
                final_report['richness'] = richness_report.to_dict()
                logger.info(
                    "[RICHNESS] Job #%d | moments=%d blocks=%d words=%d images=%d sims=%d "
                    "knowledge_checks=%d worked_examples=%d est_time=%.1fmin visual_ratio=%.2f score=%.2f",
                    job_id,
                    richness_report.learning_moments,
                    richness_report.blocks,
                    richness_report.total_words,
                    richness_report.images,
                    richness_report.simulations,
                    richness_report.knowledge_checks,
                    richness_report.worked_examples,
                    richness_report.estimated_reading_time_minutes,
                    richness_report.visual_to_text_ratio,
                    richness_report.richness_score,
                )
            except Exception as richness_exc:
                logger.warning("[RICHNESS] Job #%d — Richness calculation failed: %s", job_id, richness_exc)

            graph_instance.quality_report = final_report
            graph_instance.provenance = {
                **provenance,
                'compiler_trace': trace.to_dict(),
            }
            graph_instance.save(update_fields=['quality_report', 'provenance'])

            # Update lesson title if empty
            if not lesson.title:
                lesson.title = plan_dict.get('title', learning_unit.name)
                lesson.save(update_fields=['title'])

            # Emit compiler trace to logs
            trace.log()

            # Mark job completed
            LessonPersistenceService.update_job_status(job.id, 'completed')

        except Exception as exc:
            LessonPersistenceService.update_job_status(job.id, 'failed', str(exc))
            logger.error("[PEDAGOGICAL ENGINE] Job #%d FAILED: %s", job_id, exc, exc_info=True)
            raise
