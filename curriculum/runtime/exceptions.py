class GraphExecutionError(Exception):
    """Base exception for runtime graph execution errors."""
    pass

class NodeNotFoundError(GraphExecutionError):
    """Raised when a referenced node ID is not found in the graph."""
    pass

class InvalidTransitionError(GraphExecutionError):
    """Raised when an attempted transition from a node is invalid."""
    pass
