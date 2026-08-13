import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def apply_perfect_card_structures():
    print("Applying clean, uncluttered card structures across all Form 3 Chemistry lessons...")

    topic_22 = Topic.objects.get(id=22) # Gas Laws
    topic_23 = Topic.objects.get(id=23) # The Mole
    topic_24 = Topic.objects.get(id=24) # Organic Chemistry I

    # =========================================================================
    # REFINING LESSON 169 (STOICHIOMETRY & MOLAR GAS VOLUMES)
    # =========================================================================
    lesson_169_cards = [
        {
            "page_number": 1,
            "page_title": "Chemical Recipes & Stoichiometry",
            "block_type": "learning_goal",
            "component_type": "learning_goal",
            "content": {
                "text": "By the end of this module, you will read balanced chemical equations as nature's exact recipe ratios, understand the physical size of Molar Gas Volume ($22.4\\text{ dm}^3$ at s.t.p. and $24.0\\text{ dm}^3$ at r.t.p.), and calculate reacting gas volumes with confidence."
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
                "text": "Consider the combustion of methane gas:\n$$\\text{CH}_{4(g)} + 2\\text{O}_{2(g)} \\rightarrow \\text{CO}_{2(g)} + 2\\text{H}_2\\text{O}_{(l)}$$\n\nLook at the numbers (coefficients) in front of each formula:\n* **Mole Recipe Ratio**: $1\\text{ mole of } \\text{CH}_4$ needs **$2\\text{ moles of } \\text{O}_2$** to make **$1\\text{ mole of } \\text{CO}_2$** and **$2\\text{ moles of } \\text{H}_2\\text{O}$**.\n* **Mass Check**: $16.0\\text{ g of } \\text{CH}_4 + 64.0\\text{ g of } \\text{O}_2 = 80.0\\text{ g of reactants} \\rightarrow 44.0\\text{ g of } \\text{CO}_2 + 36.0\\text{ g of } \\text{H}_2\\text{O} = 80.0\\text{ g of products}$. Mass is completely conserved!"
            }
        },
        {
            "page_number": 2,
            "page_title": "Diagram: Molar Gas Volume Reference Cubes",
            "block_type": "suggested_diagram",
            "component_type": "suggested_diagram",
            "content": {
                "prompt": "Diagram showing 1 mole of any gas occupying a cube of 22.4 dm3 at s.t.p. and a cube of 24.0 dm3 at r.t.p., with a 20L water jerrican shown alongside for real-world size comparison.",
                "caption": "Avogadro's Gas Law: 1 mole of ANY gas occupies 22.4 dm3 at s.t.p. and 24.0 dm3 at r.t.p. (roughly the size of a 20L water jerrican plus a kettle)."
            },
            "asset_info": {
                "title": "Molar Gas Volume Comparison Diagram",
                "description": "Visual comparison of 1 mole of gas occupying 22.4L at s.t.p. and 24.0L at r.t.p. against everyday container volumes.",
                "ai_instruction": "Create an illustration comparing two transparent gas cubes labeled 22.4 dm3 (s.t.p., 0°C) and 24.0 dm3 (r.t.p., 25°C) holding 1 mole of gas alongside a familiar 20-litre water container."
            }
        },
        {
            "page_number": 3,
            "page_title": "Molar Gas Volume ($V_m$)",
            "block_type": "definition_card",
            "component_type": "definition_card",
            "content": {
                "term": "Molar Gas Volume ($V_m$)",
                "content": "The volume occupied by exactly one mole of any gas under standard laboratory conditions ($22.4\\text{ dm}^3$ at s.t.p. and $24.0\\text{ dm}^3$ at r.t.p.)."
            }
        },
        {
            "page_number": 3,
            "page_title": "Gas Volume Calculation Formulas",
            "block_type": "formula_breakdown",
            "component_type": "formula_breakdown",
            "content": {
                "formula": "V = n \\times V_m \\quad \\Longleftrightarrow \\quad n = \\frac{V}{V_m}",
                "content": "* **$V$** = Volume of gas in $\\text{dm}^3$ (or $\\text{cm}^3$)\n* **$n$** = Number of moles\n* **$V_m$** = Molar gas volume ($22.4\\text{ dm}^3$ at s.t.p. / $24.0\\text{ dm}^3$ at r.t.p.)\n\n*Rule of Thumb*: To find volume, multiply moles by $V_m$. To find moles from volume, divide volume by $V_m$!"
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
                "text": "In a gas, molecules are separated by massive empty spaces. The physical size of the actual molecule is negligible.\n\nThink of 100 flying bees spaced 10 meters apart versus 100 flying birds spaced 10 meters apart—both flocks occupy the exact same cloud volume! At the same temperature and pressure, volume depends strictly on the **count of particles ($6.022 \\times 10^{23}$)**, not their weight."
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

    # Save Lesson 169
    l169 = Lesson.objects.get(id=169)
    LessonBlock.objects.filter(lesson=l169).delete()
    LessonAsset.objects.filter(lesson=l169).delete()
    for order, card in enumerate(lesson_169_cards, start=1):
        block_id = f"block_{l169.id}_{order}_{uuid.uuid4().hex[:6]}"
        b = LessonBlock.objects.create(
            lesson=l169,
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
                lesson=l169,
                asset_type="diagram",
                source_type="uploaded",
                storage_type="local",
                status="pending",
                title=info["title"],
                description=info["description"],
                metadata={"ai_instruction": info["ai_instruction"], "block_id": b.block_id}
            )
    print("Lesson 169 refactored into clean component cards successfully.")

if __name__ == "__main__":
    apply_perfect_card_structures()
