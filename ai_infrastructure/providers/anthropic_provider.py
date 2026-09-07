import json
import time
import logging as std_logging
from typing import Any, Dict, List, Optional, Generator

from ai_infrastructure.providers.base import AbstractAIProvider
from ai_infrastructure import config, exceptions

logger = std_logging.getLogger("ai_infrastructure")

try:
    import anthropic
    from anthropic import Anthropic, APIStatusError, APITimeoutError, RateLimitError
except ImportError as e:
    raise ImportError(
        "anthropic package is required to use AnthropicProvider. "
        "Install it via: pip install anthropic"
    ) from e


class AnthropicProvider(AbstractAIProvider):
    """
    Anthropic Claude provider implementation.
    Structured output uses a tool-calling trick: the schema is provided as a
    single tool definition and the model is forced to call it, yielding
    reliable JSON output that is then parsed into the Pydantic model.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = (api_key or config.ANTHROPIC_API_KEY or "").strip()
        if not self.api_key:
            raise exceptions.ProviderError(
                "Anthropic API key is not set. Please add ANTHROPIC_API_KEY to your environment."
            )
        self.client = Anthropic(api_key=self.api_key)
        self.default_model = config.LLM_MODEL or config.DEFAULT_ANTHROPIC_MODEL
        logger.info("Initializing AnthropicProvider (model: %s)", self.default_model)

    def _execute_with_retry(self, func, *args, **kwargs):
        retry_limit = config.DEFAULT_RETRY_LIMIT
        backoff = config.DEFAULT_RETRY_BACKOFF_FACTOR
        last_exc = None
        for attempt in range(1, retry_limit + 1):
            try:
                return func(*args, **kwargs)
            except (RateLimitError, APITimeoutError) as e:
                last_exc = e
                logger.warning(
                    "Anthropic transient error on attempt %d/%d: %s", attempt, retry_limit, e
                )
                if attempt == retry_limit:
                    break
                time.sleep(backoff ** attempt)
            except APIStatusError as e:
                raise exceptions.ProviderError(f"Anthropic API error: {e}", e)
            except Exception as e:
                raise exceptions.ProviderError(f"Unexpected error calling Anthropic: {e}", e)
        raise exceptions.ProviderError(
            f"Anthropic call failed after {retry_limit} attempts: {last_exc}", last_exc
        )

    def generate(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 8192,
        **kwargs,
    ) -> str:
        model = model_name or self.default_model
        kwargs_msg: dict = {"model": model, "max_tokens": max_output_tokens, "temperature": temperature}
        if system_instruction:
            kwargs_msg["system"] = system_instruction
        kwargs_msg["messages"] = [{"role": "user", "content": prompt}]

        def _call():
            response = self.client.messages.create(**kwargs_msg)
            return response.content[0].text if response.content else ""

        return self._execute_with_retry(_call)

    def generate_structured(
        self,
        prompt: str,
        response_schema: Any,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> Any:
        """
        Structured generation via tool-use forcing.
        Claude is asked to call a single tool whose input_schema mirrors the
        Pydantic model's JSON schema, guaranteeing structured JSON output.
        """
        model = model_name or self.default_model

        # Build the tool definition from the Pydantic schema
        if hasattr(response_schema, "model_json_schema"):
            schema = response_schema.model_json_schema()
        else:
            schema = {"type": "object"}

        tool_def = {
            "name": "structured_response",
            "description": "Return the structured response matching the required schema.",
            "input_schema": schema,
        }

        call_kwargs: dict = {
            "model": model,
            "max_tokens": 8192,
            "temperature": temperature,
            "tools": [tool_def],
            "tool_choice": {"type": "tool", "name": "structured_response"},
            "messages": [{"role": "user", "content": prompt}],
        }
        if system_instruction:
            call_kwargs["system"] = system_instruction

        def _call():
            response = self.client.messages.create(**call_kwargs)
            for block in response.content:
                if block.type == "tool_use" and block.name == "structured_response":
                    data = block.input
                    if hasattr(response_schema, "model_validate"):
                        return response_schema.model_validate(data)
                    return data
            raise exceptions.ProviderError(
                "Anthropic structured response: no tool_use block found in response."
            )

        return self._execute_with_retry(_call)

    def generate_stream(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> Generator[str, None, None]:
        model = model_name or self.default_model
        call_kwargs: dict = {
            "model": model,
            "max_tokens": 8192,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system_instruction:
            call_kwargs["system"] = system_instruction

        with self.client.messages.stream(**call_kwargs) as stream:
            for text in stream.text_stream:
                yield text

    def start_chat(
        self,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        history: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> "AnthropicChatSession":
        model = model_name or self.default_model
        return AnthropicChatSession(
            self.client, model, system_instruction or "", list(history or []), temperature
        )


class AnthropicChatSession:
    """Stateful chat session wrapper for Anthropic."""

    def __init__(
        self,
        client: "Anthropic",
        model: str,
        system: str,
        history: list,
        temperature: float,
    ):
        self._client = client
        self._model = model
        self._system = system
        self._history = history
        self._temperature = temperature

    def send_message(self, message: str, **kwargs) -> str:
        self._history.append({"role": "user", "content": message})
        call_kwargs: dict = {
            "model": self._model,
            "max_tokens": 8192,
            "temperature": self._temperature,
            "messages": self._history,
        }
        if self._system:
            call_kwargs["system"] = self._system
        response = self._client.messages.create(**call_kwargs)
        reply = response.content[0].text if response.content else ""
        self._history.append({"role": "assistant", "content": reply})
        return reply

    def get_history(self) -> List[Dict[str, Any]]:
        return list(self._history)
