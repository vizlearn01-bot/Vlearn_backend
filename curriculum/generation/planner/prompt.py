import json
from .models import LearningExperiencePlan
from .playbook import get_playbook_text

MASTER_PLANNER_PROMPT = """\
You are Agent 3: Learning Experience Planner (Pedagogical Engine) for the VLearn Learning Compiler.
Your sole responsibility is converting structured educational knowledge into adaptive, multi-moment learning experiences that match the quality of an expert master educator.

You are NOT responsible for media rendering, UI code, or asset retrieval.
Your focus is strictly on instructional intelligence, cognitive progression, and conceptual clarity.

═══════════════════════════════════════════════════════
 PRIMARY OBJECTIVE
═══════════════════════════════════════════════════════
Design HOW students learn a concept by strictly applying the VLearn Teaching Playbook rules below.

The lesson should feel like an excellent teacher — not a textbook.

Philosophy: Maximum Understanding. Minimum Text. Maximum Interaction.

DO NOT generate walls of text. Each node's `content` MUST be 2-4 sentences maximum.
Instead of long paragraphs, generate: concise observations, short explanations, worked numbers, pointed questions, visual callouts.

═══════════════════════════════════════════════════════
 TRAVERSAL MODEL — SEQUENTIAL EXECUTION ORDER
═══════════════════════════════════════════════════════
Nodes are executed in ascending `execution_order` (1, 2, 3...).
You do NOT need to manually wire next_nodes for normal sequential flow.
Only set is_branch_point=True and populate next_nodes if a node genuinely forks
into adaptive paths (e.g., a practice node that sends struggling students to remediation).

═══════════════════════════════════════════════════════
 MANDATORY INSTRUCTIONAL PROGRESSION
═══════════════════════════════════════════════════════
EVERY lesson MUST contain ALL of the following instructional moment types.
The exact number of nodes scales with topic complexity (set in cognitive_analysis.complexity):

  simple   → 6-8 nodes  (e.g., a single definition or straightforward concept)
  standard → 10-12 nodes (most topics)
  complex  → 13-16 nodes (multi-concept, high abstraction, e.g., Electrochemistry)

Required node types and sequence:
  1.  learning_goal     — What will the student be able to do? One clear sentence.
  2.  hook              — Surprising, concrete phenomenon. One sentence. Create curiosity.
  3.  real_world        — Where does this appear in Kenya / everyday life?
  4.  predict           — Student commits a thought BEFORE being told. Frame as a question.
  5.  explain           — Core explanation. ONE cognitive shift. 2-4 sentences MAXIMUM.
  6.  visualization     — Describe the invisible mechanism that MUST be visualized. (No image yet — describe what the visual should reveal.)
  7.  analogy           — Mental model with EXPLICIT boundary ("This analogy breaks down when...").
  8.  worked_example    — Step-by-step with real numbers/values. Student-facing language.
  9.  misconception     — Common wrong belief → why it seems right → disruption → correction.
 10.  knowledge_check   — One diagnostic question. Tests reasoning/application, NOT recall.
 11.  reflection        — What changed in your thinking today?
 12.  summary           — 3 bullet-point key takeaways. Extremely concise.

For complex topics, add additional explain/observe/practice nodes between steps 5-10.

═══════════════════════════════════════════════════════
 OPERATIONAL INSTRUCTIONS
═══════════════════════════════════════════════════════
1. Conduct a Cognitive Analysis on the topic. Set complexity to 'simple', 'standard', or 'complex'.
2. EXECUTE the Required Delivery Framework provided below and respect its compatible primitives.
3. Set execution_order starting from 1 for the first node, incrementing by 1 for each subsequent node.
4. For EVERY node, specify layout_template matching the framework recommendations.
5. The content field for each node MUST be written directly to the student without meta-commentary, titles, or 'Step X' prefixes.
6. Use an engaging tone, rich analogies (with explicit boundaries), and relatable local Kenyan context.
7. For knowledge_check nodes: set personalization.adaptive_questioning=True. For misconception nodes: set personalization.remediation_available=True.

INSTRUCTIONAL PLAYBOOK RULES:
{playbook_rules}

OUTPUT FORMAT:
You MUST output a single JSON object that perfectly conforms to the following JSON schema. Do NOT wrap it in markdown code blocks. Do NOT include any text outside the JSON object.

JSON SCHEMA:
{schema_json}
"""

def _serialize_knowledge(knowledge: dict) -> str:
    """
    Serializes the categorized knowledge dict into a readable prompt section.
    Handles both structured concept dicts (name+description) and raw chunk dicts (content).
    """
    parts = []
    for category, chunks in knowledge.items():
        if not chunks:
            continue
        parts.append(f"\n--- {category.upper().replace('_', ' ')} ({len(chunks)} items) ---")
        for chunk in chunks:
            chunk_id = chunk.get('id', '?')
            # Structured concept: has 'name' + 'description'
            if 'name' in chunk and 'description' in chunk:
                name = chunk['name']
                desc = chunk['description'] or ''
                keywords = ', '.join(chunk.get('keywords', []))
                text = f"{name}: {desc}"
                if keywords:
                    text += f" [Keywords: {keywords}]"
                parts.append(f"[Item {chunk_id}] {text}")
            # Assessment/misconception: structured with 'description' only
            elif 'description' in chunk:
                text = chunk['description']
                extra = chunk.get('correction') or chunk.get('bloom_level') or ''
                if extra:
                    text += f" → {extra}"
                parts.append(f"[Item {chunk_id}] {text}")
            # Raw chunk: has 'content'
            elif 'content' in chunk:
                parts.append(f"[Chunk {chunk_id}] {chunk['content']}")
    return '\n'.join(parts)


def build_planner_prompt(context_package: dict) -> str:
    """
    Builds the instructional designer prompt for the Learning Experience Planner.
    Injects the pure structured pedagogical context from Agent 2 and the Teaching Playbook.
    """
    schema_json = json.dumps(LearningExperiencePlan.model_json_schema(), indent=2)
    playbook_text = get_playbook_text()
    prompt = MASTER_PLANNER_PROMPT.replace('{playbook_rules}', playbook_text).replace('{schema_json}', schema_json)

    parts = [prompt, ""]

    # Curriculum Context
    meta = context_package.get('metadata', {})
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" CURRICULUM CONTEXT")
    parts.append("════════════════════════════════════════════════════════")
    parts.append(f"Curriculum    : {meta.get('curriculum')}")
    parts.append(f"Grade         : {meta.get('grade')}")
    parts.append(f"Subject       : {meta.get('subject')}")
    parts.append(f"Topic         : {meta.get('topic')}")
    parts.append(f"Learning Unit : {meta.get('learning_unit')}")
    parts.append(f"Description   : {meta.get('learning_unit_description')}")
    parts.append("")

    # Delivery Framework
    framework = context_package.get('framework', {})
    if framework:
        parts.append("════════════════════════════════════════════════════════")
        parts.append(" REQUIRED DELIVERY FRAMEWORK")
        parts.append("════════════════════════════════════════════════════════")
        parts.append(f"Framework Name        : {framework.get('framework_name')}")
        parts.append(f"Learning Archetype    : {framework.get('archetype_category', 'Conceptual Learning')}")
        parts.append(f"Recommended Layout    : {framework.get('recommended_layout_template', 'DiscoveryLayout')}")
        parts.append(f"Cognitive Focus       : {', '.join(framework.get('cognitive_characteristics', []))}")
        parts.append(f"Common Misconceptions : {framework.get('common_misconceptions')}")
        parts.append(f"Assessment Guidance   : {framework.get('assessment_recommendations')}")
        parts.append(f"Personalization       : {framework.get('personalization_opportunities')}")
        parts.append(f"ALLOWED PRIMITIVES    : {', '.join(framework.get('compatible_primitives', []))}")
        parts.append("")
        parts.append("Your lesson MUST use ONLY the Allowed Primitives listed above as the core pedagogical actions for the nodes.")
        parts.append("")

    # Knowledge Context — use correct serializer per category
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" EDUCATIONAL KNOWLEDGE (Your Factual Source — use this to write accurate content)")
    parts.append("════════════════════════════════════════════════════════")

    knowledge = context_package.get('knowledge', {})
    knowledge_text = _serialize_knowledge(knowledge)

    total_items = sum(len(v) for v in knowledge.items() if isinstance(v, list)) if knowledge else 0
    if not knowledge_text.strip():
        parts.append("[WARNING: No knowledge chunks were retrieved. Generate the best lesson possible from the curriculum context above.]")
    else:
        parts.append(knowledge_text)
    parts.append("")

    return '\n'.join(parts)
