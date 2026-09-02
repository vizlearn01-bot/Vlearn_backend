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
        "Your role is analyzing a LearningExperiencePlan and converting key instructional moments "
        "into focused MediaRequirements.\n\n"
        "RULES OF DISCIPLINE & PEDAGOGICAL COVERAGE:\n"
        "1. MANDATORY VIDEO: Every lesson MUST have exactly ONE high-yield educational video requirement on the primary core concept/mechanism node (e.g. preferred_media_type='video', media_category='Educational Video', search_keywords=['<Major Concept> experiment explanation animation']).\n"
        "2. VISUALS ON CORE CARDS: Request 3 TO 5 high-impact diagrams/visuals across the core explanation, worked example, formula breakdown, or real-world application nodes.\n"
        "3. Nodes that do NOT typically require media:\n"
        "   - Short learning goals, predict prompts, reflections, and summaries.\n"
        "4. Every requested visual/video must answer: 'What physical, spatial, or structural relationship does the learner understand better because they can see this?'\n"
        "5. For all requirements:\n"
        "   - Provide 3+ highly specific, domain-accurate search_keywords.\n"
        "   - Set entity_name, educational_purpose, and accessibility_requirements clearly.\n"
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
