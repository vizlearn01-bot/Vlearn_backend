"""
VLearn Form 4 Physics — Complete Prose Humanizer & Parenthetical Symbol Remover

Scans all blocks in Topics 1 to 11 and removes awkward parenthetical KaTeX symbols
such as ($lpha$), ($\alpha$), ($\beta^-$), ($\gamma$), (^{A}_{Z}\text{X}), ($\lambda$), etc.
that clutter the student view. Replaces them with natural, fluent textbook English.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock

# Specific string & regex patterns to strip/humanize
REPLACEMENTS = [
    # Remove parenthetical Greek symbols after English words
    (r"Alpha\s*\(\s*\\?\$?\\?alpha\\?\$?\s*\)", "Alpha"),
    (r"Beta\s*\(\s*\\?\$?\\?beta\^-\\?\$?\s*\)", "Beta"),
    (r"Beta\s*\(\s*\\?\$?\\?beta\\?\$?\s*\)", "Beta"),
    (r"Gamma\s*\(\s*\\?\$?\\?gamma\\?\$?\s*\)", "Gamma"),
    (r"X-Rays\s*\(\s*X-rays\s*\)", "X-Rays"),

    # Standalone parenthetical symbols
    (r"\(\s*\\?\$?\\?alpha\\?\$?\s*\)", ""),
    (r"\(\s*\\?\$?\\?beta\^-\\?\$?\s*\)", ""),
    (r"\(\s*\\?\$?\\?beta\\?\$?\s*\)", ""),
    (r"\(\s*\\?\$?\\?gamma\\?\$?\s*\)", ""),
    (r"\(\s*\^\{A\}_\{Z\}\\?text\{X\}\s*\)", ""),
    (r"\(\s*\^\{A\}_\{Z\}X\s*\)", ""),
    (r"Nuclide Notation\s*\(\s*\^\{A\}_\{Z\}\\?text\{X\}\s*\)", "Nuclide Notation"),

    # Clean double spaces caused by removal
    (r"\s{2,}", " "),
]

def humanize_text_string(text: str) -> str:
    if not isinstance(text, str):
        return text

    new_text = text

    # Apply direct string cleanups first
    new_text = new_text.replace("Alpha ($\alpha$)", "Alpha")
    new_text = new_text.replace("Alpha ($lpha$)", "Alpha")
    new_text = new_text.replace("Beta ($\beta^-$)", "Beta")
    new_text = new_text.replace("Beta ($eta^-$)", "Beta")
    new_text = new_text.replace("Gamma ($\gamma$)", "Gamma")
    new_text = new_text.replace("Nuclide Notation ($^{A}_{Z}\text{X}$)", "Nuclide Notation")
    new_text = new_text.replace("Nuclide Notation (^{A}_{Z}X)", "Nuclide Notation")

    # Apply regex replacements
    for pattern, replacement in REPLACEMENTS:
        new_text = re.sub(pattern, replacement, new_text)

    # Clean any leftover trailing spaces before punctuation
    new_text = re.sub(r'\s+([,\.\?\:])', r'\1', new_text)
    return new_text.trim() if hasattr(new_text, 'trim') else new_text.strip()

def clean_block_data(obj):
    if isinstance(obj, str):
        return humanize_text_string(obj)
    elif isinstance(obj, list):
        return [clean_block_data(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: clean_block_data(v) for k, v in obj.items()}
    return obj

def run_prose_humanization():
    print("=" * 80)
    print("FORM 4 PHYSICS — PROSE HUMANIZATION & SYMBOL CLEANUP")
    print("=" * 80)

    topics = Topic.objects.filter(subject__name="Physics", subject__grade__name="Form 4").order_by("order")

    total_blocks_humanized = 0

    for topic in topics:
        topic_humanized = 0
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            if not lesson:
                continue
            for block in lesson.blocks.all():
                changed = False

                if block.title:
                    new_title = humanize_text_string(block.title)
                    if new_title != block.title:
                        block.title = new_title
                        changed = True

                if block.page_title:
                    new_page_title = humanize_text_string(block.page_title)
                    if new_page_title != block.page_title:
                        block.page_title = new_page_title
                        changed = True

                if isinstance(block.content, dict):
                    new_content = clean_block_data(block.content)
                    if new_content != block.content:
                        block.content = new_content
                        changed = True

                if changed:
                    block.save()
                    topic_humanized += 1
                    total_blocks_humanized += 1

        print(f"Topic {topic.order:2d}: '{topic.name}' -> {topic_humanized} blocks humanized.")

    print("=" * 80)
    print(f"HUMANIZATION COMPLETE! Total Blocks Humanized: {total_blocks_humanized}")
    print("=" * 80)

if __name__ == "__main__":
    run_prose_humanization()
