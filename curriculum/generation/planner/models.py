from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Core Pedagogical Schema (No Media/UI Allowed)
# ---------------------------------------------------------------------------

class InstructionalIntent(BaseModel):
    concept_group: str = Field(
        ...,
        description="The overarching concept this node belongs to. Nodes sharing the same concept_group belong to the same instructional topic cluster."
    )
    layout_template: Optional[str] = Field(
        "DiscoveryLayout",
        description="Frontend layout template for rendering this concept page (e.g. 'DiscoveryLayout', 'ComparativeLayout', 'ProcessLayout', 'ProceduralLayout', 'NarrativeTimelineLayout', 'SpatialStructuralLayout')."
    )
    learning_moment: str = Field(
        ...,
        description="The specific cognitive phase (e.g. 'Phenomenon Observation', 'Intuition Building', 'Terminology Formalization', 'Misconception Disruption', 'Diagnostic Application')."
    )
    student_goal: str = Field(
        ...,
        description="What the student is striving to accomplish or understand in this node."
    )
    required_cognitive_change: str = Field(
        ...,
        description="The single mental shift or realization that must occur for the student (One Cognitive Shift Per Moment rule)."
    )
    evidence_of_understanding: str = Field(
        ...,
        description="Observable student behavior or reasoning demonstrating successful completion of the cognitive shift."
    )
    recommended_learning_support: str = Field(
        ...,
        description="Pedagogical media requirement. Must state: 1) Educational purpose (why visual exists), 2) Invisible mechanism revealed, 3) What learner must notice, 4) Targeted misconception."
    )
    learning_constraints: Optional[str] = Field(
        None,
        description="Any specific constraints, potential false analogies, or oversimplifications to avoid."
    )

class PersonalizationOpportunities(BaseModel):
    extension_available: bool = Field(False, description="Is there an opportunity for advanced learners to go deeper here?")
    remediation_available: bool = Field(False, description="Is there a common misconception here that might require remediation?")
    adaptive_questioning: bool = Field(False, description="Can we ask dynamic questions here to test understanding before proceeding?")

class StrategyNode(BaseModel):
    node_id: str = Field(
        ...,
        description="Unique identifier for this node (e.g., 'hook_1', 'observe_osmosis')."
    )
    node_type: str = Field(
        ...,
        description="The pedagogical type of this node (e.g., 'predict', 'observe', 'explain', 'practice', 'assessment', 'remediation', 'hook', 'real_world', 'worked_example', 'misconception', 'reflection', 'summary')."
    )
    execution_order: int = Field(
        ...,
        description="Sequential position of this node in the lesson (1 = first node). Nodes are executed in ascending order. This is the PRIMARY traversal mechanism."
    )
    instructional_intent: InstructionalIntent
    personalization: PersonalizationOpportunities
    content: str = Field(
        ...,
        description="The final, polished text read directly by the student. MUST be CONCISE: 2-4 sentences maximum. Follow Intuition Before Terminology (phenomenon -> mental model -> formal terms). Direct, engaging tone using relatable Kenyan context and analogies (stating boundaries). NO meta-commentary, titles, or 'Step X' prefixes. NO walls of text."
    )

    # ---------------------------------------------------------------------------
    # DEPRECATED: next_nodes — kept for backward compatibility and explicit branching.
    # The compiler now uses execution_order for primary sequential traversal.
    # Only populate next_nodes when this node is a genuine adaptive branch point
    # (e.g., a remediation fork or extension activity).
    # ---------------------------------------------------------------------------
    next_nodes: Optional[List[str]] = Field(
        default_factory=list,
        description="[DEPRECATED — use execution_order for normal flow] Optional list of node_ids for explicit adaptive branching (remediation, extension). Leave empty for standard sequential lessons."
    )
    is_branch_point: bool = Field(
        default=False,
        description="Set to True only if this node genuinely forks into multiple adaptive paths (e.g., success -> extension, failure -> remediation)."
    )
    success_criteria: Optional[str] = Field(
        None,
        description="If this node involves assessment/practice, diagnostic criteria testing reasoning or application (NOT definition recall) dictating the next node."
    )
    failure_criteria: Optional[str] = Field(
        None,
        description="If this node involves assessment/practice, diagnostic criteria detecting specific misconceptions dictating a remediation branch."
    )

class CognitiveAnalysis(BaseModel):
    difficulty: str = Field(..., description="The estimated difficulty level (e.g., 'Low', 'Medium', 'High', 'Advanced').")
    complexity: str = Field(default="standard", description="Topic complexity tier: 'simple', 'standard', or 'complex'. Used to set adaptive lesson depth targets.")
    prior_knowledge_needed: List[str] = Field(..., description="List of concepts the student must know before this lesson.")
    abstractness: str = Field(..., description="How abstract this concept is, and strategies to make it concrete.")

class LearningExperiencePlan(BaseModel):
    title: str = Field(..., description="The title of this learning experience.")
    cognitive_analysis: CognitiveAnalysis = Field(
        ...,
        description="Analysis of difficulty, complexity tier, prior knowledge needed, abstractness, etc."
    )
    strategy_selected: str = Field(
        ...,
        description="The overarching pedagogical strategy (e.g., 'Predict-Observe-Explain', 'Story-Based Learning', 'Misconception-Driven Teaching')."
    )
    nodes: List[StrategyNode] = Field(
        ...,
        description="The complete ordered sequence of instructional nodes. Nodes MUST be sorted by execution_order. The lesson is traversed sequentially unless is_branch_point=True on a node."
    )
    entry_node_id: str = Field(
        ...,
        description="The node_id of the first node (execution_order=1) to start the learning experience."
    )
