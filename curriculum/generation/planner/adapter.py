from curriculum.models import LessonBlock, Lesson, LearningExperienceGraph

class Agent4AdapterStub:
    """
    TEMPORARY: Provides a bridging mechanism to visualize the output of Agent 3
    in the existing legacy VLearn Lesson Viewer.
    
    This flattens the LearningExperienceGraph by doing a simple traversal
    and generating basic `concept_explanation` LessonBlocks.
    
    WARNING: This is a hack for backward compatibility. Do NOT rely on this
    structure. Agent 4 will completely replace this adapter.
    """
    
    @staticmethod
    def flatten_to_legacy_blocks(lesson: Lesson, graph: LearningExperienceGraph) -> None:
        plan = graph.graph_data
        nodes = plan.get('nodes', [])
        entry_node_id = plan.get('entry_node_id')
        
        if not nodes or not entry_node_id:
            return
            
        node_dict = {n.get('node_id'): n for n in nodes}
        
        # Flatten via BFS to get a mostly logical linear flow for the viewer
        visited = set()
        queue = [entry_node_id]
        linear_nodes = []
        
        while queue:
            current_id = queue.pop(0)
            if current_id in visited or current_id not in node_dict:
                continue
                
            visited.add(current_id)
            node = node_dict[current_id]
            linear_nodes.append(node)
            
            for next_id in node.get('next_nodes', []):
                if next_id not in visited:
                    queue.append(next_id)
        
        # Clear existing blocks
        LessonBlock.objects.filter(lesson=lesson).delete()
        
        for idx, node in enumerate(linear_nodes):
            intent = node.get('instructional_intent', {})
            content_str = (
                f"**Pedagogical Node: {node.get('node_type', 'unknown').upper()}**\\n\\n"
                f"**Learning Moment:** {intent.get('learning_moment', 'N/A')}\\n\\n"
                f"**Goal:** {intent.get('student_goal', 'N/A')}\\n\\n"
                f"**Content:**\\n{node.get('content', '')}\\n\\n"
                f"*(Agent 4 will later transform this abstract node into interactive UI elements)*"
            )
            
            LessonBlock.objects.create(
                lesson=lesson,
                block_type='concept_explanation',
                title=f"Step {idx + 1}: {node.get('node_id')}",
                content={'text': content_str},
                order=idx,
                page_number=idx + 1,
                page_title=node.get('node_id').replace('_', ' ').title(),
                component_type='concept_explanation',
                component_order=1
            )
