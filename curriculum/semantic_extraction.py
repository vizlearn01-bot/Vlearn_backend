import json
from curriculum.models import KnowledgePack, KnowledgeChunk, Concept, ConceptRelationship, LearningObjective, Misconception, LearningUnit
from curriculum.generation.llm_client import LLMClient

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
        # Gather all chunks for this learning unit. If not explicitly linked,
        # we pull the core chunks for the KnowledgePack to deduce concepts.
        chunks = KnowledgeChunk.objects.filter(
            knowledge_pack=self.knowledge_pack,
            learning_unit=self.learning_unit
        )
        if not chunks.exists():
            chunks = KnowledgeChunk.objects.filter(
                knowledge_pack=self.knowledge_pack, 
                chunk_type__in=['core_text', 'definition', 'worked_example']
            )[:20] # Limit to avoid context window explosion for now
            
        if not chunks.exists():
            print("No chunks found to process.")
            return

        combined_text = "\n\n".join([f"[Chunk ID: {c.id} Page: {c.start_page}] {c.content_text}" for c in chunks])
        
        prompt = f"""
You are a Knowledge Pipeline Engineer. Extract structured semantic educational knowledge from the following text.
Your output must be a valid JSON object with the exact schema below. Do not include markdown formatting.

SCHEMA:
{{
    "concepts": [
        {{
            "name": "Concept Name",
            "description": "Detailed explanation",
            "keywords": ["key1", "key2"],
            "instructional_metadata": {{
                "cognitive_category": "e.g., conceptual, procedural, factual",
                "mathematical_reasoning": false,
                "procedural_nature": false,
                "discussion_suitability": false,
                "experimentation_suitability": false
            }},
            "origin_chunk_id": 123,
            "page_number": 1
        }}
    ],
    "relationships": [
        {{
            "source_concept_name": "Concept A",
            "target_concept_name": "Concept B",
            "type": "prerequisite|part_of|causes|related_to",
            "origin_chunk_id": 123
        }}
    ],
    "objectives": [
        {{
            "description": "The student will be able to...",
            "bloom_level": "Understand",
            "related_concept_name": "Concept Name",
            "origin_chunk_id": 123,
            "page_number": 1
        }}
    ],
    "misconceptions": [
        {{
            "description": "Common false belief",
            "correction": "Factual correction",
            "related_concept_name": "Concept Name",
            "origin_chunk_id": 123,
            "page_number": 1
        }}
    ]
}}

TEXT:
{combined_text}
"""
        
        # Phase 4 Semantic Extraction
        response = LLMClient.generate(prompt)
        
        try:
            clean_response = response.strip()
            if clean_response.startswith('```json'):
                clean_response = clean_response[7:-3]
            elif clean_response.startswith('```'):
                clean_response = clean_response[3:-3]
                
            data = json.loads(clean_response)
            self._save_to_db(data)
        except Exception as e:
            print(f"Failed to parse or save semantic structuring output: {e}")

    def _save_to_db(self, data):
        """Phase 5: Repository Population"""
        concept_map = {}
        
        for c in data.get("concepts", []):
            chunk = KnowledgeChunk.objects.filter(id=c.get("origin_chunk_id")).first()
            concept = Concept.objects.create(
                name=c["name"],
                description=c["description"],
                keywords=c.get("keywords", []),
                instructional_metadata=c.get("instructional_metadata", {}),
                learning_unit=self.learning_unit,
                knowledge_pack=self.knowledge_pack,
                origin_chunk=chunk,
                page_number_origin=c.get("page_number")
            )
            concept_map[c["name"]] = concept
            
        for r in data.get("relationships", []):
            source = concept_map.get(r.get("source_concept_name"))
            target = concept_map.get(r.get("target_concept_name"))
            if source and target:
                chunk = KnowledgeChunk.objects.filter(id=r.get("origin_chunk_id")).first()
                ConceptRelationship.objects.get_or_create(
                    source=source,
                    target=target,
                    relationship_type=r.get("type", "related_to"),
                    defaults={'origin_chunk': chunk}
                )
                
        for o in data.get("objectives", []):
            related_concept = concept_map.get(o.get("related_concept_name"))
            chunk = KnowledgeChunk.objects.filter(id=o.get("origin_chunk_id")).first()
            LearningObjective.objects.create(
                description=o["description"],
                bloom_taxonomy_level=o.get("bloom_level"),
                learning_unit=self.learning_unit,
                concept=related_concept,
                origin_chunk=chunk,
                page_number_origin=o.get("page_number")
            )
            
        for m in data.get("misconceptions", []):
            related_concept = concept_map.get(m.get("related_concept_name"))
            if related_concept:
                chunk = KnowledgeChunk.objects.filter(id=m.get("origin_chunk_id")).first()
                Misconception.objects.create(
                    description=m["description"],
                    correction=m["correction"],
                    concept=related_concept,
                    origin_chunk=chunk,
                    page_number_origin=m.get("page_number")
                )
