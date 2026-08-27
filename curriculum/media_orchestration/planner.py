import json
from ai_infrastructure.llm_factory import LLMFactory
from ai_infrastructure.config import DEFAULT_GEMINI_MODEL
from .contracts import LearningExperiencePlan, MediaManifest

class MediaPlanner:
    """
    Module 1: Media Planner (AI)
    Consumes the Instructional Intent (LearningExperiencePlan).
    Determines media requirements for each learning moment.
    Never retrieves or generates media itself.
    Never alters instructional intent.
    """
    
    SYSTEM_INSTRUCTION = (
        "You are the Lead Media Planner for the VLearn Learning Compiler.\n"
        "Your role is analyzing a LearningExperiencePlan and converting its instructional intent "
        "into complete, provider-agnostic MediaRequirements and VisualSpecifications.\n\n"
        "Your specifications must equally support deterministic media retrieval (e.g. Wikimedia Commons, educational repositories), "
        "human content creators (illustrators, video editors, teachers), and future AI visual generation engines (currently temporarily disabled for token optimization).\n\n"
        "RULES OF EXCELLENCE:\n"
        "1. NEVER alter pedagogy, lesson sequence, or instructional intent.\n"
        "2. Reject decorative visuals. Request media ONLY when it reveals an invisible mechanism, spatial relationship, temporal process, or system change.\n"
        "3. Describe the learner's visualization requirements rather than assuming a specific production or acquisition method.\n"
        "4. For every visual requirement, populate ALL fields in VisualSpecification:\n"
        "   - visual_format, subject_focus, spatial_layout_and_perspective, key_labels, color_emphasis, style_guidelines.\n"
        "   - invisible_mechanism: Specify the hidden microscopic/physical/logical process.\n"
        "   - targeted_misconception: Specify the exact misbelief being refuted.\n"
        "   - guided_attention_target: State what specific feature the learner must observe and notice.\n"
        "   - temporal_sequence: List high-level educational stages (Initial State -> Transformation -> Outcome).\n"
        "5. Maximise Retrieval & Generation Precision: Extract entity_name, scientific_name, aliases, related_concepts, and 3+ domain-specific search_keywords.\n"
        "6. Output MUST conform strictly to the MediaManifest JSON schema."
    )
    
    @staticmethod
    def generate_manifest(plan: LearningExperiencePlan) -> MediaManifest:
        provider = LLMFactory.get_provider()
        
        # Serialize the plan to JSON for the prompt
        plan_json = plan.model_dump_json(indent=2)
        prompt = (
            f"Analyze the following Learning Experience Plan and generate a Media Manifest.\n\n"
            f"{plan_json}"
        )
        
        # Request structured output matching our MediaManifest Pydantic model
        result = provider.generate_structured(
            prompt=prompt,
            response_schema=MediaManifest,
            system_instruction=MediaPlanner.SYSTEM_INSTRUCTION,
            model_name=DEFAULT_GEMINI_MODEL
        )
        
        # Gemini provider returns a pydantic model instance if generate_structured is used properly
        if isinstance(result, MediaManifest):
            return result
        elif isinstance(result, str):
            # In case the provider returns a JSON string instead of parsed model
            return MediaManifest.model_validate_json(result)
        else:
            # If it's a dict
            return MediaManifest.model_validate(result)
