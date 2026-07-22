"""
VLearn Teaching Playbook
Single source of instructional intelligence for the Learning Experience Planner.
Captures how master educators construct intuitive, engaging, and rigorous lessons.
"""

TEACHING_PLAYBOOK_TEXT = """\
════════════════════════════════════════════════════════
 VLEARN TEACHING PLAYBOOK: CORE INSTRUCTIONAL PRINCIPLES
════════════════════════════════════════════════════════

1. INTUITION BEFORE TERMINOLOGY
   • Always introduce a concept through an observable phenomenon, familiar experience, or intuitive scenario.
   • Build the student's internal mental model FIRST.
   • Introduce scientific terminology and formal definitions ONLY after understanding has formed, as convenient labels for what they already grasp.
   • NEVER begin an explanation with a dictionary or textbook definition.

2. ONE COGNITIVE SHIFT PER LEARNING MOMENT
   • Each node must achieve exactly ONE specific mental change or realization.
   • Avoid explaining multiple major ideas simultaneously. Stop explaining once the target understanding is reached.
   • Prefer an interactive engagement (predict, observe, question) over adding another paragraph of text.

3. ACTIVE LEARNING (THINK BEFORE BEING TOLD)
   • Require students to commit to a thought before revealing answers.
   • Use primitives (predict, observe, compare, reason, investigate, reflect) before explaining the underlying mechanism.
   • Prioritize creating curiosity and cognitive gaps over information delivery.

4. MISCONCEPTION-DRIVEN TEACHING
   • Proactively confront common misconceptions using this explicit sequence:
     Common Misconception → Why It Seems Correct → Counter-Example/Disruption → Correct Mental Model.
   • Integrate misconceptions directly into the core narrative flow, not as isolated side notes or trivia.

5. RICH ANALOGIES WITH BOUNDARIES
   • Use analogies that explain physical or logical mechanisms rather than superficial similarities.
   • Every analogy MUST:
     a) Map key functional relationships accurately.
     b) Explicitly state where the analogy breaks down to prevent incorrect transfer of reasoning.

6. GUIDED VISUAL THINKING (MEDIA WITH PURPOSE)
   • Every media specification (recommended_learning_support) MUST answer:
     a) WHY the visual exists (educational objective).
     b) WHAT invisible mechanism or hidden process it reveals.
     c) WHAT specific feature the learner must focus on and notice.
     d) WHICH misconception it resolves.
   • Visuals exist to build mental models, never merely to decorate.

7. DIAGNOSTIC QUESTIONS & REASONING
   • Questions must measure conceptual understanding and transfer, NEVER definition memorization.
   • Focus questions on prediction, application to novel scenarios, system disruptions, cause-and-effect, and decision making.
   • Always require learners to explain "why" or justify their reasoning.

8. NARRATIVE FLOW & TRANSITIONS
   • Connect every learning node seamlessly to the preceding one.
   • Transitions must make clear why the learner is moving forward, what question has now emerged, and what mystery remains.
   • Avoid disconnected or modular instructional blocks.

9. COGNITIVE PACING & VARIETY
   • Alternate systematically between thinking, explaining, visualizing, practicing, and reflecting.
   • NEVER exceed 2 consecutive pure explanation nodes without an interactive or observational primitive.
   • Change the learner's active cognitive mode every few nodes to sustain focus.

10. INVISIBLE MECHANISMS
    • For concepts involving hidden processes (particles, forces, energy, algorithms, biological systems, fields):
    • Explicitly identify the invisible mechanism blocking understanding.
    • Design explanations, analogies, and visual supports specifically to make that hidden process visible and intuitive.
"""

def get_playbook_text() -> str:
    """Returns the formatted Teaching Playbook text for injection into planner prompts."""
    return TEACHING_PLAYBOOK_TEXT
