from typing import Any, List, Optional, Dict
from ai_infrastructure.contracts.base import BaseModel, Field

class ComponentBlueprintSchema(BaseModel):
    """Pydantic schema representing a single learning component in a lesson blueprint."""
    type: str = Field(..., description="Type of learning component (e.g., learning_goal, concept_explanation, etc.)")
    content: Optional[Any] = Field(None, description="The primary textual content or dictionary structure of the component")
    title: Optional[str] = Field(None, description="Optional component title")
    check_type: Optional[str] = Field(None, description="Type of knowledge check (e.g., multiple_choice, true_false)")
    options: Optional[List[str]] = Field(None, description="Options for multiple choice questions")
    answer: Optional[Any] = Field(None, description="Answer key for assessments")
    term: Optional[str] = Field(None, description="Glossary term for definitions")
    formula: Optional[str] = Field(None, description="Equation formula string")
    
    # Suggested media parameters (brief fields)
    purpose: Optional[str] = Field(None, description="Pedagogical objective of the suggested asset")
    instruction: Optional[str] = Field(None, description="Brief instructing how the media should look/be structured")
    designer_brief: Optional[str] = Field(None, description="Brief for chemistry media steps")
    avoid: Optional[str] = Field(None, description="Things the media creator should avoid")
    priority: Optional[str] = Field(None, description="Priority rank (high/medium/low)")
    labels: Optional[List[str]] = Field(None, description="Labels that should appear in the diagram")
    duration: Optional[str] = Field(None, description="Suggested video duration")
    variables: Optional[List[str]] = Field(None, description="Variables to expose in interactive simulation")
    expected_discovery: Optional[str] = Field(None, description="Outcome user discovers in simulation")
    materials: Optional[List[str]] = Field(None, description="Materials list for activity")
    expected_outcome: Optional[str] = Field(None, description="Result of executing activity")
    admin_instruction: Optional[str] = Field(None, description="Admin instruction slot text")


class PageBlueprintSchema(BaseModel):
    """Pydantic schema representing a single card/page in a lesson blueprint."""
    title: str = Field(..., description="Title of the page/concept")
    primary_concept: Optional[str] = Field(None, description="Single primary concept taught on this page")
    difficulty: Optional[str] = Field(None, description="Pacing difficulty (foundation/core/advanced/revision)")
    reading_time_minutes: Optional[float] = Field(None, description="Calculated duration to complete page")
    visual_importance: Optional[str] = Field(None, description="Importance of visual elements")
    reading_load: Optional[str] = Field(None, description="Text intensity of the page")
    builds_on: Optional[str] = Field(None, description="Reference to predecessor concept page")
    prepares_for: Optional[str] = Field(None, description="Reference to successor concept page")
    importance: Optional[str] = Field(None, description="Degree of relevance (core/supporting/enrichment)")
    components: List[ComponentBlueprintSchema] = Field(default_factory=list, description="Sequence of components forming the page")


class LessonBlueprintSchema(BaseModel):
    """Pydantic schema representing a complete compiled instructional lesson blueprint."""
    lesson_title: Optional[str] = Field(None, description="Overarching title of the lesson")
    pages: List[PageBlueprintSchema] = Field(default_factory=list, description="List of pages in correct pedagogical sequence")
