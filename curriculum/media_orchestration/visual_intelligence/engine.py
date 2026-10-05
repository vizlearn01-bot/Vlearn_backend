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
        Deterministically classifies if a requirement should be generated (SVG/Mermaid)
        or retrieved from external providers (Wikimedia, YouTube, PhET, etc.).
        """
        preferred = (req.preferred_media_type or '').lower().strip()
        generatable_types = {'diagram', 'flowchart', 'concept_map', 'chart', 'svg', 'generated_visual', 'schematic'}

        # 1. If preferred type is explicitly a diagram/chart/schematic, it is generatable
        if preferred in generatable_types:
            return True

        # 2. If preferred type is an image, photo, video, or simulation, it is NOT generatable via SVG
        if preferred in ('image', 'photo', 'photograph', 'picture', 'video', 'simulation'):
            return False

        # 3. Check non-generatable media categories (real-world photos, specimens, videos, simulations)
        non_generatable = {
            "real-world visualization",
            "historical visualization",
            "interactive visualization",
            "photograph",
            "specimen",
            "video",
            "simulation",
        }
        if (req.media_category or '').lower().strip() in non_generatable:
            return False

        # 4. Check for concrete physical indicators that require photographic evidence
        concrete_indicators = {
            'photo', 'photograph', 'real-world', 'specimen', 'microscopic', 'telescope',
            'organism', 'animal', 'plant', 'satellite', 'landscape', 'geological', 'apparatus'
        }
        search_terms = set(req.search_keywords or [])
        if req.entity_name:
            search_terms.update(req.entity_name.lower().split())
        purpose_words = set((req.educational_purpose or '').lower().split())

        if (concrete_indicators & search_terms) or (concrete_indicators & purpose_words):
            return False

        # 5. Fallback check
        if (req.fallback_media_type or '').lower().strip() in generatable_types:
            return True

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
