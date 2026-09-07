import json
import time
import logging as std_logging
from typing import Any, Dict, List, Optional, Generator

from ai_infrastructure.providers.base import AbstractAIProvider
from ai_infrastructure import config, exceptions

logger = std_logging.getLogger("ai_infrastructure")

try:
    from openai import OpenAI
    from openai import APIError, RateLimitError, APITimeoutError
except ImportError as e:
    raise ImportError(
        "openai package is required to use OpenAIProvider. "
        "Install it via: pip install openai"
    ) from e


class OpenAIProvider(AbstractAIProvider):
    """
    OpenAI provider implementation.
    Uses the Chat Completions API. Structured output is achieved via
    JSON mode (response_format={"type": "json_object"}) plus Pydantic parsing.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = (api_key or config.OPENAI_API_KEY or "").strip()
        if not self.api_key:
            raise exceptions.ProviderError(
                "OpenAI API key is not set. Please add OPENAI_API_KEY to your environment."
            )
        self.client = OpenAI(api_key=self.api_key)
        self.default_model = config.LLM_MODEL or config.DEFAULT_OPENAI_MODEL
        logger.info("Initializing OpenAIProvider (model: %s)", self.default_model)

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
                    "OpenAI transient error on attempt %d/%d: %s", attempt, retry_limit, e
                )
                if attempt == retry_limit:
                    break
                time.sleep(backoff ** attempt)
            except APIError as e:
                raise exceptions.ProviderError(f"OpenAI API error: {e}", e)
            except Exception as e:
                raise exceptions.ProviderError(f"Unexpected error calling OpenAI: {e}", e)
        raise exceptions.ProviderError(
            f"OpenAI call failed after {retry_limit} attempts: {last_exc}", last_exc
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
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        def _call():
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_output_tokens,
            )
            return response.choices[0].message.content or ""

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
        Generate structured output. Uses JSON mode + Pydantic model_validate.
        The prompt must instruct the model to return valid JSON matching the schema.
        """
        model = model_name or self.default_model
        schema_hint = ""
        if hasattr(response_schema, "model_json_schema"):
            schema_hint = f"\n\nRespond ONLY with a valid JSON object matching this schema:\n{json.dumps(response_schema.model_json_schema(), indent=2)}"

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction + schema_hint})
        else:
            messages.append({"role": "system", "content": "You are a helpful assistant." + schema_hint})
        messages.append({"role": "user", "content": prompt})

        def _call():
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                response_format={"type": "json_object"},
            )
            raw = response.choices[0].message.content or "{}"
            data = json.loads(raw)
            if hasattr(response_schema, "model_validate"):
                return response_schema.model_validate(data)
            return data

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
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        stream = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    def start_chat(
        self,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        history: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> "OpenAIChatSession":
        model = model_name or self.default_model
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        if history:
            messages.extend(history)
        return OpenAIChatSession(self.client, model, messages, temperature)


class OpenAIChatSession:
    """Stateful chat session wrapper for OpenAI."""

    def __init__(self, client: "OpenAI", model: str, history: list, temperature: float):
        self._client = client
        self._model = model
        self._history = history
        self._temperature = temperature

    def send_message(self, message: str, **kwargs) -> str:
        self._history.append({"role": "user", "content": message})
        response = self._client.chat.completions.create(
            model=self._model,
            messages=self._history,
            temperature=self._temperature,
        )
        reply = response.choices[0].message.content or ""
        self._history.append({"role": "assistant", "content": reply})
        return reply

    def get_history(self) -> List[Dict[str, Any]]:
        return list(self._history)
