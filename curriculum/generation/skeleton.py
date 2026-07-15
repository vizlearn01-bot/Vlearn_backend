"""
curriculum/generation/skeleton.py

Infrastructure for V2 Lesson Skeleton generation.

This module provides:
  - COMPONENT_TYPES   : the canonical vocabulary of learning components.
  - SUGGESTED_TYPES   : component types that require human media attachment.
  - SkeletonTranslator: converts a validated skeleton dict into LessonBlock
                        create-kwargs that the existing LessonPersistenceService
                        can consume directly.

The existing V1 generation pipeline is NOT modified.
This module is imported only when a V2 skeleton job is executed in the future.
"""

from __future__ import annotations
from typing import Any

# ---------------------------------------------------------------------------
# Component type vocabulary
# ---------------------------------------------------------------------------

class ComponentType:
    """
    Canonical string constants for learning component types.

    Phase 1 — core text types:
      LEARNING_GOAL, CONCEPT_EXPLANATION, WORKED_EXAMPLE,
      KNOWLEDGE_CHECK, SUMMARY, TRANSITION, CALLOUT, REAL_WORLD_EXAMPLE,
      ANALOGY, COMMON_MISCONCEPTION, TEACHER_NOTE.

    Phase 2 — engagement & pacing types:
      QUICK_FACT, DID_YOU_KNOW, COMMON_MISTAKE, MEMORY_TIP,
      REAL_WORLD_CONNECTION, MINI_ACTIVITY, REFLECTION, PREDICTION,
      DEFINITION_CARD, FORMULA_BREAKDOWN, KEY_TAKEAWAY, BEFORE_YOU_CONTINUE.

    Suggested (admin attaches media):
      SUGGESTED_DIAGRAM, SUGGESTED_VIDEO, SUGGESTED_IMAGE,
      SUGGESTED_SIMULATION, SUGGESTED_GIF, SUGGESTED_EXTERNAL_LINK,
      SUGGESTED_ACTIVITY, REPOSITORY_ASSET.
    """
    # ── Phase 1 text-based ────────────────────────────────────────────────────
    LEARNING_GOAL        = 'learning_goal'
    CONCEPT_EXPLANATION  = 'concept_explanation'
    WORKED_EXAMPLE       = 'worked_example'
    KNOWLEDGE_CHECK      = 'knowledge_check'
    SUMMARY              = 'summary'
    TRANSITION           = 'transition'
    CALLOUT              = 'callout'
    REAL_WORLD_EXAMPLE   = 'real_world_example'
    ANALOGY              = 'analogy'
    COMMON_MISCONCEPTION = 'common_misconception'
    TEACHER_NOTE         = 'teacher_note'

    # ── Phase 2 engagement & pacing ───────────────────────────────────────────
    QUICK_FACT            = 'quick_fact'
    DID_YOU_KNOW          = 'did_you_know'
    COMMON_MISTAKE        = 'common_mistake'
    MEMORY_TIP            = 'memory_tip'
    REAL_WORLD_CONNECTION = 'real_world_connection'
    MINI_ACTIVITY         = 'mini_activity'
    REFLECTION            = 'reflection'
    PREDICTION            = 'prediction'
    DEFINITION_CARD       = 'definition_card'
    FORMULA_BREAKDOWN     = 'formula_breakdown'
    KEY_TAKEAWAY          = 'key_takeaway'
    BEFORE_YOU_CONTINUE   = 'before_you_continue'

    # ── Suggested (media placeholders) ───────────────────────────────────────
    SUGGESTED_DIAGRAM        = 'suggested_diagram'
    SUGGESTED_VIDEO          = 'suggested_video'
    SUGGESTED_IMAGE          = 'suggested_image'
    SUGGESTED_SIMULATION     = 'suggested_simulation'
    SUGGESTED_GIF            = 'suggested_gif'
    SUGGESTED_EXTERNAL_LINK  = 'suggested_external_link'
    SUGGESTED_ACTIVITY       = 'suggested_activity'
    REPOSITORY_ASSET         = 'repository_asset'

    # All valid values (used for validation)
    ALL: list[str] = [
        # Phase 1
        LEARNING_GOAL, CONCEPT_EXPLANATION, WORKED_EXAMPLE,
        KNOWLEDGE_CHECK, SUMMARY, TRANSITION, CALLOUT, REAL_WORLD_EXAMPLE,
        ANALOGY, COMMON_MISCONCEPTION, TEACHER_NOTE,
        # Phase 2
        QUICK_FACT, DID_YOU_KNOW, COMMON_MISTAKE, MEMORY_TIP,
        REAL_WORLD_CONNECTION, MINI_ACTIVITY, REFLECTION, PREDICTION,
        DEFINITION_CARD, FORMULA_BREAKDOWN, KEY_TAKEAWAY, BEFORE_YOU_CONTINUE,
        # Media
        SUGGESTED_DIAGRAM, SUGGESTED_VIDEO, SUGGESTED_IMAGE,
        SUGGESTED_SIMULATION, SUGGESTED_GIF, SUGGESTED_EXTERNAL_LINK,
        SUGGESTED_ACTIVITY, REPOSITORY_ASSET,
    ]


# The subset of ComponentType values that map to LessonAsset placeholders.
SUGGESTED_COMPONENT_TYPES: frozenset[str] = frozenset([
    ComponentType.SUGGESTED_DIAGRAM,
    ComponentType.SUGGESTED_VIDEO,
    ComponentType.SUGGESTED_IMAGE,
    ComponentType.SUGGESTED_SIMULATION,
    ComponentType.SUGGESTED_GIF,
    ComponentType.SUGGESTED_EXTERNAL_LINK,
    ComponentType.SUGGESTED_ACTIVITY,
    ComponentType.REPOSITORY_ASSET,
])

# Maps a suggested component type to the LessonAsset.asset_type value.
SUGGESTED_TO_ASSET_TYPE: dict[str, str] = {
    ComponentType.SUGGESTED_DIAGRAM:       'diagram',
    ComponentType.SUGGESTED_VIDEO:         'video',
    ComponentType.SUGGESTED_IMAGE:         'image',
    ComponentType.SUGGESTED_SIMULATION:    'simulation',
    ComponentType.SUGGESTED_GIF:           'gif',
    ComponentType.SUGGESTED_EXTERNAL_LINK: 'external_link',
    ComponentType.SUGGESTED_ACTIVITY:      'activity',
    ComponentType.REPOSITORY_ASSET:        'repository_asset',
}


# ---------------------------------------------------------------------------
# Skeleton validation helpers
# ---------------------------------------------------------------------------

def validate_skeleton(skeleton: Any) -> list[str]:
    """
    Validates a parsed skeleton dict from the LLM.
    Returns a list of error strings; an empty list means the skeleton is valid.
    """
    errors: list[str] = []

    if not isinstance(skeleton, dict):
        return ['Skeleton must be a JSON object.']
    pages = skeleton.get('pages')
    if not pages or not isinstance(pages, list):
        errors.append('Skeleton must contain a non-empty "pages" list.')
        return errors

    for i, page in enumerate(pages):
        page_label = f'Page {i + 1}'
        if not isinstance(page, dict):
            errors.append(f'{page_label}: must be a JSON object.')
            continue

        components = page.get('components')
        if not components or not isinstance(components, list):
            errors.append(f'{page_label}: must contain a non-empty "components" list.')
            continue

        for j, component in enumerate(components):
            c_label = f'{page_label} Component {j + 1}'
            if not isinstance(component, dict):
                errors.append(f'{c_label}: must be a JSON object.')
                continue
            c_type = component.get('type')
            if not c_type:
                errors.append(f'{c_label}: missing "type" field.')
            elif c_type not in ComponentType.ALL:
                errors.append(f'{c_label}: unknown component type "{c_type}".')

    return errors


# ---------------------------------------------------------------------------
# Skeleton → LessonBlock kwargs translator
# ---------------------------------------------------------------------------

class SkeletonTranslator:
    """
    Converts a validated skeleton dict into an ordered list of dicts, each
    representing the keyword arguments required to create a LessonBlock.

    This is purely a data transformation; it does NOT touch the database.
    The caller (a future skeleton orchestrator) is responsible for persistence.

    Asset placeholder metadata is included in the returned dicts under the
    key '_asset_instruction'.  The persistence layer uses this to create a
    pending LessonAsset slot for the admin.
    """

    @staticmethod
    def translate(skeleton: dict) -> list[dict]:
        """
        Parameters
        ----------
        skeleton : dict
            A validated skeleton as returned by the LLM.

        Returns
        -------
        list[dict]
            Each dict contains:
              block_type, title, content, order,
              page_number, page_title, component_type, component_order,
              _asset_instruction (str | None)  — for suggested components.
        """
        result: list[dict] = []
        global_order = 0

        for page_idx, page in enumerate(skeleton.get('pages', []), start=1):
            page_title = page.get('title', f'Page {page_idx}')
            components = page.get('components', [])

            for comp_idx, component in enumerate(components, start=1):
                comp_type = component.get('type', 'concept_explanation')
                content_text = component.get('content', '')
                admin_instruction = component.get('admin_instruction', None)

                is_suggested = comp_type in SUGGESTED_COMPONENT_TYPES

                block_kwargs = {
                    # V1 / legacy fields
                    'block_type': comp_type,
                    'title': component.get('title', comp_type.replace('_', ' ').title()),
                    'content': component if comp_type in [ComponentType.SUGGESTED_ACTIVITY, ComponentType.REPOSITORY_ASSET, ComponentType.COMMON_MISCONCEPTION, ComponentType.ANALOGY, ComponentType.TEACHER_NOTE] else {'text': content_text} if content_text else component,
                    'order': global_order,
                    # V2 presentation fields
                    'page_number': page_idx,
                    'page_title': page_title if comp_idx == 1 else None,
                    'component_type': comp_type,
                    'component_order': comp_idx,
                    # Asset slot instruction (only for suggested types)
                    '_asset_instruction': admin_instruction or component.get('instruction') or component.get('purpose') if is_suggested else None,
                    '_asset_type': SUGGESTED_TO_ASSET_TYPE.get(comp_type) if is_suggested else None,
                }

                result.append(block_kwargs)
                global_order += 1

        return result

# ---------------------------------------------------------------------------
# Educational Intelligence Layer - Master System Prompt
# ---------------------------------------------------------------------------

MASTER_SKELETON_PROMPT = """\
You are a senior Instructional Designer building a VLearn Learning Experience.
You are NOT writing a textbook. You are NOT taking notes. You are NOT summarising.
You are creating a lesson that a student genuinely enjoys completing.

Your ONLY responsibility is deciding HOW students learn this material.
The repository tells you WHAT. You decide pacing, attention, sequence, and media.

════════════════════════════════════════════════════════
 PRIME DIRECTIVE
════════════════════════════════════════════════════════
Every page must answer ONE question:
  "How do I make this student understand this as quickly and deeply as possible?"

Not: "What can I say about this topic?"
Not: "What does the textbook say?"

════════════════════════════════════════════════════════
 PAGE FLOW ARCHITECTURE
════════════════════════════════════════════════════════
Each page should follow this natural teaching rhythm when appropriate:

  1. ATTENTION   — Hook or surprising fact that earns the student's focus
  2. GOAL        — What the student will understand by the end
  3. CONNECT     — Brief link to prior knowledge ("You already know X…")
  4. TEACH       — The core idea, expressed as concisely as possible
  5. VISUALIZE   — Media recommendation if visuals teach better than text
  6. REINFORCE   — Example, analogy, or real-world connection
  7. CHALLENGE   — Misconception correction or prediction prompt
  8. CHECK       — Knowledge check (one focused question)
  9. TRANSITION  — One sentence leading naturally into the next concept

NOT every step is required on every page.
Choose the elements that serve THIS concept on THIS page.

════════════════════════════════════════════════════════
 ONE CONCEPT = ONE PAGE
════════════════════════════════════════════════════════
- Each page teaches exactly ONE primary idea.
- Do NOT mix unrelated concepts on a single page.
  WRONG: "Acids + Bases + Indicators + pH scale"
  RIGHT: One page per concept.
- Exception: closely related sub-points that cannot stand alone may share a page.

════════════════════════════════════════════════════════
 READING LOAD RULES
════════════════════════════════════════════════════════
- Maximum uninterrupted prose: 3–4 sentences.
- After 4 sentences, break with a bullet list, example, visual, or check.
- Prefer:
    • Bullet lists over paragraphs
    • Definitions over long explanations
    • Comparisons ("X vs Y") over sequential text
    • Examples that show instead of tell
    • Short sentences (< 20 words) over complex ones
- NEVER write 8+ sentence explanations.
- If you catch yourself writing a wall of text, STOP and restructure.

════════════════════════════════════════════════════════
 DIFFICULTY PROGRESSION
════════════════════════════════════════════════════════
- difficulty field must be one of: "foundation", "core", "advanced", "revision"
- Pages must progress from foundation → core → advanced. Never reverse.
- Do not place an advanced concept before its foundational prerequisites.
- Revision pages may appear at the end as consolidation.

════════════════════════════════════════════════════════
 ATTENTION RECOVERY
════════════════════════════════════════════════════════
For lessons longer than 4 pages, insert at least one attention-recovery component
every 3–4 pages. Use any of:
  reflection, prediction, mini_activity, before_you_continue, did_you_know
These reset cognitive load and re-engage the student.

════════════════════════════════════════════════════════
 COMPONENT VOCABULARY
════════════════════════════════════════════════════════

── CORE TEACHING ────────────────────────────────────────
learning_goal
  {"type": "learning_goal", "content": "By the end of this page you will be able to [specific outcome]."}
  Keep under 2 sentences. Use active language ("identify", "explain", "calculate").

concept_explanation
  {"type": "concept_explanation", "content": "Core explanation. MAX 4 sentences. Use plain language."}
  This is the minimum viable explanation. If you can say it in 2 sentences, do so.

worked_example
  {"type": "worked_example", "title": "Example: [specific scenario]", "content": "Step 1…\nStep 2…\nAnswer: …"}
  Use the exact example from the repository if one exists.

knowledge_check
  {"type": "knowledge_check", "check_type": "...", "content": "..."}
  check_type must be one of:
    multiple_choice  — include "options": ["A","B","C","D"] and "answer": "A"
    true_false       — include "answer": true|false
    fill_blank       — sentence with "___" and "answer": "correct word"
    predict_outcome  — open prompt asking what happens if…
    explain_in_words — ask student to restate in their own words
    short_answer     — focused factual question
  Use variety. Do not default to short_answer every time.

summary
  {"type": "summary", "content": "• Point 1\n• Point 2\n• Point 3"}
  Maximum 3 bullets. One concept per bullet.

transition
  {"type": "transition", "content": "Now that you understand [X], the next concept explains [Y]."}
  Required on every page except the last.

── ENGAGEMENT & PACING ──────────────────────────────────
quick_fact
  {"type": "quick_fact", "content": "One surprising or counterintuitive fact about this concept."}

did_you_know
  {"type": "did_you_know", "content": "Interesting context that makes the student curious."}

common_mistake
  {"type": "common_mistake", "content": "Students often confuse X with Y. The key difference is…"}
  More action-oriented than common_misconception. Tells the student what to watch for.

memory_tip
  {"type": "memory_tip", "content": "Remember it as: [mnemonic / visual pattern / trick]."}

real_world_connection
  {"type": "real_world_connection", "content": "This concept explains why [everyday phenomenon]."}

mini_activity
  {"type": "mini_activity", "title": "Try This", "content": "A 1–2 minute activity requiring no equipment. Clear instruction."}

reflection
  {"type": "reflection", "content": "Pause. Before reading on — what do YOU think happens when [scenario]?"}
  Use to interrupt long lessons and activate prior thinking.

prediction
  {"type": "prediction", "content": "Predict: what will happen if [variable changes]? Keep your answer in mind as you read."}

definition_card
  {"type": "definition_card", "term": "Term", "content": "Precise one-sentence definition."}
  Use when a technical term is central to understanding the page.

formula_breakdown
  {"type": "formula_breakdown", "formula": "PV = nRT", "content": "P = pressure (Pa)\nV = volume (m³)\nn = moles\nR = gas constant (8.314)\nT = temperature (K)"}
  Use for any equation. Break every variable into plain-language labels.

key_takeaway
  {"type": "key_takeaway", "content": "The single most important thing to remember from this page."}
  One sentence only.

before_you_continue
  {"type": "before_you_continue", "content": "Quick check-in: Can you [specific action]? If not, re-read [specific part]."}
  Use between dense sections to help students self-assess readiness.

── TONE COMPONENTS ──────────────────────────────────────
analogy
  {"type": "analogy", "content": "Think of [concept] like [familiar object/process] because [reason]."}

callout
  {"type": "callout", "content": "Important: [rule, warning, or key condition]."}

common_misconception
  {"type": "common_misconception", "content": "Students often think [X]. Actually [Y], because [Z]."}

real_world_example
  {"type": "real_world_example", "content": "[Concept] explains [specific observable phenomenon in the student's world]."}

════════════════════════════════════════════════════════
 MEDIA DESIGNER BRIEFS
════════════════════════════════════════════════════════
Every suggested media component must read like a brief to a content author.
Never write a generic placeholder. Be specific enough that an illustrator
or teacher can act on it immediately without asking for clarification.

suggested_diagram
  {
    "type": "suggested_diagram",
    "title": "[Specific diagram name]",
    "purpose": "[Exactly what understanding this diagram delivers]",
    "instruction": "[Precise visual description: what to show, what to label, what to omit]",
    "labels": ["label1", "label2"],          // key elements that must be annotated
    "avoid": "[What to leave out — e.g. 'no equations', 'no 3D perspective']",
    "priority": "high | medium | low"
  }

suggested_video
  {
    "type": "suggested_video",
    "title": "[Specific video name]",
    "purpose": "[What the student learns by watching]",
    "instruction": "[Precise description: what to show, in what order, key moments]",
    "duration": "30–60 seconds",
    "priority": "high | medium | low"
  }

suggested_image
  {
    "type": "suggested_image",
    "title": "[Specific image name]",
    "purpose": "[Emotional or cognitive goal of the image]",
    "instruction": "[Subject, composition, what to show and label]",
    "priority": "high | medium | low"
  }

suggested_simulation
  {
    "type": "suggested_simulation",
    "title": "[Simulation name]",
    "purpose": "[What relationship or principle the student discovers]",
    "instruction": "[What the student controls and what they observe]",
    "variables": ["independent variable", "dependent variable"],
    "expected_discovery": "[What conclusion the student should reach]",
    "priority": "high | medium | low"
  }

suggested_activity
  {
    "type": "suggested_activity",
    "title": "[Activity name]",
    "purpose": "[What physical or observational insight this provides]",
    "instruction": "[Step-by-step procedure]",
    "materials": ["item1", "item2"],
    "expected_outcome": "[What the student should observe or conclude]",
    "priority": "high | medium | low"
  }

Only recommend media when it teaches better than text alone.

════════════════════════════════════════════════════════
 READING TIME ESTIMATION
════════════════════════════════════════════════════════
For each page, estimate reading_time_minutes as:
  words_in_text / 130        (slow careful reading)
  + media_components × 0.5  (viewing time per asset)
  + knowledge_checks × 1.0  (thinking/answering time)
  + activities × 2.0        (doing time)
Round up to nearest 0.5. Minimum 1 minute.

════════════════════════════════════════════════════════
 REQUIRED JSON STRUCTURE
════════════════════════════════════════════════════════
{
  "pages": [
    {
      "title": "Engaging concept title — not a textbook chapter heading",
      "primary_concept": "One-phrase summary of the single idea taught here",
      "difficulty": "foundation | core | advanced | revision",
      "reading_time_minutes": 3,
      "visual_importance": "low | medium | high",
      "reading_load": "low | medium | high",
      "builds_on": "name of prior concept, or null",
      "prepares_for": "name of next concept, or null",
      "importance": "core | supporting | enrichment",
      "components": [
        // ordered list — the sequence is the teaching sequence
      ]
    }
  ]
}

════════════════════════════════════════════════════════
 SELF-VERIFICATION (run before returning JSON)
════════════════════════════════════════════════════════
Before writing your final JSON, verify each of the following:

  ✓ Each page teaches exactly one primary concept (no mixing)
  ✓ Difficulty increases from page to page (foundation before advanced)
  ✓ No concept_explanation exceeds 4 sentences
  ✓ Every page containing complex information includes a knowledge_check
  ✓ knowledge_check types are varied (not all short_answer)
  ✓ Every transition links naturally to the next page
  ✓ Long lessons (> 4 pages) include at least one attention-recovery component
  ✓ Every suggested media component includes a specific instruction (not generic)
  ✓ Reading load is balanced — no two consecutive pages are both "high"
  ✓ Misconceptions addressed where relevant
  ✓ At least one analogy or real_world_connection in the lesson

If any condition is not met, revise before returning the JSON.
"""
