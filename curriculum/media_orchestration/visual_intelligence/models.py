from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from curriculum.media_orchestration.contracts import ResolvedAsset

class VisualSpecification(BaseModel):
    """
    Output of the Visual Reasoner (LLM).
    A detailed specification for a visualization that the deterministic renderer can execute.
    """
    node_id: str = Field(description="The strategy node this visual is for.")
    format: str = Field(description="The format of the visual (e.g., 'svg', 'mermaid', 'coordinate_graph', 'interactive_widget').")
    code: str = Field(description="The actual code or structured payload to be rendered.")
    explanation: str = Field(description="A brief explanation of what the visual demonstrates.")
    alt_text: str = Field(description="Accessibility text.")

class GeneratedVisual(ResolvedAsset):
    """
    Output of the Visual Renderer. 
    Inherits from ResolvedAsset so it can be transparently injected into the ExperienceAssemblyService.
    """
    # Overriding to make sure we know it's generated
    provenance: str = Field(default="VisualIntelligenceEngine", description="Source origin.")
    licensing: str = Field(default="Generated", description="License type.")
    fallback_used: bool = Field(default=False, description="Generated visuals are primary, not fallbacks.")
    
    # Specific to GeneratedVisual
    raw_code: str = Field(default="", description="The underlying code (SVG/Mermaid) that was generated.")
    render_format: str = Field(default="", description="The format of the raw code.")

class GenerationFailure(BaseModel):
    """
    Emitted when the Visual Reasoner determines it cannot/should not generate the visual,
    or if the Renderer fails.
    """
    node_id: str
    reason: str = Field(description="Why generation failed or was skipped (e.g., 'Too complex', 'Requires real-world photo').")
    confidence: float = Field(description="Confidence in the failure decision.")
    fallback_recommendation: Optional[str] = Field(default=None, description="Recommendation for the Acquisition Engine.")
