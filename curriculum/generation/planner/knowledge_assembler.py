import logging
from curriculum.models import KnowledgeChunk, LearningUnit, Concept, Misconception, LearningObjective

logger = logging.getLogger("curriculum.generation")

class KnowledgeAssembler:
    """
    Consumes the structured Knowledge Repository (Agent 2 output) and prepares
    a pure pedagogical context payload. Avoids any legacy generation constraints.
    """
    
    @staticmethod
    def assemble(learning_unit_id: int) -> dict:
        """
        Retrieves all KnowledgeChunks associated with a LearningUnit and organizes
        them logically for the Learning Experience Planner LLM.
        """
        try:
            learning_unit = LearningUnit.objects.select_related(
                'topic', 
                'topic__subject', 
                'topic__subject__grade', 
                'topic__subject__grade__curriculum'
            ).get(id=learning_unit_id)
        except LearningUnit.DoesNotExist:
            raise ValueError(f"LearningUnit {learning_unit_id} not found.")

        topic = learning_unit.topic
        subject = topic.subject
        grade = subject.grade
        curriculum = grade.curriculum

        # Group by chunk type to provide structured educational knowledge
        categorized_chunks = {
            'core_concepts': [],
            'definitions': [],
            'examples': [],
            'misconceptions': [],
            'assessments': []
        }

        provenance_ids = []

        # 1. Fetch structured semantic knowledge (Agent 2 Phase 4 & 5)
        concepts = Concept.objects.filter(
            learning_unit=learning_unit
        ).prefetch_related('misconceptions', 'objectives')

        for concept in concepts:
            item = {
                'id': concept.id,
                'name': concept.name,
                'description': concept.description,
                'keywords': concept.keywords,
                'instructional_metadata': concept.instructional_metadata,
            }
            categorized_chunks['core_concepts'].append(item)
            if concept.origin_chunk_id:
                provenance_ids.append(concept.origin_chunk_id)

            for obj in concept.objectives.all():
                categorized_chunks['assessments'].append({
                    'id': obj.id,
                    'description': obj.description,
                    'bloom_level': obj.bloom_taxonomy_level
                })
                if obj.origin_chunk_id:
                    provenance_ids.append(obj.origin_chunk_id)

            for misc in concept.misconceptions.all():
                categorized_chunks['misconceptions'].append({
                    'id': misc.id,
                    'description': misc.description,
                    'correction': misc.correction
                })
                if misc.origin_chunk_id:
                    provenance_ids.append(misc.origin_chunk_id)

        # 2. Fetch raw fallback/legacy chunks
        chunks = KnowledgeChunk.objects.filter(
            learning_unit=learning_unit
        ).order_by('order')

        for chunk in chunks:
            # Skip if this chunk was successfully parsed into a concept already
            # (We check if it exists in provenance to avoid duplicating data)
            if chunk.id in provenance_ids:
                continue

            c_type = chunk.chunk_type.lower()
            text = chunk.content_text.strip()
            if not text:
                continue
                
            provenance_ids.append(chunk.id)

            item = {
                'id': chunk.id,
                'content': text,
                'metadata': chunk.metadata
            }
            
            if 'definition' in c_type:
                categorized_chunks['definitions'].append(item)
            elif 'example' in c_type or 'practical' in c_type:
                categorized_chunks['examples'].append(item)
            elif 'misconception' in c_type or 'warning' in c_type:
                categorized_chunks['misconceptions'].append(item)
            elif 'exercise' in c_type or 'question' in c_type:
                categorized_chunks['assessments'].append(item)
            else:
                categorized_chunks['core_concepts'].append(item)

        # --- Telemetry: Log knowledge retrieval stats ---
        total_items = sum(len(v) for v in categorized_chunks.values())
        total_chars = sum(
            len(str(item.get('description', '') or item.get('content', '') or ''))
            for items in categorized_chunks.values()
            for item in items
        )
        logger.info(
            "[KNOWLEDGE ASSEMBLER] LearningUnit=%d (%s) | "
            "concepts=%d definitions=%d examples=%d misconceptions=%d assessments=%d | "
            "total_items=%d total_chars=%d",
            learning_unit_id, learning_unit.name,
            len(categorized_chunks['core_concepts']),
            len(categorized_chunks['definitions']),
            len(categorized_chunks['examples']),
            len(categorized_chunks['misconceptions']),
            len(categorized_chunks['assessments']),
            total_items, total_chars
        )

        return {
            'metadata': {
                'curriculum': curriculum.name,
                'grade': grade.name,
                'subject': subject.name,
                'topic': topic.name,
                'learning_unit': learning_unit.name,
                'learning_unit_description': learning_unit.description or "",
            },
            'knowledge': categorized_chunks,
            'provenance_chunk_ids': provenance_ids
        }

