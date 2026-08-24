"""
VLearn CBC Grade 8 Home Science — Topic 1: Foods and Nutrition
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (Level: 8)
Subject: Home Science
Topic: Foods and Nutrition (Topic Order: 1)

Decomposed into 5 Learning Units & 5 Published Lessons (40 Total Structured Pages):
  1. Kitchen Gardening & Household Food Security (8 Pages)
  2. The Science of Cooking Starchy Carbohydrates (8 Pages)
  3. Table Setting, Meal Presentation & Service Styles (8 Pages)
  4. Nutritional Meal Planning for Special Groups (8 Pages)
  5. Meals for Special Occasions & Kitchen Waste Management (8 Pages)

Features:
  - Rich typography with bold key terms, phrases, and structured bullets.
  - Step-by-step process workflows.
  - Formatted comparison tables and callouts.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_home_science_topic1.py [--replace]
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
    """Returns the comprehensive pedagogical page and block structure for Topic 1: Foods and Nutrition."""
    return [
        # =====================================================================
        # LESSON 1: Kitchen Gardening & Household Food Security
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Kitchen Gardening & Household Food Security",
            "unit_description": "Innovative kitchen garden technologies, food vs nutrition security, vegetable classification by plant part eaten, organic gardening, and record keeping.",
            "lesson_title": "Kitchen Gardening & Household Food Security",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Welcome to Kitchen Gardening: Growing Fresh Food Anywhere",
                        "content": {
                            "title": "Welcome to Kitchen Gardening: Growing Fresh Food Anywhere",
                            "caption": "A thriving home vegetable garden producing fresh leafy greens and crops in organized beds."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Kitchen Gardening",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Distinguish between **food security** (caloric quantity) and **nutrition security** (dietary nutrient quality).",
                                "Explore **5 innovative garden technologies** for small or concrete spaces: tyre, container, wick, drip, and multi-storey gardens.",
                                "Classify kitchen crops and categorize vegetables by their **edible plant parts**.",
                                "Apply **organic gardening practices** and maintain professional garden record files."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Kitchen Gardens Matter",
                        "content": {
                            "title": "A Mini-Market at Your Doorstep",
                            "text": "Imagine going to prepare a family meal and discovering you are missing fresh **coriander (dhania)** or **spinach**. Instead of spending money at the market for wilted produce, a **kitchen garden** gives you immediate access to vibrant, chemical-free greens right outside your doorstep!\n\n• **Freshness on Demand**: Harvest crops at peak freshness with zero transport delay.\n• **Cost Savings**: Drastically reduce household vegetable expenditures.\n• **Environmental Protection**: Recycle domestic containers and organic kitchen waste into rich soil compost."
                        }
                    }
                ],
                # Page 2: Food Security vs Nutrition Security
                [
                    {
                        "type": "concept_explanation",
                        "title": "Understanding Food vs. Nutrition Security",
                        "content": {
                            "title": "Quantity vs. Quality in Everyday Diet",
                            "text": "Understanding what we eat requires distinguishing between two fundamental concepts:\n\n• **Food Security**: Having physical and economic access to **enough quantity** of food to satisfy hunger and daily energy needs.\n• **Nutrition Security**: Ensuring that the food consumed is **nutrient-dense**, containing the required balance of vitamins, minerals, proteins, and healthy fats necessary for disease immunity, physical growth, and cognitive development."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Food Security vs. Nutrition Security",
                        "content": {
                            "title": "Food Security vs. Nutrition Security",
                            "headers": ["Aspect", "Food Security (Calories)", "Nutrition Security (Quality)"],
                            "rows": [
                                ["Primary Focus", "Quantity and fullness (caloric intake)", "Nutrient density (vitamins, minerals, protein)"],
                                ["Example Meal", "A large plate of plain starch (e.g., plain maize ugali)", "Starch paired with fresh indigenous greens (managu, terere) and tomatoes"],
                                ["Health Impact", "Staves off hunger but may leave the body malnourished", "Boosts immunity, builds blood, and supports brain and body vitality"],
                                ["Garden Contribution", "Provides supplemental carbohydrate crops (sweet potatoes)", "Supplies immediate daily vitamins (A, C) and minerals (Iron)"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Key Nutritional Insight",
                        "content": {
                            "title": "Full Stomach != Healthy Body",
                            "text": "Eating a large bowl of starch fills the stomach, but without micronutrients from fresh vegetables, the body remains vulnerable to **hidden hunger** (micronutrient deficiencies). Growing indigenous vegetables like **black nightshade (managu)** and **amaranth (terere)** provides vital **iron** and **vitamin A** right at home."
                        }
                    }
                ],
                # Page 3: Innovative Kitchen Garden Technologies
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Anatomy and Capillary Action of a Wick Container Garden",
                        "content": {
                            "title": "Anatomy and Capillary Action of a Wick Container Garden",
                            "caption": "Cross-sectional blueprint of a self-watering wick garden utilizing capillary action."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "5 Innovative Technologies for Limited Spaces",
                        "content": {
                            "title": "Urban Farming Technologies",
                            "text": "You do not need expansive farmland to grow fresh food. Innovative designs utilize vertical space and recycled domestic containers:\n\n• **1. Container Garden**: Growing vegetables in repurposed plastic buckets, 5-litre bottles, or wooden crates with bottom drainage holes.\n• **2. Tyre Garden**: Stacking discarded vehicle tyres filled with a fertile soil-compost blend to create raised planting beds.\n• **3. Wick Garden**: A self-watering system where a **cotton fabric wick** draws water upward from a reservoir by **capillary action** to keep roots moist.\n• **4. Simple Drip Garden**: Inverted plastic bottles with micro-perforations that slowly deliver targeted water drops directly to plant roots.\n• **5. Multi-Storey Garden**: Tiered vertical sacks or stacked pipes that allow growing up to 60 vegetable plants in just **1 square meter**."
                        }
                    }
                ],
                # Page 4: Vegetable & Crop Classification by Plant Part
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Plant Part Map: Classifying Edible Vegetables",
                        "content": {
                            "title": "The Plant Part Map: Classifying Edible Vegetables",
                            "caption": "Diagram mapping edible vegetables to their botanical plant parts."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Vegetable Classification by Part Eaten",
                        "content": {
                            "title": "Categories of Common Kitchen Garden Vegetables",
                            "headers": ["Plant Part", "Vegetable Classification", "Common Kenyan Examples", "Nutritional Value"],
                            "rows": [
                                ["Leaves", "Leafy Vegetables", "Spinach, Sukuma Wiki (Kale), Managu, Terere", "Iron, Vitamin A, Vitamin C, Dietary Fibre"],
                                ["Roots", "Root Vegetables", "Carrots, Sweet Potatoes, Beetroots", "Beta-carotene (Vitamin A), Complex Carbohydrates"],
                                ["Bulbs", "Bulb Vegetables", "Onions, Garlic, Shallots", "Antioxidants, Allicin, Flavour enhancers"],
                                ["Stems", "Stem Vegetables", "Celery, Asparagus", "Water, Dietary Fibre, Potassium"],
                                ["Flowers", "Flower Vegetables", "Broccoli, Cauliflower", "Folate, Vitamin C, Phytochemicals"],
                                ["Seeds & Pods", "Legume Vegetables", "Green Peas, French Beans", "Plant Protein, Iron, B-Vitamins"],
                                ["Botanical Fruits", "Fruit Vegetables", "Tomatoes, Capsicum (Sweet Pepper), Eggplant", "Lycopene, Vitamin C, Vitamin A"]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example — Establishing a Container Garden
                [
                    {
                        "type": "step_process",
                        "title": "Step-by-Step: Establishing a Container Garden in a Concrete Yard",
                        "content": {
                            "title": "Step-by-Step Procedure",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Select & Drill Drainage Holes",
                                    "description": "Gather recycled **20-litre plastic buckets** or crates. Drill 3–4 drainage holes in the base to prevent waterlogging."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Prepare the Planting Medium",
                                    "description": "Thoroughly mix **2 parts fertile topsoil** with **1 part organic compost**. Add a handful of dry wood ash to balance pH and deter pests."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Fill & Moisten",
                                    "description": "Fill the container, leaving **2 inches (5 cm)** of rim space at the top. Moisten the soil evenly with clean water."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Transplant Seedlings",
                                    "description": "Carefully plant healthy spinach or kale seedlings in the cool evening, pressing soil firmly around root balls."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Position & Maintain",
                                    "description": "Place containers where they receive at least **6 hours of direct sunlight** daily. Water regularly in the early morning."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Critical Mistake to Avoid",
                        "content": {
                            "title": "Never Skip Drainage Holes!",
                            "text": "Planting in unperforated containers traps stagnant water around plant roots. This cuts off oxygen, promotes fungal rot, and turns vegetable leaves yellow."
                        }
                    }
                ],
                # Page 6: Organic Practices & Record Keeping
                [
                    {
                        "type": "concept_explanation",
                        "title": "Organic Garden Management & Farm Business Records",
                        "content": {
                            "title": "Sustainable Practices & Farm Business Records",
                            "text": "• **Organic Soil Feeding**: Nourish crops using decayed organic compost from kitchen vegetable peels and dry leaves rather than synthetic chemical fertilizers.\n• **Natural Pest Repellents**: Control garden pests using organic sprays made from **neem oil**, crushed garlic, chili, and wood ash.\n• **The 3 Essential Garden Records**:\n  1. **Weekly Garden Report**: Records dates, moisture levels, plant height, weeding dates, and pest observations.\n  2. **Garden File**: Organizes seed receipts, crop budgets, and seasonal planting calendars.\n  3. **Garden Portfolio**: Collects harvest photos, yield logs (in kg), and calculates family cost-savings."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Setting Up Your School Garden Log",
                        "content": {
                            "title": "Activity: Design a 1-Week Garden Ledger",
                            "instructions": "In your notebook or on a card, rule a table with 5 columns: **Date**, **Technology Used**, **Crop Observed**, **Action Taken (e.g., Weeding/Watering)**, and **Harvest Yield (kg)**. Record daily observations for one container plant this week."
                        }
                    }
                ],
                # Page 7: Misconceptions & Summary
                [
                    {
                        "type": "did_you_know",
                        "title": "Common Misconception: Land Size vs. Productivity",
                        "content": {
                            "title": "Myth: You Need a Huge Farm to Grow Food",
                            "text": "Fact: A single multi-storey sack garden occupying just **1 square meter** of ground space can support up to **60 vegetable plants** simultaneously, producing fresh leafy greens for a family of four for over 6 months!"
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Kitchen Gardening",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "**Nutrition security** requires micronutrient-dense leafy greens and vegetables alongside staple starches.",
                                "**Wick and container gardens** bypass the lack of open ground and conserve water through capillary action.",
                                "Vegetables are classified into **7 categories** based on the edible plant part (leaves, roots, bulbs, stems, flowers, pods, fruit vegetables).",
                                "**Organic composting** and **careful record-keeping** ensure high yields and financial savings."
                            ]
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Kitchen Gardening & Food Security",
                        "content": {
                            "question": "A family living in a dry, semi-arid urban area with scarce tap water wants to grow vegetables on a sunny concrete balcony. Which technology is best suited for their needs, and why?",
                            "options": [
                                "An open ground garden, because open soil always holds more water.",
                                "A wick container garden, because it uses self-watering capillary action to minimize evaporation and conserve water.",
                                "Sprinkler irrigation on loose soil, because sprinklers cover large areas.",
                                "Flooding buckets with water twice daily without drainage holes."
                            ],
                            "correct_index": 1,
                            "explanation": "A wick garden utilizes capillary action through a cotton strip to draw water from an enclosed reservoir directly to plant roots, drastically reducing evaporation losses in dry, water-scarce environments."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: The Science of Cooking Starchy Carbohydrates
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Scientific Cooking of Starchy Carbohydrate Foods",
            "unit_description": "Methods of heat transfer, carbohydrate taxonomy, starch gelatinisation and dextrinisation chemistry, the 8 nutrient conservation rules, and solanine/aflatoxin food safety.",
            "lesson_title": "Scientific Cooking of Starchy Carbohydrate Foods",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The Culinary Science of Carbohydrates: From Raw to Delicious",
                        "content": {
                            "title": "The Culinary Science of Carbohydrates: From Raw to Delicious",
                            "caption": "Freshly harvested and washed potatoes ready for culinary transformation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Carbohydrate Science",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify the three methods of heat transfer in cooking: **conduction**, **convection**, and **radiation**.",
                                "Classify dietary carbohydrates into **complex starches**, **double sugars**, and **simple sugars**.",
                                "Explain the biochemical transformations of starch: moist-heat **gelatinisation** and dry-heat **dextrinisation**.",
                                "Apply the **8 golden rules of nutrient conservation** and detect toxic **solanine** and **aflatoxins**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Do We Cook Starchy Foods?",
                        "content": {
                            "title": "The Molecular Magic of Cooking",
                            "text": "Eating raw maize flour or hard raw cassava is unpleasant, gritty, and difficult for the human stomach to digest. Cooking applies thermal energy to:\n\n• **Soften Tough Cellulose**: Break down structural plant cell walls to make tubers and grains tender.\n• **Swell Starch Granules**: Unlock tightly packed starch polymers for digestive enzymes.\n• **Develop Aromas & Flavours**: Create appetizing textures, glossy pastes, and golden-brown crusts."
                        }
                    }
                ],
                # Page 2: Three Methods of Heat Transfer
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Three Methods of Heat Transfer in a Home Kitchen",
                        "content": {
                            "title": "Three Methods of Heat Transfer in a Home Kitchen",
                            "caption": "Diagram illustrating conduction through pan metal, convection circulation in boiling liquid, and radiation waves from charcoal."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Conduction vs. Convection vs. Radiation",
                        "content": {
                            "title": "Comparing Heat Transfer Mechanisms in Cooking",
                            "headers": ["Method", "Medium of Transfer", "How It Works", "Kitchen Cooking Example"],
                            "rows": [
                                ["Conduction", "Solids (direct contact)", "Heat moves molecule-by-molecule through metal to food", "Baking chapati on a hot dry pan; heat moves directly from metal to dough"],
                                ["Convection", "Fluids (liquids & gases)", "Heated fluid expands, rises, cools, and sinks, creating continuous circulating currents", "Boiling sweet potatoes in a pot of water; baking bread in an enclosed oven"],
                                ["Radiation", "Electromagnetic waves (no medium needed)", "Infrared heat waves travel straight from the heat source to food surface", "Roasting maize or cassava over glowing red-hot charcoal on a wire grill"]
                            ]
                        }
                    }
                ],
                # Page 3: Carbohydrate Classification
                [
                    {
                        "type": "concept_explanation",
                        "title": "Carbohydrate Taxonomy: Complex vs. Simple",
                        "content": {
                            "title": "From Grain to Sugar",
                            "text": "Carbohydrates provide our body's primary energy fuel. They are classified into three distinct categories:\n\n• **1. Complex Starches (Polysaccharides)**: Long chains of hundreds of glucose units tightly packed in granules. Found in maize, rice, wheat, millet, potatoes, cassava, yams, and green bananas. Provide **slow-release, sustained energy**.\n• **2. Double Sugars (Disaccharides)**: Two sugar molecules bonded together, such as **sucrose** (table sugar) and **maltose**.\n• **3. Simple Sugars (Monosaccharides)**: Single glucose or fructose molecules found in ripe fruits and natural bee honey. Deliver **rapid, immediate energy**."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Taste vs. Molecular Structure",
                        "content": {
                            "title": "Why Isn't Raw Starch Sweet?",
                            "text": "Raw starch granules do not taste sweet because their glucose chains are locked in crystalline granules. Heat and salivary enzymes (**amylase**) unwind and break these long chains into sweet, digestible sugars as you chew."
                        }
                    }
                ],
                # Page 4: Starch Chemistry — Gelatinisation vs. Dextrinisation
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Molecular Pathways: Gelatinisation (Moist Heat) vs. Dextrinisation (Dry Heat)",
                        "content": {
                            "title": "Molecular Pathways: Gelatinisation vs. Dextrinisation",
                            "caption": "Microscopic stages of starch granules swelling and gelling in water vs dry thermal browning."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Gelatinisation vs. Dextrinisation",
                        "content": {
                            "title": "Comparing Chemical Changes in Cooked Starch",
                            "headers": ["Feature", "Gelatinisation (Moist Heat)", "Dextrinisation (Dry Heat)"],
                            "rows": [
                                ["Heating Medium", "Liquid / Water (Moist Heat)", "Dry Air / Direct Surface (Dry Heat)"],
                                ["Temperature Threshold", "Begins around 60°C; complete by 85–100°C", "High dry heat (160°C–200°C)"],
                                ["Mechanism", "Granules absorb water, swell, burst, and form a thick viscous gel", "Starch chains break down thermally into smaller, sweeter dextrin molecules"],
                                ["Visual & Texture Result", "Translucent, thick, velvety paste (thickened porridge, ugali)", "Golden-brown, crunchy, toasted surface with pleasant aroma"],
                                ["Culinary Examples", "Cooking maize flour uji, boiling rice, thickening soup with cornstarch", "Toasting bread slices, roasting cassava over coals, baking cake crust"]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example — Cooking Lump-Free Maize Uji
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Cooking Lump-Free, Velvety Porridge (Uji)",
                        "content": {
                            "title": "Culinary Scientific Procedure",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Blend Flour with Cold Water",
                                    "description": "Place measured maize flour in a bowl and stir in **cold water** to form a smooth paste. (Cold water separates starch granules before heat is applied)."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Boil Base Liquid",
                                    "description": "Bring the water in the cooking pot to a steady, rolling boil over the stove."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Incorporate While Stirring",
                                    "description": "Slowly pour the cold flour slurry into the boiling water while **stirring continuously** with a wooden spoon."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Continuous Low-Heat Stirring",
                                    "description": "Stir continuously over medium-low heat as the mixture reaches **60°C–80°C**. Starch granules swell uniformly without clumping."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Simmer to Full Gelatinisation",
                                    "description": "Cover and simmer gently for **10–15 minutes** until the uji turns glossy, smooth, and completely cooked."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Scientific Rationale",
                        "content": {
                            "title": "Why Dumping Dry Flour Into Boiling Water Fails",
                            "text": "If dry flour is added directly into boiling water, the outer layer gelatinises instantly into a sticky skin, trapping dry, raw flour inside hard lumps!"
                        }
                    }
                ],
                # Page 6: Kitchen Safety Hazards — Solanine & Aflatoxins
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kitchen Safety Warning: Detecting Solanine and Aflatoxins",
                        "content": {
                            "title": "Kitchen Safety Warning: Detecting Solanine and Aflatoxins",
                            "caption": "Visual identification of green solanine patches on sprouting potatoes and toxic aflatoxin mold on grains."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Two Deadly Kitchen Chemical Hazards",
                        "content": {
                            "title": "Protecting Your Family from Toxins",
                            "text": "• **1. Solanine Poisoning**: A natural glycoalkaloid toxin that forms when potatoes and yams are exposed to light or begin sprouting. It appears as **green patches** under the peel and around sprouted 'eyes.' Solanine causes severe nausea, abdominal cramps, vomiting, and neurological distress. **Never cook green or sprouted tubers!**\n\n• **2. Aflatoxin Contamination**: Lethal chemical toxins produced by *Aspergillus* molds on damp or improperly stored grains (maize, sorghum, peanuts). Aflatoxins cause irreversible **liver damage and cancer**. Critically, **cooking heat DOES NOT destroy aflatoxins**. Always inspect and discard moldy, discolored, or damp grains."
                        }
                    }
                ],
                # Page 7: The 8 Golden Rules of Nutrient Conservation
                [
                    {
                        "type": "summary",
                        "title": "The 8 Golden Rules of Nutrient Conservation",
                        "content": {
                            "title": "Preserving Vitamins and Minerals During Cooking",
                            "summary": "1. **Peel Thinly**: Most vitamins lie directly beneath the skin; better yet, boil tubers in their jackets.\n2. **Wash Before Cutting**: Never wash peeled/cut tubers, as water-soluble vitamins (B and C) leach into wash water.\n3. **Use Minimal Water**: Use just enough water to cook food to prevent vitamin loss.\n4. **Keep Pot Covered**: Retain steam to accelerate cooking time and reduce nutrient oxidation.\n5. **Cook Only Until Tender**: Avoid prolonged overcooking that degrades delicate vitamins.\n6. **Blend Flours Cold**: Mix starch flours with cold water first to ensure smooth, uniform heat distribution.\n7. **Stir Continuously**: Prevent localized burning and ensure even gelatinisation.\n8. **Aim for Golden Brown**: In dry-heat roasting/baking, stop at a light golden hue to avoid charring."
                        }
                    },
                    {
                        "type": "memory_tip",
                        "title": "Recall Helper",
                        "content": {
                            "title": "Remember 'W-P-M-C'",
                            "tip": "**W**ash before cutting, **P**eel thinly, **M**inimal water, **C**over the pot!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Cooking Starchy Carbohydrates",
                        "content": {
                            "question": "Your sibling is boiling sweet potatoes and wants to ensure maximum retention of water-soluble vitamins. Which procedure should you advise?",
                            "options": [
                                "Peel the potatoes thickly, soak them in water for 2 hours, and boil in an open pot filled to the brim.",
                                "Wash potatoes thoroughly before cutting, peel thinly or cook in skins, use minimal water, and keep the pot covered.",
                                "Chop potatoes into tiny cubes, wash them several times after chopping, and boil vigorously without a lid.",
                                "Use green sprouted potatoes and fry them in deep smoking oil."
                            ],
                            "correct_index": 1,
                            "explanation": "Washing before cutting, peeling thinly (or cooking in jackets), using minimal water, and keeping the pot covered prevents water-soluble vitamins B and C from leaching away or oxidizing."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Table Setting, Meal Presentation & Service Styles
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Table Setting, Meal Presentation & Service Styles",
            "unit_description": "Table appointments, technical rules for setting a cover, meal service styles (family, blue plate, buffet), edible garnishing, and hygiene etiquette.",
            "lesson_title": "Table Setting, Meal Presentation & Service Styles",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "The Art of Dining: Meal Presentation and Table Setting",
                        "content": {
                            "title": "The Art of Dining: Meal Presentation and Table Setting",
                            "caption": "A neatly set dining cover with clean linen, sparkling crockery, and a fresh natural centerpiece."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Meal Presentation",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify table setting appointments: **furniture**, **linen**, **crockery**, **cutlery**, **glassware**, and **centerpieces**.",
                                "Master the **1-inch rule** and technical layout for setting a standard main meal cover.",
                                "Compare 3 meal service styles: **Family Service**, **Blue Plate Service**, and **Buffet Service**.",
                                "Apply **edible garnishing techniques** and public health hygiene protocols during dining."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Table Presentation Matters",
                        "content": {
                            "title": "Dining is an Experience",
                            "text": "Eating is more than satisfying hunger; it is a shared social and cultural event. An organized, clean, and beautifully set table:\n\n• **Welcomes Diners**: Expresses warmth, respect, and hospitality.\n• **Ensures Safety & Convenience**: Arranges cutlery logically in the order of use so guests dine without spills.\n• **Elevates Appetite**: Attractive presentation stimulates the senses and makes nutritious meals enjoyable."
                        }
                    }
                ],
                # Page 2: Table Setting Appointments
                [
                    {
                        "type": "comparison_table",
                        "title": "The 6 Essential Table Setting Appointments",
                        "content": {
                            "title": "Classification of Table Appointments",
                            "headers": ["Appointment", "Key Components", "Primary Purpose", "Local / Improvised Option"],
                            "rows": [
                                ["Furniture", "Dining table, comfortable dining chairs", "Provides stable, ergonomic eating surface", "Clean, sturdy wooden bench and level table"],
                                ["Table Linen", "Tablecloth, placemats, fabric/paper napkins", "Protects table, absorbs spills, defines individual space", "Woven sisal or banana fiber mats, clean cotton cloths"],
                                ["Crockery", "Dinner plate (main meal), side plate (bread/bones)", "Holds food hygienically", "Clean ceramic, enameled metal, or glass plates"],
                                ["Cutlery (Silverware)", "Table fork, table knife, dessert/soup spoon", "Utensils for eating and cutting food cleanly", "Stainless steel forks and spoons with clean handles"],
                                ["Glassware", "Water tumbler, juice glass", "Holds drinking fluids securely", "Clear glass tumblers or clean ceramic cups"],
                                ["Centrepiece", "Small vase of fresh flowers, potted succulent, fresh fruit bowl", "Adds visual cheer and natural beauty to the table", "Recycled glass bottle with wild green leaves and flowers"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Centrepiece Golden Rule",
                        "content": {
                            "title": "Keep It Low!",
                            "text": "A dining centerpiece must always be **low enough** so that diners seated opposite each other can make direct eye contact and converse comfortably without obstruction."
                        }
                    }
                ],
                # Page 3: Setting a Cover for a Main Meal
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Bird's-Eye Technical Blueprint of a Standard Main Meal Cover",
                        "content": {
                            "title": "Bird's-Eye Technical Blueprint of a Standard Main Meal Cover",
                            "caption": "Top-down schematic showing the 1-inch table margin, fork left, knife blade facing inward, and glass placement."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Technical Rules for Setting a Cover",
                        "content": {
                            "title": "The Anatomy of a Dining Cover",
                            "text": "A **cover** is the individual space and appointment layout set for one diner (typically 20–24 inches wide). It follows precise ergonomic standards:\n\n• **The 1-Inch Margin**: Align the bottom edge of the placemat, plates, and all cutlery exactly **1 inch (2.5 cm)** from the table edge so sleeves do not accidentally brush utensils onto the floor.\n• **Plate & Napkin (Center)**: Center the dinner plate on the placemat with the folded napkin resting on top.\n• **Table Fork (Left)**: Place the fork to the left of the dinner plate, tines pointing upward.\n• **Table Knife (Right)**: Place the knife immediately to the right of the plate with the **cutting blade pointing inward** toward the plate.\n• **Spoon (Far Right)**: Place the soup/dessert spoon to the right of the knife.\n• **Water Glass (Top Right)**: Position the glass just above the tip of the table knife for convenient reaching.\n• **Side Plate (Far Left)**: Place the side plate to the left of the fork for bread or bone discards."
                        }
                    }
                ],
                # Page 4: Three Styles of Meal Service
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparing Three Meal Service Styles and Guest Flows",
                        "content": {
                            "title": "Comparing Three Meal Service Styles and Guest Flows",
                            "caption": "Diagram comparing Family Service bowl-passing, Blue Plate kitchen plating, and Buffet linear serving line."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Family Service vs. Blue Plate vs. Buffet Service",
                        "content": {
                            "title": "Service Style Selection Guide",
                            "headers": ["Service Style", "How Food is Served", "Best Used For", "Key Advantage"],
                            "rows": [
                                ["Family Service", "Dishes placed in serving bowls in table center; diners pass bowls around", "Everyday family meals, small informal gatherings", "Encourages warm bonding, sharing, and portion choice"],
                                ["Blue Plate Service", "Individual plates portioned and styled in the kitchen, then served", "Quick meals, restaurants, convalescent trays", "Ensures precise portion control and neat food presentation"],
                                ["Buffet Service", "Food arranged on a long separate table; guests queue and serve themselves", "Large gatherings (birthdays, graduations, school events)", "Feeds large crowds efficiently with minimal service staff"]
                            ]
                        }
                    }
                ],
                # Page 5: Worked Example — Setting an Informal Lunch Cover
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Setting an Informal Lunch Cover for Two",
                        "content": {
                            "title": "Step-by-Step Execution",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Sanitize & Align Mats",
                                    "description": "Wipe the tabletop clean. Place two clean placemats opposite each other, aligned **1 inch from the table edge**."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Position Dinner Plates",
                                    "description": "Place a clean, dry dinner plate directly in the center of each placemat."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Arrange Cutlery",
                                    "description": "Place the table fork on the left. Place the table knife on the right (**blade facing inward**), followed by the spoon."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Set Glassware & Napkins",
                                    "description": "Place the water glass at the top right near the knife tip. Fold a fabric napkin neatly into a triangle atop the plate."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Add Centerpiece",
                                    "description": "Place a low glass jar with fresh green herbs or garden flowers in the center of the table."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Edible Garnishing & Hygiene Etiquette
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Art of Edible Garnishing & Food Safety",
                        "content": {
                            "title": "Garnishing Rules and Hygiene Protocols",
                            "text": "• **Garnishes Must Be Edible**: Never use inedible plastic decorations. Use fresh **tomato roses**, **curly parsley**, **onion rings**, or **citrus wheels** to complement flavors and colors.\n• **Contrast & Balance**: Pair savory brown stews with vibrant green parsley or red tomato; decorate sweet desserts with mint leaves or fruit slices.\n• **Cutlery Handling Protocol**: Always hold cutlery by the **handles**, never touching the prongs, blades, or spoon bowls.\n• **Public Health Hygiene**: Wash hands thoroughly before setting tables, cover dishes against flies, and provide dedicated **serving spoons** for every shared dish."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Safety First",
                        "content": {
                            "title": "Why Knife Blades Face Inward",
                            "text": "The sharp cutting edge of the table knife must always point **inward toward the plate**. If placed outward, a diner reaching across the table risks slicing their fingers against the exposed edge."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Etiquette Rules
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Table Setting & Presentation",
                        "content": {
                            "title": "Core Rules of Table Presentation",
                            "takeaways": [
                                "The **1-inch rule** keeps all appointments neatly aligned and safe from accidental sleeve snagging.",
                                "**Forks belong on the left**; **knives (blade inward) and spoons belong on the right**.",
                                "**Buffet service** is the most practical choice for large gatherings with limited seating.",
                                "All food garnishes must be **fresh, edible, and hygienic**."
                            ]
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Meal Presentation & Service Styles",
                        "content": {
                            "question": "You are organizing a lunch for 60 guests on a school sports day in a hall with only two large tables. Which meal service style should you select, and how should cutlery be arranged on tables?",
                            "options": [
                                "Blue Plate service, bringing each plated meal individually from the kitchen with cutlery placed randomly on top.",
                                "Buffet service, arranging food in serving dishes along one long table so guests can queue and serve themselves.",
                                "Family service, placing 60 individual bowls on the floor for guests to pass around.",
                                "Formal Russian service, hiring 20 waiters to serve guests synchronously."
                            ],
                            "correct_index": 1,
                            "explanation": "Buffet service is ideal for large gatherings because guests walk along a designated service line to serve themselves, allowing a small catering team to feed large numbers quickly and efficiently."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Nutritional Meal Planning for Special Groups
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Nutritional Meal Planning for Special Groups",
            "unit_description": "Dietary guidelines for 10 physiological special groups, nutrient balance matrix, debunking cultural food taboos, and convalescent meal preparation.",
            "lesson_title": "Nutritional Meal Planning for Special Groups",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Nutrition Across the Life Stages: Diverse Dietary Needs",
                        "content": {
                            "title": "Nutrition Across the Life Stages: Diverse Dietary Needs",
                            "caption": "A vibrant variety of balanced food groups providing customized nutrients for all life stages."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Special Groups Nutrition",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify the **10 special nutritional groups** and their distinct physiological dietary requirements.",
                                "Analyze the **nutritional balance matrix** comparing energy, protein, calcium, and iron demands across life stages.",
                                "Debunk harmful **cultural food taboos** using scientific nutritional evidence.",
                                "Plan, calculate, and prepare easily digestible meals for **convalescents** and **manual workers**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why One Diet Does Not Fit All",
                        "content": {
                            "title": "Tailoring Food to Physiological Needs",
                            "text": "A breastfeeding mother, an active adolescent athlete, a bedridden patient, and a construction worker sitting at the same table cannot eat identical food portions. Nutritional needs depend on **age**, **physical activity level**, and **health status**!"
                        }
                    }
                ],
                # Page 2: The 10 Special Groups Nutritional Balance Matrix
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Nutritional Balance Matrix: Life-Stage Dietary Priorities",
                        "content": {
                            "title": "The Nutritional Balance Matrix: Life-Stage Dietary Priorities",
                            "caption": "Infographic showing nutrient demands for infants, adolescents, manual workers, expectant mothers, and the elderly."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Nutritional Guidelines for the 10 Special Groups",
                        "content": {
                            "title": "Nutritional Priorities for Diverse Physiological Needs",
                            "headers": ["Special Group", "Key Physiological Needs", "Critical Nutrients Required", "Recommended Foods"],
                            "rows": [
                                ["1. Infants (0–1 yr)", "Rapid brain and body growth; delicate digestive system", "Breast milk, Calcium, High-quality protein, Iron", "Exclusive breastmilk for 6 months, enriched pumpkin/millet purees"],
                                ["2. Children (1–12 yrs)", "Continuous skeletal growth and high physical play activity", "Protein, Calcium, Vitamin A, Vitamin C, Energy", "Milk, eggs, beans, fruit salads, small frequent balanced meals"],
                                ["3. Adolescents (13–19)", "Intense growth spurt, puberty, and menstrual blood loss in girls", "Iron (blood formation), Calcium (bone density), Protein", "Leafy greens (managu), liver, beans, whole grains, dairy"],
                                ["4. Expectant Mothers", "Nourishing developing fetus, building maternal blood volume", "Folic acid (neural tube), Iron (prevent anemia), Calcium", "Eggs, dark green vegetables, citrus fruits, lean meat, milk"],
                                ["5. Lactating Mothers", "High breastmilk synthesis, hydration, and nutrient replenishment", "Extra Fluids, Calcium, High Protein, Energy", "Nutritious soups, milk, porridge, clean water, legumes"],
                                ["6. Manual Workers", "Heavy physical exertion (farming, construction, masonry)", "Massive Energy (complex carbohydrates), B-Vitamins, Fluids", "Ugali, sweet potatoes, cassava, beans, plenty of water"],
                                ["7. Older Persons", "Reduced physical metabolism, fragile bones, weaker digestion", "Vitamins, Calcium, Dietary Fibre (prevent constipation), Low Salt", "Soft steamed vegetables, bone broth, mashed tubers, low-fat stew"],
                                ["8. Invalids (Sick)", "Bedridden, low appetite, vulnerable immune system", "Fluids, High Vitamins (A, C, E), Trace Minerals, Low Fat", "Clear chicken/vegetable broths, fresh fruit juices, herbal teas"],
                                ["9. Convalescents (Recovering)", "Rebuilding damaged body tissues, regaining muscle strength", "High-quality Protein (tissue repair), Iron, Energy", "Boiled chicken, egg drop soup, soft velvety uji, steamed greens"],
                                ["10. Vegetarians", "Zero animal flesh; need complete amino acid profile", "Plant Proteins, Vitamin B12, Iron, Zinc", "Combinations of legumes + grains (e.g., beans with rice/chapati)"]
                            ]
                        }
                    }
                ],
                # Page 3: Debunking Cultural Food Taboos
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Scientific Evidence vs. Harmful Cultural Food Taboos",
                        "content": {
                            "title": "Scientific Evidence vs. Harmful Cultural Food Taboos",
                            "caption": "Debunking common myths that restrict eggs, poultry, and fish from vulnerable mothers and children."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Evaluating Food Taboos and Superstitions",
                        "content": {
                            "title": "Culture Meets Science",
                            "text": "A **food taboo** is a cultural or religious prohibition against eating certain foods. While some historical taboos protected communities from spoiled foods, many taboos unfairly targeted vulnerable groups like pregnant women and children:\n\n• **Taboo Myth**: *'Pregnant women must not eat eggs or the baby will be born bald or with speech defects.'*\n  • **Scientific Reality**: Eggs provide **complete, affordable protein**, **choline** for fetal brain development, and **iron**. Denying eggs leads to maternal anemia and low birth weight!\n\n• **Taboo Myth**: *'Children should not eat chicken gizzards or fish heads because it makes them rebellious.'*\n  • **Scientific Reality**: Organ meats and fish are packed with **zinc**, **omega-3 fatty acids**, and **vitamin A** vital for child cognitive growth."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Pregnancy Myth: 'Eating for Two'",
                        "content": {
                            "title": "Double the Quality, Not Double the Quantity",
                            "text": "An expectant mother does not need to eat double the volume of food (which causes unhealthy maternal obesity and complications). She needs **'double the nutrient quality'**—dense iron, calcium, folic acid, and vitamins!"
                        }
                    }
                ],
                # Page 4: Worked Example — Convalescent Broth Preparation
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Preparing a Convalescent Chicken & Vegetable Broth",
                        "content": {
                            "title": "Step-by-Step Procedure for a Convalescent",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Measure Ingredients",
                                    "description": "Weigh **100g skinless chicken breast** (lean protein), 50g carrots, 50g peeled potatoes, and 30g fresh spinach."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Simmer Lean Chicken",
                                    "description": "Cut chicken into small cubes and simmer in **400ml clean water** to extract a clear, fat-free protein broth."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Add Diced Roots",
                                    "description": "Add finely sliced carrots and potatoes; simmer until fork-tender to release soluble starches and beta-carotene."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Quick-Cook Greens",
                                    "description": "Add shredded spinach in the **final 2 minutes** of cooking to preserve heat-sensitive Vitamin C."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Serve Warm & Light",
                                    "description": "Serve warm in a clean bowl with soft maize uji. (Avoid heavy oil, chili, or strong spices that irritate recovering stomachs)."
                                }
                            ]
                        }
                    }
                ],
                # Page 5: Practical Menu Balancing Activity
                [
                    {
                        "type": "mini_activity",
                        "title": "Menu Challenge: Balancing Plates for Two Lifestyles",
                        "content": {
                            "title": "Activity: Manual Worker vs. Adolescent Sports Girl",
                            "instructions": "Plan a lunch menu for both:\n\n• **(A) Construction Worker**: Needs **3,200 calories** of sustained energy.\n• **(B) 14-Year-Old Female Athlete**: Needs **high iron and calcium** for blood oxygenation and bone density.\n\nList the main starch, protein, vegetable, and beverage for each."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Accurate Measurement in Meal Planning",
                        "content": {
                            "title": "Using Kitchen Scales & Ratios",
                            "text": "Professional home cooks measure ingredients using kitchen scales (grams/kilograms) and measuring jugs (milliliters/liters). Standard catering calculations allow accurate portioning:\n• Raw rice per adult: **~80g–100g**\n• Lean meat per portion: **~100g–150g**\n• Cooked vegetable side: **~80g**"
                        }
                    }
                ],
                # Page 6: Summary & Key Nutritional Rules
                [
                    {
                        "type": "summary",
                        "title": "Summary: Nutrition for Special Groups",
                        "content": {
                            "title": "Core Rules of Physiological Nutrition",
                            "summary": "1. **Match Nutrients to Life Stage**: Rapid growth demands protein and calcium; heavy physical labor demands high carbohydrates; illness recovery demands clear broths and vitamins.\n2. **Reject Harmful Superstitions**: Ensure vulnerable women and children receive high-protein foods like eggs, fish, and dairy.\n3. **Convalescent Meals**: Keep foods warm, soft, easily chewable, low in heavy fat, and rich in clear broths.\n4. **Plant Protein Complementation**: Combine cereals and legumes (e.g., rice and beans) to provide all essential amino acids for vegetarians."
                        }
                    }
                ],
                # Page 7: Memory Tip
                [
                    {
                        "type": "memory_tip",
                        "title": "Life-Stage Recall Tip",
                        "content": {
                            "title": "Remember 'P-I-C-E'",
                            "tip": "**P**rotein for growth & repair, **I**ron for blood & stamina, **C**alcium for bones & teeth, **E**nergy for daily activity!"
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Special Groups Nutrition",
                        "content": {
                            "question": "A 15-year-old girl who actively competes in school athletics is experiencing fatigue. Her grandmother suggests that she should avoid eating eggs and liver because of an old cultural belief. What is the correct scientific advice?",
                            "options": [
                                "Follow the taboo and eat only white bread and sweet tea.",
                                "Explain that adolescent girls have increased iron requirements due to growth and menstrual cycles, and eggs and liver provide crucial iron and protein for oxygen transport and stamina.",
                                "Double her food intake by eating twice as much plain ugali without vegetables.",
                                "Stop doing sports and drink only cold water."
                            ],
                            "correct_index": 1,
                            "explanation": "Adolescent girls have elevated requirements for iron to prevent anemia and support muscle metabolism during athletic activity. Eggs and liver provide high-bioavailability iron and protein that should never be restricted."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Meals for Special Occasions & Kitchen Waste Management
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Meals for Special Occasions & Kitchen Waste Management",
            "unit_description": "Event meal planning, budgeting, baking in a jiko sand-oven, food presentation, and circular kitchen waste management (reduce, reuse, compost).",
            "lesson_title": "Meals for Special Occasions & Kitchen Waste Management",
            "pages": [
                # Page 1: Topic Introduction & Visual Hook
                [
                    {
                        "type": "suggested_image",
                        "title": "Celebration Dining and Environmental Responsibility",
                        "content": {
                            "title": "Celebration Dining and Environmental Responsibility",
                            "caption": "A festive community celebration featuring beautifully decorated dishes and a clean kitchen environment."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Special Occasions & Waste Management",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify common special occasions (weddings, birthdays, graduations, funerals) and their **menu planning guidelines**.",
                                "Construct an **event food budget** and estimate ingredient quantities using standard catering ratios.",
                                "Bake and decorate celebratory dishes using locally available cooking equipment (**jiko sand-oven**).",
                                "Implement the **3-bin circular waste management system**: Reduce, Reuse, and Compost."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Dual Challenge of Celebrations",
                        "content": {
                            "title": "Food, Hospitality, and the Planet",
                            "text": "Special occasions bring families and communities together in celebration and mourning. However, catering for large crowds presents two major challenges:\n\n• **Financial Strain**: Overspending caused by inaccurate guest estimation and lack of budgeting.\n• **Environmental Waste**: Huge piles of food trimmings and single-use packaging ending up in polluting landfills.\n\nMastering meal planning and **circular waste management** makes you a skilled, environmentally responsible home scientist!"
                        }
                    }
                ],
                # Page 2: Planning Factors & Common Catering Mistakes
                [
                    {
                        "type": "comparison_table",
                        "title": "Occasion Types, Menu Guidelines & Planning Pitfalls",
                        "content": {
                            "title": "Special Occasion Planning Matrix",
                            "headers": ["Occasion Type", "Appropriate Menu Tone", "Key Planning Success Factors", "Common Pitfall to Avoid"],
                            "rows": [
                                ["Birthday Party", "Festive, colorful, kid-friendly; includes decorative cake", "Precise guest count, finger foods, clear budget", "Overspending on non-edible decorations"],
                                ["Graduation / Initiation", "Substantial, celebratory; includes pilau, stews, salads", "Generous carbohydrate & protein ratios, buffet line", "Under-catering (running out of food halfway through)"],
                                ["Funeral / Memorial", "Respectful, simple, comforting, easily served warm", "Fast batch preparation, easily packaged foods", "Preparing overly complex dishes that delay service"],
                                ["Wedding Celebration", "Elegant, multi-course, diverse dietary options", "Strict timetable, organized service team, cold storage", "Buying perishables too early without refrigeration"]
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Common Mistake in Event Catering",
                        "content": {
                            "title": "The Perishable Trap",
                            "text": "A frequent mistake is purchasing large quantities of fresh meat, milk, and vegetables without having adequate cold storage. In warm weather, food spoils rapidly, leading to catastrophic financial loss and food poisoning risks."
                        }
                    }
                ],
                # Page 3: Event Budgeting & Quantity Calculation
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Event Catering Budget Spreadsheet Model",
                        "content": {
                            "title": "The Event Catering Budget Spreadsheet Model",
                            "caption": "Sample budgeting spreadsheet linking guest numbers, ingredient ratios, estimated costs, and savings."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How to Calculate Food Quantities for Crowds",
                        "content": {
                            "title": "Standard Catering Ratios",
                            "text": "To prevent both food shortages and food waste, professional caterers calculate raw ingredients per head:\n\n• **Grains (Rice/Maize)**: **80g–100g raw** per adult guest.\n• **Meat/Fish/Poultry**: **120g–150g raw** per person.\n• **Legumes (Beans/Peas)**: **50g–60g dry** per person.\n• **Fresh Vegetables**: **80g–100g trimmed** per person.\n\nMultiplying these unit weights by the total guest count gives exact purchasing quantities, preventing financial loss and kitchen waste!"
                        }
                    }
                ],
                # Page 4: Worked Example — Baking Cake in a Jiko Sand-Oven
                [
                    {
                        "type": "step_process",
                        "title": "Worked Example: Baking a Birthday Sponge Cake in a Jiko Sand-Oven under 300 KES",
                        "content": {
                            "title": "Step-by-Step Baking Procedure",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Budget & Measure Ingredients",
                                    "description": "Measure **200g flour (30 KES)**, **100g sugar (20 KES)**, **2 eggs (30 KES)**, **100g margarine (40 KES)**, and **1 tsp baking powder (5 KES)**. Total ingredient cost = **125 KES** (leaving 175 KES savings!)."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Cream Margarine and Sugar",
                                    "description": "Beat margarine and sugar in a clean bowl using a wooden spoon until pale, light, and fluffy (traps air bubbles for rising)."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Incorporate Eggs & Flour",
                                    "description": "Gradually whisk in beaten eggs. Sift in flour and baking powder, gently folding with a metal spoon to preserve trapped air."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Prepare Jiko Sand-Oven",
                                    "description": "Place **2 inches of clean, dry sand** in a large sufuria over a low charcoal jiko. Place a metal wire trivet on the sand and preheat covered."
                                },
                                {
                                    "step_number": 5,
                                    "title": "Bake & Decorate",
                                    "description": "Pour batter into greased tin, place on trivet in sand-oven, cover lid with a few glowing coals, and bake for **30 minutes**. Cool and decorate with fresh orange and banana rings."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Why the Sand-Oven Works",
                        "content": {
                            "title": "Convection & Even Heat Distribution",
                            "text": "The dry sand absorbs intense heat from the charcoal and radiates it evenly around the baking tin via **convection currents**, preventing the cake base from burning while cooking the center perfectly."
                        }
                    }
                ],
                # Page 5: Circular Kitchen Waste Management (3-Bin System)
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 3-Bin Kitchen Waste Sorting Station and Circular Composting Loop",
                        "content": {
                            "title": "The 3-Bin Kitchen Waste Sorting Station",
                            "caption": "Diagram showing Green Organic Composting Bin, Blue Recyclables Bin, and Black General Trash Bin."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 3-R Environmental Protocol in Foods and Nutrition",
                        "content": {
                            "title": "Closing the Food Cycle",
                            "text": "Large catering events produce immense kitchen waste. Applying circular waste management protects our environment and feeds our gardens:\n\n• **1. Reduce**: Calculate guest ratios accurately so minimal leftovers remain.\n• **2. Reuse**: Promptly chill clean, unserved leftover foods in airtight containers for subsequent meals.\n• **3. Recycle & Compost**: Separate organic food waste (potato skins, vegetable trimmings, eggshells) into the **Green Bin**. Deposit this matter into a school compost pit, where microorganisms convert it into rich **organic fertilizer** for the kitchen garden!"
                        }
                    }
                ],
                # Page 6: Hands-On Activity — Waste Audit
                [
                    {
                        "type": "mini_activity",
                        "title": "Hands-On: Setting Up a 3-Bin Separation Station",
                        "content": {
                            "title": "Activity: Kitchen Waste Audit",
                            "instructions": "Label three containers at school or home:\n\n• **GREEN BIN**: Organic Vegetable Peels & Food Scraps\n• **BLUE BIN**: Recyclable Containers, Bottles & Clean Foil\n• **BLACK BIN**: General Non-Recyclable Trash\n\nFor three days, audit kitchen scraps and calculate the total weight of organic matter diverted to the compost pit."
                        }
                    }
                ],
                # Page 7: Key Takeaways & Summary
                [
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaways: Occasions & Waste Management",
                        "content": {
                            "title": "Core Ideas to Remember",
                            "takeaways": [
                                "Accurate **guest ratios** prevent embarrassing food shortages and costly over-catering.",
                                "**Jiko sand-ovens** utilize convection and radiation to bake delicious celebratory dishes affordably.",
                                "Separating **organic kitchen waste** from non-biodegradable trash produces nutrient-dense compost for home gardens.",
                                "A successful host balances **hospitality**, **budgeting**, **hygiene**, and **environmental responsibility**."
                            ]
                        }
                    }
                ],
                # Page 8: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Occasions & Waste Management",
                        "content": {
                            "question": "After catering a school graduation ceremony for 80 guests, your team has 5 kg of clean raw vegetable peelings and potato skins. What is the most responsible, sustainable way to manage this kitchen waste?",
                            "options": [
                                "Pack the peelings in plastic bags and dump them in an open ditch outside the school gate.",
                                "Burn the peelings together with plastic cups over a roaring open fire.",
                                "Separate the organic peels from plastics, carry them to the school kitchen garden compost pit, and layer them with dry leaves and soil to produce organic fertilizer.",
                                "Wash them down the kitchen sink drain to save time."
                            ],
                            "correct_index": 2,
                            "explanation": "Composting organic kitchen waste diverts biodegradable matter from landfills, prevents pollution, and converts vegetable scraps into rich organic compost that nourishes future kitchen garden crops."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_home_science_topic1(replace=False):
    """Executes the atomic ingestion of CBC Grade 8 Home Science Topic 1."""
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 8 HOME SCIENCE — TOPIC 1: FOODS AND NUTRITION")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        curriculum = Curriculum.objects.create(
            name="CBC",
            description="Kenyan Competency-Based Curriculum (2-6-3-3-3)",
            max_selectable_subjects=8,
            max_priority_subjects=3
        )
        print(f"[+] Created Curriculum: {curriculum.name} (ID: {curriculum.id})")
    else:
        print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade 8
    grade, g_created = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Grade 8",
        defaults={"level": 8, "description": "Junior Secondary Grade 8"}
    )
    print(f"[{'+' if g_created else '*'}] Grade 8: ID {grade.id} (Level {grade.level})")

    # 3. Resolve Subject: Home Science
    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="Home Science",
        defaults={"description": "CBC Junior Secondary Home Science & Applied Nutrition"}
    )
    print(f"[{'+' if s_created else '*'}] Subject: {subject.name} (ID {subject.id})")

    # 4. Resolve Topic: Foods and Nutrition
    topic_name = "Foods and Nutrition"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=1,
            description="Comprehensive CBC Grade 8 module on kitchen gardens, carbohydrate cooking chemistry, table setting and service styles, life-stage nutrition, and occasion planning with circular waste management."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic1_curriculum()
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            unit_order = unit_data["unit_order"]
            unit_name = unit_data["unit_name"]
            unit_desc = unit_data["unit_description"]
            lesson_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": unit_desc}
            )

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.version = 1
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"\n  [+] Ingesting Lesson {unit_order}: '{lesson.title}' (Lesson ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Page {page_idx}")
                for b_data in page_blocks:
                    b_type = b_data["type"]
                    b_title = b_data.get("title", first_block_title)
                    b_content = clean_dict(b_data.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_idx,
                        page_title=first_block_title,
                        title=b_title,
                        block_type=b_type,
                        component_type=b_type,
                        component_order=block_order,
                        order=block_order,
                        content=b_content,
                        metadata={}
                    )
                    block_order += 10
                    total_blocks += 1

            total_lessons += 1
            total_pages += lesson_page_count
            print(f"      [OK] Ingested {lesson_page_count} Pages ({len(lesson.blocks.all())} Blocks) for Unit {unit_order}.")

    print("\n" + "=" * 80)
    print("[SUCCESS] CBC Grade 8 Home Science Topic 1 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_cbc_grade8_home_science_topic1(replace=replace_flag)
