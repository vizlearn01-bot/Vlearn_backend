from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class AbstractAIService(ABC):
    """Base class for any service wrapping AI capabilities."""
    pass


class AbstractPipelineStage(ABC):
    """Represents a discrete stage in the compiler pipeline."""
    
    @abstractmethod
    def execute(self, context: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Run the logic of this specific compiler stage."""
        pass


class AbstractOrchestrator(ABC):
    """Orchestrates multiple compilation stages into an end-to-end flow."""
    
    @abstractmethod
    def execute_job(self, job_id: int) -> None:
        """Run the end-to-end compiler job."""
        pass


class AbstractValidator(ABC):
    """Validates the output of a stage or generator against constraints."""
    
    @abstractmethod
    def validate(self, data: Any, schema: Optional[Any] = None) -> bool:
        """Return True if data conforms to constraints, False otherwise."""
        pass


class AbstractCache(ABC):
    """Abstractions for caching results to reduce API requests and cost."""
    
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        pass
        
    @abstractmethod
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        pass


class AbstractMonitor(ABC):
    """Abstractions for tracking latency, metrics, and compilation status."""
    
    @abstractmethod
    def record_metric(self, name: str, value: float, tags: Optional[Dict[str, str]] = None) -> None:
        pass
