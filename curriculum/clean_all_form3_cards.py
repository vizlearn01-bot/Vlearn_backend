import os
import sys
import django
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock

def clean_all_cards():
    print("Executing systematic card cleaning across Form 3 Chemistry (Topics 22, 23, 24)...")

    # Define clean, focused definitions for all key technical terms across Form 3
    clean_definitions = {
        # Gas Laws
        "Boyle's Law": "For a fixed mass of gas at constant temperature, the volume is inversely proportional to its pressure ($P_1V_1 = P_2V_2$).",
        "Charles's Law": "The volume of a fixed mass of gas is directly proportional to its absolute temperature in Kelvin at constant pressure ($\\frac{V_1}{T_1} = \\frac{V_2}{T_2}$).",
        "Combined Gas Law": "Combines Boyle's and Charles's laws into a single relationship for a fixed mass of gas: $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$.",
        "Standard Gas Conditions": "Standard Temperature and Pressure (s.t.p.) is $0^\\circ\\text{C}$ ($273\\text{ K}$) and $1\\text{ atm}$ ($760\\text{ mmHg}$). Room Temperature and Pressure (r.t.p.) is $25^\\circ\\text{C}$ ($298\\text{ K}$) and $1\\text{ atm}$.",
        "Graham's Law of Diffusion": "The rate of diffusion of a gas is inversely proportional to the square root of its density or molecular mass ($\\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}}$).",
        
        # The Mole
        "Relative Atomic Mass ($A_r$)": "The average mass of one atom of an element compared to $\\frac{1}{12}\\text{th}$ the mass of an atom of Carbon-12.",
        "Relative Molecular Mass ($M_r$)": "The sum of the relative atomic masses of all atoms present in one molecule of a covalent substance.",
        "Relative Formula Mass (R.F.M.)": "The sum of the relative atomic masses of all atoms present in one formula unit of an ionic compound.",
        "The Mole": "The amount of substance containing exactly $6.022 \\times 10^{23}$ elementary particles (Avogadro's Constant, $L$).",
        "Molar Mass ($M$)": "The mass in grams of exactly one mole of a chemical substance (measured in $\\text{g/mol}$).",
        "Empirical Formula": "The simplest formula showing the lowest whole-number ratio of atoms of each element in a compound.",
        "Molecular Formula": "The actual formula showing the exact number of atoms of each element present in one molecule of a compound.",
        "Molar Solution (1.0 M)": "A solution that contains exactly one mole of solute dissolved in water to make one cubic decimeter ($1\\text{ dm}^3$ or $1000\\text{ cm}^3$) of solution.",
        "Concentration": "The quantity of dissolved solute present in a unit volume of solution (expressed in $\\text{g/dm}^3$ or $\\text{mol/dm}^3$).",
        "The Dilution Law": "Adding solvent to a solution increases volume while keeping solute moles constant ($C_1V_1 = C_2V_2$).",
        "Molar Gas Volume ($V_m$)": "The volume occupied by exactly one mole of any gas under standard conditions ($22.4\\text{ dm}^3$ at s.t.p. and $24.0\\text{ dm}^3$ at r.t.p.).",
        "Acid-Base Titration": "A quantitative volumetric technique where a standard solution is gradually added from a burette to neutralize an exact volume of unknown solution in a flask.",
        "Back Titration": "An indirect volumetric analysis method where an insoluble or slow-reacting sample is dissolved in excess standard acid, and the leftover unreacted acid is titrated against standard base.",
        "Redox Titration": "A volumetric analysis method involving electron transfer between an oxidizing agent and a reducing agent, often using self-indicating reagents like $\\text{KMnO}_4$.",
        
        # Organic Chemistry I
        "Hydrocarbon": "An organic compound containing carbon and hydrogen atoms only.",
        "Homologous Series": "A family of organic compounds sharing the same general formula, similar chemical properties, and showing a gradual gradation in physical properties.",
        "Alkanes": "A homologous series of saturated hydrocarbons containing only single carbon-carbon bonds (general formula $\\text{C}_n\\text{H}_{2n+2}$).",
        "Structural Isomers": "Compounds with the same molecular formula but different structural connectivity of their atoms.",
        "Decarboxylation": "A chemical reaction that removes a carboxyl group ($-\\text{COONa}$) from an alkanoate salt, releasing an alkane and sodium carbonate.",
        "Alkenes": "A homologous series of unsaturated hydrocarbons containing at least one carbon-carbon double bond (general formula $\\text{C}_n\\text{H}_{2n}$).",
        "Alkynes": "A homologous series of unsaturated hydrocarbons containing at least one carbon-carbon triple bond (general formula $\\text{C}_n\\text{H}_{2n-2}$).",
        "Addition Polymerisation": "A reaction where thousands of unsaturated monomer molecules join together by opening their double bonds to form a single giant polymer chain without forming any byproduct.",
        "Cracking": "The industrial process of breaking long-chain, heavy alkane fractions from crude oil into shorter, high-demand petrol fuels and reactive alkene monomers."
    }

    # Iterate through all blocks in Form 3
    for b in LessonBlock.objects.filter(lesson__topic__id__in=[22, 23, 24]):
        # 1. Clean definition cards
        if b.block_type == 'definition_card':
            c = b.content
            term = c.get('term', b.page_title or b.title or '')
            
            # Clean term from noisy prefixes
            term_clean = term.replace('###', '').replace('(In Plain English)', '').strip()
            
            matched = False
            for k, clean_def in clean_definitions.items():
                if k.lower() in term_clean.lower() or term_clean.lower() in k.lower():
                    b.content = {
                        "term": k,
                        "content": clean_def
                    }
                    b.title = k
                    b.page_title = k
                    b.save()
                    print(f"Updated definition card: Lesson {b.lesson.id} -> '{k}'")
                    matched = True
                    break
            
            if not matched:
                # Strip raw markdown headings and rules
                txt = c.get('content', '') or c.get('text', '')
                clean_txt = re.sub(r'###.*?\n', '', txt)
                clean_txt = clean_txt.replace('---', '').strip()
                b.content = {
                    "term": term_clean,
                    "content": clean_txt[:250]
                }
                b.save()
                print(f"Sanitized definition card: Lesson {b.lesson.id} -> '{term_clean}'")

        # 2. Clean concept explanation cards from raw duplicate headings
        elif b.block_type in ['concept_explanation', 'learning_goal', 'common_misconception', 'summary']:
            c = b.content
            txt = c.get('text', '')
            if txt and (txt.startswith('###') or '### What is' in txt):
                clean_txt = re.sub(r'^###\s*.*?\n', '', txt).strip()
                b.content['text'] = clean_txt
                b.save()

    print("All Form 3 cards cleaned and sanitized successfully!")

if __name__ == "__main__":
    clean_all_cards()
