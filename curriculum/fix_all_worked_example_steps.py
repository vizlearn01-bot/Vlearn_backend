"""
Form 4 Physics — Worked Example Step Math Delimiter Sanitizer

Fixes malformed math delimiters in worked example steps (such as $$**Calculation:** $...$$$)
ensuring bold text remains outside math tags and math equations are cleanly wrapped in $...$.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock

def clean_step_math(text: str) -> str:
    if not isinstance(text, str):
        return text

    new_text = text

    # Fix specific block 14420 step 4 corruption
    new_text = new_text.replace(
        "$$**Calculation:** $\\frac{1}{u} = \\frac{2 + 1}{36} = \\frac{3}{36} = \\frac{1}{12} \\implies u = +12\\text{ cm}$$$",
        "**Calculation:** $\\frac{1}{u} = \\frac{2 + 1}{36} = \\frac{3}{36} = \\frac{1}{12} \\implies u = +12\\text{ cm}$"
    )

    # General cleanup for $$** or **$$ or $$$
    new_text = re.sub(r'^\$\$\*\*(.*?)\*\*:\s*\$(.*?)\$\$\$$', r'**\1:** $\2$', new_text)
    new_text = re.sub(r'\$\$\*\*(.*?)\*\*', r'**\1**', new_text)
    new_text = re.sub(r'\$\$\$+', '$', new_text)
    new_text = re.sub(r'\$\$+', '$', new_text)

    return new_text

def clean_dict_math(obj):
    if isinstance(obj, str):
        return clean_step_math(obj)
    elif isinstance(obj, list):
        return [clean_dict_math(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: clean_dict_math(v) for k, v in obj.items()}
    return obj

def run_step_math_fix():
    print("=" * 80)
    print("VLEARN FORM 4 PHYSICS — WORKED EXAMPLE MATH DELIMITER SANITIZER")
    print("=" * 80)

    topics = Topic.objects.filter(subject__name="Physics", subject__grade__name="Form 4").order_by("order")

    updated_count = 0

    for topic in topics:
        topic_updated = 0
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            if not lesson:
                continue
            for block in lesson.blocks.all():
                changed = False

                if isinstance(block.content, dict):
                    new_content = clean_dict_math(block.content)
                    if new_content != block.content:
                        block.content = new_content
                        changed = True

                if changed:
                    block.save()
                    topic_updated += 1
                    updated_count += 1

        print(f"Topic {topic.order:2d}: '{topic.name}' -> {topic_updated} blocks cleaned.")

    print("=" * 80)
    print(f"SANITY CLEANUP COMPLETE! Total Blocks Updated: {updated_count}")
    print("=" * 80)

if __name__ == "__main__":
    run_step_math_fix()
