"""
Form 4 Physics — Master Math & Symbol Sanity Cleaner

Scans every block in Topics 1-11, replaces all raw escape artifacts like
\\$\\alpha\\$, \\$\\beta^-\\$, \\$\\$^{0}_{0}\\gamma\\$, etc. with clean, valid KaTeX math tags ($...$).
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock

def sanitize_block_text(text: str) -> str:
    if not isinstance(text, str):
        return text

    new_text = text

    # Remove escaped backslashes before dollar signs
    new_text = new_text.replace(r"\$\alpha\$", r"$\alpha$")
    new_text = new_text.replace(r"\$\beta^-\$", r"$\beta^-$")
    new_text = new_text.replace(r"\$\beta\$", r"$\beta$")
    new_text = new_text.replace(r"\$\gamma\$", r"$\gamma$")
    new_text = new_text.replace(r"\$\$", r"$")

    # Regex to clean any \\$ patterns
    new_text = re.sub(r'\\+\$', '$', new_text)

    # Specific nuclide and symbol fixes
    new_text = new_text.replace("Nuclide Notation (^{A}_{Z}X)", r"Nuclide Notation ($^{A}_{Z}\text{X}$)")
    new_text = new_text.replace("Nuclide Notation ^{A}_{Z}X", r"Nuclide Notation ($^{A}_{Z}\text{X}$)")

    return new_text

def clean_dict_obj(obj):
    if isinstance(obj, str):
        return sanitize_block_text(obj)
    elif isinstance(obj, list):
        return [clean_dict_obj(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: clean_dict_obj(v) for k, v in obj.items()}
    return obj

def run_master_cleanup():
    print("=" * 80)
    print("MASTER MATH & SYMBOL SANITY CLEANER FOR FORM 4 PHYSICS")
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

                new_title = sanitize_block_text(block.title or "")
                if new_title != block.title:
                    block.title = new_title
                    changed = True

                new_page_title = sanitize_block_text(block.page_title or "")
                if new_page_title != block.page_title:
                    block.page_title = new_page_title
                    changed = True

                if isinstance(block.content, dict):
                    new_content = clean_dict_obj(block.content)
                    if new_content != block.content:
                        block.content = new_content
                        changed = True

                if changed:
                    block.save()
                    topic_updated += 1
                    updated_count += 1

        print(f"Topic {topic.order:2d}: '{topic.name}' -> {topic_updated} blocks sanitized.")

    print("=" * 80)
    print(f"MASTER CLEANUP COMPLETE! Total Blocks Updated: {updated_count}")
    print("=" * 80)

if __name__ == "__main__":
    run_master_cleanup()
