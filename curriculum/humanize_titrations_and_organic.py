import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_humanize_titrations():
    print("Executing full humanization for Titrations (170-172) and Organic Chemistry (173-179)...")

    topic_23 = Topic.objects.get(id=23)
    topic_24 = Topic.objects.get(id=24)

    lessons_payload = {
        # =====================================================================
        # LESSON 170: VOLUMETRIC ANALYSIS (TITRATIONS)
        # =====================================================================
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
                        "text": "By the end of this module, you will understand the purpose of acid-base titration, correctly use pipettes and burettes, pick the right indicator for any reaction, and calculate unknown acid/base concentrations using the titration formula ($\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b}$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Quality Control in Food and Factories",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When a food manufacturer in Kenya bottles vinegar or fruit juice, government health inspectors require the exact acidity to be certified. How do chemists find the exact concentration of an unknown acid or alkali?\n\nThey use **Titration (Volumetric Analysis)**—a precision laboratory method where a solution of known strength (a standard solution) is dripped into an exact volume of unknown solution until neutralization is complete!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Glassware & The Color-Changing Detectives",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Here are the precision tools you use in a titration:\n\n1. **Pipette**: Delivers an exact fixed volume (usually $25.0\\text{ cm}^3$) of base into a clean conical flask.\n2. **Burette**: Holds the acid and drips it down drop-by-drop until the exact neutralization **end-point** is reached.\n3. **Indicators (Color Detectives)**:\n   - **Phenolphthalein**: Bright pink in base $\\rightarrow$ Turns completely colorless at the end-point.\n   - **Methyl Orange**: Yellow in base $\\rightarrow$ Turns orange/pink at the end-point (used when titrating carbonates like $\\text{Na}_2\\text{CO}_3$)."
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
                    "page_title": "The Master Titration Formula (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Titration Calculations",
                        "content": "### The Master Titration Formula:\n$$\\mathbf{\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b}}$$\n\n* **$M_a$** = Molarity of Acid ($\\text{mol/dm}^3$)\n* **$V_a$** = Average volume of Acid from burette ($\\text{cm}^3$)\n* **$M_b$** = Molarity of Base ($\\text{mol/dm}^3$)\n* **$V_b$** = Volume of Base measured by pipette ($\\text{cm}^3$)\n* **$a$ and $b$** = Recipe numbers (mole coefficients) from your balanced equation ($a\\text{ Acid} + b\\text{ Base} \\rightarrow \\text{Salt} + \\text{Water}$)"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Standardising Hydrochloric Acid",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$25.0\\text{ cm}^3$ of $0.10\\text{ M } \\text{Na}_2\\text{CO}_3$ solution required $20.0\\text{ cm}^3$ of $\\text{HCl}$ for complete neutralization with methyl orange indicator. Find the molarity and mass concentration (in $\\text{g/dm}^3$) of the hydrochloric acid. ($A_r$: $\\text{H}=1.0, \\text{Cl}=35.5$).",
                        "steps": [
                            "**1. Write the Balanced Equation First!**\n$$\\mathbf{2}\\text{HCl}_{(aq)} + \\mathbf{1}\\text{Na}_2\\text{CO}_{3(aq)} \\rightarrow 2\\text{NaCl}_{(aq)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)}$$\n- Equation numbers: $a = 2\\text{ (for Acid)}, b = 1\\text{ (for Base)}$",
                            "**2. What do we know?**\n- Acid: $V_a = 20.0\\text{ cm}^3, M_a = \\text{Target Molarity}$\n- Base: $M_b = 0.10\\text{ M}, V_b = 25.0\\text{ cm}^3$",
                            "**3. Apply the Titration Formula**:\n$$\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b} \\quad \\implies \\quad M_a = \\frac{a \\times M_b \\times V_b}{b \\times V_a}$$",
                            "**4. Substitute & Calculate**:\n$$M_a = \\frac{2 \\times 0.10\\text{ M} \\times 25.0\\text{ cm}^3}{1 \\times 20.0\\text{ cm}^3} = \\frac{5.0}{20.0} = 0.25\\text{ M}$$",
                            "**5. Convert Molarity to $\\text{g/dm}^3$**:\n- Molar mass of $\\text{HCl} = 1.0 + 35.5 = 36.5\\text{ g/mol}$\n$$\\text{Concentration} = 0.25\\text{ mol/dm}^3 \\times 36.5\\text{ g/mol} = 9.125\\text{ g/dm}^3$$\n- **Result**: The acid is $0.25\\text{ M}$ ($9.13\\text{ g/dm}^3$)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Glassware Rinsing Protocols",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### The Glassware Rinsing Rules:\n1. **Burette & Pipette**: Must be rinsed with distilled water, then **rinsed with the chemical solution they will hold**! Rinsing only with water leaves water droplets that dilute the solution, ruining your measurement.\n2. **Conical Flask**: Must be rinsed **ONLY with distilled water**! Never rinse with base. Leftover water droplets in the flask do NOT change the number of moles of base pipetted inside."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Titration Mole Ratio",
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
                    "page_number": 6,
                    "page_title": "Practice Question 2: Why Water in Conical Flask is OK",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Why does having droplets of distilled water inside the conical flask before pipetting base NOT affect titration accuracy?",
                        "options": [
                            "The water droplets do not change the total number of solute moles delivered by the pipette.",
                            "Distilled water neutralizes the acid instantly.",
                            "The indicator only changes color in pure water.",
                            "Water makes the burette stopcock turn smoother."
                        ],
                        "answer": "A",
                        "explanation": "The pipette delivers a fixed count of solute moles. Extra water in the conical flask changes the liquid volume, but does not alter the number of moles reacting with the acid."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Volumetric Analysis",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Titrations\n- **Tools**: Pipette (fixed volume), Burette (variable titre), Conical flask on white tile.\n- **Indicators**: Phenolphthalein (pink $\\rightarrow$ colorless); Methyl Orange (yellow $\\rightarrow$ orange/pink).\n- **The Formula**: $\\frac{M_a V_a}{M_b V_b} = \\frac{a}{b}$."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 171: BACK TITRATIONS
        # =====================================================================
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
                        "text": "By the end of this module, you will understand the two-stage logic of Back Titration, determine the purity of insoluble samples (such as limestone, eggshells, and antacids), and calculate residual unreacted moles with ease."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Analyzing Insoluble Rocks & Eggshells",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In regular titrations, your sample must dissolve in water so you can draw it into a pipette. But how do quality control chemists at **Bamburi Cement in Mombasa** test the purity of solid limestone ($\\text{CaCO}_3$) rocks? Or how do doctors test the active ingredient in an antacid tablet?\n\nLimestone does not dissolve in water! You cannot put solid rock into a pipette. To solve this, chemists use an indirect method called **Back Titration**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The 2-Stage Strategy: The Shopping Change Analogy",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Think of a back titration like buying groceries:\n* You walk into a supermarket with a **$1000\\text{ shilling}$ note** (known excess acid).\n* You buy your groceries (the limestone dissolves, consuming some acid).\n* When you pay, the cashier hands you **$200\\text{ shillings}$ in change** (the leftover unreacted acid).\n* How much did you spend on groceries? Easy: $1000 - 200 = \\mathbf{800\\text{ shillings}}$!\n\nThat is all back titration is: We add a known excess of acid, and then titrate the leftover change to see how much acid was consumed by the rock!"
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
                    "page_title": "The Back Titration Formulas (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Back Titration Principle",
                        "content": "### The 3 Calculation Steps:\n\n1. **Step 1: Total Moles of Acid Added**:\n   $$n_{\\text{total}} = \\frac{M_{\\text{acid}} \\times V_{\\text{acid}}}{1000}$$\n\n2. **Step 2: Moles of Leftover Acid (from Titration with $\\text{NaOH}$)**:\n   $$n_{\\text{leftover}} = \\frac{M_{\\text{base}} \\times V_{\\text{base}}}{1000}$$\n\n3. **Step 3: Moles Reacted with Solid Sample**:\n   $$\\mathbf{n_{\\text{reacted}} = n_{\\text{total}} - n_{\\text{leftover}}}$$\n\n---\n\n### Finding Percentage Purity:\n$$\\mathbf{\\%\\text{ Purity} = \\frac{\\text{Calculated Mass of Pure Compound}}{\\text{Total Mass of Impure Sample}} \\times 100}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Limestone Purity Calculation",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$1.25\\text{ g}$ of impure limestone was added to $50.0\\text{ cm}^3$ of $1.0\\text{ M } \\text{HCl}$ (an excess). The unreacted acid required $20.0\\text{ cm}^3$ of $0.50\\text{ M } \\text{NaOH}$ for complete neutralization. Calculate the percentage purity of calcium carbonate ($\\text{CaCO}_3$) in the sample. ($A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$).",
                        "steps": [
                            "**1. Step 1: Total Moles of Acid Added Initially**\n$$n_{\\text{total}}(\\text{HCl}) = \\frac{1.0\\text{ M} \\times 50.0\\text{ cm}^3}{1000} = 0.050\\text{ moles}$$",
                            "**2. Step 2: Moles of Leftover Acid Titrated by $\\text{NaOH}$**\n- Moles of $\\text{NaOH}$: $\\frac{0.50\\text{ M} \\times 20.0\\text{ cm}^3}{1000} = 0.010\\text{ moles}$\n$$\\implies n_{\\text{leftover}}(\\text{HCl}) = 0.010\\text{ moles}$$",
                            "**3. Step 3: Moles of Acid That Reacted with Limestone**\n$$n_{\\text{reacted}}(\\text{HCl}) = 0.050 - 0.010 = 0.040\\text{ moles}$$",
                            "**4. Step 4: Mass of Pure $\\text{CaCO}_3$**\n- Reaction: $\\text{CaCO}_3 + 2\\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2$ (Ratio $1 : 2$)\n$$n(\\text{CaCO}_3) = \\frac{0.040\\text{ mol}}{2} = 0.020\\text{ moles}$$\n- Molar mass of $\\text{CaCO}_3 = 100.0\\text{ g/mol}$\n$$\\text{Mass of pure } \\text{CaCO}_3 = 0.020\\text{ mol} \\times 100.0\\text{ g/mol} = 1.00\\text{ g}$$",
                            "**5. Step 5: Percentage Purity**\n$$\\%\\text{ Purity} = \\frac{1.00\\text{ g}}{1.25\\text{ g}} \\times 100 = 80.0\\%$$\n- **Result**: The limestone is $80.0\\%$ pure calcium carbonate."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why We Subtract Leftover Moles",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why is it called a \"Back\" Titration?\nBecause you don't titrate the solid directly. You add extra acid to dissolve the solid, and then \"titrate back\" the leftover portion to see what was left behind."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Back Titration Moles",
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
                        "explanation": "Moles of $\\text{HCl}$ reacted $= 0.030 - 0.010 = 0.020\\text{ mol}$. From the equation ratio ($1\\text{ Mg} : 2\\text{ HCl}$), moles of $\\text{Mg} = \\frac{0.020}{2} = 0.010\\text{ mol}$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Why Add Excess Acid",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "In a back titration, what is the main reason for adding excess standardized acid to an insoluble solid in Stage 1?",
                        "options": [
                            "To ensure the solid reacts completely and dissolves fully into solution.",
                            "To make the indicator change color permanently.",
                            "To evaporate the water in the flask.",
                            "To turn the solution alkaline."
                        ],
                        "answer": "A",
                        "explanation": "Insoluble solids cannot be titrated directly. Adding excess acid guarantees complete reaction and dissolution so the remaining liquid can be titrated."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Back Titrations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Back Titrations\n- **Purpose**: Analyzing insoluble or slow-reacting solids.\n- **Method**: Dissolve solid in known excess acid $\\rightarrow$ Titrate leftover acid with standard base.\n- **Equation**: $\\text{Moles Reacted} = \\text{Total Added} - \\text{Leftover}$."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 172: REDOX TITRATIONS
        # =====================================================================
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
                        "text": "By the end of this module, you will understand redox volumetric analysis, explain how Potassium Manganate(VII) acts as a self-indicating reagent, and calculate unknown concentrations using redox electron transfer ratios ($1:5$)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Self-Indicating Reagents",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In acid-base titrations, both liquids were clear as water, so we had to add an external indicator to see the end-point.\n\nIn **Redox Titrations**, many transition metal oxidizing agents have intense built-in colors. The most famous is **Potassium Manganate(VII) ($\\text{KMnO}_4$)**, whose deep purple solution acts as its own **self-indicating reagent**!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "The Chemistry of KMnO4 Titrations",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "In acidic solution, the deep purple manganate(VII) ion ($\\text{MnO}_4^-$) is reduced to the colorless $\\text{Mn}^{2+}$ ion:\n\n* **Reduction Half-Equation (Burette Solution)**:\n  $$\\text{MnO}_{4(aq)}^- + 8\\text{H}^+_{(aq)} + 5e^- \\rightarrow \\text{Mn}^{2+}_{(aq)} + 4\\text{H}_2\\text{O}_{(l)} \\quad (\\text{Deep Purple} \\rightarrow \\text{Colorless})$$\n\n* **Oxidation Half-Equation (Conical Flask: $\\text{Fe}^{2+}$)**:\n  $$\\text{Fe}^{2+}_{(aq)} \\rightarrow \\text{Fe}^{3+}_{(aq)} + e^- \\quad (\\text{Pale Green} \\rightarrow \\text{Yellow})$$\n\n* **Overall Balanced Ionic Equation**:\n  $$\\mathbf{\\text{MnO}_{4(aq)}^- + 8\\text{H}^+_{(aq)} + 5\\text{Fe}^{2+}_{(aq)} \\rightarrow \\text{Mn}^{2+}_{(aq)} + 5\\text{Fe}^{3+}_{(aq)} + 4\\text{H}_2\\text{O}_{(l)}}$$\n  *Mole Ratio*: **$1\\text{ mole } \\text{MnO}_4^- : 5\\text{ moles } \\text{Fe}^{2+}$**."
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
                    "page_title": "Redox Titration Rules (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Redox Titration Rules",
                        "content": "### 3 Essential Rules for $\\text{KMnO}_4$ Titrations:\n\n1. **No Indicator Needed**: The end-point occurs when **one drop of excess purple $\\text{KMnO}_4$** gives the solution a permanent faint pink color.\n2. **Read the TOP of the Meniscus**: Because $\\text{KMnO}_4$ is intensely dark, you cannot see the bottom curve of the liquid. Always read the top edge!\n3. **Acidify ONLY with Dilute Sulfuric Acid ($\\text{H}_2\\text{SO}_4$)**:\n   - *Why not $\\text{HCl}$?* $\\text{KMnO}_4$ oxidizes $\\text{Cl}^-$ into toxic chlorine gas ($\\text{Cl}_2$), giving a falsely high titre!\n   - *Why not $\\text{HNO}_3$?* Nitric acid is an oxidizing agent that steals $\\text{Fe}^{2+}$ electrons, giving a falsely low titre!\n   - *Why $\\text{H}_2\\text{SO}_4$?* Sulfate ions ($\\text{SO}_4^{2-}$) are completely inert to oxidation."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Standardising KMnO4",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "$25.0\\text{ cm}^3$ of $0.10\\text{ M } \\text{Fe}^{2+}$ solution was acidified with dilute sulfuric acid and titrated against potassium manganate(VII) ($\\text{KMnO}_4$). Exactly $20.0\\text{ cm}^3$ of $\\text{KMnO}_4$ was required to reach the faint pink end-point. Find the molarity of the $\\text{KMnO}_4$ solution.",
                        "steps": [
                            "**1. Step 1: Calculate Moles of $\\text{Fe}^{2+}$ Used**\n$$n(\\text{Fe}^{2+}) = \\frac{0.10\\text{ M} \\times 25.0\\text{ cm}^3}{1000} = 0.0025\\text{ moles}$$",
                            "**2. Step 2: Use the Redox Mole Ratio ($1 : 5$)**\n- Equation: $1\\text{ mole } \\text{MnO}_4^- \\text{ reacts with } 5\\text{ moles } \\text{Fe}^{2+}$\n$$n(\\text{MnO}_4^-) = \\frac{0.0025\\text{ mol}}{5} = 0.00050\\text{ moles}$$",
                            "**3. Step 3: Calculate Molarity of $\\text{KMnO}_4$**\n$$M = \\frac{n \\times 1000}{V(\\text{cm}^3)} = \\frac{0.00050\\text{ mol} \\times 1000}{20.0\\text{ cm}^3} = 0.025\\text{ mol/dm}^3\\text{ (or } 0.025\\text{ M)}$$",
                            "**Result**: The standardized $\\text{KMnO}_4$ solution is $0.025\\text{ M}$."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why We Acidify With Sulfuric Acid",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why only sulfuric acid?\nDilute sulfuric acid provides the necessary hydrogen ions ($\\text{H}^+$) for reduction without taking part in unwanted side-reactions. It is the only safe acid for manganate titrations!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Redox Mole Ratio",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "In an acidified redox titration between $\\text{KMnO}_4$ and $\\text{FeSO}_4$, what is the stoichiometric mole ratio of $\\text{MnO}_4^-$ to $\\text{Fe}^{2+}$?",
                        "options": [
                            "$1 : 1$",
                            "$1 : 2$",
                            "$1 : 5$",
                            "$2 : 5$"
                        ],
                        "answer": "C",
                        "explanation": "Because one $\\text{MnO}_4^-$ ion accepts 5 electrons and each $\\text{Fe}^{2+}$ ion loses 1 electron, the mole ratio is strictly $1 : 5$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: End-point Color",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What color change marks the end-point of a $\\text{KMnO}_4$ redox titration?",
                        "options": [
                            "Colorless to permanent faint pink",
                            "Purple to orange",
                            "Pale green to dark blue",
                            "Pink to colorless"
                        ],
                        "answer": "A",
                        "explanation": "Once all reducing agent is oxidized, the very next drop of purple $\\text{KMnO}_4$ is not reduced and imparts a permanent faint pink tint."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Redox Titrations",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Redox Titrations\n- **Self-Indicating**: $\\text{KMnO}_4$ turns from colorless to faint pink at the end-point.\n- **Acidification**: Use exclusively dilute $\\text{H}_2\\text{SO}_4$.\n- **Stoichiometry**: $\\text{MnO}_4^- : \\text{Fe}^{2+} = 1 : 5$."
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
    run_humanize_titrations()
