from curriculum.generation.planner.models import LearningExperiencePlan
from curriculum.generation.planner.graph_validator import GraphValidator
from .models import ValidationReport

# Instructional diversity buckets — each lesson needs at least one node per bucket
REQUIRED_DIVERSITY_BUCKETS = {
    'explanation':    ['explain', 'concept', 'core', 'present', 'teach'],
    'visualization':  ['visual', 'diagram', 'observe', 'illustrat'],
    'worked_example': ['worked', 'example', 'demonstrat', 'worked_example'],
    'assessment':     ['assess', 'quiz', 'check', 'predict', 'practice', 'knowledge_check'],
    'real_world':     ['real_world', 'application', 'context', 'case_study', 'real'],
    'summary':        ['summary', 'reflect', 'recap', 'consolidat', 'reflection'],
}

# Media requirement check: at least one node should have a non-empty recommended_learning_support
MEDIA_REQUIREMENT_FIELD = 'recommended_learning_support'


class CompilerValidator:
    """
    Agent 5: Validation Engine.
    Executes structural, pedagogical, instructional diversity, and media coverage checks.
    
    Hard errors (pipeline-blocking):
      - Structural graph errors (invalid entry node, bad edges)
      - Empty plan (no nodes)
      - Missing instructional_intent fields
    
    Warnings (logged, non-blocking):
      - Missing instructional diversity types
      - No media requirements specified
      - No assessment nodes
      - No remediation paths
    """

    @staticmethod
    def validate_plan(plan: LearningExperiencePlan) -> ValidationReport:
        report = ValidationReport()

        # 1. Structural Validation
        plan_dict = plan.model_dump()
        graph_issues = GraphValidator.validate(plan_dict)

        hard_errors = [e for e in graph_issues if not e.startswith("WARNING:")]
        warnings = [e for e in graph_issues if e.startswith("WARNING:")]

        if hard_errors:
            for err in hard_errors:
                report.add_error("Structural Error", err)
            # Fatal — stop here
            return report
        else:
            report.add_ok("Structural Integrity", "Graph topology is valid.")

        for w in warnings:
            report.add_warning("Graph Warning", w)

        # 2. Basic content check
        nodes = plan.nodes
        if not nodes:
            report.add_error("Empty Plan", "No strategy nodes found in the plan.")
            return report

        # 3. Pedagogical Field Validation
        for node in nodes:
            intent = node.instructional_intent
            if not intent.learning_moment or not intent.student_goal:
                report.add_error(
                    "Missing Instructional Intent",
                    f"Node '{node.node_id}' is missing a core learning moment or goal."
                )
            if not intent.required_cognitive_change:
                report.add_warning(
                    "Missing Cognitive Change",
                    f"Node '{node.node_id}' lacks a defined cognitive shift."
                )

        # 4. Instructional Diversity Validation
        covered_buckets = set()
        has_assessments = False
        has_remediation = False
        has_reflection = False
        has_media_requirement = False

        for node in nodes:
            nt = (node.node_type or '').lower()
            for bucket, keywords in REQUIRED_DIVERSITY_BUCKETS.items():
                if any(k in nt for k in keywords):
                    covered_buckets.add(bucket)

            if node.node_type in ('assessment', 'predict', 'practice', 'knowledge_check'):
                has_assessments = True
            if node.node_type == 'remediation' or node.personalization.remediation_available:
                has_remediation = True
            if node.node_type in ('reflection', 'summary'):
                has_reflection = True

            # Check if any node has a media requirement specified
            media_req = node.instructional_intent.recommended_learning_support or ''
            if media_req and len(media_req) > 10:
                has_media_requirement = True

        missing_buckets = set(REQUIRED_DIVERSITY_BUCKETS.keys()) - covered_buckets
        for bucket in missing_buckets:
            report.add_warning(
                "Missing Instructional Diversity",
                f"No '{bucket}' node found. Lesson lacks this instructional type."
            )

        if covered_buckets:
            report.add_ok(
                "Instructional Diversity",
                f"Covered {len(covered_buckets)}/{len(REQUIRED_DIVERSITY_BUCKETS)} diversity buckets: {', '.join(sorted(covered_buckets))}."
            )

        # 5. Assessment Coverage
        if has_assessments:
            report.add_ok("Assessment Coverage", "Plan includes assessment or practice nodes.")
        else:
            report.add_warning("Assessment Coverage", "No assessments or practice opportunities found.")

        # 6. Remediation Paths
        if has_remediation:
            report.add_ok("Remediation Paths", "Plan includes remediation logic.")
        else:
            report.add_warning("Remediation Paths", "No explicit remediation nodes or flags found.")

        # 7. Media Requirements
        if has_media_requirement:
            report.add_ok("Media Requirements", "At least one node specifies a media/visual requirement.")
        else:
            report.add_warning("Media Requirements", "No nodes specify visual or media requirements. Lesson may ship without images.")

        report.add_ok("Pedagogical Validation", "Core instructional intent validated.")

        return report
