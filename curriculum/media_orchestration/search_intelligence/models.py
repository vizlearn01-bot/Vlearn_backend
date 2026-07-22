from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class SearchPayload(BaseModel):
    """
    Standardized payload for executing searches across diverse providers.
    Constructed deterministically by the QueryBuilder.
    """
    primary_query: str = Field(description="The main search query to execute (often Entity Name or Scientific Name).")
    alternate_queries: List[str] = Field(default_factory=list, description="Fallback queries if the primary query yields no results.")
    entity_type: Optional[str] = Field(default=None, description="Type of entity being searched (e.g., 'animal', 'chemical', 'historical_figure').")
    preferred_media_category: str = Field(description="The requested media category (e.g., 'Real-world Visualization').")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Any specific filters, such as license type, orientation, or resolution minimums.")
    is_suitable_for_wikimedia: bool = Field(default=False, description="Whether this request is suitable for Wikimedia Commons retrieval.")
