from typing import List, Tuple
from curriculum.media_orchestration.contracts import MediaManifest, MediaRequirement
from .models import GeneratedVisual, GenerationFailure
from .reasoner import VisualReasoner
from .renderer import VisualRenderer

class VisualIntelligenceEngine:
    """
    Module 4: Visual Intelligence Engine.
    Attempts to programmatically generate visuals (SVG, Mermaid) via the Reasoner/Renderer flow.
    Requirements that are not generatable or fail generation are passed back in a modified MediaManifest
    to be sent to the MediaAcquisitionEngine. (Wait, they actually execute in parallel now, but we still need to
    return generated visuals).
    """
    
    def __init__(self):
        self.reasoner = VisualReasoner()
        self.renderer = VisualRenderer()

    def _is_generatable(self, req: MediaRequirement) -> bool:
        """
        Deterministically classifies if a requirement should be generated or retrieved.
        """
        non_generatable = {
            "Real-world Visualization",
            "Historical Visualization",
            "Reference Material",
            "Interactive Visualization"
        }
        if req.media_category in non_generatable:
            return False
        return True

    def process_manifest(self, manifest: MediaManifest, pedagogical_context: dict) -> Tuple[List[GeneratedVisual], MediaManifest]:
        generated_visuals: List[GeneratedVisual] = []
        remaining_requirements: List[MediaRequirement] = []
        
        for req in manifest.requirements:
            if not req.is_required:
                remaining_requirements.append(req)
                continue
                
            if not self._is_generatable(req):
                # Skip generation entirely, let Provider Registry handle it
                remaining_requirements.append(req)
                continue
                
            # 1. Reasoner (LLM): Can we generate this?
            spec, failure = self.reasoner.evaluate_requirement(req, pedagogical_context)
            
            if failure:
                # LLM decided it cannot generate
                remaining_requirements.append(req)
                continue
                
            # 2. Renderer (Deterministic): Generate the artifact
            visual, render_failure = self.renderer.render(spec)
            
            if render_failure:
                # Rendering failed
                remaining_requirements.append(req)
                continue
                
            # Success!
            generated_visuals.append(visual)
            
        # Return the generated visuals and a NEW manifest containing what was not generated
        remaining_manifest = MediaManifest(requirements=remaining_requirements)
        return generated_visuals, remaining_manifest
