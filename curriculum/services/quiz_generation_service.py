"""
Revision Quiz Generation Service.

Generates curriculum-grounded revision quizzes and exam papers using OpenAI
with structured output. Supports KCSE (8-4-4) and CBC (Competency Based Curriculum)
frameworks, inline SVG diagrams, strict examiner evaluation, and batch paper grading.
"""

import logging
from typing import Any, Dict, List, Optional
from django.utils import timezone
from pydantic import BaseModel, Field

from curriculum.models import (
    Topic,
    LearningUnit,
    Lesson,
    LessonBlock,
    KnowledgeChunk,
    Concept,
    Misconception,
)
from ai_infrastructure.llm_factory import LLMFactory

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Pydantic Schemas for Structured LLM Output
# ---------------------------------------------------------------------------

class QuizQuestionSchema(BaseModel):
    question: str = Field(
        description="The question prompt. For structured theory questions, append marks like '(2 marks)'.",
    )
    check_type: str = Field(
        default="multiple_choice",
        description="Question format: multiple_choice, true_false, kcse_structured, or cbc_scenario_structured.",
    )
    assessment_framework: Optional[str] = Field(
        default="kcse",
        description="Curriculum framework: 'kcse' or 'cbc'.",
    )
    options: List[str] = Field(
        default_factory=list,
        description="List of 4 options (A, B, C, D) for MCQ, or ['True', 'False'] for true_false. Leave empty for structured questions.",
    )
    correct_answer: str = Field(
        description="The correct answer ('A', 'B', 'C', 'D' for MCQ, 'True'/'False' for T/F, or complete model answer for structured theory).",
    )
    max_marks: Optional[int] = Field(
        default=1,
        description="Total marks for this question (1 for MCQ/TF, 2 to 4 for structured).",
    )
    marking_scheme: Optional[str] = Field(
        default="",
        description="Breakdown of points awarded (e.g. '1 mark for M1 formula, 1 mark for A1 answer' or CBC rubric criteria).",
    )
    explanation: str = Field(
        description="Deep pedagogical explanation. Clearly explain why the correct answer is factually right, address misconceptions, and suggest subtopics.",
    )
    hint: Optional[str] = Field(
        default="",
        description="Helpful clue or hint if the student gets stuck.",
    )
    subtopic_to_review: Optional[str] = Field(
        default="",
        description="Specific subtopic or concept name the student should revisit.",
    )
    difficulty: str = Field(
        default="medium",
        description="Difficulty rating: easy, medium, or hard.",
    )
    scenario_stimulus: Optional[str] = Field(
        default="",
        description="Authentic real-world situation or context narrative (essential for CBC questions, e.g. local farm problem, environmental conservation, kitchen science).",
    )
    diagram_svg: Optional[str] = Field(
        default="",
        description="Clean, self-contained semantic SVG illustration code when a diagram is appropriate (e.g. circuit, apparatus, ray diagram, data chart). Must have viewBox='0 0 500 300' and legible text labels.",
    )
    diagram_caption: Optional[str] = Field(
        default="",
        description="Caption for the diagram, e.g. 'Figure 1: Experimental setup for fractional distillation of ethanol-water mixture'.",
    )
    competency_tested: Optional[str] = Field(
        default="",
        description="For CBC questions: the core competency tested (e.g. 'Critical Thinking & Problem Solving', 'Scientific Inquiry', 'Creativity & Imagination').",
    )
    rubric_level_criteria: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        description="For CBC tasks: brief descriptors for Level 4 (EE), Level 3 (ME), Level 2 (AE), Level 1 (BE).",
    )


class GeneratedQuizSchema(BaseModel):
    title: str = Field(
        description="Engaging and accurate title for this revision quiz or exam paper.",
    )
    description: str = Field(
        description="Summary of core curriculum concepts tested in this quiz.",
    )
    difficulty: str = Field(
        default="intermediate",
        description="Overall difficulty level: beginner, intermediate, or advanced.",
    )
    assessment_framework: Optional[str] = Field(
        default="kcse",
        description="Assessment framework: 'kcse' or 'cbc'.",
    )
    time_limit_mins: Optional[int] = Field(
        default=20,
        description="Recommended time in minutes for this assessment.",
    )
    questions: List[QuizQuestionSchema] = Field(
        description="List of generated revision quiz questions.",
    )


class KCSEGradingResponse(BaseModel):
    marks_awarded: int = Field(description="Marks awarded out of max_marks (integer between 0 and max_marks)")
    max_marks: int = Field(description="Maximum possible marks for this question")
    feedback: str = Field(description="Strict examiner commentary directly quoting the student's text, explaining what was credited and what was penalized.")
    points_earned: List[str] = Field(description="Bullet points of concepts/keywords student earned marks for")
    points_missed: List[str] = Field(description="Bullet points of concepts/keywords student missed or answered incorrectly")
    model_answer: str = Field(description="Ideal complete model answer to award full marks with mark breakdown (M1, A1, B1)")
    subtopic_to_review: Optional[str] = Field(default="", description="Specific subtopic the student should revisit")
    competency_level: Optional[str] = Field(default="", description="For CBC: Performance level, e.g. 'Meeting Expectations (ME)'")


# ---------------------------------------------------------------------------
# Knowledge Context Retrieval Helpers (Decomposed for Low Cyclomatic Complexity)
# ---------------------------------------------------------------------------

def _gather_chunks_context(topic: Topic) -> List[str]:
    """Retrieve raw textbook chunk text for the topic."""
    chunks = KnowledgeChunk.objects.filter(topic=topic).exclude(content_text="")[:10]
    if not chunks.exists():
        chunks = KnowledgeChunk.objects.filter(
            learning_unit__topic=topic
        ).exclude(content_text="")[:10]

    sections: List[str] = []
    for chunk in chunks:
        text = chunk.content_text.strip()
        if text:
            title = chunk.section_title or "Textbook Extract"
            sections.append(f"### {title}\n{text}")
    return sections


def _gather_concepts_context(topic: Topic) -> List[str]:
    """Retrieve approved concepts for the topic."""
    concepts = Concept.objects.filter(learning_unit__topic=topic)[:8]
    if not concepts.exists():
        return []
    items = [f"- **{c.name}**: {c.description}" for c in concepts if c.name]
    return ["### Key Concepts\n" + "\n".join(items)] if items else []


def _gather_misconceptions_context(topic: Topic) -> List[str]:
    """Retrieve known misconceptions for the topic."""
    misconceptions = Misconception.objects.filter(concept__learning_unit__topic=topic)[:6]
    if not misconceptions.exists():
        return []
    items = [
        f"- Misconception: {m.description} -> Correction: {m.correction}"
        for m in misconceptions
        if m.description
    ]
    return ["### Common Student Misconceptions\n" + "\n".join(items)] if items else []


def _gather_published_blocks_context(topic: Topic) -> List[str]:
    """Fallback: retrieve text from published lesson blocks if no chunks exist."""
    blocks = LessonBlock.objects.filter(
        lesson__topic=topic,
        lesson__status="published",
        block_type__in=["concept_explanation", "core_explanation", "definition", "overview"],
    )[:8]
    sections: List[str] = []
    for b in blocks:
        c = b.content
        b_text = c if isinstance(c, str) else (c.get("text") or c.get("content") or "")
        if b_text:
            sections.append(f"### {b.title or 'Lesson Material'}\n{b_text}")
    return sections


def gather_topic_knowledge_context(topic: Topic, max_words: int = 3500) -> str:
    """
    Retrieve knowledge base chunks, concepts, and misconceptions from the DB
    for a given topic to ground the LLM generation.
    """
    sections: List[str] = []
    sections.extend(_gather_chunks_context(topic))
    sections.extend(_gather_concepts_context(topic))
    sections.extend(_gather_misconceptions_context(topic))

    if not sections:
        sections.extend(_gather_published_blocks_context(topic))

    combined = "\n\n".join(sections)
    words = combined.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + "..."
    return combined or f"Subject: {topic.subject.name}, Topic: {topic.name}. Focus on core curriculum competencies."


# ---------------------------------------------------------------------------
# Prompt Construction
# ---------------------------------------------------------------------------

def _is_cbc_context(curr_name: str, grade_name: str) -> bool:
    """Check if curriculum or grade name matches CBC keywords."""
    cbc_keywords = ("cbc", "grade", "junior", "kjsea")
    return any(k in curr_name or k in grade_name for k in cbc_keywords)


def detect_framework_for_topic(topic: Topic, requested_framework: Optional[str] = None) -> str:
    """
    Detect whether assessment should follow CBC or KCSE.
    Defaults to KCSE for Forms 1-4 and CBC for Grades 7-9.
    """
    req = (requested_framework or "auto").strip().lower()
    if req in ["kcse", "cbc"]:
        return req

    grade = getattr(topic.subject, "grade", None) if topic.subject else None
    if not grade:
        return "kcse"

    curr_name = (grade.curriculum.name if grade.curriculum else "").lower()
    grade_name = (grade.name or "").lower()
    return "cbc" if _is_cbc_context(curr_name, grade_name) else "kcse"


def _get_difficulty_guidelines(difficulty: str) -> str:
    """Return instructions matching the requested difficulty."""
    diff_map = {
        "beginner": (
            "Difficulty: BEGINNER / EASY. Questions should test core recall, standard terminology, "
            "basic definitions, and foundational concepts. Avoid confusing trick choices."
        ),
        "intermediate": (
            "Difficulty: INTERMEDIATE / MEDIUM. Questions should test conceptual understanding, "
            "standard calculations, application of rules, and relationship between components."
        ),
        "advanced": (
            "Difficulty: ADVANCED / HARD. Questions should test multi-step reasoning, analytical problem "
            "solving, edge cases, formula derivations, and deep diagnosis of common misconceptions."
        ),
    }
    return diff_map.get(difficulty.lower(), "Difficulty: INTERMEDIATE / MEDIUM.")


def _get_type_guidelines(
    quiz_type: str,
    assessment_framework: str = "kcse",
    include_diagrams: bool = True,
) -> str:
    """Return instructions matching the quiz question format and curriculum framework."""
    is_cbc = assessment_framework.lower() == "cbc"

    framework_intro = (
        "ASSESSMENT FRAMEWORK: COMPETENCY BASED CURRICULUM (CBC / CBA / KJSEA / SENIOR SECONDARY).\n"
        "- Structure questions around authentic Kenyan situational scenarios (e.g. sustainable agriculture, local health/hygiene, solar energy, water purification in arid regions, food storage).\n"
        "- In 'scenario_stimulus', provide the real-world context background.\n"
        "- In 'competency_tested', specify the core competency (e.g. Critical Thinking & Problem Solving, Communication, Scientific Inquiry, Creativity).\n"
        "- Set check_type to 'cbc_scenario_structured' for open inquiry tasks or 'multiple_choice' for scenario MCQs."
        if is_cbc
        else
        "ASSESSMENT FRAMEWORK: KENYA CERTIFICATE OF SECONDARY EDUCATION (KCSE / 8-4-4 / KNEC).\n"
        "- Follow official KNEC paper guidelines: Bloom's taxonomy, precise scientific definitions, step-by-step calculations, chemical/physical equations.\n"
        "- Include explicit mark allocations like '(2 marks)' or '(3 marks)'.\n"
        "- In 'marking_scheme', detail KNEC mark distributions: M1 (Method mark), A1 (Accuracy mark), B1 (Independent fact mark)."
    )

    diagram_instructions = ""
    if include_diagrams:
        diagram_instructions = (
            "\n\nDIAGRAM & VISUAL STIMULUS REQUIREMENT:\n"
            "- For at least 1 or 2 questions (especially medium/hard questions or questions testing experimental setups, ray optics, circuits, cell biology, or data charts), generate a clean, self-contained SVG illustration in 'diagram_svg'.\n"
            "- The SVG MUST be valid XML with viewBox='0 0 500 300' and xmlns='http://www.w3.org/2000/svg'.\n"
            "- Use clean geometric elements (<rect>, <circle>, <line>, <path>), clear stroke colors (e.g. #02a0bf, #374151), soft fills, and legible <text> labels with font-size='14'.\n"
            "- Set 'diagram_caption' (e.g. 'Figure 1: Experimental setup for heating calcium carbonate').\n"
            "- Two consecutive questions CAN share the same diagram (e.g. Question 1 refers to Figure 1 part (a), and Question 2 refers to Figure 1 part (b)). When doing so, mention 'Refer to Figure 1 above:'."
        )

    type_instructions_map = {
        "multiple_choice": "All questions must be Multiple Choice (MCQ) with 4 distinct choices (A, B, C, D) and check_type='multiple_choice'.",
        "true_false": "All questions must be True/False format with options ['True', 'False'] and check_type='true_false'.",
        "kcse_structured": (
            "All questions must be KCSE-style structured theory / short-answer questions with check_type='kcse_structured', "
            "empty options=[], allocated 2 to 4 marks each, a complete model answer, and a point-by-point marking_scheme (M1, A1, B1)."
        ),
        "cbc_scenario_structured": (
            "All questions must be CBC scenario-based structured inquiry questions with check_type='cbc_scenario_structured', "
            "a detailed 'scenario_stimulus' grounded in local Kenyan context, tested core competency, rubric criteria, and 2 to 4 marks each."
        ),
        "full_paper": (
            f"Generate an authentic, complete national examination paper for {assessment_framework.upper()}.\n"
            "- Include a mix of Section A (foundational conceptual questions / MCQs) and Section B (extended structured theory / scenario inquiry tasks with 2-4 marks each).\n"
            "- Allocate appropriate time_limit_mins."
        ),
        "mixed": (
            "Provide a balanced mix of Multiple Choice (check_type='multiple_choice'), "
            "True/False (check_type='true_false'), and Structured theory / Scenario inquiry questions (check_type='kcse_structured' or 'cbc_scenario_structured')."
        ),
        "short_answer": "All questions must be short-answer / conceptual questions with empty options=[]."
    }

    selected_type_text = type_instructions_map.get(quiz_type.lower(), type_instructions_map["multiple_choice"])
    return f"{framework_intro}\n\n{selected_type_text}{diagram_instructions}"


def build_quiz_prompts(
    topic: Topic,
    difficulty: str,
    num_questions: int,
    quiz_type: str,
    custom_prompt: str = "",
    knowledge_context: str = "",
    assessment_framework: str = "kcse",
    include_diagrams: bool = True,
) -> Dict[str, str]:
    """
    Build system and user prompts for OpenAI structured quiz generation.
    """
    subject_name = topic.subject.name if topic.subject else "General Science"
    grade_name = topic.subject.grade.name if (topic.subject and topic.subject.grade) else "Secondary"

    diff_instructions = _get_difficulty_guidelines(difficulty)
    type_instructions = _get_type_guidelines(quiz_type, assessment_framework, include_diagrams)

    framework_label = "CBC Competency-Based Assessment" if assessment_framework == "cbc" else "KCSE / 8-4-4 KNEC"
    system_instruction = (
        f"You are a senior national examiner and curriculum assessment specialist for the Kenyan educational curriculum "
        f"({framework_label} - {grade_name} {subject_name}). Your task is to design an authentic, rigorous, and pedagogically sound assessment.\n"
        f"Every question must be strictly grounded in curriculum facts.\n"
        f"For explanations, provide deep pedagogical feedback:\n"
        f"1. Explain clearly why the correct answer is factually right.\n"
        f"2. Explain why common misconceptions or distractor choices are incorrect.\n"
        f"3. In 'subtopic_to_review', name the specific subtopic or concept the student must revisit.\n"
        f"4. If generating SVG diagrams, ensure valid syntax and clear visual readability."
    )

    user_prompt = (
        f"Generate a {difficulty.upper()} {framework_label} assessment for {grade_name} - {subject_name}.\n"
        f"Topic: {topic.name}\n"
        f"Number of Questions: {num_questions}\n"
        f"{type_instructions}\n"
        f"{diff_instructions}\n"
    )

    if custom_prompt.strip():
        user_prompt += f"\nInstructor Custom Focus & Instructions:\n{custom_prompt.strip()}\n"

    user_prompt += (
        f"\n--- GROUNDING CURRICULUM TEXTBOOK KNOWLEDGE ---\n"
        f"{knowledge_context}\n"
        f"-------------------------------------------------\n"
        f"Ensure all {num_questions} questions are well-phrased, unambiguous, and formatted according to schema."
    )

    return {"system": system_instruction, "user": user_prompt}


# ---------------------------------------------------------------------------
# LLM Invocation & Structured Response Parsing
# ---------------------------------------------------------------------------

def generate_quiz_with_openai(
    system_instruction: str,
    user_prompt: str,
) -> GeneratedQuizSchema:
    """
    Call OpenAI provider using structured output with GeneratedQuizSchema.
    Falls back gracefully to the default provider if OpenAI is unconfigured.
    """
    try:
        provider = LLMFactory.get_provider("openai")
    except Exception as exc:
        logger.warning("Failed to initialize OpenAI provider (%s), using default provider", exc)
        provider = LLMFactory.get_provider()

    result = provider.generate_structured(
        prompt=user_prompt,
        response_schema=GeneratedQuizSchema,
        system_instruction=system_instruction,
        temperature=0.35,
    )

    if isinstance(result, GeneratedQuizSchema):
        return result

    if isinstance(result, dict):
        return GeneratedQuizSchema.model_validate(result)

    raise ValueError(f"Unexpected response format from provider: {type(result)}")


# ---------------------------------------------------------------------------
# Database Persistence Helpers (Decomposed for Low Cyclomatic Complexity)
# ---------------------------------------------------------------------------

def _create_quiz_overview_block(
    lesson: Lesson,
    title: str,
    description: str,
    difficulty: str,
    question_count: int,
    assessment_framework: str = "kcse",
    quiz_mode: str = "full_paper",
    time_limit_mins: Optional[int] = None,
) -> LessonBlock:
    """Create the initial Overview block on Page 1."""
    limit = time_limit_mins or max(5, question_count * 2)
    instructions = (
        "This is a Full Examination Paper. Complete all questions across the paper at your own pace. "
        "Your answers will be preserved as you navigate. When finished, submit the entire paper for strict AI examiner marking."
        if quiz_mode == "full_paper"
        else "Read each question carefully and select or write your answer. You will receive immediate feedback and explanations upon submission."
    )

    content = {
        "title": title,
        "description": description,
        "difficulty": difficulty.lower(),
        "question_count": question_count,
        "time_limit_mins": limit,
        "assessment_framework": assessment_framework,
        "quiz_mode": quiz_mode,
        "instructions": instructions,
    }
    return LessonBlock.objects.create(
        lesson=lesson,
        block_type="overview",
        component_type="learning_goal",
        title="Revision Quiz Overview",
        order=0,
        page_number=1,
        page_title="Quiz Overview",
        content=content,
        metadata={
            "concept_group": "Overview",
            "is_quiz_intro": True,
            "quiz_mode": quiz_mode,
            "assessment_framework": assessment_framework,
        },
    )


def _resolve_options_for_check_type(check_type: str, raw_options: Optional[List[str]]) -> List[str]:
    """Helper to determine option list based on question format."""
    if check_type in ["kcse_structured", "cbc_scenario_structured", "short_answer"]:
        return []
    if check_type == "true_false":
        return ["True", "False"] if not raw_options else raw_options
    return raw_options or []


def _build_question_content(
    q: QuizQuestionSchema,
    difficulty: str,
    framework: str,
) -> Dict[str, Any]:
    """Helper to format question block dictionary payload."""
    clean_type = q.check_type or "multiple_choice"
    default_marks = 2 if clean_type in ["kcse_structured", "cbc_scenario_structured"] else 1
    marks = q.max_marks or default_marks

    content = q.model_dump()
    content["check_type"] = clean_type
    content["options"] = _resolve_options_for_check_type(clean_type, q.options)
    content["answer"] = str(q.correct_answer).strip()
    content["correct_answer"] = content["answer"]
    content["max_marks"] = marks
    content["assessment_framework"] = framework

    if not content.get("difficulty"):
        content["difficulty"] = difficulty.lower()
    return content


def _create_question_block(
    lesson: Lesson,
    q: QuizQuestionSchema,
    idx: int,
    difficulty: str,
    framework: str,
) -> LessonBlock:
    """Create a single interactive question block on Page idx+1."""
    content = _build_question_content(q, difficulty, framework)
    return LessonBlock.objects.create(
        lesson=lesson,
        block_type="knowledge_check",
        component_type="knowledge_check",
        title=f"Question {idx}",
        order=idx,
        page_number=idx + 1,
        page_title=f"Question {idx}",
        content=content,
        metadata={
            "concept_group": f"Question {idx}",
            "difficulty": content["difficulty"],
            "assessment_framework": framework,
            "check_type": content["check_type"],
        },
    )


# ---------------------------------------------------------------------------
# Strict LLM Examiner Grading Helpers
# ---------------------------------------------------------------------------

def _build_kcse_grading_prompt(
    question_text: str,
    max_marks: int,
    marking_scheme: str,
    model_answer: str,
    explanation: str,
    subtopic: str,
    student_answer: str,
    scenario_stimulus: str = "",
    framework: str = "kcse",
    competency: str = "",
) -> str:
    """Construct prompt for strict KNEC / CBC answer evaluation."""
    scheme_text = marking_scheme or "Award marks for factual accuracy, correct technical terminology, and logical reasoning."
    stimulus_part = f"### SCENARIO / STIMULUS CONTEXT\n{scenario_stimulus}\n\n" if scenario_stimulus else ""
    comp_part = f"### CORE COMPETENCY TESTED\n{competency}\n\n" if competency else ""

    return (
        f"### ASSESSMENT FRAMEWORK\n{framework.upper()}\n\n"
        f"{stimulus_part}"
        f"{comp_part}"
        f"### QUESTION\n{question_text}\n\n"
        f"### MAXIMUM MARKS\n{max_marks}\n\n"
        f"### OFFICIAL MARKING SCHEME / KEY POINTS\n{scheme_text}\n\n"
        f"### MODEL ANSWER / EXPLANATION\n{model_answer}\n{explanation}\n\n"
        f"### SUBTOPIC REFERENCE\n{subtopic}\n\n"
        f"### STUDENT'S SUBMITTED ANSWER\n\"{student_answer.strip()}\"\n\n"
        "Evaluate the student's answer strictly against the scheme and guidelines now."
    )


def grade_kcse_answer_with_llm(block: LessonBlock, student_answer: str) -> Dict[str, Any]:
    """
    Grade a student's answer to a structured question using strict LLM evaluation.
    Directly references and quotes the student's submitted text.
    """
    content = block.content if isinstance(block.content, dict) else {}
    question_text = content.get("question", "")
    max_marks = int(content.get("max_marks", 2))
    marking_scheme = content.get("marking_scheme", "")
    model_answer = content.get("correct_answer") or content.get("answer", "")
    explanation = content.get("explanation", "")
    subtopic = content.get("subtopic_to_review", "")
    scenario_stimulus = content.get("scenario_stimulus", "")
    framework = content.get("assessment_framework", "kcse")
    competency = content.get("competency_tested", "")

    framework_name = "KNEC KCSE" if framework == "kcse" else "CBC / KICD"
    system_instruction = (
        f"You are a strict, senior Kenya National Examinations Council ({framework_name}) chief examiner. "
        "Your marking must be rigorous, objective, and adhere strictly to official scoring rubrics.\n\n"
        "Strictness & Feedback Rules:\n"
        f"1. Maximum Marks: {max_marks}. Award an integer between 0 and {max_marks}.\n"
        "2. ZERO TOLERANCE FOR MISSING TECHNICAL TERMS: If the student uses vague colloquial expressions instead of "
        "precise scientific terms (e.g., writing 'it expands' instead of 'volume increases at constant pressure', "
        "or omitting chemical states (s), (l), (g), (aq), or forgetting physical units like cm³, mol/dm³, N, J), "
        "strictly DEDUCT marks.\n"
        "3. QUOTE THE STUDENT'S EXACT WORDS: In the 'feedback', explicitly reference and quote the student's text. "
        "State: 'You wrote: \"...\" - this earned credit for [...] but missed [...] because [...].'\n"
        "4. EXPLAIN THE RUBRIC GAP: Explain specifically why the student's phrasing did or did not satisfy the mark scheme criteria.\n"
        "5. List specific points earned and points missed.\n"
        "6. Provide a complete, textbook-grade model answer with explicit mark breakdown (M1, A1, B1).\n"
        "7. Specify the exact subtopic the student must revise."
    )

    user_prompt = _build_kcse_grading_prompt(
        question_text=question_text,
        max_marks=max_marks,
        marking_scheme=marking_scheme,
        model_answer=model_answer,
        explanation=explanation,
        subtopic=subtopic,
        student_answer=student_answer,
        scenario_stimulus=scenario_stimulus,
        framework=framework,
        competency=competency,
    )

    try:
        provider = LLMFactory.get_provider("openai")
    except Exception as exc:
        logger.warning("Failed to initialize OpenAI provider (%s), using default provider", exc)
        provider = LLMFactory.get_provider()

    result = provider.generate_structured(
        prompt=user_prompt,
        response_schema=KCSEGradingResponse,
        system_instruction=system_instruction,
        temperature=0.2,
        model_name="gpt-4o-mini",
    )

    if isinstance(result, KCSEGradingResponse):
        graded_data = result.model_dump()
    elif isinstance(result, dict):
        graded_data = KCSEGradingResponse.model_validate(result).model_dump()
    else:
        raise ValueError(f"Unexpected grading response format: {type(result)}")

    graded_data["marks_awarded"] = max(0, min(max_marks, graded_data.get("marks_awarded", 0)))
    graded_data["max_marks"] = max_marks
    if not graded_data.get("subtopic_to_review"):
        graded_data["subtopic_to_review"] = subtopic

    return graded_data


# ---------------------------------------------------------------------------
# Full Exam Paper Batch Grading Engine (Decomposed for Low CC)
# ---------------------------------------------------------------------------

def _is_answer_matching(student_ans: str, correct_ans: str) -> bool:
    """Case-insensitive string comparison for deterministic answers."""
    if not student_ans or not correct_ans:
        return False
    return student_ans.strip().lower() == correct_ans.strip().lower()


def _format_deterministic_feedback(is_correct: bool, correct: str, explanation: str) -> str:
    """Format explanation string for deterministic multiple choice / true-false."""
    if is_correct:
        return "Correct! Well done."
    return f"Incorrect. The correct answer is '{correct}'. {explanation}"


def _extract_correct_answer(content: Dict[str, Any]) -> str:
    """Extract standard correct answer string from block content."""
    ans = content.get("answer") or content.get("correct_answer") or ""
    return str(ans).strip()


def _grade_deterministic_question(
    block: LessonBlock,
    student_answer: str,
) -> Dict[str, Any]:
    """Grade MCQ and True/False questions deterministically."""
    content = block.content if isinstance(block.content, dict) else {}
    correct = _extract_correct_answer(content)
    max_marks = int(content.get("max_marks", 1))
    std_ans = str(student_answer or "").strip()

    is_correct = _is_answer_matching(std_ans, correct)
    marks_awarded = max_marks if is_correct else 0
    feedback = _format_deterministic_feedback(is_correct, correct, content.get("explanation", ""))

    return {
        "block_id": block.id,
        "question_title": block.title or f"Question {block.page_number - 1}",
        "check_type": content.get("check_type", "multiple_choice"),
        "student_answer": std_ans,
        "correct_answer": correct,
        "marks_awarded": marks_awarded,
        "max_marks": max_marks,
        "is_correct": is_correct,
        "feedback": feedback,
        "points_earned": ["Correct option selected"] if is_correct else [],
        "points_missed": [] if is_correct else [f"Expected '{correct}'"],
        "model_answer": correct,
        "subtopic_to_review": content.get("subtopic_to_review", ""),
    }


def _build_unattempted_response(
    block: LessonBlock,
    content: Dict[str, Any],
    max_marks: int,
) -> Dict[str, Any]:
    """Construct standard payload for unattempted structured questions."""
    return {
        "block_id": block.id,
        "question_title": block.title or f"Question {block.page_number - 1}",
        "check_type": content.get("check_type", "kcse_structured"),
        "student_answer": "",
        "correct_answer": content.get("correct_answer", ""),
        "marks_awarded": 0,
        "max_marks": max_marks,
        "is_correct": False,
        "feedback": "Question was not attempted. 0 marks awarded.",
        "points_earned": [],
        "points_missed": ["No response submitted by student"],
        "model_answer": content.get("correct_answer", "") or content.get("explanation", ""),
        "subtopic_to_review": content.get("subtopic_to_review", ""),
    }


def _grade_structured_question(
    block: LessonBlock,
    student_answer: str,
) -> Dict[str, Any]:
    """Grade theory / scenario question with strict LLM evaluation."""
    content = block.content if isinstance(block.content, dict) else {}
    max_marks = int(content.get("max_marks", 2))
    std_ans = str(student_answer or "").strip()

    if not std_ans:
        return _build_unattempted_response(block, content, max_marks)

    graded = grade_kcse_answer_with_llm(block, std_ans)
    marks_awarded = graded.get("marks_awarded", 0)
    is_correct = (marks_awarded == max_marks)

    return {
        "block_id": block.id,
        "question_title": block.title or f"Question {block.page_number - 1}",
        "check_type": content.get("check_type", "kcse_structured"),
        "student_answer": std_ans,
        "correct_answer": graded.get("model_answer") or content.get("correct_answer", ""),
        "marks_awarded": marks_awarded,
        "max_marks": max_marks,
        "is_correct": is_correct,
        "feedback": graded.get("feedback", ""),
        "points_earned": graded.get("points_earned", []),
        "points_missed": graded.get("points_missed", []),
        "model_answer": graded.get("model_answer", ""),
        "subtopic_to_review": graded.get("subtopic_to_review") or content.get("subtopic_to_review", ""),
    }


_KCSE_GRADE_THRESHOLDS = (
    (80, "A"), (75, "A-"), (70, "B+"), (65, "B"), (60, "B-"),
    (55, "C+"), (50, "C"), (45, "C-"), (40, "D+"), (35, "D"), (30, "D-")
)

def _calculate_kcse_grade(pct: float) -> str:
    """Map percentage to standard KCSE grade scale using threshold table."""
    for threshold, grade in _KCSE_GRADE_THRESHOLDS:
        if pct >= threshold:
            return grade
    return "E"


def _calculate_cbc_level(pct: float) -> str:
    """Map percentage to standard CBC 4-level performance rubric."""
    if pct >= 75: return "Exceeding Expectations (EE)"
    if pct >= 50: return "Meeting Expectations (ME)"
    if pct >= 35: return "Approaching Expectations (AE)"
    return "Below Expectations (BE)"


def _compile_verdict(pct: float, grade: str, framework: str) -> str:
    """Format overall examiner verdict statement."""
    if framework == "cbc":
        return f"Overall Performance: {grade} ({pct:.1f}%). Focus on practical inquiry and real-world application."
    return f"KNEC Examination Result: Grade {grade} ({pct:.1f}%). Rigorous revision on highlighted subtopics will reinforce key mark scheme criteria."


def _grade_single_paper_block(
    block: LessonBlock,
    student_responses: Dict[str, Any],
) -> Dict[str, Any]:
    """Helper to grade a single question block according to its check_type."""
    content = block.content if isinstance(block.content, dict) else {}
    ctype = content.get("check_type", "multiple_choice")
    std_ans = student_responses.get(str(block.id)) or student_responses.get(block.id, "")

    if ctype in ["multiple_choice", "true_false"]:
        return _grade_deterministic_question(block, std_ans)
    return _grade_structured_question(block, std_ans)


def _accumulate_priorities(priorities: List[str], q_res: Dict[str, Any]) -> None:
    """Helper to accumulate weak subtopics for follow-up revision."""
    sub = q_res.get("subtopic_to_review")
    if not q_res["is_correct"] and sub and sub not in priorities:
        priorities.append(sub)


def grade_full_exam_paper(
    lesson_id: int,
    student_responses: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Batch grade all questions in a full examination paper.
    MCQs/True-False are graded deterministically; theory/scenario questions are graded by AI examiner.
    """
    lesson = Lesson.objects.prefetch_related("blocks").get(pk=lesson_id)
    framework = (lesson.immutable_metadata or {}).get("assessment_framework", "kcse")

    question_blocks = [
        b for b in lesson.blocks.all().order_by("page_number", "order")
        if b.block_type == "knowledge_check"
    ]

    graded_questions: List[Dict[str, Any]] = []
    total_awarded = 0
    total_max = 0
    priorities: List[str] = []

    for block in question_blocks:
        q_res = _grade_single_paper_block(block, student_responses)
        graded_questions.append(q_res)
        total_awarded += q_res["marks_awarded"]
        total_max += q_res["max_marks"]
        _accumulate_priorities(priorities, q_res)

    pct = round((total_awarded / total_max * 100), 1) if total_max > 0 else 0.0
    grade = _calculate_cbc_level(pct) if framework == "cbc" else _calculate_kcse_grade(pct)
    verdict = _compile_verdict(pct, grade, framework)

    return {
        "lesson_id": lesson.id,
        "title": lesson.title,
        "assessment_framework": framework,
        "total_marks_awarded": total_awarded,
        "total_max_marks": total_max,
        "percentage": pct,
        "grade": grade,
        "examiner_verdict": verdict,
        "questions": graded_questions,
        "revision_priorities": priorities,
    }


# ---------------------------------------------------------------------------
# Database Persistence & High-Level Generation Workflow
# ---------------------------------------------------------------------------

def persist_generated_quiz_as_lesson(
    topic: Topic,
    quiz_data: GeneratedQuizSchema,
    difficulty: str,
    quiz_type: str,
    custom_prompt: str = "",
    assessment_framework: str = "kcse",
    quiz_mode: str = "full_paper",
    include_diagrams: bool = True,
) -> Lesson:
    """
    Save the generated quiz as a Lesson with its interactive LessonBlocks.
    """
    learning_unit = topic.learning_units.order_by("order", "id").first()
    title = quiz_data.title or f"{topic.name} - {difficulty.capitalize()} Revision Quiz"

    lesson = Lesson.objects.create(
        topic=topic,
        learning_unit=learning_unit,
        title=title,
        status="draft",
        version=1,
        immutable_metadata={
            "lesson_type": "revision_quiz",
            "difficulty": difficulty.lower(),
            "quiz_type": quiz_type,
            "assessment_framework": assessment_framework,
            "quiz_mode": quiz_mode,
            "include_diagrams": include_diagrams,
            "question_count": len(quiz_data.questions),
            "generated_with": "openai",
            "custom_prompt": custom_prompt,
            "generated_at": timezone.now().isoformat(),
        },
    )

    _create_quiz_overview_block(
        lesson=lesson,
        title=title,
        description=quiz_data.description or f"Revision assessment for {topic.name}.",
        difficulty=difficulty,
        question_count=len(quiz_data.questions),
        assessment_framework=assessment_framework,
        quiz_mode=quiz_mode,
        time_limit_mins=quiz_data.time_limit_mins,
    )

    for idx, q in enumerate(quiz_data.questions, start=1):
        _create_question_block(lesson, q, idx, difficulty, assessment_framework)

    logger.info(
        "Persisted Revision Quiz %d ('%s') [%s / %s] with %d questions",
        lesson.id,
        lesson.title,
        assessment_framework,
        quiz_mode,
        len(quiz_data.questions),
    )
    return lesson


def generate_revision_quiz_for_topic(
    topic_id: int,
    difficulty: str = "intermediate",
    num_questions: int = 5,
    quiz_type: str = "multiple_choice",
    custom_prompt: str = "",
    assessment_framework: str = "auto",
    quiz_mode: str = "full_paper",
    include_diagrams: bool = True,
) -> Lesson:
    """
    Orchestrate full quiz generation:
    1. Look up topic
    2. Detect assessment framework (KCSE vs CBC)
    3. Gather grounded knowledge
    4. Construct prompts with curriculum guidelines & diagrams
    5. Call OpenAI structured output
    6. Persist to DB as Lesson and LessonBlocks
    """
    topic = Topic.objects.select_related("subject", "subject__grade", "subject__grade__curriculum").get(pk=topic_id)
    framework = detect_framework_for_topic(topic, assessment_framework)
    knowledge_context = gather_topic_knowledge_context(topic)

    prompts = build_quiz_prompts(
        topic=topic,
        difficulty=difficulty,
        num_questions=num_questions,
        quiz_type=quiz_type,
        custom_prompt=custom_prompt,
        knowledge_context=knowledge_context,
        assessment_framework=framework,
        include_diagrams=include_diagrams,
    )

    generated_quiz = generate_quiz_with_openai(
        system_instruction=prompts["system"],
        user_prompt=prompts["user"],
    )

    return persist_generated_quiz_as_lesson(
        topic=topic,
        quiz_data=generated_quiz,
        difficulty=difficulty,
        quiz_type=quiz_type,
        custom_prompt=custom_prompt,
        assessment_framework=framework,
        quiz_mode=quiz_mode,
        include_diagrams=include_diagrams,
    )
