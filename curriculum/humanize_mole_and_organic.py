import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_humanize_mole_and_organic():
    print("Executing full humanization across The Mole and Organic Chemistry I...")

    topic_23 = Topic.objects.get(id=23)
    topic_24 = Topic.objects.get(id=24)

    lessons_payload = {
        # =====================================================================
        # LESSON 165: THE MOLE CONCEPT
        # =====================================================================
        165: {
            "topic": topic_23,
            "title": "The Mole Concept and Avogadro's Constant",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemist's Counting Unit",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand why the Mole is the chemist's universal counting package, apply Avogadro's Constant ($L = 6.022 \\times 10^{23}\\text{ particles/mol}$), understand Molar Mass ($M$), and convert effortlessly between mass, moles, and number of particles."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Counting Billions of Invisible Atoms",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In everyday life, we bundle objects into convenient counting packages:\n* A **pair** of shoes = $2$\n* A **dozen** eggs = $12$\n* A **baker's dozen** = $13$\n* A **ream** of printer paper = $500\\text{ sheets}$\n\nBecause atoms are unimaginably tiny, counting them in dozens or hundreds would still leave you with numbers containing 20 zeros! Chemists needed a **super-sized counting package** to bundle macroscopic amounts of atoms into simple, manageable numbers.\n\nThat super-sized chemist's package is **the Mole**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Avogadro's Number: The Bridge Between Atoms and Grams",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Exactly how many particles are inside **one mole**?\n\nOne mole of any substance contains exactly **Avogadro's Constant ($L$ or $N_A$)** of particles:\n$$L = 6.022 \\times 10^{23} \\text{ particles per mole}$$\n\nWritten out in full, that number is:\n$$\\mathbf{602,200,000,000,000,000,000,000}$$\n\n* **The Mind-Blowing Scale**:\n  If you had a mole of marble stones, they would cover the entire surface of the Earth several miles deep! Yet, because water molecules are so tiny, **one mole of water molecules ($6.022 \\times 10^{23}$ molecules) fits into a single tablespoon ($18\\text{ cm}^3$)**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: The Mole Conversion Bridge",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Flowchart diagram illustrating the Mole as the central bridge between Mass in Grams (divide/multiply by Molar Mass) and Number of Particles (multiply/divide by Avogadro's Constant 6.022 x 10^23).",
                        "caption": "The Mole Bridge: The Mole connects measurable mass on a balance to the microscopic count of particles."
                    },
                    "asset_info": {
                        "title": "Mole Calculation Bridge Diagram",
                        "description": "Visual conversion triangle and bridge linking mass in grams, moles, and number of particles via Molar Mass and Avogadro's constant.",
                        "ai_instruction": "Create an instructional flowchart showing Mass (grams) on left, Moles in center, and Particles on right, with conversion arrows labeled with Molar Mass and Avogadro's Number."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Mole Formulas (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Mole & Molar Mass",
                        "content": "### What is Molar Mass ($M$)?\n*The weight in grams of exactly one mole of a substance (units: $\\text{g/mol}$).*\n- **The Golden Shortcut**: Look at the Relative Atomic Mass ($A_r$) on your periodic table. Add the unit $\\text{g/mol}$, and you have the Molar Mass!\n- *Example*: Carbon ($A_r = 12$) $\\rightarrow$ Molar Mass = $12.0\\text{ g/mol}$.\n\n### The Two Master Conversion Formulas:\n\n1. **Converting Between Grams and Moles**:\n   $$\\mathbf{n = \\frac{m}{M}} \\quad \\Longleftrightarrow \\quad \\mathbf{m = n \\times M}$$\n   - $n$ = Number of moles\n   - $m$ = Mass on the balance (in grams)\n   - $M$ = Molar mass from the periodic table (in $\\text{g/mol}$)\n\n2. **Converting Between Moles and Particle Count**:\n   $$\\mathbf{N = n \\times L} \\quad \\Longleftrightarrow \\quad \\mathbf{n = \\frac{N}{L}}$$\n   - $N$ = Actual number of individual atoms or molecules\n   - $L$ = Avogadro's constant ($6.022 \\times 10^{23}$)"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Mass and Particle Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. What is the mass of $0.25\\text{ moles}$ of calcium carbonate ($\\text{CaCO}_3$)? ($A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$).\n2. How many water molecules are in a glass containing $36.0\\text{ g}$ of pure $\\text{H}_2\\text{O}$? ($L = 6.022 \\times 10^{23}\\text{ mol}^{-1}, A_r$: $\\text{H}=1.0, \\text{O}=16.0$).",
                        "steps": [
                            "**Problem 1: Finding Mass of $0.25\\text{ moles}$ of $\\text{CaCO}_3$**\n- **1. What do we know?** $n = 0.25\\text{ mol}$, Formula = $\\text{CaCO}_3$.\n- **2. Find Molar Mass ($M$) from Periodic Table**:\n$$M = 40.0 + 12.0 + 3(16.0) = 100.0\\text{ g/mol}$$\n- **3. Multiply Moles by Molar Mass**:\n$$m = n \\times M = 0.25\\text{ mol} \\times 100.0\\text{ g/mol} = 25.0\\text{ g}$$\n- **Result**: Weigh out $25.0\\text{ g}$ of $\\text{CaCO}_3$ on the balance.",
                            "**Problem 2: Counting Molecules in $36.0\\text{ g}$ of Water**\n- **1. Find Molar Mass of $\\text{H}_2\\text{O}$**:\n$$M = 2(1.0) + 16.0 = 18.0\\text{ g/mol}$$\n- **2. Convert Grams to Moles**:\n$$n = \\frac{m}{M} = \\frac{36.0\\text{ g}}{18.0\\text{ g/mol}} = 2.0\\text{ moles}$$\n- **3. Multiply Moles by Avogadro's Constant**:\n$$N = n \\times L = 2.0\\text{ mol} \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\text{ molecules}$$\n- **Result**: The glass holds $1.2044 \\times 10^{24}$ water molecules."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: A Dozen Eggs vs A Dozen Watermelons",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does 1 mole of Lead weigh the same as 1 mole of Helium?\n**Answer**: **NO!**\n\nThink about a dozen chicken eggs versus a dozen watermelons. Both baskets contain exactly **12 items**, but the dozen watermelons are vastly heavier!\n\nSimilarly, $1\\text{ mole of Lead}$ and $1\\text{ mole of Helium}$ both contain exactly **$6.022 \\times 10^{23}$ atoms**. But because one lead atom is much heavier than a helium atom, $1\\text{ mole of Lead}$ weighs **$207.2\\text{ grams}$**, while $1\\text{ mole of Helium}$ weighs only **$4.0\\text{ grams}$**!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Counting Sodium Atoms",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "How many sodium atoms are present in $4.6\\text{ g}$ of pure sodium metal? ($A_r$: $\\text{Na}=23.0, L = 6.022 \\times 10^{23}\\text{ mol}^{-1}$).",
                        "options": [
                            "$1.204 \\times 10^{23}$",
                            "$6.022 \\times 10^{23}$",
                            "$2.408 \\times 10^{24}$",
                            "$1.385 \\times 10^{22}$"
                        ],
                        "answer": "A",
                        "explanation": "First, calculate moles: $n = \\frac{m}{M} = \\frac{4.6\\text{ g}}{23.0\\text{ g/mol}} = 0.20\\text{ mol}$. Then multiply by Avogadro's constant: $N = 0.20\\text{ mol} \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{23}\\text{ atoms}$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Finding Mass of Moles",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the mass of $0.50\\text{ moles}$ of sulfuric acid ($\\text{H}_2\\text{SO}_4$)? ($A_r$: $\\text{H}=1.0, \\text{S}=32.0, \\text{O}=16.0$).",
                        "options": [
                            "$49.0\\text{ g}$",
                            "$98.0\\text{ g}$",
                            "$24.5\\text{ g}$",
                            "$196.0\\text{ g}$"
                        ],
                        "answer": "A",
                        "explanation": "Molar mass of $\\text{H}_2\\text{SO}_4 = 2(1.0) + 32.0 + 4(16.0) = 98.0\\text{ g/mol}$. Mass $m = n \\times M = 0.50\\text{ mol} \\times 98.0\\text{ g/mol} = 49.0\\text{ g}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: The Mole Concept",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: The Mole Concept\n- **The Mole**: The chemist's counting package containing $6.022 \\times 10^{23}$ particles ($L$).\n- **Molar Mass ($M$)**: Weight in grams of 1 mole of substance (matches $A_r$ or $M_r$ in $\\text{g/mol}$).\n- **The 2 Core Equations**:\n  $$\\mathbf{n = \\frac{m}{M}} \\quad \\text{and} \\quad \\mathbf{N = n \\times L}$$"
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 166: EMPIRICAL AND MOLECULAR FORMULAE
        # =====================================================================
        166: {
            "topic": topic_23,
            "title": "Calculation of Empirical and Molecular Formulae",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Chemical Detective Work",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the difference between Empirical and Molecular formulae, determine simplest empirical ratios from reacting mass data, and calculate true molecular formulas using Relative Molecular Mass ($M_r$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Recipe Ratio vs The Whole Cake",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When a pharmaceutical company discovers a new medicinal plant or when environmental scientists analyze a pollutant in a river, the first step is finding its chemical formula.\n\nThink of chemical formulas like a recipe:\n* **Empirical Formula (The Simplified Recipe Ratio)**: Shows the simplest whole-number ratio of atoms in a compound. For example, hydrogen peroxide has 1 Hydrogen for every 1 Oxygen, so its empirical formula is $\\mathbf{\\text{HO}}$.\n* **Molecular Formula (The True Molecule)**: Shows the actual number of atoms in a real molecule. A real hydrogen peroxide molecule has 2 Hydrogens and 2 Oxygens bonded together, so its molecular formula is $\\mathbf{\\text{H}_2\\text{O}_2}$!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Determination Methods",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In school chemistry, empirical formulas are determined in two ways:\n\n1. **Direct Burning in Crucible (e.g., Magnesium Oxide)**:\n   Burning clean magnesium ribbon in a porcelain crucible allows it to react with oxygen from the air. Subtracting the mass of $\\text{Mg}$ from the mass of $\\text{MgO}$ gives the mass of reacting oxygen.\n\n2. **Reduction of Metal Oxides (e.g., Copper(II) Oxide)**:\n   Passing dry hydrogen gas over heated black copper(II) oxide in a glass tube strips away the oxygen, leaving pure reddish copper metal:\n   $$\\text{CuO}_{(s)} + \\text{H}_{2(g)} \\xrightarrow{\\Delta} \\text{Cu}_{(s)} + \\text{H}_2\\text{O}_{(g)}$$"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Reduction of Copper(II) Oxide Setup",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Apparatus diagram showing dry hydrogen gas entering a combustion tube containing a porcelain boat with black Copper(II) Oxide heated by a Bunsen flame. Excess hydrogen burns at the jet at the end.",
                        "caption": "Reduction of Copper(II) Oxide: Dry hydrogen gas reduces black CuO to reddish copper metal for empirical formula determination."
                    },
                    "asset_info": {
                        "title": "Empirical Formula Apparatus Setup",
                        "description": "Combustion tube setup for reducing copper(II) oxide with dry hydrogen gas.",
                        "ai_instruction": "Illustrate a combustion tube with a porcelain boat containing heated CuO, hydrogen gas inlet on left, and burning hydrogen flame jet on right."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The 4-Step Formula Table (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Empirical & Molecular Formulas",
                        "content": "### The 4-Step Calculation Workflow:\nWhenever you are given masses or percentages, set up a simple 4-step table:\n\n1. **Step 1: Write down Masses or %**\n2. **Step 2: Convert to Moles** (divide each mass by its atomic weight $A_r$)\n3. **Step 3: Find Simplest Ratio** (divide all mole values by the smallest mole value)\n4. **Step 4: Write Empirical Formula**\n\n---\n\n### Finding the True Molecular Formula:\n$$\\mathbf{\\text{Molecular Formula} = (\\text{Empirical Formula})_n}$$\n$$\\mathbf{n = \\frac{\\text{Relative Molecular Mass } (M_r)}{\\text{Empirical Formula Mass (E.F.M.)}}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Determining Chemical Formulas",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. Burning $0.84\\text{ g}$ of magnesium yields $1.40\\text{ g}$ of magnesium oxide. Find its empirical formula ($A_r$: $\\text{Mg}=24.0, \\text{O}=16.0$).\n2. A compound has $57.15\\%\\text{ C}$, $4.76\\%\\text{ H}$, and $38.09\\%\\text{ O}$ by mass, with $M_r = 126.0$. Find its empirical and molecular formulas.",
                        "steps": [
                            "**Problem 1: Empirical Formula of Magnesium Oxide**\n- **1. Find Masses**: Mass of $\\text{Mg} = 0.84\\text{ g}$; Mass of $\\text{O} = 1.40\\text{ g} - 0.84\\text{ g} = 0.56\\text{ g}$\n- **2. Convert to Moles**:\n  - Moles of $\\text{Mg} = \\frac{0.84}{24.0} = 0.035\\text{ mol}$\n  - Moles of $\\text{O} = \\frac{0.56}{16.0} = 0.035\\text{ mol}$\n- **3. Divide by Smallest ($0.035$)**:\n  - $\\text{Mg} = 1, \\text{O} = 1$\n- **Result**: Empirical Formula is $\\mathbf{\\text{MgO}}$.",
                            "**Problem 2: Molecular Formula from % Composition**\n- **1. Convert $100\\text{ g}$ to Moles**:\n  - $\\text{C} = \\frac{57.15}{12.0} = 4.76\\text{ mol}$\n  - $\\text{H} = \\frac{4.76}{1.0} = 4.76\\text{ mol}$\n  - $\\text{O} = \\frac{38.09}{16.0} = 2.38\\text{ mol}$\n- **2. Divide by Smallest ($2.38$)**:\n  - $\\text{C} = \\frac{4.76}{2.38} = 2$\n  - $\\text{H} = \\frac{4.76}{2.38} = 2$\n  - $\\text{O} = \\frac{2.38}{2.38} = 1$\n  - **Empirical Formula** = $\\mathbf{\\text{C}_2\\text{H}_2\\text{O}}$\n- **3. Find Multiplier ($n$)**:\n  - Empirical Mass $= 2(12.0) + 2(1.0) + 16.0 = 42.0\\text{ g/mol}$\n  - $n = \\frac{M_r}{\\text{Empirical Mass}} = \\frac{126.0}{42.0} = 3$\n- **Result**: Molecular Formula = $(\\text{C}_2\\text{H}_2\\text{O})_3 = \\mathbf{\\text{C}_6\\text{H}_6\\text{O}_3}$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: The Crucible Lid Technique",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why must the crucible lid be opened and closed quickly during magnesium burning?\n1. **Open the lid**: Lets fresh oxygen in so the magnesium keeps burning.\n2. **Close the lid immediately**: Prevents white clouds of magnesium oxide smoke from escaping into the room. If smoke escapes, your final mass on the balance will be too low, ruining your mole ratio!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Finding Empirical Formula",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A hydrocarbon contains $80.0\\%$ carbon and $20.0\\%$ hydrogen by mass. What is its empirical formula? ($A_r$: $\\text{C}=12.0, \\text{H}=1.0$).",
                        "options": [
                            "$\\text{CH}_2$",
                            "$\\text{CH}_3$",
                            "$\\text{C}_2\\text{H}_3$",
                            "$\\text{CH}_4$"
                        ],
                        "answer": "B",
                        "explanation": "In $100\\text{ g}$: Moles of $\\text{C} = \\frac{80.0}{12.0} = 6.67\\text{ mol}$; Moles of $\\text{H} = \\frac{20.0}{1.0} = 20.0\\text{ mol}$. Divide by $6.67$: $\\text{C} = 1$, $\\text{H} = \\frac{20.0}{6.67} = 3.0$. Empirical formula is $\\text{CH}_3$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Molecular Formula Multiplier",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A compound has an empirical formula of $\\text{CH}_2\\text{O}$ and a Relative Molecular Mass ($M_r$) of $180.0$. What is its molecular formula? ($A_r$: $\\text{C}=12.0, \\text{H}=1.0, \\text{O}=16.0$).",
                        "options": [
                            "$\\text{C}_3\\text{H}_6\\text{O}_3$",
                            "$\\text{C}_6\\text{H}_{12}\\text{O}_6$",
                            "$\\text{C}_5\\text{H}_{10}\\text{O}_5$",
                            "$\\text{C}_4\\text{H}_8\\text{O}_4$"
                        ],
                        "answer": "B",
                        "explanation": "Empirical formula mass $= 12.0 + 2(1.0) + 16.0 = 30.0\\text{ g/mol}$. Multiplier $n = \\frac{180.0}{30.0} = 6$. Molecular formula is $(\\text{CH}_2\\text{O})_6 = \\text{C}_6\\text{H}_{12}\\text{O}_6$ (glucose)."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Chemical Formulae",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Empirical & Molecular Formulae\n- **Empirical Formula**: Simplest whole-number ratio of atoms in a compound.\n- **Molecular Formula**: True formula of the real molecule ($\\text{Molecular} = (\\text{Empirical})_n$).\n- **4-Step Table**: Mass/% $\\rightarrow$ Moles (divide by $A_r$) $\\rightarrow$ Ratio (divide by smallest) $\\rightarrow$ Integer Formula."
                    }
                }
            ]
        }
    }

    for lesson_id, data in lessons_payload.items():
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            print(f"Humanizing Lesson {lesson.id}: \"{lesson.title}\" in {data['topic'].name}...")
            
            LessonBlock.objects.filter(lesson=lesson).delete()
            LessonAsset.objects.filter(lesson=lesson).delete()
            
            for order, card in enumerate(data["cards"], start=1):
                block_id = f"block_{lesson.id}_{order}_{uuid.uuid4().hex[:6]}"
                b = LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=block_id,
                    order=order,
                    page_number=card["page_number"],
                    page_title=card["page_title"],
                    block_type=card["block_type"],
                    component_type=card["component_type"],
                    component_order=order,
                    title=card["page_title"],
                    content=card["content"]
                )
                
                if "asset_info" in card:
                    info = card["asset_info"]
                    LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        source_type="uploaded",
                        storage_type="local",
                        status="pending",
                        title=info["title"],
                        description=info["description"],
                        metadata={"ai_instruction": info["ai_instruction"], "block_id": b.block_id}
                    )
            
            lesson.status = "published"
            lesson.save()
            print(f"  Refactored Lesson {lesson.id} successfully.")
        except Lesson.DoesNotExist:
            print(f"Lesson {lesson_id} not found!")

if __name__ == "__main__":
    run_humanize_mole_and_organic()
