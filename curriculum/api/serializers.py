from rest_framework import serializers
from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit,
    Lesson, LessonBlock, LessonAsset, KnowledgePack, KnowledgeChunk,
    GenerationJob, PedagogyTemplate, GenerationRule,
    Concept, ConceptRelationship, LearningObjective, Misconception,
    LearningExperienceGraph, LearningSession, RuntimeNodeProgress,
    Simulation,
)


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ['id', 'name', 'description', 'is_active']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'curriculum', 'name', 'level', 'description']


class SubjectSerializer(serializers.ModelSerializer):
    grade_name = serializers.CharField(source='grade.name', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'grade', 'grade_name', 'name', 'description']


class TopicSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    has_published_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'subject_name', 'name', 'description', 'order', 'image', 'has_published_lesson']

    def get_has_published_lesson(self, obj):
        return obj.lessons.filter(status='published').exists()


class LearningUnitSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source='topic.name', read_only=True)

    class Meta:
        model = LearningUnit
        fields = ['id', 'topic', 'topic_name', 'name', 'description', 'order']


class GenerationRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerationRule
        fields = ['id', 'template', 'block_type', 'order', 'is_mandatory', 'system_prompt', 'validation_schema']


class PedagogyTemplateSerializer(serializers.ModelSerializer):
    rules = GenerationRuleSerializer(many=True, read_only=True)

    class Meta:
        model = PedagogyTemplate
        fields = ['id', 'subject', 'name', 'description', 'is_active', 'rules']


class LessonBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonBlock
        fields = ['id', 'lesson', 'block_id', 'block_type', 'title', 'content', 'order', 'metadata',
                  'page_number', 'page_title', 'component_type', 'component_order']


class LessonSerializer(serializers.ModelSerializer):
    blocks = LessonBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'id', 'topic', 'learning_unit', 'title', 'status', 'version',
            'published_at', 'immutable_metadata', 'knowledge_pack', 'blocks',
            'created_at', 'updated_at',
        ]


class KnowledgeChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeChunk
        fields = [
            'id', 'knowledge_pack', 'topic', 'learning_unit', 'lesson',
            'content_text', 'chunk_type', 'start_page', 'end_page',
            'section_title', 'paragraph_index', 'metadata', 'order',
        ]


class KnowledgePackSerializer(serializers.ModelSerializer):
    """
    NOTE: Chunks are NOT inlined by default. Fetching a KnowledgePack
    list with inline chunks would cause massive over-fetching. Use the
    /knowledge-chunks/?knowledge_pack=<id> endpoint to retrieve chunks.
    A lightweight chunk_count is exposed instead.
    """
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    chunk_count = serializers.SerializerMethodField()

    class Meta:
        model = KnowledgePack
        fields = [
            'id', 'subject', 'subject_name', 'source_file_url', 'file', 'status',
            'version', 'created_at', 'updated_at', 'approved_at', 'chunk_count',
            'extracted_structure'
        ]

    def get_chunk_count(self, obj):
        return obj.chunks.count()


class GenerationJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerationJob
        fields = [
            'id', 'lesson', 'status', 'job_type', 'generation_mode',
            'target_block_id', 'error_message', 'created_at', 'completed_at',
        ]


# ---------------------------------------------------------------------------
# Semantic Graph & V3/V4 Serializers
# ---------------------------------------------------------------------------

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = [
            'id', 'name', 'description', 'keywords', 'learning_unit',
            'knowledge_pack', 'origin_chunk', 'page_number_origin',
            'version', 'created_at', 'updated_at', 'instructional_metadata',
        ]

class ConceptRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptRelationship
        fields = [
            'id', 'source', 'target', 'relationship_type', 'origin_chunk', 'version'
        ]

class LearningObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningObjective
        fields = [
            'id', 'description', 'bloom_taxonomy_level', 'learning_unit',
            'concept', 'origin_chunk', 'page_number_origin', 'version'
        ]

class MisconceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misconception
        fields = [
            'id', 'description', 'correction', 'concept', 'origin_chunk',
            'page_number_origin', 'version'
        ]

class LearningExperienceGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningExperienceGraph
        fields = [
            'id', 'learning_unit', 'generation_job', 'version', 'status',
            'graph_data', 'quality_report', 'provenance', 'created_at', 'updated_at'
        ]

class LearningSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSession
        fields = [
            'id', 'user', 'graph', 'status', 'mastery_score',
            'created_at', 'updated_at', 'completed_at'
        ]

class RuntimeNodeProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuntimeNodeProgress
        fields = [
            'id', 'session', 'node_id', 'status', 'attempts',
            'elapsed_time_seconds', 'metadata', 'created_at', 'updated_at'
        ]

# ---------------------------------------------------------------------------
# V2 Serializers — Additive only. V1 serializers above are unchanged.
# ---------------------------------------------------------------------------

class LessonAssetSerializer(serializers.ModelSerializer):
    """
    Full read/write representation of a LessonAsset.
    Used by the Content Studio to create and update asset slots.
    """
    class Meta:
        model = LessonAsset
        fields = [
            'id', 'lesson', 'blocks',
            'asset_type', 'source_type', 'storage_type', 'status',
            'title', 'description', 'file', 'url',
            'knowledge_chunk', 'metadata', 'version',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class LessonAssetBriefSerializer(serializers.ModelSerializer):
    """
    Lightweight representation for embedding inside a LessonBlock.
    Only the fields the Lesson Viewer actually needs to render an asset.
    """
    class Meta:
        model = LessonAsset
        fields = [
            'id', 'asset_type', 'source_type', 'storage_type', 'status',
            'title', 'description', 'file', 'url', 'metadata', 'version',
        ]


class LessonBlockV2Serializer(serializers.ModelSerializer):
    """
    V2 block serializer. Extends V1 fields with presentation metadata and
    inline assets.  Fully backward compatible — new fields are always
    present in the response but are null for legacy (V1) blocks, so existing
    frontend code that ignores unknown keys is unaffected.
    """
    assets = LessonAssetBriefSerializer(many=True, read_only=True)

    class Meta:
        model = LessonBlock
        fields = [
            # V1 fields (unchanged)
            'id', 'lesson', 'block_id', 'block_type', 'title',
            'content', 'order', 'metadata',
            # V2 presentation fields
            'page_number', 'page_title', 'component_type', 'component_order',
            # Related assets
            'assets',
        ]


class LessonV2Serializer(serializers.ModelSerializer):
    """
    V2 lesson serializer. Blocks carry full V2 presentation metadata and
    inline assets. Assets at the lesson level are also exposed so the
    Content Studio can manage the full asset inventory in one response.
    """
    blocks = LessonBlockV2Serializer(many=True, read_only=True)
    assets = LessonAssetSerializer(many=True, read_only=True)
    quality_report = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = [
            'id', 'topic', 'learning_unit', 'title', 'status', 'version',
            'published_at', 'immutable_metadata', 'knowledge_pack',
            'blocks', 'assets', 'quality_report',
            'created_at', 'updated_at',
        ]
        
    def get_quality_report(self, obj):
        latest_job = obj.generation_jobs.order_by('-created_at').first()
        if latest_job:
            graph = latest_job.generated_graphs.first()
            if graph and graph.quality_report:
                return graph.quality_report
        return {}


class SimulationSerializer(serializers.ModelSerializer):
    subject_display = serializers.CharField(source='get_subject_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Simulation
        fields = [
            'id', 'key', 'title', 'subject', 'subject_display',
            'topic', 'status', 'status_display', 'description',
            'archetype', 'config', 'created_at', 'updated_at'
        ]

