import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_humanize_organic_all():
    print("Executing full humanization for Organic Chemistry I (Lessons 174 - 179)...")

    topic_24 = Topic.objects.get(id=24)

    lessons_payload = {
        # =====================================================================
        # LESSON 174: ALKANES NOMENCLATURE & ISOMERISM
        # =====================================================================
        174: {
            "topic": topic_24,
            "title": "Alkanes (Nomenclature, Structure, and Isomerism)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Architecture of Alkanes",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will master IUPAC systematic naming for straight and branched alkanes, understand structural isomerism using intuitive Lego-block models, and draw structural formulas accurately."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Saturated Single-Bond Family",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Alkanes are the simplest family of organic compounds, often called **paraffins** (meaning \"little affinity\" because they are chemically unreactive).\n\nEvery carbon atom forms 4 single covalent bonds, holding the maximum possible number of hydrogen atoms. Because there are no double or triple bonds, alkanes are **saturated**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "What is an Isomer? (The Lego Block Analogy)",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine you have 4 black Lego blocks (Carbon) and 10 white Lego blocks (Hydrogen). You can connect them in a straight row of 4 blocks (**butane**), OR you can connect 3 in a row and attach the 4th block as a side branch (**2-methylpropane**).\n\nBoth shapes use the exact same blocks ($\\text{C}_4\\text{H}_{10}$), but they have different structures and different boiling points! This phenomenon is called **Structural Isomerism**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Butane vs 2-Methylpropane Isomers",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Side-by-side structural diagrams comparing Butane (straight chain of 4 carbons) and 2-Methylpropane (branched chain of 3 carbons with a methyl group on carbon 2), both sharing molecular formula C4H10.",
                        "caption": "Structural Isomerism: Butane (unbranched, bp 0°C) and 2-methylpropane (branched, bp -12°C) share the formula C4H10."
                    },
                    "asset_info": {
                        "title": "Alkane Isomer Structural Comparison",
                        "description": "Comparative structural formula diagram of butane and 2-methylpropane.",
                        "ai_instruction": "Create side-by-side structural formulas of butane and 2-methylpropane highlighting the branch on carbon 2."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "IUPAC Naming in 3 Simple Steps (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "IUPAC Alkane Naming",
                        "content": "### How to Name Any Alkane in 3 Easy Steps:\n\n1. **Step 1: Find the Longest Carbon Chain (The Surname)**:\n   - $1\\text{ Carbon}$: meth- $\\rightarrow$ methane\n   - $2\\text{ Carbons}$: eth- $\\rightarrow$ ethane\n   - $3\\text{ Carbons}$: prop- $\\rightarrow$ propane\n   - $4\\text{ Carbons}$: but- $\\rightarrow$ butane\n   - $5\\text{ Carbons}$: pent- $\\rightarrow$ pentane\n\n2. **Step 2: Number the Chain from the End Nearest a Branch**:\n   - Give the branch the lowest possible position number (e.g. 2- rather than 3-).\n\n3. **Step 3: Name the Branch (The Prefix)**:\n   - $-\\text{CH}_3$ branch = **methyl**\n   - $-\\text{C}_2\\text{H}_5$ branch = **ethyl**\n   - *Example*: A methyl branch on carbon 2 of a 4-carbon chain is **2-methylbutane**!"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Naming Branched Hydrocarbons",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Give the IUPAC systematic name for the branched hydrocarbon with structural formula $\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\text{CH}_2-\\text{CH}_3$.",
                        "steps": [
                            "**1. Step 1: Find the Longest Continuous Carbon Chain**\n- Counting carbons in a continuous line gives **4 carbons**.\n- Therefore, the parent alkane name is **butane**.",
                            "**2. Step 2: Number the Chain to Give the Branch the Lowest Number**\n- Numbering from the left: The branch is on **Carbon 2**.\n- Numbering from the right: The branch would be on Carbon 3.\n- We choose the lowest number: **2**.",
                            "**3. Step 3: Identify the Branch Group**\n- The branch is a single carbon group ($-\\text{CH}_3$), which is a **methyl** group.",
                            "**4. Assemble the Full Name**\n- Position + Branch + Parent = **2-methylbutane**."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Straight vs Bent Chains",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Is drawing a chain in a zig-zag or bent shape a new isomer?\n**NO!**\n\nThink of a flexible beaded necklace: Whether you lay the necklace in a straight line or bend it into an \"L\" or \"U\" shape on the table, it is still the exact same single strand of beads!\n\nA true isomer only forms when you physically disconnect a carbon atom and reconnect it to the middle of the chain."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Alkane IUPAC Naming",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the systematic IUPAC name for $(\\text{CH}_3)_3\\text{C}-\\text{CH}_3$ (a central carbon bonded to four methyl groups)?",
                        "options": [
                            "Pentane",
                            "2,2-dimethylpropane",
                            "2-methylbutane",
                            "Tetramethylmethane"
                        ],
                        "answer": "B",
                        "explanation": "The longest continuous chain contains 3 carbons (propane). Carbon 2 holds two separate methyl branches, giving 2,2-dimethylpropane."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Isomer Count of Pentane",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "How many structural isomers exist for pentane ($\\text{C}_5\\text{H}_{12}$)?",
                        "options": [
                            "2",
                            "3",
                            "4",
                            "5"
                        ],
                        "answer": "B",
                        "explanation": "Pentane has exactly 3 structural isomers: pentane (straight chain), 2-methylbutane (1 branch), and 2,2-dimethylpropane (2 branches)."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Alkane Structure & Naming",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Alkanes\n- **General Formula**: $\\text{C}_n\\text{H}_{2n+2}$ (saturated single bonds).\n- **Isomers**: Same molecular formula, different structural connectivity.\n- **Naming Rules**: Longest chain $\\rightarrow$ Number nearest branch $\\rightarrow$ Add prefix."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 175: ALKANE PREPARATION & CHEMICAL PROPERTIES
        # =====================================================================
        175: {
            "topic": topic_24,
            "title": "Laboratory Preparation and Chemical Properties of Alkanes",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Clean Energy from Methane",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand how methane is prepared in the school laboratory by decarboxylation, explain complete versus incomplete combustion, and describe substitution reactions with halogens in UV light."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Biogas: Kenya's Renewable Energy Source",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In rural Kenya, methane gas ($\\text{CH}_4$) is produced naturally in farm biogas digesters when bacteria digest cow dung without oxygen. Methane burns with a clean, hot, non-sooty blue flame, providing renewable energy for cooking without cutting down trees!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Preparation by Decarboxylation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In the laboratory, methane is prepared by heating a dry solid mixture of **sodium ethanoate** with **soda lime** (a mixture of $\\text{NaOH}$ and $\\text{CaO}$):\n$$\\mathbf{\\text{CH}_3\\text{COONa}_{(s)} + \\text{NaOH}_{(s)} \\xrightarrow{\\text{CaO}, \\Delta} \\text{CH}_{4(g)} + \\text{Na}_2\\text{CO}_{3(s)}}$$\n\n* **Why is Soda Lime used instead of pure Sodium Hydroxide?**\n  Pure $\\text{NaOH}$ absorbs water vapor from air, melts easily, and violently attacks/corrodes the laboratory glassware. Calcium oxide ($\\text{CaO}$) keeps the mixture dry, porous, and prevents glass etching!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Methane Laboratory Preparation Apparatus",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Apparatus diagram showing hard glass test tube clamped horizontally holding solid sodium ethanoate and soda lime mixture heated by Bunsen flame, with delivery tube leading to downward displacement of water collection trough.",
                        "caption": "Laboratory Preparation of Methane: Solid sodium ethanoate and soda lime are heated, and methane gas is collected over water."
                    },
                    "asset_info": {
                        "title": "Methane Lab Preparation Setup",
                        "description": "Experimental setup for preparing methane by decarboxylation and collection over water.",
                        "ai_instruction": "Illustrate a horizontal test tube with solid reactants heated by Bunsen burner, with delivery tube collecting methane gas over a water trough."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Chemical Reactions of Alkanes (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Alkane Reactions",
                        "content": "### 1. Complete Combustion (Excess Air)\nBurns cleanly with a hot blue flame to make carbon dioxide and steam:\n$$\\text{CH}_{4(g)} + 2\\text{O}_{2(g)} \\rightarrow \\text{CO}_{2(g)} + 2\\text{H}_2\\text{O}_{(g)} + \\text{Heat}$$\n\n### 2. Incomplete Combustion (Limited Air)\nBurns with a yellow sooty flame producing deadly, odorless carbon monoxide gas:\n$$2\\text{CH}_{4(g)} + 3\\text{O}_{2(g)} \\rightarrow 2\\text{CO}_{(g)} + 4\\text{H}_2\\text{O}_{(g)}$$\n\n### 3. Substitution Reaction with Chlorine (in UV Light)\nIn ultraviolet light, chlorine atoms substitute hydrogen atoms one-by-one:\n$$\\text{CH}_4 + \\text{Cl}_2 \\xrightarrow{\\text{UV}} \\text{CH}_3\\text{Cl} + \\text{HCl} \\rightarrow \\dots \\rightarrow \\text{CCl}_4$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Calculating Oxygen Volume for Combustion",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of oxygen gas at r.t.p. required for the complete combustion of $32.0\\text{ g}$ of methane gas. ($A_r$: $\\text{C}=12.0, \\text{H}=1.0, V_m = 24.0\\text{ dm}^3\\text{/mol}$).",
                        "steps": [
                            "**1. Step 1: Find Moles of Methane**\n- Molar mass of $\\text{CH}_4 = 12.0 + 4(1.0) = 16.0\\text{ g/mol}$\n$$n(\\text{CH}_4) = \\frac{32.0\\text{ g}}{16.0\\text{ g/mol}} = 2.0\\text{ moles}$$",
                            "**2. Step 2: Use Stoichiometric Mole Ratio from Equation**\n- Equation: $\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}$\n- Mole ratio $\\text{CH}_4 : \\text{O}_2 = 1 : 2$\n$$n(\\text{O}_2) = 2 \\times 2.0\\text{ mol} = 4.0\\text{ moles of } \\text{O}_2$$",
                            "**3. Step 3: Convert Moles to Gas Volume at r.t.p.**\n$$V(\\text{O}_2) = 4.0\\text{ mol} \\times 24.0\\text{ dm}^3\\text{/mol} = 96.0\\text{ dm}^3$$\n- **Result**: Exactly $96.0\\text{ dm}^3$ of oxygen gas is required."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Sunlight is Required for Substitution",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why won't methane react with chlorine in the dark?\nIn the dark, chlorine molecules ($\\text{Cl}_2$) are stable and unreactive toward saturated alkanes. Sunlight or UV radiation provides the specific photon energy needed to split the $\\text{Cl}-\\text{Cl}$ bond into highly reactive chlorine free radicals ($\\text{Cl}^\\bullet$)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Soda Lime Decarboxylation",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which gas is collected when anhydrous sodium propanoate is heated with soda lime?",
                        "options": [
                            "Methane ($\\text{CH}_4$)",
                            "Ethane ($\\text{C}_2\\text{H}_6$)",
                            "Propane ($\\text{C}_3\\text{H}_8$)",
                            "Ethene ($\\text{C}_2\\text{H}_4$)"
                        ],
                        "answer": "B",
                        "explanation": "Decarboxylation removes the carboxylate carbon, producing an alkane with ONE LESS carbon than the salt: $\\text{C}_2\\text{H}_5\\text{COONa} + \\text{NaOH} \\rightarrow \\text{C}_2\\text{H}_6 + \\text{Na}_2\\text{CO}_3$ (ethane)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Chlorine Substitution Condition",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Under what condition will methane react with chlorine gas in a substitution reaction?",
                        "options": [
                            "In total darkness at room temperature",
                            "In the presence of ultraviolet light or sunlight",
                            "In the presence of concentrated sulfuric acid catalyst",
                            "Under high pressure without light"
                        ],
                        "answer": "B",
                        "explanation": "Photochemical halogenation requires UV light or diffuse sunlight to break $\\text{Cl}_2$ into free radicals."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Alkane Reactions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Alkane Properties\n- **Preparation**: Decarboxylation of sodium alkanoate with soda lime.\n- **Combustion**: Complete (blue flame $\\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O}$); Incomplete (yellow flame $\\rightarrow \\text{CO} + \\text{C} + \\text{H}_2\\text{O}$).\n- **Substitution**: Halogens replace hydrogens step-by-step in UV light."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 176: ALKENES NOMENCLATURE & STRUCTURE
        # =====================================================================
        176: {
            "topic": topic_24,
            "title": "Alkenes (Nomenclature, Structure, and Isomerism)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of the Double Bond",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the reactive nature of the carbon-carbon double bond ($\\text{C}=\\text{C}$), master alkene IUPAC naming, and identify positional isomers (such as but-1-ene vs but-2-ene)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Fruit-Ripening Plant Hormone",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In fruit markets across Kenya, traders place a ripe passion fruit or banana inside a crate of green mangoes. Within two days, all the mangoes turn bright yellow and sweet! Why?\n\nRipe fruits naturally emit **ethene gas ($\\text{C}_2\\text{H}_4$)**, a natural plant hormone that triggers rapid ripening. Ethene is the first member of the **Alkene** family."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Reactive Double Bond ($\\text{C}=\\text{C}$)",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Alkenes contain at least one **carbon-carbon double bond ($\\text{C}=\\text{C}$)**.\n\n* **Why are Alkenes \"Unsaturated\"?**\n  Because of the double bond, the carbons are not holding the maximum number of hydrogens. The double bond consists of a strong $\\sigma$-bond and a weaker $\\pi$-bond. This weaker bond easily \"pops open\" like a spring-loaded latch to add new atoms, making alkenes **far more reactive than alkanes**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Alkene Positional Isomerism",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram comparing But-1-ene (double bond between carbon 1 and 2) versus But-2-ene (double bond between carbon 2 and 3), showing how the position of the double bond changes the isomer.",
                        "caption": "Positional Isomers: But-1-ene and But-2-ene share formula C4H8 but differ in double bond location."
                    },
                    "asset_info": {
                        "title": "Alkene Positional Isomerism Diagram",
                        "description": "Comparative structural diagram of but-1-ene and but-2-ene.",
                        "ai_instruction": "Create structural formulas for but-1-ene and but-2-ene highlighting double bond locations."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Alkene Naming Rules (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Alkene IUPAC Naming",
                        "content": "### How to Name Alkenes in 3 Easy Steps:\n\n1. **General Formula**: $\\mathbf{\\text{C}_n\\text{H}_{2n}}$ (starts at $n=2$, ethene).\n2. **Change Suffix to -ene** (ethene, propene, butene, pentene).\n3. **State the Number Where the Double Bond Starts**:\n   - Number the chain from the end that gives the double bond the **lowest possible number**!\n   - *Example*: $\\text{CH}_2=\\text{CH}-\\text{CH}_2-\\text{CH}_3$ is **but-1-ene**.\n   - *Example*: $\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$ is **but-2-ene**."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Naming Branched Alkenes",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Give the systematic IUPAC name for $\\text{CH}_2=\\text{C}(\\text{CH}_3)-\\text{CH}_3$.",
                        "steps": [
                            "**1. Step 1: Find Longest Chain Containing the Double Bond**\n- Longest continuous chain has 3 carbons $\\implies$ **propene**.",
                            "**2. Step 2: Number the Chain from the Double Bond End**\n- Double bond starts on Carbon 1.",
                            "**3. Step 3: Identify the Branch**\n- Carbon 2 holds a methyl group ($-\\text{CH}_3$).",
                            "**4. Assemble the Name**\n- **2-methylprop-1-ene** (or simply 2-methylpropene)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Methene Does Not Exist",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why is there no such thing as \"Methene\"?\nAn alkene requires a double bond **between two carbon atoms ($\\text{C}=\\text{C}$)**. Because methane has only one single carbon atom ($n=1$), it is physically impossible to form an alkene with one carbon! The alkene homologous series starts at $n=2$ (ethene)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Alkene Formula",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the molecular formula of an alkene containing 5 carbon atoms?",
                        "options": [
                            "$\\text{C}_5\\text{H}_{12}$",
                            "$\\text{C}_5\\text{H}_{10}$",
                            "$\\text{C}_5\\text{H}_8$",
                            "$\\text{C}_5\\text{H}_6$"
                        ],
                        "answer": "B",
                        "explanation": "Alkenes follow $\\text{C}_n\\text{H}_{2n}$. For $n=5$: $2(5) = 10 \\implies \\text{C}_5\\text{H}_{10}$ (pentene)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Positional Isomers",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which pair of compounds represents positional isomers?",
                        "options": [
                            "But-1-ene and but-2-ene",
                            "Butane and 2-methylpropane",
                            "Pentane and pent-1-ene",
                            "Ethene and ethane"
                        ],
                        "answer": "A",
                        "explanation": "But-1-ene and but-2-ene have the exact same carbon backbone, but differ in the position of the $\\text{C}=\\text{C}$ double bond."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Alkenes",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Alkenes\n- **General Formula**: $\\text{C}_n\\text{H}_{2n}$ ($n \\ge 2$).\n- **Functional Group**: Reactive $\\text{C}=\\text{C}$ double bond.\n- **Isomerism**: Positional isomers differ by where the double bond is located."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 177: ALKENE ADDITION REACTIONS
        # =====================================================================
        177: {
            "topic": topic_24,
            "title": "Preparation and Chemical Properties of Alkenes (Addition Reactions)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "Addition Reactions & The Unsaturation Test",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the laboratory preparation of ethene by dehydration of ethanol, master the chemical tests for unsaturation (bromine water and $\\text{KMnO}_4$), and explain hydrogenation in making margarine."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Making Blue Band Margarine: Hydrogenation",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Vegetable cooking oils (like sunflower or corn oil) are liquid alkenes with multiple double bonds. When hydrogen gas is bubbled through warm vegetable oil using a Nickel catalyst at $150^\\circ\\text{C}$, the double bonds open up and accept hydrogen atoms.\n\nThis turns the liquid oil into solid edible fat—the exact process used in Kenyan factories to manufacture **margarine and cooking fat**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Laboratory Preparation by Dehydration of Ethanol",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In the laboratory, ethene is prepared by heating ethanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$) with excess **concentrated sulfuric acid** at **$180^\\circ\\text{C}$**:\n$$\\mathbf{\\text{CH}_3\\text{CH}_2\\text{OH}_{(l)} \\xrightarrow{\\text{conc. H}_2\\text{SO}_4, 180^\\circ\\text{C}} \\text{CH}_2=\\text{CH}_{2(g)} + \\text{H}_2\\text{O}_{(l)}}$$\nConcentrated $\\text{H}_2\\text{SO}_4$ acts as a powerful **dehydrating agent**, stripping out the elements of water."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Dehydration of Ethanol Apparatus",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Apparatus diagram showing round-bottom flask containing ethanol and conc H2SO4 with thermometer at 180°C heated by Bunsen burner, passing through sodium hydroxide wash bottle (to remove SO2 and CO2 impurities) and collecting ethene gas over water.",
                        "caption": "Preparation of Ethene: Ethanol is dehydrated at 180°C and ethene gas is purified and collected over water."
                    },
                    "asset_info": {
                        "title": "Ethene Dehydration Setup",
                        "description": "Laboratory apparatus schematic for preparing ethene from ethanol and concentrated sulfuric acid.",
                        "ai_instruction": "Illustrate round-bottom flask with thermometer reading 180°C, delivery tube through NaOH wash bottle, and inverted gas jar over water."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Tests for Unsaturation (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Addition Reactions & Unsaturation Tests",
                        "content": "How do you prove in a lab test that a liquid is an alkene and not an alkane? Use these two tests:\n\n### 1. The Bromine Water Test (No Light Needed!)\n* **Observation**: Reddish-brown bromine water turns **completely colorless instantly**!\n* **Reaction**: $\\text{CH}_2=\\text{CH}_2 + \\text{Br}_2 \\rightarrow \\text{CH}_2\\text{Br}-\\text{CH}_2\\text{Br}$ (1,2-dibromoethane).\n\n### 2. Acidified Potassium Manganate(VII) Test\n* **Observation**: Purple $\\text{KMnO}_4$ solution turns **completely colorless**!\n* **Reaction**: Ethene is oxidized to ethane-1,2-diol (antifreeze glycol)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Bromine Addition Mass Calculation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the mass of bromine ($\\text{Br}_2$) required to react completely with $5.6\\text{ g}$ of ethene ($\\text{C}_2\\text{H}_4$). ($A_r$: $\\text{C}=12.0, \\text{H}=1.0, \\text{Br}=80.0$).",
                        "steps": [
                            "**1. Step 1: Find Moles of Ethene**\n- Molar mass of $\\text{C}_2\\text{H}_4 = 2(12.0) + 4(1.0) = 28.0\\text{ g/mol}$\n$$n = \\frac{5.6\\text{ g}}{28.0\\text{ g/mol}} = 0.20\\text{ moles}$$",
                            "**2. Step 2: Use Stoichiometric Mole Ratio ($1 : 1$)**\n- Equation: $\\text{C}_2\\text{H}_4 + \\text{Br}_2 \\rightarrow \\text{C}_2\\text{H}_4\\text{Br}_2$\n$$n(\\text{Br}_2) = 0.20\\text{ moles}$$",
                            "**3. Step 3: Convert Moles to Mass of Bromine**\n- Molar mass of $\\text{Br}_2 = 2(80.0) = 160.0\\text{ g/mol}$\n$$m(\\text{Br}_2) = 0.20\\text{ mol} \\times 160.0\\text{ g/mol} = 32.0\\text{ g}$$\n- **Result**: Exactly $32.0\\text{ g}$ of bromine is consumed."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Alkenes Don't Need UV Light",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does bromine react with alkenes in the dark, but needs sunlight for alkanes?\nAlkanes have strong single bonds, so bromine needs UV photons to break into radicals. In alkenes, the double bond's $\\pi$-cloud is rich in electrons and easily attacks the bromine molecule on contact without any light!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Dehydration Temperature",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What happens if ethanol is heated with concentrated sulfuric acid at $140^\\circ\\text{C}$ instead of $180^\\circ\\text{C}$?",
                        "options": [
                            "Ethene gas is produced at a faster rate.",
                            "Ethoxyethane (ether) is formed instead of ethene.",
                            "Carbon dioxide gas is liberated.",
                            "No reaction occurs at all."
                        ],
                        "answer": "B",
                        "explanation": "At $140^\\circ\\text{C}$ with excess ethanol, intermolecular dehydration produces diethyl ether ($2\\text{C}_2\\text{H}_5\\text{OH} \\rightarrow \\text{C}_2\\text{H}_5\\text{OC}_2\\text{H}_5 + \\text{H}_2\\text{O}$). Full dehydration to ethene requires $180^\\circ\\text{C}$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Bromine Water Color Change",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "When ethene gas is bubbled into reddish-brown bromine water in the dark, what is observed?",
                        "options": [
                            "The solution turns dark purple.",
                            "The reddish-brown solution turns completely colorless rapidly.",
                            "A white precipitate forms instantly.",
                            "No color change occurs without UV light."
                        ],
                        "answer": "B",
                        "explanation": "Ethene undergoes addition across the double bond, rapidly decolorizing reddish-brown bromine water to colorless 1,2-dibromoethane."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Alkene Reactions",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Alkene Reactions\n- **Preparation**: Dehydration of ethanol with conc. $\\text{H}_2\\text{SO}_4$ at $180^\\circ\\text{C}$.\n- **Addition Reactions**: Double bond opens to add $\\text{H}_2$ (margarine), $\\text{Br}_2$ (colorless test), or $\\text{H}_2\\text{O}$ (alcohols).\n- **Unsaturation Test**: Instant decolorization of bromine water and acidified $\\text{KMnO}_4$."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 178: ALKYNES
        # =====================================================================
        178: {
            "topic": topic_24,
            "title": "Alkynes (Nomenclature, Preparation, and Properties)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Super-Hot Welding Flame",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand the chemistry of the carbon-carbon triple bond ($\\text{C}\\equiv\\text{C}$), explain the laboratory preparation of ethyne from calcium carbide, and describe its role in oxy-acetylene welding."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Oxy-Acetylene Torches: Cutting Steel Like Butter",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "If you visit an industrial metal workshop in Nairobi or Mombasa, you will see metalworkers wearing dark goggles cutting through thick steel plates with a hissing blue flame.\n\nThat torch burns **ethyne gas (acetylene, $\\text{C}_2\\text{H}_2$)** mixed with pure oxygen. It burns at an astonishing temperature of over **$3300^\\circ\\text{C}$**—hot enough to melt through steel in seconds!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Preparation of Ethyne from Calcium Carbide",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In the laboratory, ethyne is prepared simply by dripping cold water onto solid grey lumps of **calcium carbide ($\\text{CaC}_2$)**:\n$$\\mathbf{\\text{CaC}_{2(s)} + 2\\text{H}_2\\text{O}_{(l)} \\rightarrow \\text{Ca(OH)}_{2(aq)} + \\text{C}_2\\text{H}_{2(g)}}$$\n\n* **Laboratory Observation**:\n  The reaction is vigorously effervescent and highly exothermic. Sand is placed at the bottom of the flask to absorb heat and prevent the glass from cracking!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Ethyne Generator Setup",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram showing dropping funnel dripping water onto grey calcium carbide solid on a layer of sand in a flat-bottomed flask, with gas passing through acidified copper(II) sulfate wash bottle (to remove phosphine and H2S impurities) and collecting ethyne gas over water.",
                        "caption": "Preparation of Ethyne: Water reacts with calcium carbide; gas is purified with CuSO4 solution and collected over water."
                    },
                    "asset_info": {
                        "title": "Ethyne Lab Generator Diagram",
                        "description": "Apparatus diagram for generating and purifying ethyne gas from calcium carbide.",
                        "ai_instruction": "Create a diagram showing dropping funnel dripping water onto CaC2 on sand layer, passing through CuSO4 wash bottle, and collecting over water."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Alkyne Properties & Reactions (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Alkyne Chemistry",
                        "content": "### 1. General Formula: $\\mathbf{\\text{C}_n\\text{H}_{2n-2}}$ (starts at $n=2$, ethyne)\n\n### 2. Combustion in Air vs Pure Oxygen:\n* **In Air**: Burns with a very **smoky, sooty yellow flame** because it has a high percentage of carbon ($92.3\\%$ carbon by mass).\n* **In Pure Oxygen**: Burns completely to give the intense **$3300^\\circ\\text{C}$ oxy-acetylene flame**.\n\n### 3. Two-Stage Addition Reactions:\nBecause an alkyne has a triple bond, it reacts in **two successive stages**:\n$$\\text{Alkyne } (\\text{C}\\equiv\\text{C}) \\xrightarrow{+\\text{Br}_2} \\text{Alkene } (\\text{C}=\\text{C}) \\xrightarrow{+\\text{Br}_2} \\text{Alkane } (\\text{C}-\\text{C})$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Ethyne Volume from Calcium Carbide",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of ethyne gas ($\\text{C}_2\\text{H}_2$) produced at r.t.p. when $6.4\\text{ g}$ of pure calcium carbide ($\\text{CaC}_2$) reacts completely with water. ($A_r$: $\\text{Ca}=40.0, \\text{C}=12.0$; $V_m = 24.0\\text{ dm}^3\\text{/mol}$).",
                        "steps": [
                            "**1. Step 1: Find Moles of $\\text{CaC}_2$**\n- Molar mass of $\\text{CaC}_2 = 40.0 + 2(12.0) = 64.0\\text{ g/mol}$\n$$n = \\frac{6.4\\text{ g}}{64.0\\text{ g/mol}} = 0.10\\text{ moles}$$",
                            "**2. Step 2: Use Equation Ratio ($1 : 1$)**\n- Equation: $\\text{CaC}_2 + 2\\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2 + \\text{C}_2\\text{H}_2$\n$$n(\\text{C}_2\\text{H}_2) = 0.10\\text{ moles}$$",
                            "**3. Step 3: Convert Moles to Volume at r.t.p.**\n$$V = 0.10\\text{ mol} \\times 24.0\\text{ dm}^3\\text{/mol} = 2.40\\text{ dm}^3\\text{ (or } 2400\\text{ cm}^3\\text{)}$$\n- **Result**: $2.40\\text{ dm}^3$ of ethyne gas is collected."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Sand is Put Under Calcium Carbide",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why must sand be placed in the flask before adding calcium carbide?\nAdding water to calcium carbide releases tremendous localized heat. If carbide touches the bare glass directly, the intense thermal shock will crack the bottom of the flask!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Alkyne General Formula",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the molecular formula of an alkyne containing 4 carbon atoms?",
                        "options": [
                            "$\\text{C}_4\\text{H}_{10}$",
                            "$\\text{C}_4\\text{H}_8$",
                            "$\\text{C}_4\\text{H}_6$",
                            "$\\text{C}_4\\text{H}_4$"
                        ],
                        "answer": "C",
                        "explanation": "Alkynes follow $\\text{C}_n\\text{H}_{2n-2}$. For $n=4$: $2(4) - 2 = 6 \\implies \\text{C}_4\\text{H}_6$ (butyne)."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Why Ethyne Burns Sootily in Air",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why does ethyne burn with a much sootier flame in air compared to ethene and ethane?",
                        "options": [
                            "Ethyne has a higher percentage of carbon by mass ($92.3\\%$), requiring more oxygen than is available in atmospheric air for complete combustion.",
                            "Ethyne contains oxygen impurities.",
                            "Ethyne does not react with oxygen at room pressure.",
                            "Ethyne produces carbon monoxide only."
                        ],
                        "answer": "A",
                        "explanation": "Ethyne contains $92.3\\%$ carbon by mass (compared to $85.7\\%$ in ethene and $80.0\\%$ in ethane). Atmospheric air cannot supply oxygen fast enough, leaving unburned glowing carbon soot particles."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Alkynes",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Alkynes\n- **General Formula**: $\\text{C}_n\\text{H}_{2n-2}$ (triple bond $\\text{C}\\equiv\\text{C}$).\n- **Preparation**: Water + Calcium Carbide ($\\text{CaC}_2$).\n- **Use**: Oxy-acetylene welding torches ($>3300^\\circ\\text{C}$)."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 179: CRACKING AND POLYMERISATION
        # =====================================================================
        179: {
            "topic": topic_24,
            "title": "Industrial Applications of Hydrocarbons (Cracking and Polymerisation)",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "From Crude Oil to Everyday Plastics",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand how fractional distillation separates crude oil, explain thermal and catalytic cracking, and describe addition polymerization in manufacturing plastic shopping bags and PVC pipes."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Wonder of Modern Plastics",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Look around you right now: your plastic ruler, drinking water bottle, electrical wire insulation, synthetic clothes, and water pipes are all made from **polymers**!\n\nAll of these materials originate from thick black crude oil pumped from the ground. Through chemical engineering, chemists break down large oil molecules (**Cracking**) and link the small fragments into long durable chains (**Polymerisation**)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Cracking: Breaking Big Molecules into High-Value Fuels",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Crude oil contains a large surplus of heavy, viscous, long-chain alkanes (like heavy fuel oil) for which there is very little consumer demand. Meanwhile, there is massive worldwide demand for petrol (gasoline) and ethene monomers.\n\n**Cracking** is the process of breaking long, heavy alkane molecules into shorter, useful petrol fractions and reactive alkenes:\n$$\\mathbf{\\text{C}_{10}\\text{H}_{22} \\xrightarrow{\\text{Catalyst, } 500^\\circ\\text{C}} \\text{C}_8\\text{H}_{18} \\text{ (Petrol)} + \\text{C}_2\\text{H}_4 \\text{ (Ethene Monomer)}}$$\n\n* **Thermal Cracking**: High temperature ($>700^\\circ\\text{C}$) and pressure.\n* **Catalytic Cracking**: Lower temperature ($500^\\circ\\text{C}$) using silica-alumina catalyst ($\\text{SiO}_2 / \\text{Al}_2\\text{O}_3$)."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Polymerization of Ethene to Polythene",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram showing thousands of individual ethene monomers (CH2=CH2) breaking their double bonds and linking head-to-tail to form a long poly(ethene) chain [-CH2-CH2-]n.",
                        "caption": "Addition Polymerization: Ethene monomers link head-to-tail into tough polythene plastic chains."
                    },
                    "asset_info": {
                        "title": "Addition Polymerization Mechanism",
                        "description": "Visual mechanism diagram of monomer double bonds opening to form continuous polymer chain.",
                        "ai_instruction": "Create a diagram showing 3 separate ethene molecules opening double bonds to link into a single continuous poly(ethene) chain."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "Addition Polymerisation (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Polymerisation Principles",
                        "content": "### What is a Polymer?\n*A giant macromolecule made by linking thousands of small repeating units (**monomers**) end-to-end like paperclips in a long chain.*\n\n---\n\n### Everyday Plastics You Use:\n1. **Poly(ethene) / Polythene**:\n   - *Monomer*: Ethene ($\\text{CH}_2=\\text{CH}_2$)\n   - *Uses*: Plastic shopping bags, squeeze bottles, food wrap.\n\n2. **Polychloroethene (PVC)**:\n   - *Monomer*: Chloroethene ($\\text{CH}_2=\\text{CHCl}$)\n   - *Uses*: Water pipes, electrical cable insulation, raincoats.\n\n3. **Polypropene**:\n   - *Monomer*: Propene ($\\text{CH}_2=\\text{CH}-\\text{CH}_3$)\n   - *Uses*: Ropes, plastic chairs, bottle crates."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Calculating Monomer Units in a Polymer",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "A sample of poly(ethene) plastic has an average Relative Molecular Mass ($M_r$) of $56,000$. How many ethene monomer units ($n$) are joined together in this polymer chain? ($A_r$: $\\text{C}=12.0, \\text{H}=1.0$).",
                        "steps": [
                            "**1. Step 1: Find Molecular Mass of One Ethene Monomer ($\\text{C}_2\\text{H}_4$)**\n- Monomer mass $= 2(12.0) + 4(1.0) = 28.0\\text{ g/mol}$",
                            "**2. Step 2: Divide Total Polymer Mass by Monomer Mass**\n$$n = \\frac{\\text{Total Molecular Mass of Polymer}}{\\text{Monomer Mass}} = \\frac{56000}{28.0} = 2000$$\n- **Result**: Exactly $2,000$ ethene molecules are joined together to make this single plastic chain."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why Plastics Don't Rot in Soil",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why are plastics non-biodegradable?\nNatural decomposers (bacteria and fungi) evolved over millions of years to break down natural bonds in wood and food. They do not possess enzymes capable of breaking the synthetic, inert carbon-carbon backbone of addition polymers!\n\nThis is why plastics persist in the environment for hundreds of years, making recycling and biodegradable alternatives essential in Kenya."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Monomer Identification",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which monomer is used to manufacture PVC (polychloroethene) water pipes?",
                        "options": [
                            "Ethene ($\\text{CH}_2=\\text{CH}_2$)",
                            "Chloroethene ($\\text{CH}_2=\\text{CHCl}$)",
                            "Propene ($\\text{CH}_2=\\text{CH}-\\text{CH}_3$)",
                            "Ethane ($\\text{CH}_3-\\text{CH}_3$)"
                        ],
                        "answer": "B",
                        "explanation": "PVC stands for Polyvinyl Chloride (or polychloroethene), made by polymerizing chloroethene monomers."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Cracking Catalyst",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What is the primary industrial catalyst used during catalytic cracking of heavy oil fractions?",
                        "options": [
                            "Vanadium(V) oxide",
                            "Silica-alumina ($\\text{SiO}_2 / \\text{Al}_2\\text{O}_3$)",
                            "Finely divided iron",
                            "Platinum gauze"
                        ],
                        "answer": "B",
                        "explanation": "Catalytic cracking uses synthetic zeolite or silica-alumina ($\\text{SiO}_2 / \\text{Al}_2\\text{O}_3$) catalysts at $\approx 500^\\circ\\text{C}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Cracking & Polymers",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Cracking & Polymers\n- **Cracking**: Breaking long-chain alkanes into petrol fractions and reactive alkene monomers.\n- **Addition Polymerisation**: Double bonds pop open to join thousands of monomers into giant plastic chains (e.g. polythene, PVC)."
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
    run_humanize_organic_all()
