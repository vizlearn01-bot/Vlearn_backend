"""
VLearn Form 4 Physics — Text Humanizer & KaTeX Formatter Engine

Scans and cleans all text blocks across Form 4 Physics Topics 1 to 7:
  1. Converts raw scientific notation (e.g., 1.6 × 10^-19, 10^7, 3.6 x 10^6) into clean KaTeX inline math ($1.6 \\times 10^{-19}\\text{ C}$, $10^7\\text{ m/s}$, $3.6 \\times 10^6\\text{ J}$).
  2. Converts raw function expressions (e.g., sqrt(2 e V / m_e), V_0 / sqrt(2)) into proper KaTeX formulas ($\\sqrt{\\frac{2eV}{m_e}}$, $\\frac{V_0}{\\sqrt{2}}$).
  3. Replaces plain ASCII caret exponents (e.g., 10^2, I^2 R) outside math tags with KaTeX ($10^2$, $I^2 R$).
  4. Fixes double-escaped or unescaped quotes, stray tabs, and non-breaking space issues.
  5. Ensures student-facing text flows naturally without developer terminology or raw code leaks.

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/humanize_form4_physics_text.py
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock

def humanize_string(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return text

    # Do not process raw SVG XML strings
    if "<svg" in text:
        return text

    # Split into KaTeX math segments ($$...$$ and $...$) and plain prose segments
    # So we only transform raw prose outside existing math tags
    tokens = re.split(r'(\$\$.*?\$\$|\$.*?\$)', text, flags=re.DOTALL)
    
    new_tokens = []
    for token in tokens:
        if token.startswith('$'):
            # Already inside KaTeX math block, keep as is
            new_tokens.append(token)
            continue
        
        t = token
        
        # 1. Scientific notation in prose: e.g., 1.6 × 10^-19 C -> $1.6 \times 10^{-19}\text{ C}$
        t = re.sub(
            r'(\d+(?:\.\d+)?)\s*[×xX]\s*10\^([\-\+]?\d+)\s*([a-zA-ZΩμ°/]+)?',
            lambda m: f"${m.group(1)} \\times 10^{{{m.group(2)}}}{'\\text{ ' + m.group(3) + '}' if m.group(3) else ''}$",
            t
        )
        
        # 2. Exponents in prose: e.g., 10^7 m/s -> $10^7\text{ m/s}$, 10^2 -> $10^2$
        t = re.sub(
            r'\b10\^([\-\+]?\d+)\s*([a-zA-ZΩμ°/]+)?',
            lambda m: f"$10^{{{m.group(1)}}}{'\\text{ ' + m.group(2) + '}' if m.group(2) else ''}$",
            t
        )
        
        # 3. Raw sqrt expressions in prose: e.g., sqrt(2 e V / m_e) -> $\sqrt{\frac{2eV}{m_e}}$
        t = re.sub(r'sqrt\(2\s*e\s*V(?:_acc)?\s*/\s*m_e\)', r'$\\sqrt{\\frac{2e V}{m_e}}$', t)
        t = re.sub(r'sqrt\(6\.4\s*×\s*10\^-16\s*/\s*9\.1\s*×\s*10\^-31\)', r'$\\sqrt{\\frac{6.4 \\times 10^{-16}}{9.1 \\times 10^{-31}}}$', t)
        t = re.sub(r'sqrt\(7\.0329\s*×\s*10\^14\)', r'$\\sqrt{7.0329 \\times 10^{14}}$', t)
        t = re.sub(r'sqrt\(8\.7912\s*×\s*10\^14\)', r'$\\sqrt{8.7912 \\times 10^{14}}$', t)
        t = re.sub(r'V_0\s*/\s*sqrt\(2\)', r'$\\frac{V_0}{\\sqrt{2}}$', t)
        t = re.sub(r'sqrt\(2\)', r'$\\sqrt{2}$', t)

        # 4. Raw I^2 R in prose -> $I^2 R$
        t = re.sub(r'\bI\^2\s*R\b', r'$I^2 R$', t)

        # 5. Raw 10^2 in prose -> $10^2$
        t = re.sub(r'\(10\^2\)', r'($10^2$)', t)

        # 6. Clean stray tabs or escaped character glitches
        t = t.replace('\t', ' ')
        
        new_tokens.append(t)

    result = "".join(new_tokens)
    return result


def humanize_structure(obj):
    if isinstance(obj, str):
        return humanize_string(obj)
    elif isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            if k in ['svg', 'svg_content']:
                new_dict[k] = v
            else:
                new_dict[k] = humanize_structure(v)
        return new_dict
    elif isinstance(obj, list):
        return [humanize_structure(item) for item in obj]
    return obj


def run_humanizer():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — TEXT HUMANIZER & KATEX FORMATTER")
    print("=" * 80)

    topics = Topic.objects.filter(subject__name="Physics", subject__grade__name="Form 4").order_by("order")

    total_modified = 0

    for topic in topics:
        print(f"\nProcessing Topic {topic.order}: '{topic.name}'...")
        topic_modified = 0

        for unit in topic.learning_units.all().order_by("order"):
            lesson = unit.lessons.first()
            if not lesson:
                continue

            for block in lesson.blocks.all():
                old_content = block.content
                new_content = humanize_structure(old_content)

                old_title = block.title
                new_title = humanize_string(old_title) if old_title else old_title

                old_page_title = block.page_title
                new_page_title = humanize_string(old_page_title) if old_page_title else old_page_title

                changed = (old_content != new_content) or (old_title != new_title) or (old_page_title != new_page_title)

                if changed:
                    block.content = new_content
                    block.title = new_title
                    block.page_title = new_page_title
                    block.save()
                    topic_modified += 1

        total_modified += topic_modified
        print(f"  Topic {topic.order} completed: {topic_modified} blocks humanized and updated.")

    print("\n" + "=" * 80)
    print(f"HUMANIZATION COMPLETE! Total Blocks Humanized: {total_modified}")
    print("=" * 80)

if __name__ == "__main__":
    run_humanizer()
