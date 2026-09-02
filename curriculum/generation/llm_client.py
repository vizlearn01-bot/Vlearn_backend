from typing import Optional
from ai_infrastructure.llm_factory import LLMFactory


class LLMClient:
    """
    Thin wrapper around LLMFactory.
    All curriculum generation code that used get_ai_provider() directly should
    either call LLMClient.generate / generate_structured, or use
    LLMFactory.get_provider() for advanced usage (streaming, chat sessions, etc.).
    """

    @staticmethod
    def generate(prompt: str, model_name: Optional[str] = None) -> str:
        provider = LLMFactory.get_provider()
        return provider.generate(prompt, model_name=model_name)

    @staticmethod
    def generate_structured(prompt: str, response_schema: type, model_name: Optional[str] = None) -> any:
        provider = LLMFactory.get_provider()
        return provider.generate_structured(prompt, response_schema=response_schema, model_name=model_name)

