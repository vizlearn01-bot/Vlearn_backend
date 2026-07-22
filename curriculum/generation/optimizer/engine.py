import json
from curriculum.generation.planner.models import LearningExperiencePlan
from ai_infrastructure.di import get_ai_provider

def build_optimizer_prompt(plan: LearningExperiencePlan) -> str:
    plan_json = plan.model_dump_json(indent=2)
    return f"""
    You are the Optimization Engine for the VLearn Learning Compiler.
    Your job is to optimize the wording, pacing, and clarity of the provided Learning Experience Plan.
    
    CRITICAL RULES:
    1. NEVER add or remove any strategy nodes. The 'nodes' list length and 'node_id's must remain identical.
    2. NEVER alter the graph structure (do not change 'next_nodes', 'entry_node_id', or transitions).
    3. NEVER change the pedagogical intent ('node_type', 'success_criteria', 'failure_criteria').
    
    You MAY:
    1. Improve, compress, or clarify the 'content' strings for better reading load and pacing.
    2. Enhance the 'instructional_intent' descriptions to be more actionable.
    3. Provide a list of qualitative 'recommendations' explaining what you improved.
    
    Output exactly in JSON matching the LearningExperiencePlan schema, but add a top-level "recommendations" list of strings explaining your changes.
    
    PLAN TO OPTIMIZE:
    {plan_json}
    """

class OptimizerEngine:
    """
    Agent 5: Optional LLM Optimization Pass.
    """
    
    @staticmethod
    def optimize(plan: LearningExperiencePlan) -> tuple[LearningExperiencePlan, list[str]]:
        provider = get_ai_provider()
        prompt = build_optimizer_prompt(plan)
        
        # We ask for a raw response because we want to extract the extra "recommendations" field
        # before validating against the strict LearningExperiencePlan schema.
        try:
            raw_response = provider.generate(prompt)
            import re
            clean_response = re.sub(r'^```(?:json)?\s*|\s*```$', '', raw_response.strip(), flags=re.MULTILINE)
            plan_dict = json.loads(clean_response)
            
            recommendations = plan_dict.pop('recommendations', [])
            optimized_plan = LearningExperiencePlan(**plan_dict)
            
            # Re-validation: ensure optimizer didn't change structure
            original_nodes = {n.node_id for n in plan.nodes}
            optimized_nodes = {n.node_id for n in optimized_plan.nodes}

            if original_nodes != optimized_nodes:
                raise ValueError("Optimizer illegally added or removed nodes.")

            for orig, opt in zip(
                sorted(plan.nodes, key=lambda n: n.execution_order),
                sorted(optimized_plan.nodes, key=lambda n: n.execution_order),
            ):
                # execution_order must not change — it defines traversal sequence
                if orig.execution_order != opt.execution_order:
                    raise ValueError(
                        f"Optimizer illegally modified execution_order on node {orig.node_id} "
                        f"({orig.execution_order} -> {opt.execution_order})."
                    )
                if orig.node_type != opt.node_type:
                    raise ValueError(f"Optimizer illegally modified node_type on node {orig.node_id}.")

            return optimized_plan, recommendations
            
        except Exception as e:
            # If optimization fails or violates structural rules, fallback to original plan
            print(f"Optimization failed or rejected: {e}")
            return plan, [f"Optimization failed: {str(e)}"]
