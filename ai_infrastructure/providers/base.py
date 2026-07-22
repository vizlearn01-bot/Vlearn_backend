from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Generator

class AbstractAIProvider(ABC):
    """
    Abstract interface for AI Providers.
    Any LLM backend (e.g., Gemini, OpenAI, Claude) must implement this interface.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 8192,
        **kwargs
    ) -> str:
        """
        Execute a standard stateless text generation request.
        """
        pass

    @abstractmethod
    def generate_structured(
        self,
        prompt: str,
        response_schema: Any,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Any:
        """
        Execute a request expecting structured output corresponding to a schema (Pydantic model or Dict).
        """
        pass

    @abstractmethod
    def generate_stream(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Stream the text generation output chunk by chunk.
        """
        pass

    @abstractmethod
    def start_chat(
        self,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        history: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Any:
        """
        Start a stateful interaction (chat session) with the model.
        """
        pass
