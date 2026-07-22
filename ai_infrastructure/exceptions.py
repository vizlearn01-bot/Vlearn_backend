class AIError(Exception):
    """Base exception class for all AI infrastructure errors."""
    def __init__(self, message: str, original_exception: Exception = None):
        super().__init__(message)
        self.message = message
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{self.message} (Caused by: {self.original_exception})"
        return self.message


class ProviderError(AIError):
    """Exception raised when an AI provider returns an error (e.g., rate limits, API key issue)."""
    pass


class ValidationError(AIError):
    """Exception raised when structured model inputs or outputs fail validation."""
    pass


class ParsingError(AIError):
    """Exception raised when the LLM response format fails to parse into the desired structure (e.g., malformed JSON)."""
    pass


class TimeoutError(AIError):
    """Exception raised when an AI request times out."""
    pass


class RetryError(AIError):
    """Exception raised when all retry attempts fail."""
    pass
