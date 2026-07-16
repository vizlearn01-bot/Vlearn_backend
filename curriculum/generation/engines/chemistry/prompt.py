"""
curriculum/generation/engines/chemistry/prompt.py

Assembles the Learning Experience Designer prompt for the Chemistry pipeline.

Responsibilities
----------------
- Inject curriculum context.
- Inject repository chunks as raw factual material.
- Apply the MASTER_CHEMISTRY_PROMPT as the governing instructional philosophy.
- Return a single string ready for LLMClient.generate().
"""

# ---------------------------------------------------------------------------
# Chunk formatting helper (Reused concept, modified for Chemistry)
# ---------------------------------------------------------------------------

def _format_chunk_section(heading: str, hint: str, chunks: list) -> str:
    """Return a formatted repository section string, or '' if no usable chunks."""
    if not chunks:
        return ''
    lines = [f"\n--- {heading} ---", f"[Instruction: {hint}]"]
    for c in chunks:
        page = c.get('pages') or 'n/a'
        content = (c.get('content') or '').strip()
        if content and content != '[Image/Diagram]':
            lines.append(f"[Page {page}] {content}")
        elif content == '[Image/Diagram]':
            img = c.get('image_url', 'no-url')
            lines.append(f"[Page {page}] Diagram available at: {img}")
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Master Chemistry System Prompt
# ---------------------------------------------------------------------------

MASTER_CHEMISTRY_PROMPT = """\
You are a senior Chemistry Instructional Designer building a VLearn Learning Experience.
You are NOT writing a textbook. You are NOT taking notes. You are NOT summarising.
You are creating a highly engaging chemistry lesson tailored for Kenyan students.

Your ONLY responsibility is deciding HOW students learn this material.
The repository tells you WHAT. You decide the instructional steps, pacing, and media.

════════════════════════════════════════════════════════
 PRIME DIRECTIVE
════════════════════════════════════════════════════════
You must output a structured Learning Experience Blueprint. 
You must think in terms of "Learning Experiences" and "Instructional Steps", not pages or paragraphs.

Every Learning Experience must answer ONE question:
  "How do I make the student understand this specific chemistry concept deeply?"

════════════════════════════════════════════════════════
 THE CHEMISTRY PROGRESSION
════════════════════════════════════════════════════════
A highly effective chemistry learning experience typically flows as follows:

  1. Hook (Draw them in with a surprising chemical fact or phenomenon)
  2. Learning Objective (Clear, active goal)
  3. Core Explanation (The minimum viable chemistry theory)
  4. Scientific Visualization (Request a specific diagram or animation of the molecules/process)
  5. Kenyan Real-World Example (Connect the chemistry to local life, agriculture, or industry)
  6. Interactive Simulation (Suggest a virtual lab or simulation for discovery)
  7. Worked Example (Step-by-step problem solving, e.g., stoichiometry or balancing equations)
  8. Misconception (Address a common misunderstanding in chemistry)
  9. Knowledge Check (Verify understanding)
  10. Summary & Key Takeaways

Not every step is mandatory for every concept. Use the steps that best serve the specific chemistry topic being taught.

════════════════════════════════════════════════════════
 INSTRUCTIONAL STEP VOCABULARY
════════════════════════════════════════════════════════
Use ONLY these `step_purpose` values:

hook
  {"step_purpose": "hook", "content": "Surprising fact or question to start."}
learning_objective
  {"step_purpose": "learning_objective", "content": "By the end of this you will..."}
core_explanation
  {"step_purpose": "core_explanation", "content": "Clear, concise theory (max 4 sentences)."}
scientific_visualization
  {"step_purpose": "scientific_visualization", "designer_brief": "Detailed instruction for an illustrator on what molecules/process to draw."}
kenyan_real_world_example
  {"step_purpose": "kenyan_real_world_example", "content": "Relate the chemistry to a Kenyan context (e.g., Lake Magadi, agriculture, local industry)."}
required_media
  {"step_purpose": "required_media", "designer_brief": "Brief for a video or specific image needed."}
interactive_simulation
  {"step_purpose": "interactive_simulation", "designer_brief": "Describe the variables the student should manipulate in a virtual lab."}
worked_example
  {"step_purpose": "worked_example", "title": "Example", "content": "Step 1... Step 2..."}
misconception
  {"step_purpose": "misconception", "content": "Students often think X, but actually Y because Z."}
knowledge_check
  {"step_purpose": "knowledge_check", "check_type": "multiple_choice | true_false | short_answer", "question": "...", "options": ["A","B","C","D"], "answer": "A"}
reflection
  {"step_purpose": "reflection", "content": "Pause and think..."}
summary
  {"step_purpose": "summary", "content": "• Point 1\\n• Point 2"}
ai_tutor_context
  {"step_purpose": "ai_tutor_context", "content": "Hidden context for the AI tutor to help students with this specific concept."}
completion_takeaway
  {"step_purpose": "completion_takeaway", "content": "The single most important thing to remember."}

════════════════════════════════════════════════════════
 REQUIRED JSON STRUCTURE
════════════════════════════════════════════════════════
{
  "lesson_title": "Engaging lesson title",
  "learning_experiences": [
    {
      "concept_title": "Name of the core concept",
      "cognitive_load": "low | medium | high",
      "instructional_steps": [
        // Sequence of instructional step objects
      ]
    }
  ]
}

════════════════════════════════════════════════════════
 GROUNDING RULES — NON-NEGOTIABLE
════════════════════════════════════════════════════════
- Base EVERY core scientific fact on the Repository Content provided below.
- You MUST invent the Kenyan real-world examples, analogies, and hooks to teach these facts.
- Do NOT pad explanations to hit a word count. Keep explanations concise.
- ALWAYS return a valid JSON object. No markdown fences, no explanation.
"""

def build_chemistry_prompt(context_package: dict) -> str:
    """
    Build the full instructional-designer prompt for Chemistry.

    Parameters
    ----------
    context_package : dict
        Output of RetrievalService.assemble_context().

    Returns
    -------
    str
        A single prompt string ready for LLMClient.generate().
    """
    chunks = context_package.get('chunks', {})
    parts: list = []

    parts.append(MASTER_CHEMISTRY_PROMPT.strip())
    parts.append('')

    # Curriculum context
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" CURRICULUM CONTEXT")
    parts.append("════════════════════════════════════════════════════════")
    parts.append(f"Curriculum    : {context_package.get('curriculum', 'Unknown')}")
    parts.append(f"Grade         : {context_package.get('grade', 'Unknown')}")
    parts.append(f"Subject       : {context_package.get('subject', 'Unknown')} (CHEMISTRY FOCUS)")
    parts.append(f"Topic         : {context_package.get('topic', 'Unknown')}")
    parts.append(f"Learning Unit : {context_package.get('learning_unit', 'Unknown')}")
    parts.append('')

    # Repository content
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" REPOSITORY CONTENT (your ONLY factual source)")
    parts.append("════════════════════════════════════════════════════════")

    s = _format_chunk_section(
        "CORE TEXT",
        "Translate this factual text into a learning experience progression.",
        chunks.get('core_text', []),
    )
    if s: parts.append(s)

    s = _format_chunk_section(
        "DEFINITIONS",
        "Integrate these into the core explanation or as a dedicated step.",
        chunks.get('definitions', []),
    )
    if s: parts.append(s)

    s = _format_chunk_section(
        "WORKED EXAMPLES",
        "Transform these into interactive worked_example steps.",
        chunks.get('worked_examples', []),
    )
    if s: parts.append(s)

    s = _format_chunk_section(
        "DIAGRAMS & FIGURES",
        "Request these via scientific_visualization steps.",
        chunks.get('diagrams', []),
    )
    if s: parts.append(s)

    s = _format_chunk_section(
        "PRACTICALS / EXPERIMENTS",
        "Convert into interactive_simulation or scientific_visualization briefs.",
        chunks.get('practicals', []),
    )
    if s: parts.append(s)

    s = _format_chunk_section(
        "ASSESSMENT QUESTIONS",
        "Adapt into knowledge_check steps.",
        chunks.get('exercises', []),
    )
    if s: parts.append(s)

    return '\n'.join(parts)
