from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class DeliveryFramework(BaseModel):
    """
    A Delivery Framework is a reusable instructional pattern used to guide the pedagogical engine.
    It defines which primitives are compatible with a specific type of concept.
    """
    id: str = Field(..., description="Unique identifier for the framework.")
    name: str = Field(..., description="Human-readable name.")
    archetype_category: str = Field(default="Conceptual", description="Associated Learning Archetype (e.g. Process, Structural, Procedural, Comparative).")
    recommended_layout_template: str = Field(default="DiscoveryLayout", description="Recommended frontend page layout template.")
    cognitive_characteristics: List[str] = Field(default_factory=list, description="The types of thinking this framework supports.")
    selection_criteria: List[str] = Field(default_factory=list, description="Conditions under which this framework should be selected.")
    compatible_primitives: List[str] = Field(default_factory=list, description="IDs of instructional primitives that fit well in this framework.")
    common_misconceptions: str = Field(..., description="Guidance on how to handle misconceptions in this framework.")
    assessment_recommendations: str = Field(..., description="Guidance on how to assess mastery within this framework.")
    personalization_opportunities: str = Field(..., description="Ways the engine can branch or adapt for different learners.")

# ---------------------------------------------------------------------------
# Standard Framework Library
# ---------------------------------------------------------------------------

FRAMEWORKS: Dict[str, DeliveryFramework] = {
    "process_based": DeliveryFramework(
        id="process_based",
        name="Process-Based Learning",
        archetype_category="Process Learning",
        recommended_layout_template="ProcessLayout",
        cognitive_characteristics=["cause and effect", "sequential reasoning", "system thinking"],
        selection_criteria=["concept involves natural phenomena", "concept is a scientific mechanism", "experimentation_suitability is high"],
        compatible_primitives=["predict", "observe", "investigate", "experiment", "explain", "summarize"],
        common_misconceptions="Confront teleological thinking (assuming intention/purpose in physical processes). Reveal the invisible microscopic/particle mechanism driving the process.",
        assessment_recommendations="Use Diagnostic System Disruption: Ask student to predict and explain outcomes when a core stage or component of the process is altered or removed.",
        personalization_opportunities="If prediction fails, route to an interactive visual step revealing the hidden mechanism before re-testing."
    ),
    "abstract_logical": DeliveryFramework(
        id="abstract_logical",
        name="Abstract & Logical Learning",
        archetype_category="Procedural Learning",
        recommended_layout_template="ProceduralLayout",
        cognitive_characteristics=["deductive reasoning", "symbol manipulation", "abstraction"],
        selection_criteria=["concept relies on mathematical reasoning", "abstraction_level is high"],
        compatible_primitives=["model", "compare", "practice", "apply", "assess"],
        common_misconceptions="Address literal symbol manipulation without intuitive grounding. Establish intuitive physical/visual model BEFORE introducing formal mathematical notation.",
        assessment_recommendations="Assess transfer: Present novel, unseen problem scenarios rather than memorized formula execution.",
        personalization_opportunities="Provide concrete physical analogies (explicitly identifying breakdown boundaries) as scaffolding."
    ),
    "human_social": DeliveryFramework(
        id="human_social",
        name="Human & Social Learning",
        archetype_category="Historical & Narrative Learning",
        recommended_layout_template="NarrativeTimelineLayout",
        cognitive_characteristics=["empathy", "perspective taking", "ethical reasoning"],
        selection_criteria=["concept involves human behavior, history, or society", "discussion_suitability is high"],
        compatible_primitives=["debate", "compare", "evaluate", "reflect", "summarize"],
        common_misconceptions="Address presentism (judging historical actors by modern standards) and oversimplifying motives. Sequence: Narrative context → Diverse perspectives → Critical evaluation.",
        assessment_recommendations="Assess through decision-making dilemmas, perspective defense, and cause-and-effect historical reasoning.",
        personalization_opportunities="Branch based on local community relevance or contrasting historical viewpoints."
    ),
    "language_communication": DeliveryFramework(
        id="language_communication",
        name="Language & Communication Learning",
        archetype_category="Conceptual Learning",
        recommended_layout_template="DiscoveryLayout",
        cognitive_characteristics=["pattern recognition", "fluency", "semantic understanding"],
        selection_criteria=["concept is highly language dependent", "concept involves syntax or grammar"],
        compatible_primitives=["observe", "practice", "construct", "apply", "reflect"],
        common_misconceptions="Address direct-translation errors and rigid rule memorization without communicative context. Build intuitive usage before formal syntax rules.",
        assessment_recommendations="Assess communicative production and comprehension in authentic context rather than isolated grammar definitions.",
        personalization_opportunities="Adjust vocabulary difficulty and provide contextual usage scaffolding."
    ),
    "procedural_algorithmic": DeliveryFramework(
        id="procedural_algorithmic",
        name="Procedural & Algorithmic Learning",
        archetype_category="Procedural Learning",
        recommended_layout_template="ProceduralLayout",
        cognitive_characteristics=["step-by-step execution", "efficiency", "rule following"],
        selection_criteria=["concept has a high procedural_nature", "concept is a skill or algorithm"],
        compatible_primitives=["observe", "practice", "apply", "assess"],
        common_misconceptions="Address blind step execution without understanding 'why'. Reveal the hidden state changes occurring at each algorithmic step.",
        assessment_recommendations="Assess execution accuracy on unexpected edge cases and system perturbations.",
        personalization_opportunities="Vary problem complexity and provide step-by-step state visualization."
    ),
    "creative_evaluative": DeliveryFramework(
        id="creative_evaluative",
        name="Creative & Evaluative Learning",
        archetype_category="Comparative Learning",
        recommended_layout_template="ComparativeLayout",
        cognitive_characteristics=["divergent thinking", "synthesis", "critical judgment"],
        selection_criteria=["concept involves design, art, or open-ended problem solving"],
        compatible_primitives=["investigate", "construct", "evaluate", "reflect", "debate"],
        common_misconceptions="Address the 'any answer is valid' myth. Guide student to justify choices using explicit evaluative criteria and constraints.",
        assessment_recommendations="Assess using criteria-based rubrics focusing on justification, trade-off analysis, and constraint adherence.",
        personalization_opportunities="Offer choice in medium of expression and problem domain."
    ),
    "generic_fallback": DeliveryFramework(
        id="generic_fallback",
        name="Generic Instructional Framework",
        archetype_category="Conceptual Learning",
        recommended_layout_template="DiscoveryLayout",
        cognitive_characteristics=["general comprehension", "knowledge acquisition"],
        selection_criteria=["metadata is missing", "no specific framework fits perfectly"],
        compatible_primitives=["observe", "explain", "practice", "summarize", "assess"],
        common_misconceptions="Confront basic misconceptions by starting with intuitive phenomena before formal concepts.",
        assessment_recommendations="Use reasoning and scenario application checks over simple factual recall.",
        personalization_opportunities="Provide concrete analogies and additional visual support if comprehension is low."
    )
}

def get_framework(framework_id: str) -> Optional[DeliveryFramework]:
    return FRAMEWORKS.get(framework_id)
