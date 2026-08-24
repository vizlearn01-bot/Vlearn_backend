"""
Form 4 Chemistry — Phase 0: Global Cleanups & Normalization
1. Strip trailing `\ \text{}` artefacts from mathematical/chemical equations in all blocks
2. Replace all student-facing meta labels in block titles (e.g. 'Building Intuition:', 'Visual Representation:')
3. Archive legacy V1 Lesson 20 ('Overview: Topic 1: Acids, Bases and Salts')
4. Clean up broken/empty placeholder assets (e.g. Lesson 12 placeholder video with no URL)
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Subject, Topic, Lesson, LessonBlock, LessonAsset

def clean_latex_field(val):
    if isinstance(val, str):
        # Strip trailing \ \text{} and \text{}
        new_val = val.replace(r'\ \text{}', '').replace(r'\text{}', '')
        return new_val
    elif isinstance(val, dict):
        return {k: clean_latex_field(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [clean_latex_field(item) for item in val]
    return val

TITLE_REPLACEMENTS = {
    # Topic 1
    "Building Intuition: From Daily Observations to the Lab": "Acids in Everyday Life and Laboratory Practice",
    "Building Intuition: The Vinegar vs. Battery Acid Puzzle": "Comparing Acid Strengths",
    "Building Intuition: The Bitter, Slippery Cleaners": "Properties of Bases and Alkalis",
    "Building Intuition: The Silent Gas and the Active Liquid": "Role of the Solvent in Acid-Base Character",
    "Building Intuition: The Chemical \"Chameleon\"": "Amphoteric Behaviour in Oxides and Hydroxides",
    "Building Intuition: The Legacy of Acid-Base Battles": "Introduction to Salts and Their Formation",
    "Building Intuition: The Instant Solid": "Precipitation Reactions and Insoluble Salts",
    "Building Intuition: The Disappearing Solid": "Formation and Behaviour of Complex Ions",
    "Building Intuition: The Sugar-in-Tea Limit": "Solubility Dynamics and Saturation",
    "Building Intuition: The Mixed Salt Dilemma": "Principles of Fractional Crystallisation",
    "Building Intuition: The Soap That Refused to Lather": "Water Hardness and Soap Chemistry",
    "Building Intuition: The Cost of Hard Water": "Industrial and Domestic Disadvantages of Hard Water",
    "Building Intuition: The Mineral Water Paradox": "Health and Industrial Benefits of Hard Water",
    "Building Intuition: The Chemical Extraction of Minerals": "Techniques for Softening Hard Water",

    # Topic 2
    "Building Intuition: The Molecular Tug-of-War": "Energy Balance in Bond Breaking and Formation",
    "Building Intuition: The Temperature Tale of Two Solutes": "Distinguishing Exothermic and Endothermic Processes",
    "Building Intuition: The Chemical Balance Sheet": "Thermochemical Equations and Enthalpy Notation",
    "Building Intuition: Measuring the Invisible Fire": "Calorimetric Determination of Enthalpy Changes",
    "Building Intuition: The Need for a Level Playing Field": "Standard Thermodynamic States and Reference Conditions",
    "Building Intuition: The Mountain Climber’s Rule": "Hess's Law and Alternative Reaction Pathways",
    "Building Intuition: Tearing Down the Castle to Build Water Jackets": "Lattice Energy and Hydration in Solution Formation",
    "Building Intuition: The Energy of Our Civilization": "Chemical Fuels as Energy Sources",
    "Building Intuition: The Energy-per-Shilling Question": "Fuel Calorific Value and Heating Efficiencies",
    "Building Intuition: The Double-Edged Sword of Energy": "Safety Guidelines and Fire Safety with Fuels",
    "Building Intuition: The Cost of Carbon": "Environmental Impact of Fuel Combustion",

    # Topic 3
    "Building Intuition: Fast vs. Slow Reactions": "Observing Reaction Speeds in Chemistry",
    "Building Intuition: The Crowded Hallway": "Collision Theory and Activation Energy Barriers",
    "Building Intuition: Controlling the Clock": "Key Factors Governing Reaction Rates",
    "Building Intuition: The Crowded Room": "Influence of Pressure on Gaseous Reaction Rates",
    "Building Intuition: The Infinite Escalator": "Dynamic Nature of Chemical Equilibrium",
    "Building Intuition: The Self-Balancing Seesaw": "Le Chatelier's Principle in Dynamic Systems",
    "Building Intuition: The Low Tunnel": "Catalytic Lowering of Activation Energy",
    "Building Intuition: The Heart of Sulfuric Acid Production": "Catalytic Oxidation of Sulfur Dioxide in the Contact Process",

    # Topic 7
    "Visual representation of nuclear mass defect and binding energy equivalent": "Nuclear Mass Defect and Binding Energy",
    "Visual Representation: Writing Equations for Beta ($\\beta$) Emission": "Balancing Beta (β) Decay Equations",
}

def run_phase0():
    subject = Subject.objects.get(id=4)
    print("=" * 80)
    print(f"STARTING PHASE 0: Global Cleanups for Form 4 Chemistry (Subject ID {subject.id})")
    print("=" * 80)

    # 1. LaTeX trailing \text{} cleanup
    blocks = LessonBlock.objects.filter(lesson__topic__subject=subject)
    latex_fixed = 0
    for b in blocks:
        if b.content:
            new_content = clean_latex_field(b.content)
            if new_content != b.content:
                b.content = new_content
                b.save(update_fields=['content'])
                latex_fixed += 1
    print(f"[1/4] LaTeX Cleanup: Stripped trailing '\\text{{}}' from {latex_fixed} content blocks.")

    # 2. Block Title Meta Language Fixes
    titles_fixed = 0
    for b in blocks:
        if b.title and b.title in TITLE_REPLACEMENTS:
            old_title = b.title
            b.title = TITLE_REPLACEMENTS[old_title]
            b.save(update_fields=['title'])
            titles_fixed += 1
            print(f"  [Title Updated] Block {b.id}: '{old_title}' -> '{b.title}'")
        elif b.title and "Building Intuition:" in b.title:
            old_title = b.title
            b.title = b.title.replace("Building Intuition:", "").strip()
            b.save(update_fields=['title'])
            titles_fixed += 1
            print(f"  [Title Auto-Cleaned] Block {b.id}: '{old_title}' -> '{b.title}'")
    print(f"[2/4] Title Cleanup: Replaced meta labels in {titles_fixed} block titles.")

    # 3. Archive Legacy Lesson 20
    try:
        lesson_20 = Lesson.objects.get(id=20)
        lesson_20.status = 'archived'
        lesson_20.save(update_fields=['status'])
        print(f"[3/4] Legacy Lesson Archival: Lesson 20 ('{lesson_20.title}') marked as archived.")
    except Lesson.DoesNotExist:
        print("[3/4] Lesson 20 not found, skipping.")

    # 4. Clean up broken placeholder assets in Lesson 12
    broken_assets = LessonAsset.objects.filter(lesson__topic__subject=subject, url__isnull=True, storage_type='url')
    broken_count = broken_assets.count()
    for a in broken_assets:
        print(f"  [Removing Broken Asset] ID {a.id}: '{a.title}' in Lesson {a.lesson.id}")
        a.delete()
    print(f"[4/4] Asset Cleanup: Removed {broken_count} empty/unlinked URL assets.")

    print("=" * 80)
    print("PHASE 0 COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_phase0()
