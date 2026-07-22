from typing import List
from curriculum.media_orchestration.contracts import ResolvedAsset
from curriculum.media_orchestration.search_intelligence.models import SearchPayload
from curriculum.models import KnowledgeChunk, Concept
from .base import BaseProvider

class KnowledgeRepoProvider(BaseProvider):
    @property
    def provider_name(self) -> str:
        return "KnowledgeRepository"

    def search(self, payload: SearchPayload, node_id: str) -> List[ResolvedAsset]:
        results = []
        if payload.preferred_media_category not in ["Abstract Visualization", "Real-world Visualization", "Reference Material"]:
            return results

        keywords = set([payload.primary_query.lower()] + [q.lower() for q in payload.alternate_queries])

        concepts_with_images = Concept.objects.filter(origin_chunk__image__isnull=False).exclude(origin_chunk__image='')
        for concept in concepts_with_images:
            concept_text = f"{concept.name} {concept.description} {' '.join(concept.keywords)}".lower()
            if any(kw in concept_text for kw in keywords):
                results.append(ResolvedAsset(
                    node_id=node_id,
                    asset_type='image',
                    url=concept.origin_chunk.image.url,
                    provenance='KnowledgeRepository',
                    source='KnowledgeRepository',
                    provider=self.provider_name,
                    licensing='Internal/Proprietary',
                    alt_text=f"Image for {concept.name}",
                    confidence_score=0.95,
                    knowledge_chunk_id=concept.origin_chunk.id,
                    verified=True,
                    metadata={"concept_match": True}
                ))

        chunks_with_images = KnowledgeChunk.objects.exclude(image='')
        for chunk in chunks_with_images:
            chunk_text = chunk.content_text.lower()
            if any(kw in chunk_text for kw in keywords):
                # Ensure we don't duplicate
                if not any(r.knowledge_chunk_id == chunk.id for r in results):
                    results.append(ResolvedAsset(
                        node_id=node_id,
                        asset_type='image',
                        url=chunk.image.url,
                        provenance='KnowledgeRepository',
                        source='KnowledgeRepository',
                        provider=self.provider_name,
                        licensing='Internal/Proprietary',
                        alt_text="Content reference image",
                        confidence_score=0.85,
                        knowledge_chunk_id=chunk.id,
                        verified=True,
                        metadata={"chunk_match": True}
                    ))

        return results

class SimulationProvider(BaseProvider):
    @property
    def provider_name(self) -> str:
        return "PhET Interactive Simulations"

    def search(self, payload: SearchPayload, node_id: str) -> List[ResolvedAsset]:
        results = []
        if payload.preferred_media_category != 'Interactive Visualization':
            return results

        keywords = set([payload.primary_query.lower()] + [q.lower() for q in payload.alternate_queries])
        search_terms = " ".join(keywords)
        
        if "gas" in search_terms or "boyle" in search_terms:
            results.append(ResolvedAsset(
                node_id=node_id,
                asset_type='simulation',
                url='https://phet.colorado.edu/sims/html/gas-properties/latest/gas-properties_en.html',
                provenance='PhET',
                source='PhET',
                provider=self.provider_name,
                licensing='CC-BY 4.0',
                alt_text='Interactive Gas Properties Simulation',
                confidence_score=0.90,
                verified=True,
                metadata={"topic": "gas properties"}
            ))

        return results
