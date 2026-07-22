from abc import ABC, abstractmethod
from typing import Optional
from .contracts import MediaRequirement, ResolvedAsset
from curriculum.models import KnowledgeChunk, Concept

class BaseAssetAdapter(ABC):
    """
    Interface for asset resolution providers.
    """
    @abstractmethod
    def resolve(self, requirement: MediaRequirement) -> Optional[ResolvedAsset]:
        """
        Attempt to resolve a MediaRequirement into a ResolvedAsset.
        Returns None if no asset is found.
        """
        pass

class KnowledgeRepoAdapter(BaseAssetAdapter):
    """
    Adapter that searches the local KnowledgeRepository (KnowledgeChunk & Concept models).
    """
    def resolve(self, requirement: MediaRequirement) -> Optional[ResolvedAsset]:
        # Prefer images or diagrams from the local repository
        if requirement.preferred_media_type not in ['image', 'diagram'] and requirement.fallback_media_type not in ['image', 'diagram']:
            return None
            
        # 1. High-precision semantic match: look for Concepts linked to an image chunk
        concepts_with_images = Concept.objects.filter(origin_chunk__image__isnull=False).exclude(origin_chunk__image='')
        for concept in concepts_with_images:
            concept_text = f"{concept.name} {concept.description} {' '.join(concept.keywords)}".lower()
            if any(keyword.lower() in concept_text for keyword in requirement.search_keywords):
                return ResolvedAsset(
                    node_id=requirement.node_id,
                    asset_type='image',
                    url=concept.origin_chunk.image.url,
                    provenance='KnowledgeRepository (Concept Match)',
                    licensing='Internal/Proprietary',
                    alt_text=requirement.accessibility_requirements,
                    confidence_score=0.95,
                    fallback_used=(requirement.preferred_media_type not in ['image', 'diagram']),
                    knowledge_chunk_id=concept.origin_chunk.id
                )
                
        # 2. Basic fallback: look for a chunk with an image that matches keywords
        chunks_with_images = KnowledgeChunk.objects.exclude(image='')
        for chunk in chunks_with_images:
            chunk_text = chunk.content_text.lower()
            # Simple keyword matching
            if any(keyword.lower() in chunk_text for keyword in requirement.search_keywords):
                return ResolvedAsset(
                    node_id=requirement.node_id,
                    asset_type='image',
                    url=chunk.image.url if chunk.image else None,
                    provenance='KnowledgeRepository',
                    licensing='Internal/Proprietary',
                    alt_text=requirement.accessibility_requirements,
                    confidence_score=0.85,
                    fallback_used=(requirement.preferred_media_type not in ['image', 'diagram']),
                    knowledge_chunk_id=chunk.id
                )
        return None

class WikimediaAdapter(BaseAssetAdapter):
    """
    Adapter for Wikimedia Commons API.
    Currently stubbed/mocked to gracefully degrade as per implementation constraints.
    """
    def resolve(self, requirement: MediaRequirement) -> Optional[ResolvedAsset]:
        # Gracefully degrade / mock for now
        # In the future, this will make real HTTP requests to Wikipedia API.
        
        # MOCK BEHAVIOR: Simulate finding a Wikipedia image for certain keywords.
        search_terms = " ".join(requirement.search_keywords).lower()
        if "atom" in search_terms or "molecule" in search_terms:
            return ResolvedAsset(
                node_id=requirement.node_id,
                asset_type='image',
                url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Stylised_atom_with_three_Bohr_model_orbits_and_stylised_nucleus.svg/500px-Stylised_atom_with_three_Bohr_model_orbits_and_stylised_nucleus.svg.png',
                provenance='Wikimedia Commons',
                licensing='CC-BY-SA 3.0',
                alt_text=requirement.accessibility_requirements,
                confidence_score=0.75,
                fallback_used=False
            )
            
        return None

class SimulationAdapter(BaseAssetAdapter):
    """
    Adapter for interactive simulations (e.g., PhET).
    Currently stubbed/mocked to gracefully degrade.
    """
    def resolve(self, requirement: MediaRequirement) -> Optional[ResolvedAsset]:
        if requirement.preferred_media_type != 'simulation' and requirement.fallback_media_type != 'simulation':
            return None
            
        search_terms = " ".join(requirement.search_keywords).lower()
        if "gas" in search_terms or "boyle" in search_terms:
            return ResolvedAsset(
                node_id=requirement.node_id,
                asset_type='simulation',
                url='https://phet.colorado.edu/sims/html/gas-properties/latest/gas-properties_en.html',
                provenance='PhET Interactive Simulations',
                licensing='CC-BY 4.0',
                alt_text=requirement.accessibility_requirements,
                confidence_score=0.90,
                fallback_used=False
            )
            
        return None
