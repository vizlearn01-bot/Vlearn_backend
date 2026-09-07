from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator

from curriculum.generation.planner.models import LearningExperiencePlan

# ---------------------------------------------------------------------------
# AGENT 4 CONTRACTS
# ---------------------------------------------------------------------------

class VisualSpecification(BaseModel):
    visual_format: Optional[str] = Field(default="scientific_diagram", description="Visual format (e.g. 'scientific_diagram', 'process_flowchart', 'comparison_graphic', 'sequential_animation').")
    subject_focus: Optional[str] = Field(default="", description="Primary objects or structures to depict.")
    spatial_layout_and_perspective: Optional[str] = Field(default="Standard frontal view", description="Camera angle, viewpoint, or cross-section perspective.")
    key_labels: Optional[List[str]] = Field(default_factory=list, description="Required anatomical, step, or key-value labels.")
    color_emphasis: Optional[str] = Field(default="Default palette", description="Color highlighting guidance for visual hierarchy.")
    style_guidelines: Optional[str] = Field(default="Clean vector style", description="Style guidelines for visual production.")
    
    # Enhanced Pedagogical Specification Fields
    invisible_mechanism: Optional[str] = Field(default=None, description="The hidden physical, microscopic, or logical process being revealed.")
    targeted_misconception: Optional[str] = Field(default=None, description="The specific misbelief or false mental model this visual refutes.")
    guided_attention_target: Optional[str] = Field(default=None, description="EXACTLY what feature or change the learner must observe and notice.")
    temporal_sequence: Optional[List[str]] = Field(default_factory=list, description="High-level educational stages (e.g. ['Initial State', 'Transformation', 'Outcome']) for process diagrams, animations, or videos.")

    @field_validator('visual_format', 'subject_focus', 'spatial_layout_and_perspective', 'color_emphasis', 'style_guidelines', mode='before')
    @classmethod
    def sanitize_strings(cls, v):
        return v if v is not None else ""

    @field_validator('key_labels', 'temporal_sequence', mode='before')
    @classmethod
    def sanitize_lists(cls, v):
        return v if v is not None else []

class MediaRequirement(BaseModel):
    node_id: str = Field(default="", description="The strategy node this media is for.")
    is_required: bool = Field(default=False, description="True if media is required for this step.")
    preferred_media_type: str = Field(default="image", description="E.g., 'image', 'video', 'simulation', 'diagram'.")
    fallback_media_type: Optional[str] = Field(default=None, description="Fallback type if preferred is unavailable.")
    media_category: Optional[str] = Field(default="Reference Material", description="Category like 'Abstract Visualization', 'Real-world Visualization', etc.")
    educational_purpose: Optional[str] = Field(default="", description="Why this media is needed (e.g., 'To visualize the atomic structure').")
    accessibility_requirements: Optional[str] = Field(default="", description="Description of what alt text or captions must convey.")
    visual_spec: Optional[VisualSpecification] = Field(default=None, description="Detailed visual specification for generative/retrieval engines.")
    search_keywords: Optional[List[str]] = Field(default_factory=list, description="Keywords for the acquisition engine to use.")
    entity_name: Optional[str] = Field(default=None, description="The primary concept or entity name.")
    scientific_name: Optional[str] = Field(default=None, description="Scientific or formal name if applicable.")
    aliases: Optional[List[str]] = Field(default_factory=list, description="Alternate names or synonyms.")
    related_concepts: Optional[List[str]] = Field(default_factory=list, description="Related terms to aid search.")

    @field_validator('accessibility_requirements', 'educational_purpose', 'preferred_media_type', 'media_category', mode='before')
    @classmethod
    def sanitize_strings(cls, v):
        return v if v is not None else ""

    @field_validator('is_required', mode='before')
    @classmethod
    def sanitize_bool(cls, v):
        return bool(v) if v is not None else False

    @field_validator('search_keywords', 'aliases', 'related_concepts', mode='before')
    @classmethod
    def sanitize_lists(cls, v):
        return v if v is not None else []

class MediaManifest(BaseModel):
    """
    Output of the Media Planner (Module 1).
    """
    requirements: List[MediaRequirement] = Field(default_factory=list)

class ResolvedAsset(BaseModel):
    """
    Output of the Acquisition Engine (Module 2).
    """
    node_id: str
    asset_type: str = Field(description="The actual media type resolved.")
    url: Optional[str] = Field(default=None, description="URL or embed code of the asset.")
    file_path: Optional[str] = Field(default=None, description="Local file path if applicable.")
    provenance: str = Field(description="Source origin (e.g., 'Wikimedia', 'KnowledgeRepository', 'Teacher').")
    licensing: str = Field(description="License type (e.g., 'CC-BY-SA', 'Proprietary').")
    alt_text: str = Field(description="Accessibility text.")
    confidence_score: float = Field(ge=0.0, le=1.0, description="How confident the engine is that this asset matches the requirement.")
    fallback_used: bool = Field(default=False, description="True if the preferred type was unavailable.")
    knowledge_chunk_id: Optional[int] = Field(default=None, description="ID of the KnowledgeChunk if sourced from the repository.")
    source: str = Field(default="Unknown", description="Source platform or origin.")
    provider: str = Field(default="Unknown", description="The provider engine used to retrieve this asset.")
    verified: bool = Field(default=False, description="Whether this asset has been verified for accuracy.")
    author: Optional[str] = Field(default=None, description="Author or creator of the asset.")
    attribution: Optional[str] = Field(default=None, description="Required attribution text.")
    generation_method: Optional[str] = Field(default=None, description="Method used if generated (e.g., 'gemini-2.5-pro').")
    created_at: Optional[str] = Field(default=None, description="Timestamp of creation or retrieval.")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional structured metadata.")

class ExperiencePackage(BaseModel):
    """
    Output of Experience Assembly (Module 3).
    A bundled payload containing the immutable pedagogical plan and the resolved assets.
    """
    plan: LearningExperiencePlan
    resolved_assets: List[ResolvedAsset] = Field(default_factory=list)
