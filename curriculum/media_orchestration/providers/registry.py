from typing import List
from .base import BaseProvider
from .internal import KnowledgeRepoProvider, SimulationProvider
from .wikimedia import WikimediaProvider
from .youtube import YouTubeProvider

class ProviderRegistry:
    """
    Maintains available providers and routes search payloads to them.
    """
    def __init__(self):
        self.providers: List[BaseProvider] = [
            KnowledgeRepoProvider(),
            SimulationProvider(),
            YouTubeProvider(),
            WikimediaProvider()
        ]
        
    def register(self, provider: BaseProvider):
        self.providers.append(provider)

    def get_providers(self) -> List[BaseProvider]:
        return self.providers
