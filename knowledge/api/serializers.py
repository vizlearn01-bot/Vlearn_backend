from rest_framework import serializers
from knowledge.models import Article, ArticleCategory, ArticleTag
from curriculum.models import Topic, LearningUnit, Simulation, Concept, Misconception, ConceptRelationship


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "linked_subject_name",
            "order",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = [
            "id",
            "name",
            "slug",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class CurriculumTopicOptionSerializer(serializers.ModelSerializer):
    subject_id = serializers.IntegerField(source="subject.id", read_only=True)
    subject_name = serializers.CharField(source="subject.name", read_only=True)
    grade_name = serializers.CharField(source="subject.grade.name", read_only=True)
    curriculum_name = serializers.CharField(source="subject.grade.curriculum.name", read_only=True)

    class Meta:
        model = Topic
        fields = ["id", "name", "subject_id", "subject_name", "grade_name", "curriculum_name", "order"]


class CurriculumLearningUnitOptionSerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField(source="topic.id", read_only=True)
    topic_name = serializers.CharField(source="topic.name", read_only=True)

    class Meta:
        model = LearningUnit
        fields = ["id", "name", "topic_id", "topic_name", "order"]


class CurriculumSimulationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = [
            "id",
            "key",
            "title",
            "subject",
            "topic",
            "status",
            "description",
        ]


class PublicConceptRelationshipSerializer(serializers.ModelSerializer):
    target_concept_id = serializers.IntegerField(source="target.id", read_only=True)
    target_concept_name = serializers.CharField(source="target.name", read_only=True)

    class Meta:
        model = ConceptRelationship
        fields = [
            "id",
            "relationship_type",
            "target_concept_id",
            "target_concept_name",
        ]


class PublicMisconceptionSerializer(serializers.ModelSerializer):
    concept_id = serializers.IntegerField(source="concept.id", read_only=True)
    concept_name = serializers.CharField(source="concept.name", read_only=True)

    class Meta:
        model = Misconception
        fields = [
            "id",
            "content_uuid",
            "concept_id",
            "concept_name",
            "description",
            "correction",
        ]


class PublicConceptSerializer(serializers.ModelSerializer):
    misconceptions = PublicMisconceptionSerializer(many=True, read_only=True)
    relationships = PublicConceptRelationshipSerializer(
        source="outgoing_relationships", many=True, read_only=True
    )

    class Meta:
        model = Concept
        fields = [
            "id",
            "content_uuid",
            "name",
            "description",
            "keywords",
            "relationships",
            "misconceptions",
        ]


class PublicArticleListSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(read_only=True)
    tags = ArticleTagSerializer(many=True, read_only=True)
    author_name = serializers.SerializerMethodField()
    reading_time_minutes = serializers.ReadOnlyField()

    class Meta:
        model = Article
        fields = [
            "id",
            "content_uuid",
            "title",
            "slug",
            "article_type",
            "summary",
            "featured_image_url",
            "featured_image_alt",
            "category",
            "tags",
            "published_at",
            "reading_time_minutes",
            "author_name",
            "created_at",
        ]

    def get_author_name(self, obj):
        if obj.author:
            full_name = obj.author.get_full_name()
            return full_name if full_name else obj.author.username
        return None


class PublicArticleDetailSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(read_only=True)
    tags = ArticleTagSerializer(many=True, read_only=True)
    linked_topic = CurriculumTopicOptionSerializer(read_only=True)
    linked_learning_unit = CurriculumLearningUnitOptionSerializer(read_only=True)
    linked_simulation = CurriculumSimulationOptionSerializer(read_only=True)
    curriculum_lineage = serializers.ReadOnlyField()
    simulation_teaser = serializers.ReadOnlyField()
    simulation_cta_label = serializers.ReadOnlyField()
    related_concepts = PublicConceptSerializer(many=True, read_only=True)
    common_misconceptions = PublicMisconceptionSerializer(many=True, read_only=True)
    related_articles = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    reading_time_minutes = serializers.ReadOnlyField()

    class Meta:
        model = Article
        fields = [
            "id",
            "content_uuid",
            "title",
            "slug",
            "article_type",
            "summary",
            "body",
            "featured_image_url",
            "featured_image_alt",
            "meta_title",
            "meta_description",
            "category",
            "tags",
            "linked_topic",
            "linked_learning_unit",
            "linked_simulation",
            "curriculum_lineage",
            "simulation_teaser",
            "simulation_cta_label",
            "related_concepts",
            "common_misconceptions",
            "related_articles",
            "published_at",
            "reading_time_minutes",
            "author_name",
            "created_at",
            "updated_at",
        ]

    def get_related_articles(self, obj):
        qs = (
            obj.related_articles.filter(status="published")
            .select_related("category", "author")
            .prefetch_related("tags")
        )
        if not qs.exists() and obj.category:
            qs = (
                Article.objects.filter(status="published", category=obj.category)
                .exclude(pk=obj.pk)
                .select_related("category", "author")
                .prefetch_related("tags")[:3]
            )
        return PublicArticleListSerializer(qs, many=True, context=self.context).data

    def get_author_name(self, obj):
        if obj.author:
            full_name = obj.author.get_full_name()
            return full_name if full_name else obj.author.username
        return None


class AdminArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=ArticleCategory.objects.all(),
        required=False,
        allow_null=True,
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=ArticleTag.objects.all(),
        many=True,
        required=False,
    )
    related_articles = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(),
        many=True,
        required=False,
    )
    linked_topic = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(),
        required=False,
        allow_null=True,
    )
    linked_learning_unit = serializers.PrimaryKeyRelatedField(
        queryset=LearningUnit.objects.all(),
        required=False,
        allow_null=True,
    )
    linked_simulation = serializers.PrimaryKeyRelatedField(
        queryset=Simulation.objects.all(),
        required=False,
        allow_null=True,
    )

    category_details = ArticleCategorySerializer(source="category", read_only=True)
    tags_details = ArticleTagSerializer(source="tags", many=True, read_only=True)
    linked_topic_details = CurriculumTopicOptionSerializer(
        source="linked_topic", read_only=True
    )
    linked_learning_unit_details = CurriculumLearningUnitOptionSerializer(
        source="linked_learning_unit", read_only=True
    )
    linked_simulation_details = CurriculumSimulationOptionSerializer(
        source="linked_simulation", read_only=True
    )
    author_name = serializers.SerializerMethodField()
    reading_time_minutes = serializers.ReadOnlyField()

    class Meta:
        model = Article
        fields = [
            "id",
            "content_uuid",
            "title",
            "slug",
            "article_type",
            "summary",
            "body",
            "featured_image_url",
            "featured_image_alt",
            "meta_title",
            "meta_description",
            "linked_topic",
            "linked_learning_unit",
            "linked_simulation",
            "category",
            "tags",
            "related_articles",
            "status",
            "author",
            "published_at",
            "created_at",
            "updated_at",
            "category_details",
            "tags_details",
            "linked_topic_details",
            "linked_learning_unit_details",
            "linked_simulation_details",
            "author_name",
            "reading_time_minutes",
        ]
        read_only_fields = ["id", "content_uuid", "created_at", "updated_at"]
        extra_kwargs = {
            "slug": {"required": False},
        }

    def get_author_name(self, obj):
        if obj.author:
            full_name = obj.author.get_full_name()
            return full_name if full_name else obj.author.username
        return None
