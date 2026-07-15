from rest_framework import serializers
from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit,
    Lesson, LessonBlock, LessonAsset, KnowledgePack, KnowledgeChunk,
    GenerationJob, PedagogyTemplate, GenerationRule,
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

    class Meta:
        model = Lesson
        fields = [
            'id', 'topic', 'learning_unit', 'title', 'status', 'version',
            'published_at', 'immutable_metadata', 'knowledge_pack',
            'blocks', 'assets',
            'created_at', 'updated_at',
        ]
