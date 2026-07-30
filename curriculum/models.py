from django.db import models
from Resources.models import User

class Curriculum(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="e.g., CBC, IGCSE")
    description = models.TextField(blank=True, null=True)
    max_selectable_subjects = models.PositiveIntegerField(default=8, help_text="Maximum subjects a student can select")
    max_priority_subjects = models.PositiveIntegerField(default=3, help_text="Maximum help priority subjects allowed")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, related_name='grades')
    name = models.CharField(max_length=255, help_text="e.g., Grade 10, Form 4")
    level = models.IntegerField(default=1, help_text="Numeric level for ordering")
    description = models.TextField(blank=True, null=True)
    max_selectable_subjects_override = models.PositiveIntegerField(null=True, blank=True, help_text="Grade-level override for max subjects")
    max_priority_subjects_override = models.PositiveIntegerField(null=True, blank=True, help_text="Grade-level override for max priority subjects")

    class Meta:
        ordering = ['level']
        unique_together = ('curriculum', 'name')

    def __str__(self):
        return f"{self.curriculum.name} - {self.name}"

class Subject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=255, help_text="e.g., Chemistry, Physics")
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('grade', 'name')

    def __str__(self):
        return f"{self.grade.name} - {self.name}"

class PedagogyTemplate(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='pedagogy_templates')
    name = models.CharField(max_length=255, help_text="e.g., Chemistry Standard Flow")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class GenerationRule(models.Model):
    template = models.ForeignKey(PedagogyTemplate, on_delete=models.CASCADE, related_name='rules')
    block_type = models.CharField(max_length=50, help_text="e.g., overview, objective, core_explanation")
    order = models.IntegerField(default=0, help_text="Sequence of the block in the template")
    is_mandatory = models.BooleanField(default=False, help_text="If True, this block must be present for a lesson to be published")
    system_prompt = models.TextField(help_text="Instructions for the LLM to generate this block")
    validation_schema = models.JSONField(default=dict, blank=True, help_text="Optional JSON schema for validation")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.template.name} - {self.block_type} ({self.order})"

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=255, help_text="e.g., Gas Laws, The Mole")
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Sequence of the topic")
    image = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.subject.name} - {self.name}"

class LearningUnit(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='learning_units')
    name = models.CharField(max_length=255, help_text="e.g., Boyle's Law, Charles's Law")
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Sequence of the learning unit")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.topic.name} - {self.name}"


class Lesson(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('review', 'In Review'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lessons')
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.CASCADE, related_name='lessons', null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Optional title for the lesson")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    version = models.IntegerField(default=1)
    
    # Immutable metadata
    immutable_metadata = models.JSONField(default=dict, blank=True, help_text="Stores generation_job_id, ai_model, prompt_version, knowledge_pack_version, generated_at")
    
    # Reference to the Knowledge Pack that served as the ground truth
    knowledge_pack = models.ForeignKey('KnowledgePack', on_delete=models.SET_NULL, null=True, blank=True, related_name='generated_lessons')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-version']

    def __str__(self):
        return f"{self.topic.name} - v{self.version} ({self.get_status_display()})"


class GenerationJob(models.Model):
    JOB_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('generating', 'Generating'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    JOB_TYPE_CHOICES = [
        ('full_lesson', 'Full Lesson'),
        ('single_block', 'Single Block'),
    ]
    GENERATION_MODE_CHOICES = [
        ('legacy',    'Legacy (V1 block-by-block)'),
        ('blueprint', 'Instructional Blueprint (V2)'),
        ('learning_experience_planner', 'Learning Experience Planner (V3 Pedagogical)'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='generation_jobs')
    status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, default='pending')
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_lesson')
    generation_mode = models.CharField(
        max_length=50,
        choices=GENERATION_MODE_CHOICES,
        default='legacy',
        help_text=(
            "Controls which generation engine is used. "
            "'legacy' preserves the V1 GenerationRule loop; "
            "'blueprint' uses the Instructional Designer AI; "
            "'learning_experience_planner' uses the V3 Pedagogical Engine."
        ),
    )
    target_block_id = models.CharField(max_length=100, blank=True, null=True, help_text="Set if generating a single block")
    error_message = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Job {self.id} ({self.status}) for {self.lesson}"


class LessonBlock(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='blocks')
    block_id = models.CharField(max_length=100, blank=True, null=True, help_text="Unique identifier generated by AI")
    block_type = models.CharField(max_length=50, help_text="e.g., overview, objective, core_explanation, video_ref")
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.JSONField(default=dict, blank=True, null=True, help_text="Stores markdown string, or JSON payload for media references")
    order = models.IntegerField(default=0)
    metadata = models.JSONField(default=dict, blank=True, help_text="Optional block-level metadata like search keywords")

    # -------------------------------------------------------------------------
    # V2 Presentation Metadata — all nullable; legacy blocks are unaffected.
    # Pages are a frontend grouping concern, NOT a separate database table.
    # -------------------------------------------------------------------------
    page_number = models.IntegerField(
        null=True, blank=True,
        help_text="Which page (1-indexed) this block belongs to. NULL = legacy V1 block."
    )
    page_title = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="Optional display title for the page this block introduces."
    )
    component_type = models.CharField(
        max_length=80, null=True, blank=True,
        help_text=(
            "Fine-grained learning component role. "
            "e.g., learning_goal, concept_explanation, worked_example, "
            "knowledge_check, summary, transition, callout, real_world_example, "
            "suggested_diagram, suggested_video, suggested_image, suggested_simulation, "
            "suggested_gif, suggested_external_link."
        )
    )
    component_order = models.IntegerField(
        null=True, blank=True,
        help_text="Position of this component within its page. NULL = legacy V1 block."
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.lesson} - {self.block_type} ({self.order})"


# ---------------------------------------------------------------------------
# LessonAsset — Persistent media attached to Lessons and LessonBlocks.
# ---------------------------------------------------------------------------

class LessonAsset(models.Model):
    """
    Represents a persistent media or link asset that supports one or more
    LessonBlocks within a Lesson.  Assets are NEVER regenerated during viewing.

    Sources:
      - knowledge_repository : extracted directly from a KnowledgeChunk.
      - uploaded             : manually provided by an administrator.
      - ai_generated         : produced by a generative media service.
      - external             : a URL to an external website, YouTube, simulation, etc.

    Storage:
      - file   : asset stored on the server filesystem / object storage.
      - url    : asset lives at a remote URL (YouTube, simulation embed, etc.).
      - embed  : asset is an embed code or iframe src stored in `url`.
    """

    ASSET_TYPE_CHOICES = [
        ('image',        'Image'),
        ('diagram',      'Diagram'),
        ('video',        'Video'),
        ('youtube',      'YouTube Video'),
        ('gif',          'GIF'),
        ('simulation',   'Simulation / Interactive Widget'),
        ('external_link','External Link'),
        ('generated',    'AI-Generated Media'),
    ]

    SOURCE_TYPE_CHOICES = [
        ('knowledge_repository', 'Knowledge Repository'),
        ('uploaded',             'Admin Uploaded'),
        ('ai_generated',         'AI Generated'),
        ('external',             'External URL'),
    ]

    STORAGE_TYPE_CHOICES = [
        ('file',  'File (server / object storage)'),
        ('url',   'Remote URL'),
        ('embed', 'Embed Code / iframe src'),
    ]

    STATUS_CHOICES = [
        ('pending',   'Pending — slot created, media not yet attached'),
        ('attached',  'Attached — media has been provided'),
        ('archived',  'Archived'),
    ]

    # --- Ownership -----------------------------------------------------------
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='assets',
        help_text="The lesson this asset belongs to."
    )
    # A single asset can be referenced by multiple blocks (e.g., the same
    # diagram used in an explanation block and in a worked-example block).
    blocks = models.ManyToManyField(
        LessonBlock, blank=True, related_name='assets',
        help_text="Which LessonBlocks display this asset."
    )

    # --- Classification ------------------------------------------------------
    asset_type   = models.CharField(max_length=50, choices=ASSET_TYPE_CHOICES)
    source_type  = models.CharField(max_length=50, choices=SOURCE_TYPE_CHOICES, default='external')
    storage_type = models.CharField(max_length=20, choices=STORAGE_TYPE_CHOICES, default='url')
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # --- Content -------------------------------------------------------------
    title       = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(
        blank=True, null=True,
        help_text="Caption, alt-text, or AI suggestion prompt for this asset slot."
    )
    # File-based assets (uploaded or AI-generated)
    file = models.FileField(
        upload_to='lesson_assets/', blank=True, null=True,
        help_text="For uploaded or AI-generated static files."
    )
    # URL-based assets (YouTube, external, simulation embeds)
    url = models.URLField(
        blank=True, null=True,
        help_text="For YouTube, External, or CDN-hosted links."
    )

    # --- Provenance ----------------------------------------------------------
    knowledge_chunk = models.ForeignKey(
        'KnowledgeChunk', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='lesson_assets',
        help_text="Link back to the originating textbook chunk, if applicable."
    )

    # --- Extensible metadata -------------------------------------------------
    metadata = models.JSONField(
        default=dict, blank=True,
        help_text=(
            "Extensible payload. Examples: "
            "{\"youtube_id\": \"abc123\", \"duration_seconds\": 180} or "
            "{\"admin_instruction\": \"Upload a diagram of Boyle's Law here.\"}"
        )
    )

    # --- Versioning ----------------------------------------------------------
    version = models.IntegerField(
        default=1,
        help_text="Incremented each time this asset is replaced with a newer file/URL."
    )

    # --- Timestamps ----------------------------------------------------------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lesson', 'asset_type', 'created_at']

    def __str__(self):
        return f"[{self.get_asset_type_display()}] {self.title or 'Untitled'} — {self.lesson}"

class KnowledgePack(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('review', 'Pending Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='knowledge_packs')
    source_file_url = models.URLField(help_text="URL of the uploaded textbook", blank=True, null=True)
    file = models.FileField(upload_to='textbooks/', blank=True, null=True, help_text="Uploaded textbook file")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    version = models.IntegerField(default=1)
    extracted_structure = models.JSONField(default=list, blank=True, help_text="JSON structure of Topics and Learning Units extracted from the document")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-version']

    def __str__(self):
        return f"KP: {self.subject.name} - v{self.version} ({self.get_status_display()})"


class KnowledgeChunk(models.Model):
    knowledge_pack = models.ForeignKey(KnowledgePack, on_delete=models.CASCADE, related_name='chunks')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='chunks')
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.SET_NULL, null=True, blank=True, related_name='chunks')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name='chunks')
    
    content_text = models.TextField(blank=True, help_text="The raw extracted textbook text")
    chunk_type = models.CharField(max_length=50, help_text="e.g., core_text, worked_example, exercise, definition, diagram, table")
    
    image = models.ImageField(upload_to='knowledge_assets/', blank=True, null=True, help_text="Extracted image or cropped scanned region")
    bounding_box = models.JSONField(blank=True, null=True, help_text="Coordinates [x0, y0, x1, y1]")
    ocr_confidence = models.FloatField(blank=True, null=True, help_text="OCR confidence score if applicable")
    
    # Source Span Metadata
    start_page = models.IntegerField(blank=True, null=True)
    end_page = models.IntegerField(blank=True, null=True)
    section_title = models.CharField(max_length=255, blank=True, null=True)
    paragraph_index = models.IntegerField(blank=True, null=True)
    
    metadata = models.JSONField(default=dict, blank=True, help_text="Additional extracted properties")
    
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['knowledge_pack', 'order']

    def __str__(self):
        return f"Chunk {self.order} ({self.chunk_type}) - {self.section_title}"

# ---------------------------------------------------------------------------
# Semantic Knowledge Graph Models (Agent 2 Phase 4 & 5)
# ---------------------------------------------------------------------------

class Concept(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(help_text="Detailed semantic explanation of the concept")
    keywords = models.JSONField(default=list, blank=True, help_text="List of semantic keywords")
    
    # Anchors
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.CASCADE, related_name='concepts', help_text="The primary curriculum entity this concept belongs to")
    
    # Provenance
    knowledge_pack = models.ForeignKey(KnowledgePack, on_delete=models.SET_NULL, null=True, blank=True, related_name='extracted_concepts', help_text="The ingestion source")
    origin_chunk = models.ForeignKey('KnowledgeChunk', on_delete=models.SET_NULL, null=True, blank=True, related_name='derived_concepts', help_text="The exact chunk this concept was extracted from")
    page_number_origin = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Phase 5: Concept Intelligence
    instructional_metadata = models.JSONField(
        default=dict, 
        blank=True, 
        help_text="Optional metadata (e.g. cognitive_category, conceptual_complexity) used by the Framework Selection Engine"
    )

    class Meta:
        ordering = ['learning_unit', 'name']

    def __str__(self):
        return f"Concept: {self.name}"

class ConceptRelationship(models.Model):
    RELATIONSHIP_CHOICES = [
        ('prerequisite', 'Is a prerequisite for'),
        ('part_of', 'Is part of'),
        ('causes', 'Causes'),
        ('related_to', 'Is related to'),
    ]
    source = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='outgoing_relationships')
    target = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='incoming_relationships')
    relationship_type = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    
    # Provenance
    origin_chunk = models.ForeignKey('KnowledgeChunk', on_delete=models.SET_NULL, null=True, blank=True)
    version = models.IntegerField(default=1)

    class Meta:
        unique_together = ('source', 'target', 'relationship_type')

    def __str__(self):
        return f"{self.source.name} --[{self.relationship_type}]--> {self.target.name}"

class LearningObjective(models.Model):
    description = models.TextField()
    bloom_taxonomy_level = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., Remember, Understand, Apply, Analyze, Evaluate, Create")
    
    # Anchors
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.CASCADE, related_name='learning_objectives')
    concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, null=True, blank=True, related_name='objectives')
    
    # Provenance
    origin_chunk = models.ForeignKey('KnowledgeChunk', on_delete=models.SET_NULL, null=True, blank=True)
    page_number_origin = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.description[:50]

class Misconception(models.Model):
    description = models.TextField(help_text="The false belief or misunderstanding")
    correction = models.TextField(help_text="The factual correction or explanation")
    
    # Anchors
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='misconceptions')
    
    # Provenance
    origin_chunk = models.ForeignKey('KnowledgeChunk', on_delete=models.SET_NULL, null=True, blank=True)
    page_number_origin = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(default=1)

    def __str__(self):
        return f"Misconception: {self.description[:50]}"

# ---------------------------------------------------------------------------
# V3 Pedagogical Engine — Learning Experience Graph
# ---------------------------------------------------------------------------

class LearningExperienceGraph(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    learning_unit = models.ForeignKey(
        LearningUnit, 
        on_delete=models.CASCADE, 
        related_name='learning_experience_graphs'
    )
    generation_job = models.ForeignKey(
        GenerationJob, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='generated_graphs'
    )
    
    version = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    # The actual pedagogical graph structure
    graph_data = models.JSONField(
        default=dict, 
        help_text="The structured Adaptive Strategy Graph generated by Agent 3."
    )
    
    # Quality Report from Agent 5
    quality_report = models.JSONField(
        default=dict,
        blank=True,
        help_text="The Validation and Quality Engine report (Validation results, Quality score, Optimizations)."
    )
    
    # Provenance and metadata
    provenance = models.JSONField(
        default=dict, 
        blank=True, 
        help_text="Metadata tracking the knowledge chunks used to build this graph."
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-version']

    def __str__(self):
        return f"LX Graph v{self.version} for {self.learning_unit}"

# ---------------------------------------------------------------------------
# V4 Adaptive Runtime Engine — Student Session Tracking
# ---------------------------------------------------------------------------

class LearningSession(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learning_sessions')
    graph = models.ForeignKey(
        LearningExperienceGraph,
        on_delete=models.CASCADE,
        related_name='learning_sessions'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    mastery_score = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session {self.id} for {self.user.username} on Graph {self.graph.id}"

class RuntimeNodeProgress(models.Model):
    STATUS_CHOICES = [
        ('locked', 'Locked'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('skipped', 'Skipped'),
    ]

    session = models.ForeignKey(LearningSession, on_delete=models.CASCADE, related_name='node_progress')
    node_id = models.CharField(max_length=100)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='locked')
    attempts = models.IntegerField(default=0)
    
    # Telemetry
    elapsed_time_seconds = models.IntegerField(default=0)
    metadata = models.JSONField(default=dict, blank=True, help_text="e.g., hints used, confidence score, raw answers")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        unique_together = ('session', 'node_id')

    def __str__(self):
        return f"Node {self.node_id} ({self.status}) for Session {self.session.id}"

# ---------------------------------------------------------------------------
# Signals (Auto-bootstrap Pedagogy Templates)
# ---------------------------------------------------------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Subject)
def create_default_pedagogy_template(sender, instance, created, **kwargs):
    """
    Ensure every new Subject automatically gets a default Pedagogy Template.
    This prevents the Content Studio from throwing a 'No active PedagogyTemplate' error,
    allowing the administrator to immediately generate lessons from an empty database.
    """
    if kwargs.get('raw', False):
        return
    if created:
        template = PedagogyTemplate.objects.create(
            subject=instance,
            name=f"Standard Lesson Template ({instance.name})",
            description="Auto-generated default pedagogy structure.",
            is_active=True
        )

        rules = [
            ("introduction", 1, True, "Generate an engaging hook and clearly state the learning objectives.", {}),
            ("concept_explanation", 2, True, "Explain the core concepts simply and clearly.", {}),
            ("visual_learning", 3, True, "Provide detailed descriptions for any visual diagrams or charts.", {}),
            ("knowledge_check", 4, False, "Create 3 multiple choice questions to test understanding.", {}),
            ("summary", 5, True, "Summarize the key takeaways of the lesson.", {})
        ]

        for block_type, order, is_mandatory, prompt, schema in rules:
            GenerationRule.objects.create(
                template=template,
                block_type=block_type,
                order=order,
                is_mandatory=is_mandatory,
                system_prompt=prompt,
                validation_schema=schema
            )


# ---------------------------------------------------------------------------
# Interactive Simulation Registry Models
# ---------------------------------------------------------------------------

class SubjectDomain(models.TextChoices):
    CHEMISTRY = 'CHEMISTRY', 'Chemistry'
    PHYSICS = 'PHYSICS', 'Physics'
    BIOLOGY = 'BIOLOGY', 'Biology'
    MATHEMATICS = 'MATHEMATICS', 'Mathematics'


class SimulationStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    IN_DEVELOPMENT = 'IN_DEVELOPMENT', 'In Development'
    PLACEHOLDER = 'PLACEHOLDER', 'Placeholder'


class Simulation(models.Model):
    key = models.CharField(max_length=100, unique=True, db_index=True, help_text="Unique identifier key (e.g. charles_law)")
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=50, choices=SubjectDomain.choices, default=SubjectDomain.CHEMISTRY)
    topic = models.CharField(max_length=255, help_text="e.g., Gas Laws, Electrochemistry")
    status = models.CharField(max_length=50, choices=SimulationStatus.choices, default=SimulationStatus.PLACEHOLDER)
    description = models.TextField(blank=True, null=True, help_text="Brief pedagogical overview")
    archetype = models.CharField(max_length=100, help_text="Client-side component identifier")
    config = models.JSONField(default=dict, blank=True, help_text="Initial parameters and telemetry specs")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['subject', 'status', 'title']

    def __str__(self):
        return f"[{self.get_subject_display()}] {self.title} ({self.get_status_display()})"

