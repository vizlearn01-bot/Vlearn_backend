import os
import sys
import uuid
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def ingest_form3_topic3_organic():
    print("================================================================================")
    print("Starting VLearn Form 3 Chemistry Batch 3 Ingestion: Organic Chemistry I (3.1-3.7)")
    print("================================================================================")

    # 1. Verify Curriculum Hierarchy
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
        defaults={"description": "Form 3 Chemistry (KLB Syllabus)"}
    )

    topic, _ = Topic.objects.get_or_create(
        subject=subject,
        name="Topic 3: Organic Chemistry I (Aliphatic Hydrocarbons)",
        defaults={
            "description": "Comprehensive study of carbon bonding, homologous series, alkanes, alkenes, alkynes, fractional distillation, cracking, and addition polymerisation.",
            "order": 3
        }
    )
    print(f"Topic verified: {topic.name} (ID: {topic.id}) under {subject.name} (Grade: {grade.name})")

    # 2. Define Clean, Student-Facing Content Data Dictionary (Modules 3.1 - 3.7)
    modules_data = [
        {
            "unit_name": "Module 3.1: Introduction to Organic Chemistry and Homologous Series",
            "unit_order": 1,
            "lesson_title": "Introduction to Organic Chemistry and Homologous Series",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of Carbon",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will enter the world of Organic Chemistry, discover carbon's unique bonding properties (tetravalency and catenation), distinguish between saturated and unsaturated hydrocarbons, and explore the defining characteristics of a Homologous Series."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Carbon: The Universal Element of Life",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "What do the food we eat, the clothes we wear, the biogas powering stoves in rural Kenya, the medicines that heal us, and even the DNA in our cells have in common? They are all built from **carbon**!\n\nWhile the periodic table contains 118 elements, the chemistry of carbon is so vast and unique that it forms an entire branch of science: **Organic Chemistry**. Carbon atoms can link together like building blocks to form endless chains, branches, and rings."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Tetravalency and Catenation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's examine why carbon is capable of forming millions of compounds:\n\n* **Macroscopic Properties**:\n  Organic compounds like liquid paraffin, cooking gas (LPG), or plastics are combustible, have lower melting points than ionic salts, and dissolve easily in organic solvents like ethanol or propanone rather than water.\n\n* **Microscopic Particle Model**:\n  - **Tetravalency**: Carbon (atomic number 6, electron configuration 2.4) has 4 valence electrons. It forms exactly four strong, stable covalent bonds to complete its octet.\n  - **Catenation**: Carbon possesses the unique ability to form strong, stable covalent bonds with other carbon atoms, linking into long chains or rings.\n  - **Multiple Bonding**: Carbon can form single ($C-C$), double ($C=C$), or triple ($C\\equiv C$) bonds with other carbon atoms."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Homologous Series Chain Progression",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Illustrate the structural progression of a homologous series with repeating methylene units.",
                        "instruction": "Structural progression diagram showing Methane ($CH_4$) -> Ethane ($CH_3-CH_3$) -> Propane ($CH_3-CH_2-CH_3$), highlighting the incremental addition of a repeating $-\\text{CH}_2-$ unit.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    },
                    "asset_info": {
                        "title": "Homologous Series Progression",
                        "description": "Visual diagram demonstrating incremental addition of methylene units in hydrocarbon series.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/States_of_matter_En.svg/800px-States_of_matter_En.svg.png"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Hydrocarbon Classes & Homologous Series",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Hydrocarbon Classification",
                        "content": "### Organic Chemistry\nThe scientific study of carbon compounds, excluding simple oxides ($CO, CO_2$), carbonates, and hydrogencarbonates (which behave like inorganic mineral salts).\n\n### Hydrocarbons\nCompounds containing **carbon and hydrogen only**.\n* **Saturated Hydrocarbons**: Linked by single covalent bonds only (Alkanes: $C_nH_{2n+2}$).\n* **Unsaturated Hydrocarbons**: Contain double or triple bonds (Alkenes: $C_nH_{2n}$, Alkynes: $C_nH_{2n-2}$).\n\n### Characteristics of a Homologous Series:\n1. Same functional group.\n2. Same general molecular formula.\n3. Similar chemical properties.\n4. Gradual trend in physical properties (boiling point increases with chain length).\n5. Successive members differ by a $-\\text{CH}_2-$ group ($14\\text{ a.m.u.}$).\n6. Prepared by the same general chemical methods."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Petroleum Refining and Clean Energy in Kenya",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Fractional Distillation of Crude Oil\nCrude oil is separated into useful fuels (petrol, kerosene, diesel) in a fractionating column based on boiling point differences.\n\nIn Kenya and the wider East African Community, refineries and fuel importers adhere to the **Clean Fuel Standards**, which mandate low-sulfur diesel and unleaded petrol to minimize sulfur dioxide emissions and protect public health and the environment."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Analyzing Homologous Mass Differences",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Show that the third alkene member ($C_4H_8$) differs from the second member ($C_3H_6$) by a $-\\text{CH}_2-$ group, and calculate the difference in their relative molecular masses ($C = 12.0, H = 1.0$).",
                        "steps": [
                            "**Step 1: Formula Difference**:\n$$\\text{Difference} = C_4H_8 - C_3H_6 = C_{(4-3)}H_{(8-6)} = -\\text{CH}_2-$$",
                            "**Step 2: Calculate Molecular Masses ($M_r$)**:\n- $M_r(C_3H_6) = 3(12.0) + 6(1.0) = 36.0 + 6.0 = 42.0$\n- $M_r(C_4H_8) = 4(12.0) + 8(1.0) = 48.0 + 8.0 = 56.0$",
                            "**Step 3: Mass Difference**:\n$$\\Delta M_r = 56.0 - 42.0 = 14.0$$\n*Interpretation*: The mass of one $-\\text{CH}_2-$ unit is $12.0 + 2(1.0) = 14.0\\text{ a.m.u.}$ Every successive member in a homologous series increases by exactly $14.0\\text{ a.m.u.}$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Homologous Series",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following is NOT a property of a homologous series?",
                        "options": [
                            "Members share the same general formula",
                            "Consecutive members differ by a molecular mass of 14",
                            "All members have identical physical properties",
                            "All members are prepared by similar general chemical methods"
                        ],
                        "answer": "C",
                        "explanation": "Members of a homologous series do not have identical physical properties; they exhibit a gradual, steady trend (such as boiling point increasing as molecular mass and chain length increase)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Homologous Series",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Organic Chemistry & Homologous Series\n- **Tetravalency & Catenation**: 4 valence electrons enable carbon to form stable covalent chains.\n- **Homologous Series**: Family of compounds with same functional group, general formula, and $-\\text{CH}_2-$ incremental step.\n- **Exclusions**: Oxides and carbonates are classified as inorganic mineral salts."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 3.2: Alkanes (Nomenclature, Structure, and Isomerism)",
            "unit_order": 2,
            "lesson_title": "Alkanes (Nomenclature, Structure, and Isomerism)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Architecture of Alkanes",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will master the IUPAC naming system, molecular structures, and structural isomerism of alkanes (saturated hydrocarbons with the general formula $\\text{C}_n\\text{H}_{2n+2}$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Building Molecular Structures",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Just as four toy blocks can be stacked in a straight column or arranged in a T-shape, four carbon atoms and ten hydrogen atoms can link together in a straight chain or branch.\n\nEven though both arrangements share the identical molecular formula ($C_4H_{10}$), they are completely distinct chemical substances with different boiling points and densities: **Isomers**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Saturated Hydrocarbons & Alkane Representation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Alkanes are saturated hydrocarbons containing only single covalent bonds, conforming to the general formula **$C_nH_{2n+2}$**:\n\n* **Molecular Formula**: States actual atom counts (e.g. $C_4H_{10}$).\n* **Structural Formula**: Displays every individual bond explicitly.\n* **Condensed Formula**: Groups attached hydrogens (e.g. $CH_3-CH_2-CH_2-CH_3$).\n* **Skeletal Formula**: Depicts the carbon backbone as a zig-zag line where vertices and ends represent carbon atoms."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "IUPAC Systematic Nomenclature for Alkanes",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "IUPAC Naming Rules for Alkanes",
                        "content": "### Step-by-Step Rules:\n1. **Identify Parent Chain**: Find the longest continuous carbon chain (1: meth-, 2: eth-, 3: prop-, 4: but-, 5: pent-, 6: hex-, 7: hept-, 8: oct-, 9: non-, 10: dec-).\n2. **Identify Alkyl Branches**: Remove 1 hydrogen from an alkane ($-CH_3$: methyl, $-C_2H_5$: ethyl).\n3. **Number Carbons**: Number from the end that gives branches the lowest position numbers.\n4. **Assemble Name**: Position-prefix-parent (e.g. 2-methylpropane). Use di-, tri- for multiples with commas separating numbers."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Structural Isomerism in Alkanes",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Isomerism",
                        "content": "### Definition\nCompounds with the **same molecular formula** but **different structural formulas**.\n\n### Alkane Isomer Scope:\n* $C_1$ to $C_3$ (Methane, Ethane, Propane): No isomers.\n* $C_4H_{10}$ (Butane): 2 isomers (butane, 2-methylpropane).\n* $C_5H_{12}$ (Pentane): 3 isomers (pentane, 2-methylbutane, 2,2-dimethylpropane).\n* $C_6H_{14}$ (Hexane): 5 isomers."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Naming Branched Hydrocarbons",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "State the systematic IUPAC name for the compound: $$CH_3-CH(CH_3)-CH(CH_2CH_3)-CH_2-CH_3$$",
                        "steps": [
                            "**Step 1: Find Longest Chain**:\nTracing the continuous carbon backbone gives 5 carbons $\\implies$ Parent alkane is **pentane**.",
                            "**Step 2: Number for Lowest Locants**:\n- Left-to-right: branches at C2 (methyl) and C3 (ethyl) $\\implies (2, 3)$.\n- Right-to-left: branches at C3 and C4 $\\implies (3, 4)$.\n- Choose left-to-right numbering.",
                            "**Step 3: Alphabetize & Assemble**:\nEthyl precedes methyl alphabetically $\\implies$ **3-ethyl-2-methylpentane**."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Straight vs Bent Chains",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Is a carbon chain drawn around a corner a branched alkane?\nNo! Drawing $CH_3-CH_2-CH_2$ with a $CH_3$ going downwards is simply a bent representation of **straight-chain butane**.\n\nA true branch occurs only when a carbon atom is bonded to at least three other carbon atoms. If you can trace all carbons continuously without lifting your pen or backtracking, it is a single continuous parent chain."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Alkane Nomenclature",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the systematic IUPAC name for $(CH_3)_3C-CH_2-CH_3$?",
                        "options": [
                            "Pentane",
                            "2-methylbutane",
                            "2,2-dimethylpropane",
                            "2,2-dimethylbutane"
                        ],
                        "answer": "D",
                        "explanation": "Expanding gives $CH_3-C(CH_3)_2-CH_2-CH_3$. The longest continuous chain has 4 carbons (butane). Carbon 2 holds two methyl branches, giving 2,2-dimethylbutane."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Alkane Structure",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Alkanes\n- **Formula**: General formula $C_nH_{2n+2}$ (saturated single bonds).\n- **IUPAC Pipeline**: Longest chain $\\rightarrow$ lowest branch numbering $\\rightarrow$ alphabetical prefixes.\n- **Isomerism**: Same formula, different structural configurations; branching lowers boiling point by reducing molecular contact surface area."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 3.3: Laboratory Preparation and Chemical Properties of Alkanes",
            "unit_order": 3,
            "lesson_title": "Laboratory Preparation and Chemical Properties of Alkanes",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Clean Energy from Methane",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will study the laboratory preparation of methane and ethane through decarboxylation, and explore combustion and free-radical substitution reactions of alkanes."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Biogas: Kenya's Renewable Energy Source",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "On farms across **Kiambu, Eldoret, and Meru**, biogas digesters convert cow dung and agricultural waste into clean, combustible methane gas ($CH_4$) through anaerobic bacterial fermentation.\n\nIn the school laboratory, we can prepare methane in minutes using thermal decarboxylation."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Preparation and Collection of Methane and Ethane",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Decarboxylation with Soda Lime:\nHeating anhydrous sodium ethanoate with **soda lime** produces methane gas:\n$$CH_3COONa(s) + NaOH(s) \\xrightarrow[\\text{CaO}]{\\text{heat}} CH_4(g) + Na_2CO_3(s)$$\n\n* **Why Soda Lime ($NaOH + CaO$) instead of pure $NaOH$?**\n  Pure $NaOH$ is deliquescent and would melt into a liquid, attacking and shattering the hot glass test tube. Calcium oxide ($CaO$) keeps the mixture dry and porous.\n* **Ethane Preparation**:\n  $$CH_3CH_2COONa(s) + NaOH(s) \\xrightarrow[\\text{CaO}]{\\text{heat}} C_2H_6(g) + Na_2CO_3(s)$$\n* **Collection**: Collected **over water** because alkanes are non-polar and slightly soluble in water."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Physical Properties of Alkanes",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Physical Properties of Alkanes",
                        "content": "### States at Room Temperature:\n* $C_1$ to $C_4$ (Methane to Butane): Colorless, odorless gases.\n* $C_5$ to $C_{17}$: Volatile liquids.\n* $C_{18}+$: Waxy solids.\n\n### Trends & Solubility:\n* **Boiling Points**: Increase steadily down the series due to increasing strength of intermolecular van der Waals forces.\n* **Solubility**: Insoluble in polar water, highly soluble in non-polar organic solvents (ethanol, tetrachloromethane).\n* **Density**: Less dense than water."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Combustion Reactions: Complete vs Incomplete",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Alkanes are widely used as fuels due to high heat release during combustion:\n\n* **Complete Combustion (Plentiful Oxygen)**:\n  Burns with a clean, blue, non-sooty flame:\n  $$CH_4(g) + 2O_2(g) \\rightarrow CO_2(g) + 2H_2O(l) + \\text{Heat}$$\n\n* **Incomplete Combustion (Limited Oxygen)**:\n  Produces toxic carbon(II) oxide ($CO$) and carbon black (soot):\n  $$2CH_4(g) + 3O_2(g) \\rightarrow 2CO(g) + 4H_2O(l)$$\n  *Industrial Note*: Carbon black is used in printer inks, black paints, and vehicle tyre reinforcement."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Photochemical Halogenation of Methane",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In the presence of **ultraviolet (UV) light or sunlight**, alkanes undergo chain substitution with halogens:\n\n1. $$CH_4 + Cl_2 \\xrightarrow{\\text{UV}} CH_3Cl + HCl \\quad (\\text{Chloromethane})$$\n2. $$CH_3Cl + Cl_2 \\xrightarrow{\\text{UV}} CH_2Cl_2 + HCl \\quad (\\text{Dichloromethane})$$\n3. $$CH_2Cl_2 + Cl_2 \\xrightarrow{\\text{UV}} CHCl_3 + HCl \\quad (\\text{Trichloromethane / Chloroform})$$\n4. $$CHCl_3 + Cl_2 \\xrightarrow{\\text{UV}} CCl_4 + HCl \\quad (\\text{Tetrachloromethane})$$"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Combustion Air Volume",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of air (21% $O_2$ by volume) required to completely burn $32\\text{ g}$ of methane at r.t.p. ($V_m = 24.0\\text{ dm}^3\\text{ mol}^{-1}, C=12.0, H=1.0$).",
                        "steps": [
                            "**Step 1: Moles of Methane**:\n$$n(CH_4) = \\frac{32.0\\text{ g}}{16.0\\text{ g/mol}} = 2.0\\text{ moles}$$",
                            "**Step 2: Stoichiometric Moles of $O_2$**:\n$$CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O \\implies n(O_2) = 2 \\times 2.0 = 4.0\\text{ moles}$$",
                            "**Step 3: Volume of Pure $O_2$ and Air**:\n- $\\text{Volume of } O_2 = 4.0\\text{ mol} \\times 24.0\\text{ dm}^3/\\text{mol} = 96.0\\text{ dm}^3$\n- $\\text{Volume of Air} = 96.0 \\times \\frac{100}{21} = 457.14\\text{ dm}^3$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Alkane Reactions",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which substance is produced alongside methane during the decarboxylation of sodium ethanoate with soda lime?",
                        "options": [
                            "Water",
                            "Carbon(IV) oxide",
                            "Sodium carbonate",
                            "Calcium carbonate"
                        ],
                        "answer": "C",
                        "explanation": "Equation: $CH_3COONa(s) + NaOH(s) \\xrightarrow{\\text{CaO, heat}} CH_4(g) + Na_2CO_3(s)$. Solid sodium carbonate is the co-product."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Alkane Properties",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Alkane Properties\n- **Preparation**: Decarboxylation of carboxylate salts with soda lime ($NaOH + CaO$).\n- **Combustion**: Clean blue flame in excess $O_2$; toxic $CO$ and soot in limited $O_2$.\n- **Substitution**: Halogenation requires UV light to generate free radicals."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 3.4: Alkenes (Nomenclature, Structure, and Isomerism)",
            "unit_order": 4,
            "lesson_title": "Alkenes (Nomenclature, Structure, and Isomerism)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of the Double Bond",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore alkenes (unsaturated hydrocarbons with carbon-carbon double bonds, $\\text{C}=\\text{C}$), master their IUPAC nomenclature, and draw positional and chain isomers."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Fruit-Ripening Gas",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When green bananas are enclosed in a bag with a ripe avocado in a Nairobi market, they turn sweet and yellow in two days. The trigger is **ethene ($C_2H_4$)**, a natural plant hormone gas.\n\nEthene is also the precursor to polythene plastic. Its high reactivity stems from a single feature: the **carbon-carbon double bond ($C=C$)**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Unsaturation and the Carbon-Carbon Double Bond",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Anatomy of a Double Bond:\n* **Sigma ($\\sigma$) and Pi ($\\pi$) Bonds**: The double bond consists of one strong $\\sigma$ bond and one weaker, exposed $\\pi$ bond.\n* **High Electron Density**: The $\\pi$ electron cloud above and below the molecular plane makes alkenes nucleophilic and readily attacked by reagents.\n* **Unsaturation**: General formula **$C_nH_{2n}$ ($n \\ge 2$)**. Alkenes contain fewer hydrogens than corresponding alkanes, allowing addition of new atoms across the double bond."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "IUPAC Nomenclature for Alkenes",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Alkene Naming Rules",
                        "content": "### Systematic IUPAC Rules:\n1. **Parent Chain**: Must contain both carbons of the $C=C$ double bond (suffix **-ene**).\n2. **Priority Numbering**: Number from the end closest to the double bond (the functional group has priority over alkyl branches).\n3. **Locant Positioning**: Use the lower carbon number to indicate double bond position (e.g. $\\text{but-1-ene}$, $\\text{but-2-ene}$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Positional and Branching Isomerism in Alkenes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Alkenes ($C_4+$) exhibit two forms of structural isomerism:\n\n* **Positional Isomerism** (Shifting double bond along chain):\n  - $\\text{But-1-ene}$: $CH_2=CH-CH_2-CH_3$\n  - $\\text{But-2-ene}$: $CH_3-CH=CH-CH_3$\n\n* **Branching Isomerism** (Rearranging carbon skeleton):\n  - $\\text{2-Methylprop-1-ene}$: $CH_2=C(CH_3)-CH_3$"
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Constructing All Isomers of Pentene",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Draw and systematically name all structural isomers of pentene ($C_5H_{10}$).",
                        "steps": [
                            "**Straight-Chain Isomers (5 Carbons)**:\n1. $CH_2=CH-CH_2-CH_2-CH_3 \\implies \\mathbf{pent\\text{-}1\\text{-}ene}$\n2. $CH_3-CH=CH-CH_2-CH_3 \\implies \\mathbf{pent\\text{-}2\\text{-}ene}$",
                            "**Branched-Chain Isomers (4 Carbons in parent)**:\n3. $CH_2=C(CH_3)-CH_2-CH_3 \\implies \\mathbf{2\\text{-}methylbut\\text{-}1\\text{-}ene}$\n4. $CH_2=CH-CH(CH_3)-CH_3 \\implies \\mathbf{3\\text{-}methylbut\\text{-}1\\text{-}ene}$\n5. $CH_3-C(CH_3)=CH-CH_3 \\implies \\mathbf{2\\text{-}methylbut\\text{-}2\\text{-}ene}$",
                            "**Total Count**: Pentene has 5 structural isomers."
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Why \"Methene\" Does Not Exist",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does the alkene series start at $n=2$ instead of $n=1$?\nA carbon-carbon double bond ($C=C$) requires **at least two carbon atoms** sharing four electrons.\n\nSince a single carbon cannot form a double bond with itself, there is no one-carbon alkene."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Alkene Isomerism",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the systematic IUPAC name for $CH_3-C(CH_3)=CH-CH_3$?",
                        "options": [
                            "2-methylbut-2-ene",
                            "3-methylbut-2-ene",
                            "2-methylbut-3-ene",
                            "Pent-2-ene"
                        ],
                        "answer": "A",
                        "explanation": "The 4-carbon chain contains a double bond at C2 (butene). Numbering from the left gives the methyl group position 2, yielding 2-methylbut-2-ene."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Alkene Structure",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Alkenes\n- **General Formula**: $C_nH_{2n}$ ($n \\ge 2$).\n- **Functional Group**: Reactive $C=C$ double bond (one $\\sigma$ and one $\\pi$ bond).\n- **Isomerism**: Positional and branched structural isomers occur starting at $C_4H_8$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 3.5: Preparation and Chemical Properties of Alkenes (Addition Reactions)",
            "unit_order": 5,
            "lesson_title": "Preparation and Chemical Properties of Alkenes (Addition Reactions)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Saturated Fats vs Unsaturated Oils",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will examine the laboratory preparation of ethene by dehydration of ethanol, and discover how electrophilic addition reactions across the double bond distinguish alkenes from alkanes."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of Cooking Oils and Margarine",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Adding reddish-brown bromine water to yellow liquid vegetable oil decolourizes it instantly, whereas adding it to solid animal fat leaves the color unchanged.\n\nVegetable oils contain carbon-carbon double bonds that readily add bromine across the bond, while saturated animal fats cannot undergo addition. In this module, we prepare ethene and explore these addition reactions."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Preparation of Ethene",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Dehydration of Ethanol:\n1. **Acid Dehydration** ($170^\\circ\\text{C}$):\n   $$C_2H_5OH(l) \\xrightarrow[170^\\circ\\text{C}]{\\text{conc. } H_2SO_4} C_2H_4(g) + H_2O(l)$$\n   - **Sand Bath**: Ensures uniform heating to prevent flask cracking.\n   - **Broken Porcelain**: Prevents violent bumping.\n   - **$NaOH$ Wash Bottle**: Neutralizes acidic $CO_2$ and $SO_2$ impurities formed from acid reduction.\n   - **Collection**: Collected over water.\n\n2. **Catalytic Dehydration over Aluminium Oxide**:\n   $$C_2H_5OH(g) \\xrightarrow{\\text{Al}_2\\text{O}_3\\text{, heat}} C_2H_4(g) + H_2O(g)$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Ethene Laboratory Preparation Setup",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "purpose": "Experimental setup for dehydration of ethanol to ethene gas.",
                        "instruction": "Round-bottomed flask on sand bath containing ethanol and concentrated H2SO4 with thermometer at 170°C. Delivery tube leads to wash bottle containing NaOH solution, then to beehive shelf collecting ethene over water.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    },
                    "asset_info": {
                        "title": "Ethene Preparation Apparatus",
                        "description": "Apparatus diagram for ethanol dehydration to produce ethene gas.",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Diffusion_of_ammonia_and_hydrogen_chloride.jpg/800px-Diffusion_of_ammonia_and_hydrogen_chloride.jpg"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Addition Reactions: Halogenation & Hydrogenation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "The weaker $\\pi$ bond breaks to add two atoms across the carbons:\n\n* **Halogenation (Test for Unsaturation)**:\n  $$CH_2=CH_2 + Br_2(aq) \\rightarrow CH_2Br-CH_2Br \\quad (\\text{Colourless 1,2-dibromoethane})$$\n  *Diagnostic Observation*: Reddish-brown bromine water turns colourless instantly without light.\n\n* **Hydrogenation (Manufacture of Margarine)**:\n  $$CH_2=CH_2 + H_2 \\xrightarrow[180^\\circ\\text{C}]{\\text{Nickel}} CH_3-CH_3$$\n  *Application*: Hydrogenating liquid vegetable oils saturates double bonds, raising melting points into solid margarine."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Predicting Alkene Addition Products",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Predict the structural formula and systematic IUPAC name of the organic product formed when propene ($CH_3-CH=CH_2$) reacts with: (a) Bromine water ($Br_2(aq)$), (b) Gaseous hydrogen chloride ($HCl(g)$).",
                        "steps": [
                            "**Part (a): Reaction with Bromine**:\n- Addition occurs across the double bond: $CH_3-CH=CH_2 + Br_2 \\rightarrow CH_3-CHBr-CH_2Br$\n- IUPAC Name: **1,2-dibromopropane**",
                            "**Part (b): Reaction with Hydrogen Chloride**:\n- Hydrogen and chlorine add across the double bond: $CH_3-CH=CH_2 + HCl \\rightarrow CH_3-CHCl-CH_3$\n- IUPAC Name: **2-chloropropane**"
                        ]
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Think About This: Addition vs Substitution",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### How do bromine reactions distinguish alkanes from alkenes?\n* **Alkenes**: Undergo **addition**, decolourizing bromine water instantly in the dark at room temperature.\n* **Alkanes**: Undergo **substitution**, requiring intense UV light and proceeding much more slowly."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Alkene Reactions",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the primary function of passing ethene gas through sodium hydroxide solution during laboratory preparation?",
                        "options": [
                            "To dry the ethene gas",
                            "To absorb unreacted ethanol vapor",
                            "To remove acidic carbon(IV) oxide and sulfur(IV) oxide impurities",
                            "To catalyze hydrogenation"
                        ],
                        "answer": "C",
                        "explanation": "Hot concentrated sulphuric acid oxidizes ethanol to carbon oxides while being reduced to sulfur(IV) oxide ($SO_2$). Passing the gas through $NaOH$ neutralizes and removes these acidic impurities."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Alkene Reactions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Alkene Reactions\n- **Preparation**: Dehydration of ethanol at $170^\\circ\\text{C}$ with conc. $H_2SO_4$ or hot $\\text{Al}_2\\text{O}_3$.\n- **Addition Reactions**: Halogenation ($Br_2$), Hydrogenation ($H_2/Ni$ at $180^\\circ\\text{C}$), Hydrohalogenation ($HX$), Hydration ($H_2O$).\n- **Diagnostic Tests**: Decolourization of bromine water and acidified $KMnO_4$."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 3.6: Alkynes (Nomenclature, Preparation, and Properties)",
            "unit_order": 6,
            "lesson_title": "Alkynes (Nomenclature, Preparation, and Properties)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Intense Heat from the Triple Bond",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore alkynes (unsaturated hydrocarbons with carbon-carbon triple bonds, $\\text{C}\\equiv\\text{C}$), study the laboratory preparation of ethyne from calcium dicarbide, and investigate its distinctive combustion and addition reactions."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Oxy-Acetylene Welding in Kenya",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In metal fabrication workshops in **Gikomba (Nairobi), Mwembe Tayari (Mombasa), and Kondele (Kisumu)**, welders use gas torches producing blinding blue flames over $3000^\\circ\\text{C}$ to cut steel plates.\n\nThis extreme heat is generated by burning **ethyne (acetylene)** in pure oxygen: the oxy-acetylene flame."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Structure and Nomenclature of Alkynes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Triple Bond Functional Group:\n* **Bonding**: Contains one strong $\\sigma$ bond and two weaker $\\pi$ bonds ($-C\\equiv C-$).\n* **Geometry**: Linear geometry with a $180^\\circ$ bond angle.\n* **General Formula**: **$C_nH_{2n-2}$ ($n \\ge 2$)** (Ethyne: $C_2H_2$, Propyne: $C_3H_4$, Butyne: $C_4H_6$).\n* **IUPAC Suffix**: **-yne** with lowest position numbers (e.g. $\\text{but-1-yne}$, $\\text{but-2-yne}$)."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Laboratory Preparation of Ethyne",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Preparation of Ethyne",
                        "content": "### Reaction with Calcium Carbide:\n$$CaC_2(s) + 2H_2O(l) \\rightarrow C_2H_2(g) + Ca(OH)_2(aq)$$\n\n### Experimental Safety Protocol:\n* **Violent Exothermic Reaction**: Releases intense heat rapidly.\n* **Protective Sand Layer**: A layer of clean sand is placed at the bottom of the flask to absorb thermal shock and prevent the glass from shattering."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Combustion of Alkynes: Smoky Air vs Oxy-Acetylene",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### Combustion Behavior:\n* **In Atmospheric Air (Luminous, Smoky Flame)**:\n  Due to a high carbon-to-hydrogen ratio, ethyne burns incompletely in air, producing yellow flames with heavy black soot:\n  $$2C_2H_2(g) + 5O_2(g) \\rightarrow 4CO_2(g) + 2H_2O(l)$$\n* **In Pure Oxygen (Oxy-Acetylene Flame)**:\n  Complete combustion in pressurized oxygen releases enormous energy, exceeding $3000^\\circ\\text{C}$ for industrial steel welding and cutting."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Two-Stage Addition Reactions of Alkynes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Because alkynes contain two $\\pi$ bonds, addition occurs in two successive steps:\n\n* **Bromination**:\n  - Stage 1: $CH\\equiv CH + Br_2 \\rightarrow CHBr=CHBr \\quad (\\text{1,2-dibromoethene})$\n  - Stage 2: $CHBr=CHBr + Br_2 \\rightarrow CHBr_2-CHBr_2 \\quad (\\text{1,1,2,2-tetrabromoethane})$\n\n* **Hydrogenation** ($Ni$ catalyst at $200^\\circ\\text{C}$):\n  - Stage 1: $C_2H_2 + H_2 \\rightarrow C_2H_4 \\quad (\\text{Ethene})$\n  - Stage 2: $C_2H_4 + H_2 \\rightarrow C_2H_6 \\quad (\\text{Ethane})$"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Determining Formula of Unknown Hydrocarbon Y",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "An organic gas $Y$ contains 92.3% carbon and 7.7% hydrogen by mass with $M_r = 26.0$. Determine its empirical and molecular formulas ($C=12.0, H=1.0$).",
                        "steps": [
                            "**Step 1: Empirical Formula Calculation**:\n- Moles of $C = \\frac{92.3}{12.0} = 7.69$; Moles of $H = \\frac{7.7}{1.0} = 7.70$\n- Mole ratio $7.69 : 7.70 = 1 : 1 \\implies \\text{Empirical Formula: } CH$",
                            "**Step 2: Molecular Formula Determination**:\n- Empirical mass of $CH = 12.0 + 1.0 = 13.0$\n- Multiplier $n = \\frac{M_r}{\\text{Empirical Mass}} = \\frac{26.0}{13.0} = 2$\n- Molecular Formula $= (CH)_2 = \\mathbf{C_2H_2} \\quad (\\text{Ethyne})$"
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Alkynes",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the final saturated organic product formed when excess bromine water reacts with ethyne?",
                        "options": [
                            "1,2-dibromoethane",
                            "1,2-dibromoethene",
                            "1,1,2,2-tetrabromoethane",
                            "Bromoethane"
                        ],
                        "answer": "C",
                        "explanation": "Ethyne adds two successive moles of bromine across the triple bond: $C_2H_2 + 2Br_2 \\rightarrow CHBr_2-CHBr_2$ (1,1,2,2-tetrabromoethane)."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Alkynes",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Alkynes\n- **General Formula**: $C_nH_{2n-2}$ ($n \\ge 2$).\n- **Functional Group**: Linear $-C\\equiv C-$ triple bond (one $\\sigma$ and two $\\pi$ bonds).\n- **Preparation**: $CaC_2 + 2H_2O \\rightarrow C_2H_2 + Ca(OH)_2$ (sand buffer required).\n- **Reactions**: Smoky combustion in air, $>3000^\\circ\\text{C}$ in oxygen, two-stage addition."
                    }
                }
            ]
        },

        {
            "unit_name": "Module 3.7: Industrial Applications of Hydrocarbons (Cracking and Polymerisation)",
            "unit_order": 7,
            "lesson_title": "Industrial Applications of Hydrocarbons (Cracking and Polymerisation)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Transforming Crude Oil into Modern Materials",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "In this module, you will explore industrial petroleum refining, comparing thermal and catalytic cracking, and study addition polymerisation to understand how synthetic plastics like polythene and PVC are formed."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Petrochemical Revolution",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "From PVC water pipes and plastic packaging to synthetic polyester fabrics and high-octane petrol, modern life is built on petrochemical transformations.\n\nCrude oil is a dark, viscous mixture of mostly long-chain hydrocarbons. Chemical engineers transform this unrefined mixture into valuable fuels and modern plastics using **Cracking** and **Polymerisation**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Market Demand and Cracking of Alkanes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "### The Supply-Demand Mismatch:\nCrude oil yields an excess of heavy, long-chain fractions ($C_{20}-C_{70}$) with low commercial demand, while market demand is highest for short-chain petrol ($C_5-C_{10}$) and reactive alkene monomers ($C_2-C_4$).\n\n### Cracking Types:\n* **Thermal Cracking**: $450^\\circ\\text{C}-700^\\circ\\text{C}$, high pressure, no catalyst (high alkene yield).\n* **Catalytic Cracking**: $400^\\circ\\text{C}-500^\\circ\\text{C}$, zeolite/silica-alumina catalyst (produces high-quality petrol and hydrogen gas for Haber ammonia synthesis).\n* **Example Equation**: $$C_{10}H_{22}(l) \\xrightarrow{\\text{catalyst, heat}} C_8H_{18}(l) + C_2H_4(g)$$"
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Addition Polymerisation of Alkenes",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Polymerisation Principles",
                        "content": "### Definition\nThe chemical process of linking thousands of small molecules (**monomers**) into a single giant macromolecule (**polymer**).\n\n### Addition Polymerisation Mechanism:\nMonomers containing $C=C$ double bonds join without eliminating any atoms. The weaker $\\pi$ bonds break, forming a continuous saturated carbon backbone:\n$$n(\\text{Monomer}) \\xrightarrow{\\text{heat, pressure, initiator}} -[-\\text{Repeating Unit}-]-_n$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Key Industrial Polymers: Polyethene and PVC",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Important Addition Polymers",
                        "content": "### 1. Polyethene (Polythene):\n* **Monomer**: Ethene ($CH_2=CH_2$)\n* **Equation**: $$nCH_2=CH_2 \\rightarrow -[-\\text{CH}_2-\\text{CH}_2-]-_n$$\n* **Uses**: Plastic bags, squeeze bottles, packaging films.\n\n### 2. Polyvinyl Chloride (PVC / Polychloroethene):\n* **Monomer**: Chloroethene ($CH_2=CHCl$)\n* **Equation**: $$nCH_2=CHCl \\rightarrow -[-\\text{CH}_2-\\text{CH(Cl)}-]-_n$$\n* **Uses**: Municipal water pipes, electrical cable insulation, rainwear."
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Environmental Impact of Synthetic Plastics",
                    "block_type": "real_world_example",
                    "component_type": "real_world_example",
                    "content": {
                        "text": "### Non-Biodegradability and Pollution\nSynthetic addition polymers like polythene and PVC are **non-biodegradable**; microbial decomposers cannot break the strong $C-C$ backbone, leading to soil degradation and clogged urban drainage.\n\n*Incineration Hazard*: Burning PVC releases toxic hydrogen chloride ($HCl$) gas and dioxins. Kenya's ban on single-use plastic bags represents an environmental milestone in combating plastic pollution."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Calculating Degree of Polymerisation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A PVC polymer chain has a relative molecular mass of $125,000$. Determine the degree of polymerisation ($n$) ($H=1.0, C=12.0, Cl=35.5$).",
                        "steps": [
                            "**Step 1: Monomer Molecular Mass ($M_r$)**:\n$$M_r(CH_2=CHCl) = 2(12.0) + 3(1.0) + 35.5 = 24.0 + 3.0 + 35.5 = 62.5$$",
                            "**Step 2: Calculate Monomer Count ($n$)**:\n$$\\text{Mass of Polymer} = n \\times M_r(\\text{Monomer})$$\n$$125,000 = n \\times 62.5 \\implies n = \\frac{125,000}{62.5} = 2000$$",
                            "**Interpretation**: The polymer chain contains exactly 2000 linked chloroethene monomer units."
                        ]
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Practice Questions: Petrochemicals",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What does 'n' represent in the polymerisation equation $n(CH_2=CH_2) \\rightarrow -[-\\text{CH}_2-\\text{CH}_2-]-_n$?",
                        "options": [
                            "The number of carbon atoms in a single monomer",
                            "The reaction temperature in degrees Celsius",
                            "The degree of polymerisation (number of linked monomer units)",
                            "The volume of ethene gas in litres"
                        ],
                        "answer": "C",
                        "explanation": "The integer $n$ represents the degree of polymerisation—the number of repeating monomer units joined to form the macromolecule."
                    }
                },
                {
                    "page_number": 8,
                    "page_title": "Key Takeaways: Industrial Hydrocarbons",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Core Principles: Cracking & Polymerisation\n- **Cracking**: Breaking heavy alkanes into lighter alkanes, alkenes, and hydrogen gas.\n- **Addition Polymerisation**: $C=C$ bonds open to form saturated macromolecular chains (Polyethene, PVC).\n- **Formula**: $\\text{Polymer } M_r = n \\times \\text{Monomer } M_r$."
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
            block_id = f"f3_chem_t3_l{lesson.id}_b{order}_{uuid.uuid4().hex[:6]}"
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
    print("Ingestion Completed Successfully! All 7 Modules Published to Form 3 Topic 3.")
    print("================================================================================")

if __name__ == "__main__":
    ingest_form3_topic3_organic()
