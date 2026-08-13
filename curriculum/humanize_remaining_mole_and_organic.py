import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_humanize_remaining():
    print("Executing full humanization for Lessons 168 through 179...")

    topic_23 = Topic.objects.get(id=23)
    topic_24 = Topic.objects.get(id=24)

    lessons_payload = {
        # =====================================================================
        # LESSON 168: DILUTION OF SOLUTIONS
        # =====================================================================
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
                        "text": "By the end of this module, you will understand the Dilution Law ($C_1V_1 = C_2V_2$), calculate the exact volume of stock acid needed to make any diluted solution, and explain why adding water preserves the total number of solute particles."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Making Juice from Concentrate",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "If you take a sip of pure blackcurrant juice concentrate directly from the bottle, it tastes overpoweringly sweet and strong. To make it enjoyable, you pour a little concentrate into a glass and top it up with clean water.\n\nNotice something important: Adding water did **not** destroy or add any sugar molecules! It simply gave the exact same number of sugar molecules a larger volume of water to swim around in.\n\nIn Chemistry, this process of lowering concentration by adding solvent is called **Dilution**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Why Solute Moles Never Change During Dilution",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Let's look at what happens in the laboratory when you dilute concentrated hydrochloric acid ($\\text{HCl}$):\n\n* **Macroscopic Action**:\n  You measure $25\\text{ cm}^3$ of strong $2.0\\text{ M } \\text{HCl}$, pour it into a flask, and add distilled water until the total volume reaches $250\\text{ cm}^3$.\n* **Microscopic Particle Model**:\n  The initial $25\\text{ cm}^3$ contains a fixed number of hydrogen ions ($\\text{H}^+$) and chloride ions ($\\text{Cl}^-$). Adding water pushes the ions further apart, lowering their density per cubic centimeter without changing the total count of ions!\n\n* **The Conservation Equation**:\n  $$\\text{Moles of solute BEFORE dilution} = \\text{Moles of solute AFTER dilution}$$\n  $$\\mathbf{C_1 V_1 = C_2 V_2}$$"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Solute Particle Conservation in Dilution",
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
                    "page_title": "The Dilution Formula & Water Accounting",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "The Dilution Law",
                        "content": "### The Master Dilution Formula:\n$$\\mathbf{C_1 V_1 = C_2 V_2}$$\n\n* **$C_1$** = Initial concentration of stock solution (stronger)\n* **$V_1$** = Volume of stock solution you need to measure\n* **$C_2$** = Final target concentration (weaker)\n* **$V_2$** = Total final volume of the diluted mixture\n\n---\n\n### How Much Water Do You Add?\n$$\\mathbf{V_{\\text{water added}} = V_2 - V_1}$$\n*(Subtract the stock volume from the total final volume to know how much distilled water to pour in!)*"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Dilution Calculations",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. If $25.0\\text{ cm}^3$ of $2.0\\text{ M } \\text{HCl}$ stock is diluted with distilled water to a total volume of $250.0\\text{ cm}^3$, find the new concentration ($C_2$).\n2. What volume of $2.0\\text{ M } \\text{H}_2\\text{SO}_4$ stock is needed to prepare $500.0\\text{ cm}^3$ of $0.10\\text{ M}$ acid? How much water must be added?",
                        "steps": [
                            "**Problem 1: Finding Diluted Concentration ($C_2$)**\n- **1. What do we know?** $C_1 = 2.0\\text{ M}, V_1 = 25.0\\text{ cm}^3, V_2 = 250.0\\text{ cm}^3$\n- **2. Apply Formula**: $C_1V_1 = C_2V_2 \\implies C_2 = \\frac{C_1 V_1}{V_2}$\n- **3. Calculate**:\n$$C_2 = \\frac{2.0\\text{ M} \\times 25.0\\text{ cm}^3}{250.0\\text{ cm}^3} = 0.20\\text{ M}$$\n- **Result**: The diluted acid has a strength of $0.20\\text{ M}$ (10 times more dilute).",
                            "**Problem 2: Volume of Stock and Water Needed**\n- **1. What do we know?** $C_1 = 2.0\\text{ M}, C_2 = 0.10\\text{ M}, V_2 = 500.0\\text{ cm}^3$\n- **2. Find Stock Volume ($V_1$)**:\n$$V_1 = \\frac{C_2 V_2}{C_1} = \\frac{0.10\\text{ M} \\times 500.0\\text{ cm}^3}{2.0\\text{ M}} = 25.0\\text{ cm}^3$$\n- **3. Calculate Water Added**:\n$$V_{\\text{water}} = V_2 - V_1 = 500.0\\text{ cm}^3 - 25.0\\text{ cm}^3 = 475.0\\text{ cm}^3$$\n- **Result**: Measure $25.0\\text{ cm}^3$ of stock acid and mix with $475.0\\text{ cm}^3$ of distilled water."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: The Acid Dilution Safety Rule",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### The Golden Safety Rule: Always Add Acid to Water (AA)\n**Never pour water into concentrated sulfuric acid!**\n\nMixing concentrated $\\text{H}_2\\text{SO}_4$ with water releases enormous heat. Because water is lighter than acid, pouring water causes it to float on top. The extreme heat boils the water instantly, causing violent explosions that splatter boiling acid onto your skin and face!\n\n**Always pour concentrated acid slowly down a glass rod into a large volume of water while stirring continuously.**"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Diluting Nitric Acid",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of distilled water must be added to $50.0\\text{ cm}^3$ of $4.0\\text{ M } \\text{HNO}_3$ to dilute it to a $0.50\\text{ M}$ solution?",
                        "options": [
                            "$400.0\\text{ cm}^3$",
                            "$350.0\\text{ cm}^3$",
                            "$450.0\\text{ cm}^3$",
                            "$500.0\\text{ cm}^3$"
                        ],
                        "answer": "B",
                        "explanation": "First find total final volume $V_2$: $C_1V_1 = C_2V_2 \\implies V_2 = \\frac{4.0 \\times 50.0}{0.50} = 400.0\\text{ cm}^3$. The question asks for water added: $V_{\\text{water}} = V_2 - V_1 = 400.0 - 50.0 = 350.0\\text{ cm}^3$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Calculating Diluted Molarity",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "If $100\\text{ cm}^3$ of $1.0\\text{ M } \\text{NaCl}$ solution is diluted to a total volume of $500\\text{ cm}^3$ with distilled water, what is the new molarity?",
                        "options": [
                            "$0.50\\text{ M}$",
                            "$0.20\\text{ M}$",
                            "$0.10\\text{ M}$",
                            "$0.05\\text{ M}$"
                        ],
                        "answer": "B",
                        "explanation": "Applying Dilution Law: $C_2 = \\frac{C_1 V_1}{V_2} = \\frac{1.0\\text{ M} \\times 100\\text{ cm}^3}{500\\text{ cm}^3} = 0.20\\text{ M}$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Dilution",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Dilution of Solutions\n- **Core Rule**: Total moles of solute remain constant during dilution.\n- **The Formula**: $C_1V_1 = C_2V_2$.\n- **Water Added**: $V_{\\text{water}} = V_2 - V_1$.\n- **Safety Protocol**: Always add concentrated acid to water slowly with stirring."
                    }
                }
            ]
        },

        # =====================================================================
        # LESSON 169: STOICHIOMETRY
        # =====================================================================
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
                        "text": "By the end of this module, you will read balanced chemical equations as nature's exact recipe ratios, calculate reacting masses, apply Molar Gas Volumes ($22.4\\text{ dm}^3$ at s.t.p. and $24.0\\text{ dm}^3$ at r.t.p.), and solve gas volume problems using Gay-Lussac's Law."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "Nature's Perfect Recipes",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "When baking mandazis or a cake, you must follow an exact recipe: 2 cups of flour + 1 cup of milk + 2 eggs. If you add too much flour, the dough is ruined!\n\nChemical reactions follow nature's exact quantitative recipes. A balanced chemical equation tells us the precise recipe ratio in which atoms and molecules combine. In Chemistry, the study of these quantitative mass and volume relationships is called **Stoichiometry**."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Reading a Chemical Equation Like a Recipe",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Consider the combustion of methane gas:\n$$\\mathbf{1\\text{CH}_{4(g)} + 2\\text{O}_{2(g)} \\rightarrow 1\\text{CO}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)}}$$\n\nLook at the numbers (coefficients) in front of each formula:\n* **Mole Recipe Ratio**: $1\\text{ mole of } \\text{CH}_4$ needs **$2\\text{ moles of } \\text{O}_2$** to make **$1\\text{ mole of } \\text{CO}_2$** and **$2\\text{ moles of } \\text{H}_2\\text{O}$**.\n* **Mass Check**: $16.0\\text{ g of } \\text{CH}_4 + 64.0\\text{ g of } \\text{O}_2 = 80.0\\text{ g of reactants} \\rightarrow 44.0\\text{ g of } \\text{CO}_2 + 36.0\\text{ g of } \\text{H}_2\\text{O} = 80.0\\text{ g of products}$. Mass is completely conserved!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Molar Gas Volume Reference Cubes",
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
                    "page_title": "Molar Gas Volumes (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Molar Gas Volume",
                        "content": "### What is Molar Gas Volume ($V_m$)?\n*The volume occupied by **exactly 1 mole of ANY gas** under standard laboratory conditions.*\n\n* **At standard temperature and pressure (s.t.p., $0^\\circ\\text{C}$)**:\n  $$\\mathbf{V_m = 22.4\\text{ dm}^3\\text{ (or } 22400\\text{ cm}^3\\text{)}}$$\n* **At room temperature and pressure (r.t.p., $25^\\circ\\text{C}$)**:\n  $$\\mathbf{V_m = 24.0\\text{ dm}^3\\text{ (or } 24000\\text{ cm}^3\\text{)}}$$\n\n### Gas Volume Formulas:\n$$\\mathbf{\\text{Volume of Gas } (V) = \\text{Moles } (n) \\times V_m}$$\n$$\\mathbf{n = \\frac{\\text{Volume in dm}^3}{V_m}}$$"
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Reacting Mass & Gas Volume",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "Calculate the volume of carbon dioxide gas ($\\text{CO}_2$) produced at r.t.p. when $10.0\\text{ g}$ of pure calcium carbonate ($\\text{CaCO}_3$) reacts with excess dilute hydrochloric acid.\n$$\\text{CaCO}_{3(s)} + 2\\text{HCl}_{(aq)} \\rightarrow \\text{CaCl}_{2(aq)} + \\text{H}_2\\text{O}_{(l)} + \\text{CO}_{2(g)}$$\n(Given $A_r$: $\\text{Ca}=40.0, \\text{C}=12.0, \\text{O}=16.0$; $V_m$ at r.t.p. = $24.0\\text{ dm}^3\\text{/mol}$).",
                        "steps": [
                            "**1. Step 1: Find Moles of the Given Reactant ($\\text{CaCO}_3$)**\n- Molar mass of $\\text{CaCO}_3 = 40.0 + 12.0 + 3(16.0) = 100.0\\text{ g/mol}$\n$$n = \\frac{10.0\\text{ g}}{100.0\\text{ g/mol}} = 0.10\\text{ moles of } \\text{CaCO}_3$$",
                            "**2. Step 2: Use the Equation Mole Ratio**\n- Equation shows: $1\\text{ mole of } \\text{CaCO}_3 \\rightarrow 1\\text{ mole of } \\text{CO}_2$\n$$\\implies n(\\text{CO}_2) = 0.10\\text{ moles of } \\text{CO}_2$$",
                            "**3. Step 3: Convert Moles to Gas Volume at r.t.p.**\n$$V(\\text{CO}_2) = n \\times V_m = 0.10\\text{ mol} \\times 24.0\\text{ dm}^3\\text{/mol} = 2.40\\text{ dm}^3$$\n$$V = 2.40 \\times 1000 = 2400\\text{ cm}^3$$\n- **Result**: Exactly $2.40\\text{ dm}^3$ ($2400\\text{ cm}^3$) of $\\text{CO}_2$ gas is collected."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Why All Gases Have the Same Volume",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### Why does 1 mole of heavy CO2 (44g) fill the same volume as 1 mole of light H2 (2g)?\nIn a gas, molecules are separated by massive empty spaces. The physical size of the actual molecule is negligible.\n\nAt the same temperature and pressure, the push against the walls depends strictly on the **count of particles ($6.022 \\times 10^{23}$)**, not how heavy each individual particle is!"
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Hydrogen Gas at STP",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of hydrogen gas at s.t.p. is liberated when $2.4\\text{ g}$ of magnesium reacts completely with excess dilute hydrochloric acid? ($A_r$: $\\text{Mg}=24.0, V_m = 22.4\\text{ dm}^3\\text{/mol}$).\n$$\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2$$",
                        "options": [
                            "$2.24\\text{ dm}^3$",
                            "$22.4\\text{ dm}^3$",
                            "$4.48\\text{ dm}^3$",
                            "$1.12\\text{ dm}^3$"
                        ],
                        "answer": "A",
                        "explanation": "Moles of $\\text{Mg} = \\frac{2.4}{24.0} = 0.10\\text{ mol}$. Mole ratio $\\text{Mg} : \\text{H}_2 = 1 : 1 \\implies 0.10\\text{ mol } \\text{H}_2$. Volume at s.t.p. $= 0.10\\text{ mol} \\times 22.4\\text{ dm}^3\\text{/mol} = 2.24\\text{ dm}^3$."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Gay-Lussac Combining Volumes",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "What volume of oxygen gas is needed for complete combustion of $40.0\\text{ cm}^3$ of propane ($\\text{C}_3\\text{H}_8$) at constant temperature and pressure?\n$$\\text{C}_3\\text{H}_{8(g)} + 5\\text{O}_{2(g)} \\rightarrow 3\\text{CO}_{2(g)} + 4\\text{H}_2\\text{O}_{(l)}$$",
                        "options": [
                            "$40.0\\text{ cm}^3$",
                            "$120.0\\text{ cm}^3$",
                            "$200.0\\text{ cm}^3$",
                            "$8.0\\text{ cm}^3$"
                        ],
                        "answer": "C",
                        "explanation": "By Gay-Lussac's Law, gas volume ratio matches equation coefficients: $\\text{C}_3\\text{H}_8 : \\text{O}_2 = 1 : 5$. Volume of $\\text{O}_2 = 5 \\times 40.0\\text{ cm}^3 = 200.0\\text{ cm}^3$."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Stoichiometry",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Stoichiometry\n- **Mole Ratio**: Read directly from balanced equation coefficients.\n- **Molar Gas Volumes**: $1\\text{ mole} = 22.4\\text{ dm}^3$ at s.t.p.; $24.0\\text{ dm}^3$ at r.t.p.\n- **3-Step Workflow**: Known Grams $\\rightarrow$ Moles of Known $\\rightarrow$ Target Moles (Mole Ratio) $\\rightarrow$ Target Grams or Gas Volume."
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
    run_humanize_remaining()
