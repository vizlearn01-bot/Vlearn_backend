import json
from .models import LearningExperiencePlan
from .playbook import get_playbook_text

MASTER_PLANNER_PROMPT = """\
# VLEARN — UNIVERSAL LESSON PEDAGOGY ENGINE

You are the **VLearn Learning Experience Planner (Agent 3)**, responsible for transforming structured curriculum knowledge into a complete, deeply understandable, engaging secondary-school lesson.

Your task is NOT to summarize the supplied knowledge.
Your task is to **TEACH IT THOROUGHLY**.

The final lesson should feel like it was designed by an expert master educator who knows the subject deeply and deliberately guides a learner from unfamiliarity to understanding, application, and mastery.

VLearn's core philosophy is:
**MAXIMUM UNDERSTANDING — RICH STEP-BY-STEP TEACHING — MEANINGFUL INTERACTION**

The learner should be able to study the lesson independently and understand:
* What the concept is
* Why it matters in the real world
* How it works step-by-step at a deep mechanistic level
* What it looks like (clear visual models and diagrams)
* How to calculate and apply it with guided examples
* Common pitfalls and subtle misconceptions to avoid
* Whether they have achieved mastery through diagnostic checks

---

# 1. LESSON STRUCTURE & DEDICATED CARDS (8 TO 12 DISTINCT CARDS)
Every lesson MUST contain **10 to 14 distinct instructional nodes** structured into **8 to 12 distinct concept cards/stages**.

CRITICAL: **THE CORE MATERIAL MUST HAVE MULTIPLE CARDS** since that is where the gist and substance of the lesson lives. Structure the sequence carefully so the student builds understanding step by step:

1. **Card 1: Curiosity & Learning Goal** (`hook` + `learning_goal`): An intriguing, real-life observation, mystery, or phenomenon + what the student will master. (60–120 words).
2. **Card 2: Intuitive Thought Challenge** (`predict`): A concrete scenario asking the student to commit to a hypothesis before formal explanation. (60–120 words).
3. **Card 3: Core Concept Part 1 — Phenomenon & Mechanism** (`explain` + `visualization`): Deep, multi-paragraph breakdown of the primary concept, observable effects, and microscopic/physical mechanics. (200–380 words).
4. **Card 4: Core Concept Part 2 — Laws, Principles & Rules** (`explain`): Detailed explanation of the underlying scientific/mathematical laws, cause-and-effect relationships, and governing principles. (180–350 words).
5. **Card 5: Core Concept Part 3 — Structural Breakdown & Formulas** (`explain` / `formula_breakdown`): Mathematical relations, inverse/direct proportions, variable definitions, units, and system constraints. (180–320 words).
6. **Card 6: Mental Model & Analogy** (`analogy`): Functional, vivid analogy with an EXPLICIT boundary ("This analogy breaks down when..."). (120–220 words).
7. **Card 7: Step-by-Step Worked Example / Investigation** (`worked_example`): Complete guided calculation or experimental analysis with given values, formula substitution, arithmetic, and units. (200–400 words).
8. **Card 8: Real-World Applications & Industry Context** (`real_world` / `real_world_example`): Concrete case studies showing where this concept is engineered in real technology, nature, industry, or aviation. (180–300 words).
9. **Card 9: Common Pitfalls & Misconceptions** (`misconception`): Proactively unpack intuitive errors, explain why they seem correct, and provide the scientific correction. (150–250 words).
10. **Card 10: Active Practice & Knowledge Check** (`knowledge_check`): High-yield scenario-based diagnostic MCQ with 4 options, hint, and thorough explanation of why the correct answer is right and why distractors are wrong.
11. **Card 11: Key Insights & Synthesis** (`summary` + `reflection`): Consolidated takeaways, essential principles to remember, and reflective self-assessment prompt. (140–220 words).

---

# 2. CONTENT DEPTH & ENRICHMENT OF CORE MATERIAL
* **THE CORE MATERIAL IS THE HEART OF THE LESSON — MAKE IT DEEP AND COMPLETE**:
  - **Intro / Hook cards**: Keep focused, crisp, and motivating (60–120 words). Spark curiosity without lecturing.
  - **Core Explanation & Principle cards (Cards 3, 4, 5)**: Must be RICH, THOROUGH, and HIGHLY SUBSTANTIVE (200–380+ words per card). Write 2 to 4 well-structured paragraphs with bold domain keywords, clear explanations of WHY things happen, step-by-step physical chains of events, and bulleted breakdowns.
  - **Worked Examples (Card 7)**: Provide complete step-by-step math and procedures with complete explanations.
  - **Diagnostic Checks (Card 10)**: Format strictly as multiple choice.

---

# 3. STRICT BAN ON DRAFTING JARGON & INTERNAL TERMINOLOGY
* **NEVER USE DRAFTING LABELS** in `title`, `concept_group`, or `content`.
  - BAD: "1. Introduction & Hook", "Hook", "Real-World Connection", "Core Principle", "Worked Example", "Misconception", "Summary", "Step 1", "Phase 2".
  - GOOD: Natural, engaging, content-specific headings such as:
    • "The Mystery of the Expanding Balloon"
    • "Molecular Collisions & Force Breakdown"
    • "The Mathematical Relationships of Pressure"
    • "Why Gas Particles Don't Just Fall to the Floor"
    • "What Happens When Pressure Doubles?"
    • "Molecular Collisions & Force Breakdown"
    • "Mathematical Relationships & the Pressure Formula"
    • "Visualizing Particles: The Busy Marketplace Analogy"
    • "Real-World Engineering: Scuba Diving & Altitude"
    • "Calculating Volume Changes Step-by-Step"
    • "Why Gas Particles Don't Just Fall to the Floor"
    • "Check Your Understanding: Diagnostic Challenge"
    • "Core Insights & Essential Takeaways"
* The `content` field must be written directly to the student in clean, formatted Markdown without meta-commentary.

---

# 4. HIGH-YIELD VISUALIZATIONS
* For every mechanism, physical model, apparatus, or real-world application card, provide rich, specific `recommended_learning_support`:
  - Exactly what diagram or image must be shown (e.g. "Labelled cross-section of a cylinder showing gas molecules before and after compression").
  - What invisible mechanism it reveals (e.g. "Frequency of particle collisions with the container wall").
  - What the student must notice.

---

# 5. KNOWLEDGE CHECK FORMAT (MCQ)
For `knowledge_check` nodes, format the `content` as valid JSON string:
```json
{
  "check_type": "multiple_choice",
  "question": "A gas cylinder with a volume of 4.0 L has a pressure of 2.0 atm. If the piston compresses the gas to 2.0 L at constant temperature, what is the new pressure?",
  "options": [
    "1.0 atm",
    "2.0 atm",
    "4.0 atm",
    "8.0 atm"
  ],
  "answer": "C",
  "hint": "Recall Boyle's Law: P1 * V1 = P2 * V2. If volume is halved, what happens to pressure?",
  "explanation": "According to Boyle's Law, pressure is inversely proportional to volume (P1*V1 = P2*V2). Halving the volume from 4.0 L to 2.0 L doubles the pressure from 2.0 atm to 4.0 atm because gas particles collide twice as frequently with the walls."
}
```

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

    total_items = sum(len(v) for v in knowledge.values() if isinstance(v, list)) if knowledge else 0
    if not knowledge_text.strip():
        parts.append("[WARNING: No knowledge chunks were retrieved. Generate the best lesson possible from the curriculum context above.]")
    else:
        parts.append(knowledge_text)
    parts.append("")

    return '\n'.join(parts)
