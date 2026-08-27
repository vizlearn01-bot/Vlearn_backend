"""
LLMFactory — provider-agnostic LLM resolution.

Reads `LLM_PROVIDER` from the environment and returns the matching
`AbstractAIProvider` singleton. All curriculum generation code should use
`LLMFactory.get_provider()` instead of calling `get_ai_provider()` directly.

Supported providers (set via LLM_PROVIDER env var):
  gemini     — Google Gemini (default, always available)
  openai     — OpenAI GPT family (requires OPENAI_API_KEY + `pip install openai`)
  anthropic  — Anthropic Claude family (requires ANTHROPIC_API_KEY + `pip install anthropic`)
"""
import logging
from ai_infrastructure import config
from ai_infrastructure.providers.base import AbstractAIProvider

logger = logging.getLogger("ai_infrastructure")

# Singleton cache keyed by provider name
_provider_cache: dict = {}


class LLMFactory:
    """
    Factory that resolves the active LLM provider from environment configuration.
    Call `LLMFactory.get_provider()` anywhere instead of `get_ai_provider()`.
    """

    @staticmethod
    def get_provider(provider_name: str | None = None) -> AbstractAIProvider:
        """
        Return a cached provider instance.

        Args:
            provider_name: Override the env-configured provider for this call.
                           If None, reads `config.LLM_PROVIDER`.

        Returns:
            An `AbstractAIProvider` instance.

        Raises:
            ValueError: If the requested provider name is not recognised.
        """
        name = (provider_name or config.LLM_PROVIDER).lower()

        if name in _provider_cache:
            return _provider_cache[name]

        provider = LLMFactory._create(name)
        _provider_cache[name] = provider
        logger.info("LLMFactory: resolved provider '%s'", name)
        return provider

    @staticmethod
    def _create(name: str) -> AbstractAIProvider:
        if name == "gemini":
            from ai_infrastructure.providers.gemini import GeminiProvider
            return GeminiProvider()

        if name == "openai":
            from ai_infrastructure.providers.openai_provider import OpenAIProvider
            return OpenAIProvider()

        if name == "anthropic":
            from ai_infrastructure.providers.anthropic_provider import AnthropicProvider
            return AnthropicProvider()

        raise ValueError(
            f"Unknown LLM provider '{name}'. "
            "Set LLM_PROVIDER to one of: gemini, openai, anthropic."
        )

    @staticmethod
    def reset() -> None:
        """Clear the singleton cache (useful for tests)."""
        _provider_cache.clear()
