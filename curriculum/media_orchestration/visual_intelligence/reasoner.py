import json
from typing import Optional, List, Tuple
from pydantic import BaseModel, Field

from ai_infrastructure.llm_factory import LLMFactory
from ai_infrastructure.config import DEFAULT_GEMINI_MODEL

from curriculum.media_orchestration.contracts import MediaRequirement
from .models import VisualSpecification, GenerationFailure

class ReasonerResponse(BaseModel):
    """
    Wrapper for the LLM output to handle both success and failure branches.
    """
    can_generate: bool = Field(description="True if the visual can be generated programmatically, False if an external asset search is required.")
    format: Optional[str] = Field(default=None, description="The chosen format (svg, mermaid) if can_generate is True.")
    code: Optional[str] = Field(default=None, description="The generated raw code (SVG/Mermaid) if can_generate is True. Use standard SVG or Mermaid syntax.")
    explanation: Optional[str] = Field(default=None, description="Brief explanation of the generated visual.")
    alt_text: Optional[str] = Field(default=None, description="Accessibility text.")
    failure_reason: Optional[str] = Field(default=None, description="Why generation is not suitable if can_generate is False.")
    confidence: float = Field(default=1.0, description="Confidence score 0.0 to 1.0.")

class VisualReasoner:
    """
    Module 4a: Visual Reasoner (LLM).
    Evaluates a MediaRequirement to determine if it can be programmatically generated.
    If yes, outputs the specific visualization code. If no, emits a failure for fallback.
    """
    
    SYSTEM_INSTRUCTION = (
        "You are the Visual Reasoner for the VLearn Learning Compiler.\n"
        "Your responsibility is to analyze a media requirement and determine if it can be "
        "programmatically generated (e.g., as an SVG diagram, Mermaid flowchart, etc.).\n\n"
        "RULES:\n"
        "1. Prefer generation for: mathematical models, flowcharts, logic gates, chemical bonds, "
        "timelines, standard diagrams, and abstract concepts.\n"
        "2. Do NOT generate for: real-world photographs, historical artifacts, high-fidelity 3D "
        "renders, or things requiring real-life accuracy (e.g., 'A photo of Abraham Lincoln').\n"
        "3. If you can generate it, set `can_generate` to true and provide valid SVG or Mermaid code in the `code` field.\n"
        "4. If you cannot generate it, set `can_generate` to false and provide a `failure_reason`.\n"
        "5. For SVGs: Output clean, standalone SVG XML string without markdown codeblocks. Do not include outer HTML. Must have viewBox.\n"
        "6. For Mermaid: Output valid Mermaid syntax without markdown codeblocks.\n"
    )
    
    def __init__(self):
        self.provider = LLMFactory.get_provider()

    def evaluate_requirement(self, req: MediaRequirement, pedagogical_context: dict) -> Tuple[Optional[VisualSpecification], Optional[GenerationFailure]]:
        """
        Evaluate a single requirement.
        Returns (VisualSpecification, None) on success, or (None, GenerationFailure) on failure.
        """
        prompt = (
            f"Analyze the following Media Requirement and pedagogical context.\n"
            f"Decide if you can generate a visual for it.\n\n"
            f"REQUIREMENT:\n"
            f"{req.model_dump_json(indent=2)}\n\n"
            f"CONTEXT:\n"
            f"{json.dumps(pedagogical_context, indent=2)}\n"
        )
        
        result = self.provider.generate_structured(
            prompt=prompt,
            response_schema=ReasonerResponse,
            system_instruction=self.SYSTEM_INSTRUCTION,
            model_name=DEFAULT_GEMINI_MODEL
        )
        
        # Parse result into ReasonerResponse
        if isinstance(result, str):
            response_obj = ReasonerResponse.model_validate_json(result)
        elif isinstance(result, dict):
            response_obj = ReasonerResponse.model_validate(result)
        else:
            response_obj = result
            
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
