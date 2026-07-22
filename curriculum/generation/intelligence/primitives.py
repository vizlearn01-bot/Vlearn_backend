from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class InstructionalPrimitive(BaseModel):
    """
    An Instructional Primitive represents a reusable cognitive action or pedagogical step.
    It is completely decoupled from media or frontend presentation components.
    """
    id: str = Field(..., description="Unique identifier for the primitive (e.g., 'predict', 'observe').")
    name: str = Field(..., description="Human-readable name.")
    educational_purpose: str = Field(..., description="Why this primitive is used in a learning experience.")
    cognitive_objective: str = Field(..., description="The cognitive goal for the student.")
    entry_conditions: List[str] = Field(default_factory=list, description="What the student must know/do before this step.")
    exit_conditions: List[str] = Field(default_factory=list, description="What the student has achieved by completing this step.")
    suitable_assessment_styles: List[str] = Field(default_factory=list, description="Recommended ways to assess this primitive.")
    preferred_learning_supports: List[str] = Field(default_factory=list, description="Recommended scaffolds or interactions (e.g., 'hints', 'worked examples').")
    misconceptions_addressed: bool = Field(default=False, description="Does this primitive typically address misconceptions directly?")
    recommended_interaction_patterns: List[str] = Field(default_factory=list, description="How the student interacts (e.g., 'active recall', 'synthesis').")

# ---------------------------------------------------------------------------
# Standard Primitive Library
# ---------------------------------------------------------------------------

PRIMITIVES: Dict[str, InstructionalPrimitive] = {
    "predict": InstructionalPrimitive(
        id="predict",
        name="Predict",
        educational_purpose="Activate prior knowledge and create a knowledge gap.",
        cognitive_objective="Formulate a hypothesis based on existing understanding.",
        entry_conditions=["Basic familiarity with variables involved."],
        exit_conditions=["Student has committed to a specific outcome."],
        suitable_assessment_styles=["multiple_choice", "short_answer", "predict_outcome"],
        preferred_learning_supports=["scenario descriptions", "contrasting cases"],
        misconceptions_addressed=True,
        recommended_interaction_patterns=["commit_first", "active_recall"]
    ),
    "observe": InstructionalPrimitive(
        id="observe",
        name="Observe",
        educational_purpose="Provide empirical data or a phenomenon to analyze.",
        cognitive_objective="Identify key features, patterns, or anomalies.",
        entry_conditions=["A prediction or context has been established."],
        exit_conditions=["Student has gathered data or noted specific behaviors."],
        suitable_assessment_styles=["fill_blank", "short_answer"],
        preferred_learning_supports=["visualizations", "simulations", "guided focus"],
        recommended_interaction_patterns=["guided_attention", "data_collection"]
    ),
    "explain": InstructionalPrimitive(
        id="explain",
        name="Explain",
        educational_purpose="Synthesize observations into a coherent mental model.",
        cognitive_objective="Articulate the underlying mechanism or 'why' behind a phenomenon.",
        entry_conditions=["Observations or data have been collected."],
        exit_conditions=["Student can articulate the causal relationship."],
        suitable_assessment_styles=["explain_in_words", "concept_mapping"],
        preferred_learning_supports=["analogies", "step-by-step breakdown"],
        misconceptions_addressed=True,
        recommended_interaction_patterns=["sense_making", "synthesis"]
    ),
    "compare": InstructionalPrimitive(
        id="compare",
        name="Compare",
        educational_purpose="Highlight similarities and differences to build nuanced understanding.",
        cognitive_objective="Discriminate between related concepts or cases.",
        entry_conditions=["Familiarity with at least two concepts."],
        exit_conditions=["Student understands boundaries and overlaps between concepts."],
        suitable_assessment_styles=["true_false", "matching", "multiple_choice"],
        preferred_learning_supports=["venn_diagrams", "side-by-side tables"],
        recommended_interaction_patterns=["pattern_recognition", "discrimination"]
    ),
    "investigate": InstructionalPrimitive(
        id="investigate",
        name="Investigate",
        educational_purpose="Drive inquiry-based learning and active discovery.",
        cognitive_objective="Systematically explore a topic to uncover relationships.",
        entry_conditions=["A guiding question or problem."],
        exit_conditions=["Student has drawn evidence-based conclusions."],
        suitable_assessment_styles=["short_answer", "explain_in_words"],
        preferred_learning_supports=["inquiry scaffolding", "guiding questions"],
        recommended_interaction_patterns=["exploration", "inquiry"]
    ),
    "construct": InstructionalPrimitive(
        id="construct",
        name="Construct",
        educational_purpose="Build a tangible or conceptual representation.",
        cognitive_objective="Assemble parts into a coherent whole.",
        entry_conditions=["Understanding of individual components."],
        exit_conditions=["A completed model, argument, or structure."],
        suitable_assessment_styles=["rubric_based", "peer_review"],
        preferred_learning_supports=["templates", "building blocks"],
        recommended_interaction_patterns=["creation", "synthesis"]
    ),
    "model": InstructionalPrimitive(
        id="model",
        name="Model",
        educational_purpose="Represent a complex system simplified for understanding.",
        cognitive_objective="Abstract real-world phenomena into manageable rules or equations.",
        entry_conditions=["Understanding of the core variables."],
        exit_conditions=["Student can manipulate the model to predict behavior."],
        suitable_assessment_styles=["calculate", "predict_outcome"],
        preferred_learning_supports=["interactive_simulations", "formula breakdowns"],
        recommended_interaction_patterns=["manipulation", "abstraction"]
    ),
    "debate": InstructionalPrimitive(
        id="debate",
        name="Debate",
        educational_purpose="Explore multiple perspectives or ambiguous outcomes.",
        cognitive_objective="Evaluate arguments and counter-arguments.",
        entry_conditions=["Familiarity with opposing viewpoints."],
        exit_conditions=["Student has defended a position with evidence."],
        suitable_assessment_styles=["short_answer", "explain_in_words"],
        preferred_learning_supports=["structured arguments", "evidence banks"],
        misconceptions_addressed=True,
        recommended_interaction_patterns=["evaluation", "argumentation"]
    ),
    "reflect": InstructionalPrimitive(
        id="reflect",
        name="Reflect",
        educational_purpose="Consolidate learning and promote metacognition.",
        cognitive_objective="Assess one's own understanding or learning process.",
        entry_conditions=["Completion of a learning sequence."],
        exit_conditions=["Student has identified what they learned and what remains confusing."],
        suitable_assessment_styles=["open_ended", "self_assessment"],
        preferred_learning_supports=["prompts", "learning journals"],
        recommended_interaction_patterns=["metacognition", "internalization"]
    ),
    "experiment": InstructionalPrimitive(
        id="experiment",
        name="Experiment",
        educational_purpose="Test a hypothesis through controlled actions.",
        cognitive_objective="Determine causal relationships by isolating variables.",
        entry_conditions=["A clear hypothesis."],
        exit_conditions=["Data proving or disproving the hypothesis."],
        suitable_assessment_styles=["data_analysis", "conclusion_drawing"],
        preferred_learning_supports=["simulations", "step-by-step procedures"],
        recommended_interaction_patterns=["variable_control", "causal_reasoning"]
    ),
    "practice": InstructionalPrimitive(
        id="practice",
        name="Practice",
        educational_purpose="Build fluency and automaticity in a skill or concept.",
        cognitive_objective="Apply a known procedure or concept repeatedly.",
        entry_conditions=["Understanding of the core procedure/concept."],
        exit_conditions=["Increased speed and accuracy."],
        suitable_assessment_styles=["multiple_choice", "fill_blank", "calculate"],
        preferred_learning_supports=["hints", "worked_examples", "immediate feedback"],
        recommended_interaction_patterns=["repetition", "fluency_building"]
    ),
    "assess": InstructionalPrimitive(
        id="assess",
        name="Assess",
        educational_purpose="Measure mastery of a concept.",
        cognitive_objective="Demonstrate comprehension without heavy scaffolding.",
        entry_conditions=["Sufficient practice and instruction."],
        exit_conditions=["A mastery score or clear indicator of understanding."],
        suitable_assessment_styles=["comprehensive_test", "summative"],
        preferred_learning_supports=["minimal"],
        recommended_interaction_patterns=["retrieval_practice", "demonstration"]
    ),
    "summarize": InstructionalPrimitive(
        id="summarize",
        name="Summarize",
        educational_purpose="Distill complex information into core takeaways.",
        cognitive_objective="Identify the most critical points and discard noise.",
        entry_conditions=["Exposure to the full content."],
        exit_conditions=["A concise representation of the topic."],
        suitable_assessment_styles=["explain_in_words", "matching"],
        preferred_learning_supports=["graphic organizers", "bullet points"],
        recommended_interaction_patterns=["distillation", "compression"]
    ),
    "apply": InstructionalPrimitive(
        id="apply",
        name="Apply",
        educational_purpose="Transfer knowledge to a novel context.",
        cognitive_objective="Use learned concepts to solve new, unseen problems.",
        entry_conditions=["Mastery of the concept in a familiar context."],
        exit_conditions=["Successful resolution of the novel problem."],
        suitable_assessment_styles=["case_study", "problem_solving"],
        preferred_learning_supports=["real_world_scenarios", "analogies"],
        recommended_interaction_patterns=["transfer", "problem_solving"]
    ),
    "evaluate": InstructionalPrimitive(
        id="evaluate",
        name="Evaluate",
        educational_purpose="Judge the value, validity, or quality of an idea/process.",
        cognitive_objective="Make informed judgments based on criteria.",
        entry_conditions=["Deep understanding of the subject and criteria."],
        exit_conditions=["A justified critique or decision."],
        suitable_assessment_styles=["explain_in_words", "critique"],
        preferred_learning_supports=["rubrics", "criteria lists"],
        recommended_interaction_patterns=["judgment", "critical_thinking"]
    )
}

def get_primitive(primitive_id: str) -> Optional[InstructionalPrimitive]:
    return PRIMITIVES.get(primitive_id)
