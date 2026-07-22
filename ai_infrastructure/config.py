import os

# Centralized AI configurations
# Reads from environment variables, providing sensible defaults

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# AI Model Configuration
DEFAULT_GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
SUPPORTED_MODELS = {
    "gemini-flash": "gemini-flash-latest",
    "gemini-pro": "gemini-pro-latest",
    "gemini-1.5-flash": "gemini-1.5-flash-latest",
    "gemini-1.5-pro": "gemini-1.5-pro",
    "gemini-2.5-pro": "gemini-2.5-pro",
    "gemini-3.5-flash": "gemini-3.5-flash",
    "gemini-3.1-flash-lite": "gemini-3.1-flash-lite",
}

# Timeout settings (in seconds)
DEFAULT_TIMEOUT_SECONDS = int(os.getenv("AI_TIMEOUT_SECONDS", "30"))

# Retry settings
DEFAULT_RETRY_LIMIT = int(os.getenv("AI_RETRY_LIMIT", "3"))
DEFAULT_RETRY_BACKOFF_FACTOR = float(os.getenv("AI_RETRY_BACKOFF_FACTOR", "2.0"))

# Feature Flags
USE_NEW_GENAI_SDK = os.getenv("AI_USE_NEW_SDK", "True").lower() == "true"
ENABLE_LOGGING_PAYLOADS = os.getenv("AI_LOG_PAYLOADS", "True").lower() == "true"
