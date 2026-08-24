import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def ingest_form3_topic2_mole():
    print("================================================================================")
    print("Starting VLearn Form 3 Chemistry Batch 2 Ingestion: The Mole (Modules 2.1 - 2.9)")
    print("================================================================================")

    # 1. Setup Curriculum Hierarchy
    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(name="844", description="Kenyan 8-4-4 Secondary Curriculum")

    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Form 3",
        defaults={"level": 3, "description": "Form 3 Secondary Level"}
    )

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Chemistry",
        defaults={"description": "Form 3 Chemistry (Secondary Chemistry Curriculum)"}
    )

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 2: The Mole: Formulae and Chemical Equations",
        defaults={
            "description": "Comprehensive study of relative masses, the mole concept, empirical & molecular formulae, molar solutions, dilution, reaction stoichiometry, volumetric analysis, back titrations, and redox titrations.",
            "order": 2
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name} (Grade: {grade.name})")

    # 2. Define Natural, Student-Facing Content Data Dictionary (Modules 2.1 - 2.9)
    modules_data = [
        {
            "unit_name": "Module 2.1: Relative Atomic, Molecular, and Formula Masses",
            "unit_order": 1,
            "lesson_title": "Relative Atomic, Molecular, and Formula Masses",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Understanding Relative Mass",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore the Carbon-12 standard of atomic mass, distinguish between Relative Atomic Mass ($A_r$), Relative Molecular Mass ($M_r$), and Formula Mass (R.F.M.), and calculate relative masses for covalent and ionic compounds."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Counting by Weighing",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine walking into a busy open-air market in **Thika, Eldoret, or Kisumu**. Traders sell heaps of fruits: bananas, oranges, and mangoes. If a customer wants 12 oranges, the trader counts them out one by one. But if a local juice factory buys 100,000 oranges, counting them individually would take days! Instead, the trader uses a clever shortcut: **counting by weighing**.\n\nIn Chemistry, atoms are so unimaginably tiny that a single hydrogen atom weighs about $1.67 \\times 10^{-24}\\text{ g}$. We cannot see or count individual atoms for a reaction. Therefore, chemists count atoms and molecules by weighing them against a universal standard of comparison: the **Scale of Relative Masses**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Carbon-12 Standard",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's connect our laboratory balances with the atomic world:\n\n* **Macroscopic Observation**:\n  We can weigh $0.24\\text{ g}$ of shiny magnesium ribbon or $0.32\\text{ g}$ of yellow sulphur powder on a balance. These masses are easily measured, but the numbers alone do not reveal how many atoms are present in each sample.\n\n* **Microscopic Reality**:\n  An atom of sulphur is heavier than an atom of magnesium, which is heavier than an atom of hydrogen. Because individual atomic masses are minuscule, we select one specific atom as a standard and compare all other atomic masses against it.\n\n* **Symbolic Representation**:\n  The international standard chosen by IUPAC is the **Carbon-12 isotope ($^{12}\\text{C}$)**, assigned an exact mass of $12.000\\text{ atomic mass units (a.m.u.)}$:\n  $$1\\text{ a.m.u.} = \\frac{1}{12}\\text{th of the mass of one atom of Carbon-12}$$\n  If a Magnesium atom is twice as heavy as a Carbon-12 atom, its relative atomic mass is $24$."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Equal-Arm Balance Model of Atomic Mass",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Conceptual balance scale comparing one Magnesium atom with 24 units of 1/12th Carbon-12.",
                        "instruction": "An equal-arm balance scale. Left pan: 1 single atom of Magnesium. Right pan: 24 identical unit blocks, each representing 1/12th of a Carbon-12 atom (1 a.m.u.). The pans balance perfectly, visually proving why Magnesium has a relative atomic mass of 24 without gram units.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    },
                    "asset_info": {
                        "title": "Atomic Mass Comparison Model",
                        "description": "Visual balance scale illustrating relative atomic mass against Carbon-12 standard.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Defining Relative Masses: Ar, Mr, and R.F.M.",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Relative Masses in Chemistry",
                        "content": "### 1. Relative Atomic Mass ($A_r$)\nThe average mass of one atom of an element compared to $\\frac{1}{12}\\text{th}$ of the mass of an atom of Carbon-12.\n$$A_r = \\frac{\\text{Average mass of one atom of the element}}{\\frac{1}{12} \\times \\text{mass of one atom of Carbon-12}}$$\n*Note*: Because $A_r$ is a ratio of two masses, the units cancel out. $A_r$ is a **dimensionless number**.\n\n### 2. Relative Molecular Mass ($M_r$)\nApplies to **covalent substances** existing as discrete molecules (e.g. $\\text{H}_2\\text{O}, \\text{CO}_2$). Calculated by summing the $A_r$ values of all atoms in the molecular formula.\n\n### 3. Relative Formula Mass (R.F.M.)\nApplies to **ionic compounds** (e.g. $\\text{NaCl}, \\text{CaCl}_2$) that form giant three-dimensional crystalline lattices rather than separate molecules. Calculated from the simplest formula unit."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Industrial Applications in Kenya",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Quality Control and Water Treatment\nAnalytical chemists at the **Kenya Bureau of Standards (KEBS)** and industrial plants such as Kel Chemicals in Thika calculate relative formula masses to formulate exact batches of fertilisers, food additives, and industrial acids.\n\nFor example, to manufacture high-purity **aluminium sulphate** (used in municipal water treatment at the **Ruiru and Ndakaini water works**), chemical engineers use relative formula masses of raw bauxite and sulphuric acid to ensure complete conversion with no hazardous residue."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Calculating Molecular and Formula Masses",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the Relative Molecular Mass of Carbon(IV) oxide ($\\text{CO}_2$) and the Relative Formula Mass of Ammonium sulphate ($(\\text{NH}_4)_2\\text{SO}_4$).\n($A_r$: $\\text{C}=12.0, \\text{O}=16.0, \\text{N}=14.0, \\text{H}=1.0, \\text{S}=32.0$)",
                        "steps": [
                            "**Calculation 1: Carbon(IV) oxide ($\\text{CO}_2$)**:\n$$M_r = (1 \\times A_r(\\text{C})) + (2 \\times A_r(\\text{O})) = (1 \\times 12.0) + (2 \\times 16.0) = 12.0 + 32.0 = 44.0$$\n*Meaning*: One molecule of $\\text{CO}_2$ is 44 times heavier than $\\frac{1}{12}\\text{th}$ of a Carbon-12 atom.",
                            "**Calculation 2: Ammonium sulphate ($(\\text{NH}_4)_2\\text{SO}_4$)**:\n$$\\text{R.F.M.} = 2 \\times [A_r(\\text{N}) + 4(A_r(\\text{H}))] + A_r(\\text{S}) + 4(A_r(\\text{O}))$$\n$$\\text{R.F.M.} = 2 \\times [14.0 + 4(1.0)] + 32.0 + 4(16.0) = 2(18.0) + 32.0 + 64.0 = 36.0 + 32.0 + 64.0 = 132.0$$\n*Meaning*: The formula unit mass is 132.0 (dimensionless, no units)."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why Relative Masses Have No Units",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why do we not write \"grams\" after relative mass values?\nIn everyday life, weighing something produces a unit like grams or kilograms. However, Relative Atomic Mass and Relative Molecular Mass are **pure ratios** comparing the mass of one atom or molecule against the mass of another standard atom ($^{12}\\text{C}$).\n\nBecause the comparison divides mass by mass ($\\text{grams} / \\text{grams}$), the units cancel out completely. Relative masses are always dimensionless numbers!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Relative Masses",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Calculate the Relative Formula Mass of hydrated copper(II) sulphate, $\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}$. ($A_r$: $\\text{Cu} = 63.5, \\text{S} = 32.0, \\text{O} = 16.0, \\text{H} = 1.0$)",
                        "options": [
                            "159.5",
                            "177.5",
                            "249.5",
                            "184.5"
                        ],
                        "answer": "C",
                        "explanation": "To calculate the R.F.M. of a hydrated salt, add the mass of water of crystallisation: $\\text{R.F.M.} = 63.5 + 32.0 + 4(16.0) + 5[2(1.0) + 16.0] = 159.5 + 5(18.0) = 159.5 + 90.0 = 249.5$. Option A (159.5) only accounts for anhydrous copper sulphate, omitting the five water molecules."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Relative Masses",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Relative Masses\n- **Standard**: Carbon-12 ($^{12}\\text{C}$) is assigned a mass of exactly $12.000\\text{ a.m.u.}$\n- **Relative Atomic Mass ($A_r$)**: Average atom mass compared to $\\frac{1}{12}\\text{th}$ Carbon-12 mass.\n- **Relative Molecular Mass ($M_r$)**: Sum of $A_r$ values for covalent molecules.\n- **Relative Formula Mass (R.F.M.)**: Sum of $A_r$ values for ionic giant crystal lattices.\n- **Dimensionless**: Relative masses have no units."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.2: The Mole Concept and Avogadro's Constant",
            "unit_order": 2,
            "lesson_title": "The Mole Concept and Avogadro's Constant",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemist's Counting Unit",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master the chemist's counting unit—the Mole—using Avogadro's constant ($L = 6.02 \\times 10^{23}\\text{ particles mol}^{-1}$), and convert smoothly between mass, moles, and particle counts."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Counting Billions of Invisible Atoms",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When buying ping-pong balls for a school tournament, wholesalers sell them in convenient counting units like a **dozen** (12) or a **gross** (144).\n\nIn Chemistry, particles are so small that even a single refreshing sip of water (about $18\\text{ mL}$) contains approximately **602,000,000,000,000,000,000,000** molecules! Counting them one by one at a rate of one per second would take over 19 quadrillion years—longer than the age of the universe.\n\nTo solve this, chemists use a giant, standardized counting unit: **The Mole**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Bridging Microscopic Atoms and Lab Balances",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "How does this massive number connect to laboratory measurements?\n\n* **Macroscopic Observation**:\n  Weighing out $12.0\\text{ g}$ of Carbon-12 powder, $23.0\\text{ g}$ of Sodium metal, or $56.0\\text{ g}$ of Iron filings produces piles of visibly different volumes and textures.\n\n* **Microscopic Particle Reality**:\n  Because the mass of each atom is proportional to its relative atomic mass, each of these weighed samples contains **exactly the same number of individual atoms**!\n\n* **Symbolic Representation**:\n  This universal count is **Avogadro's Constant ($L$ or $N_A$)**:\n  $$L = 6.02 \\times 10^{23}\\text{ particles mol}^{-1}$$\n  One mole of any element or compound contains exactly $6.02 \\times 10^{23}$ elementary particles."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Mole, Molar Mass, and Key Formulae",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Mole & Molar Mass",
                        "content": "### Definition of the Mole\nThe amount of substance containing as many elementary entities (atoms, molecules, ions, or electrons) as there are atoms in exactly $12.000\\text{ g}$ of the Carbon-12 isotope ($6.02 \\times 10^{23}$ particles).\n\n### Molar Mass ($M$)\nThe mass of one mole of a substance, expressed in grams per mole ($\\text{g mol}^{-1}$ or $\\text{g/mol}$).\n* Numerical Rule: $\\text{Molar Mass } (M) = \\text{Relative Formula Mass (R.F.M.)}$\n  - Molar Mass of Carbon = $12.0\\text{ g mol}^{-1}$\n  - Molar Mass of $\\text{CO}_2$ = $44.0\\text{ g mol}^{-1}$\n\n### Fundamental Molar Formulae:\n$$\\text{Number of Moles } (n) = \\frac{\\text{Mass in grams } (m)}{\\text{Molar Mass } (M)}$$\n$$\\text{Number of Particles} = \\text{Number of Moles } (n) \\times \\text{Avogadro's Constant } (L)$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Industrial Applications of Moles",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Chemical Manufacturing & Lime Processing\nThe mole concept is the foundation of all chemical production. When pharmaceutical manufacturers in Nairobi formulate medicines, or when the **Homa Lime Company in Koru** processes limestone ($\\text{CaCO}_3$) into quicklime ($\\text{CaO}$), engineers calculate molar ratios to ensure reactants combine completely without leaving expensive or hazardous unreacted material."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Mass and Particle Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. How many moles are present in $10.6\\text{ g}$ of sodium carbonate ($\\text{Na}_2\\text{CO}_3$)?\n2. Calculate the number of copper atoms in a pure $3.175\\text{ g}$ copper coin.\n($A_r$: $\\text{Na}=23.0, \\text{C}=12.0, \\text{O}=16.0, \\text{Cu}=63.5$; $L = 6.02 \\times 10^{23}\\text{ atoms mol}^{-1}$)",
                        "steps": [
                            "**Problem 1 (Moles of $\\text{Na}_2\\text{CO}_3$)**:\n- Molar Mass $M = 2(23.0) + 12.0 + 3(16.0) = 46.0 + 12.0 + 48.0 = 106.0\\text{ g mol}^{-1}$\n- Moles $n = \\frac{m}{M} = \\frac{10.6\\text{ g}}{106.0\\text{ g mol}^{-1}} = 0.1\\text{ moles}$",
                            "**Problem 2 (Number of Copper Atoms)**:\n- Step 1: Calculate moles $n = \\frac{3.175\\text{ g}}{63.5\\text{ g mol}^{-1}} = 0.05\\text{ moles}$\n- Step 2: Calculate atoms $= n \\times L = 0.05\\text{ mol} \\times 6.02 \\times 10^{23}\\text{ atoms mol}^{-1} = 3.01 \\times 10^{22}\\text{ atoms}$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Quantity vs Mass",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does 1 mole of helium weigh the same as 1 mole of carbon?\nNo! While both contain exactly the same number of particles ($6.02 \\times 10^{23}$ atoms), their masses are very different.\n\nJust as 1 dozen chicken eggs has the same count as 1 dozen watermelons but a vastly smaller mass, 1 mole of helium weighs $4.0\\text{ g}$ while 1 mole of carbon weighs $12.0\\text{ g}$. Moles measure particle count, not mass!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: The Mole Concept",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "How many total oxygen atoms are present in $0.5\\text{ moles}$ of carbon(IV) oxide ($\\text{CO}_2$)? ($L = 6.02 \\times 10^{23}\\text{ particles mol}^{-1}$)",
                        "options": [
                            "$3.01 \\times 10^{23}$",
                            "$6.02 \\times 10^{23}$",
                            "$1.204 \\times 10^{24}$",
                            "$1.505 \\times 10^{23}$"
                        ],
                        "answer": "B",
                        "explanation": "Each molecule of $\\text{CO}_2$ contains 2 oxygen atoms. Therefore, $0.5\\text{ moles}$ of $\\text{CO}_2$ contains $0.5 \\times 2 = 1.0\\text{ mole}$ of oxygen atoms. Atoms of oxygen $= 1.0\\text{ mol} \\times 6.02 \\times 10^{23} = 6.02 \\times 10^{23}\\text{ atoms}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: The Mole Concept",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: The Mole\n- **Mole Definition**: Amount containing $6.02 \\times 10^{23}$ elementary particles ($L$).\n- **Molar Mass ($M$)**: Mass in $\\text{g mol}^{-1}$, numerically equal to relative formula mass.\n- **Converting Formulae**: $n = \\frac{m}{M}$ and $\\text{Particles} = n \\times L$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.3: Calculation of Empirical and Molecular Formulae",
            "unit_order": 3,
            "lesson_title": "Calculation of Empirical and Molecular Formulae",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Chemical Detective Work",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will determine empirical and molecular formulae from experimental percentage composition and reaction data, using mole ratios to reveal the simplest and actual chemical structures of compounds."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Identifying Unknown Chemical Substances",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine investigating an unknown white powder. A forensic elemental analysis reveals it contains **40.0% Carbon, 6.7% Hydrogen, and 53.3% Oxygen** by mass. But what is the actual compound? Is it toxic formaldehyde, sweet glucose, or sour vinegar?\n\nTo solve this, we translate elemental percentage masses into simplest atomic ratios: the **Empirical Formula**. Combining this with the compound's overall molecular mass reveals its true identity: the **Molecular Formula**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Determination Methods",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In the laboratory, empirical formulae are determined using two classic experiments:\n\n* **1. Oxidation of Magnesium in a Crucible**:\n  Burning clean magnesium ribbon in air produces white magnesium oxide powder ($\\text{MgO}$). The mass increases as magnesium atoms bind with atmospheric oxygen.\n\n* **2. Reduction of Copper(II) Oxide by Hydrogen**:\n  Passing dry hydrogen gas over heated black copper(II) oxide strips oxygen away, leaving reddish-brown solid copper metal ($\\text{CuO} + \\text{H}_2 \\rightarrow \\text{Cu} + \\text{H}_2\\text{O}$).\n\nBy measuring starting and final masses, dividing by relative atomic masses ($A_r$), and simplifying to integers, we deduce the empirical formula."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Reduction of Copper(II) Oxide Setup",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Apparatus setup for determining empirical formula of copper oxide via hydrogen reduction.",
                        "instruction": "Horizontal hard-glass combustion tube clamped over Bunsen burner. Ceramic boat inside containing copper oxide transitioning from black to reddish copper. Left inlet delivering dry hydrogen gas; right jet safely burning excess hydrogen.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    },
                    "asset_info": {
                        "title": "Copper Oxide Reduction Apparatus",
                        "description": "Apparatus setup for empirical formula determination via gas reduction.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Empirical vs Molecular Formulae",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Chemical Formula Types",
                        "content": "### Empirical Formula\nThe simplest formula showing the lowest whole-number ratio of atoms of the different elements present in a compound.\n\n### Molecular Formula\nThe formula showing the actual number of each kind of atom present in one molecule of a compound.\n\n### Mathematical Relationship:\n$$\\text{Molecular Formula} = (\\text{Empirical Formula})_n$$\n$$n = \\frac{\\text{Relative Molecular Mass of Compound}}{\\text{Empirical Formula Mass}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Mineral Exploration and Mining in Kenya",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Ore Purity Analysis in West Pokot and Kwale\nWhen mining corporations analyze copper deposits in **West Pokot** or titanium-bearing rutile/ilmenite in **Kwale County**, geochemists perform combustion and reduction assays to verify the exact empirical formulas and purity percentages of metal oxides before industrial smelting."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Determining Empirical and Molecular Formulae",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. Burning $0.84\\text{ g}$ of magnesium ribbon yields $1.40\\text{ g}$ of magnesium oxide. Find its empirical formula ($A_r$: $\\text{Mg}=24.0, \\text{O}=16.0$).\n2. An organic compound has $57.15\\%\\text{ C}$, $4.76\\%\\text{ H}$, and $38.09\\%\\text{ O}$, with $M_r = 126.0$. Find its molecular formula.",
                        "steps": [
                            "**Problem 1 (Magnesium Oxide)**:\n- Reacting Oxygen mass $= 1.40\\text{ g} - 0.84\\text{ g} = 0.56\\text{ g}$\n- Moles of $\\text{Mg} = \\frac{0.84}{24.0} = 0.035$; Moles of $\\text{O} = \\frac{0.56}{16.0} = 0.035$\n- Ratio $= 0.035 : 0.035 = 1 : 1 \\implies \\text{Empirical Formula: } \\text{MgO}$",
                            "**Problem 2 (Molecular Formula)**:\n- Moles in $100\\text{ g}$: $\\text{C} = \\frac{57.15}{12.0} = 4.76$, $\\text{H} = \\frac{4.76}{1.0} = 4.76$, $\\text{O} = \\frac{38.09}{16.0} = 2.38$\n- Divide by smallest ($2.38$): $\\text{C}=2, \\text{H}=2, \\text{O}=1 \\implies \\text{Empirical Formula: } \\text{C}_2\\text{H}_2\\text{O}$\n- Empirical Mass $= 2(12.0) + 2(1.0) + 16.0 = 42.0$\n- Multiplier $n = \\frac{126.0}{42.0} = 3 \\implies \\text{Molecular Formula: } (\\text{C}_2\\text{H}_2\\text{O})_3 = \\text{C}_6\\text{H}_6\\text{O}_3$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: The Crucible Lid Technique",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why do we lift the crucible lid briefly during magnesium combustion?\nMagnesium burns with a brilliant white flame, producing dense white smoke of $\\text{MgO}$ particles. If the lid is removed completely, the smoke escapes, leading to an artificially low measured product mass and incorrect mole ratios.\n\nBy keeping the lid on and lifting it for just a fraction of a second at intervals, we allow oxygen to enter while trapping all product smoke safely inside."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Chemical Formulae",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A gaseous hydrocarbon has an empirical formula of $\\text{CH}_2$ and a relative molecular mass of $28.0$. What is its molecular formula? ($A_r$: $\\text{C}=12.0, \\text{H}=1.0$)",
                        "options": [
                            "$\\text{CH}_2$",
                            "$\\text{C}_2\\text{H}_4$",
                            "$\\text{C}_3\\text{H}_6$",
                            "$\\text{C}_4\\text{H}_8$"
                        ],
                        "answer": "B",
                        "explanation": "Empirical formula mass of $\\text{CH}_2 = 12.0 + 2(1.0) = 14.0$. Multiplier $n = \\frac{28.0}{14.0} = 2$. Therefore, Molecular Formula $= (\\text{CH}_2)_2 = \\text{C}_2\\text{H}_4$ (ethene gas)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Formula Calculations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Empirical & Molecular Formulae\n- **Empirical Formula**: Simplest whole-number mole ratio of atoms in a compound.\n- **Molecular Formula**: Exact count of atoms in a single molecule ($(\\text{Empirical Formula})_n$).\n- **Method**: Convert mass/percentage to moles, divide by smallest mole value, multiply by $n = M_r / \\text{Empirical Mass}$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.4: Concentration of Solutions and Molar Solutions",
            "unit_order": 4,
            "lesson_title": "Concentration of Solutions and Molar Solutions",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Measuring Solution Strength",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore the concentration of solutions, master molarity (moles per litre), convert between mass concentration ($\\text{g dm}^{-3}$) and molar concentration ($\\text{mol dm}^{-3}$), and describe standard solution preparation."
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
                    "page_number": 3,
                    "page_title": "Molar Solutions & Concentration Formulae",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Concentration & Molarity",
                        "content": "### Molar Solution (1.0 M)\nA solution containing exactly one mole of solute dissolved and made up to exactly one litre ($1000\\text{ cm}^3$) of solution.\n\n### Key Formulas:\n$$\\text{Concentration } (\\text{g/dm}^3) = \\frac{\\text{Mass of solute in grams } (m)}{\\text{Volume in dm}^3 (V)}$$\n$$\\text{Molarity } (\\text{mol/dm}^3) = \\frac{\\text{Moles of solute } (n)}{\\text{Volume in dm}^3 (V)}$$\n$$\\text{Concentration } (\\text{g/dm}^3) = \\text{Molarity } (\\text{mol/dm}^3) \\times \\text{Molar Mass } (M_m)$$\n$$\\text{Number of Moles } (n) = \\frac{\\text{Molarity } (M) \\times \\text{Volume in cm}^3 (V)}{1000}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Preparing a Standard Solution in the Laboratory",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Step-by-Step Preparation of $1.0\\text{ M } \\text{NaOH}$\n1. **Weigh Solute**: Calculate molar mass of $\\text{NaOH}$ ($40.0\\text{ g/mol}$) and weigh exactly $40.0\\text{ g}$ on a balance.\n2. **Initial Dissolution**: Dissolve pellets in $\\approx 200\\text{ cm}^3$ of distilled water in a beaker, stirring with a glass rod.\n3. **Quantitative Transfer**: Pour into a $1\\text{ Litre}$ volumetric flask; rinse the beaker and rod with distilled water and add washings into the flask.\n4. **Fill to Mark**: Add distilled water slowly until the bottom of the meniscus aligns with the calibration line.\n5. **Homogenize**: Stopper and invert several times for uniform concentration."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Concentration & Molarity Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. If $4.0\\text{ g}$ of $\\text{NaOH}$ is dissolved to make $500\\text{ cm}^3$ of solution, find concentration in $\\text{g/dm}^3$ and Molarity ($A_r$: $\\text{Na}=23, \\text{O}=16, \\text{H}=1$).\n2. Calculate mass of $\\text{CaCl}_2$ required to prepare $250\\text{ cm}^3$ of $0.2\\text{ M}$ solution ($A_r$: $\\text{Ca}=40.0, \\text{Cl}=35.5$).",
                        "steps": [
                            "**Problem 1 ($\\text{NaOH}$ Concentration)**:\n- Concentration $(\\text{g/dm}^3) = \\frac{4.0\\text{ g}}{0.5\\text{ dm}^3} = 8.0\\text{ g/dm}^3$\n- Moles of $\\text{NaOH} = \\frac{4.0\\text{ g}}{40.0\\text{ g/mol}} = 0.1\\text{ mol}$\n- Molarity $= \\frac{0.1\\text{ mol}}{0.5\\text{ dm}^3} = 0.2\\text{ mol/dm}^3\\text{ (or } 0.2\\text{ M)}$",
                            "**Problem 2 (Mass of $\\text{CaCl}_2$)**:\n- Molar mass of $\\text{CaCl}_2 = 40.0 + 2(35.5) = 111.0\\text{ g/mol}$\n- Moles needed $n = \\frac{M \\times V(\\text{cm}^3)}{1000} = \\frac{0.2 \\times 250}{1000} = 0.05\\text{ mol}$\n- Mass needed $m = n \\times M = 0.05\\text{ mol} \\times 111.0\\text{ g/mol} = 5.55\\text{ g}$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why Volumetric Flasks Have Narrow Necks",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why is a volumetric flask neck so long and narrow?\nIn a wide beaker, adding an extra drop of water causes an imperceptible height change. In a very narrow flask neck, however, even a single drop of water causes a noticeable, sharp rise in the liquid meniscus.\n\nThis narrow geometry makes it impossible to overshoot the calibration mark without noticing, ensuring high volumetric accuracy."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Molarity",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "If $5.3\\text{ g}$ of anhydrous sodium carbonate ($\\text{Na}_2\\text{CO}_3$) is dissolved to make $250\\text{ cm}^3$ of solution, what is the molarity? ($A_r$: $\\text{Na}=23.0, \\text{C}=12.0, \\text{O}=16.0$)",
                        "options": [
                            "$0.2\\text{ M}$",
                            "$0.05\\text{ M}$",
                            "$0.1\\text{ M}$",
                            "$0.5\\text{ M}$"
                        ],
                        "answer": "A",
                        "explanation": "Molar mass of $\\text{Na}_2\\text{CO}_3 = 2(23) + 12 + 3(16) = 106.0\\text{ g/mol}$. Moles dissolved $= 5.3 / 106.0 = 0.05\\text{ moles}$. Molarity $= \\frac{0.05 \\times 1000}{250} = 0.2\\text{ M}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Molar Solutions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Concentration & Molarity\n- **Molarity ($M$)**: Moles of solute per litre ($1000\\text{ cm}^3$) of solution.\n- **Link**: $\\text{Concentration } (\\text{g/dm}^3) = \\text{Molarity} \\times \\text{Molar Mass}$.\n- **Formula**: $n = \\frac{M \\times V(\\text{cm}^3)}{1000}$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.5: Dilution of Solutions",
            "unit_order": 5,
            "lesson_title": "Dilution of Solutions",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Principle of Dilution",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will understand how dilution alters solution concentration while keeping solute moles constant, and apply the dilution equation ($C_1V_1 = C_2V_2$) to laboratory and industrial preparations."
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
                        "text": "Let's examine dilution at macroscopic and particle levels:\n\n* **Macroscopic Observation**:\n  Pipetting $25\\text{ cm}^3$ of concentrated $2.0\\text{ M } \\text{HCl}$ into a $250\\text{ cm}^3$ volumetric flask and topping up with distilled water yields a much milder, safer acid solution.\n\n* **Microscopic Particle Model**:\n  The initial $25\\text{ cm}^3$ contains a fixed quantity of hydronium and chloride ions. Adding water inserts solvent molecules between ions, increasing their spacing without altering the total count of solute particles.\n\n* **Symbolic Representation**:\n  $$\\text{Moles of solute before dilution} = \\text{Moles of solute after dilution}$$\n  $$\\frac{C_1V_1}{1000} = \\frac{C_2V_2}{1000} \\quad \\implies \\quad C_1V_1 = C_2V_2$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Dilution Law & Volume Accounting",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Dilution Law",
                        "content": "$$C_1V_1 = C_2V_2$$\nWhere:\n- $C_1$ = Initial stock concentration\n- $V_1$ = Volume of stock solution used\n- $C_2$ = Target diluted concentration\n- $V_2$ = Total final volume ($V_2 = V_1 + \\text{Volume of water added}$)\n\n*Rule*: The units of volume must be identical on both sides of the equation."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Stock Solutions in Chemistry Laboratories",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Preparing Practical Exam Solutions\nIn school and university laboratories across Kenya, laboratory technologists purchase commercial concentrated acids ($18\\text{ M } \\text{H}_2\\text{SO}_4$ or $12\\text{ M } \\text{HCl}$) and perform precise dilutions to prepare $1.0\\text{ M}$ or $2.0\\text{ M}$ solutions for secondary students during national KCSE practical examinations."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Dilution Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. A student dilutes $25\\text{ cm}^3$ of $2.0\\text{ M } \\text{HCl}$ to a final volume of $250\\text{ cm}^3$. Find the new concentration.\n2. What volume of $2.0\\text{ M } \\text{NaOH}$ stock is required to prepare $250\\text{ cm}^3$ of $0.8\\text{ M } \\text{NaOH}$?",
                        "steps": [
                            "**Problem 1 (Diluted Concentration)**:\n- $C_1 = 2.0\\text{ M}, V_1 = 25\\text{ cm}^3, V_2 = 250\\text{ cm}^3$\n- $C_2 = \\frac{C_1 \\times V_1}{V_2} = \\frac{2.0 \\times 25}{250} = 0.2\\text{ M}$",
                            "**Problem 2 (Stock Volume Needed)**:\n- $C_1 = 2.0\\text{ M}, C_2 = 0.8\\text{ M}, V_2 = 250\\text{ cm}^3$\n- $V_1 = \\frac{C_2 \\times V_2}{C_1} = \\frac{0.8 \\times 250}{2.0} = 100\\text{ cm}^3$\n- *Interpretation*: Pipette $100\\text{ cm}^3$ of stock and add $150\\text{ cm}^3$ of distilled water ($250 - 100$) to reach the mark."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: The Acid Dilution Safety Rule",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why must you always add acid to water, never water to acid?\nDiluting concentrated sulphuric acid is strongly **exothermic** (releasing massive heat). If water is poured into concentrated acid, the first droplet boils violently on contact, causing concentrated acid to spit and splash onto your face and hands.\n\nBy adding acid slowly down the side of a beaker into a large volume of water while stirring, the water absorbs and disperses the heat safely."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Dilution",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of distilled water must be added to $100\\text{ cm}^3$ of a $3.0\\text{ M } \\text{HCl}$ solution to make its concentration exactly $1.0\\text{ M}$?",
                        "options": [
                            "$300\\text{ cm}^3$",
                            "$100\\text{ cm}^3$",
                            "$200\\text{ cm}^3$",
                            "$150\\text{ cm}^3$"
                        ],
                        "answer": "C",
                        "explanation": "Target final volume $V_2 = \\frac{C_1 \\times V_1}{C_2} = \\frac{3.0 \\times 100}{1.0} = 300\\text{ cm}^3$. Volume of water to add $= V_2 - V_1 = 300\\text{ cm}^3 - 100\\text{ cm}^3 = 200\\text{ cm}^3$. Option A (300 cm3) is the total final volume, not the added water."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Dilution",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Dilution\n- **Governing Law**: $C_1V_1 = C_2V_2$ (solute moles remain constant).\n- **Final Volume**: $V_2 = V_1 + V_{\\text{water added}}$.\n- **Safety Protocol**: Always add concentrated acid slowly to water with continuous stirring."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.6: Stoichiometry of Chemical Equations (Reacting Masses and Volumes)",
            "unit_order": 6,
            "lesson_title": "Stoichiometry of Chemical Equations (Reacting Masses and Volumes)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Chemical Recipes & Stoichiometry",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master chemical stoichiometry, relate balanced equation mole ratios to reacting masses and gas volumes, and apply molar gas volumes at s.t.p. ($22.4\\text{ dm}^3$) and r.t.p. ($24.0\\text{ dm}^3$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Exact Recipes of Nature",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When baking mandazis or chapatis, you follow a fixed recipe: 2 cups of flour for every 1 cup of water. Adding too much flour leaves dry crumbs; adding too much water makes sticky soup.\n\nChemical reactions follow exact mathematical recipes. Atoms combine in precise integer ratios. This quantitative study of reacting proportions in balanced equations is called **Stoichiometry**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Reacting Atoms & Balanced Equations",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's examine reacting proportions in the lab:\n\n* **Macroscopic Observation**:\n  Dropping grey zinc into dilute hydrochloric acid produces vigorous bubbling (effervescence), dissolving the zinc and evolving flammable hydrogen gas.\n\n* **Microscopic Particle Model**:\n  Each single zinc atom displaces two hydrogen ions from solution, forming one molecule of hydrogen gas ($H_2$).\n\n* **Symbolic Representation**:\n  $$\\text{Zn(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{ZnCl}_2\\text{(aq)} + \\text{H}_2\\text{(g)}$$\n  The stoichiometric mole ratio is $1 : 2 : 1 : 1$, allowing us to predict exact masses and volumes."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Molar Gas Volumes & Gay-Lussac's Law",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Gas Stoichiometry Principles",
                        "content": "### Molar Gas Volume ($V_m$)\nOne mole of **any gas** occupies the same volume under identical temperature and pressure conditions:\n* **At S.T.P.** ($0^\\circ\\text{C}, 1\\text{ atm}$): $V_m = 22.4\\text{ dm}^3\\text{ mol}^{-1}$ ($22,400\\text{ cm}^3$)\n* **At R.T.P.** ($25^\\circ\\text{C}, 1\\text{ atm}$): $V_m = 24.0\\text{ dm}^3\\text{ mol}^{-1}$ ($24,000\\text{ cm}^3$)\n\n### Gay-Lussac's Law of Combining Volumes\nWhen gases react, they do so in volumes that bear simple whole-number ratios to one another and to gaseous products at constant temperature and pressure ($\\text{Volume Ratio} = \\text{Mole Ratio}$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Stoichiometry in Vehicle Safety Systems",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Automotive Airbag Deployment\nVehicle safety airbags contain sodium azide ($\\text{NaN}_3$). In a crash, a crash sensor ignites a precise mass of azide, generating exactly the volume of nitrogen gas needed ($2\\text{NaN}_3 \\rightarrow 2\\text{Na} + 3\\text{N}_2$) to inflate the cushion in 30 milliseconds without over-pressurizing."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Reacting Mass and Gas Volume Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. $\\text{MgCO}_3\\text{(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{MgCl}_2\\text{(aq)} + \\text{CO}_2\\text{(g)} + \\text{H}_2\\text{O(l)}$. Calculate volume of $\\text{CO}_2$ at s.t.p. produced from $8.4\\text{ g } \\text{MgCO}_3$ ($M = 84.0\\text{ g/mol}$, $V_m = 22.4\\text{ dm}^3$).\n2. $2\\text{SO}_2\\text{(g)} + \\text{O}_2\\text{(g)} \\rightarrow 2\\text{SO}_3\\text{(g)}$. If $20\\text{ cm}^3$ of $\\text{SO}_2$ reacts, calculate required volume of $\\text{O}_2$ and formed $\\text{SO}_3$.",
                        "steps": [
                            "**Problem 1 (Gas Volume from Solid Mass)**:\n- Moles of $\\text{MgCO}_3 = \\frac{8.4\\text{ g}}{84.0\\text{ g/mol}} = 0.1\\text{ mol}$\n- Mole ratio $\\text{MgCO}_3 : \\text{CO}_2 = 1 : 1 \\implies \\text{Moles of } \\text{CO}_2 = 0.1\\text{ mol}$\n- Volume at s.t.p. $= 0.1\\text{ mol} \\times 22.4\\text{ dm}^3\\text{ mol}^{-1} = 2.24\\text{ dm}^3$ ($2240\\text{ cm}^3$)",
                            "**Problem 2 (Gay-Lussac's Volume Ratios)**:\n- Volume ratio $\\text{SO}_2 : \\text{O}_2 = 2 : 1 \\implies \\text{Volume of } \\text{O}_2 = \\frac{20}{2} = 10\\text{ cm}^3$\n- Volume ratio $\\text{SO}_2 : \\text{SO}_3 = 2 : 2 = 1 : 1 \\implies \\text{Volume of } \\text{SO}_3 = 20\\text{ cm}^3$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why All Gases Have Equal Molar Volumes",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does 1 mole of heavy chlorine gas occupy more space than 1 mole of light helium?\nIn gases, individual molecules are separated by vast distances of empty space. The physical size of the particle itself is negligible compared to the vast empty space between them.\n\nTherefore, at identical temperature and pressure, 1 mole of ANY gas occupies exactly the same volume ($22.4\\text{ dm}^3$ at s.t.p. or $24.0\\text{ dm}^3$ at r.t.p.), regardless of molecular mass."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Stoichiometry",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of hydrogen gas at r.t.p. is evolved when $6.54\\text{ g}$ of zinc metal reacts completely with excess dilute hydrochloric acid? ($A_r$: $\\text{Zn} = 65.4$, $V_m = 24.0\\text{ dm}^3\\text{ mol}^{-1}$)",
                        "options": [
                            "$2.24\\text{ dm}^3$",
                            "$24.0\\text{ dm}^3$",
                            "$2.40\\text{ dm}^3$",
                            "$1.20\\text{ dm}^3$"
                        ],
                        "answer": "C",
                        "explanation": "Equation: $\\text{Zn} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2$. Moles of $\\text{Zn} = 6.54 / 65.4 = 0.1\\text{ mol}$. Moles of $\\text{H}_2 = 0.1\\text{ mol}$. Volume at r.t.p. $= 0.1 \\times 24.0 = 2.40\\text{ dm}^3$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Stoichiometry",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Stoichiometry\n- **Stoichiometric Ratio**: Molar coefficients in balanced equations.\n- **Molar Gas Volumes**: $22.4\\text{ dm}^3$ at s.t.p., $24.0\\text{ dm}^3$ at r.t.p.\n- **Gay-Lussac's Law**: For reacting gases, $\\text{Volume Ratio} = \\text{Mole Ratio}$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.7: Volumetric Analysis (Acid-Base Titrations)",
            "unit_order": 7,
            "lesson_title": "Volumetric Analysis (Acid-Base Titrations)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Determining Exact Concentrations",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master volumetric analysis and laboratory titration techniques, learn correct rinsing protocols for burettes and pipettes, choose suitable indicators, and calculate unknown solution concentrations."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Quality Control in Food and Manufacturing",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In a quality-control lab at a commercial food factory in Nairobi producing vinegar (ethanoic acid), chemists must verify that the acidity meets regulatory standards before bottling.\n\nThey perform a **Titration**: slowly adding a standard base of known concentration from a graduated burette into an acid sample until neutralisation is complete. This quantitative measurement is called **Volumetric Analysis**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Running a Laboratory Titration",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's look at the steps and particle chemistry of an acid-base titration:\n\n* **Macroscopic Observation**:\n  Pipetting $25.0\\text{ cm}^3$ of $\\text{NaOH}$ into a conical flask and adding phenolphthalein indicator produces a bright pink solution. Adding $\\text{HCl}$ from a burette causes the pink color to swirl and fade. A single drop delivers the **end-point**, turning the solution permanently colourless.\n\n* **Microscopic Particle Model**:\n  Incoming hydrogen ions ($H^+$) combine with hydroxide ions ($OH^-$) to form neutral water:\n  $$\\text{H}^+\\text{(aq)} + \\text{OH}^-\\text{(aq)} \\rightarrow \\text{H}_2\\text{O(l)}$$\n  When the final $OH^-$ ion is neutralized, the indicator changes colour.\n\n* **Symbolic Representation**:\n  $$\\text{HCl(aq)} + \\text{NaOH(aq)} \\rightarrow \\text{NaCl(aq)} + \\text{H}_2\\text{O(l)}$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Glassware Rinsing Protocols & Indicator Selection",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Titration Glassware & Indicators",
                        "content": "### Glassware Cleaning Rules:\n* **Pipette**: Rinse with distilled water, then with the solution to be delivered.\n* **Burette**: Rinse with distilled water, then with the titrant acid/base.\n* **Conical Flask**: Rinse **only with distilled water** (never with reagent!).\n\n### Indicator Selection Guide:\n* **Strong Acid + Strong Base**: Phenolphthalein (Pink $\\rightarrow$ Colourless) or Methyl Orange.\n* **Strong Acid + Weak Base**: Methyl Orange (Yellow $\\rightarrow$ Orange).\n* **Weak Acid + Strong Base**: Phenolphthalein (Pink $\\rightarrow$ Pale Pink/Colourless)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Titrations in Water Quality and Agriculture",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Soil Acidity Analysis at KALRO\nSoil scientists at **KALRO (Kenya Agricultural and Livestock Research Organisation)** perform titrations on soil extracts to measure acidity, advising farmers in the Rift Valley and Western Kenya on optimal agricultural lime application rates to maximize maize and tea yields."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Titration Calculations & Acid Standardisation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. $25.0\\text{ cm}^3$ of $0.10\\text{ M } \\text{NaOH}$ required $25.0\\text{ cm}^3$ of $\\text{HCl}$ to reach the end-point. Calculate $\\text{HCl}$ molarity.\n2. To standardize $\\text{HCl}$, $1.325\\text{ g}$ of $\\text{Na}_2\\text{CO}_3$ was made up to $250.0\\text{ cm}^3$. A $25.0\\text{ cm}^3$ portion required $22.5\\text{ cm}^3$ of $\\text{HCl}$. Find acid molarity.",
                        "steps": [
                            "**Problem 1 (Direct Titration)**:\n- Moles of $\\text{NaOH} = \\frac{0.10 \\times 25.0}{1000} = 0.0025\\text{ mol}$\n- Mole ratio $\\text{HCl} : \\text{NaOH} = 1 : 1 \\implies \\text{Moles of } \\text{HCl} = 0.0025\\text{ mol}$\n- Molarity of $\\text{HCl} = \\frac{0.0025 \\times 1000}{25.0} = 0.10\\text{ M}$",
                            "**Problem 2 (Standardisation with $\\text{Na}_2\\text{CO}_3$)**:\n- Total moles in $250\\text{ cm}^3 = \\frac{1.325\\text{ g}}{106.0\\text{ g/mol}} = 0.0125\\text{ mol} \\implies M_{\\text{carbonate}} = 0.05\\text{ M}$\n- Moles in $25.0\\text{ cm}^3$ sample $= \\frac{0.05 \\times 25.0}{1000} = 0.00125\\text{ mol}$\n- Equation: $\\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\rightarrow 2\\text{NaCl} + \\text{CO}_2 + \\text{H}_2\\text{O}$ (Ratio $1 : 2$)\n- Moles of $\\text{HCl} = 2 \\times 0.00125 = 0.0025\\text{ mol}$\n- Molarity of $\\text{HCl} = \\frac{0.0025 \\times 1000}{22.5} = 0.111\\text{ M}$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why a Wet Conical Flask Does Not Ruin a Titration",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Does residual water in a conical flask invalidate titration results?\nNo! Water droplets inside the flask dilute the analyte concentration, but they do **not change the number of moles** delivered by the pipette.\n\nBecause titration neutralizes absolute moles of reactant, water droplets do not alter the required titre volume. In contrast, rinsing the flask with base would introduce extra, unmeasured moles, ruining the experiment!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Titrations",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A $25.0\\text{ cm}^3$ portion of $0.05\\text{ M } \\text{Na}_2\\text{CO}_3$ required $20.0\\text{ cm}^3$ of dilute sulphuric(VI) acid for complete neutralisation. What is the molarity of the acid? ($\\text{H}_2\\text{SO}_4 + \\text{Na}_2\\text{CO}_3 \\rightarrow \\text{Na}_2\\text{SO}_4 + \\text{CO}_2 + \\text{H}_2\\text{O}$)",
                        "options": [
                            "$0.0625\\text{ M}$",
                            "$0.125\\text{ M}$",
                            "$0.05\\text{ M}$",
                            "$0.025\\text{ M}$"
                        ],
                        "answer": "A",
                        "explanation": "Moles of $\\text{Na}_2\\text{CO}_3 = \\frac{0.05 \\times 25.0}{1000} = 0.00125\\text{ mol}$. Equation ratio is $1 : 1 \\implies \\text{Moles of } \\text{H}_2\\text{SO}_4 = 0.00125\\text{ mol}$. Molarity of $\\text{H}_2\\text{SO}_4 = \\frac{0.00125 \\times 1000}{20.0} = 0.0625\\text{ M}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Titration Techniques",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Volumetric Analysis\n- **Glassware Rules**: Pipette & burette rinsed with reagent; conical flask rinsed ONLY with water.\n- **Readings**: Burette recorded to 2 decimal places (ending in .00 or .05); concordant titres within $\\pm 0.20\\text{ cm}^3$.\n- **Calculation Pipeline**: Moles of standard $\\rightarrow$ Stoichiometric ratio $\\rightarrow$ Moles of analyte $\\rightarrow$ Molarity."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.8: Analyzing Complex Systems: Back Titrations",
            "unit_order": 8,
            "lesson_title": "Analyzing Complex Systems: Back Titrations",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Challenge of Insoluble Reactants",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master two-stage back titrations, understanding how unreacted excess acid is titrated to determine the purity or composition of insoluble and slow-reacting samples."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Analyzing Insoluble Rocks and Minerals",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Civil engineers in **Mombasa and Nairobi** frequently test limestone shipments (calcium carbonate, $\\text{CaCO}_3$) to verify purity before concrete manufacturing. If limestone has excess clay impurities, concrete will crack.\n\nHowever, limestone is completely insoluble in water, making direct titration impossible. To solve this, chemists use a **Back Titration**: dissolving the sample in a known excess of acid and titrating the leftover surplus acid."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Two-Stage Back Titration Strategy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's trace the two-stage analytical pathway:\n\n* **Stage 1 (Dissolution with Excess Acid)**:\n  Crushed limestone is reacted with a surplus volume of strong acid (e.g. $100.0\\text{ cm}^3$ of $0.20\\text{ M } \\text{HCl}$):\n  $$\\text{CaCO}_3\\text{(s)} + 2\\text{HCl(aq)} \\rightarrow \\text{CaCl}_2\\text{(aq)} + \\text{CO}_2\\text{(g)} + \\text{H}_2\\text{O(l)}$$\n  The carbonate reacts completely, leaving unreacted hydrogen ions in solution.\n\n* **Stage 2 (Titrating Leftover Acid)**:\n  The solution is titrated with standard base (e.g. $0.10\\text{ M } \\text{NaOH}$):\n  $$\\text{HCl(aq)} + \\text{NaOH(aq)} \\rightarrow \\text{NaCl(aq)} + \\text{H}_2\\text{O(l)}$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Golden Principle of Back Titration",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Back Titration Principle",
                        "content": "$$\\text{Moles of Acid Reacted with Sample} = \\text{Total Initial Acid Moles} - \\text{Leftover Acid Moles from Titration}$$\n\n### Why Back Titrations are Essential:\n* **Insoluble Solids**: Carbonates, oxides, and ores that cannot dissolve in water.\n* **Slow-Reacting Substances**: Where direct reactions do not yield a sharp end-point.\n* **Volatile Analytes**: Such as ammonia gas, which would evaporate during direct titration."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Industrial Applications: Limestone & Fertilizer Assays",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Cement and Agricultural Lime Testing\nAt cement manufacturing facilities in **Bamburi (Mombasa) and Athi River**, quality analysts perform back titrations daily on limestone quarry samples to ensure calcium carbonate content exceeds 85% purity for structural grade cement."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Limestone Purity Calculation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A $1.00\\text{ g}$ limestone sample was added to $100.0\\text{ cm}^3$ of $0.20\\text{ M } \\text{HCl}$. The unreacted acid required $24.8\\text{ cm}^3$ of $0.10\\text{ M } \\text{NaOH}$. Find percentage purity of $\\text{CaCO}_3$ ($A_r$: $\\text{Ca}=40, \\text{C}=12, \\text{O}=16$).",
                        "steps": [
                            "**Step 1: Total Initial Acid Moles**:\n$$n_{\\text{initial}} = \\frac{0.20 \\times 100.0}{1000} = 0.020\\text{ moles}$$",
                            "**Step 2: Leftover Acid Moles from Titration**:\n$$n_{\\text{leftover}} = \\frac{0.10 \\times 24.8}{1000} = 0.00248\\text{ moles } (\\text{since } \\text{HCl}:\\text{NaOH} = 1:1)$$",
                            "**Step 3: Acid Moles Reacted with Sample**:\n$$n_{\\text{reacted}} = 0.020 - 0.00248 = 0.01752\\text{ moles}$$",
                            "**Step 4: Moles of $\\text{CaCO}_3$**:\n$$\\text{Ratio } \\text{CaCO}_3 : \\text{HCl} = 1 : 2 \\implies n_{\\text{carbonate}} = \\frac{0.01752}{2} = 0.00876\\text{ moles}$$",
                            "**Step 5: Mass and Percentage Purity**:\n- Molar mass of $\\text{CaCO}_3 = 100.0\\text{ g/mol}$\n- Pure mass $= 0.00876\\text{ mol} \\times 100.0\\text{ g/mol} = 0.876\\text{ g}$\n- Percentage purity $= \\frac{0.876\\text{ g}}{1.00\\text{ g}} \\times 100\\% = 87.6\\%$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why We Subtract Leftover Moles",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### What do the moles from the titration represent?\nIn a back titration, the titration measures the **leftover unreacted acid**, not the sample itself.\n\nUsing the titration value directly without subtracting from initial moles would calculate the unreacted surplus rather than the analyte. Always subtract leftover moles from initial moles first!"
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Back Titration",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A $0.50\\text{ g}$ sample of metal carbonate ($\\text{MCO}_3$) was dissolved in $30.0\\text{ cm}^3$ of $0.50\\text{ M } \\text{HCl}$. The unreacted acid required $10.0\\text{ cm}^3$ of $1.0\\text{ M } \\text{NaOH}$. How many moles of acid reacted with the carbonate?",
                        "options": [
                            "$0.005\\text{ moles}$",
                            "$0.010\\text{ moles}$",
                            "$0.015\\text{ moles}$",
                            "$0.020\\text{ moles}$"
                        ],
                        "answer": "A",
                        "explanation": "Initial acid moles $= \\frac{0.50 \\times 30.0}{1000} = 0.015\\text{ mol}$. Leftover acid moles $= \\frac{1.0 \\times 10.0}{1000} = 0.010\\text{ mol}$. Acid reacted with carbonate $= 0.015 - 0.010 = 0.005\\text{ moles}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Back Titrations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Back Titrations\n- **Purpose**: Volumetric analysis of insoluble, slow, or volatile samples.\n- **Stage 1**: React sample with known excess reagent.\n- **Stage 2**: Titrate leftover surplus reagent.\n- **Core Formula**: $\\text{Reacted Moles} = \\text{Initial Moles} - \\text{Leftover Moles}$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 2.9: Gas Stoichiometry and Redox Titrations",
            "unit_order": 9,
            "lesson_title": "Gas Stoichiometry and Redox Titrations",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Electron Transfer in Solution",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will connect gas stoichiometry with redox titrations, balancing redox half-equations with potassium manganate(VII) and calculating reactant amounts from titrimetric data."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Color Changes in Redox Reactions",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In acid-base titrations, indicators are needed because reactants and products are colourless. In **Redox Titrations**, however, the molecules themselves change colour as they gain or lose electrons.\n\nWhen a deep purple drop of potassium manganate(VII) touches an iron(II) solution, the purple colour instantly disappears as manganate is reduced to colourless manganese(II) ions!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Chemistry of Redox Titrations",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's examine electron transfer in the manganate-iron(II) system:\n\n* **Reduction Half-Equation (Manganate)**:\n  $$\\text{MnO}_4^-\\text{(aq)} + 8\\text{H}^+\\text{(aq)} + 5\\text{e}^- \\rightarrow \\text{Mn}^{2+}\\text{(aq)} + 4\\text{H}_2\\text{O(l)}$$\n  Deep purple $\\text{MnO}_4^-$ (Mn in $+7$ state) reduces to colourless $\\text{Mn}^{2+}$.\n\n* **Oxidation Half-Equation (Iron(II))**:\n  $$\\text{Fe}^{2+}\\text{(aq)} \\rightarrow \\text{Fe}^{3+}\\text{(aq)} + \\text{e}^-$$\n  Pale green $\\text{Fe}^{2+}$ loses an electron to form yellow $\\text{Fe}^{3+}$.\n\n* **Overall Balanced Ionic Equation**:\n  $$\\text{MnO}_4^-\\text{(aq)} + 8\\text{H}^+\\text{(aq)} + 5\\text{Fe}^{2+}\\text{(aq)} \\rightarrow \\text{Mn}^{2+}\\text{(aq)} + 5\\text{Fe}^{3+}\\text{(aq)} + 4\\text{H}_2\\text{O(l)}$$\n  The stoichiometric mole ratio is **$1 : 5$**!"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Principles of Redox Volumetric Analysis",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Redox Titration Principles",
                        "content": "### Self-Indicating Reagents\nReagents like potassium manganate(VII) ($\\text{KMnO}_4$) and potassium dichromate(VI) ($\\text{K}_2\\text{Cr}_2\\text{O}_7$) undergo dramatic colour changes during redox, requiring no external indicator:\n- $\\text{MnO}_4^-$ (Purple) $\\rightarrow \\text{Mn}^{2+}$ (Colourless)\n- $\\text{Cr}_2\\text{O}_7^{2-}$ (Orange) $\\rightarrow \\text{Cr}^{3+}$ (Emerald Green)\n\n### The Boiled Water Protocol:\nStandard $\\text{Fe}^{2+}$ solutions must be prepared using boiled, cooled distilled water to expel dissolved oxygen, preventing pre-oxidation to $\\text{Fe}^{3+}$ before titration."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Applications in Food and Environmental Analysis",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Vitamin C and Water Ecosystem Quality\n* **Food Testing**: Redox titrations with iodine or manganate determine Vitamin C (ascorbic acid) concentrations in fresh Kenyan citrus exports.\n* **Environmental Monitoring**: Dissolved oxygen levels in **Lake Victoria and Lake Naivasha** are measured using Winkler redox titrations to monitor aquatic health."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Standardising Potassium Manganate(VII)",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A $25.0\\text{ cm}^3$ sample of $0.10\\text{ M } \\text{Fe}^{2+}$ standard solution required $22.5\\text{ cm}^3$ of acidified $\\text{KMnO}_4$ for complete oxidation. Calculate the molarity of $\\text{KMnO}_4$.",
                        "steps": [
                            "**Step 1: Calculate moles of $\\text{Fe}^{2+}$ reacted**:\n$$n_{\\text{Fe}^{2+}} = \\frac{0.10\\text{ M} \\times 25.0\\text{ cm}^3}{1000} = 0.0025\\text{ moles}$$",
                            "**Step 2: Use stoichiometric ratio ($1 : 5$)**:\n$$n_{\\text{MnO}_4^-} = \\frac{n_{\\text{Fe}^{2+}}}{5} = \\frac{0.0025}{5} = 0.00050\\text{ moles}$$",
                            "**Step 3: Calculate Molarity of $\\text{KMnO}_4$**:\n$$M = \\frac{0.00050\\text{ mol} \\times 1000}{22.5\\text{ cm}^3} = 0.0222\\text{ mol dm}^{-3}\\text{ (or } 0.0222\\text{ M)}$$"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why We Only Acidify With Sulphuric Acid",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why can't we use hydrochloric or nitric acid to acidify manganate?\nManganate(VII) is an extremely powerful oxidizer:\n* **Hydrochloric acid ($\\text{HCl}$)**: Manganate oxidizes chloride ions ($Cl^-$) into toxic chlorine gas ($Cl_2$), consuming extra manganate and inflating the titre volume.\n* **Nitric acid ($\\text{HNO}_3$)**: Nitric acid is itself an oxidizer and competes with manganate to oxidize the iron(II), invalidating the stoichiometry.\n\nDilute sulphuric(VI) acid ($\\text{H}_2\\text{SO}_4$) is the only stable, non-interfering acid suitable for acidification."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Redox Titrations",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "A $25.0\\text{ cm}^3$ sample of $\\text{Fe}^{2+}$ required $20.0\\text{ cm}^3$ of $0.02\\text{ M } \\text{K}_2\\text{Cr}_2\\text{O}_7$ to reach the green end-point. What is the molarity of $\\text{Fe}^{2+}$? ($\\text{Cr}_2\\text{O}_7^{2-} + 14\\text{H}^+ + 6\\text{Fe}^{2+} \\rightarrow 2\\text{Cr}^{3+} + 6\\text{Fe}^{3+} + 7\\text{H}_2\\text{O}$)",
                        "options": [
                            "$0.016\\text{ M}$",
                            "$0.096\\text{ M}$",
                            "$0.024\\text{ M}$",
                            "$0.048\\text{ M}$"
                        ],
                        "answer": "B",
                        "explanation": "Moles of dichromate $= \\frac{0.02 \\times 20.0}{1000} = 0.00040\\text{ mol}$. Mole ratio $\\text{Cr}_2\\text{O}_7^{2-} : \\text{Fe}^{2+} = 1 : 6 \\implies \\text{Moles of } \\text{Fe}^{2+} = 6 \\times 0.00040 = 0.00240\\text{ mol}$. Molarity $= \\frac{0.00240 \\times 1000}{25.0} = 0.096\\text{ M}$."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Redox Titrations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Redox Titrations\n- **Mechanism**: Electron transfer between oxidising and reducing agents.\n- **Manganate Ratio**: $\\text{MnO}_4^- : \\text{Fe}^{2+} = 1 : 5$.\n- **Dichromate Ratio**: $\\text{Cr}_2\\text{O}_7^{2-} : \\text{Fe}^{2+} = 1 : 6$.\n- **Acidification Rule**: Strictly use dilute sulphuric(VI) acid to prevent side reactions."
                    }
                }
            ]
        }
    ]

    # 3. Execute Ingestion & Publishing for Each Module
    for m_data in modules_data:
        unit_name = m_data["unit_name"]
        unit_order = m_data["unit_order"]
        lesson_title = m_data["lesson_title"]
        cards = m_data["cards"]

        print(f"\n--- Ingesting {unit_name} ---")

        # Create or update LearningUnit
        unit, unit_created = LearningUnit.objects.get_or_create(
            topic=topic,
            name=unit_name,
            defaults={"order": unit_order, "description": f"Curriculum module for {lesson_title}"}
        )
        if not unit_created:
            unit.order = unit_order
            unit.save()
        print(f"  Learning Unit: {unit.name} (ID: {unit.id})")

        # Create or retrieve Lesson
        lesson, lesson_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": lesson_title,
                "status": "published",
                "version": 1
            }
        )
        lesson.title = lesson_title
        lesson.status = "published"
        lesson.save()
        print(f"  Lesson: {lesson.title} (ID: {lesson.id}, Status: {lesson.status})")

        # Clean existing blocks and assets for this lesson to prevent duplicates
        LessonBlock.objects.filter(lesson=lesson).delete()
        LessonAsset.objects.filter(lesson=lesson).delete()

        # Ingest each block
        for order, card in enumerate(cards, start=1):
            block_id = f"f3_chem_t2_l{lesson.id}_b{order}_{uuid.uuid4().hex[:6]}"
            block = LessonBlock.objects.create(
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

            # Ingest attached LessonAsset if specified
            if "asset_info" in card:
                info = card["asset_info"]
                asset = LessonAsset.objects.create(
                    lesson=lesson,
                    title=info["title"],
                    description=info["description"],
                    asset_type="image",
                    source_type="external",
                    storage_type="url",
                    url=info.get("url", ""),
                    status="attached"
                )
                asset.blocks.add(block)

        print(f"  Successfully created {len(cards)} structured LessonBlocks across 8 natural concept pages.")

    print("\n================================================================================")
    print("Ingestion Completed Successfully! All 9 Modules Published to Form 3 Topic 2.")
    print("================================================================================")

if __name__ == "__main__":
    ingest_form3_topic2_mole()
