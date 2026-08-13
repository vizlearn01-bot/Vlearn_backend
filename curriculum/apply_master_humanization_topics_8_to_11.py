"""
Form 4 Physics — Master Humanization Engine for Topics 8-11

Removes all parenthetical math clutter (e.g. ($lpha$), ($\alpha$), ($\beta^-$), ($\gamma$),
($T_{1/2}$), ($E = \Delta m c^2$), (^{A}_{Z}X), etc.) from block titles, page titles,
headers, definition cards, and text body across Topics 8, 9, 10, and 11.
"""

import os
import sys
import re
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, LessonBlock

# Title & string maps for exact replacements
EXACT_TITLE_REPLACEMENTS = {
    # Topic 8
    "Energy Conversion Physics ($99\%$ Heat vs $1\%$ X-Rays)": "Energy Conversion Physics: Heat vs. X-Rays",
    "X-Ray Attenuation & Linear Absorption ($I = I_0 e^{-\mu x}$)": "X-Ray Attenuation and Linear Absorption",
    "Crystallography & Bragg's Law ($2d \sin\theta = n\lambda$)": "Crystallography and Bragg's Law",
    "X-Ray Tube Energy Conversion Efficiency ($\eta < 1\%$)": "X-Ray Tube Energy Conversion Efficiency",

    # Topic 9
    "Work Function Energy Barrier ($\Phi = h f_0$)": "Work Function Energy Barrier",
    "Threshold Wavelength ($\lambda_0 = c / f_0$)": "Threshold Wavelength",
    "Einstein's Photoelectric Equation ($h f = \Phi + K_{\max}$)": "Einstein's Photoelectric Equation",
    "Stopping Potential ($V_s$) Mechanics": "Stopping Potential Mechanics",

    # Topic 10
    "Alpha ($\alpha$) Radiation Properties": "Alpha Radiation Properties",
    "Beta ($\beta^-$) Radiation Properties": "Beta Radiation Properties",
    "Gamma ($\gamma$) Radiation Properties": "Gamma Radiation Properties",
    "Alpha ($\alpha$) Decay Nuclear Balance": "Alpha Decay Nuclear Balance",
    "Beta ($\beta^-$) Decay Nuclear Balance": "Beta Decay Nuclear Balance",
    "Gamma ($\gamma$) Emission Mechanics": "Gamma Emission Mechanics",
    "Half-Life ($T_{1/2}$) & Decay Curve Kinetics": "Half-Life and Decay Curve Kinetics",
    "Carbon-14 Radioactive Dating ($^{14}\text{C}$)": "Carbon-14 Radioactive Dating",
    "Mass Defect & Nuclear Binding Energy ($E = \Delta m c^2$)": "Mass Defect and Nuclear Binding Energy",
    "Nuclear Fusion Mechanics ($^{2}_{1}\text{H} + ^{3}_{1}\text{H}$)": "Nuclear Fusion Mechanics",
    "Worked Example Level 4 — Mass Defect & Released Energy ($E = \Delta m c^2$)": "Worked Example Level 4: Mass Defect and Released Energy",

    # Topic 11
    "Transistor Current Equations & Current Gain ($\beta$)": "Transistor Current Equations and Current Gain",
}

REGEX_REPLACEMENTS = [
    # Remove parenthetical symbol after words
    (r"Alpha\s*\(\s*\\?\$?\\?alpha\\?\$?\s*\)", "Alpha"),
    (r"Beta\s*\(\s*\\?\$?\\?beta\^?-\\?\$?\s*\)", "Beta"),
    (r"Beta\s*\(\s*\\?\$?\\?beta\\?\$?\s*\)", "Beta"),
    (r"Gamma\s*\(\s*\\?\$?\\?gamma\\?\$?\s*\)", "Gamma"),
    (r"Nuclide Notation\s*\(\s*\\?\$?\^\{A\}_\{Z\}\\?text\{X\}\\?\$?\s*\)", "Nuclide Notation"),
    (r"Nuclide Notation\s*\(\s*\^\{A\}_\{Z\}X\s*\)", "Nuclide Notation"),
    (r"Half-Life\s*\(\s*\\?\$?T_\{1/2\}\\?\$?\s*\)", "Half-Life"),
    (r"Work Function\s*\(\s*\\?\$?\\?Phi\\?\$?\s*\)", "Work Function"),
    (r"Stopping Potential\s*\(\s*\\?\$?V_s\\?\$?\s*\)", "Stopping Potential"),
    (r"Threshold Frequency\s*\(\s*\\?\$?f_0\\?\$?\s*\)", "Threshold Frequency"),
    (r"Threshold Wavelength\s*\(\s*\\?\$?\\?lambda_0\\?\$?\s*\)", "Threshold Wavelength"),

    # Remove bare parenthetical symbols
    (r"\(\s*\\?\$?\\?alpha\\?\$?\s*\)", ""),
    (r"\(\s*\\?\$?\\?beta\^?-\\?\$?\s*\)", ""),
    (r"\(\s*\\?\$?\\?beta\\?\$?\s*\)", ""),
    (r"\(\s*\\?\$?\\?gamma\\?\$?\s*\)", ""),
    (r"\(\s*\^\{A\}_\{Z\}X\s*\)", ""),

    # Clean double spaces
    (r"\s{2,}", " "),
]

def clean_humanized_text(text: str) -> str:
    if not isinstance(text, str):
        return text

    new_text = text

    # Apply exact replacements first
    for orig, repl in EXACT_TITLE_REPLACEMENTS.items():
        if orig in new_text:
            new_text = new_text.replace(orig, repl)

    # Apply regex replacements
    for pat, repl in REGEX_REPLACEMENTS:
        new_text = re.sub(pat, repl, new_text)

    # Clean any space before punctuation
    new_text = re.sub(r'\s+([,\.\?\:])', r'\1', new_text)
    return new_text.strip()

def clean_dict_fields(obj):
    if isinstance(obj, str):
        return clean_humanized_text(obj)
    elif isinstance(obj, list):
        return [clean_dict_fields(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: clean_dict_fields(v) for k, v in obj.items()}
    return obj

def run_master_humanization():
    print("=" * 80)
    print("MASTER HUMANIZATION FOR TOPICS 8, 9, 10, 11")
    print("=" * 80)

    topics = Topic.objects.filter(
        subject__name="Physics",
        subject__grade__name="Form 4",
        order__in=[8, 9, 10, 11]
    ).order_by("order")

    total_blocks_updated = 0

    for topic in topics:
        topic_updated = 0
        for unit in topic.learning_units.all():
            lesson = unit.lessons.first()
            if not lesson:
                continue
            for block in lesson.blocks.all():
                changed = False

                if block.title:
                    new_title = clean_humanized_text(block.title)
                    if new_title != block.title:
                        block.title = new_title
                        changed = True

                if block.page_title:
                    new_page_title = clean_humanized_text(block.page_title)
                    if new_page_title != block.page_title:
                        block.page_title = new_page_title
                        changed = True

                if isinstance(block.content, dict):
                    new_content = clean_dict_fields(block.content)
                    if new_content != block.content:
                        block.content = new_content
                        changed = True

                if changed:
                    block.save()
                    topic_updated += 1
                    total_blocks_updated += 1

        print(f"Topic {topic.order:2d}: '{topic.name}' -> {topic_updated} blocks humanized.")

    print("=" * 80)
    print(f"MASTER HUMANIZATION COMPLETE! Total Blocks Updated: {total_blocks_updated}")
    print("=" * 80)

if __name__ == "__main__":
    run_master_humanization()
