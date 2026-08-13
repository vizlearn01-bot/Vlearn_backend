import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock

def audit_form3_chemistry():
    grade = Grade.objects.get(name="Form 3")
    subject = Subject.objects.get(grade=grade, name="Chemistry")
    topics = Topic.objects.filter(subject=subject).order_by("order")

    total_lessons = 0
    total_blocks = 0
    issues = []

    # Patterns to detect
    escaped_underscore_pattern = re.compile(r'\\[_]')
    broken_latex_pattern = re.compile(r'(\\\\[a-zA-Z]+|\$\s*\$|\\\(\s*\\\)|\$\w+\\_)')
    boilerplate_pattern = re.compile(r'(?i)by the end of this (module|lesson|concept|chapter|unit)')
    banned_meta_labels = [
        "real-world hook", "real world hook",
        "visualization",
        "misconception buster",
        "teacher note",
        "concept explanation",
        "understanding check",
        "worked example",
        "worked calculation",
        "authoring label",
        "misconception card",
        "learning objective",
        "step purpose"
    ]
    # Broken text patterns like "pprox", isolated hanging fragments before formulas/bold
    broken_text_patterns = [
        re.compile(r'\bpprox\b'),
        re.compile(r'(?<=\s)[b-zB-Z]\s*\(\$'), # isolated hanging non-'a' single letter before math
        re.compile(r'(?<=\s)[b-zB-Z]\s+\*\*[A-Z]'), # isolated hanging non-'a' single letter before bold
        re.compile(r'\\text\{\s*\}'),
    ]

    for topic in topics:
        lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
        for lesson in lessons:
            total_lessons += 1
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by("order")
            for block in blocks:
                total_blocks += 1
                content_str = json.dumps(block.content, ensure_ascii=False)
                title_str = block.title or ""
                page_title_str = block.page_title or ""

                # 1. Boilerplate learning objective
                if boilerplate_pattern.search(content_str):
                    match = boilerplate_pattern.search(content_str).group(0)
                    issues.append({
                        "category": "BOILERPLATE_LEARNING_OBJECTIVE",
                        "topic": topic.name,
                        "lesson_id": lesson.id,
                        "lesson_title": lesson.title,
                        "block_id": block.id,
                        "component_type": block.component_type,
                        "page_number": block.page_number,
                        "detail": f"Contains boilerplate '{match}' in content: {content_str[:120]}..."
                    })

                # 2. Escaped underscores or formula formatting
                if escaped_underscore_pattern.search(content_str) or r"\_" in content_str:
                    issues.append({
                        "category": "FORMULA_FORMATTING",
                        "topic": topic.name,
                        "lesson_id": lesson.id,
                        "lesson_title": lesson.title,
                        "block_id": block.id,
                        "component_type": block.component_type,
                        "page_number": block.page_number,
                        "detail": f"Contains escaped underscores in content: {content_str[:150]}"
                    })

                # 3. Broken text around formulas
                for b_pat in broken_text_patterns:
                    if b_pat.search(content_str):
                        match = b_pat.search(content_str).group(0)
                        issues.append({
                            "category": "BROKEN_TEXT",
                            "topic": topic.name,
                            "lesson_id": lesson.id,
                            "lesson_title": lesson.title,
                            "block_id": block.id,
                            "component_type": block.component_type,
                            "page_number": block.page_number,
                            "detail": f"Matched pattern '{b_pat.pattern}' ('{match}') in: {content_str[:150]}"
                        })

                # 4. Internal labels exposed in titles or page titles
                for tag in banned_meta_labels:
                    if tag in title_str.lower():
                        issues.append({
                            "category": "INTERNAL_LABEL_EXPOSED",
                            "topic": topic.name,
                            "lesson_id": lesson.id,
                            "lesson_title": lesson.title,
                            "block_id": block.id,
                            "component_type": block.component_type,
                            "page_number": block.page_number,
                            "detail": f"Block title contains '{tag}': '{title_str}'"
                        })
                    if tag in page_title_str.lower():
                        issues.append({
                            "category": "INTERNAL_LABEL_EXPOSED",
                            "topic": topic.name,
                            "lesson_id": lesson.id,
                            "lesson_title": lesson.title,
                            "block_id": block.id,
                            "component_type": block.component_type,
                            "page_number": block.page_number,
                            "detail": f"Page title contains '{tag}': '{page_title_str}'"
                        })

                # 5. Malformed LaTeX / unclosed math
                # Check for unclosed single $ or $$ in string values
                def check_unclosed_dollars(obj):
                    if isinstance(obj, str):
                        # Count $ excluding escaped \$
                        unescaped = re.sub(r'\\\$', '', obj)
                        # Count single dollars and double dollars
                        # If count of $ is odd, it's malformed
                        dollar_count = unescaped.count('$')
                        if dollar_count % 2 != 0:
                            issues.append({
                                "category": "MALFORMED_LATEX",
                                "topic": topic.name,
                                "lesson_id": lesson.id,
                                "lesson_title": lesson.title,
                                "block_id": block.id,
                                "component_type": block.component_type,
                                "page_number": block.page_number,
                                "detail": f"Odd number of dollar signs ({dollar_count}) in text: {obj[:150]}"
                            })
                    elif isinstance(obj, dict):
                        for k, v in obj.items():
                            check_unclosed_dollars(v)
                    elif isinstance(obj, list):
                        for item in obj:
                            check_unclosed_dollars(item)

                check_unclosed_dollars(block.content)

    print(f"============================================================")
    print(f"FORM 3 CHEMISTRY AUDIT RESULTS")
    print(f"============================================================")
    print(f"Total Lessons Inspected: {total_lessons}")
    print(f"Total Blocks Inspected:  {total_blocks}")
    print(f"Total Potential Issues Found: {len(issues)}")
    print(f"============================================================")

    # Group issues by category
    by_cat = {}
    for iss in issues:
        by_cat.setdefault(iss["category"], []).append(iss)

    for cat, cat_issues in by_cat.items():
        print(f"\n--- {cat} ({len(cat_issues)} issues) ---")
        for i in cat_issues[:15]:
            print(f"  [Lesson {i['lesson_id']}: {i['lesson_title']} | Page {i['page_number']}] {i['detail']}")
        if len(cat_issues) > 15:
            print(f"  ... and {len(cat_issues) - 15} more")

if __name__ == "__main__":
    audit_form3_chemistry()
