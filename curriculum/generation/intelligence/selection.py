from curriculum.models import Concept, LearningUnit
from .frameworks import get_framework, FRAMEWORKS

class FrameworkSelectionEngine:
    """
    Deterministically selects an appropriate Delivery Framework for a Learning Unit.
    It relies on the Concept instructional_metadata provided by Agent 2 (Concept Intelligence).
    If metadata is missing or inconclusive, it uses fallback logic.
    """
    
    @staticmethod
    def select(learning_unit: LearningUnit) -> dict:
        concepts = Concept.objects.filter(learning_unit=learning_unit)
        
        # We aggregate cognitive characteristics and abstraction levels
        characteristics = []
        is_math_heavy = False
        is_procedural = False
        is_discussion_heavy = False
        is_process_heavy = False
        
        for concept in concepts:
            metadata = concept.instructional_metadata or {}
            
            # Extract metadata
            cog_cat = metadata.get("cognitive_category", "").lower()
            if cog_cat:
                characteristics.append(cog_cat)
                
            if metadata.get("mathematical_reasoning", False) or "math" in cog_cat or "logic" in cog_cat:
                is_math_heavy = True
                
            if metadata.get("procedural_nature", False) or "procedure" in cog_cat or "algorithm" in cog_cat:
                is_procedural = True
                
            if metadata.get("discussion_suitability", False) or "human" in cog_cat or "social" in cog_cat:
                is_discussion_heavy = True
                
            if metadata.get("experimentation_suitability", False) or "process" in cog_cat or "mechanism" in cog_cat:
                is_process_heavy = True
                
            # Fallback heuristics based on keywords if metadata is sparse
            keywords = [k.lower() for k in concept.keywords]
            name = concept.name.lower()
            
            if any(w in name or w in keywords for w in ["calculate", "equation", "formula", "algebra"]):
                is_math_heavy = True
            if any(w in name or w in keywords for w in ["step", "method", "algorithm", "procedure"]):
                is_procedural = True
            if any(w in name or w in keywords for w in ["society", "ethics", "debate", "history", "people"]):
                is_discussion_heavy = True
            if any(w in name or w in keywords for w in ["reaction", "cycle", "process", "mechanism", "experiment"]):
                is_process_heavy = True

        # Deterministic rules based on aggregated indicators
        selected_framework_id = "generic_fallback"
        
        if is_math_heavy:
            selected_framework_id = "abstract_logical"
        elif is_procedural:
            selected_framework_id = "procedural_algorithmic"
        elif is_discussion_heavy:
            selected_framework_id = "human_social"
        elif is_process_heavy:
            selected_framework_id = "process_based"
            
        framework = get_framework(selected_framework_id)
        if not framework:
            framework = get_framework("generic_fallback")
            
        return {
            "framework_id": framework.id,
            "framework_name": framework.name,
            "archetype_category": framework.archetype_category,
            "recommended_layout_template": framework.recommended_layout_template,
            "cognitive_characteristics": framework.cognitive_characteristics,
            "compatible_primitives": framework.compatible_primitives,
            "common_misconceptions": framework.common_misconceptions,
            "assessment_recommendations": framework.assessment_recommendations,
            "personalization_opportunities": framework.personalization_opportunities
        }
