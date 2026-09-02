from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Core Pedagogical Schema (No Media/UI Allowed)
# ---------------------------------------------------------------------------

class InstructionalIntent(BaseModel):
    concept_group: str = Field(
        ...,
        description="The overarching concept/card title this node belongs to (e.g. 'The Mystery of Expanding Gases', 'Molecular Collisions & Kinetic Pressure', 'Mathematical Formulation & Formula Breakdown', 'Real-World Applications in Aviation', 'Common Pitfalls & Clarifications', 'Core Insights & Synthesis'). Nodes sharing the same concept_group belong to the same instructional card. NEVER use generic drafting labels like '1. Introduction & Hook', 'Core Concept', 'Phase 1'."
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
    required_cognitive_change: Optional[str] = Field(
        None,
        description="The single mental shift or realization that must occur for the student (One Cognitive Shift Per Moment rule)."
    )
    evidence_of_understanding: Optional[str] = Field(
        None,
        description="Observable student behavior or reasoning demonstrating successful completion of the cognitive shift."
    )
    recommended_learning_support: Optional[str] = Field(
        None,
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
        description="Unique identifier for this node (e.g., 'balloon_pressure_hook', 'gas_particles_motion')."
    )
    title: Optional[str] = Field(
        None,
        description="Engaging, natural student-facing title for this card/step (e.g. 'The Mystery of the Expanding Balloon', 'How Fast Do Molecules Move?', 'Applying the Pressure Formula'). NEVER use drafting labels like 'Introduction', 'Hook', 'Worked Example', 'Misconception', 'Predict', 'Summary', 'Step 1'."
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
        description="The final, polished text read directly by the student. Write comprehensive, high-quality, deeply instructive content (1-3 rich paragraphs for core concepts, worked examples, and explanations; engaging and clear for hooks and questions). Use bold formatting for key scientific terms and bullet points for step-by-step procedures where appropriate. An intro card should be focused and motivating (60-120 words), while core principles, mechanisms, and worked examples must be detailed, thorough, and step-by-step (180-350+ words). NO meta-commentary, drafting jargon, or 'Step X' prefixes."
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
