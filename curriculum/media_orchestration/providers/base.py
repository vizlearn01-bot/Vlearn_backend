from abc import ABC, abstractmethod
from typing import List
from curriculum.media_orchestration.contracts import ResolvedAsset
from curriculum.media_orchestration.search_intelligence.models import SearchPayload

class BaseProvider(ABC):
    """
    Interface for external and internal asset providers.
    """
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Name of the provider (e.g., 'Wikimedia Commons')"""
        pass

    @abstractmethod
    def search(self, payload: SearchPayload, node_id: str) -> List[ResolvedAsset]:
        """
        Executes a search based on the provided SearchPayload.
        Returns a list of candidate ResolvedAssets.
        """
        pass
