"""
VLearn CBC Grade 9 Agriculture — Topic 1: Conserving Animal Feeds (Forage, Drought, and Hay)
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 9 (Level: 9)
Subject: Agriculture
Topic: Conserving Animal Feeds (Forage, Drought, and Hay) (Topic Order: 1)

Decomposed into 12 Learning Units & 12 Published Lessons:
  1. Meaning of Forage and Environmental Forage Materials (6 Pages, 12 Blocks)
  2. The Effects of Drought on Livestock Feed Resources (6 Pages, 11 Blocks)
  3. Introduction to Forage Conservation Methods (Baled Haymaking) (6 Pages, 11 Blocks)
  4. Types of Bales and Safe Hay Storage Practices (6 Pages, 11 Blocks)
  5. Meaning, Preparation, and Management of Standing Forage (6 Pages, 11 Blocks)
  6. Advanced Field Management Techniques for Standing Forage (6 Pages, 11 Blocks)
  7. Stacking (Haystacks) as a Forage Conservation Method (6 Pages, 11 Blocks)
  8. Box-Bailing Concepts and Equipment (6 Pages, 10 Blocks)
  9. Practical Activity: Preparing and Conserving Forage using Stacking (6 Pages, 11 Blocks)
  10. Practical Activity: Box-Bailing Hay using Locally Available Materials (6 Pages, 11 Blocks)
  11. Household Strategies to Conserve Forage During Drought (5 Pages, 10 Blocks)
  12. Relational and Economic Benefits of Hay Conservation & Capstone Review (10 Pages, 18 Blocks)

Features:
  - Rich typography with bold key terms, phrases, and structured bullets.
  - Step-by-step practical process workflows.
  - Formatted comparison tables, callouts, and mnemonic tips.
  - Formative scenario MCQs and Topic Summative MCQs with educational feedback.
  - Zero citation bracket leaks and zero raw LaTeX.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade9_agriculture_topic1.py [--replace]
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Convert unicode bullets to markdown list items
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def build_topic1_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 1: Conserving Animal Feeds."""
    return [
        # =====================================================================
        # LESSON 1: Meaning of Forage and Environmental Forage Materials
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning of Forage and Environmental Forage Materials",
            "unit_description": "Forage definition, biological plant categories (grasses, legumes), crop residues, and local feed identification.",
            "lesson_title": "Meaning of Forage and Environmental Forage Materials",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Welcome to Livestock Feed: Exploring Pasture Forage",
                        "content": {
                            "title": "Welcome to Livestock Feed: Exploring Pasture Forage",
                            "caption": "A healthy dairy cow grazing on a vibrant, mixed pasture containing long grasses and leafy legumes."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Livestock Forage",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **forage** as a primary category of animal feed grown naturally or planted by humans.",
                                "List common plant materials in the local environment suitable for livestock feed.",
                                "Distinguish between **grass forage**, **legume forage**, and **crop residues**.",
                                "Categorize local plants into energy-giving and protein-rich feed sources."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Foundation of Livestock Farming",
                        "content": {
                            "title": "More Than Just Grass",
                            "text": "When you observe cattle grazing in a field, they are not simply eating weeds. They are consuming a balanced diet of different pasture plants collectively known as **forage**!\n\n- **Direct Grazing**: Animals walk freely across pastures to feed on living plants.\n- **Indirect Feeding (Zero-Grazing)**: Farmers cut fresh forage, chop it, and bring it directly to sheltered livestock pens.\n- **Economic Lifeline**: Forage is the most natural, affordable, and bulky source of nutrition for cattle, sheep, goats, donkeys, and rabbits."
                        }
                    }
                ],
                # Page 2: Biological Taxonomy: Grasses and Legumes
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Primary Forage Families",
                        "content": {
                            "title": "Grasses for Energy & Legumes for Protein",
                            "text": "Agricultural forage is divided into two primary biological plant families:\n\n- **Grasses (Energy & Bulk Fiber)**: Narrow-leaved plants that provide structural carbohydrates and energy. Examples include **Rhodes grass** (ideal for haymaking), **Napier grass** (high-yielding zero-grazing fodder), and cereals like **sorghum** and **oats**.\n- **Legumes (Protein & Minerals)**: Broad-leaved plants with seed pods that fix nitrogen in the soil and supply vital protein for milk production and muscle growth. A key local example is **Desmodium**, a climbing legume frequently intercropped with grasses."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Grass Forage vs. Legume Forage",
                        "content": {
                            "title": "Grasses vs. Legumes in Animal Nutrition",
                            "headers": ["Nutritional Aspect", "Forage Grasses (e.g. Rhodes, Napier)", "Forage Legumes (e.g. Desmodium)"],
                            "rows": [
                                ["Primary Nutrient", "Structural carbohydrates & bulk fiber", "High protein, calcium & minerals"],
                                ["Plant Leaf Structure", "Narrow, parallel-veined leaves", "Broad leaves with seed pods"],
                                ["Livestock Benefit", "Provides energy and keeps the rumen full", "Boosts daily milk yield and muscle repair"],
                                ["Agronomic Value", "Fast growing and produces massive biomass", "Fixes atmospheric nitrogen to enrich soil fertility"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Key Agronomic Tip",
                        "content": {
                            "title": "The Power of Mixed Pasture",
                            "text": "Planting **Rhodes grass** together with **Desmodium** creates a balanced pasture. The grass provides bulk energy, while the legume provides protein and fertilizes the soil naturally through nitrogen fixation!"
                        }
                    }
                ],
                # Page 3: Crop Residues as Emergency Feed
                [
                    {
                        "type": "concept_explanation",
                        "title": "Valuable Farm By-Products: Crop Residues",
                        "content": {
                            "title": "Saving Crop Leftovers",
                            "text": "After harvesting grain crops for human food, the remaining stalks, leaves, and husks are known as **crop residues**.\n\n- **Maize Stover**: Dry stalks, leaves, and husks left in the field after harvesting maize cobs.\n- **Wheat & Barley Straw**: Dry golden stems remaining after harvesting small cereal grains.\n- **Strategic Value**: Although lower in protein than fresh green pasture, crop residues are dry, rich in digestible fiber, and can be stored easily to feed herds during critical feed shortages."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Botanical and Agricultural Forage Classification Wheel",
                        "content": {
                            "title": "Botanical and Agricultural Forage Classification Wheel",
                            "caption": "Classification map separating green forage grasses, protein-rich legumes, and dry harvested crop residues."
                        }
                    }
                ],
                # Page 4: Plant Identification & Practical Sorting
                [
                    {
                        "type": "worked_example",
                        "title": "Practical Field Classification: Identifying Forage",
                        "content": {
                            "intro": "Let us classify common farm plants found around a typical rural household into their correct nutritional category:",
                            "steps": [
                                "**Rhodes Grass**: Categorized as a **Grass**. It has long, narrow leaves and provides structural bulk fiber for grazing.",
                                "**Desmodium**: Categorized as a **Legume**. It has broad clover-like leaves and supplies essential protein for dairy cows.",
                                "**Maize Stover**: Categorized as a **Crop Residue**. It consists of dry harvested stalks saved for dry-season feeding.",
                                "**Napier Grass**: Categorized as a **Grass**. It produces thick, tall canes harvested green for zero-grazing stall feeding."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Compound Forage Scouting",
                        "content": {
                            "title": "Explore Your Local Environment",
                            "instruction": "Take a 10-minute walk around your school garden or home compound. Collect 3 different plant samples that domestic animals eat. In your notebook, classify each sample as a **Grass**, a **Legume**, or a **Crop Residue** based on its leaf shape."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Identifying Forage Types",
                        "content": {
                            "question": "Farmer Omondi wants to plant a high-protein forage crop that will improve the milk yield of his dairy cows when mixed with Rhodes grass. Which of the following plants should he select?",
                            "options": [
                                "Maize Stover",
                                "Wheat Straw",
                                "Desmodium",
                                "Napier Grass"
                            ],
                            "answer": "C",
                            "explanation": "Desmodium is a legume, meaning it is rich in crude protein and minerals essential for milk synthesis. Maize stover and wheat straw are fibrous crop residues, while Napier is a carbohydrate-rich grass."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Forage** includes all pasture plants and harvested vegetation used to nourish domestic livestock.\n- **Grasses** (like Rhodes and Napier) deliver bulk structural fiber and carbohydrates.\n- **Legumes** (like Desmodium) supply high-value proteins and enrich soil nitrogen.\n- **Crop residues** (such as maize stover and wheat straw) are dry, durable feed reserves for periods of scarcity."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we know the types of forage, what happens when rainfall fails and pastures dry up? In the next lesson, we will investigate the physiological and economic impacts of severe drought on livestock feed resources."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: The Effects of Drought on Livestock Feed Resources
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "The Effects of Drought on Livestock Feed Resources",
            "unit_description": "Drought definition, pasture moisture loss, lignification and fiber increase, nutritional decline, and herd economic consequences.",
            "lesson_title": "The Effects of Drought on Livestock Feed Resources",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Drought in the Pasture: When Rains Fail",
                        "content": {
                            "title": "Drought in the Pasture: When Rains Fail",
                            "caption": "Parched, cracked pasture soil under a blazing sun with dry, sparse grass and grazing livestock searching for feed."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Effects of Drought",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **drought** in an agricultural context.",
                                "Explain how prolonged dry weather reduces the **quantity** of pasture forage.",
                                "Analyze how drought causes pasture **quality** to collapse through moisture loss and lignification.",
                                "Identify the serious **health, production, and economic consequences** of feed scarcity on livestock herds."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Reality of Climate Stress",
                        "content": {
                            "title": "When Pastures Turn from Green to Dust",
                            "text": "**Drought** is a prolonged period of dry weather with little or no rainfall. In agriculture, drought is not just hot weather—it is a severe environmental crisis that halts plant vegetative growth, dries out soil moisture, and leaves grazing herds without feed!"
                        }
                    }
                ],
                # Page 2: Quantity vs. Quality Collapse
                [
                    {
                        "type": "concept_explanation",
                        "title": "How Drought Degrades Livestock Pasture",
                        "content": {
                            "title": "Two-Way Destruction: Quantity and Quality",
                            "text": "Drought attacks pasture in two distinct ways:\n\n- **Decline in Quantity (Volume)**: Without rain, soil moisture vanishes. Grasses stop growing, dry out, and get trampled into dust, drastically reducing the total tonnage of feed available.\n- **Decline in Quality (Nutrient Value)**: Green grass contains up to 80% succulent water, soluble sugars, and vitamins. As drought intensifies, water evaporates, proteins degrade, and the plant builds thick, woody cell walls made of **lignin** and **cellulose** to stay upright."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Wet Season vs. Drought Season Pasture",
                        "content": {
                            "title": "Pasture Properties: Rain vs. Drought",
                            "headers": ["Pasture Property", "Wet Season Pasture", "Drought Season Pasture"],
                            "rows": [
                                ["Physical Appearance", "Deep green, tall, lush, soft to chew", "Pale brown/yellow, brittle, sparse, dusty"],
                                ["Moisture Content", "High (75% - 85% water)", "Extremely low (less than 15% water)"],
                                ["Crude Protein Level", "High (supports heavy milk & growth)", "Very low (proteins break down under intense heat)"],
                                ["Fiber & Lignin", "Low, tender, highly digestible", "Extremely woody, tough, very hard to digest in rumen"],
                                ["Livestock Response", "Rapid weight gain & peak milk yield", "Severe weight loss, emaciation & milk drop"]
                            ]
                        }
                    }
                ],
                # Page 3: The Impact Chain on Livestock & Farmers
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Biological & Economic Drought Impact Chain",
                        "content": {
                            "title": "The Biological & Economic Drought Impact Chain",
                            "caption": "Step-by-step pathway from failed rainfall to plant lignification, livestock malnutrition, and household financial losses."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Consequences for Herds and Farming Families",
                        "content": {
                            "title": "The Domino Effect of Feed Scarcity",
                            "text": "When animals are forced to eat tough, woody, dry pasture, severe complications follow:\n\n- **Livestock Malnutrition & Weight Loss**: Animals expend more energy chewing and digesting woody fiber than they extract in nutrition, leading to rapid muscle wasting.\n- **Plummeting Milk Yield**: Daily milk production can drop by 50% to 80%, devastating family nutrition and daily cash flow.\n- **Increased Disease Susceptibility**: Weakened animals lose immune resistance against tick-borne and respiratory diseases.\n- **Economic Hardship**: Farmers are forced to buy expensive commercial fodder or sell valuable breeding stock at emergency panic prices."
                        }
                    }
                ],
                # Page 4: Scenario Analysis & Practical Diagnostics
                [
                    {
                        "type": "worked_example",
                        "title": "Diagnostic Case Study: Diagnosing Pasture Crisis",
                        "content": {
                            "intro": "Farmer Maina owns 4 dairy cows. During a 4-month dry spell, his communal grazing field has turned completely brown. His cows have lost body condition and milk production has fallen from 40 liters to 12 liters daily.",
                            "steps": [
                                "**Symptom Analysis**: The pasture has lost its green color and moisture, turning highly fibrous and woody.",
                                "**Biological Cause**: The cows are experiencing severe nutrient deficit because woody dry grass cannot provide digestible protein and energy.",
                                "**Economic Consequence**: Maina loses daily milk income while risking the permanent death or forced sale of his breeding cows.",
                                "**Strategic Fix**: Establishing conserved forage reserves (such as baled hay or haystacks) during the rainy season shields the herd from dry-season starvation."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Critical Farming Insight",
                        "content": {
                            "title": "Lignified Grass is Like Cardboard",
                            "text": "When pasture grasses dry up and turn brown, their cell walls become **lignified** (woody). Feeding lignified grass to a cow is like feeding it dry cardboard—it fills the stomach but provides almost zero digestible energy!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Drought Impacts on Pasture",
                        "content": {
                            "question": "How does prolonged drought affect the physical fiber content and digestibility of pasture forage?",
                            "options": [
                                "It completely removes all plant fiber, making grass soft.",
                                "It increases tough, woody fiber (lignin), making the grass very hard to digest.",
                                "It converts dry fiber into liquid sugars and vitamins.",
                                "It turns grasses into high-protein legumes."
                            ],
                            "answer": "B",
                            "explanation": "Drought forces plants to build thick, woody cell walls (lignin and cellulose) to survive dehydration. This makes the dry forage extremely fibrous, tough to chew, and hard for ruminants to digest."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Drought** is a prolonged dry period that halts plant growth and evaporates soil moisture.\n- Drought reduces both pasture **quantity** (total volume) and **quality** (nutritional value).\n- Dry pasture becomes **lignified**, losing water and protein while increasing woody indigestible fiber.\n- Without stored feed, livestock suffer from malnutrition, weight loss, low milk yield, and economic disaster."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Knowing that drought is an inevitable climate reality, how do successful farmers prepare during times of plenty? In the next lesson, we introduce the principles of forage conservation and baled haymaking."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Introduction to Forage Conservation Methods (Baled Haymaking)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Introduction to Forage Conservation Methods (Baled Haymaking)",
            "unit_description": "Feed conservation definition, surplus management, haymaking science, sun-drying moisture reduction, and baling principles.",
            "lesson_title": "Introduction to Forage Conservation Methods (Baled Haymaking)",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Harvesting Sunshine: The Art of Haymaking",
                        "content": {
                            "title": "Harvesting Sunshine: The Art of Haymaking",
                            "caption": "Mowed green pasture grass spread in neat windrows across a sunny farm field to sun-dry for hay."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Haymaking Basics",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **conservation** in relation to agricultural livestock feeds.",
                                "Identify the **three primary forage conservation methods**: baled hay, stacked hay, and standing forage.",
                                "Explain the biological science of **haymaking** and how sun-drying prevents spoilage.",
                                "Describe how compressing dry hay into **bales** saves storage space and eases transport."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Turning Wet-Season Surplus into Dry-Season Security",
                        "content": {
                            "title": "The Meaning of Conservation",
                            "text": "**Feed conservation** is the efficient management of surplus forage produced during rainy seasons by reducing loss and waste so it can be safely stored and fed to livestock during periods of scarcity and drought."
                        }
                    }
                ],
                # Page 2: The Science of Haymaking
                [
                    {
                        "type": "concept_explanation",
                        "title": "What is Hay and How Does Drying Preserve It?",
                        "content": {
                            "title": "The Secret is Moisture Reduction",
                            "text": "**Hay** refers to pasture grasses, legumes, or other forage crops that are cut while green, sun-dried to reduce moisture, and stored safely for future feeding.\n\n- **Fresh Pasture Moisture**: Fresh green grass contains up to 75% to 80% water. If wet grass is piled into a heap, anaerobic bacteria and fungi cause it to rot and heat up dangerously.\n- **The Target Moisture Level**: By spreading cut grass under the hot sun for 2 to 3 days, moisture drops to **15% - 20%**.\n- **Preservation Effect**: At 15% moisture, microbial and fungal activity stops completely, preserving nutrients for months without spoilage."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "The Three Core Forage Conservation Methods",
                        "content": {
                            "title": "Comparison: The Three Forage Conservation Pathways",
                            "headers": ["Conservation Method", "How It is Prepared", "Storage Location", "Primary Advantage"],
                            "rows": [
                                ["Baled Hay", "Forage is cut, sun-dried, and compacted into tight tied blocks (bales)", "Sheltered barn, shed, or covered pallet stack", "Highly compact, saves space, easy to transport and sell"],
                                ["Stacked Hay (Haystacks)", "Loose dry forage is piled neatly into a structured, sloped dome", "Raised outdoor wooden platform with thatch/tarp cover", "Low cost, requires zero baling machinery or boxes"],
                                ["Standing Forage", "Pasture section is fenced off and left uncut to grow undisturbed", "Directly in the pasture field as a living reserve", "Zero harvest labor or processing cost, grazed directly"]
                            ]
                        }
                    }
                ],
                # Page 3: The Compaction Advantage of Baling
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Moisture Reduction and Volume Compaction in Haymaking",
                        "content": {
                            "title": "Moisture Reduction and Volume Compaction in Haymaking",
                            "caption": "Infographic showing moisture dropping from 80% to 15% during sun-drying, followed by volume compaction into dense rectangular bales."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Compress Hay into Bales?",
                        "content": {
                            "title": "Beating Bulkiness",
                            "text": "Loose dry grass is extremely bulky, light, and easily scattered by the wind. Baling compresses huge piles of loose grass into tight, dense blocks:\n\n- **Space Efficiency**: Compacting reduces forage volume by over 70%, allowing hundreds of feeds to fit in a small storeroom.\n- **Ease of Transport**: Uniform bales can be loaded onto wheelbarrows, carts, or trucks without scattering.\n- **Precision Feeding**: Bales allow the farmer to count and ration feed accurately every day."
                        }
                    }
                ],
                # Page 4: Step-by-Step Haymaking Workflow
                [
                    {
                        "type": "step_process",
                        "title": "The 4 Core Stages of Baled Haymaking",
                        "content": {
                            "title": "From Pasture to Barn: The Haymaking Sequence",
                            "steps": [
                                "**Harvest at Early Flowering**: Cut pasture grass just as it begins to flower (50% flowering stage) when protein and sugar content are at their peak.",
                                "**Sun-Drying (Wilting)**: Spread the cut forage evenly in windrows under the hot sun for 2 to 3 days, turning it with a wooden rake to dry uniformly.",
                                "**Compaction & Baling**: Pack the thoroughly dry forage into a baling machine or manual wooden box baler, compress tightly, and tie with sisal twine.",
                                "**Safe Storage**: Stack the completed bales off the ground in a well-ventilated, waterproof barn to protect them from rain and sunlight."
                            ]
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Golden Rule of Haymaking",
                        "content": {
                            "text": "**Never bale wet grass!** If grass is damp when baled, internal moisture will trigger mould growth, build internal heat, and spoil the entire bale."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: The Science of Haymaking",
                        "content": {
                            "question": "Why must harvested forage be dried in the sun until its moisture drops to 15-20% before being stored as hay?",
                            "options": [
                                "To make the grass taste sweeter to animals.",
                                "To increase the physical weight of the bales.",
                                "To stop microbial activity and prevent rotting, heating, and mould growth.",
                                "To change grasses into high-protein legumes."
                            ],
                            "answer": "C",
                            "explanation": "Lowering the moisture content to 15-20% deprives rot-causing bacteria and fungi of the moisture they need to survive. This halts decomposition, prevents toxic mould, and preserves nutrients."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Feed conservation** preserves rainy-season surplus forage for use during dry-season scarcity.\n- The 3 primary methods are **baled hay**, **stacked hay**, and **standing forage**.\n- **Haymaking** involves cutting green pasture at early flowering and sun-drying it to 15-20% moisture.\n- **Baling** compresses bulky dry hay into compact, stackable bricks that save space and ease transport."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Once hay is compressed into bales, how do we classify the different bale shapes, and how do we design storage structures to keep them safe from rain and pests? In the next lesson, we explore bale types and safe storage practices."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Types of Bales and Safe Hay Storage Practices
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Types of Bales and Safe Hay Storage Practices",
            "unit_description": "Bale shapes (rectangular, square, cylindrical), handling advantages, storage threats (moisture, mould, sunlight, pests), and storage facility design.",
            "lesson_title": "Types of Bales and Safe Hay Storage Practices",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Organized Feed Storage: Protecting Baled Hay",
                        "content": {
                            "title": "Organized Feed Storage: Protecting Baled Hay",
                            "caption": "Tightly packed rectangular hay bales stacked systematically inside a dry, well-ventilated farm barn."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Bale Types & Storage",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify the three main shapes of hay bales: **rectangular**, **square**, and **cylindrical (round)**.",
                                "Analyze the operational advantages of compacting hay into rectangular blocks on smallholder farms.",
                                "Examine the environmental threats to stored hay: **moisture, direct sunlight, mould, and rodents**.",
                                "Design a safe, well-ventilated hay storage facility elevated off the ground."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Geometry of Hay Storage",
                        "content": {
                            "title": "Why Bale Shape Matters",
                            "text": "Compacted hay bales are produced in three distinct geometric shapes depending on farm equipment and herd size. Choosing the right bale shape determines how easily feed can be stacked, moved, and protected from spoilage."
                        }
                    }
                ],
                # Page 2: Classification of Bale Shapes
                [
                    {
                        "type": "comparison_table",
                        "title": "Characteristics of Hay Bale Shapes",
                        "content": {
                            "title": "Classification Matrix: Hay Bale Geometries",
                            "headers": ["Bale Shape", "Physical Structure", "Key Advantage", "Ideal Farm Scale"],
                            "rows": [
                                ["Rectangular Bales", "Box-like blocks with flat sides (approx. 40cm x 50cm x 75cm)", "Lightweight, easy to lift by hand, stacks tightly like bricks", "Small to medium smallholder farms"],
                                ["Square Bales", "Large, dense cubic blocks (often over 200kg)", "High density, holds maximum volume per square meter", "Large mechanized commercial farms"],
                                ["Cylindrical (Round) Bales", "Large circular rolls wrapped in netting", "Curved outer surface naturally sheds rain if stored outdoors", "Large ranches with tractor front-loaders"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Smallholder Advantage",
                        "content": {
                            "title": "Why Rectangular Bales Rule Smallholder Farming",
                            "text": "**Rectangular bales** are the gold standard for smallholder farmers across Kenya. They can be produced using cheap manual wooden boxes, carried by one person, and stacked to the ceiling in small barns without heavy machinery!"
                        }
                    }
                ],
                # Page 3: The Enemies of Stored Hay & Spoilage Prevention
                [
                    {
                        "type": "concept_explanation",
                        "title": "Storage Threats: Moisture, Mould, and Sunlight",
                        "content": {
                            "title": "Protecting the Investment",
                            "text": "Even perfectly dried hay will spoil rapidly if stored improperly:\n\n- **Soil Dampness (Rising Moisture)**: Bare earth transfers capillary moisture into bottom bales, turning them into a mushy, rotten fungal breeding ground.\n- **Rain Leaks**: Roof leaks create moisture pockets where toxic fungi (such as *Aspergillus*) produce hazardous **mycotoxins**.\n- **Direct Sunlight (Bleaching)**: Ultraviolet rays destroy Vitamin A and bleach golden-green hay into tasteless gray fiber.\n- **Poor Ventilation**: Trapped humidity causes heat build-up and spontaneous heating."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Engineering Blueprint: A Safe, Weatherproof Hay Storage Facility",
                        "content": {
                            "title": "Engineering Blueprint: A Safe, Weatherproof Hay Storage Facility",
                            "caption": "Cross-sectional blueprint of a ventilated hay barn showing elevated wooden pallets, rainproof roof, and rodent-proof barriers."
                        }
                    }
                ],
                # Page 4: Rules for Safe Hay Storage
                [
                    {
                        "type": "step_process",
                        "title": "4 Golden Rules for Safe Hay Storage",
                        "content": {
                            "title": "Building a Rot-Proof Hay Stack",
                            "steps": [
                                "**Elevate Off the Ground**: Never place bales on bare soil. Stack bales on wooden pallets or timber poles at least 30cm off the floor to allow air circulation.",
                                "**Ensure Overhead Rain Protection**: Store under a leak-proof corrugated iron or thatch roof. If stacking outdoors, drape heavy waterproof tarpaulins secured with weighted ropes.",
                                "**Maintain Cross-Ventilation**: Leave narrow air gaps between bale stacks and keep side walls open or meshed to prevent heat and humidity accumulation.",
                                "**Implement Rodent Control**: Keep the floor clean and clear brush around the shed to prevent mice and rats from nesting and tearing twine."
                            ]
                        }
                    },
                    {
                        "type": "common_mistake",
                        "title": "Common Storage Mistake",
                        "content": {
                            "text": "**Stacking bales directly on concrete or dirt without pallets.** Even concrete floors sweat in humid weather! Always place a layer of timber pallets or dry straw beneath your bottom bales to create an insulating air barrier."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Safe Hay Storage",
                        "content": {
                            "question": "Why is it dangerous to stack hay bales directly on bare soil inside a storeroom?",
                            "options": [
                                "Soil dampness rises through capillary action, causing bottom bales to rot and grow toxic mould.",
                                "Bare soil attracts domestic livestock into the storeroom.",
                                "Soil causes the hay bales to lose weight and turn into liquid.",
                                "Soil bleaches the green color out of the hay."
                            ],
                            "answer": "A",
                            "explanation": "Bare soil contains moisture that seeps upward into compacted hay. This creates a damp environment where fungal mould flourishes, ruining the feed and producing toxins dangerous to livestock."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Bales are produced in **rectangular**, **square**, or **cylindrical (round)** geometries.\n- Rectangular bales are ideal for small farms because they are hand-portable and stack neatly.\n- The greatest threats to stored hay are **ground moisture**, **rain leaks**, **sun bleaching**, and **rodents**.\n- Safe storage requires **elevated pallets**, a **waterproof roof**, **good airflow**, and **dry conditions**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have explored processing and storing mowed hay. But what if a farmer has no storage shed or baling equipment? In the next lesson, we examine standing forage—conserving pasture feed directly in the field."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Meaning, Preparation, and Management of Standing Forage
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Meaning, Preparation, and Management of Standing Forage",
            "unit_description": "Standing forage concept, living pasture banking, zero-harvest benefits, ecological and climatic risks, and land requirement analysis.",
            "lesson_title": "Meaning, Preparation, and Management of Standing Forage",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Living Pasture Bank: Standing Forage",
                        "content": {
                            "title": "The Living Pasture Bank: Standing Forage",
                            "caption": "A dense, tall stand of Napier grass and Rhodes grass fenced off during the wet season to serve as a dry-season standing feed bank."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Standing Forage",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **standing forage** as a low-cost feed conservation method.",
                                "Explain how standing forage acts as a **living pasture bank** for the dry season.",
                                "Analyze the operational and biological **advantages** of standing forage (zero processing, direct grazing).",
                                "Evaluate the **risks and limitations** of standing forage, including land requirements, wildfires, and weather exposure."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Conserving Feed Without Harvesting",
                        "content": {
                            "title": "The Nature-Based Pasture Bank",
                            "text": "**Standing forage** refers to pasture or forage crops that are left uncut, ungrazed, and undisturbed in the field during the rainy season so they can be grazed directly by livestock in the future when drought hits."
                        }
                    }
                ],
                # Page 2: Operational Advantages of Standing Forage
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Farmers Utilize Standing Forage",
                        "content": {
                            "title": "Zero Processing, Zero Machinery",
                            "text": "Standing forage is one of the most accessible conservation methods for resource-constrained farmers:\n\n- **Zero Processing Costs**: Requires no cutting tools, drying labor, sisal twines, baling boxes, or storage barns.\n- **Consumed Fresh**: Livestock graze the pasture directly, consuming plants with intact root systems.\n- **Weather Independent**: Unlike haymaking (which requires 3 consecutive sunny days to dry grass), standing forage can be accessed in cloudy or wet weather without spoilage."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Standing Forage vs. Baled Hay",
                        "content": {
                            "title": "Operational Profile: Standing Forage vs. Baled Hay",
                            "headers": ["Management Feature", "Standing Forage (Field Banking)", "Baled Hay (Barn Storage)"],
                            "rows": [
                                ["Equipment Needed", "Fencing and gates only", "Panga, rake, baling box/machine, sisal twine"],
                                ["Labor Requirement", "Very low (animals graze themselves)", "High (cutting, turning, packing, tying, transporting)"],
                                ["Storage Infrastructure", "Zero (stored standing in field soil)", "Requires dry, well-ventilated covered barn"],
                                ["Weather Vulnerability", "High (exposed to wildfires, hailstones, floods)", "Low (safely sheltered inside barn)"],
                                ["Land Requirement", "Large (requires dedicated fenced pastures)", "Small (compact bales store in small shed)"]
                            ]
                        }
                    }
                ],
                # Page 3: Environmental Risks & Vulnerabilities
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Standing Forage Pasture Banking Cycle & Risk Factors",
                        "content": {
                            "title": "The Standing Forage Pasture Banking Cycle & Risk Factors",
                            "caption": "Diagram illustrating the seasonal reservation of pasture banks alongside outdoor risk threats (wildfires, hail, floods, overgrazing)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Vulnerabilities of Leaving Feed Outdoors",
                        "content": {
                            "title": "Outdoor Exposure Threats",
                            "text": "While cheap, leaving feed standing in an open field involves significant risks:\n\n- **Wildfire Hazard**: During intense droughts, dry standing grass is highly flammable. A single accidental spark can incinerate a farm's entire feed reserve in minutes.\n- **Severe Weather Damage**: Hailstones and flash floods can flatten and wash away standing pasture.\n- **High Land Demand**: Setting aside large pastures is impossible on tiny smallholder plots under 1 acre.\n- **Nutrient Dilution**: As standing grass overmatures and flowers, its protein level naturally declines over time compared to early-cut baled hay."
                        }
                    }
                ],
                # Page 4: Decision Framework for Smallholders
                [
                    {
                        "type": "worked_example",
                        "title": "Farm Decision Matrix: Choosing the Right Method",
                        "content": {
                            "intro": "How does a Grade 9 agriculture student advise a local farmer on whether to use Standing Forage or Box-Baling?",
                            "steps": [
                                "**Scenario A (Large Land, Low Labor)**: A farmer with 10 acres and 5 cows should use **Standing Forage** by fencing off 3 acres as a deferred pasture bank.",
                                "**Scenario B (Small Plot, High Labor)**: A farmer with 0.5 acres and 2 zero-grazed cows should harvest grass and make **Baled Hay**, because land is too limited for pasture banking.",
                                "**Scenario C (High Fire Risk Zone)**: In dry savanna zones prone to grass fires, harvesting and storing **Baled Hay** in a sheltered barn is far safer than standing forage."
                            ]
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Local Farm Evaluation",
                        "content": {
                            "title": "Evaluate Your Neighborhood",
                            "instruction": "Interview a local livestock keeper. Ask whether they leave standing grass in their paddocks for dry months or make hay. Note down their primary reason (land size, labor, or lack of storage)."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Standing Forage Trade-offs",
                        "content": {
                            "question": "Which of the following is a major environmental risk of conserving feed as standing forage in the field?",
                            "options": [
                                "It requires expensive wooden baling boxes.",
                                "It can be completely destroyed by dry-season wildfires, hailstones, or floods.",
                                "It rots immediately when exposed to sunlight.",
                                "It turns into dry wheat straw."
                            ],
                            "answer": "B",
                            "explanation": "Because standing forage remains outdoors in open pastures, it is vulnerable to environmental hazards such as dry-season wildfires, hailstones, and pest infestations."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Standing forage** is pasture left uncut and undisturbed to serve as a living dry-season feed bank.\n- It requires **zero machinery or processing labor** and allows direct grazing in any weather.\n- Its key limitations are **high land requirements**, **exposure to wildfires and hailstones**, and **natural nutrient decline**.\n- To succeed, the deferred pasture must be large enough to sustain the herd throughout the dry season."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "If animals are allowed to roam freely into standing forage, they will trample and ruin the grass in days. How do we manage grazing systematically? In the next lesson, we explore rotational grazing, paddocking, and stocking rate management."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Advanced Field Management Techniques for Standing Forage
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Advanced Field Management Techniques for Standing Forage",
            "unit_description": "Paddocking, rotational grazing cycles, deferred grazing strategy, stocking rate vs carrying capacity, and overgrazing prevention.",
            "lesson_title": "Advanced Field Management Techniques for Standing Forage",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Precision Pasture Management: Fenced Paddocks",
                        "content": {
                            "title": "Precision Pasture Management: Fenced Paddocks",
                            "caption": "Dairy cattle grazing inside a fenced paddock while adjacent pasture plots rest and regrow."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Grazing Management",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain how **paddocking** and **rotational grazing** maximize pasture productivity.",
                                "Describe **deferred grazing** as a systematic method for banking standing forage.",
                                "Define **stocking rate** and **carrying capacity** to prevent destructive overgrazing.",
                                "Calculate pasture rest and grazing cycles for sustainable livestock production."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Problem with Continuous Grazing",
                        "content": {
                            "title": "Why Free-Roaming Kills Pasture",
                            "text": "If cattle have unrestricted access to an entire farm all year, they selectively eat only the sweetest young grass shoots, trample tall forage, and never allow root systems to rest. The pasture quickly degrades into bare, weed-infested soil."
                        }
                    }
                ],
                # Page 2: Paddocking and Rotational Cycles
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Mechanics of Rotational Grazing",
                        "content": {
                            "title": "Divide, Graze, Rest, and Regrow",
                            "text": "**Paddocking** is the practice of dividing a farm's pasture into smaller, fenced sections called **paddocks**.\n\n- **The Grazing Period**: Livestock are placed in Paddock 1 for a short, controlled time (e.g. 4 to 7 days) until grass is grazed to a safe stubble height (approx. 5cm).\n- **The Move**: Livestock are moved to Paddock 2.\n- **The Rest Period**: While animals graze Paddock 2, Paddock 1 rests undisturbed for 30 to 45 days, allowing grass roots to recharge, store starches, and produce lush new leaves."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "6-Paddock Rotational & Deferred Grazing System Blueprint",
                        "content": {
                            "title": "6-Paddock Rotational & Deferred Grazing System Blueprint",
                            "caption": "Spatial farm blueprint showing a 6-paddock layout with active grazing, regrowing paddocks, and a deferred standing forage reserve."
                        }
                    }
                ],
                # Page 3: Deferred Grazing and Stocking Rate Control
                [
                    {
                        "type": "concept_explanation",
                        "title": "Deferred Grazing (Pasture Banking)",
                        "content": {
                            "title": "Locking the Gate for Dry Times",
                            "text": "**Deferred grazing** is a specialized rotational strategy where a farmer deliberately leaves one or more paddocks completely untouched throughout the entire rainy growing season.\n\n- While livestock rotate through Paddocks 1 to 5, the deferred paddock (Paddock 6) grows tall, dense, and seed-rich.\n- When the dry season arrives and normal paddocks stop growing, the farmer unlocks the deferred paddock to provide an abundant standing feed supply."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Balancing Animal Demand and Pasture Supply",
                        "content": {
                            "title": "Stocking Rate Concepts and Ecological Balance",
                            "headers": ["Management Metric", "Definition", "Farm Consequence if Imbalanced"],
                            "rows": [
                                ["Carrying Capacity", "The maximum number of animals a pasture can sustain without degradation", "Underestimating capacity leaves surplus grass unutilized"],
                                ["Stocking Rate", "The actual number of animals grazing a specific area over time", "Overstocking causes severe overgrazing, bare soil & erosion"],
                                ["Strategic Destocking", "Selling older or unproductive livestock at the start of drought", "Preserves scarce pasture and hay for productive breeding stock"]
                            ]
                        }
                    }
                ],
                # Page 4: Mathematical Calculation: Grazing Rest Cycles
                [
                    {
                        "type": "worked_example",
                        "title": "Pasture Mathematics: Calculating Rest Periods",
                        "content": {
                            "intro": "Let us calculate the recovery rest time for a farm divided into 6 paddocks:",
                            "steps": [
                                "**Farm Setup**: The farm has 6 paddocks.",
                                "**Grazing Duration**: Cows spend 5 days grazing in each paddock before moving to the next.",
                                "**Total Cycle Length**: 6 paddocks × 5 days = 30 days for a full farm rotation.",
                                "**Rest Calculation**: When cows leave Paddock 1, they spend 5 days × 5 other paddocks = 25 days elsewhere.",
                                "**Conclusion**: Paddock 1 enjoys **25 full days of rest** to regrow its root system and foliage before cows return!"
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Ecological Rule of Thumb",
                        "content": {
                            "title": "Take Half, Leave Half",
                            "text": "Never allow cows to graze pasture down to the bare roots. Grazing only the top 50% of the grass blade leaves the plant with enough green leaf area to photosynthesize and regrow rapidly!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Pasture Management Strategies",
                        "content": {
                            "question": "Farmer Amina divides her 6-acre pasture into 6 fenced paddocks. She moves her cows weekly and leaves Paddock 6 completely untouched throughout the rainy season to feed her herd during the dry spell. What technique is she practicing in Paddock 6?",
                            "options": [
                                "Continuous Overstocking",
                                "Deferred Grazing (Pasture Banking)",
                                "Mechanical Weed Control",
                                "Uncontrolled Burning"
                            ],
                            "answer": "B",
                            "explanation": "Deferred grazing is the practice of delaying grazing on a specific paddock during the main growing season, allowing the forage to accumulate undisturbed so it can serve as a standing feed reserve in the dry season."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Paddocking** divides pasture into small, fenced fields to control grazing intensity.\n- **Rotational grazing** systematically moves herds through paddocks, giving rested fields time to regenerate.\n- **Deferred grazing** sets aside a dedicated paddock during rains to build a standing dry-season feed bank.\n- **Stocking rate** must balance the land's **carrying capacity** to prevent destructive overgrazing."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have seen how to manage standing pasture. But what if a farmer wants to harvest and store mowed loose forage without expensive baling machinery? In the next lesson, we introduce stacking (haystacks)."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Stacking (Haystacks) as a Forage Conservation Method
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Stacking (Haystacks) as a Forage Conservation Method",
            "unit_description": "Stacking definition, raised wooden platform engineering, sloped roof water-shedding design, and thatch/tarp weatherproofing.",
            "lesson_title": "Stacking (Haystacks) as a Forage Conservation Method",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Agricultural Engineering: The Haystack",
                        "content": {
                            "title": "Traditional Agricultural Engineering: The Haystack",
                            "caption": "A classic, well-constructed haystack built on a raised wooden platform with a steeply sloped crown to shed rainwater."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Haystacking Science",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **stacking (haystacks)** as a low-technology forage conservation method.",
                                "Analyze the structural engineering principles of a weatherproof haystack.",
                                "Explain why haystacks must be built on **raised platforms** with **sloped roofs**.",
                                "Compare the cost, labor, and space trade-offs of stacked hay versus baled hay."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Conserving Bulk Hay Without Machines",
                        "content": {
                            "title": "Smart Farm Architecture",
                            "text": "**Stacking** (or creating haystacks) refers to piling loose, sun-dried forage—such as pasture grass, maize stover, sorghum stalks, or wheat straw—into a structured mound on a raised surface to protect it from moisture and weather."
                        }
                    }
                ],
                # Page 2: Engineering a Weatherproof Haystack
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Architectural Pillars of a Safe Haystack",
                        "content": {
                            "title": "Why Haystacks Don't Rot",
                            "text": "A properly engineered haystack incorporates four essential design features:\n\n- **1. The Raised Platform Foundation**: Sturdy wooden posts and timber rafters elevate the stack at least **30cm off the ground**, allowing air to circulate underneath and blocking rising ground moisture.\n- **2. Compacted Core**: Loose dry forage is packed and stamped down tightly in layers to eliminate air pockets.\n- **3. Sloped Crown (The Roof)**: The top layers are tapered into a steep cone or wedge (like a house roof) so rainwater slides off the sides rather than pooling on top.\n- **4. Waterproof Thatch / Tarpaulin**: The sloped top is covered with thatch grass or plastic sheeting secured with weighted ropes."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Engineering Cross-Section of a Weatherproof Haystack",
                        "content": {
                            "title": "Engineering Cross-Section of a Weatherproof Haystack",
                            "caption": "Detailed architectural cross-section of a haystack showing the 30cm raised wooden platform, compacted core, sloped crown, and weighted tie ropes."
                        }
                    }
                ],
                # Page 3: Trade-Off Analysis: Stacking vs. Baling
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Stacked Hay vs. Baled Hay",
                        "content": {
                            "title": "Operational Profile: Stacked Hay vs. Baled Hay",
                            "headers": ["Evaluation Criteria", "Stacked Hay (Haystack)", "Baled Hay (Box-Baled)"],
                            "rows": [
                                ["Machinery & Equipment", "Zero machinery (built with simple hand tools and timber)", "Requires wooden box baler or mechanical baler and twine"],
                                ["Capital Cost", "Extremely low (uses locally available poles and thatch)", "Low to moderate (requires purchasing sisal twine)"],
                                ["Farm Space Requirement", "High (loose stacks take up large open yard space)", "Low (compact bales store tightly to the ceiling in sheds)"],
                                ["Portability & Sale", "Poor (loose hay cannot be transported or sold easily)", "Excellent (compact bales are easily loaded and marketed)"],
                                ["Weather Exposure", "Moderate (outer layer exposed to wind and sun)", "Very low (completely enclosed in sheltered barn)"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Design Warning",
                        "content": {
                            "title": "Never Build a Flat-Topped Haystack!",
                            "text": "If the top of a haystack is flat, rainwater will pool, seep straight down into the core, and rot the entire feed reserve in a few days. Always shape the top into a steep slope like a house roof!"
                        }
                    }
                ],
                # Page 4: Diagnosing Structural Mistakes
                [
                    {
                        "type": "worked_example",
                        "title": "Diagnostic Exercise: Inspecting Haystack Faults",
                        "content": {
                            "intro": "An agricultural officer inspects a newly constructed haystack on a school farm. What structural flaws must be corrected?",
                            "steps": [
                                "**Flaw 1 (Direct Ground Contact)**: The hay is piled directly on damp dirt -> *Fix*: Dismantle and construct a 30cm raised timber platform.",
                                "**Flaw 2 (Flat Roof)**: The top is flat and unpitched -> *Fix*: Add more dry forage to shape the crown into a steep 45-degree cone.",
                                "**Flaw 3 (Loose Cover)**: A plastic sheet is thrown on top without ropes -> *Fix*: Drape sisal twines across the sheet and tie heavy stones to the ends as counterweights."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Haystack Engineering",
                        "content": {
                            "question": "Why is it absolutely necessary to construct a haystack on a raised wooden platform of posts and rafters rather than directly on bare earth?",
                            "options": [
                                "To make the haystack look more attractive.",
                                "To protect the base from rising ground moisture and allow ventilating air to flow beneath.",
                                "To prevent wild birds from nesting in the grass.",
                                "To let domestic livestock graze directly from the bottom."
                            ],
                            "answer": "B",
                            "explanation": "Soil contains moisture that moves upward via capillary action. Building a raised platform (at least 30cm high) stops ground moisture from rotting the bottom layers and provides an airflow gap to keep the stack dry."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Stacking** is piling loose dry forage into a structured mound on a raised surface.\n- It is **extremely low-cost**, requires **zero baling machinery**, and utilizes local timber.\n- Essential design features include a **30cm raised platform**, a **compacted core**, a **sloped crown**, and a **weighted cover**.\n- Stacking takes up more space than baling and leaves the outer layer exposed to weathering."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What if a farmer wants the compact, space-saving advantages of rectangular bales without buying an expensive tractor machine? In the next lesson, we explore manual box-bailing concepts and equipment."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Box-Bailing Concepts and Equipment
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Box-Bailing Concepts and Equipment",
            "unit_description": "Manual box baler mechanics, standard dimensions (40cm x 50cm x 75cm), sisal twine routing, compaction physics, and required farm tools.",
            "lesson_title": "Box-Bailing Concepts and Equipment",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Appropriate Technology: The Manual Box Baler",
                        "content": {
                            "title": "Appropriate Technology: The Manual Box Baler",
                            "caption": "A sturdy handcrafted wooden box baler with sisal twines positioned inside, ready for manual hay compaction."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Box-Bailing Concepts",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **box-bailing** as a manual, low-cost method for compacting hay.",
                                "Identify the standard dimensions and construction materials of a **wooden box baler**.",
                                "Explain the mechanical purpose and pre-packing placement of **sisal twines**.",
                                "List the essential tools, protective gear, and materials required for manual baling."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Empowering Smallholders with Simple Mechanics",
                        "content": {
                            "title": "Baling Without Tractors",
                            "text": "**Box-bailing** is a manual haymaking technique where sun-dried forage is compressed inside a rectangular wooden or metal box mold to create uniform, tightly tied bales without expensive motorized machinery."
                        }
                    }
                ],
                # Page 2: Standard Dimensions and Tool Inventory
                [
                    {
                        "type": "concept_explanation",
                        "title": "Anatomy of the Wooden Box Baler",
                        "content": {
                            "title": "The 40cm x 50cm x 75cm Standard",
                            "text": "A standard manual wooden box baler is constructed from sturdy timber planks with standard dimensions:\n\n- **Width**: 40cm\n- **Height**: 50cm\n- **Length**: 75cm\n- **Hinged Side Door**: Allows the completed, compressed bale to be removed effortlessly without tearing."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Equipment and Materials Inventory for Box-Bailing",
                        "content": {
                            "title": "Tools, Materials, and Safety Equipment",
                            "headers": ["Item Name", "Category", "Specific Agricultural Function"],
                            "rows": [
                                ["Wooden Box Baler", "Mold & Press", "Serves as the structural chamber to shape and compress rectangular bales"],
                                ["Sisal Twine / String", "Binding Material", "Binds and locks the compacted hay bale tightly to preserve density"],
                                ["Panga / Sickle", "Cutting Tool", "Harvests green pasture grass and chops tough maize stovers"],
                                ["Wooden Rake", "Gathering Tool", "Spreads mowed forage for sun-drying and gathers dry hay into piles"],
                                ["Leather Gloves", "Protective Gear", "Protects hands from blisters, sharp stalks, and twine friction cuts"],
                                ["Gumboots", "Protective Gear", "Protects feet and provides solid downward force while stamping hay"]
                            ]
                        }
                    }
                ],
                # Page 3: The Golden Rule of Twine Routing
                [
                    {
                        "type": "suggested_diagram",
                        "title": "3D Blueprint of a Wooden Box Baler & Pre-Packing Twine Routing",
                        "content": {
                            "title": "3D Blueprint of a Wooden Box Baler & Pre-Packing Twine Routing",
                            "caption": "Transparent blueprint showing the 40cm x 50cm x 75cm box baler with sisal twines routed along the walls and floor before forage is loaded."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Twines Go In First",
                        "content": {
                            "title": "The Pre-Packing Rule",
                            "text": "Before adding a single handful of grass into the box, two lengths of **sisal twine** (each approx. 2.5 meters long) must be laid inside the empty chamber:\n\n- The twines run down the front wall, flat across the floor, and up the back wall.\n- The loose ends hang over the outer edges.\n- **Why?** Once the hay is packed and heavily compressed, it is physically impossible to thread strings under the dense bale!"
                        }
                    }
                ],
                # Page 4: Step-by-Step Box-Baling Mechanics
                [
                    {
                        "type": "step_process",
                        "title": "The Mechanical Sequence of Box-Bailing",
                        "content": {
                            "title": "How Loose Grass Becomes a Solid Bale",
                            "steps": [
                                "**Position Twines**: Lay two sisal twines along the walls and floor of the empty wooden box with ends hanging outside.",
                                "**Layer and Stamp**: Add a 20cm layer of dry grass and stamp heavily with gumboots (or a wooden plunger) to compress out all air pockets.",
                                "**Repeat to Capacity**: Continue adding layers and stamping until the compressed forage reaches the top rim of the box.",
                                "**Pull and Knot**: Pull the twine ends tightly across the top of the hay, apply maximum body weight, and tie secure double knots.",
                                "**Unlatch and Extract**: Open the hinged side door and slide out the solid rectangular hay bale."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Box-Baling Operations",
                        "content": {
                            "question": "When preparing to make a rectangular bale inside a manual wooden box baler, at what exact step should the farmer place the sisal twines into the box?",
                            "options": [
                                "After the box is completely packed and compacted with grass.",
                                "Halfway through compaction, when the box is half-full.",
                                "Into the empty box baler before any forage is added.",
                                "Only after the completed bale has been lifted out of the box."
                            ],
                            "answer": "C",
                            "explanation": "Sisal twines must always be positioned in the empty box first, running down the walls and across the bottom. If grass is packed first, the twines cannot be threaded underneath the dense, heavy compressed hay."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Box-bailing** is a manual, affordable technique for producing rectangular hay bales without motorized machinery.\n- The standard smallholder box baler measures **40cm width x 50cm height x 75cm length**.\n- Essential equipment includes the **box baler**, **sisal twine**, **panga**, **rake**, **gloves**, and **gumboots**.\n- **Sisal twines must be laid inside the empty box first** before forage is loaded and stamped."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we understand the tools and concepts of both stacking and baling, let us step onto the school farm for our practical sessions! In the next lesson, we construct a real-world haystack."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Practical Activity: Preparing and Conserving Forage using Stacking
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Practical Activity: Preparing and Conserving Forage using Stacking",
            "unit_description": "Hands-on field construction of a raised timber platform, building a compacted haystack core, shaping the sloped roof crown, and securing weatherproof covers.",
            "lesson_title": "Practical Activity: Preparing and Conserving Forage using Stacking",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "School Farm Practical: Building a Weatherproof Haystack",
                        "content": {
                            "title": "School Farm Practical: Building a Weatherproof Haystack",
                            "caption": "Agriculture students collaborating on a school farm to construct a raised timber frame for loose hay storage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: Haystack Construction",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Select a well-drained, sheltered site on the school farm for haystack construction.",
                                "Construct a sturdy **raised timber platform** at least 30cm off the ground using local posts and rafters.",
                                "Build and compact the **haystack core** using sun-dried grass, maize stover, and sorghum straw.",
                                "Shape a **sloped crown roof** and secure a waterproof thatch or tarpaulin cover with weighted tie ropes."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hands-On Agricultural Engineering",
                        "content": {
                            "title": "Putting Theory into Practice",
                            "text": "Today, we become agricultural engineers! Working in safety-equipped teams, we will build a full-scale, rot-proof haystack to conserve school-farm forage for the dry season."
                        }
                    }
                ],
                # Page 2: Materials & Safety Protocols
                [
                    {
                        "type": "comparison_table",
                        "title": "Field Materials, Tools, and Safety Checklist",
                        "content": {
                            "title": "Practical Session Checklist",
                            "headers": ["Component / Stage", "Required Materials & Tools", "Safety & Quality Requirement"],
                            "rows": [
                                ["Platform Construction", "4 heavy wooden corner posts, timber planks (rafters), nails, hammer, crowbar, saw", "Dig corner posts 40cm deep for stability; ensure platform is at least 30cm high"],
                                ["Forage Stock", "Thoroughly sun-dried Rhodes grass, maize stovers, wheat straw", "Verify forage is 100% dry (15-20% moisture); never stack damp grass"],
                                ["Roof & Weatherproofing", "Waterproof plastic tarpaulin or thatch grass, sisal twines, heavy stones/logs", "Tie ropes tightly across cover and hang counterweight stones on sides"],
                                ["Personal Protective Equipment", "Leather work gloves, gumboots, dust masks", "Wear gloves when handling rough timber and gumboots when treading in soil"]
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "4-Stage Haystack Construction Process Flow",
                        "content": {
                            "title": "4-Stage Haystack Construction Process Flow",
                            "caption": "Step-by-step visual process flow from bare ground to raised platform, compacted core, and sloped weighted cover."
                        }
                    }
                ],
                # Page 3: Step-by-Step Practical Field Procedure
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Haystack Construction",
                        "content": {
                            "title": "Step-by-Step Field Instructions",
                            "steps": [
                                "**Site Selection & Ground Prep**: Choose a flat, elevated, well-drained site protected from strong winds.",
                                "**Build the Raised Platform**: Dig holes with a crowbar, plant 4 sturdy corner posts, and nail horizontal timber rafters across them to build a platform 30cm above the ground.",
                                "**Build & Compact the Core**: Layer loose dry forage onto the platform, pressing and stamping down each layer firmly to squeeze out air pockets as the stack rises to 1.5 meters.",
                                "**Shape the Sloped Crown**: As the stack reaches peak height, taper the top layers into a sharp 45-degree ridge or cone to shed rain.",
                                "**Cover & Anchor**: Drape a waterproof sheet or thick layer of thatch over the sloped top, pass sisal twines across, and hang heavy stones on the ends to resist wind."
                            ]
                        }
                    }
                ],
                # Page 4: Quality Inspection & Troubleshooting
                [
                    {
                        "type": "worked_example",
                        "title": "Field Quality Inspection Protocol",
                        "content": {
                            "intro": "How to inspect and verify the quality of your completed haystack:",
                            "steps": [
                                "**Airflow Check**: Look underneath the platform. Air should circulate freely under the timber rafters with zero grass touching bare dirt.",
                                "**Water-Shedding Check**: Pour a cup of water over the top cover. Water must stream down the sloped sides immediately without pooling.",
                                "**Wind-Resistance Check**: Gently shake the side ropes. The hanging counterweight stones should keep the cover taut and immovable."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Practical Stacking Safety",
                        "content": {
                            "question": "Why do farmers hang heavy stones or logs at the ends of sisal twines draped across a haystack cover?",
                            "options": [
                                "To compress the grass inside the stack.",
                                "To prevent wild animals from climbing onto the platform.",
                                "To weigh down the waterproof cover so strong winds do not blow it away.",
                                "To decorate the farm."
                            ],
                            "answer": "C",
                            "explanation": "During rainstorms, strong wind gusts can easily lift and tear tarpaulins or thatch off haystacks. Counterweight stones hanging on the twine ends provide constant tension that keeps the roof cover firmly anchored."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Practical haystacking protects dry loose forage through sound **structural engineering**.\n- A **30cm raised platform** blocks soil moisture and provides essential bottom ventilation.\n- A **steeply sloped crown** ensures rainwater slides off instantly without soaking the core.\n- **Counterweighted ropes** anchor the protective cover against strong storms."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we have constructed a loose haystack, let us master the practical skills of manual box-bailing! In the next lesson, we will pack, stamp, tie, and release real rectangular hay bales."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Practical Activity: Box-Bailing Hay using Locally Available Materials
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Practical Activity: Box-Bailing Hay using Locally Available Materials",
            "unit_description": "Hands-on field box-baling, twine positioning, incremental layering and stamping, reef knot tying, bale extraction, and storage stacking.",
            "lesson_title": "Practical Activity: Box-Bailing Hay using Locally Available Materials",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hands-On Baling: Compacting Grass into Bricks",
                        "content": {
                            "title": "Hands-On Baling: Compacting Grass into Bricks",
                            "caption": "Agricultural students wearing gumboots stamping dry forage inside a manual wooden box baler."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: Manual Box-Baling",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Set up a wooden box baler (40cm × 50cm × 75cm) on flat, dry ground.",
                                "Route two lengths of **sisal twine** correctly inside the empty box prior to loading forage.",
                                "Pack, stamp, and compress sun-dried grass incrementally to achieve high bale density.",
                                "Tie secure **reef knots** and extract a firm, rectangular hay bale ready for dry storage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Art of the Perfect Bale",
                        "content": {
                            "title": "Transforming Loose Grass into Market-Ready Bales",
                            "text": "Today, every team will operate a manual box baler to produce standard rectangular hay bales that can be stacked, stored, or sold!"
                        }
                    }
                ],
                # Page 2: Step-by-Step Practical Operation
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Step Manual Box-Baling Operation Workflow",
                        "content": {
                            "title": "5-Step Manual Box-Baling Operation Workflow",
                            "caption": "Step-by-step workflow showing twine placement, incremental stamping, top packing, reef knot tying, and bale extraction."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Box-Bailing",
                        "content": {
                            "title": "Step-by-Step Baling Instructions",
                            "steps": [
                                "**Box Preparation & Twine Routing**: Place the box baler on level ground. Cut two 2.5m lengths of sisal twine and lay them inside the empty box—down the front wall, along the floor, and up the back wall, letting the ends hang outside.",
                                "**Incremental Layering & Stamping**: Throw in an armful of dry grass (20cm layer). Step into the box and stamp firmly with gumboots to compress out air pockets.",
                                "**Fill to Capacity**: Continue adding layers and stamping vigorously until the compressed forage reaches the top rim of the box.",
                                "**Knotting the Bale**: Pull the hanging twine ends over the top of the hay, pull them as tight as possible using your body weight, and tie secure double knots.",
                                "**Bale Extraction**: Open the side door latch and slide out the solid, brick-like rectangular hay bale.",
                                "**Store Elevated**: Carry the bale to the storage shed and stack it on wooden pallets off the ground."
                            ]
                        }
                    }
                ],
                # Page 3: Bale Quality Evaluation & Troubleshooting
                [
                    {
                        "type": "comparison_table",
                        "title": "Bale Quality Diagnostic Guide",
                        "content": {
                            "title": "Troubleshooting Common Box-Baling Faults",
                            "headers": ["Bale Fault", "Underlying Operational Cause", "Corrective Action for Next Bale"],
                            "rows": [
                                ["Bale sags or falls apart when lifted", "Twines were tied too loosely or knot slipped", "Pull twines with full body weight and tie tight double reef knots"],
                                ["Bale is light, spongy, and fluffy", "Insufficient stamping between forage layers", "Stamp firmly after every 20cm layer of grass loaded"],
                                ["Bale turns black, hot, and smelly in barn", "Forage was baled with high moisture (damp grass)", "Always sun-dry grass for 2-3 days until moisture drops to 15-20%"],
                                ["Twines cannot be tied around bale", "Forgot to place twines in box before loading grass", "Always lay twines inside the empty box before adding any forage"]
                            ]
                        }
                    }
                ],
                # Page 4: Practical Reflection
                [
                    {
                        "type": "mini_activity",
                        "title": "Team Bale Audit",
                        "content": {
                            "title": "Test Your Finished Bale",
                            "instruction": "Lift your team's completed hay bale by its sisal strings. Check if it holds its rectangular shape firmly without grass falling out. Measure its dimensions with a tape measure to verify compliance with the 40cm x 50cm x 75cm standard."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Box-Baling Troubleshooting",
                        "content": {
                            "question": "A student team notices that their newly made hay bale feels light, spongy, and easily falls apart when lifted. What was the most likely mistake made during construction?",
                            "options": [
                                "They used sisal twine instead of metal wire.",
                                "They did not stamp and compact the forage layers firmly during packing.",
                                "They used Rhodes grass instead of maize stover.",
                                "They placed the box baler on flat ground."
                            ],
                            "answer": "B",
                            "explanation": "A firm, brick-like bale requires heavy, repeated compaction after every layer of grass is added. If stamping is skipped or too light, large air pockets remain, leaving the bale fluffy and structurally weak."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Practical box-baling produces **firm, uniform rectangular hay bales** using low-cost wooden equipment.\n- **Laying twines in the empty box first** is the cardinal operational rule of box-baling.\n- **Frequent, heavy stamping** produces dense, high-capacity bales that resist rotting.\n- Completed bales must be tied with **tight reef knots** and stored **elevated on pallets**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we have hands-on practical skills in both stacking and baling, how does a household combine these tools into a comprehensive dry-season survival plan? In the next lesson, we explore household-level drought mitigation strategies."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Household Strategies to Conserve Forage During Drought
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Household Strategies to Conserve Forage During Drought",
            "unit_description": "Household feed budgeting mathematics, strategic destocking economics, supplementary crop residue feeding, and drought-tolerant forage establishment.",
            "lesson_title": "Household Strategies to Conserve Forage During Drought",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Strategic Farm Planning: Household Drought Defense",
                        "content": {
                            "title": "Strategic Farm Planning: Household Drought Defense",
                            "caption": "A farming family inspecting their stored hay reserves and calculating feed rations to survive an upcoming dry season."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Household Drought Planning",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Formulate a household **feed budget** to match stored forage reserves against herd consumption.",
                                "Explain how **strategic destocking** lowers feed demand while generating emergency capital.",
                                "Develop a **supplementary feeding strategy** using crop residues to stretch premium hay reserves.",
                                "Select and establish deep-rooted **drought-tolerant forage crops**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Survival by Design, Not by Chance",
                        "content": {
                            "title": "The 4 Pillars of Household Drought Defense",
                            "text": "Surviving severe droughts requires strategic, proactive planning. Successful households deploy a combined 4-pillar defense strategy: **drought-tolerant planting**, **feed budgeting**, **strategic destocking**, and **supplementary residue feeding**."
                        }
                    }
                ],
                # Page 2: The 4-Pillar Drought Defense Framework
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 4-Pillar Household Forage Conservation Framework",
                        "content": {
                            "title": "The 4-Pillar Household Forage Conservation Framework",
                            "caption": "Matrix diagram outlining the four core household tactics: drought-tolerant planting, feed budgeting, destocking, and residue recycling."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Household Strategy Breakdown",
                        "content": {
                            "title": "The 4 Household Drought Management Strategies",
                            "headers": ["Strategy Pillar", "Action Taken by Family", "Direct Benefit During Drought"],
                            "rows": [
                                ["Drought-Tolerant Crops", "Plant deep-rooted Rhodes grass, Sorghum, and Desmodium", "Maintains vegetative growth under low soil moisture"],
                                ["Strategic Destocking", "Sell off older, non-milking, or male livestock at onset of dry spell", "Lowers daily feed demand and injects emergency cash"],
                                ["Crop Residue Recycling", "Collect, chop, and store maize stover and wheat straw after grain harvest", "Provides cheap bulk fiber to stretch valuable hay reserves"],
                                ["Feed Budgeting", "Calculate daily herd consumption against stored bales", "Eliminates feed wastage and prevents unexpected starvation"]
                            ]
                        }
                    }
                ],
                # Page 3: Mathematical Feed Budgeting
                [
                    {
                        "type": "worked_example",
                        "title": "Practical Farm Mathematics: The Feed Budget Equation",
                        "content": {
                            "intro": "Let us calculate a feed budget for Farmer Kiprop to determine if his hay reserve will last through a 90-day dry season:",
                            "steps": [
                                "**Herd Size**: Farmer Kiprop owns 2  dairy cows.",
                                "**Consumption Rate**: Each cow consumes 1  rectangular hay bale every 4 days, which is 0.25  bales/cow/day.",
                                "**Total Daily Herd Demand**: 2  cows × 0.25  bales = 0.5  bales per day.",
                                "**Total Feed Needed for 90 Days**: 0.5  bales/day × 90  days = 45  bales.",
                                "**Stored Reserve**: Kiprop has stored 60  rectangular bales in his dry barn.",
                                "**Budget Outcome**: 60  stored - 45  needed = +15  surplus bales! Kiprop has enough feed to survive the drought with 15 surplus bales to sell for profit!"
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Feed Stretching Secret",
                        "content": {
                            "title": "The 50/50 Rationing Rule",
                            "text": "During extreme feed scarcity, feed dry chopped maize stover in the morning for bulk energy, and reserve high-protein hay for the evening milking. This stretches your premium hay twice as long!"
                        }
                    }
                ],
                # Page 4: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Household Feed Budgeting",
                        "content": {
                            "question": "Farmer Kiptoo has 2 cows. Each cow eats 1 rectangular bale every 5 days (0.2 bales/day per cow). Kiptoo has stored 24 bales for a dry season predicted to last 100 days. What is his feed budget outcome?",
                            "options": [
                                "Kiptoo has exactly enough feed with zero shortage.",
                                "Kiptoo faces a shortage of 16 bales (needs 40 bales, has only 24).",
                                "Kiptoo has a surplus of 10 bales to sell.",
                                "Cows do not require feed during dry seasons."
                            ],
                            "answer": "B",
                            "explanation": "Daily herd consumption is 2 cows x 0.2 bales/day = 0.4 bales/day. Over 100 days, the cows need 0.4 x 100 = 40 bales. Since Kiptoo only stored 24 bales, he faces a deficit of 40 - 24 = 16 bales and must source crop residues or destock."
                        }
                    }
                ],
                # Page 5: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Household drought security requires **feed budgeting**, **destocking**, **residue recycling**, and **resilient planting**.\n- **Feed budgeting math** prevents unexpected mid-drought feed collapse.\n- **Strategic destocking** reduces pasture pressure and provides capital.\n- **Crop residues** serve as an essential bulk supplement to stretch premium hay."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered all the technical and management skills of forage conservation. In our final capstone lesson, we examine the economic and community rewards of haymaking, review an instructional video, and complete the Topic Assessment."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Relational and Economic Benefits of Hay Conservation & Capstone Review
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Relational and Economic Benefits of Hay Conservation",
            "unit_description": "Economic cost-savings, milk yield stability, community climate resilience, dispute reduction, instructional video review, and topic-level summative assessment.",
            "lesson_title": "Relational and Economic Benefits of Hay Conservation",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Economic Reward of Feed Conservation",
                        "content": {
                            "title": "The Economic Reward of Feed Conservation",
                            "caption": "A smiling Kenyan dairy farmer holding milk churns and receiving income from steady dry-season milk sales."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Economic & Community Benefits",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Calculate the **economic cost savings** of home-conserved hay versus purchased commercial feed during drought.",
                                "Explain how stored forage maintains **steady milk production, body condition, and herd value**.",
                                "Analyze the **relational and social benefits** of forage management (community peace, zero pasture trespassing).",
                                "Synthesize the entire topic through an **instructional video review** and complete the **Topic Summative Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Forage Conservation is Highly Profitable",
                        "content": {
                            "title": "The Financial Shield of Stored Feed",
                            "text": "During droughts, the market price of commercial dairy feeds and purchased hay doubles or triples. Farmers who make their own hay using rainy-season grass spend almost **zero shillings on feed**, protecting their profits while neighbors suffer catastrophic losses."
                        }
                    }
                ],
                # Page 2: Economic Comparison: Conserved vs. Purchased Feed
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Economic Cost-Benefit Comparison: Conserved Hay vs. Commercial Feed",
                        "content": {
                            "title": "Economic Cost-Benefit Comparison: Conserved Hay vs. Commercial Feed",
                            "caption": "Financial chart contrasting daily profit margins of a farmer with home-made hay (+300 KES/day) against a farmer buying emergency feed (-100 KES/day)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Economic Balance Sheet: Drought Strategies",
                        "content": {
                            "title": "Financial Breakdown: Farmer with Hay vs. Farmer Without Hay",
                            "headers": ["Financial Metric", "Farmer Cherono (Conserved 80 Bales)", "Farmer Mwangi (No Stored Feed)"],
                            "rows": [
                                ["Daily Feed Cost", "0 KES (uses home-conserved hay)", "400 KES (buys commercial feed daily)"],
                                ["Daily Milk Revenue", "350 KES (cow remains healthy & productive)", "300 KES (cow produces low yield due to stress)"],
                                ["Net Daily Profit/Loss", "+350 KES Daily Profit", "-100 KES Daily Net Loss"],
                                ["Herd Body Condition", "Healthy, high market value, breeding safe", "Emaciated, weak, vulnerable to disease"],
                                ["Forced Panic Sales", "None (preserves valuable breeding cows)", "Forced to sell cows at throwaway prices"]
                            ]
                        }
                    }
                ],
                # Page 3: Relational, Social, and Community Benefits
                [
                    {
                        "type": "concept_explanation",
                        "title": "Beyond Money: Social and Community Harmony",
                        "content": {
                            "title": "Building Peaceful, Resilient Communities",
                            "text": "Forage conservation creates vital social and community benefits:\n\n- **Peace & Harmony (Zero Trespassing)**: Desperate farmers often herd hungry cattle onto neighbors' farms, sparking violent land and crop boundary disputes. Stored feed allows animals to stay confined peacefully.\n- **Community Climate Resilience**: When multiple households in a village conserve forage, the entire community withstands climate shocks without food insecurity.\n- **Mutual Cooperation**: Farmers form self-help groups to share labor during haymaking, box construction, and storage building."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Community Action",
                        "content": {
                            "title": "Forage Banking as a Youth Enterprise",
                            "text": "Grade 9 learners can form school or community youth groups to harvest surplus roadside grasses, box-bale them, and sell hay to local dairy farmers during dry seasons—creating jobs and climate resilience!"
                        }
                    }
                ],
                # Page 4: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Economic & Social Benefits",
                        "content": {
                            "question": "How does forage conservation help maintain social peace and harmony in a rural farming community?",
                            "options": [
                                "It forces all farmers to sell their cattle.",
                                "It makes grass grow along public highways.",
                                "Stored feed allows livestock to be fed at home, preventing destructive trespassing onto neighbors' crops.",
                                "It eliminates the need for water."
                            ],
                            "answer": "C",
                            "explanation": "Confining animals and feeding them home-conserved hay eliminates trespass grazing on neighbors' crops, which is the primary cause of community boundary disputes during dry seasons."
                        }
                    }
                ],
                # Page 5: Topic Synthesis & Key Takeaways
                [
                    {
                        "type": "key_takeaway",
                        "title": "Topic 1 Master Summary",
                        "content": {
                            "text": "- **Forage** (grasses, legumes, residues) is the primary nutritional foundation for livestock.\n- **Drought** causes both pasture volume and quality to collapse through moisture loss and lignification.\n- **Haymaking** captures surplus green pasture by drying it to 15-20% moisture to prevent rot.\n- **Stacking** and **box-baling** provide low-cost, machine-free conservation pathways for smallholders.\n- **Paddocking and rotational grazing** prevent pasture degradation and create living deferred feed banks.\n- **Feed budgeting** protects farm profitability, animal health, and community harmony."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Manual Box-Bailing and Haymaking on Smallholder Farms",
                        "content": {
                            "title": "Topic Video Review: Manual Box-Bailing and Haymaking on Smallholder Farms",
                            "url": "https://www.youtube.com/watch?v=XGzUL9tRelc",
                            "resolved_video_id": "XGzUL9tRelc",
                            "caption": "Watch this practical demonstration showing how smallholder farmers construct a wooden box baler, position sisal twines, stamp cut forage, and bind solid rectangular hay bales for dry-season storage."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Things to Observe in the Video",
                        "content": {
                            "title": "Focus Questions for Video Reflection",
                            "text": "- **1. Twine Placement**: Notice how the twines are laid in the empty box baler before any grass is added.\n- **2. Compaction Density**: Observe the physical effort of stamping down each layer of dry forage.\n- **3. Knot Tying**: Watch how the operator applies body weight to tie tight double knots before opening the side door."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Forage Classification",
                        "content": {
                            "question": "Farmer Omondi wants to plant a high-protein forage crop that can be intercropped with Rhodes grass to improve the nutritional quality of his dry-season hay. Which plant should he select?",
                            "options": [
                                "Maize Stover",
                                "Desmodium",
                                "Napier Grass",
                                "Wheat Straw"
                            ],
                            "answer": "B",
                            "explanation": "Desmodium is a high-protein legume with broad leaves and nitrogen-fixing root nodules. Mixing it with structural grasses like Rhodes grass produces a balanced, nutritious hay mix."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Drought Biology",
                        "content": {
                            "question": "During a prolonged drought, why does standing pasture grass become pale yellow, dry, and extremely tough for cattle to chew?",
                            "options": [
                                "The grass absorbs excessive water from dry soil.",
                                "Fungal mould grows on the living leaves, turning them yellow.",
                                "Plants halt vegetative growth, lose moisture and protein, and build tough woody cellulose and lignin to stay upright.",
                                "Grazing animals trample the grass into organic compost."
                            ],
                            "answer": "C",
                            "explanation": "To survive moisture deprivation, pasture plants stop active growth, lose water, and develop dense, woody structural fibers (lignin and cellulose) that are hard for livestock to chew and digest."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 4)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Spoilage Biology",
                        "content": {
                            "question": "A farmer harvests fresh green Rhodes grass and immediately compresses it into a box baler without drying it in the sun. What is the most likely outcome when this bale is stored in a barn?",
                            "options": [
                                "The wet grass will transform into high-protein desmodium.",
                                "The bale will lose its fiber and turn into liquid sugar.",
                                "Trapped internal moisture will cause rapid bacterial and fungal growth, leading to rotting, heating, and toxic mould.",
                                "The wet bale will become easier to transport and stack."
                            ],
                            "answer": "C",
                            "explanation": "Baling forage with high moisture creates an ideal anaerobic environment for rot-causing microbes and fungi to thrive. This destroys nutrients, generates dangerous heat, and produces toxic fungal spores."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Haystack Engineering",
                        "content": {
                            "question": "Why is it absolutely necessary to construct a haystack on a raised wooden platform of posts and rafters rather than directly on bare earth?",
                            "options": [
                                "To make the haystack look taller from a distance.",
                                "To protect the base from rising ground moisture and provide an airflow gap beneath.",
                                "To prevent wild birds from nesting in the grass.",
                                "To allow livestock to graze directly from the bottom."
                            ],
                            "answer": "B",
                            "explanation": "Soil contains moisture that rises via capillary action. A raised platform (at least 30cm high) stops ground moisture from rotting the bottom layers and provides an airflow gap to keep the stack dry."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 5 to 6)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Deferred Grazing",
                        "content": {
                            "question": "Farmer Nekesa sets aside Paddock 4 of her farm during the entire rainy season, preventing her goats from entering it. When rains stop and other pastures turn dry, she opens Paddock 4. What pasture management technique is she practicing?",
                            "options": [
                                "Concentrated Overgrazing",
                                "Continuous Overstocking",
                                "Deferred Grazing (Pasture Banking)",
                                "Mechanical Weed Control"
                            ],
                            "answer": "C",
                            "explanation": "Deferred grazing is the practice of delaying grazing on a specific paddock during the main growing season, allowing the forage to accumulate undisturbed so it can serve as a standing feed reserve in the dry season."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Box-Baling Operations",
                        "content": {
                            "question": "When preparing to make a rectangular bale inside a manual wooden box baler, at what exact step should the farmer place the sisal twines into the box?",
                            "options": [
                                "After the box is completely packed and compacted with grass.",
                                "Halfway through compaction, when the box is half-full.",
                                "Into the empty box baler before any forage is added.",
                                "Only after the completed bale has been lifted out of the box."
                            ],
                            "answer": "C",
                            "explanation": "Sisal twines must always be positioned in the empty box first, running down the walls and across the bottom. If grass is packed first, the twines cannot be threaded underneath the dense, heavy compressed hay."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 7 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Overgrazing Ecology",
                        "content": {
                            "question": "A farmer keeps 12 dairy cows on a tiny 0.5-acre pasture field. Within three weeks, the pasture is bare, and the soil has become compacted, hard, and eroded. What ecological mistake was made?",
                            "options": [
                                "The stocking rate was too high for the land's carrying capacity, leading to severe overgrazing.",
                                "The farmer practiced too much rotational grazing.",
                                "The cows did not eat enough dry maize stover.",
                                "The farmer planted too much desmodium."
                            ],
                            "answer": "A",
                            "explanation": "Keeping too many animals on a small piece of land is overstocking. The excessive stocking rate exceeds the carrying capacity, causing animals to eat grass down to bare roots while hooves compact and erode soil."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Feed Budgeting Math",
                        "content": {
                            "question": "Farmer Kiprop has 2 dairy cows. Each cow consumes 1 rectangular hay bale every 4 days (0.25 bales/cow/day). Kiprop has stored 60 rectangular hay bales for a 90-day dry season. What is his feed budget outcome?",
                            "options": [
                                "Kiprop has exactly enough bales with zero surplus.",
                                "Kiprop will face a shortage of 15 bales before the dry season ends.",
                                "Kiprop needs 45 bales (0.5 bales/day x 90 days), leaving him with a surplus of 15 bales to sell for profit.",
                                "Kiprop will face a massive shortage of 50 bales."
                            ],
                            "answer": "C",
                            "explanation": "Daily consumption for 2 cows is 2 x 0.25 = 0.5 bales per day. Over 90 days, the cows consume 0.5 x 90 = 45 bales. Since Kiprop stored 60 bales, he has a surplus of 60 - 45 = 15 bales that he can sell for profit."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Farm Economics",
                        "content": {
                            "question": "During a drought, commercial feed prices double to 400 KES per bale. Farmer Mwangi (no stored feed) spends 400 KES daily buying feed and sells milk for 350 KES. Farmer Cherono (home-made hay) spends 0 KES on feed and sells milk for 350 KES. What is the financial comparison?",
                            "options": [
                                "Mwangi makes a daily profit of 50 KES.",
                                "Cherono makes a daily profit of 350 KES, while Mwangi suffers a daily loss of 50 KES.",
                                "Both farmers make the same profit because they produce equal milk.",
                                "Mwangi is more profitable because his expenses are higher."
                            ],
                            "answer": "B",
                            "explanation": "Cherono makes 350 - 0 = +350 KES profit daily. Mwangi makes 350 - 400 = -50 KES loss daily. Home forage conservation acts as a financial shield against dry-season commercial feed price spikes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Environmental Risk Analysis",
                        "content": {
                            "question": "A farmer is deciding whether to conserve forage as standing forage in the field or baled hay in a barn. Which environmental analysis is accurate?",
                            "options": [
                                "Standing forage is safe from wildfires, but hay in a barn is destroyed by hailstones.",
                                "Hay in a barn rots from rain, but standing forage is immune to flooding.",
                                "Standing forage is cheap and requires zero harvest labor, but is exposed to outdoor wildfires, hailstones, and floods; baled hay requires harvest labor but is sheltered safely in a barn.",
                                "Baled hay has no weather dependency, while standing forage requires 3 days of dry sunshine to graze."
                            ],
                            "answer": "C",
                            "explanation": "Standing forage requires no harvest machinery or storage barns, but remains exposed to wildfires, hail, and floods. Baled hay requires cutting, drying, and compaction labor, but provides secure, sheltered feed inside a barn."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade9_agriculture_topic1(replace: bool = True):
    """Executes the database transaction to ingest Topic 1 into CBC Grade 9 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 9 AGRICULTURE — TOPIC 1")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Hierarchy
        curriculum, _ = Curriculum.objects.get_or_create(
            name="CBC",
            defaults={"description": "Competency Based Curriculum"}
        )
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Grade 9",
            defaults={"level": 9, "description": "Junior Secondary School Grade 9"}
        )
        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Agriculture",
            defaults={"description": "Grade 9 Agriculture (CBC)"}
        )

        print(f"[*] Hierarchy Resolved: {curriculum.name} -> {grade.name} -> {subject.name}")

        # 2. Resolve Topic
        topic_name = "Conserving Animal Feeds (Forage, Drought, and Hay)"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 1,
                "description": "Comprehensive forage management, drought impact mitigation, standing pasture banking, loose hay stacking, and manual box-baling."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        # 3. Ingest Units and Lessons
        curriculum_data = build_topic1_curriculum()
        total_units = len(curriculum_data)
        total_lessons = 0
        total_pages = 0
        total_blocks = 0

        for unit_data in curriculum_data:
            u_order = unit_data["unit_order"]
            u_name = clean_text(unit_data["unit_name"])
            u_desc = clean_text(unit_data["unit_description"])
            l_title = clean_text(unit_data["lesson_title"])
            pages_data = unit_data["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                name=u_name,
                order=u_order,
                description=u_desc
            )

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1
            )
            total_lessons += 1

            block_order = 0
            for page_idx, page_blocks in enumerate(pages_data, start=1):
                total_pages += 1
                page_title = None

                for comp_idx, b_data in enumerate(page_blocks, start=1):
                    b_type = b_data["type"]
                    b_title = clean_text(b_data.get("title", ""))
                    b_content = clean_dict(b_data.get("content", {}))

                    if not page_title and b_title:
                        page_title = b_title

                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g9_agri_t1_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        page_number=page_idx,
                        page_title=page_title,
                        component_order=comp_idx,
                        order=block_order
                    )
                    block_order += 1
                    total_blocks += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson ID {lesson.id} ({len(pages_data)} Pages, {block_order} Blocks)")

        print("\n" + "=" * 80)
        print(f"[SUCCESS] Ingestion Complete for Topic 1: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade9_agriculture_topic1(replace=replace_flag)
