from django.utils import timezone
from curriculum.models import LearningSession, RuntimeNodeProgress, LearningExperienceGraph
from .exceptions import NodeNotFoundError, InvalidTransitionError

class RuntimeEngine:
    """
    Deterministic Graph Execution Engine.
    Handles traversal of the LearningExperienceGraph based on student results.
    """
    
    @staticmethod
    def start_session(user, graph: LearningExperienceGraph) -> LearningSession:
        """Starts a new learning session for the given graph."""
        session, created = LearningSession.objects.get_or_create(
            user=user,
            graph=graph,
            defaults={'status': 'active'}
        )
        
        # If it's a new session or an active one with no progress, init the first node
        if created or not session.node_progress.exists():
            plan = graph.graph_data
            entry_node_id = plan.get('entry_node_id')
            if not entry_node_id:
                raise ValueError("Graph has no entry_node_id.")
                
            RuntimeNodeProgress.objects.create(
                session=session,
                node_id=entry_node_id,
                status='active'
            )
        
        return session

    @staticmethod
    def get_current_state(session: LearningSession) -> dict:
        """Returns the current active node and session status."""
        active_nodes = session.node_progress.filter(status='active').order_by('-updated_at')
        active_node = active_nodes.first() if active_nodes.exists() else None
        
        return {
            'session_id': session.id,
            'status': session.status,
            'active_node_id': active_node.node_id if active_node else None,
            'mastery_score': session.mastery_score
        }
        
    @staticmethod
    def submit_node_result(session: LearningSession, node_id: str, result: dict) -> dict:
        """
        Processes a node result (e.g., pass/fail), updates progress, 
        and calculates the next node.
        
        result dict should contain:
        - passed (bool)
        - score (float)
        - elapsed_time_seconds (int)
        - metadata (dict)
        """
        if session.status != 'active':
            raise InvalidTransitionError("Cannot submit results to an inactive session.")
            
        try:
            progress = session.node_progress.get(node_id=node_id, status='active')
        except RuntimeNodeProgress.DoesNotExist:
            raise InvalidTransitionError(f"Node {node_id} is not active in this session.")
            
        # 1. Evaluate result
        passed = result.get('passed', True)
        progress.status = 'completed' if passed else 'failed'
        progress.attempts += 1
        
        elapsed_time = result.get('elapsed_time_seconds', 0)
        progress.elapsed_time_seconds += elapsed_time
        
        meta = progress.metadata or {}
        meta['last_result'] = result
        progress.metadata = meta
        progress.save()
        
        # 2. Determine next node based on graph topology
        plan = session.graph.graph_data
        nodes = plan.get('nodes', [])
        node_dict = {n.get('node_id'): n for n in nodes}
        
        current_node = node_dict.get(node_id)
        if not current_node:
            raise NodeNotFoundError(f"Node {node_id} not found in graph data.")
            
        next_nodes = current_node.get('next_nodes', [])
        next_node_id = None
        
        if not next_nodes:
            # End of graph
            session.status = 'completed'
            session.completed_at = timezone.now()
            session.save()
        elif len(next_nodes) == 1:
            # Linear progression
            next_node_id = next_nodes[0]
        else:
            # Branching logic: deterministic evaluation
            # If passed -> take the first branch (success path)
            # else take the second branch (remediation path)
            if passed:
                next_node_id = next_nodes[0]
            else:
                next_node_id = next_nodes[1] if len(next_nodes) > 1 else next_nodes[0]
                
        # 3. Create active state for next node
        if next_node_id:
            if next_node_id not in node_dict:
                raise NodeNotFoundError(f"Target node {next_node_id} not found.")
                
            # Create or update next node to 'active'
            next_progress, created = RuntimeNodeProgress.objects.get_or_create(
                session=session,
                node_id=next_node_id,
                defaults={'status': 'active'}
            )
            
            if not created and next_progress.status != 'active':
                next_progress.status = 'active'
                next_progress.save()
            
        return RuntimeEngine.get_current_state(session)
