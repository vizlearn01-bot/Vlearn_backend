import traceback
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from ai_infrastructure.logging import set_trace_id, get_trace_id, clear_trace_id

logger = logging.getLogger("ai_infrastructure")


class AbstractBackgroundTask(ABC):
    """
    Interface for background task logic.
    Standardizes how processing jobs (ingestion, compilation, acquisition)
    are executed and logged with tracking contexts.
    """

    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """Execute the job logic."""
        pass


class TaskTraceContext:
    """
    Context manager that manages trace ID context and exception logging
    for Celery tasks and background workers without spawning unmanaged threads.
    """
    def __init__(self, task_name: str, parent_trace_id: Optional[str] = None):
        self.task_name = task_name
        self.parent_trace_id = parent_trace_id
        self.trace_id = None

    def __enter__(self):
        if self.parent_trace_id:
            set_trace_id(self.parent_trace_id)
        else:
            set_trace_id(get_trace_id())
        self.trace_id = get_trace_id()
        logger.info(f"[TASK] [{self.trace_id}] Starting task: {self.task_name}")
        return self.trace_id

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            stack = "".join(traceback.format_exception(exc_type, exc_val, exc_tb))
            logger.error(
                f"[TASK] [{self.trace_id}] Task failed: {self.task_name} | Error: {exc_val}\n{stack}"
            )
        else:
            logger.info(f"[TASK] [{self.trace_id}] Task completed successfully: {self.task_name}")
        clear_trace_id()
        return False  # Do not suppress exception


class SafeBackgroundTask(AbstractBackgroundTask):
    """
    Base helper class for executing background task logic safely inside Celery workers.
    Provides trace context management and structured error handling.
    Note: Unmanaged thread spawning (execute_in_thread) was deprecated and removed in M2.
    """
    def __init__(self, task_name: str, parent_trace_id: Optional[str] = None):
        self.task_name = task_name
        self.parent_trace_id = parent_trace_id

    def execute(self, *args, **kwargs) -> Any:
        """Executes task logic synchronously within worker task context."""
        with TaskTraceContext(self.task_name, self.parent_trace_id):
            return self.run(*args, **kwargs)
