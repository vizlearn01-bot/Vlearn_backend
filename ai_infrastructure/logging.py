import logging
import threading
import uuid
import time
from typing import Any, Dict
from ai_infrastructure import config

# Thread-local storage to track trace IDs across execution contexts
_thread_local = threading.local()

logger = logging.getLogger("ai_infrastructure")

def get_trace_id() -> str:
    """Retrieve the current thread's trace ID, generating one if not set."""
    if not hasattr(_thread_local, "trace_id") or not _thread_local.trace_id:
        _thread_local.trace_id = str(uuid.uuid4())
    return _thread_local.trace_id

def set_trace_id(trace_id: str) -> None:
    """Set the trace ID for the current thread context."""
    _thread_local.trace_id = trace_id

def clear_trace_id() -> None:
    """Clear the trace ID for the current thread context."""
    if hasattr(_thread_local, "trace_id"):
        del _thread_local.trace_id

def log_request(model_name: str, prompt: str, parameters: Dict[str, Any] = None) -> float:
    """Log an outgoing LLM request and return the start timestamp."""
    trace_id = get_trace_id()
    start_time = time.time()
    
    extra = {
        "trace_id": trace_id,
        "model_name": model_name,
        "parameters": parameters or {},
    }
    
    if config.ENABLE_LOGGING_PAYLOADS:
        logger.info(
            f"[AI_REQ] [{trace_id}] Model: {model_name} | Prompt (first 200 chars): {prompt[:200]!r}...",
            extra=extra
        )
    else:
        logger.info(
            f"[AI_REQ] [{trace_id}] Model: {model_name} (Payload logging disabled)",
            extra=extra
        )
        
    return start_time

def log_response(model_name: str, start_time: float, response_text: str, success: bool, error: str = None) -> None:
    """Log the incoming LLM response and calculate duration."""
    duration = time.time() - start_time
    trace_id = get_trace_id()
    
    extra = {
        "trace_id": trace_id,
        "model_name": model_name,
        "duration_ms": int(duration * 1000),
        "success": success,
        "error": error
    }
    
    status_str = "SUCCESS" if success else "FAILED"
    if success:
        if config.ENABLE_LOGGING_PAYLOADS:
            logger.info(
                f"[AI_RESP] [{trace_id}] {status_str} in {duration:.3f}s | Response (first 200 chars): {response_text[:200]!r}...",
                extra=extra
            )
        else:
            logger.info(
                f"[AI_RESP] [{trace_id}] {status_str} in {duration:.3f}s",
                extra=extra
            )
    else:
        logger.error(
            f"[AI_RESP] [{trace_id}] {status_str} in {duration:.3f}s | Error: {error}",
            extra=extra
        )
