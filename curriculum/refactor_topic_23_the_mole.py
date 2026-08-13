import os
import sys
import django
import uuid

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_refactor_topic_23():
    print("Executing full pedagogical refactoring for Topic 23: The Mole (Lessons 164 - 172)...")

    topic_23 = Topic.objects.get(id=23)

    lessons_data = {
        # =========================================================================
        # LESSON 164: RELATIVE MASSES
        # =========================================================================
        164: {
            "topic": topic_23,
            "title": "Relative Atomic, Molecular, and Formula Masses",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Understanding Relative Mass",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand why atomic masses are measured relative to the Carbon-12 standard, define Relative Atomic Mass ($A_r$), Relative Molecular Mass ($M_r$), and Relative Formula Mass (R.F.M.), and calculate the masses of complex chemical compounds."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Counting by Weighing: The Hardware Store Analogy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine walking into a hardware store in Nairobi and asking to buy $50,000$ tiny steel nails. Does the shopkeeper sit down and count them one by one? Of course not—that would take hours!\n\nInstead, the shopkeeper weighs a batch of $100$ nails, calculates the mass of a single nail, and weighs out the exact mass corresponding to $50,000$ nails. This is called **counting by weighing**.\n\nIn Chemistry, atoms and molecules are far too microscopic to count individually. A single grain of table salt contains billions of billions of sodium and chloride ions. To count atoms, chemists weigh them using relative mass scales!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Carbon-12 Standard",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Because an individual atom weighs less than $10^{-22}\\text{ grams}$, placing a single atom on a lab balance is physically impossible. Chemists therefore compare the masses of all atoms to a single internationally agreed standard: the **Carbon-12 isotope (${}^{12}_{6}\\text{C}$)**.\n\n* **The Atomic Mass Unit (a.m.u.)**:\n  By international convention, one Carbon-12 atom is assigned a mass of exactly **$12.000$ atomic mass units**.\n* One atomic mass unit ($1\\text{ a.m.u.}$) is defined as **exactly $\\frac{1}{12}\\text{th}$ the mass of one Carbon-12 atom**:\n  $$1\\text{ a.m.u.} = \\frac{1}{12} \\times \\text{Mass of one }{}^{12}\\text{C atom} \\approx 1.66 \\times 10^{-24}\\text{ g}$$\n\nWhen we say Magnesium has an atomic mass of $24$, it means a magnesium atom is exactly **twice as heavy as a Carbon-12 atom** (or $24\\text{ times}$ as heavy as $\\frac{1}{12}\\text{th}$ of a Carbon-12 atom)!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Equal-Arm Balance Model of Atomic Mass",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram of an equal-arm balance comparing 1 Magnesium atom on the left pan balancing exactly 2 Carbon-12 atoms (or 24 atomic mass units) on the right pan.",
                        "caption": "Relative Mass Balance: 1 Magnesium atom (Ar = 24) balances exactly 2 Carbon-12 atoms (each mass 12)."
                    },
                    "asset_info": {
                        "title": "Carbon-12 Relative Mass Scale",
                        "description": "Equal-arm balance comparing atomic masses against the Carbon-12 standard.",
                        "ai_instruction": "Illustrate an equal-arm balance showing a Magnesium atom balancing two Carbon-12 atoms to visually explain the concept of relative mass."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Defining Relative Masses: Ar, Mr, and R.F.M.",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Relative Masses in Chemistry",
                        "content": "### 1. Relative Atomic Mass ($A_r$)\n*The average mass of one atom of an element compared to $\\frac{1}{12}\\text{th}$ the mass of an atom of Carbon-12.*\n\n### 2. Relative Molecular Mass ($M_r$)\n*The sum of the relative atomic masses of all atoms present in one molecule of a covalent substance.*\n\n### 3. Relative Formula Mass (R.F.M.)\n*The sum of the relative atomic masses of all atoms present in one formula unit of an ionic compound (e.g., $\\text{NaCl}$, $\\text{CaCO}_3$).*\n\n*Crucial Fact*: Because relative masses are ratios comparing two masses, **they have no units**!"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Calculating Molecular and Formula Masses",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the Relative Molecular / Formula Masses for:\n1. Hydrated copper(II) sulfate crystals, $\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}$\n2. Ammonium sulfate fertilizer, $(\\text{NH}_4)_2\\text{SO}_4$\n(Given $A_r$: $\\text{Cu}=63.5, \\text{S}=32.0, \\text{O}=16.0, \\text{H}=1.0, \\text{N}=14.0$).",
                        "steps": [
                            "**Problem 1: Hydrated Copper(II) Sulfate ($\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}$)**\n- **1. What are we finding?** Total Relative Formula Mass (R.F.M.) including water of crystallization.\n- **2. Breakdown of Atoms**:\n  - $1 \\times \\text{Cu} = 1 \\times 63.5 = 63.5$\n  - $1 \\times \\text{S} = 1 \\times 32.0 = 32.0$\n  - $4 \\times \\text{O} = 4 \\times 16.0 = 64.0$\n  - $5 \\times \\text{H}_2\\text{O} = 5 \\times [2(1.0) + 16.0] = 5 \\times 18.0 = 90.0$\n- **3. Summation**:\n$$\\text{R.F.M.} = 63.5 + 32.0 + 64.0 + 90.0 = 249.5$$\n- **Result**: $\\text{R.F.M. of } \\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O} = 249.5$ (dimensionless ratio).",
                            "**Problem 2: Ammonium Sulfate ($(\\text{NH}_4)_2\\text{SO}_4$)**\n- **1. Breakdown of Atoms**:\n  - In $(\\text{NH}_4)_2$: $2 \\times \\text{N} = 2(14.0) = 28.0$; $8 \\times \\text{H} = 8(1.0) = 8.0$\n  - In $\\text{SO}_4$: $1 \\times \\text{S} = 32.0$; $4 \\times \\text{O} = 4(16.0) = 64.0$\n- **2. Summation**:\n$$\\text{R.F.M.} = 28.0 + 8.0 + 32.0 + 64.0 = 132.0$$\n- **Result**: $\\text{R.F.M. of } (\\text{NH}_4)_2\\text{SO}_4 = 132.0$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Relative Masses Have No Units",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does Relative Atomic Mass ($A_r$) have no units?\n$A_r$ is defined as a ratio of two masses:\n$$A_r = \\frac{\\text{Average mass of one atom (in grams)}}{\\frac{1}{12} \\times \\text{Mass of one }{}^{12}\\text{C atom (in grams)}}$$\nBecause grams in the numerator cancel with grams in the denominator, relative mass is a **pure dimensionless ratio**!\n\nWhen we assign the unit **grams per mole ($\\text{g/mol}$)** to this number, it becomes the **Molar Mass ($M$)**."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Calculating Formula Mass",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the Relative Molecular Mass of ethanoic acid ($\\text{CH}_3\\text{COOH}$)? (Given $A_r$: $\\text{C}=12.0, \\text{H}=1.0, \\text{O}=16.0$).",
                        "options": [
                            "$44.0$",
                            "$60.0$",
                            "$58.0$",
                            "$74.0$"
                        ],
                        "answer": "B",
                        "explanation": "Summing atomic masses for $\\text{CH}_3\\text{COOH}$: $2 \\times \\text{C} = 2(12.0) = 24.0$; $4 \\times \\text{H} = 4(1.0) = 4.0$; $2 \\times \\text{O} = 2(16.0) = 32.0$. Total $M_r = 24.0 + 4.0 + 32.0 = 60.0$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Relative Masses",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Relative Atomic, Molecular, and Formula Masses\n- **Standard Reference**: Carbon-12 isotope assigned mass of exactly $12.000\\text{ a.m.u.}$\n- **$A_r$, $M_r$, R.F.M.**: Dimensionless relative mass ratios with no units.\n- **Calculating $M_r$ / R.F.M.**: Sum the individual $A_r$ values of all constituent atoms in the chemical formula."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 165: THE MOLE CONCEPT
        # =========================================================================
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
                        "text": "By the end of this module, you will define the Mole, state and apply Avogadro's Constant ($L = 6.022 \\times 10^{23}\\text{ particles/mol}$), understand Molar Mass ($M$), and convert effortlessly between mass, moles, and number of particles."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Counting Billions of Invisible Atoms",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In everyday life, we use convenient counting units for specific quantities:\n* A **pair** of shoes = $2$\n* A **dozen** eggs = $12$\n* A **baker's dozen** = $13$\n* A **gross** of pencils = $144$\n* A **ream** of exam paper = $500\\text{ sheets}$\n\nBecause atoms are unimaginably tiny, chemists need a much larger counting unit to group macroscopic quantities of particles into manageable packages. That counting unit is **the Mole**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Avogadro's Constant: The Bridge Between Atoms and Grams",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "One **mole** is defined as the amount of substance that contains exactly the same number of elementary particles (atoms, molecules, or ions) as there are carbon atoms in exactly $12\\text{ grams}$ of pure Carbon-12.\n\nThrough precise physical measurements, this number has been determined to be **Avogadro's Constant ($L$ or $N_A$)**:\n$$L = 6.022 \\times 10^{23} \\text{ particles per mole}$$\n\nWritten out in full, $6.022 \\times 10^{23}$ is:\n$$\\mathbf{602,200,000,000,000,000,000,000}$$\n\nIf you had a mole of marble stones, they would cover the entire surface of the Earth to a depth of several miles! Yet, exactly one mole of water molecules ($6.022 \\times 10^{23}$ molecules) fits into a small sip of water measuring just $18\\text{ cm}^3$!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: The Mole Bridge",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Flowchart diagram illustrating the Mole as the central bridge between Mass in Grams (divide/multiply by Molar Mass) and Number of Particles (multiply/divide by Avogadro's Constant 6.022 x 10^23).",
                        "caption": "The Mole Bridge: The Mole connects measurable mass in grams to the microscopic count of particles."
                    },
                    "asset_info": {
                        "title": "Mole Calculation Bridge Diagram",
                        "description": "Visual conversion triangle and bridge linking mass in grams, moles, and number of particles via Molar Mass and Avogadro's constant.",
                        "ai_instruction": "Create an instructional flowchart showing Mass (grams) on left, Moles in center, and Particles on right, with conversion arrows labeled with Molar Mass and Avogadro's Number."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Mole, Molar Mass, and Key Formulae",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Mole & Molar Mass",
                        "content": "### Molar Mass ($M$)\n*The mass in grams of one mole of a chemical substance (units: $\\text{g/mol}$).*\n- Numerically, Molar Mass is equal to the Relative Atomic Mass ($A_r$) or Relative Molecular Mass ($M_r$) expressed with the unit $\\text{g/mol}$.\n\n### The Golden Conversion Equations:\n$$\\text{Number of Moles } (n) = \\frac{\\text{Mass in grams } (m)}{\\text{Molar Mass } (M)}$$\n$$\\text{Mass in grams } (m) = \\text{Number of Moles } (n) \\times \\text{Molar Mass } (M)$$\n$$\\text{Number of Particles } (N) = \\text{Number of Moles } (n) \\times 6.022 \\times 10^{23}$$\n$$\\text{Number of Moles } (n) = \\frac{\\text{Number of Particles } (N)}{6.022 \\times 10^{23}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Mass and Particle Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. Calculate the mass of $0.25\\text{ moles}$ of anhydrous calcium carbonate ($\\text{CaCO}_3$). ($A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$).\n2. How many water molecules are present in a glass of water containing $36.0\\text{ g}$ of pure $\\text{H}_2\\text{O}$? ($L = 6.022 \\times 10^{23}\\text{ mol}^{-1}, A_r$: $\\text{H}=1.0, \\text{O}=16.0$).",
                        "steps": [
                            "**Problem 1: Mass of $0.25\\text{ moles}$ of $\\text{CaCO}_3$**\n- **1. What do we know?** $n = 0.25\\text{ mol}$, Chemical formula = $\\text{CaCO}_3$.\n- **2. Calculate Molar Mass ($M$)**:\n$$M = 40.0 + 12.0 + 3(16.0) = 100.0\\text{ g/mol}$$\n- **3. Formula & Calculation**:\n$$m = n \\times M = 0.25\\text{ mol} \\times 100.0\\text{ g/mol} = 25.0\\text{ g}$$\n- **4. Result**: $0.25\\text{ moles}$ of $\\text{CaCO}_3$ has a mass of $25.0\\text{ g}$.",
                            "**Problem 2: Number of Molecules in $36.0\\text{ g}$ of $\\text{H}_2\\text{O}$**\n- **1. What do we know?** Mass $m = 36.0\\text{ g}$, $L = 6.022 \\times 10^{23}\\text{ mol}^{-1}$.\n- **2. Calculate Molar Mass of $\\text{H}_2\\text{O}$**:\n$$M = 2(1.0) + 16.0 = 18.0\\text{ g/mol}$$\n- **3. Convert Mass to Moles**:\n$$n = \\frac{m}{M} = \\frac{36.0\\text{ g}}{18.0\\text{ g/mol}} = 2.0\\text{ moles}$$\n- **4. Convert Moles to Number of Molecules**:\n$$N = n \\times L = 2.0\\text{ mol} \\times 6.022 \\times 10^{23}\\text{ molecules/mol} = 1.2044 \\times 10^{24}\\text{ molecules}$$\n- **5. Result**: There are $1.2044 \\times 10^{24}$ water molecules in the glass."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Quantity vs Mass",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Misconception: Does 1 mole of Lead have the same mass as 1 mole of Helium?\n**Answer**: **NO!**\n\nThink about a dozen eggs versus a dozen watermelons. Both groups contain exactly 12 items, but a dozen watermelons are vastly heavier than a dozen eggs!\n\nSimilarly, $1\\text{ mole of Lead}$ and $1\\text{ mole of Helium}$ contain the exact same number of atoms ($6.022 \\times 10^{23}$ atoms). However, because a lead atom is much heavier than a helium atom, $1\\text{ mole of Lead}$ weighs **$207.2\\text{ grams}$**, while $1\\text{ mole of Helium}$ weighs only **$4.0\\text{ grams}$**!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Calculating Number of Atoms",
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
                        "explanation": "First, calculate moles: $n = \\frac{m}{M} = \\frac{4.6\\text{ g}}{23.0\\text{ g/mol}} = 0.2\\text{ mol}$. Then multiply by Avogadro's constant: $N = 0.2\\text{ mol} \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{23}\\text{ atoms}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: The Mole Concept",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: The Mole Concept\n- **The Mole**: A counting unit equal to $6.022 \\times 10^{23}$ particles ($L$).\n- **Molar Mass ($M$)**: Mass in grams of 1 mole of substance (numerical equivalent of $A_r$ or $M_r$ in $\\text{g/mol}$).\n- **Core Formulas**:\n  $$n = \\frac{m}{M} \\quad \\Longleftrightarrow \\quad m = n \\times M$$\n  $$N = n \\times L \\quad \\Longleftrightarrow \\quad n = \\frac{N}{L}$$"
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 166: EMPIRICAL AND MOLECULAR FORMULAE
        # =========================================================================
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
                        "text": "By the end of this module, you will distinguish between Empirical and Molecular formulae, determine empirical formulae from reacting masses and percentage composition data, and calculate molecular formulae using Relative Molecular Mass ($M_r$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Identifying Unknown Chemical Substances",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When a forensic chemist in Nairobi analyzes a white powder found at a crime scene or when a pharmaceutical company synthesizes a new malaria drug, the first question is: **What is its chemical formula?**\n\nTo identify the compound, chemists burn or decompose a pure sample to find the percentage of each element present. From this data, they work backwards to determine the simplest atomic ratio (**Empirical Formula**) and the true formula of the molecule (**Molecular Formula**)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Determination Methods",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In the school laboratory, empirical formulae are determined using two standard experimental techniques:\n\n1. **Direct Synthesis (e.g., Magnesium Oxide)**:\n   Heating a known mass of magnesium ribbon in a covered porcelain crucible allows oxygen from the air to react, forming magnesium oxide. Subtracting the initial mass of $\\text{Mg}$ from the final mass of $\\text{MgO}$ gives the mass of reacting oxygen.\n\n2. **Reduction of Metal Oxides (e.g., Copper(II) Oxide)**:\n   Passing dry hydrogen gas or methane gas over heated black copper(II) oxide in a combustion tube reduces it to reddish-brown copper metal:\n   $$\\text{CuO}_{(s)} + \\text{H}_{2(g)} \\xrightarrow{\\Delta} \\text{Cu}_{(s)} + \\text{H}_2\\text{O}_{(g)}$$\n   The mass of lost oxygen is determined directly by weighing."
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
                    "page_title": "Empirical vs Molecular Formulae",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Chemical Formula Types",
                        "content": "### Empirical Formula\n*The simplest formula showing the lowest whole-number ratio of atoms of the different elements present in a compound.*\n\n### Molecular Formula\n*The chemical formula showing the actual number of each kind of atom present in one molecule of a covalent compound.*\n\n### Mathematical Relationship:\n$$\\mathbf{\\text{Molecular Formula} = (\\text{Empirical Formula})_n}$$\n$$\\mathbf{n = \\frac{\\text{Relative Molecular Mass } (M_r)}{\\text{Empirical Formula Mass (E.F.M.)}}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Determining Empirical and Molecular Formulae",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. Burning $0.84\\text{ g}$ of magnesium ribbon yields $1.40\\text{ g}$ of magnesium oxide. Find its empirical formula ($A_r$: $\\text{Mg}=24.0, \\text{O}=16.0$).\n2. An organic compound has $57.15\\%\\text{ C}$, $4.76\\%\\text{ H}$, and $38.09\\%\\text{ O}$ by mass, with a Relative Molecular Mass ($M_r$) of $126.0$. Determine its empirical and molecular formulae.",
                        "steps": [
                            "**Problem 1: Empirical Formula of Magnesium Oxide**\n- **1. Determine Reacting Masses**:\n  - Mass of Magnesium = $0.84\\text{ g}$\n  - Mass of Oxygen $= 1.40\\text{ g} - 0.84\\text{ g} = 0.56\\text{ g}$\n- **2. Convert Masses to Moles**:\n  - Moles of $\\text{Mg} = \\frac{0.84\\text{ g}}{24.0\\text{ g/mol}} = 0.035\\text{ mol}$\n  - Moles of $\\text{O} = \\frac{0.56\\text{ g}}{16.0\\text{ g/mol}} = 0.035\\text{ mol}$\n- **3. Find Simplest Mole Ratio** (divide by smallest, $0.035$):\n  - $\\text{Mg} = \\frac{0.035}{0.035} = 1$\n  - $\\text{O} = \\frac{0.035}{0.035} = 1$\n- **Result**: Empirical Formula is $\\mathbf{\\text{MgO}}$.",
                            "**Problem 2: Molecular Formula from Percentage Composition**\n- **1. Assume $100\\text{ g}$ of compound**:\n  - Mass of $\\text{C} = 57.15\\text{ g}$, Mass of $\\text{H} = 4.76\\text{ g}$, Mass of $\\text{O} = 38.09\\text{ g}$\n- **2. Calculate Moles of Each Element**:\n  - Moles of $\\text{C} = \\frac{57.15}{12.0} = 4.7625\\text{ mol}$\n  - Moles of $\\text{H} = \\frac{4.76}{1.0} = 4.7600\\text{ mol}$\n  - Moles of $\\text{O} = \\frac{38.09}{16.0} = 2.3806\\text{ mol}$\n- **3. Divide by Smallest Moles ($2.3806$)**:\n  - $\\text{C} = \\frac{4.7625}{2.3806} = 2.00 \\approx 2$\n  - $\\text{H} = \\frac{4.7600}{2.3806} = 2.00 \\approx 2$\n  - $\\text{O} = \\frac{2.3806}{2.3806} = 1.00 = 1$\n  - **Empirical Formula** = $\\mathbf{\\text{C}_2\\text{H}_2\\text{O}}$\n- **4. Find Multiplier ($n$) using $M_r = 126.0$**:\n  - Empirical Formula Mass $= 2(12.0) + 2(1.0) + 16.0 = 42.0\\text{ g/mol}$\n  - $n = \\frac{M_r}{\\text{E.F.M.}} = \\frac{126.0}{42.0} = 3$\n- **Result**: Molecular Formula is $(\\text{C}_2\\text{H}_2\\text{O})_3 = \\mathbf{\\text{C}_6\\text{H}_6\\text{O}_3}$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: The Crucible Lid Technique",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why must the crucible lid be lifted periodically during magnesium combustion?\n1. **To admit oxygen**: Burning magnesium inside a tightly closed crucible quickly consumes the trapped oxygen and stops burning.\n2. **To prevent escape of white fumes**: When the lid is lifted, it must be replaced immediately. If white magnesium oxide smoke escapes, the recorded final mass will be too low, giving an inaccurate empirical ratio!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Finding Empirical Formula",
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
                    "page_number": 7,
                    "page_title": "Key Takeaways: Chemical Formulae",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Empirical & Molecular Formulae\n- **Empirical Formula**: Lowest whole-number ratio of atoms in a compound.\n- **Molecular Formula**: Actual number of atoms in a molecule ($\\text{Molecular} = (\\text{Empirical})_n$).\n- **4-Step Calculation Workflow**: Mass/Percentage $\\rightarrow$ Moles (divide by $A_r$) $\\rightarrow$ Simplest Ratio (divide by smallest) $\\rightarrow$ Integer Formula."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 167: CONCENTRATION AND MOLAR SOLUTIONS
        # =========================================================================
        167: {
            "topic": topic_23,
            "title": "Concentration of Solutions and Molar Solutions",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Measuring Solution Strength",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will define concentration in $\\text{g/dm}^3$ and Molarity in $\\text{mol/dm}^3$ ($M$), prepare standard molar solutions, and interconvert between mass concentration and molarity."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Precision in Solution Preparation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When making Kenyan tea or fruit juice, we loosely describe strength as \"strong\" or \"dilute\". But in a hospital pharmacy in Nairobi preparing intravenous saline injections, concentrations must be precise to the decimal point to safeguard patient lives.\n\nIn Chemistry, the quantitative measure of dissolved solute within a given volume of solution is called **Concentration**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Understanding Dissolution at the Particle Level",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's examine how solid solute dissolves into solution:\n\n* **Macroscopic Observation**:\n  Adding white sodium hydroxide ($\\text{NaOH}$) pellets to distilled water causes the solid to disappear, forming a clear solution and releasing thermal energy (exothermic dissolution).\n\n* **Microscopic Particle Model**:\n  The crystal lattice of $\\text{Na}^+$ and $\\text{OH}^-$ ions breaks apart. Individual water molecules surround the ions (hydration) and disperse them uniformly throughout the solvent.\n\n* **Units of Measurement**:\n  - **Mass Concentration**: Grams of solute per litre of solution ($\\text{g/dm}^3$ or $\\text{g L}^{-1}$).\n  - **Molarity ($M$)**: Moles of solute per litre of solution ($\\text{mol/dm}^3$ or $\\text{M}$).\n  - *Conversion*: $1\\text{ Litre} = 1\\text{ dm}^3 = 1000\\text{ cm}^3\\text{ (or mL)}$."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Preparing a Standard Solution in a Volumetric Flask",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Multi-step diagram showing preparation of a standard solution: Step 1 (weighing solid in beaker), Step 2 (dissolving with distilled water and stirring with glass rod), Step 3 (transferring through filter funnel into volumetric flask), Step 4 (rinsing beaker and funnel), Step 5 (topping up to the graduation mark with wash bottle and inverting to mix).",
                        "caption": "Standard Solution Protocol: Dissolve solid completely, transfer quantitatively, and fill to the exact meniscus mark."
                    },
                    "asset_info": {
                        "title": "Volumetric Flask Solution Preparation",
                        "description": "Five-step procedure for preparing a primary standard solution in volumetric glassware.",
                        "ai_instruction": "Create a clean 5-panel infographic showing weighing, dissolving, quantitative transfer via funnel, meniscus adjustment, and inversion mixing."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Molar Solutions & Concentration Formulae",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Concentration & Molarity",
                        "content": "### Molar Solution (1.0 M)\n*A solution containing exactly one mole of solute dissolved in water and made up to exactly one litre ($1000\\text{ cm}^3$) of solution.*\n\n### The Fundamental Mathematical Equations:\n$$\\mathbf{\\text{Concentration } (\\text{g/dm}^3) = \\frac{\\text{Mass of solute in grams } (m)}{\\text{Volume in dm}^3 (V)}}$$\n$$\\mathbf{\\text{Molarity } (M, \\text{mol/dm}^3) = \\frac{\\text{Moles of solute } (n)}{\\text{Volume in dm}^3 (V)}}$$\n$$\\mathbf{\\text{Concentration } (\\text{g/dm}^3) = \\text{Molarity } (\\text{mol/dm}^3) \\times \\text{Molar Mass } (M)}$$\n$$\\mathbf{\\text{Number of Moles } (n) = \\frac{\\text{Molarity } (M) \\times \\text{Volume in cm}^3 (V)}{1000}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Concentration & Molarity Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. If $4.0\\text{ g}$ of sodium hydroxide ($\\text{NaOH}$) is dissolved to make $500\\text{ cm}^3$ of solution, find its concentration in $\\text{g/dm}^3$ and its Molarity ($M$). ($A_r$: $\\text{Na}=23.0, \\text{O}=16.0, \\text{H}=1.0$).\n2. Calculate the mass of calcium chloride ($\\text{CaCl}_2$) required to prepare $250\\text{ cm}^3$ of a $0.20\\text{ M}$ solution. ($A_r$: $\\text{Ca}=40.0, \\text{Cl}=35.5$).",
                        "steps": [
                            "**Problem 1: Concentration of $\\text{NaOH}$ Solution**\n- **1. What do we know?** Mass $m = 4.0\\text{ g}$, Volume $V = 500\\text{ cm}^3 = 0.50\\text{ dm}^3$.\n- **2. Calculate Mass Concentration**:\n$$\\text{Concentration} = \\frac{\\text{Mass in grams}}{\\text{Volume in dm}^3} = \\frac{4.0\\text{ g}}{0.50\\text{ dm}^3} = 8.0\\text{ g/dm}^3$$\n- **3. Calculate Molar Mass ($M$) of $\\text{NaOH}$**:\n$$M = 23.0 + 16.0 + 1.0 = 40.0\\text{ g/mol}$$\n- **4. Calculate Molarity ($M$)**:\n$$\\text{Molarity} = \\frac{\\text{Concentration in g/dm}^3}{\\text{Molar Mass}} = \\frac{8.0\\text{ g/dm}^3}{40.0\\text{ g/mol}} = 0.20\\text{ mol/dm}^3\\text{ (or } 0.20\\text{ M)}$$",
                            "**Problem 2: Mass of $\\text{CaCl}_2$ Needed**\n- **1. What do we know?** $M = 0.20\\text{ M}$, $V = 250\\text{ cm}^3$, Molar mass of $\\text{CaCl}_2 = 40.0 + 2(35.5) = 111.0\\text{ g/mol}$.\n- **2. Calculate Moles of $\\text{CaCl}_2$ Needed**:\n$$n = \\frac{M \\times V(\\text{cm}^3)}{1000} = \\frac{0.20 \\times 250}{1000} = 0.050\\text{ moles}$$\n- **3. Convert Moles to Mass**:\n$$m = n \\times M = 0.050\\text{ mol} \\times 111.0\\text{ g/mol} = 5.55\\text{ g}$$\n- **Result**: Weigh out exactly $5.55\\text{ g}$ of $\\text{CaCl}_2$ solid."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Volumetric Flasks Have Narrow Necks",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why are standard solutions prepared in volumetric flasks with long, narrow necks rather than beakers?\nIn a wide beaker, adding an extra $5\\text{ mL}$ of water changes the liquid height by only a fraction of a millimeter, making precise volume measurement impossible.\n\nIn a narrow-necked volumetric flask, even a single drop ($0.05\\text{ mL}$) causes a visible shift in the bottom of the meniscus against the etched calibration line. This ensures maximum volumetric accuracy ($\pm 0.1\\%$)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Calculating Solution Molarity",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the molarity of a solution prepared by dissolving $10.6\\text{ g}$ of anhydrous sodium carbonate ($\\text{Na}_2\\text{CO}_3$) in distilled water to make $500\\text{ cm}^3$ of solution? ($A_r$: $\\text{Na}=23.0, \\text{C}=12.0, \\text{O}=16.0$).",
                        "options": [
                            "$0.10\\text{ M}$",
                            "$0.20\\text{ M}$",
                            "$0.50\\text{ M}$",
                            "$1.00\\text{ M}$"
                        ],
                        "answer": "B",
                        "explanation": "Molar mass of $\\text{Na}_2\\text{CO}_3 = 2(23) + 12 + 3(16) = 106.0\\text{ g/mol}$. Moles $n = \\frac{10.6\\text{ g}}{106.0\\text{ g/mol}} = 0.10\\text{ mol}$. Volume in $\\text{dm}^3 = \\frac{500}{1000} = 0.50\\text{ dm}^3$. Molarity $= \\frac{0.10\\text{ mol}}{0.50\\text{ dm}^3} = 0.20\\text{ mol/dm}^3$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Molar Solutions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Concentration and Molarity\n- **Concentration**: $\\text{g/dm}^3 = \\frac{\\text{Mass}}{\\text{Volume in dm}^3}$.\n- **Molarity ($M$)**: $\\text{mol/dm}^3 = \\frac{\\text{Moles}}{\\text{Volume in dm}^3}$.\n- **Key Conversion**: $\\text{Concentration } (\\text{g/dm}^3) = \\text{Molarity } (M) \\times \\text{Molar Mass } (M)$.\n- **Moles in Volume**: $n = \\frac{M \\times V(\\text{cm}^3)}{1000}$."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 168: DILUTION OF SOLUTIONS
        # =========================================================================
        168: {
            "topic": topic_23,
            "title": "Dilution of Solutions",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Principle of Dilution",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the Dilution Law ($C_1V_1 = C_2V_2$), calculate the volume of stock solution required to prepare diluted solutions, and explain why adding solvent preserves the total moles of solute."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Spreading Particles Across Larger Volumes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When making fruit juice from concentrated syrup, taking a sip directly from the bottle is overpoweringly sweet. We pour a small volume of syrup into a glass and add clean water.\n\nAdding water does not change the total number of sugar molecules. It simply spreads them out across a larger volume. In Chemistry, this process is called **Dilution**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Constant Moles and Expanding Volumes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's examine dilution at macroscopic and particle levels:\n\n* **Macroscopic Observation**:\n  Pipetting $25\\text{ cm}^3$ of concentrated $2.0\\text{ M } \\text{HCl}$ into a $250\\text{ cm}^3$ volumetric flask and topping up with distilled water yields a much milder, safer acid solution.\n\n* **Microscopic Particle Model**:\n  The initial $25\\text{ cm}^3$ contains a fixed quantity of hydronium and chloride ions. Adding water inserts solvent molecules between ions, increasing their spacing without altering the total count of solute particles.\n\n* **Symbolic Representation**:\n  $$\\text{Moles of solute before dilution} = \\text{Moles of solute after dilution}$$\n  $$\\frac{C_1V_1}{1000} = \\frac{C_2V_2}{1000} \\quad \\implies \\quad \\mathbf{C_1V_1 = C_2V_2}$$"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Particle Spacing During Dilution",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram comparing Concentrated Solution on left (dense crowd of solute particles in small volume) and Diluted Solution on right (identical particle count spread widely throughout large volume).",
                        "caption": "Dilution Principle: Solute particle count remains perfectly constant while volume increases, lowering molarity."
                    },
                    "asset_info": {
                        "title": "Dilution Particle Model",
                        "description": "Microscopic particle model showing solute conservation during volume expansion.",
                        "ai_instruction": "Create two side-by-side beakers showing 10 solute particles packed in 50mL on left, and the same 10 particles dispersed in 250mL on right."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Dilution Law & Volume Accounting",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Dilution Law",
                        "content": "$$\\mathbf{C_1V_1 = C_2V_2}$$\nWhere:\n- $C_1$ = Initial stock concentration (Molarity or $\\text{g/dm}^3$)\n- $V_1$ = Volume of concentrated stock solution used\n- $C_2$ = Target final diluted concentration\n- $V_2$ = Total final volume of diluted solution\n\n### Volume of Water Added ($V_{\\text{water}}$):\n$$\\mathbf{V_{\\text{water}} = V_2 - V_1}$$\n*Crucial Rule*: Units of concentration and volume must be identical on both sides."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Dilution Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. If $25.0\\text{ cm}^3$ of $2.0\\text{ M } \\text{HCl}$ stock solution is diluted with distilled water to make a total volume of $250.0\\text{ cm}^3$, calculate the new concentration ($C_2$).\n2. What volume of $2.0\\text{ M } \\text{H}_2\\text{SO}_4$ stock solution is required to prepare $500.0\\text{ cm}^3$ of a $0.10\\text{ M}$ dilute acid solution? Calculate the volume of distilled water that must be added.",
                        "steps": [
                            "**Problem 1: Calculating Final Concentration ($C_2$)**\n- **1. What do we know?** $C_1 = 2.0\\text{ M}, V_1 = 25.0\\text{ cm}^3, V_2 = 250.0\\text{ cm}^3$.\n- **2. Apply Dilution Law**:\n$$C_1V_1 = C_2V_2 \\quad \\implies \\quad C_2 = \\frac{C_1 V_1}{V_2}$$\n- **3. Calculation**:\n$$C_2 = \\frac{2.0\\text{ M} \\times 25.0\\text{ cm}^3}{250.0\\text{ cm}^3} = \\frac{50.0}{250.0} = 0.20\\text{ M}$$\n- **Result**: The diluted acid has a concentration of $0.20\\text{ M}$ (a 10-fold dilution).",
                            "**Problem 2: Volume of Stock and Water Needed**\n- **1. What do we know?** $C_1 = 2.0\\text{ M}, C_2 = 0.10\\text{ M}, V_2 = 500.0\\text{ cm}^3$.\n- **2. Calculate Required Stock Volume ($V_1$)**:\n$$V_1 = \\frac{C_2 V_2}{C_1} = \\frac{0.10\\text{ M} \\times 500.0\\text{ cm}^3}{2.0\\text{ M}} = \\frac{50.0}{2.0} = 25.0\\text{ cm}^3$$\n- **3. Calculate Volume of Distilled Water to Add**:\n$$V_{\\text{water}} = V_2 - V_1 = 500.0\\text{ cm}^3 - 25.0\\text{ cm}^3 = 475.0\\text{ cm}^3$$\n- **Result**: Measure $25.0\\text{ cm}^3$ of stock acid and add $475.0\\text{ cm}^3$ of water to make $500.0\\text{ cm}^3$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: The Acid Dilution Safety Rule",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### The Golden Safety Rule: Always Add Acid to Water (AA)\nNever add water directly to concentrated sulfuric acid!\n\nDissolving concentrated $\\text{H}_2\\text{SO}_4$ in water is extremely exothermic. Because water is less dense than acid, adding water causes it to sit on top of the acid. The localized intense heat boils the water instantly, causing violent splattering of corrosive acid into your face!\n\n**Always add concentrated acid slowly down the side of a glass rod into a large volume of water with constant stirring.**"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Diluting Nitric Acid",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of water must be added to $50.0\\text{ cm}^3$ of $4.0\\text{ M } \\text{HNO}_3$ to dilute it to a $0.50\\text{ M}$ solution?",
                        "options": [
                            "$400.0\\text{ cm}^3$",
                            "$350.0\\text{ cm}^3$",
                            "$450.0\\text{ cm}^3$",
                            "$500.0\\text{ cm}^3$"
                        ],
                        "answer": "B",
                        "explanation": "First find total final volume $V_2$: $C_1V_1 = C_2V_2 \\implies V_2 = \\frac{4.0 \\times 50.0}{0.50} = 400.0\\text{ cm}^3$. The question asks for volume of water added: $V_{\\text{water}} = V_2 - V_1 = 400.0 - 50.0 = 350.0\\text{ cm}^3$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Dilution",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Dilution of Solutions\n- **Principle**: Total moles of solute remain constant during dilution.\n- **The Dilution Formula**: $C_1V_1 = C_2V_2$.\n- **Water Added**: $V_{\\text{water}} = V_2 - V_1$.\n- **Safety Protocol**: Always add concentrated acid to water slowly with stirring."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 169: STOICHIOMETRY (REACTING MASSES AND VOLUMES)
        # =========================================================================
        169: {
            "topic": topic_23,
            "title": "Stoichiometry of Chemical Equations (Reacting Masses and Volumes)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Chemical Recipes & Stoichiometry",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will interpret balanced chemical equations in terms of mole ratios, calculate reacting masses, apply Molar Gas Volume ($22.4\\text{ dm}^3$ at s.t.p. and $24.0\\text{ dm}^3$ at r.t.p.), and solve Gay-Lussac reacting volume problems."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Exact Recipes of Nature",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When baking a cake, following an exact recipe (e.g., $2\\text{ cups flour} + 1\\text{ cup sugar} + 3\\text{ eggs}$) ensures the cake rises perfectly. If you add too much flour or too little sugar, the cake is ruined.\n\nChemical reactions follow nature's exact quantitative recipes. A balanced chemical equation tells us the precise ratio in which atoms and molecules react. In Chemistry, the study of these quantitative mass and volume relationships is called **Stoichiometry**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Reacting Atoms & Balanced Equations",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Consider the combustion of methane gas:\n$$\\text{CH}_{4(g)} + 2\\text{O}_{2(g)} \\rightarrow \\text{CO}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)}$$\n\n* **Reading the Equation at Multiple Levels**:\n  - *Molecular Level*: $1\\text{ molecule of } \\text{CH}_4$ reacts with $2\\text{ molecules of } \\text{O}_2$ to yield $1\\text{ molecule of } \\text{CO}_2$ and $2\\text{ molecules of } \\text{H}_2\\text{O}$.\n  - *Molar Level*: $\\mathbf{1\\text{ mole of } \\text{CH}_4} + \\mathbf{2\\text{ moles of } \\text{O}_2} \\rightarrow \\mathbf{1\\text{ mole of } \\text{CO}_2} + \\mathbf{2\\text{ moles of } \\text{H}_2\\text{O}}$.\n  - *Mass Level*: $16.0\\text{ g of } \\text{CH}_4 + 64.0\\text{ g of } \\text{O}_2 \\rightarrow 44.0\\text{ g of } \\text{CO}_2 + 36.0\\text{ g of } \\text{H}_2\\text{O}$ (Total mass = $80.0\\text{ g}$ on both sides, confirming Conservation of Mass!)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Molar Gas Volumes at STP vs RTP",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram showing 1 mole of any gas (Helium, Oxygen, Carbon Dioxide) occupying a cube of 22.4 dm3 at s.t.p. and a cube of 24.0 dm3 at r.t.p.",
                        "caption": "Avogadro's Gas Law: 1 mole of any gas occupies 22.4 dm3 at s.t.p. and 24.0 dm3 at r.t.p."
                    },
                    "asset_info": {
                        "title": "Molar Gas Volume Comparison Diagram",
                        "description": "Visual comparison of 1 mole of gas occupying 22.4L at s.t.p. and 24.0L at r.t.p.",
                        "ai_instruction": "Create an illustration comparing two transparent gas cubes labeled 22.4 dm3 (s.t.p., 0°C) and 24.0 dm3 (r.t.p., 25°C) holding 1 mole of gas."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Molar Gas Volumes & Gay-Lussac's Law",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Gas Stoichiometry",
                        "content": "### Molar Gas Volume ($V_m$)\n*The volume occupied by one mole of any gas at a given temperature and pressure.*\n- At standard temperature and pressure (**s.t.p.**): **$V_m = 22.4\\text{ dm}^3\\text{ (or } 22400\\text{ cm}^3\\text{)}$**\n- At room temperature and pressure (**r.t.p.**): **$V_m = 24.0\\text{ dm}^3\\text{ (or } 24000\\text{ cm}^3\\text{)}$**\n\n### Gas Volume Equation:\n$$\\mathbf{\\text{Volume of Gas } (V) = \\text{Moles } (n) \\times V_m}$$\n$$\\mathbf{\\text{Number of Moles } (n) = \\frac{\\text{Volume in dm}^3}{V_m}}$$\n\n### Gay-Lussac's Law of Combining Volumes:\n*When gases react, they do so in volumes which bear a simple whole-number ratio to one another and to the volume of gaseous products, provided temperature and pressure remain constant.*"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Reacting Mass and Gas Volume Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of carbon dioxide gas ($\\text{CO}_2$) produced at r.t.p. when $10.0\\text{ g}$ of pure calcium carbonate ($\\text{CaCO}_3$) reacts completely with excess dilute hydrochloric acid.\n$$\\text{CaCO}_{3(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{CaCl}_{2(aq)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)}$$\n(Given $A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$; Molar gas volume at r.t.p. = $24.0\\text{ dm}^3\\text{/mol}$).",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- Mass of reactant $\\text{CaCO}_3 = 10.0\\text{ g}$\n- Molar mass of $\\text{CaCO}_3 = 40.0 + 12.0 + 3(16.0) = 100.0\\text{ g/mol}$\n- Reaction condition: r.t.p. ($V_m = 24.0\\text{ dm}^3\\text{/mol}$)",
                            "**2. What are we finding?**\n- Volume of $\\text{CO}_2$ gas produced in $\\text{dm}^3$ (and $\\text{cm}^3$).",
                            "**3. Step 1: Convert Reactant Mass to Moles**:\n$$n(\\text{CaCO}_3) = \\frac{m}{M} = \\frac{10.0\\text{ g}}{100.0\\text{ g/mol}} = 0.10\\text{ moles}$$",
                            "**4. Step 2: Use Stoichiometric Mole Ratio from Equation**:\n$$\\text{Mole Ratio of } \\text{CaCO}_3 : \\text{CO}_2 = 1 : 1$$\n$$\\implies n(\\text{CO}_2) = n(\\text{CaCO}_3) = 0.10\\text{ moles of } \\text{CO}_2$$",
                            "**5. Step 3: Convert Moles to Gas Volume at r.t.p.**:\n$$V(\\text{CO}_2) = n \\times V_m = 0.10\\text{ mol} \\times 24.0\\text{ dm}^3\\text{/mol} = 2.40\\text{ dm}^3$$\n$$V = 2.40 \\times 1000 = 2400\\text{ cm}^3$$\n- **Result**: Exactly $2.40\\text{ dm}^3$ ($2400\\text{ cm}^3$) of $\\text{CO}_2$ gas is collected."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why All Gases Have Equal Molar Volumes",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does 1 mole of heavy CO2 (44g) occupy the exact same volume as 1 mole of light H2 (2g)?\nIn a gas, individual particles are separated by vast empty distances (over $10\\text{ times}$ their molecular diameters). The actual physical size of the molecules is completely negligible.\n\nAt a given temperature and pressure, collision frequency and kinetic push depend strictly on the **number of particles ($6.022 \\times 10^{23}$)**, not their individual sizes or weights!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Gay-Lussac Volume Ratio",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of oxygen gas is required for the complete combustion of $40.0\\text{ cm}^3$ of propane gas ($\\text{C}_3\\text{H}_8$) at constant temperature and pressure?\n$$\\text{C}_3\\text{H}_{8(g)} + 5\\text{O}_{2(g)} \\rightarrow 3\\text{CO}_{2(g)} + 4\\text{H}_2\\text{O}_{(l)}$$",
                        "options": [
                            "$40.0\\text{ cm}^3$",
                            "$120.0\\text{ cm}^3$",
                            "$200.0\\text{ cm}^3$",
                            "$8.0\\text{ cm}^3$"
                        ],
                        "answer": "C",
                        "explanation": "According to Gay-Lussac's Law, reacting gas volumes are in the same ratio as equation coefficients. Ratio of $\\text{C}_3\\text{H}_8 : \\text{O}_2 = 1 : 5$. Volume of $\\text{O}_2 = 5 \\times 40.0\\text{ cm}^3 = 200.0\\text{ cm}^3$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Stoichiometry",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Stoichiometry and Molar Volumes\n- **Mole Ratio**: Obtained directly from balanced equation coefficients.\n- **Molar Gas Volumes**: $1\\text{ mole} = 22.4\\text{ dm}^3$ at s.t.p. ($0^\\circ\\text{C}$); $24.0\\text{ dm}^3$ at r.t.p. ($25^\\circ\\text{C}$).\n- **3-Step Stoichiometric Calculation Workflow**: Known Quantity $\\rightarrow$ Moles of Known $\\rightarrow$ Moles of Target (Mole Ratio) $\\rightarrow$ Target Mass / Volume."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 170: VOLUMETRIC ANALYSIS (ACID-BASE TITRATIONS)
        # =========================================================================
        170: {
            "topic": topic_23,
            "title": "Volumetric Analysis (Acid-Base Titrations)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Determining Exact Concentrations",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the principles of acid-base titration, correctly read burettes and pipettes, select appropriate indicators (phenolphthalein and methyl orange), and calculate unknown concentrations using the titration formula ($\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b}$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Quality Control in Food and Manufacturing",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When a beverage manufacturer in Kenya produces juice or vinegar, food regulators require the exact acidity level to be certified on the label. How do chemists determine the exact concentration of an unknown acid or alkali solution?\n\nThey use **Volumetric Analysis (Titration)**—a precision laboratory method where a solution of known concentration (a standard solution) is reacted with an exact volume of an unknown solution until neutralization is complete!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Running a Laboratory Titration",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "An acid-base titration involves precise glassware and chemical indicators:\n\n1. **Pipette**: Delivers an exact volume (usually $25.0\\text{ cm}^3$) of base into a clean conical flask.\n2. **Burette**: Dispenses acid drop-by-drop until the neutralization **end-point** is reached.\n3. **Indicators & Color Changes**:\n   - **Phenolphthalein**: Pink in base $\\rightarrow$ Colorless at end-point (used for strong base titrations).\n   - **Methyl Orange**: Yellow in base $\\rightarrow$ Orange/pink at end-point (used for strong acid / weak base titrations, e.g., $\\text{Na}_2\\text{CO}_3$)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Acid-Base Titration Apparatus",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram of a complete laboratory titration setup: Clamp stand holding a 50mL burette with stopcock filled with acid, dispensing into a conical flask containing base and indicator resting on a white tile. Zoom-in showing correct reading of the bottom of the meniscus.",
                        "caption": "Titration Setup: Acid from the burette is added dropwise into the conical flask on a white tile until the indicator sharply changes color."
                    },
                    "asset_info": {
                        "title": "Titration Apparatus Technical Schematic",
                        "description": "Standard volumetric analysis laboratory setup featuring burette, conical flask, white tile, and meniscus reading guide.",
                        "ai_instruction": "Create a clear laboratory diagram showing burette clamped over conical flask on white tile, with meniscus zoom-in box."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Master Titration Formula",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Titration Calculations",
                        "content": "### The Fundamental Titration Equation:\n$$\\mathbf{\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b}}$$\nWhere:\n- $M_a$ = Molarity of Acid ($\\text{mol/dm}^3$)\n- $V_a$ = Average volume (titre) of Acid from burette ($\\text{cm}^3$)\n- $M_b$ = Molarity of Base ($\\text{mol/dm}^3$)\n- $V_b$ = Volume of Base measured by pipette ($\\text{cm}^3$)\n- $a$ and $b$ = Mole coefficients of Acid and Base in the balanced chemical equation ($a\\text{ Acid} + b\\text{ Base} \\rightarrow \\text{Products}$)"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Acid Standardisation Titration",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$25.0\\text{ cm}^3$ of $0.10\\text{ M}$ sodium carbonate solution ($\\text{Na}_2\\text{CO}_3$) required $20.0\\text{ cm}^3$ of hydrochloric acid ($\\text{HCl}$) for complete neutralization using methyl orange indicator. Calculate the molarity and mass concentration (in $\\text{g/dm}^3$) of the hydrochloric acid. ($A_r$: $\\text{H}=1.0, \\text{Cl}=35.5$).",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- Base ($\\text{Na}_2\\text{CO}_3$): $M_b = 0.10\\text{ M}, V_b = 25.0\\text{ cm}^3$\n- Acid ($\\text{HCl}$): $V_a = 20.0\\text{ cm}^3, M_a = \\text{Target Molarity}$",
                            "**2. Write the Balanced Chemical Equation**:\n$$\\mathbf{2}\\text{HCl}_{(aq)} + \\mathbf{1}\\text{Na}_2\\text{CO}_{3(aq)} \\rightarrow 2\\text{NaCl}_{(aq)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)}$$\n- Mole ratio $a : b = 2 : 1$",
                            "**3. Apply the Titration Formula**:\n$$\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b} \\quad \\implies \\quad M_a = \\frac{a \\times M_b \\times V_b}{b \\times V_a}$$",
                            "**4. Substitute Values & Calculate Molarity**:\n$$M_a = \\frac{2 \\times 0.10\\text{ M} \\times 25.0\\text{ cm}^3}{1 \\times 20.0\\text{ cm}^3} = \\frac{5.0}{20.0} = 0.25\\text{ mol/dm}^3\\text{ (or } 0.25\\text{ M)}$$",
                            "**5. Calculate Mass Concentration in $\\text{g/dm}^3$**:\n- Molar mass of $\\text{HCl} = 1.0 + 35.5 = 36.5\\text{ g/mol}$\n$$\\text{Concentration} = M_a \\times M_r = 0.25\\text{ mol/dm}^3 \\times 36.5\\text{ g/mol} = 9.125\\text{ g/dm}^3$$\n- **Result**: The hydrochloric acid is $0.25\\text{ M}$ ($9.13\\text{ g/dm}^3$)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Glassware Rinsing Protocols",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### The Glassware Rinsing Golden Rules:\n1. **Burette & Pipette**: Must be rinsed with distilled water, then **rinsed with the actual solution they are to hold**! Rinsing only with water leaves droplets that dilute the solution, causing significant volumetric error.\n2. **Conical Flask**: Must be rinsed **ONLY with distilled water**! Never rinse with the base solution. Water droplets in the conical flask do NOT change the number of moles of base pipetted inside."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Titration Mole Ratio",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "$25.0\\text{ cm}^3$ of $0.05\\text{ M } \\text{H}_2\\text{SO}_4$ neutralizes $25.0\\text{ cm}^3$ of $\\text{NaOH}$ solution. What is the molarity of the sodium hydroxide?\n$$\\text{H}_2\\text{SO}_4 + 2\\text{NaOH} \\rightarrow \\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}$$",
                        "options": [
                            "$0.025\\text{ M}$",
                            "$0.05\\text{ M}$",
                            "$0.10\\text{ M}$",
                            "$0.20\\text{ M}$"
                        ],
                        "answer": "C",
                        "explanation": "Equation: $a=1, b=2$. $\\frac{M_a V_a}{M_b V_b} = \\frac{1}{2} \\implies M_b = \\frac{2 M_a V_a}{V_b} = \\frac{2 \\times 0.05 \\times 25.0}{25.0} = 0.10\\text{ M}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Volumetric Analysis",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Acid-Base Titrations\n- **Apparatus**: Pipette (delivers fixed volume), Burette (dispenses variable volume), Conical flask on white tile.\n- **Indicators**: Phenolphthalein (pink $\\rightarrow$ colorless); Methyl Orange (yellow $\\rightarrow$ orange).\n- **Master Equation**: $\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b}$."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 171: BACK TITRATIONS
        # =========================================================================
        171: {
            "topic": topic_23,
            "title": "Analyzing Complex Systems: Back Titrations",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Challenge of Insoluble Reactants",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will master the two-stage logic of Back Titration, determine the purity of insoluble substances (such as limestone, eggshells, and antacid tablets), and perform multi-step residual mole calculations."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Analyzing Insoluble Rocks and Minerals",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In regular direct titrations, both reactants must dissolve completely into clear aqueous solutions. But how do quality control chemists at **Bamburi Cement in Mombasa** test the purity of solid limestone ($\\text{CaCO}_3$) rocks? Or how do agronomists determine the calcium carbonate content of soil?\n\nLimestone is insoluble in water, so it cannot be put into a burette or pipette! To analyze insoluble or slow-reacting solids, chemists use an ingenious indirect technique called **Back Titration**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Two-Stage Back Titration Strategy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "A back titration is carried out in two distinct stages:\n\n* **Stage 1: Complete Dissolution in Known Excess Acid**:\n  A weighed mass of the impure solid (e.g., limestone) is reacted with a known, measured **excess volume of standardized acid** (e.g., $\\text{HCl}$):\n  $$\\text{CaCO}_{3(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{CaCl}_{2(aq)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)}$$\n  The solid dissolves completely, consuming some of the acid while leaving a known leftover portion of unreacted acid in solution.\n\n* **Stage 2: Titrating the Leftover (Excess) Acid**:\n  The unreacted excess acid is \"titrated back\" against a standard base (such as $\\text{NaOH}$):\n  $$\\text{HCl}_{(aq, \\text{leftover})} + \\text{NaOH}_{(aq)} \\rightarrow \\text{NaCl}_{(aq)} + \\text{H}_2\\text{O}_{(l)}$$\n  Knowing how much acid remains allows us to calculate exactly how much acid reacted with the limestone in Stage 1!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Two-Stage Back Titration Flowchart",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Flowchart diagram illustrating Back Titration accounting: Step 1 (Total Moles of Acid Added) = Step 2 (Moles of Acid Reacted with Insoluble Solid) + Step 3 (Moles of Acid Leftover Titrated with NaOH).",
                        "caption": "Back Titration Accounting: Total Acid Moles Added = Moles Reacted with Solid + Moles Titrated by NaOH."
                    },
                    "asset_info": {
                        "title": "Back Titration Workflow Diagram",
                        "description": "Two-stage visual flowchart illustrating total acid allocation between insoluble solid and back-titrated base.",
                        "ai_instruction": "Create a clean flowchart showing Total Acid bar split into two sections: Reacted with Sample + Titrated by Base."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Golden Principle of Back Titration",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Back Titration Accounting",
                        "content": "### The Fundamental Conservation Rule:\n$$\\mathbf{\\text{Total Moles of Acid Added} = \\text{Moles Reacted with Solid} + \\text{Moles Leftover/Unreacted}}$$\n\n### Rearranging to find the sample:\n$$\\mathbf{\\text{Moles of Acid Reacted with Solid} = \\text{Total Moles Added} - \\text{Moles Leftover (from Titration)}}$$\n\n### Percentage Purity:\n$$\\mathbf{\\%\\text{ Purity} = \\frac{\\text{Calculated Pure Mass of Substance}}{\\text{Total Mass of Impure Sample}} \\times 100}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Limestone Purity Calculation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$1.25\\text{ g}$ of impure limestone (containing $\\text{CaCO}_3$) was added to $50.0\\text{ cm}^3$ of $1.0\\text{ M } \\text{HCl}$ (an excess). After the reaction ceased, the remaining unreacted acid required $20.0\\text{ cm}^3$ of $0.50\\text{ M } \\text{NaOH}$ for complete neutralization. Calculate the percentage purity of calcium carbonate in the limestone sample. ($A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$).",
                        "steps": [
                            "**1. Step 1: Calculate Total Moles of Acid Added Initially**\n$$n_{\\text{total}}(\\text{HCl}) = \\frac{M \\times V}{1000} = \\frac{1.0\\text{ M} \\times 50.0\\text{ cm}^3}{1000} = 0.050\\text{ moles}$$",
                            "**2. Step 2: Calculate Moles of Leftover Acid Titrated by $\\text{NaOH}$**\n- Moles of $\\text{NaOH}$ used: $n(\\text{NaOH}) = \\frac{0.50\\text{ M} \\times 20.0\\text{ cm}^3}{1000} = 0.010\\text{ moles}$\n- Reaction: $\\text{HCl} + \\text{NaOH} \\rightarrow \\text{NaCl} + \\text{H}_2\\text{O}$ (Ratio $1:1$)\n$$\\implies n_{\\text{leftover}}(\\text{HCl}) = 0.010\\text{ moles}$$",
                            "**3. Step 3: Calculate Moles of Acid That Reacted with Limestone**\n$$n_{\\text{reacted}}(\\text{HCl}) = n_{\\text{total}} - n_{\\text{leftover}} = 0.050 - 0.010 = 0.040\\text{ moles}$$",
                            "**4. Step 4: Calculate Mass of Pure $\\text{CaCO}_3$ in Sample**\n- Reaction: $\\text{CaCO}_3 + 2\\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2$ (Ratio $1 \\text{ CaCO}_3 : 2 \\text{ HCl}$)\n$$n(\\text{CaCO}_3) = \\frac{n_{\\text{reacted}}(\\text{HCl})}{2} = \\frac{0.040\\text{ mol}}{2} = 0.020\\text{ moles}$$\n- Molar mass of $\\text{CaCO}_3 = 100.0\\text{ g/mol}$\n$$\\text{Mass of pure } \\text{CaCO}_3 = 0.020\\text{ mol} \\times 100.0\\text{ g/mol} = 2.00\\text{ g} \\implies 1.00\\text{ g}$$ (Note: $0.020 \\times 100.0 = 1.00\\text{ g}$)",
                            "**5. Step 5: Calculate Percentage Purity**\n$$\\%\\text{ Purity} = \\frac{\\text{Pure Mass}}{\\text{Total Sample Mass}} \\times 100 = \\frac{1.00\\text{ g}}{1.25\\text{ g}} \\times 100 = 80.0\\%$$\n- **Result**: The limestone sample is $80.0\\%$ pure calcium carbonate."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why We Subtract Leftover Moles",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why is it called a \"Back\" Titration?\nBecause we do not titrate the limestone directly. We add excess acid, and then \"titrate back\" the leftover portion.\n\nThink of it like buying groceries with a $1000\\text{ shilling}$ note: If the cashier hands you $200\\text{ shillings}$ in change, you know you spent $800\\text{ shillings}$ ($1000 - 200$) on the groceries!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: Back Titration Calculation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "$0.030\\text{ moles}$ of $\\text{HCl}$ was added to an impure magnesium sample. The unreacted acid required $0.010\\text{ moles}$ of $\\text{NaOH}$ for neutralization. How many moles of $\\text{Mg}$ were present in the sample?\n$$\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2$$",
                        "options": [
                            "$0.020\\text{ mol}$",
                            "$0.010\\text{ mol}$",
                            "$0.005\\text{ mol}$",
                            "$0.030\\text{ mol}$"
                        ],
                        "answer": "B",
                        "explanation": "Moles of $\\text{HCl}$ reacted $= 0.030 - 0.010 = 0.020\\text{ mol}$. From the equation mole ratio ($1\\text{ Mg} : 2\\text{ HCl}$), moles of $\\text{Mg} = \\frac{0.020}{2} = 0.010\\text{ mol}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Back Titrations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Back Titrations\n- **Purpose**: Analyzing insoluble, volatile, or slow-reacting solids.\n- **Method**: Dissolve solid in known excess acid $\\rightarrow$ Titrate leftover acid with standard base.\n- **Master Equation**: $\\text{Moles Reacted} = \\text{Total Moles Added} - \\text{Moles Leftover}$."
                    }
                }
            ]
        },

        # =========================================================================
        # LESSON 172: GAS STOICHIOMETRY AND REDOX TITRATIONS
        # =========================================================================
        172: {
            "topic": topic_23,
            "title": "Gas Stoichiometry and Redox Titrations",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Electron Transfer in Solution",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand volumetric analysis based on redox reactions, perform Potassium Manganate(VII) titrations with iron(II) and ethanedioate ions, and calculate concentrations using redox mole ratios ($1:5$ and $2:5$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Color Changes in Redox Reactions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In acid-base titrations, we had to add an external indicator (like phenolphthalein) because acids and bases are colorless.\n\nIn **Redox Titrations**, many transition metal oxidizing agents act as **self-indicating reagents**. The most famous of these is **Potassium Manganate(VII) ($\\text{KMnO}_4$)**, whose intense purple solution turns completely colorless as $\\text{Mn}^{7+}$ ions are reduced to $\\text{Mn}^{2+}$!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Chemistry of Potassium Manganate(VII) Titrations",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In acidic solution, the deep purple manganate(VII) ion ($\\text{MnO}_4^-$) is a powerful oxidizing agent:\n\n* **Reduction Half-Equation (Burette Solution)**:\n  $$\\text{MnO}_{4(aq)}^- + 8\\text{H}^+_{(aq)} + 5e^- \\rightarrow \\text{Mn}^{2+}_{(aq)} + 4\\text{H}_2\\text{O}_{(l)} \\quad (\\text{Purple} \\rightarrow \\text{Colorless})$$\n\n* **Oxidation Half-Equation (Conical Flask: Iron(II) ions)**:\n  $$\\text{Fe}^{2+}_{(aq)} \\rightarrow \\text{Fe}^{3+}_{(aq)} + e^- \\quad (\\text{Pale Green} \\rightarrow \\text{Yellow})$$\n\n* **Overall Balanced Ionic Equation** (multiply iron equation by 5):\n  $$\\mathbf{\\text{MnO}_{4(aq)}^- + 8\\text{H}^+_{(aq)} + 5\\text{Fe}^{2+}_{(aq)} \\rightarrow \\text{Mn}^{2+}_{(aq)} + 5\\text{Fe}^{3+}_{(aq)} + 4\\text{H}_2\\text{O}_{(l)}}$$\n  *Mole Ratio*: **$1\\text{ mole of } \\text{MnO}_4^- : 5\\text{ moles of } \\text{Fe}^{2+}$**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Potassium Manganate(VII) Redox Titration",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram of a redox titration showing deep purple KMnO4 solution in burette dispensing into conical flask containing pale green Fe2+ acidified with dilute H2SO4. A zoom-in shows the sharp end-point where one drop of excess KMnO4 imparts a permanent faint pink tint.",
                        "caption": "KMnO4 Redox Titration: Self-indicating end-point occurs when a single drop of unreacted KMnO4 turns the solution permanent faint pink."
                    },
                    "asset_info": {
                        "title": "Redox Titration Color Progression",
                        "description": "Volumetric redox titration apparatus showing purple KMnO4 burette and permanent faint pink end-point.",
                        "ai_instruction": "Create a laboratory diagram showing purple KMnO4 in burette and conical flask turning from colorless to permanent faint pink at end-point."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Principles of Redox Volumetric Analysis",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Redox Titrations",
                        "content": "### Key Operational Rules:\n1. **Self-Indicating End-Point**: No indicator is needed! The end-point is reached when one drop of excess $\\text{KMnO}_4$ imparts a **permanent faint pink color** to the solution.\n2. **Burette Reading Protocol**: Because $\\text{KMnO}_4$ is intensely dark purple, the bottom of the meniscus cannot be seen. Burettes are always read from the **top of the meniscus**.\n3. **Acidification**: The conical flask must be acidified with **dilute sulfuric acid ($\\text{H}_2\\text{SO}_4$)**."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Standardising Potassium Manganate(VII)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$25.0\\text{ cm}^3$ of $0.10\\text{ M}$ ammonium iron(II) sulfate solution (containing $\\text{Fe}^{2+}$) was acidified with dilute sulfuric acid and titrated against potassium manganate(VII) ($\\text{KMnO}_4$) solution. Exactly $20.0\\text{ cm}^3$ of the purple $\\text{KMnO}_4$ solution was required for complete oxidation to the faint pink end-point. Calculate the molarity of the $\\text{KMnO}_4$ solution.",
                        "steps": [
                            "**1. What do we know? (Given Data)**\n- $\\text{Fe}^{2+}$ solution: $M_{\\text{Fe}} = 0.10\\text{ M}, V_{\\text{Fe}} = 25.0\\text{ cm}^3$\n- $\\text{KMnO}_4$ solution: $V_{\\text{Mn}} = 20.0\\text{ cm}^3, M_{\\text{Mn}} = \\text{Target Molarity}$",
                            "**2. Step 1: Calculate Moles of $\\text{Fe}^{2+}$ Used**\n$$n(\\text{Fe}^{2+}) = \\frac{M \\times V}{1000} = \\frac{0.10\\text{ M} \\times 25.0\\text{ cm}^3}{1000} = 0.0025\\text{ moles}$$",
                            "**3. Step 2: Use Stoichiometric Redox Mole Ratio ($1 : 5$)**\n$$\\text{MnO}_4^- + 8\\text{H}^+ + 5\\text{Fe}^{2+} \\rightarrow \\text{Mn}^{2+} + 5\\text{Fe}^{3+} + 4\\text{H}_2\\text{O}$$\n$$n(\\text{MnO}_4^-) = \\frac{n(\\text{Fe}^{2+})}{5} = \\frac{0.0025\\text{ mol}}{5} = 0.00050\\text{ moles}$$",
                            "**4. Step 3: Calculate Molarity of $\\text{KMnO}_4$**\n$$M_{\\text{Mn}} = \\frac{n \\times 1000}{V(\\text{cm}^3)} = \\frac{0.00050\\text{ mol} \\times 1000}{20.0\\text{ cm}^3} = 0.025\\text{ mol/dm}^3\\text{ (or } 0.025\\text{ M)}$$",
                            "**5. Result & Conclusion**\n- The standardized potassium manganate(VII) solution has a concentration of $0.025\\text{ M}$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why We Only Acidify With Sulphuric Acid",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why can we NOT acidify $\\text{KMnO}_4$ titrations with Hydrochloric Acid ($\\text{HCl}$) or Nitric Acid ($\\text{HNO}_3$)?\n1. **Why not $\\text{HCl}$?** $\\text{KMnO}_4$ is so powerful that it would oxidize chloride ions ($\\text{Cl}^-$) in hydrochloric acid to toxic chlorine gas ($\\text{Cl}_2$), consuming extra $\\text{KMnO}_4$ and giving an artificially high titre!\n2. **Why not $\\text{HNO}_3$?** Nitric acid is itself a strong oxidizing agent that would compete with $\\text{KMnO}_4$ by oxidizing the $\\text{Fe}^{2+}$ ions, giving an artificially low titre!\n3. **Why $\\text{H}_2\\text{SO}_4$?** Dilute sulfuric acid contains sulfate ions ($\\text{SO}_4^{2-}$) in their highest oxidation state ($+6$), which are completely stable and inert toward redox side-reactions."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question: KMnO4 and Fe(II) Mole Ratio",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "In an acidified redox titration between potassium manganate(VII) ($\\text{KMnO}_4$) and iron(II) sulfate ($\\text{FeSO}_4$), what is the stoichiometric mole ratio of $\\text{MnO}_4^-$ to $\\text{Fe}^{2+}$?",
                        "options": [
                            "$1 : 1$",
                            "$1 : 2$",
                            "$1 : 5$",
                            "$2 : 5$"
                        ],
                        "answer": "C",
                        "explanation": "Because one $\\text{MnO}_4^-$ ion accepts $5$ electrons ($\text{Mn}^{7+} \\rightarrow \\text{Mn}^{2+}$) and each $\\text{Fe}^{2+}$ ion donates $1$ electron ($\text{Fe}^{2+} \\rightarrow \\text{Fe}^{3+}$), exactly $5\\text{ moles of } \\text{Fe}^{2+}$ are required to reduce $1\\text{ mole of } \\text{MnO}_4^-$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Redox Titrations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Redox Titrations\n- **Self-Indicating**: $\\text{KMnO}_4$ turns from deep purple to permanent faint pink at end-point.\n- **Acidification**: Acidify exclusively with dilute $\\text{H}_2\\text{SO}_4$ (never $\\text{HCl}$ or $\\text{HNO}_3$).\n- **Stoichiometry**: $\\text{MnO}_4^- : \\text{Fe}^{2+} = 1 : 5$; $\\text{MnO}_4^- : \\text{C}_2\\text{O}_4^{2-} = 2 : 5$."
                    }
                }
            ]
        }
    }

    for lesson_id, data in lessons_data.items():
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            print(f"Updating Lesson {lesson.id}: \"{lesson.title}\" in {data['topic'].name}...")
            
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
            print(f"  Successfully refactored Lesson {lesson.id} with {len(data['cards'])} cards.")
        except Lesson.DoesNotExist:
            print(f"Lesson ID {lesson_id} not found in database!")

if __name__ == "__main__":
    run_refactor_topic_23()
