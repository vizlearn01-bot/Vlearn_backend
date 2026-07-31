from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from Resources.permissions import HasActiveSubscription
from django.shortcuts import get_object_or_404

from curriculum.models import LearningExperienceGraph, LearningSession
from curriculum.runtime.engine import RuntimeEngine
from curriculum.runtime.exceptions import GraphExecutionError

class RuntimeSessionViewSet(viewsets.ViewSet):
    """
    API for Adaptive Runtime Execution.
    Handles starting a session, fetching state, and submitting node results.
    """
    permission_classes = [HasActiveSubscription]

    @action(detail=False, methods=['post'])
    def start(self, request):
        """Starts a learning session for a given LearningExperienceGraph."""
        graph_id = request.data.get('graph_id')
        if not graph_id:
            return Response({"error": "graph_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        graph = get_object_or_404(LearningExperienceGraph, id=graph_id, status='published')

        try:
            session = RuntimeEngine.start_session(request.user, graph)
            state = RuntimeEngine.get_current_state(session)
            return Response(state, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def state(self, request, pk=None):
        """Returns the current state of a learning session (including active node)."""
        session = get_object_or_404(LearningSession, id=pk, user=request.user)
        state = RuntimeEngine.get_current_state(session)
        return Response(state, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """
        Submits the result for an active node, triggering graph traversal.
        Payload expects:
        {
            "node_id": "...",
            "result": {
                "passed": true/false,
                "score": 100,
                "elapsed_time_seconds": 45,
                "metadata": {}
            }
        }
        """
        session = get_object_or_404(LearningSession, id=pk, user=request.user)
        node_id = request.data.get('node_id')
        result = request.data.get('result', {})

        if not node_id:
            return Response({"error": "node_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            state = RuntimeEngine.submit_node_result(session, node_id, result)
            return Response(state, status=status.HTTP_200_OK)
        except GraphExecutionError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Internal Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
