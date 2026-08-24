"""
VLearn CBC Grade 7 — Home Science
Visualization Quality Enhancement Pass

Scans all diagram / suggested_diagram blocks for non-ASCII characters
(emojis, box-drawing symbols, typographic dashes, etc.) that break SVG
text rendering, and replaces them with clean ASCII equivalents or removes
them from SVG comment nodes entirely.

Strategy:
  - Box-drawing chars (─ ━ │ ┃ etc.)     → removed from comments, kept in text as '-'
  - Typographic dashes (— –)              → '-'
  - Left/right quotes (" " ' ')           → standard ' or "
  - Emoji (codepoint > 0x2000 excluding
    common maths/arrows like →)           → label replacement per emoji
  - Other non-ASCII                       → ASCII transliteration or removed
  - All changes are applied IN-PLACE to the database block's svg/svg_content field
  - Does NOT modify any other block fields (title, text content, etc.)
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, LessonBlock

# ---------------------------------------------------------------------------
# Emoji → text label map (common emojis found in Home Science SVGs)
# ---------------------------------------------------------------------------
EMOJI_MAP = {
    # Kitchen / cooking
    "\U0001F525": "[FIRE]",
    "\U0001F374": "[FORK]",
    "\U0001F944": "[LADLE]",
    "\U0001F372": "[POT]",
    "\U0001F373": "[COOKING]",
    "\U0001F9EA": "[TEST]",
    "\U0001F9F4": "[MAGNET]",
    "\U0001F9F9": "[BROOM]",
    "\U0001F9FC": "[SOAP]",
    "\U0001F9F7": "[PIN]",
    "\U0001F9F5": "[THREAD]",
    "\U0001F9F6": "[YARN]",
    "\U0001F48A": "[PILL]",
    "\U0001F4A7": "[DROPLET]",
    "\U0001F4A6": "[SWEAT]",
    "\U0001FAA3": "[BUCKET]",
    "\U0001FAA5": "[TOOTHBRUSH]",
    "\U0001F9D4": "[PERSON]",
    # Warning / safety
    "\u26A0": "[!]",
    "\u2714": "[OK]",
    "\u274C": "[X]",
    "\u2705": "[CHECK]",
    "\u2728": "[STAR]",
    "\U0001F6A8": "[ALERT]",
    "\U0001F6AB": "[NO]",
    "\U0001F6B3": "[NO-ENTRY]",
    "\U0001F6D1": "[STOP]",
    "\U0001F44D": "[YES]",
    "\U0001F44E": "[NO]",
    # Medical
    "\U0001FA79": "[BANDAGE]",
    "\u2764": "[HEART]",
    # Tools / household
    "\U0001F528": "[HAMMER]",
    "\u2702": "[SCISSORS]",
    "\u2709": "[ENVELOPE]",
    "\u270F": "[PENCIL]",
    "\u2763": "[HEART]",
    # Nature / food
    "\U0001F33F": "[HERB]",
    "\U0001F9C2": "[SALT]",
    "\U0001F6E2": "[OIL]",
    "\U0001F9C8": "[EGG]",
    "\U0001F95B": "[MILK]",
    "\U0001F40F": "[SHEEP]",
    "\U0001F9B4": "[BONE]",
    "\U0001F969": "[MEAT]",
    "\U0001F96C": "[LEAFY-GREEN]",
    "\U0001F35E": "[BREAD]",
    "\U0001F382": "[CAKE]",
    "\U0001F36A": "[COOKIE]",
    "\U0001F9C1": "[WHISK]",
    # Money / consumer ed
    "\U0001F4B0": "[MONEY-BAG]",
    "\U0001F4B5": "[BILL]",
    "\U0001F4B3": "[CARD]",
    "\U0001F6D2": "[CART]",
    "\U0001F4CA": "[CHART]",
    "\U0001F4CB": "[CLIPBOARD]",
    "\U0001F4C4": "[DOCUMENT]",
    "\U0001F9FE": "[RECEIPT]",
    # Cleaning
    "\U0001F9BA": "[CLOTH]",
    # Textile
    "\U0001F455": "[SHIRT]",
    "\U0001F9E5": "[JACKET]",
    "\U0001F9E6": "[GLOVES]",
    "\U0001F9E3": "[SCARF]",
    "\U0001F9F5": "[THREAD]",
    # Arrows (keep as text since SVG arrow entities work)
    "\u2192": "->",
    "\u2190": "<-",
    "\u2191": "^",
    "\u2193": "v",
    "\u21D2": "=>",
    "\u2713": "OK",
    "\u2717": "X",
    # Brackets/math that look ok but still fail some renderers
    "\u2248": "~=",
    "\u00B0": " deg",
    "\u00B2": "2",
    "\u00B3": "3",
    # Box-drawing / block elements
    "\u2500": "-",
    "\u2501": "-",
    "\u2502": "|",
    "\u2503": "|",
    "\u250C": "+",
    "\u2510": "+",
    "\u2514": "+",
    "\u2518": "+",
    "\u251C": "+",
    "\u2524": "+",
    "\u252C": "+",
    "\u2534": "+",
    "\u253C": "+",
    "\u2550": "=",
    "\u2551": "|",
    "\u2554": "+",
    "\u2557": "+",
    "\u255A": "+",
    "\u255D": "+",
    "\u2560": "+",
    "\u2563": "+",
    "\u2566": "+",
    "\u2569": "+",
    "\u256C": "+",
    "\u2580": "#",
    "\u2584": "#",
    "\u2588": "#",
    "\u2591": ".",
    "\u2592": "#",
    "\u2593": "#",
    # Typography
    "\u2014": "-",   # em dash
    "\u2013": "-",   # en dash
    "\u2018": "'",
    "\u2019": "'",
    "\u201C": '"',
    "\u201D": '"',
    "\u2022": "*",   # bullet
    "\u2026": "...", # ellipsis
    "\u00A0": " ",   # non-breaking space
    "\u00B7": ".",
}


def clean_svg(svg_text: str) -> str:
    """Replace all problematic non-ASCII characters in an SVG string."""
    result = []
    for char in svg_text:
        if char in EMOJI_MAP:
            result.append(EMOJI_MAP[char])
        elif ord(char) > 127:
            # For any remaining non-ASCII not in our map:
            # Try common Latin extended -> ASCII
            fallback = (
                char
                .encode("ascii", "ignore")
                .decode("ascii")
            )
            result.append(fallback if fallback else "")
        else:
            result.append(char)
    return "".join(result)


def run_enhancement():
    print("=" * 80)
    print("[START] Grade 7 Home Science — Visualization Quality Enhancement Pass")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Grade 7 Home Science not found!"

    total_fixed = 0
    total_skipped = 0

    for topic in subject.topics.order_by("order"):
        topic_fixed = 0
        all_diags = LessonBlock.objects.filter(
            lesson__learning_unit__topic=topic,
            block_type__in=["diagram", "suggested_diagram"]
        )

        for block in all_diags:
            # Get the SVG from whichever key is used
            svg_key = "svg_content" if "svg_content" in block.content else "svg" if "svg" in block.content else None
            if not svg_key:
                total_skipped += 1
                continue

            original_svg = block.content[svg_key]
            if not original_svg:
                total_skipped += 1
                continue

            # Check if cleaning is needed
            non_ascii = [c for c in original_svg if ord(c) > 127]
            if not non_ascii:
                total_skipped += 1
                continue

            cleaned_svg = clean_svg(original_svg)

            # Verify it's actually clean now
            still_bad = [c for c in cleaned_svg if ord(c) > 127]
            if still_bad:
                # Brute-force strip anything remaining
                cleaned_svg = cleaned_svg.encode("ascii", "replace").decode("ascii")

            # Save
            new_content = dict(block.content)
            new_content[svg_key] = cleaned_svg
            block.content = new_content
            block.save(update_fields=["content"])
            topic_fixed += 1
            total_fixed += 1

        if topic_fixed > 0:
            print(f"  Topic {topic.order}: {topic.name[:45]} — fixed {topic_fixed} SVG(s)")

    # Final verification
    print("\n--- Final Verification ---")
    all_diags = LessonBlock.objects.filter(
        lesson__learning_unit__topic__subject=subject,
        block_type__in=["diagram", "suggested_diagram"]
    )
    remaining_issues = 0
    for b in all_diags:
        svg = b.content.get("svg_content") or b.content.get("svg", "")
        if any(ord(c) > 127 for c in svg):
            remaining_issues += 1
            print(f"  Still has issues: Block {b.id} — '{b.title[:55]}'")

    print("\n" + "=" * 80)
    print(f"[SUCCESS] Visualization Enhancement Pass Complete!")
    print(f"[*] SVGs cleaned:  {total_fixed}")
    print(f"[*] Already clean: {total_skipped}")
    print(f"[*] Remaining issues: {remaining_issues}")
    print("=" * 80)


if __name__ == "__main__":
    run_enhancement()
