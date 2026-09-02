import re
from curriculum.generation.planner.models import LearningExperiencePlan
from .models import QualityScore

DEFINITION_PATTERN = re.compile(
    r'^(?:[A-Z][a-z]+\s+is\s+defined\s+as|[A-Z][a-z]+\s+refers\s+to|In\s+simple\s+terms,\s+[a-z]+\s+is|Definition:)',
    re.IGNORECASE
)

class QualityEngine:
    """
    Agent 5: Educational Quality Engine.
    Calculates a deterministic quality score based on graph properties and Teaching Playbook principles.
    """
    
    @staticmethod
    def calculate_score(plan: LearningExperiencePlan) -> QualityScore:
        nodes = plan.nodes
        total_nodes = len(nodes)
        
        if total_nodes == 0:
            return QualityScore(score=0, metrics={})
            
        metrics = {}
        score = 100
        
        # 1. Interaction Density (Assessment/Practice nodes vs Content nodes)
        active_nodes = sum(1 for n in nodes if n.node_type in ('assessment', 'practice', 'predict', 'observe', 'investigate'))
        interaction_ratio = active_nodes / total_nodes
        metrics['interaction_ratio'] = round(interaction_ratio, 2)
        
        if interaction_ratio < 0.2:
            score -= 15
            metrics['interaction_penalty'] = "-15 (Too much passive reading, insufficient active interaction)"
        elif interaction_ratio > 0.6:
            score -= 10
            metrics['interaction_penalty'] = "-10 (Too many assessments, needs more instruction)"
            
        # 2. Remediation Coverage
        remediation_nodes = sum(1 for n in nodes if n.node_type == 'remediation' or n.personalization.remediation_available)
        if remediation_nodes == 0:
            score -= 10
            metrics['remediation_penalty'] = "-10 (No remediation logic defined)"
            
        # 3. Pacing and Chunking (Length of content)
        heavy_nodes = sum(1 for n in nodes if len(n.content.split()) > 450)
        if heavy_nodes > 0:
            penalty = heavy_nodes * 5
            score -= penalty
            metrics['pacing_penalty'] = f"-{penalty} ({heavy_nodes} nodes are too text-heavy (>450 words))"
            
        # 4. Success/Failure criteria defined on branching nodes
        branching_nodes = [n for n in nodes if len(n.next_nodes) > 1]
        missing_criteria = sum(1 for n in branching_nodes if not n.success_criteria and not n.failure_criteria)
        if missing_criteria > 0:
            penalty = missing_criteria * 5
            score -= penalty
            metrics['criteria_penalty'] = f"-{penalty} (Branching nodes missing clear criteria)"

        # 5. Intuition Before Terminology (Check for raw definition starts)
        definition_heavy_nodes = sum(1 for n in nodes if DEFINITION_PATTERN.search(n.content.strip()))
        if definition_heavy_nodes > 0:
            penalty = definition_heavy_nodes * 5
            score -= penalty
            metrics['intuition_penalty'] = f"-{penalty} ({definition_heavy_nodes} nodes start with formal definitions before intuition)"

        # 6. Cognitive Pacing (Max 2 consecutive explanation nodes)
        consecutive_explain = 0
        max_consecutive = 0
        for n in nodes:
            if n.node_type in ('explain', 'summarize'):
                consecutive_explain += 1
                max_consecutive = max(max_consecutive, consecutive_explain)
            else:
                consecutive_explain = 0

        if max_consecutive > 2:
            penalty = (max_consecutive - 2) * 5
            score -= penalty
            metrics['consecutive_explanation_penalty'] = f"-{penalty} ({max_consecutive} consecutive explanation nodes without active primitive)"

        # 7. Guided Visual Thinking (Check for superficial media supports)
        weak_visual_supports = sum(
            1 for n in nodes 
            if n.instructional_intent.recommended_learning_support 
            and len(n.instructional_intent.recommended_learning_support.split()) < 8
        )
        if weak_visual_supports > 0:
            penalty = weak_visual_supports * 3
            score -= penalty
            metrics['visual_intent_penalty'] = f"-{penalty} ({weak_visual_supports} nodes have superficial visual guidance)"
            
        score = max(0, score)
        
        return QualityScore(
            score=score,
            metrics=metrics,
            recommendations=[] # Populated by optional LLM pass if executed
        )
