import logging
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from django.db import transaction

from curriculum.models import KnowledgePack, KnowledgeChunk, Concept, ConceptRelationship, LearningObjective, Misconception, LearningUnit
from curriculum.generation.llm_client import LLMClient

logger = logging.getLogger("curriculum.semantic_extraction")


# ---------------------------------------------------------------------------
# Structured Pydantic Schemas for Semantic Extraction
# ---------------------------------------------------------------------------

class ConceptSchema(BaseModel):
    name: str = Field(description="Name of the concept.")
    description: str = Field(description="Detailed factual explanation.")
    keywords: List[str] = Field(default_factory=list, description="Key domain terms.")
    instructional_metadata: Dict[str, Any] = Field(default_factory=dict, description="e.g. cognitive_category, mathematical_reasoning, discussion_suitability.")
    origin_chunk_id: Optional[int] = Field(default=None, description="ID of source chunk.")
    page_number: Optional[int] = Field(default=None, description="Source page number.")


class RelationshipSchema(BaseModel):
    source_concept_name: str = Field(description="Name of the source concept.")
    target_concept_name: str = Field(description="Name of the target concept.")
    type: str = Field(default="related_to", description="prerequisite | part_of | causes | related_to")
    origin_chunk_id: Optional[int] = Field(default=None)


class ObjectiveSchema(BaseModel):
    description: str = Field(description="The student will be able to...")
    bloom_level: Optional[str] = Field(default="Understand", description="Bloom taxonomy level.")
    related_concept_name: Optional[str] = Field(default=None)
    origin_chunk_id: Optional[int] = Field(default=None)
    page_number: Optional[int] = Field(default=None)


class MisconceptionSchema(BaseModel):
    description: str = Field(description="Common false belief.")
    correction: str = Field(description="Factual correction.")
    related_concept_name: Optional[str] = Field(default=None)
    origin_chunk_id: Optional[int] = Field(default=None)
    page_number: Optional[int] = Field(default=None)


class SemanticExtractionSchema(BaseModel):
    concepts: List[ConceptSchema] = Field(default_factory=list)
    relationships: List[RelationshipSchema] = Field(default_factory=list)
    objectives: List[ObjectiveSchema] = Field(default_factory=list)
    misconceptions: List[MisconceptionSchema] = Field(default_factory=list)


class SemanticStructuringService:
    """
    Agent 2 Phase 4 & 5:
    Uses LLM to convert raw deterministic Document Chunks into structured
    educational knowledge anchored to a LearningUnit.
    """
    def __init__(self, learning_unit_id, knowledge_pack_id):
        self.learning_unit = LearningUnit.objects.get(id=learning_unit_id)
        self.knowledge_pack = KnowledgePack.objects.get(id=knowledge_pack_id)
        
    def process(self):
        """Compatibility wrapper to prevent breaking changes."""
        return self.process_chunks()

    def process_chunks(self):
        # Gather all chunks for this learning unit.
        chunks = KnowledgeChunk.objects.filter(
            knowledge_pack=self.knowledge_pack,
            learning_unit=self.learning_unit
        ).order_by('order', 'id')
        
        if not chunks.exists():
            chunks = KnowledgeChunk.objects.filter(
                knowledge_pack=self.knowledge_pack, 
                chunk_type__in=['core_text', 'definition', 'worked_example']
            ).order_by('order', 'id')[:20]
            
        if not chunks.exists():
            logger.info("No chunks found to process for LearningUnit %s", self.learning_unit.id)
            return

        combined_text = "\n\n".join([f"[Chunk ID: {c.id} Page: {c.start_page}] {c.content_text}" for c in chunks])
        
        prompt = (
            f"You are a Knowledge Pipeline Engineer. Extract structured semantic educational knowledge from the following text.\n"
            f"TEXT:\n{combined_text}\n"
        )
        
        # Phase 4 Semantic Extraction via structured schema
        try:
            data = LLMClient.generate_structured(prompt, SemanticExtractionSchema)
            if isinstance(data, SemanticExtractionSchema):
                self._save_to_db(data)
            else:
                parsed = SemanticExtractionSchema.model_validate(data)
                self._save_to_db(parsed)
        except Exception as e:
            logger.error("Failed to extract or save semantic structuring for LU %s: %s", self.learning_unit.id, e)

    @transaction.atomic
    def _save_to_db(self, data: SemanticExtractionSchema):
        """Phase 5: Repository Population with Idempotency"""
        # Clean up existing concepts/objectives for this unit before updating
        Concept.objects.filter(learning_unit=self.learning_unit, knowledge_pack=self.knowledge_pack).delete()
        LearningObjective.objects.filter(learning_unit=self.learning_unit).delete()

        concept_map = {}
        
        for c in data.concepts:
            chunk = KnowledgeChunk.objects.filter(id=c.origin_chunk_id, knowledge_pack=self.knowledge_pack).first()
            concept = Concept.objects.create(
                name=c.name,
                description=c.description,
                keywords=c.keywords,
                instructional_metadata=c.instructional_metadata,
                learning_unit=self.learning_unit,
                knowledge_pack=self.knowledge_pack,
                origin_chunk=chunk,
                page_number_origin=c.page_number
            )
            concept_map[c.name.strip().lower()] = concept
            concept_map[c.name.strip()] = concept
            
        for r in data.relationships:
            source = concept_map.get(r.source_concept_name.strip().lower()) or concept_map.get(r.source_concept_name.strip())
            target = concept_map.get(r.target_concept_name.strip().lower()) or concept_map.get(r.target_concept_name.strip())
            if source and target:
                chunk = KnowledgeChunk.objects.filter(id=r.origin_chunk_id, knowledge_pack=self.knowledge_pack).first()
                rel_type = r.type if r.type in ['prerequisite', 'part_of', 'causes', 'related_to'] else 'related_to'
                ConceptRelationship.objects.get_or_create(
                    source=source,
                    target=target,
                    relationship_type=rel_type,
                    defaults={'origin_chunk': chunk}
                )
                
        for o in data.objectives:
            related_concept = None
            if o.related_concept_name:
                related_concept = concept_map.get(o.related_concept_name.strip().lower()) or concept_map.get(o.related_concept_name.strip())
            chunk = KnowledgeChunk.objects.filter(id=o.origin_chunk_id, knowledge_pack=self.knowledge_pack).first()
            LearningObjective.objects.create(
                description=o.description,
                bloom_taxonomy_level=o.bloom_level,
                learning_unit=self.learning_unit,
                concept=related_concept,
                origin_chunk=chunk,
                page_number_origin=o.page_number
            )
            
        for m in data.misconceptions:
            related_concept = None
            if m.related_concept_name:
                related_concept = concept_map.get(m.related_concept_name.strip().lower()) or concept_map.get(m.related_concept_name.strip())
            if related_concept:
                chunk = KnowledgeChunk.objects.filter(id=m.origin_chunk_id, knowledge_pack=self.knowledge_pack).first()
                Misconception.objects.create(
                    description=m.description,
                    correction=m.correction,
                    concept=related_concept,
                    origin_chunk=chunk,
                    page_number_origin=m.page_number
                )
