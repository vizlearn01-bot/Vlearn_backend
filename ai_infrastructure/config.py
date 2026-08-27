import os

# Centralized AI configurations
# Reads from environment variables, providing sensible defaults

# ---------------------------------------------------------------------------
# API Keys
# ---------------------------------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# ---------------------------------------------------------------------------
# Provider selection — set LLM_PROVIDER to switch backends env-only.
# Supported values: 'gemini' (default) | 'openai' | 'anthropic'
# ---------------------------------------------------------------------------
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini").lower()

# Optional model override per provider.
# Leave blank to use each provider's sensible default.
LLM_MODEL = os.getenv("LLM_MODEL", "")

# Per-provider default models (used when LLM_MODEL is not set)
DEFAULT_GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
DEFAULT_OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
DEFAULT_ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")

SUPPORTED_MODELS = {
    "gemini-flash": "gemini-flash-latest",
    "gemini-pro": "gemini-pro-latest",
    "gemini-1.5-flash": "gemini-1.5-flash-latest",
    "gemini-1.5-pro": "gemini-1.5-pro",
    "gemini-2.5-pro": "gemini-2.5-pro",
    "gemini-3.5-flash": "gemini-3.5-flash",
    "gemini-3.1-flash-lite": "gemini-3.1-flash-lite",
}

# ---------------------------------------------------------------------------
# Timeout / Retry settings
# ---------------------------------------------------------------------------
DEFAULT_TIMEOUT_SECONDS = int(os.getenv("AI_TIMEOUT_SECONDS", "30"))
DEFAULT_RETRY_LIMIT = int(os.getenv("AI_RETRY_LIMIT", "3"))
DEFAULT_RETRY_BACKOFF_FACTOR = float(os.getenv("AI_RETRY_BACKOFF_FACTOR", "2.0"))

# ---------------------------------------------------------------------------
# SDK / Logging Feature Flags
# ---------------------------------------------------------------------------
USE_NEW_GENAI_SDK = os.getenv("AI_USE_NEW_SDK", "True").lower() == "true"
ENABLE_LOGGING_PAYLOADS = os.getenv("AI_LOG_PAYLOADS", "True").lower() == "true"

# ---------------------------------------------------------------------------
# Curriculum Feature Flags
# ---------------------------------------------------------------------------
# Controls whether the AI-ingestion upload mode is available in the UI.
ENABLE_AI_INGESTION_MODE = os.getenv("ENABLE_AI_INGESTION_MODE", "True").lower() == "true"

# Controls whether the new component-based lesson editor is shown.
# Default False so existing Content Studio stays unchanged until ready.
ENABLE_COMPONENT_EDITOR = os.getenv("ENABLE_COMPONENT_EDITOR", "False").lower() == "true"
