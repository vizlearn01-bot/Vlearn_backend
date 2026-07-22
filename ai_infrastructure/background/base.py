import threading
import traceback
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from ai_infrastructure.logging import set_trace_id, get_trace_id, clear_trace_id

logger = logging.getLogger("ai_infrastructure")

class AbstractBackgroundTask(ABC):
    """
    Interface for background tasks.
    Standardizes how asynchronous processing jobs (ingestion, compilation, acquisition)
    are invoked and logged with tracking contexts.
    """

    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """Execute the job logic."""
        pass


class SafeBackgroundTask(AbstractBackgroundTask):
    """
    Standard base implementation for executing tasks safely in background threads.
    Generates/manages trace context and intercepts any uncaught failures.
    """
    def __init__(self, task_name: str, parent_trace_id: Optional[str] = None):
        self.task_name = task_name
        self.parent_trace_id = parent_trace_id

    def execute_in_thread(self, *args, **kwargs) -> threading.Thread:
        """Spawns a daemon thread executing this background task."""
        thread = threading.Thread(target=self._run_wrapper, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    def _run_wrapper(self, *args, **kwargs) -> Any:
        # Set trace ID context
        if self.parent_trace_id:
            set_trace_id(self.parent_trace_id)
        else:
            set_trace_id(get_trace_id())
            
        trace_id = get_trace_id()
        logger.info(f"[BG_TASK] [{trace_id}] Starting background task: {self.task_name}")
        
        try:
            result = self.run(*args, **kwargs)
            logger.info(f"[BG_TASK] [{trace_id}] Background task completed successfully: {self.task_name}")
            return result
        except Exception as e:
            stack = traceback.format_exc()
            logger.error(
                f"[BG_TASK] [{trace_id}] Background task failed: {self.task_name} | Error: {e}\n{stack}"
            )
            self.on_failure(e, trace_id)
            raise e
        finally:
            clear_trace_id()

    def on_failure(self, exception: Exception, trace_id: str) -> None:
        """Callback hooked when the background run throws an exception. Override in subclasses."""
        pass
