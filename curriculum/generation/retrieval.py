from curriculum.models import LearningUnit, KnowledgeChunk

class RetrievalService:
    @staticmethod
    def assemble_context(learning_unit_id: int) -> dict:
        learning_unit = LearningUnit.objects.select_related(
            'topic', 
            'topic__subject', 
            'topic__subject__grade', 
            'topic__subject__grade__curriculum'
        ).get(id=learning_unit_id)
        
        chunks = KnowledgeChunk.objects.filter(learning_unit=learning_unit).order_by('order')
        
        chunk_data = {
            "definitions": [],
            "worked_examples": [],
            "diagrams": [],
            "exercises": [],
            "practicals": [],
            "core_text": []
        }
        
        for chunk in chunks:
            asset = {
                "content": chunk.content_text,
                "pages": f"{chunk.start_page}" if chunk.start_page else None
            }
            if chunk.chunk_type == 'diagram' and chunk.image:
                asset["image_url"] = chunk.image.url
                asset["content"] = "[Image/Diagram]"
                chunk_data["diagrams"].append(asset)
            elif chunk.chunk_type in chunk_data:
                chunk_data[chunk.chunk_type].append(asset)
            else:
                chunk_data["core_text"].append(asset)
            
        return {
            "curriculum": learning_unit.topic.subject.grade.curriculum.name,
            "grade": learning_unit.topic.subject.grade.name,
            "subject": learning_unit.topic.subject.name,
            "topic": learning_unit.topic.name,
            "learning_unit": learning_unit.name,
            "chunks": chunk_data
        }
