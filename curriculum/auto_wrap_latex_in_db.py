"""
Form 4 Physics — Auto-Wrap Unwrapped LaTeX & Fix Student UI Delimiters

Finds any raw LaTeX symbols (nuclides, subscripts, superscripts, Greek letters, math functions)
that are missing $...$ delimiters and auto-wraps them cleanly into valid KaTeX math tags ($...$).
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock

# Regex matching unwrapped nuclide / superscript / subscript / latex commands outside $...$
UNWRAPPED_PATTERNS = [
    # Nuclide notation: ^{A}_{Z}\text{X} or ^{A}_{Z}X or \text{X}
    (r'(?<!\$)\^\{[^\}]+\}_\{[^\}]+\}(?:\\text\{[^\}]+\}|[A-Za-z]+)(?!\$)', lambda m: f"${m.group(0)}$"),
    # Superscript / subscript combos: ^{A} or _{Z}
    (r'(?<!\$)\^\{[^\}]+\}(?!\$)', lambda m: f"${m.group(0)}$"),
    (r'(?<!\$)_\{[^\}]+\}(?!\$)', lambda m: f"${m.group(0)}$"),
    # Standalone Greek letters outside math: \alpha, \beta, \gamma, \lambda, \Delta, \sigma, \mu, \Omega
    (r'(?<!\$)\\(alpha|beta|gamma|lambda|Delta|sigma|mu|Omega|theta|pi|rho|tau|phi|omega)(?!\$)', lambda m: f"${m.group(0)}$"),
    # Unwrapped \text{...} or \frac{...}{...}
    (r'(?<!\$)\\(text|frac|sqrt)\{[^\}]+\}(?:\{[^\}]+\})?(?!\$)', lambda m: f"${m.group(0)}$"),
]

def fix_latex_delimiters(text: str) -> str:
    if not isinstance(text, str):
        return text

    new_text = text

    # First clean common raw artifact patterns
    new_text = new_text.replace("\x07lpha", r"$\alpha$")
    new_text = new_text.replace("\x08eta", r"$\beta$")
    new_text = new_text.replace("($lpha$)", r"($\alpha$)")
    new_text = new_text.replace("($eta^-$)", r"($\beta^-$)")
    new_text = new_text.replace("($eta$)", r"($\beta$)")
    new_text = new_text.replace("(lpha)", r"($\alpha$)")
    new_text = new_text.replace("(eta^-)", r"($\beta^-$)")
    new_text = new_text.replace("(gamma)", r"($\gamma$)")
    new_text = new_text.replace("Nuclide Notation (^{A}_{Z}X)", r"Nuclide Notation ($^{A}_{Z}\text{X}$)")
    new_text = new_text.replace("Nuclide Notation ^{A}_{Z}X", r"Nuclide Notation ($^{A}_{Z}\text{X}$)")

    # Clean double escaped backslashes in math
    new_text = re.sub(r'\\+\$', '$', new_text)
    new_text = new_text.replace(r"\\alpha", r"\alpha")
    new_text = new_text.replace(r"\\beta", r"\beta")
    new_text = new_text.replace(r"\\gamma", r"\gamma")
    new_text = new_text.replace(r"\\text", r"\text")

    # Split string into outside math vs inside math
    parts = re.split(r'(\$\$.*?\$\$|\$.*?\$)', new_text, flags=re.DOTALL)
    cleaned_parts = []

    for idx, part in enumerate(parts):
        if idx % 2 == 0:  # Outside math
            p_clean = part
            # Wrap any nuclides, superscripts, subscripts, or greek letters found outside math
            # 1. Nuclide notation: ^{A}_{Z}\text{X} or ^{A}_{Z}X
            p_clean = re.sub(r'(\^\{[0-9m+-]+\}_\{[0-9]+\}(?:\\text\{[A-Za-z]+\}|[A-Za-z]+))', r'$\1$', p_clean)
            # 2. Standalone nuclides like ^{238}_{92}\text{U}
            p_clean = re.sub(r'(\^\{[^\}]+\}_\{[^\}]+\}(?:\\text\{[^\}]+\})?)', r'$\1$', p_clean)
            # 3. Unwrapped Greek letters: \alpha, \beta, \gamma, \lambda, \Delta, \sigma, \mu, \Omega
            p_clean = re.sub(r'(?<![a-zA-Z0-9\\])\\(alpha|beta|gamma|lambda|Delta|sigma|mu|Omega|theta|pi|rho|tau|phi|omega)(?![a-zA-Z])', r'$\\\1$', p_clean)
            # Fix any double dollars resulting from regex wrapping
            p_clean = re.sub(r'\$\$+', '$', p_clean)
            cleaned_parts.append(p_clean)
        else:  # Inside math
            # Ensure single backslashes for commands inside math
            m_clean = part
            m_clean = re.sub(r'\$\$+', '$', m_clean)
            cleaned_parts.append(m_clean)

    final_text = "".join(cleaned_parts)
    final_text = re.sub(r'\$\$+', '$', final_text)
    return final_text

def clean_dict_structure(obj):
    if isinstance(obj, str):
        return fix_latex_delimiters(obj)
    elif isinstance(obj, list):
        return [clean_dict_structure(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: clean_dict_structure(v) for k, v in obj.items()}
    return obj

def run_auto_wrap():
    print("=" * 80)
    print("FORM 4 PHYSICS — AUTO-WRAP UNWRAPPED LATEX IN DB")
    print("=" * 80)

    topics = Topic.objects.filter(subject__name="Physics", subject__grade__name="Form 4").order_by("order")

    total_blocks_updated = 0

    for topic in topics:
        topic_updated = 0
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            if not lesson:
                continue
            for block in lesson.blocks.all():
                changed = False

                new_title = fix_latex_delimiters(block.title or "")
                if new_title != block.title:
                    block.title = new_title
                    changed = True

                new_page_title = fix_latex_delimiters(block.page_title or "")
                if new_page_title != block.page_title:
                    block.page_title = new_page_title
                    changed = True

                if isinstance(block.content, dict):
                    new_content = clean_dict_structure(block.content)
                    if new_content != block.content:
                        block.content = new_content
                        changed = True

                if changed:
                    block.save()
                    topic_updated += 1
                    total_blocks_updated += 1

        print(f"Topic {topic.order:2d}: '{topic.name}' -> {topic_updated} blocks auto-wrapped.")

    print("=" * 80)
    print(f"AUTO-WRAP COMPLETE! Total Blocks Updated: {total_blocks_updated}")
    print("=" * 80)

if __name__ == "__main__":
    run_auto_wrap()
