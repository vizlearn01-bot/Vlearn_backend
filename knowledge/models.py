import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    description = models.TextField(blank=True)
    linked_subject_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g. 'Physics' — for cross-linking with the curriculum",
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) or "category"
            slug = base_slug
            counter = 1
            while ArticleCategory.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class ArticleTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) or "tag"
            slug = base_slug
            counter = 1
            while ArticleTag.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Article(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("review", "In Review"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]
    ARTICLE_TYPE_CHOICES = [
        ("educational", "Educational Content"),
        ("platform", "Platform / Company"),
    ]

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True, db_index=True)
    article_type = models.CharField(
        max_length=20,
        choices=ARTICLE_TYPE_CHOICES,
        default="educational",
    )
    summary = models.TextField(
        help_text="1-3 sentence summary for meta description and article cards"
    )
    body = models.TextField(
        help_text="Article body in Markdown. Supports KaTeX math."
    )
    featured_image_url = models.URLField(blank=True, null=True)
    featured_image_alt = models.CharField(max_length=300, blank=True)
    meta_title = models.CharField(
        max_length=70,
        blank=True,
        help_text="Override title for <title> tag. Falls back to title.",
    )
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="Override for meta description. Falls back to summary.",
    )

    # Curriculum linkages (FK to existing curriculum models - SET_NULL)
    linked_topic = models.ForeignKey(
        "curriculum.Topic",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="knowledge_articles",
        help_text="The curriculum Topic this article relates to.",
    )
    linked_learning_unit = models.ForeignKey(
        "curriculum.LearningUnit",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="knowledge_articles",
        help_text="The specific LearningUnit, if more granular than Topic.",
    )
    linked_simulation = models.ForeignKey(
        "curriculum.Simulation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="knowledge_articles",
        help_text="A VizLearn simulation referenced or embedded in this article.",
    )

    # Taxonomies and relationships
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
    )
    tags = models.ManyToManyField(
        ArticleTag,
        blank=True,
        related_name="articles",
    )
    related_articles = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=True,
    )

    # Publishing metadata
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="authored_articles",
    )
    published_at = models.DateTimeField(blank=True, null=True)
    content_uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        indexes = [
            models.Index(fields=["status", "published_at"]),
            models.Index(fields=["article_type", "status"]),
        ]

    def __str__(self):
        return self.title

    @property
    def reading_time_minutes(self):
        if not self.body:
            return 1
        word_count = len(self.body.split())
        return max(1, round(word_count / 200))

    @property
    def curriculum_lineage(self):
        """
        Returns structured syllabus hierarchy for this article without string duplication.
        Resolves via linked_learning_unit or linked_topic.
        """
        topic = self.linked_topic
        unit = self.linked_learning_unit

        if not topic and unit:
            topic = getattr(unit, "topic", None)

        if not topic:
            return None

        subject = getattr(topic, "subject", None)
        grade = getattr(subject, "grade", None)
        curriculum = getattr(grade, "curriculum", None)

        return {
            "curriculum": curriculum.name if curriculum else "Secondary STEM Curriculum",
            "grade": grade.name if grade else "",
            "subject": subject.name if subject else (self.category.name if self.category else "STEM"),
            "topic_id": topic.id if topic else None,
            "topic_name": topic.name if topic else "",
            "learning_unit_id": unit.id if unit else None,
            "learning_unit_name": unit.name if unit else "",
        }

    @property
    def simulation_teaser(self):
        """
        Extracts pedagogical teaser elements from the linked simulation's config or description.
        Returns a dict containing overview, how_to_use steps, expected_results, and subject.
        """
        sim = self.linked_simulation
        if not sim:
            return None

        config = sim.config or {}
        context_spec = config.get("context_spec", {})

        overview = (
            context_spec.get("overview")
            or sim.description
            or f"Explore and test {sim.title} in the virtual laboratory."
        )
        how_to_use = context_spec.get("how_to_use", [])
        expected_results = context_spec.get("expected_results", [])
        if isinstance(expected_results, str):
            formatted_expected_results = [expected_results]
        elif isinstance(expected_results, list):
            formatted_expected_results = expected_results[:2]
        else:
            formatted_expected_results = []

        return {
            "title": sim.title,
            "key": sim.key,
            "subject": (sim.subject or "STEM").upper(),
            "topic": sim.topic or (self.linked_topic.name if self.linked_topic else ""),
            "overview": overview,
            "how_to_use": how_to_use[:3] if how_to_use else [
                "Adjust experimental variables and observe real-time system responses.",
                "Compare simulated observations with theoretical equations.",
            ],
            "expected_results": formatted_expected_results,
        }

    @property
    def simulation_cta_label(self):
        """
        Generates an active, specific pedagogical CTA for the linked simulation.
        Avoids generic 'Learn More'.
        """
        sim = self.linked_simulation
        if not sim:
            return "Explore Interactive Lesson"

        title = sim.title
        if any(term in title for term in ["Law", "Principle", "Theory", "Effect", "Model"]):
            return f"Explore {title} Simulation"
        return f"Launch {title} in Virtual Lab"

    @property
    def related_concepts(self):
        """
        Returns concepts associated with this article's curriculum scope.
        Prioritizes linked_learning_unit.concepts; falls back to linked_topic concepts.
        Leverages prefetch cache when available to eliminate database queries.
        """
        if hasattr(self, "_cached_related_concepts"):
            return self._cached_related_concepts

        concepts = []
        if self.linked_learning_unit_id and self.linked_learning_unit:
            unit_concepts = list(self.linked_learning_unit.concepts.all())
            if unit_concepts:
                concepts = unit_concepts

        if not concepts and self.linked_topic_id and self.linked_topic:
            if (
                hasattr(self.linked_topic, "_prefetched_objects_cache")
                and "learning_units" in self.linked_topic._prefetched_objects_cache
            ):
                for unit in self.linked_topic.learning_units.all():
                    concepts.extend(unit.concepts.all())
            else:
                from curriculum.models import Concept
                concepts = list(
                    Concept.objects.filter(learning_unit__topic_id=self.linked_topic_id)
                    .prefetch_related("misconceptions", "outgoing_relationships__target")
                )

        self._cached_related_concepts = concepts
        return self._cached_related_concepts

    @property
    def common_misconceptions(self):
        """
        Returns misconceptions linked to this article's concepts.
        Traverses prefetched concept.misconceptions in memory for 0 extra SQL queries.
        Falls back to a single bounded query if un-prefetched.
        """
        if hasattr(self, "_cached_common_misconceptions"):
            return self._cached_common_misconceptions

        concepts = self.related_concepts
        if not concepts:
            self._cached_common_misconceptions = []
            return self._cached_common_misconceptions

        first = concepts[0]
        if (
            hasattr(first, "_prefetched_objects_cache")
            and "misconceptions" in first._prefetched_objects_cache
        ):
            misconceptions = []
            for concept in concepts:
                misconceptions.extend(concept.misconceptions.all())
            self._cached_common_misconceptions = misconceptions
            return self._cached_common_misconceptions

        from curriculum.models import Misconception
        concept_ids = [c.id for c in concepts]
        misconceptions = list(
            Misconception.objects.filter(concept_id__in=concept_ids)
            .select_related("concept")
            .order_by("concept__name", "id")
        )
        self._cached_common_misconceptions = misconceptions
        return self._cached_common_misconceptions

    def save(self, *args, **kwargs):
        RESERVED_SLUGS = {"category", "tag", "search", "api", "feed"}
        if not self.slug:
            base_slug = slugify(self.title) or "article"
            if base_slug in RESERVED_SLUGS:
                base_slug = f"{base_slug}-article"
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists() or slug in RESERVED_SLUGS:
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # Manage published_at timestamp when status transitions to 'published' if not already set
        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)
