"""
curriculum/generation/blueprint_prompt.py

Assembles the instructional-designer prompt for the V2 Blueprint pipeline.

Responsibilities
----------------
- Inject curriculum context (Curriculum -> Grade -> Subject -> Topic -> LearningUnit).
- Inject repository chunks as raw factual material the AI must stay grounded in,
  with pedagogical intent hints to guide the instructional-designer persona.
- Apply the MASTER_SKELETON_PROMPT from skeleton.py as the governing philosophy.
- Return a single string ready for LLMClient.generate().

This module does NOT call the LLM directly.
It does NOT touch the database.
It does NOT duplicate any logic from prompting.py (the legacy builder).
"""

from __future__ import annotations
from curriculum.generation.skeleton import MASTER_SKELETON_PROMPT


# ---------------------------------------------------------------------------
# Chunk formatting helper
# ---------------------------------------------------------------------------

def _format_chunk_section(heading: str, hint: str, chunks: list) -> str:
    """
    Return a formatted repository section string, or '' if no usable chunks.

    Parameters
    ----------
    heading : str   Section label shown to the LLM.
    hint    : str   Pedagogical instruction: how the AI should USE these chunks.
    chunks  : list  Raw chunk dicts from RetrievalService.
    """
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
# Grounding rules — appended after the master prompt, before repo content
# ---------------------------------------------------------------------------

GROUNDING_RULES = (
    "════════════════════════════════════════════════════════\n"
    " CURRICULUM GROUNDING — NON-NEGOTIABLE\n"
    "════════════════════════════════════════════════════════\n"
    "- Base EVERY core scientific/historical fact on the Repository Content below.\n"
    "- You MUST invent analogies, real-world examples, and curiosity-driven questions to teach these facts.\n"
    "- You MUST use progressive disclosure: start with a question or hook, then introduce the concept.\n"
    "- If the repository contains a worked example, adapt it into an engaging step-by-step challenge.\n"
    "- If the repository contains a diagram reference, request it as a\n"
    "  suggested_diagram using its description — do not ignore it.\n"
    "- The AI has FULL creative authority to use metaphors, questions, and reflection prompts to teach.\n"
    "\n"
    "════════════════════════════════════════════════════════\n"
    " PAGE BUDGET RULES\n"
    "════════════════════════════════════════════════════════\n"
    "- Assign pages based on concept complexity, NOT text length.\n"
    "  . Single definition with no dependencies   -> 1 page\n"
    "  . Multi-step process or derivation         -> 2-3 pages\n"
    "  . Complex topic with many sub-concepts     -> 4 pages maximum\n"
    "- Do NOT pad pages to hit a number.\n"
    "- Do NOT create one page per sentence.\n"
)


# ---------------------------------------------------------------------------
# Public prompt builder
# ---------------------------------------------------------------------------

def build_blueprint_prompt(context_package: dict) -> str:
    """
    Build the full instructional-designer prompt.

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

    # 1. Master instructional-design philosophy
    parts.append(MASTER_SKELETON_PROMPT.strip())
    parts.append('')

    # 2. Grounding rules
    parts.append(GROUNDING_RULES.strip())
    parts.append('')

    # 3. Curriculum context
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" CURRICULUM CONTEXT")
    parts.append("════════════════════════════════════════════════════════")
    parts.append(f"Curriculum    : {context_package.get('curriculum', 'Unknown')}")
    parts.append(f"Grade         : {context_package.get('grade', 'Unknown')}")
    parts.append(f"Subject       : {context_package.get('subject', 'Unknown')}")
    parts.append(f"Topic         : {context_package.get('topic', 'Unknown')}")
    parts.append(f"Learning Unit : {context_package.get('learning_unit', 'Unknown')}")
    parts.append('')

    # 4. Repository content with pedagogical intent hints
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" REPOSITORY CONTENT (your ONLY factual source)")
    parts.append("════════════════════════════════════════════════════════")

    s = _format_chunk_section(
        "CORE TEXT",
        "Translate this factual text into a teaching sequence. Use questions, analogies, and progressive disclosure. Do NOT just summarize.",
        chunks.get('core_text', []),
    )
    if s:
        parts.append(s)

    s = _format_chunk_section(
        "DEFINITIONS",
        "Teach these definitions using real-world context before providing the formal definition_card.",
        chunks.get('definitions', []),
    )
    if s:
        parts.append(s)

    s = _format_chunk_section(
        "WORKED EXAMPLES",
        "Transform these into interactive worked_example components. Guide the student through the logic.",
        chunks.get('worked_examples', []),
    )
    if s:
        parts.append(s)

    s = _format_chunk_section(
        "DIAGRAMS & FIGURES",
        "Create a suggested_diagram component for each. Write a precise designer brief.",
        chunks.get('diagrams', []),
    )
    if s:
        parts.append(s)

    s = _format_chunk_section(
        "PRACTICALS / EXPERIMENTS",
        "Convert into suggested_activity or mini_activity with step-by-step instructions.",
        chunks.get('practicals', []),
    )
    if s:
        parts.append(s)

    s = _format_chunk_section(
        "ASSESSMENT QUESTIONS",
        "Adapt into knowledge_check components. Vary check_type across pages.",
        chunks.get('exercises', []),
    )
    if s:
        parts.append(s)

    # 5. Final output instruction
    parts.append('')
    parts.append("════════════════════════════════════════════════════════")
    parts.append(" OUTPUT INSTRUCTION")
    parts.append("════════════════════════════════════════════════════════")
    parts.append(
        "Return ONLY a valid JSON object. No prose. No markdown fences. No explanation.\n"
        "The JSON must match the Required JSON Structure above exactly.\n"
        "\n"
        "Before writing your JSON, run the Self-Verification checklist silently.\n"
        "Revise any page that fails a check before outputting.\n"
        "\n"
        "Required per page:\n"
        "  - At least one concept_explanation (max 4 sentences)\n"
        "  - At least one transition (except the final page)\n"
        "  - At least one knowledge_check on any page with complex content\n"
        "  - reading_time_minutes field calculated using the formula in the prompt\n"
        "  - primary_concept field populated\n"
        "\n"
        "Required for the full lesson:\n"
        "  - Difficulty progression: foundation -> core -> advanced\n"
        "  - At least one analogy or real_world_connection\n"
        "  - knowledge_check types varied across pages\n"
        "  - Attention-recovery component every 3-4 pages if lesson > 4 pages\n"
        "  - Every suggested media component contains a non-generic instruction brief"
    )

    return '\n'.join(parts)
