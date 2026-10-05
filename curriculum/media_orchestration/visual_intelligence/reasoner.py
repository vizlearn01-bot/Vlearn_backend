import json
from typing import Optional, List, Tuple, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
from pydantic.alias_generators import to_camel

from ai_infrastructure.llm_factory import LLMFactory
from ai_infrastructure.config import DEFAULT_GEMINI_MODEL

from curriculum.media_orchestration.contracts import MediaRequirement
from .models import VisualSpecification, GenerationFailure

class ReasonerResponse(BaseModel):
    """
    Wrapper for the LLM output to handle both success and failure branches.
    Supports both snake_case and camelCase output from all LLM providers.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel, extra='ignore')

    can_generate: bool = Field(default=False, description="True if the visual can be generated programmatically, False if an external asset search is required.")
    format: Optional[str] = Field(default=None, description="The chosen format (svg, mermaid) if can_generate is True.")
    code: Optional[str] = Field(default=None, description="The generated raw code (SVG/Mermaid) if can_generate is True. Use standard SVG or Mermaid syntax.")
    explanation: Optional[str] = Field(default=None, description="Brief explanation of the generated visual.")
    alt_text: Optional[str] = Field(default=None, description="Accessibility text.")
    failure_reason: Optional[str] = Field(default=None, description="Why generation is not suitable if can_generate is False.")
    confidence: float = Field(default=1.0, description="Confidence score 0.0 to 1.0.")

    @model_validator(mode='before')
    @classmethod
    def unwrap_properties_envelope(cls, data: Any) -> Any:
        if isinstance(data, dict) and "properties" in data and isinstance(data["properties"], dict):
            # Model echoed JSON Schema envelope: flatten properties into root
            props = data["properties"]
            return {**data, **props}
        return data

    @field_validator('can_generate', mode='before')
    @classmethod
    def sanitize_bool(cls, v):
        return bool(v) if v is not None else False

    @field_validator('confidence', mode='before')
    @classmethod
    def sanitize_confidence(cls, v):
        try:
            return float(v) if v is not None else 1.0
        except (ValueError, TypeError):
            return 1.0

    @field_validator('format', 'code', 'explanation', 'alt_text', 'failure_reason', mode='before')
    @classmethod
    def sanitize_strings(cls, v):
        return str(v) if v is not None else None

class VisualReasoner:
    """
    Module 4a: Visual Reasoner (LLM).
    Evaluates a MediaRequirement to determine if it can be programmatically generated.
    If yes, outputs the specific visualization code. If no, emits a failure for fallback.
    """
    
    SYSTEM_INSTRUCTION = (
        "You are the Visual Reasoner for the VLearn Learning Compiler.\n"
        "Your responsibility is to analyze a media requirement and pedagogical context, "
        "and generate clean, high-quality, professional educational visuals (SVG diagrams, Mermaid flowcharts).\n\n"
        "RULES:\n"
        "1. For diagrams, flowcharts, structures, processes, models, apparatus setups, and abstract concepts, generate clean SVG code.\n"
        "2. When a teacher or administrator requests a visual (e.g., 'Diagram showing this concept', 'Illustrate this lesson', etc.), "
        "infer the key educational concepts from the lesson topic, title, and specifically the target card context, set `can_generate` to true, and generate an appropriate SVG diagram.\n"
        "3. When a specific target card is provided in the context, deeply inspect that card's title, description, activity/questions, and concepts. Even if the administrator prompt is minimal or vague, produce a rich, relevant SVG diagram tailored directly to that card's subject matter.\n"
        "4. Only set `can_generate` to false if the request strictly requires a real-life historical photograph or physical artifact that cannot be illustrated with an SVG diagram.\n"
        "5. If you can generate it, set `can_generate` to true, `format` to 'svg', and provide valid, standalone SVG code in the `code` field.\n"
        "6. For SVGs: Output clean, standalone SVG XML string with a viewBox without markdown codeblocks or outer HTML.\n"
        "7. For Mermaid: Output valid Mermaid syntax without markdown codeblocks.\n"
    )
    
    def __init__(self):
        self.provider = LLMFactory.get_provider()

    def evaluate_requirement(self, req: MediaRequirement, pedagogical_context: dict) -> Tuple[Optional[VisualSpecification], Optional[GenerationFailure]]:
        """
        Evaluate a single requirement.
        Returns (VisualSpecification, None) on success, or (None, GenerationFailure) on failure.
        """
        is_targeted = bool(pedagogical_context.get("is_targeted_generation") or pedagogical_context.get("administrator_instruction"))
        admin_prompt = pedagogical_context.get("administrator_instruction") or req.description

        if is_targeted:
            targeted_card = pedagogical_context.get('targeted_card') or {}
            card_section = ""
            if targeted_card:
                card_section = (
                    f"SPECIFIC TARGET CARD TO VISUALIZE:\n"
                    f"- Card Title: {targeted_card.get('title')}\n"
                    f"- Card Type: {targeted_card.get('component_type')}\n"
                    f"- Card Content & Details:\n{targeted_card.get('details')}\n\n"
                )

            prompt = (
                f"You are the Visual Reasoner for VLearn generating an educational visual requested by a teacher/administrator.\n\n"
                f"ADMINISTRATOR INSTRUCTION:\n"
                f"\"{admin_prompt}\"\n\n"
                f"{card_section}"
                f"LESSON HIERARCHY & PEDAGOGICAL CONTEXT:\n"
                f"- Subject: {pedagogical_context.get('subject')} ({pedagogical_context.get('grade_level')})\n"
                f"- Topic: {pedagogical_context.get('topic')}\n"
                f"- Learning Unit: {pedagogical_context.get('learning_unit')}\n"
                f"- Lesson: {pedagogical_context.get('lesson_title')}\n"
                f"- Same-Page Concepts:\n{pedagogical_context.get('same_page_context') or 'N/A'}\n"
                f"- Lesson Key Concepts & Goals:\n{pedagogical_context.get('lesson_pedagogical_content') or 'N/A'}\n\n"
                f"REQUIREMENT:\n"
                f"{req.model_dump_json(indent=2)}\n\n"
                f"TASK:\n"
                f"Synthesize the administrator's instruction together with the specific target card content and lesson concepts.\n"
                f"Even if the administrator's instruction is very brief or vague (e.g. 'diagram', 'visual', 'chart', 'walk'), "
                f"deeply leverage the target card content, topic, and concepts provided above to generate a clear, professional, "
                f"pedagogically rich standalone educational SVG diagram. Set can_generate=True, format='svg', and provide valid standalone SVG with viewBox in `code`.\n"
            )
        else:
            prompt = (
                f"Analyze the following Media Requirement and pedagogical context.\n"
                f"Decide if you can generate a visual for it.\n\n"
                f"REQUIREMENT:\n"
                f"{req.model_dump_json(indent=2)}\n\n"
                f"CONTEXT:\n"
                f"{json.dumps(pedagogical_context, indent=2)}\n\n"
            )
        
        try:
            result = self.provider.generate_structured(
                prompt=prompt,
                response_schema=ReasonerResponse,
                system_instruction=self.SYSTEM_INSTRUCTION
            )
            
            # Parse result into ReasonerResponse
            if isinstance(result, str):
                response_obj = ReasonerResponse.model_validate_json(result)
            elif isinstance(result, dict):
                response_obj = ReasonerResponse.model_validate(result)
            elif isinstance(result, ReasonerResponse):
                response_obj = result
            else:
                response_obj = ReasonerResponse.model_validate(result)
                
            # If targeted generation returned can_generate=False or empty code, attempt a direct generation fallback
            if is_targeted and not (response_obj.can_generate and response_obj.code and response_obj.format):
                target_card_desc = ""
                if targeted_card:
                    target_card_desc = f"Target Card: [{targeted_card.get('component_type')}] {targeted_card.get('title')}\nTarget Card Details: {str(targeted_card.get('details'))[:400]}\n"

                direct_prompt = (
                    f"Generate a standalone educational SVG diagram illustrating the concepts for this lesson card.\n"
                    f"Lesson: {pedagogical_context.get('lesson_title', '')}\n"
                    f"Topic: {pedagogical_context.get('topic', '')}\n"
                    f"Subject: {pedagogical_context.get('subject', '')}\n"
                    f"{target_card_desc}"
                    f"Teacher Instruction: {admin_prompt}\n"
                    f"Concepts: {str(pedagogical_context.get('lesson_pedagogical_content', ''))[:400]}\n\n"
                    f"Provide format='svg', can_generate=True, and clean standalone SVG code with viewBox in `code`."
                )
                try:
                    retry_result = self.provider.generate_structured(
                        prompt=direct_prompt,
                        response_schema=ReasonerResponse,
                        system_instruction=self.SYSTEM_INSTRUCTION
                    )
                    if isinstance(retry_result, ReasonerResponse):
                        retry_obj = retry_result
                    elif isinstance(retry_result, dict):
                        retry_obj = ReasonerResponse.model_validate(retry_result)
                    elif isinstance(retry_result, str):
                        retry_obj = ReasonerResponse.model_validate_json(retry_result)
                    else:
                        retry_obj = None

                    if retry_obj and retry_obj.can_generate and retry_obj.code:
                        response_obj = retry_obj
                except Exception:
                    pass

            if response_obj.can_generate and response_obj.code and response_obj.format:
                spec = VisualSpecification(
                    node_id=req.node_id,
                    format=response_obj.format.lower(),
                    code=response_obj.code,
                    explanation=response_obj.explanation or "Generated visual.",
                    alt_text=response_obj.alt_text or req.accessibility_requirements
                )
                return spec, None
            else:
                failure = GenerationFailure(
                    node_id=req.node_id,
                    reason=response_obj.failure_reason or "Visual reasoning determined generation is not suitable.",
                    confidence=response_obj.confidence,
                    fallback_recommendation=req.preferred_media_type
                )
                return None, failure
        except Exception as eval_err:
            # Fall back safely to external asset acquisition without breaking the entire lesson compiler
            failure = GenerationFailure(
                node_id=req.node_id,
                reason=f"Visual reasoner fallback: {str(eval_err)}",
                confidence=0.0,
                fallback_recommendation=req.preferred_media_type
            )
            return None, failure
