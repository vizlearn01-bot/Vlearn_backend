import os
import sys
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Topic, Lesson, LessonBlock, LessonAsset

def run_humanize_organic():
    print("Executing full humanization for Topic 24: Organic Chemistry I (Lessons 173 - 179)...")

    topic_24 = Topic.objects.get(id=24)

    lessons_payload = {
        # =====================================================================
        # LESSON 173: INTRO TO ORGANIC CHEMISTRY & HOMOLOGOUS SERIES
        # =====================================================================
        173: {
            "topic": topic_24,
            "title": "Introduction to Organic Chemistry and Homologous Series",
            "cards": [
                {
                    "page_number": 1,
                    "page_title": "The Chemistry of Carbon",
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "content": {
                        "text": "By the end of this module, you will understand why Carbon forms millions of unique compounds (catenation and tetravalency), define what a Hydrocarbon is, and master the concept of a Homologous Series (chemical families)."
                    }
                },
                {
                    "page_number": 1,
                    "page_title": "The Wonder Element: Carbon",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Over $90\\%$ of all known chemical substances on planet Earth are organic compounds! From the DNA in your cells and the food you eat to fuels, plastics, and medicines, Carbon is the central building block of life.\n\nWhy is Carbon so special?\n1. **Tetravalency (4 Bonding Arms)**: Carbon has 4 valence electrons, allowing it to form 4 strong covalent bonds with other atoms.\n2. **Catenation (Chaining Ability)**: Carbon atoms can link together to form endless straight chains, branched trees, and closed rings!"
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "What is a Homologous Series?",
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "content": {
                        "text": "Imagine a big family where all brothers and sisters share the same surname and similar physical traits. In Chemistry, we group similar organic compounds into \"chemical families\" called a **Homologous Series**.\n\n* **4 Characteristics of Every Homologous Series**:\n  1. **Same General Formula**: All members share the same algebraic formula (e.g. Alkanes = $\\text{C}_n\\text{H}_{2n+2}$).\n  2. **Consecutive Members Differ by a $-\\text{CH}_2-$ Group** (a mass of $14\\text{ a.m.u.}$).\n  3. **Similar Chemical Properties**: Because they have the same functional group.\n  4. **Gradual Trend in Physical Properties**: Melting and boiling points increase steadily as the carbon chain gets longer."
                    }
                },
                {
                    "page_number": 2,
                    "page_title": "Diagram: Homologous Series Family Tree",
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "content": {
                        "prompt": "Diagram illustrating the three major aliphatic hydrocarbon families: Alkanes (single bonds C-C), Alkenes (double bond C=C), and Alkynes (triple bond C≡C) with their general formulas.",
                        "caption": "Hydrocarbon Families: Alkanes (saturated), Alkenes, and Alkynes (unsaturated) classified by their carbon-carbon bonds."
                    },
                    "asset_info": {
                        "title": "Hydrocarbon Families Chart",
                        "description": "Comparative classification diagram for Alkanes, Alkenes, and Alkynes.",
                        "ai_instruction": "Create a 3-column reference chart comparing Alkanes (C-C), Alkenes (C=C), and Alkynes (C≡C) with general formulas."
                    }
                },
                {
                    "page_number": 3,
                    "page_title": "The Three Hydrocarbon Families (In Plain English)",
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "content": {
                        "term": "Hydrocarbon Families",
                        "content": "### 1. Alkanes (Saturated Hydrocarbons)\n* **Bonding**: Only single carbon-carbon bonds ($\\text{C}-\\text{C}$).\n* **General Formula**: $\\mathbf{\\text{C}_n\\text{H}_{2n+2}}$ (where $n = 1, 2, 3...$)\n* **Example**: Methane ($\\text{CH}_4$), Ethane ($\\text{C}_2\\text{H}_6$).\n\n### 2. Alkenes (Unsaturated with Double Bond)\n* **Bonding**: Contains at least one double bond ($\\text{C}=\\text{C}$).\n* **General Formula**: $\\mathbf{\\text{C}_n\\text{H}_{2n}}$ (where $n = 2, 3, 4...$)\n* **Example**: Ethene ($\\text{C}_2\\text{H}_4$), Propene ($\\text{C}_3\\text{H}_6$).\n\n### 3. Alkynes (Unsaturated with Triple Bond)\n* **Bonding**: Contains at least one triple bond ($\\text{C}\\equiv\\text{C}$).\n* **General Formula**: $\\mathbf{\\text{C}_n\\text{H}_{2n-2}}$ (where $n = 2, 3, 4...$)\n* **Example**: Ethyne ($\\text{C}_2\\text{H}_2$), Propyne ($\\text{C}_3\\text{H}_4$)."
                    }
                },
                {
                    "page_number": 4,
                    "page_title": "Worked Example: Finding Formulas in a Homologous Series",
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "content": {
                        "problem": "1. Write the molecular formula for an alkane containing 6 carbon atoms ($n=6$).\n2. A hydrocarbon has the molecular formula $\\text{C}_5\\text{H}_{10}$. To which homologous series does it belong?",
                        "steps": [
                            "**Problem 1: Alkane with 6 Carbons**\n- General Formula: $\\text{C}_n\\text{H}_{2n+2}$\n- Substitute $n = 6$:\n$$\\text{Number of Hydrogens} = 2(6) + 2 = 14$$\n- **Result**: Molecular formula is $\\mathbf{\\text{C}_6\\text{H}_{14}}$ (hexane).",
                            "**Problem 2: Classifying $\\text{C}_5\\text{H}_{10}$**\n- Here $n = 5$, and number of hydrogens = $10$.\n- Since $10 = 2 \\times 5$ ($2n$), it perfectly fits the general formula $\\mathbf{\\text{C}_n\\text{H}_{2n}}$.\n- **Result**: $\\text{C}_5\\text{H}_{10}$ is an **Alkene** (pentene)."
                        ]
                    }
                },
                {
                    "page_number": 5,
                    "page_title": "Think About This: Saturated vs Unsaturated",
                    "block_type": "common_misconception",
                    "component_type": "common_misconception",
                    "content": {
                        "text": "### What does \"Saturated\" mean in Chemistry?\nThink of a sponge soaked full with water—it cannot hold any more liquid.\n\nIn an **Alkane**, carbon atoms share only single bonds, meaning every carbon is \"holding hands\" with the maximum possible number of hydrogen atoms. It is completely **saturated**! In contrast, **Alkenes and Alkynes** have double or triple bonds that can pop open to add more atoms, making them **unsaturated**."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 1: Homologous Series Traits",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following is NOT a property of a homologous series?",
                        "options": [
                            "Members share the same general formula.",
                            "Adjacent members differ by a $-\\text{CH}_2-$ unit.",
                            "All members have identical melting and boiling points.",
                            "Members possess similar chemical properties."
                        ],
                        "answer": "C",
                        "explanation": "Melting and boiling points are NOT identical; they increase gradually and steadily as carbon chain length increases due to stronger van der Waals intermolecular forces."
                    }
                },
                {
                    "page_number": 6,
                    "page_title": "Practice Question 2: Classifying Hydrocarbons",
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "content": {
                        "check_type": "multiple_choice",
                        "question": "Which of the following molecular formulas represents an alkyne?",
                        "options": [
                            "$\\text{C}_3\\text{H}_8$",
                            "$\\text{C}_3\\text{H}_6$",
                            "$\\text{C}_3\\text{H}_4$",
                            "$\\text{C}_4\\text{H}_{10}$"
                        ],
                        "answer": "C",
                        "explanation": "Alkynes follow $\\text{C}_n\\text{H}_{2n-2}$. For $n=3$: $2(3) - 2 = 4$. Therefore, $\\text{C}_3\\text{H}_4$ (propyne) is an alkyne."
                    }
                },
                {
                    "page_number": 7,
                    "page_title": "Key Takeaways: Organic Chemistry Introduction",
                    "block_type": "summary",
                    "component_type": "summary",
                    "content": {
                        "text": "### Summary: Introduction to Organic Chemistry\n- **Carbon's Versatility**: Tetravalent (4 bonds) and catenation (chains and rings).\n- **Homologous Series**: Family of organic compounds sharing the same general formula and differing by $-\\text{CH}_2-$.\n- **The Big 3 Hydrocarbon Families**: Alkanes ($\\text{C}_n\\text{H}_{2n+2}$), Alkenes ($\\text{C}_n\\text{H}_{2n}$), Alkynes ($\\text{C}_n\\text{H}_{2n-2}$)."
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
    run_humanize_organic()
