from ai_infrastructure.di import get_ai_provider
from ai_infrastructure.config import DEFAULT_GEMINI_MODEL

class LLMClient:
    """
    Modular abstraction for the AI model.
    Connects to Gemini API for lesson generation via the new AI Infrastructure layer.
    """
    @staticmethod
    def generate(prompt: str, model_name: str = DEFAULT_GEMINI_MODEL) -> str:
        # Resolve AI Provider using Dependency Injection
        provider = get_ai_provider()
        return provider.generate(prompt, model_name=model_name)

    @staticmethod
    def generate_structured(prompt: str, response_schema: type, model_name: str = DEFAULT_GEMINI_MODEL) -> any:
        provider = get_ai_provider()
        return provider.generate_structured(prompt, response_schema=response_schema, model_name=model_name)
