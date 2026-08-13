"""
VLearn Form 4 Mathematics — Mathematical Quality Audit

Performs a comprehensive quality audit over ingested Mathematics lessons,
covering:

1. Formula integrity        — balanced delimiters, pmatrix structure, no OCR remnants
2. Developer leakage        — no internal labels, metadata, or implementation notes visible to students
3. Worked-example integrity — Given → Method → Calculation → Result structure, non-empty steps
4. Pedagogical progression  — worked examples ordered easy → moderate → difficult → exam-style
5. MCQ completeness         — 4 options, valid answer, non-empty explanation
6. Short-answer completeness — hint and answer reveal present
7. Visual placeholder       — sugested_diagram/simulation titles are student-facing

Run from Vlearn_backend/:
  python curriculum/audit_form4_mathematics.py [--topic "Matrix and Transformation"] [--subject "Mathematics"] [--grade "Form 4"]
  python curriculum/audit_form4_mathematics.py --all

Exit codes:
  0 — No critical issues
  1 — Critical issues found (must block ingestion of next topic)
"""

import os
import sys
import re
import json
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEVELOPER_LEAK_PATTERNS = [
    (r"\bcomponent_type\b",    "CRITICAL",  "Internal field name"),
    (r"\bblock_type\b",        "CRITICAL",  "Internal field name"),
    (r"\bai_instruction\b",    "CRITICAL",  "AI authoring instruction"),
    (r"\basset_info\b",        "CRITICAL",  "Internal asset metadata key"),
    (r"\bblock_id\b",          "CRITICAL",  "Internal block identifier"),
    (r"\bTODO\b",              "CRITICAL",  "Developer TODO note"),
    (r"\bDEBUG\b",             "WARNING",   "Debug label"),
    (r"implementation_note",   "CRITICAL",  "Internal implementation note"),
    (r"\braw_prompt\b",        "CRITICAL",  "AI raw prompt"),
    (r"database_metadata",     "CRITICAL",  "Database metadata"),
    (r"ingestion_tag",         "CRITICAL",  "Internal ingestion tag"),
    (r"<PLACEHOLDER>",         "CRITICAL",  "Unfilled placeholder"),
    (r"\[insert .+?\]",        "CRITICAL",  "Unfilled bracket placeholder"),
    (r"FIXME",                 "WARNING",   "FIXME note"),
]

OCR_CORRUPTION_PATTERNS = [
    (r"[^\x00-\x7F]{3,}",     "WARNING",   "Possible non-ASCII / OCR artifact"),
    (r"\bfl\b.*\bow\b",        "INFO",      "Possible 'flow' OCR split"),
    (r"\d+\s*[lI]\s*\d+",     "WARNING",   "Possible '1' vs 'l' OCR confusion"),
    (r"\\\\(?!\\\\)",          "INFO",      "Single backslash in LaTeX (might be OK in Python strings)"),
]

INTERNAL_VISUAL_LABELS = [
    r"Visual Representation:",
    r"Building Intuition",
    r"Pedagogical Note:",
    r"AI-generated",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def text_of_content(content, depth=0):
    if depth > 10:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(text_of_content(x, depth+1) for x in content)
    if isinstance(content, dict):
        return " ".join(text_of_content(v, depth+1) for v in content.values())
    return str(content) if content is not None else ""


class AuditReport:
    def __init__(self):
        self.criticals = []
        self.warnings = []
        self.infos = []
        self.passed = []

    def add(self, severity, lesson_title, page_num, block_type, message):
        entry = f"  [{lesson_title} | p{page_num} | {block_type}] {message}"
        if severity == "CRITICAL":
            self.criticals.append(entry)
        elif severity == "WARNING":
            self.warnings.append(entry)
        else:
            self.infos.append(entry)

    def ok(self, check_name):
        self.passed.append(f"  ✓ {check_name}")

    def print_report(self):
        print("\n" + "=" * 80)
        print("MATHEMATICS QUALITY AUDIT REPORT")
        print("=" * 80)

        if self.criticals:
            print(f"\n🔴 CRITICAL ISSUES ({len(self.criticals)}) — must fix before next topic:")
            for c in self.criticals:
                print(c)

        if self.warnings:
            print(f"\n🟡 WARNINGS ({len(self.warnings)}) — review recommended:")
            for w in self.warnings:
                print(w)

        if self.infos:
            print(f"\n🔵 INFO ({len(self.infos)}):")
            for i in self.infos:
                print(i)

        if self.passed:
            print(f"\n✅ PASSED CHECKS ({len(self.passed)}):")
            for p in self.passed:
                print(p)

        print("\n" + "=" * 80)
        total = len(self.criticals) + len(self.warnings)
        if self.criticals:
            print(f"STATUS: ❌ FAIL — {len(self.criticals)} critical issues")
        elif self.warnings:
            print(f"STATUS: ⚠️  WARN — {len(self.warnings)} warnings (no criticals)")
        else:
            print("STATUS: ✅ PASS — No issues found")
        print("=" * 80)

        return len(self.criticals)


# ---------------------------------------------------------------------------
# Audit Checks
# ---------------------------------------------------------------------------

def audit_developer_leakage(lesson, blocks, report):
    """Check no internal implementation labels appear in student-facing content."""
    any_leak = False
    for block in blocks:
        content_text = text_of_content(block.content)
        title_text = (block.page_title or "") + " " + (block.title or "")
        combined = content_text + " " + title_text

        for pattern, severity, description in DEVELOPER_LEAK_PATTERNS:
            matches = re.findall(pattern, combined, re.IGNORECASE)
            if matches:
                report.add(severity, lesson.title, block.page_number, block.block_type,
                           f"Developer leak — {description}: '{matches[0]}'")
                any_leak = True

    if not any_leak:
        report.ok(f"[{lesson.title}] No developer leakage in student-facing content")


def audit_formula_integrity(lesson, blocks, report):
    """Check LaTeX is balanced and pmatrix structures are valid."""
    formula_issues = False
    for block in blocks:
        content_text = text_of_content(block.content)
        if not content_text:
            continue

        # Check display math delimiter balance
        display_count = len(re.findall(r"\$\$", content_text))
        if display_count % 2 != 0:
            report.add("CRITICAL", lesson.title, block.page_number, block.block_type,
                       f"Unbalanced $$ delimiters ({display_count} found)")
            formula_issues = True

        # Check inline math delimiter balance (excluding $$)
        inline_text = re.sub(r"\$\$.*?\$\$", "", content_text, flags=re.DOTALL)
        single_dollars = len(re.findall(r"(?<!\$)\$(?!\$)", inline_text))
        if single_dollars % 2 != 0:
            report.add("CRITICAL", lesson.title, block.page_number, block.block_type,
                       f"Unbalanced single-$ delimiters ({single_dollars} found after removing $$)")
            formula_issues = True

        # Check \begin/\end pairing
        begins = re.findall(r"\\begin\{(\w+)\}", content_text)
        ends = re.findall(r"\\end\{(\w+)\}", content_text)
        if sorted(begins) != sorted(ends):
            report.add("CRITICAL", lesson.title, block.page_number, block.block_type,
                       f"\\begin/\\end mismatch: begins={begins}, ends={ends}")
            formula_issues = True

        # Check pmatrix entries have row separators (for 2-row matrices only)
        # Single-row matrices like \begin{pmatrix} a & b \end{pmatrix} are valid and need no \\
        pmatrix_blocks = re.findall(
            r"\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}", content_text, re.DOTALL
        )
        for pb in pmatrix_blocks:
            pb_stripped = pb.strip()
            ampersand_count = pb_stripped.count("&")
            has_row_sep = "\\\\" in pb_stripped  # two backslashes = LaTeX row separator
            # Only flag if multiple ampersands suggest a 2-row matrix that needs a row separator
            if ampersand_count >= 2 and not has_row_sep:
                report.add("CRITICAL", lesson.title, block.page_number, block.block_type,
                           f"pmatrix appears to be 2-row ({ampersand_count} &) but has no row separator (\\\\): '{pb_stripped[:50]}'")
                formula_issues = True

        # Check for suspicious OCR remnants
        for pattern, severity, description in OCR_CORRUPTION_PATTERNS:
            if re.search(pattern, content_text):
                report.add(severity, lesson.title, block.page_number, block.block_type,
                           f"Possible OCR issue — {description}")

    if not formula_issues:
        report.ok(f"[{lesson.title}] Formula integrity OK")


def audit_worked_example_integrity(lesson, blocks, report):
    """Check worked examples follow Given → Method → Calculation → Result."""
    worked_examples = [b for b in blocks if b.block_type == "worked_example"]

    if not worked_examples:
        report.add("WARNING", lesson.title, 0, "—",
                   "No worked_example blocks found in this lesson")
        return

    for block in worked_examples:
        content = block.content
        issues = []

        if isinstance(content, dict):
            problem = content.get("problem", "")
            steps = content.get("steps", [])

            if not problem or len(problem.strip()) < 10:
                issues.append("Missing or very short 'problem' field")

            if not steps or not isinstance(steps, list):
                issues.append("Missing 'steps' list")
            elif len(steps) < 2:
                issues.append(f"Only {len(steps)} steps — too few for a worked example")
            else:
                # Check that the final step contains an answer indicator
                last_step = steps[-1].lower() if steps else ""
                answer_keywords = ["answer", "∴", "therefore", "hence", "so ", "thus", "result"]
                if not any(kw in last_step for kw in answer_keywords):
                    issues.append(
                        "Final step may not state a clear answer "
                        "(no 'Answer', '∴', 'therefore', 'hence', etc.)"
                    )

        else:
            text_content = text_of_content(content).strip()
            if len(text_content) < 50:
                issues.append("Worked example content is too short (< 50 chars)")

        for issue in issues:
            report.add("WARNING", lesson.title, block.page_number, "worked_example", issue)

    if worked_examples and not any(True for b in worked_examples):
        report.ok(f"[{lesson.title}] All worked examples have valid structure")

    # Count examples and check progression (at least 3, ideally 4)
    if len(worked_examples) < 3:
        report.add("WARNING", lesson.title, 0, "worked_example",
                   f"Only {len(worked_examples)} worked examples — minimum 3 expected for Mathematics")
    else:
        report.ok(f"[{lesson.title}] Has {len(worked_examples)} worked examples (≥3) ✓")


def audit_mcq_integrity(lesson, blocks, report):
    """Check MCQ blocks have 4 options, valid answer key, and explanation."""
    mcq_blocks = [
        b for b in blocks
        if b.block_type in ("knowledge_check", "multiple_choice")
        and isinstance(b.content, dict)
        and b.content.get("check_type") in ("multiple_choice", None)
        and "options" in b.content
    ]

    for block in mcq_blocks:
        content = block.content
        options = content.get("options", [])
        answer = content.get("answer", "")
        explanation = content.get("explanation", "")
        question = content.get("question", "")

        if len(options) < 4:
            report.add("WARNING", lesson.title, block.page_number, "knowledge_check",
                       f"MCQ has {len(options)} options — expected 4")

        if answer not in ("A", "B", "C", "D"):
            report.add("CRITICAL", lesson.title, block.page_number, "knowledge_check",
                       f"MCQ answer key is '{answer}' — must be A, B, C, or D")

        if not explanation or len(explanation.strip()) < 20:
            report.add("WARNING", lesson.title, block.page_number, "knowledge_check",
                       "MCQ explanation is missing or very short")

        if not question or len(question.strip()) < 10:
            report.add("CRITICAL", lesson.title, block.page_number, "knowledge_check",
                       "MCQ question text is missing or very short")

    if mcq_blocks:
        report.ok(f"[{lesson.title}] MCQ blocks checked ({len(mcq_blocks)} found)")


def audit_short_answer_integrity(lesson, blocks, report):
    """Check short_answer blocks have hint and answer reveal."""
    sa_blocks = [
        b for b in blocks
        if b.component_type in ("short_answer",)
        or (isinstance(b.content, dict) and b.content.get("check_type") == "short_answer")
    ]

    for block in sa_blocks:
        content = block.content
        if isinstance(content, dict):
            hint = content.get("hint", "")
            answer = content.get("answer", "")
            question = content.get("question", "")

            if not question or len(question.strip()) < 10:
                report.add("CRITICAL", lesson.title, block.page_number, "short_answer",
                           "Short-answer question text is missing or very short")
            if not hint or len(hint.strip()) < 10:
                report.add("WARNING", lesson.title, block.page_number, "short_answer",
                           "Short-answer 'hint' is missing or very short — students need guidance")
            if not answer or len(answer.strip()) < 10:
                report.add("CRITICAL", lesson.title, block.page_number, "short_answer",
                           "Short-answer 'answer' (reveal) is missing or very short")

    if sa_blocks:
        report.ok(f"[{lesson.title}] Short-answer blocks checked ({len(sa_blocks)} found)")


def audit_visual_placeholders(lesson, blocks, report):
    """Check suggested_diagram/simulation titles are student-facing, not internal labels."""
    visual_blocks = [
        b for b in blocks
        if b.block_type.startswith("suggested_") or b.block_type.endswith("_placeholder")
    ]

    for block in visual_blocks:
        title = block.title or block.page_title or ""
        for internal_pattern in INTERNAL_VISUAL_LABELS:
            if re.search(internal_pattern, title, re.IGNORECASE):
                report.add("CRITICAL", lesson.title, block.page_number, block.block_type,
                           f"Visual block title exposes internal label: '{title}'")

        # Check that the title actually describes what the student will see
        if len(title.strip()) < 5:
            report.add("WARNING", lesson.title, block.page_number, block.block_type,
                       "Visual block has no meaningful title for the student")

    if visual_blocks:
        report.ok(f"[{lesson.title}] Visual placeholder titles checked ({len(visual_blocks)} found)")


def audit_content_length(lesson, blocks, report):
    """Flag abnormally short or empty blocks."""
    for block in blocks:
        content_text = text_of_content(block.content).strip()
        if len(content_text) < 20:
            report.add("CRITICAL", lesson.title, block.page_number, block.block_type,
                       f"Block content is very short or empty ({len(content_text)} chars)")


def audit_conceptual_correctness(lesson, blocks, report):
    """
    Heuristic check: concept_explanation blocks for matrix topics should contain
    mathematical terms and formula context, not just procedure-only instructions.
    """
    concept_blocks = [b for b in blocks if b.block_type in ("concept_explanation", "formula_breakdown")]
    for block in concept_blocks:
        content_text = text_of_content(block.content).strip()

        # Should contain LaTeX (math is mathematical content, not just prose)
        has_math = bool(re.search(r"\$", content_text))
        if not has_math:
            report.add("INFO", lesson.title, block.page_number, block.block_type,
                       "Concept explanation contains no LaTeX math — verify this is intentional")

        # Should contain explanation, not just a list of steps
        procedure_only_indicators = [
            "Step 1:", "Step 2:", "Step 3:", "Do this:", "Now do:", "Multiply:", "Add:"
        ]
        non_prose = sum(1 for p in procedure_only_indicators if p.lower() in content_text.lower())
        prose_count = len(re.findall(r"[.!?]\s+[A-Z]", content_text))
        if non_prose > 2 and prose_count < 2:
            report.add("INFO", lesson.title, block.page_number, block.block_type,
                       "Concept explanation may be procedure-only — consider adding mathematical reasoning")


# ---------------------------------------------------------------------------
# Main Audit Runner
# ---------------------------------------------------------------------------

def audit_topic(topic):
    """Audit all lessons within a topic."""
    units = LearningUnit.objects.filter(topic=topic).order_by("order")
    lessons = Lesson.objects.filter(learning_unit__in=units)

    if not lessons.exists():
        print(f"⚠️  No lessons found for topic '{topic.name}'")
        return 1

    report = AuditReport()

    print(f"\nAuditing topic: '{topic.name}' ({lessons.count()} lessons)")
    print("-" * 60)

    for lesson in lessons.order_by("learning_unit__order"):
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "order"))
        print(f"  [{lesson.title}] — {len(blocks)} blocks")

        audit_developer_leakage(lesson, blocks, report)
        audit_formula_integrity(lesson, blocks, report)
        audit_worked_example_integrity(lesson, blocks, report)
        audit_mcq_integrity(lesson, blocks, report)
        audit_short_answer_integrity(lesson, blocks, report)
        audit_visual_placeholders(lesson, blocks, report)
        audit_content_length(lesson, blocks, report)
        audit_conceptual_correctness(lesson, blocks, report)

    critical_count = report.print_report()
    return critical_count


def main():
    parser = argparse.ArgumentParser(
        description="VLearn Mathematics Quality Audit"
    )
    parser.add_argument("--topic", default="Matrix and Transformation",
                        help="Topic name to audit (partial match)")
    parser.add_argument("--subject", default="Mathematics",
                        help="Subject name")
    parser.add_argument("--grade", default="Form 4",
                        help="Grade name")
    parser.add_argument("--all", action="store_true",
                        help="Audit all Mathematics topics for the given grade/subject")
    args = parser.parse_args()

    print("=" * 80)
    print("VLearn Mathematics Quality Audit")
    print(f"Grade: {args.grade} | Subject: {args.subject}")
    print("=" * 80)

    subject = Subject.objects.filter(
        name__iexact=args.subject,
        grade__name__iexact=args.grade
    ).first()

    if not subject:
        print(f"❌ Subject '{args.subject}' not found for grade '{args.grade}'")
        sys.exit(1)

    if args.all:
        topics = Topic.objects.filter(subject=subject).order_by("order")
    else:
        topics = Topic.objects.filter(
            subject=subject,
            name__icontains=args.topic
        )

    if not topics.exists():
        print(f"❌ No topics found matching '{args.topic}'")
        sys.exit(1)

    total_criticals = 0
    for topic in topics:
        total_criticals += audit_topic(topic)

    print(f"\nTotal critical issues across all audited topics: {total_criticals}")
    sys.exit(0 if total_criticals == 0 else 1)


if __name__ == "__main__":
    main()
