import json
import time
import logging as std_logging
from typing import Any, Dict, List, Optional, Generator
from ai_infrastructure.providers.base import AbstractAIProvider
from ai_infrastructure import config, exceptions, logging as ai_logging

# Configure loggers
logger = std_logging.getLogger("ai_infrastructure")

# Attempt importing new GenAI SDK
try:
    from google import genai
    from google.genai import types
except ImportError:
    raise ImportError("google-genai is not installed. Please run: pip install google-genai")


class GeminiChatSession:
    """Unified wrapper for a stateful Chat session across SDK versions."""
    def __init__(self, chat_session: Any):
        self._chat = chat_session

    def send_message(self, message: str, **kwargs) -> str:
        """Send a message to the chat session and return response text."""
        try:
            response = self._chat.send_message(message, **kwargs)
            return response.text
        except Exception as e:
            raise exceptions.ProviderError("Error during chat send_message", e)

    def get_history(self) -> List[Dict[str, Any]]:
        """Retrieve the message history of the chat."""
        history = []
        for message in self._chat.get_history():
            history.append({
                "role": message.role,
                "parts": [{"text": part.text} for part in message.parts]
            })
        return history


class GeminiProvider(AbstractAIProvider):
    """
    Gemini AI Provider implementation.
    Transparently shifts between the new google-genai SDK (Interactions API) and
    the legacy google-generativeai SDK based on availability in the environment.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or config.GEMINI_API_KEY
        if not self.api_key:
            raise exceptions.ProviderError(
                "Gemini API Key is not set. Please add GEMINI_API_KEY to your environment."
            )
        
        logger.info("Initializing GeminiProvider using the Google GenAI SDK client.")
        self.client = genai.Client(api_key=self.api_key)

    def _execute_with_retry(self, func, *args, **kwargs):
        retry_limit = config.DEFAULT_RETRY_LIMIT
        backoff = config.DEFAULT_RETRY_BACKOFF_FACTOR
        
        last_exc = None
        for attempt in range(1, retry_limit + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exc = e
                # Check for timeout signature
                err_msg = str(e).lower()
                if "deadline" in err_msg or "timeout" in err_msg or "timed out" in err_msg:
                    logger.warning(f"Timeout occurred on attempt {attempt}/{retry_limit}.")
                
                if attempt == retry_limit:
                    break
                
                sleep_duration = backoff ** attempt
                logger.warning(
                    f"Attempt {attempt}/{retry_limit} failed. Retrying in {sleep_duration}s. Reason: {e}"
                )
                time.sleep(sleep_duration)
                
        # Classify final exception
        if "deadline" in str(last_exc).lower() or "timeout" in str(last_exc).lower():
            raise exceptions.TimeoutError("Gemini operation timed out", last_exc)
        raise exceptions.RetryError(f"Gemini operation failed after {retry_limit} retries", last_exc)

    def generate(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 8192,
        **kwargs
    ) -> str:
        model = model_name or config.DEFAULT_GEMINI_MODEL
        start_time = ai_logging.log_request(model, prompt, {"temperature": temperature})
        
        try:
            gen_config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
            )
            def call_new_sdk():
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=gen_config
                )
                return response.text or ""
            
            result = self._execute_with_retry(call_new_sdk)
                
            ai_logging.log_response(model, start_time, result, success=True)
            return result
        except Exception as e:
            ai_logging.log_response(model, start_time, "", success=False, error=str(e))
            if isinstance(e, exceptions.AIError):
                raise e
            raise exceptions.ProviderError("Error executing Gemini text generation", e)

    def generate_structured(
        self,
        prompt: str,
        response_schema: Any,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Any:
        model = model_name or config.DEFAULT_GEMINI_MODEL
        start_time = ai_logging.log_request(model, prompt, {"temperature": temperature, "structured": True})
        
        try:
            # If using Pydantic schema, extract schema dictionary or class
            schema_name = getattr(response_schema, "__name__", "StructuredSchema")
            
            gen_config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature,
                response_mime_type="application/json",
                response_schema=response_schema
            )
            def call_new_sdk_structured():
                print(f"DEBUG: Calling Gemini SDK with model {model}...")
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=gen_config
                )
                print(f"DEBUG: SDK returned successfully!")
                return response.text or ""
            
            raw_json = self._execute_with_retry(call_new_sdk_structured)
            
            ai_logging.log_response(model, start_time, raw_json, success=True)
            
            # Parse response JSON
            try:
                parsed_dict = json.loads(raw_json)
            except json.JSONDecodeError as je:
                raise exceptions.ParsingError(f"Failed to parse JSON response from model: {raw_json[:200]}", je)
            
            # Map back to Pydantic if it is a Pydantic model and HAS_PYDANTIC is active
            if hasattr(response_schema, "model_validate"):
                try:
                    return response_schema.model_validate(parsed_dict)
                except Exception as ve:
                    raise exceptions.ValidationError(f"Response validation against {schema_name} failed", ve)
            
            return parsed_dict
            
        except Exception as e:
            ai_logging.log_response(model, start_time, "", success=False, error=str(e))
            if isinstance(e, exceptions.AIError):
                raise e
            raise exceptions.ProviderError("Error executing Gemini structured generation", e)

    def generate_stream(
        self,
        prompt: str,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        model = model_name or config.DEFAULT_GEMINI_MODEL
        ai_logging.log_request(model, prompt, {"temperature": temperature, "streaming": True})
        
        try:
            gen_config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature,
            )
            response_stream = self.client.models.generate_content_stream(
                model=model,
                contents=prompt,
                config=gen_config
            )
            for chunk in response_stream:
                yield chunk.text or ""
        except Exception as e:
            raise exceptions.ProviderError("Error during streaming generation", e)

    def start_chat(
        self,
        model_name: Optional[str] = None,
        system_instruction: Optional[str] = None,
        history: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> GeminiChatSession:
        model = model_name or config.DEFAULT_GEMINI_MODEL
        
        try:
            # Convert history format if necessary
            sdk_history = []
            if history:
                for item in history:
                    sdk_history.append(types.Content(
                        role=item.get("role", "user"),
                        parts=[types.Part.from_text(text=p.get("text", "")) for p in item.get("parts", [])]
                    ))
            
            chat_config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature
            )
            chat = self.client.chats.create(model=model, history=sdk_history, config=chat_config)
            return GeminiChatSession(chat)
        except Exception as e:
            raise exceptions.ProviderError("Failed to initialize stateful chat session", e)
