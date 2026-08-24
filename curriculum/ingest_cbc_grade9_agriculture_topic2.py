"""
VLearn CBC Grade 9 Agriculture — Topic 2: Conserving Leftover Food (Meaning, Importance, and Household Methods)
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 9 (Level: 9)
Subject: Agriculture
Topic: Conserving Leftover Food (Meaning, Importance, and Household Methods) (Topic Order: 2)

Decomposed into 9 Learning Units & 9 Published Lessons:
  1. Meaning and Importance of Conserving Leftover Food (6 Pages, 12 Blocks)
  2. Household Methods of Conserving Leftover Food (6 Pages, 12 Blocks)
  3. Practical Activity: Selecting and Applying a Household Conservation Method (6 Pages, 11 Blocks)
  4. Reheating Leftover Food: Methods and Guidelines (6 Pages, 12 Blocks)
  5. Practical Activity: Reheating Leftover Food Safely in the Kitchen (6 Pages, 11 Blocks)
  6. Recipe Definitions and the Benefits of Repurposing Leftovers (6 Pages, 12 Blocks)
  7. Adapting Creative Recipes to Minimize Food Wastage (6 Pages, 12 Blocks)
  8. Practical Activity: Preparing a New Recipe from Leftover Food (6 Pages, 11 Blocks)
  9. Food Safety in Handling and Storing Leftover Food & Capstone Review (10 Pages, 21 Blocks)

Features:
  - Rich typography with bold key terms, phrases, and structured bullets.
  - Step-by-step practical process workflows.
  - Formatted comparison tables, callouts, and mnemonic tips.
  - Formative scenario MCQs and Topic Summative MCQs with educational feedback.
  - Zero citation bracket leaks and zero raw LaTeX.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade9_agriculture_topic2.py [--replace]
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

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 2: Conserving Leftover Food."""
    return [
        # =====================================================================
        # LESSON 1: Meaning and Importance of Conserving Leftover Food
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning and Importance of Conserving Leftover Food",
            "unit_description": "Leftover food definition, food conservation concept, food waste reduction, household resource economy, and environmental health.",
            "lesson_title": "Meaning and Importance of Conserving Leftover Food",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Valuable Family Resources: Conserving Leftovers",
                        "content": {
                            "title": "Valuable Family Resources: Conserving Leftovers",
                            "caption": "A family dinner table with covered bowls of cooked ugali, beef stew, and greens, ready for safe storage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Leftover Food Conservation",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **leftover food** and **food conservation** in a household domestic context.",
                                "Explain the primary reasons for conserving leftover food at home.",
                                "Analyze the **financial, time-saving, labor-saving, and environmental benefits** of leftover management.",
                                "Appreciate the role of food conservation in strengthening household **food security**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Foundation of Household Resource Management",
                        "content": {
                            "title": "More Than Just Extra Food",
                            "text": "In sub-Saharan African households, efficient resource management is a core competency! Food is prepared with effort and resources, but not all of it is eaten immediately.\n\n- **Leftover Food**: Any cooked meal or prepared ingredient remaining uneaten after a meal is finished.\n- **Food Conservation**: The practice of keeping prepared food clean, safe, and fresh so it can be eaten or repurposed later without waste.\n- **Valuable Asset**: Conserving leftovers saves money, fuel, time, and kitchen labor!"
                        }
                    }
                ],
                # Page 2: Core Reasons for Conserving Leftovers
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Pillars of Leftover Conservation",
                        "content": {
                            "title": "Why Every Family Should Conserve Leftovers",
                            "text": "Conserving and reusing leftover food provides four major household advantages:\n\n- **1. Reduces Food Wastage**: Respects the labor and natural resources used to grow and harvest crops.\n- **2. Saves Money and Ingredients**: Less new raw food needs to be purchased, drastically lowering weekly grocery bills.\n- **3. Saves Kitchen Labor**: Eliminates heavy initial prep work like washing, peeling, chopping, and long boiling.\n- **4. Saves Cooking Fuel and Time**: Reheating takes 5 to 10 minutes and uses minimal gas, charcoal, or firewood."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Efficiency Comparison: Cooking Fresh vs. Conserving Leftovers",
                        "content": {
                            "title": "Resource Consumption Matrix",
                            "headers": ["Resource Category", "Cooking Fresh Meals from Scratch", "Conserving & Reusing Leftovers"],
                            "rows": [
                                ["Money Spent", "High (Requires buying all new fresh ingredients)", "Near Zero (Uses ingredients already paid for)"],
                                ["Preparation Time", "High (30 to 60+ minutes of chopping and cooking)", "Low (5 to 10 minutes of fast reheating)"],
                                ["Fuel / Energy Use", "High (Burns significant charcoal, gas, or firewood)", "Low (Requires brief heating to reach safe temperature)"],
                                ["Kitchen Labor", "High (Heavy stirring, peeling, and multiple dirty pots)", "Low (Minimal preparation and quick single-pan service)"]
                            ]
                        }
                    }
                ],
                # Page 3: Food Security & Environmental Impact
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Resource Efficiency Comparison: Fresh Cooking vs. Leftover Conservation",
                        "content": {
                            "title": "Resource Efficiency Comparison: Fresh Cooking vs. Leftover Conservation",
                            "caption": "Infographic comparing family expenditures in money, time, fuel, and labor between fresh meals and conserved leftovers."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Food Security and Environmental Hygiene",
                        "content": {
                            "title": "Protecting the Planet and Family Health",
                            "text": "Conserving leftovers delivers wider ethical and ecological rewards:\n\n- **Household Food Security**: Ensures that nutritious food is always available for every family member, especially during tight financial periods.\n- **Cleaner Environment**: Keeps food waste out of trash heaps and municipal landfills.\n- **Reduced Greenhouse Gases**: Rotting organic food in landfills produces methane gas, which drives air pollution and climate change. Reusing food keeps communities clean and smelling fresh."
                        }
                    }
                ],
                # Page 4: Scenario Analysis & Practical Diagnostics
                [
                    {
                        "type": "worked_example",
                        "title": "Economic Case Study: The Leftover Advantage",
                        "content": {
                            "intro": "Kioko's family spends 1,500 KES weekly on charcoal and 4,000 KES on groceries. They regularly throw away leftover rice and beans because they prefer cooking fresh daily.",
                            "steps": [
                                "**Problem Diagnosis**: Discarding cooked rice and beans wastes money, spent charcoal, and hours of cooking labor.",
                                "**Corrective Strategy**: Storing and reheating leftover rice and beans on Tuesdays and Thursdays replaces 2 fresh cooking sessions.",
                                "**Financial Outcome**: The family cuts their weekly grocery and charcoal expenses by over 25%, saving up to 1,400 KES each week!",
                                "**Nutritional Outcome**: The family maintains stable food security while freeing up time for study and work."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Key Household Takeaway",
                        "content": {
                            "title": "Leftovers are Already Paid For!",
                            "text": "Every spoonful of leftover food in your kitchen represents paid money and hard labor. Throwing away edible leftovers is like throwing money into the trash bin!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Benefits of Leftover Conservation",
                        "content": {
                            "question": "Why does conserving and reusing leftover food help protect our natural environment?",
                            "options": [
                                "It reduces organic food waste dumped in landfills, preventing rotting and methane pollution.",
                                "It makes soil dry and stops weeds from growing.",
                                "It allows households to use synthetic chemical sprays.",
                                "It increases the amount of charcoal burned in the kitchen."
                            ],
                            "answer": "A",
                            "explanation": "When organic food waste is dumped into garbage dumps, it decomposes anaerobically and produces harmful greenhouse gases like methane. Reusing leftovers prevents waste and keeps surroundings clean."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Leftover food** is cooked food remaining uneaten after a meal.\n- **Food conservation** protects leftovers from contamination so they can be consumed safely later.\n- Conserving leftovers saves **money, time, cooking fuel, and kitchen labor**.\n- Reducing food waste strengthens **household food security** and prevents environmental pollution."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we understand the value of leftovers, how do we prevent them from spoiling at home? In the next lesson, we explore the four main household methods of conserving leftovers: refrigeration, freezing, pickling, and composting."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Household Methods of Conserving Leftover Food
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Household Methods of Conserving Leftover Food",
            "unit_description": "Refrigeration, freezing, pickling, composting, spoilage biology, and matching leftover categories to optimal preservation methods.",
            "lesson_title": "Household Methods of Conserving Leftover Food",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Organized Kitchen Preservation: Cold Storage",
                        "content": {
                            "title": "Organized Kitchen Preservation: Cold Storage",
                            "caption": "An open household refrigerator displaying neatly arranged, labeled plastic containers with cooked stews, vegetables, and rice."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Household Conservation Methods",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify the four main household conservation methods: **refrigeration, freezing, pickling, and composting**.",
                                "Explain how low temperature, acid/salt, and decomposition preserve resources.",
                                "Distinguish between short-term storage (refrigeration) and long-term storage (freezing).",
                                "Select the appropriate conservation method based on the condition of different leftovers."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Halting the Spoilage Clock",
                        "content": {
                            "title": "Why Cooked Food Spoils",
                            "text": "At room temperature, microscopic bacteria, yeasts, and molds multiply rapidly on moist cooked food. Applying domestic conservation methods creates environments where bacteria cannot grow, keeping food safe for days, weeks, or months!"
                        }
                    }
                ],
                # Page 2: The 4 Core Household Conservation Methods
                [
                    {
                        "type": "concept_explanation",
                        "title": "Refrigeration, Freezing, Pickling, and Composting",
                        "content": {
                            "title": "How the 4 Methods Work",
                            "text": "- **Refrigeration (0°C to 4°C)**: Slows down bacterial activity to keep cooked starches, stews, and vegetables fresh for **2 to 3 days**.\n- **Freezing (Below 0°C)**: Turns water inside food into ice, completely stopping all microbial growth for **several weeks or months**.\n- **Pickling (Acid & Salt Brine)**: Submerges excess raw vegetable trimmings (onions, carrots, cucumbers) in vinegar or salt brine where bacteria cannot survive.\n- **Composting (Nutrient Recycling)**: Decomposes inedible scraps (potato peels, eggshells, spoiled items) into fertile organic manure for garden crops."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Sorting Matrix: Matching Leftovers to Conservation Methods",
                        "content": {
                            "title": "Leftover Type vs. Preservation Method",
                            "headers": ["Leftover Category", "Typical Food Items", "Best Method", "Preservation Mechanism"],
                            "rows": [
                                ["Cooked Stews & Meats", "Beef stew, chicken curry, fish soup", "Freezing (long-term) or Refrigeration (short-term)", "Low temperatures stop or slow bacterial metabolism"],
                                ["Cooked Starches", "Ugali, boiled rice, chapati, githeri", "Refrigeration in covered containers", "Maintains moisture and freshness for 2 to 3 days"],
                                ["Raw Veggie Trimmings", "Leftover onions, carrot slices, chilies", "Pickling in vinegar or salt brine", "Acid and salinity create an environment hostile to bacteria"],
                                ["Inedible / Spoiled Waste", "Potato skins, banana peels, rotten tomatoes", "Composting in garden pit or bin", "Aerobic decomposition recycles nutrients into soil manure"]
                            ]
                        }
                    }
                ],
                # Page 3: Preservation Systems Architecture
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Household Leftover Conservation Methods Matrix",
                        "content": {
                            "title": "Household Leftover Conservation Methods Matrix",
                            "caption": "System diagram organizing leftovers into Cold Storage (refrigeration, freezing), Acid/Salt Preservation (pickling), and Nutrient Recycling (composting)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Composting is Food Conservation",
                        "content": {
                            "title": "Closing the Nutrient Loop",
                            "text": "Composting is considered a conservation method because it recycles raw inedible scraps and spoiled food. Instead of polluting trash heaps, the nutrients are returned to the soil as organic fertilizer to grow next season's crops!"
                        }
                    }
                ],
                # Page 4: Decision Tree for Leftover Management
                [
                    {
                        "type": "worked_example",
                        "title": "Kitchen Sorting Decision Tree",
                        "content": {
                            "intro": "A student finds 4 different leftover items on the kitchen counter. How should each item be preserved?",
                            "steps": [
                                "**Item 1 (Pot of beef stew for next month)**: Pack in an airtight container with 1cm headspace and place in the **Freezer**.",
                                "**Item 2 (Bowl of cooked rice for tomorrow's lunch)**: Pack in a covered container and store in the **Refrigerator**.",
                                "**Item 3 (Half an onion and carrot sticks from salad prep)**: Submerge in a glass jar with vinegar and salt for **Pickling**.",
                                "**Item 4 (Potato skins and spoiled rotten tomato)**: Carry to the outdoor garden pit for **Composting**."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Critical Composting Rule",
                        "content": {
                            "title": "No Meat or Oily Stews in Basic Compost!",
                            "text": "Never throw cooked oily stews, bones, or meats into a simple backyard compost heap. Cooked fats and meats attract rats and create foul odors. Compost only raw vegetable peels and plant scraps!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Selecting Conservation Methods",
                        "content": {
                            "question": "If you have raw potato skins and spoiled, rotten onions in your kitchen, which conservation method should you apply?",
                            "options": [
                                "Freezing them in plastic containers to eat next month.",
                                "Refrigerating them in covered bowls.",
                                "Pickling them in glass vinegar jars.",
                                "Composting them in an outdoor garden pit to create organic manure."
                            ],
                            "answer": "D",
                            "explanation": "Raw vegetable peels and rotten food are inedible, so they cannot be frozen or refrigerated for eating. Composting is the best method because it decomposes organic waste into fertile soil manure for crops."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Refrigeration** cools cooked food to slow bacterial growth for 2 to 3 days.\n- **Freezing** halts all bacterial activity for long-term multi-week storage.\n- **Pickling** uses acidic vinegar or salty brine to preserve excess raw vegetables.\n- **Composting** recycles raw scraps and inedible waste into fertile soil manure."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we know the four conservation methods, let us put them into practice! In the next lesson, we conduct a practical activity to package cooked food for cold storage and set up a compost heap."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Practical Activity: Selecting and Applying a Household Conservation Method
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Practical Activity: Selecting and Applying a Household Conservation Method",
            "unit_description": "Hands-on packaging of cooked leftovers in airtight containers, labeling and dating, room-temperature cooling, and composting kitchen scraps.",
            "lesson_title": "Practical Activity: Selecting and Applying a Household Conservation Method",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Practical Storage Station: Containers & Labels",
                        "content": {
                            "title": "Practical Storage Station: Containers & Labels",
                            "caption": "Clean glass and plastic airtight storage containers, masking tape labels, and marker pen laid out on a clean kitchen counter."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: Storage & Composting",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Prepare clean, dry airtight containers and labeling materials for cold food storage.",
                                "Apply the correct step-by-step procedure to package, label, and refrigerate cooked leftovers safely.",
                                "Set up a layered compost bin for raw vegetable peels and food scraps.",
                                "Write a structured **observation report** detailing storage steps, challenges, and physical outcomes."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hands-On Kitchen Management",
                        "content": {
                            "title": "Becoming a Household Resource Manager",
                            "text": "Today, we put conservation theory into action! Working in teams, we will safely package cooked leftovers for cold storage and process raw kitchen scraps for composting."
                        }
                    }
                ],
                # Page 2: Step-by-Step Practical Procedures
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Stage Journey of a Safe Leftover: From Warm Plate to Cold Storage",
                        "content": {
                            "title": "5-Stage Journey of a Safe Leftover: From Warm Plate to Cold Storage",
                            "caption": "Sequential flowchart illustrating the flow from warm plate to room-temperature cooling, clean packaging, date labeling, and refrigerator placement."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Storing Cooked Leftovers",
                        "content": {
                            "title": "Step-by-Step Cold Storage Protocol",
                            "steps": [
                                "**Hand Hygiene**: Wash hands thoroughly with soap and warm water for 20 seconds to prevent cross-contamination.",
                                "**Food Inspection**: Check that leftovers look fresh, smell normal, and have no signs of mold or sourness.",
                                "**Room-Temperature Cooling**: Allow warm food to cool to room temperature before refrigerating (never place hot steaming food directly into the fridge).",
                                "**Airtight Packaging**: Scoop cooled food into clean, dry plastic or glass containers, leaving a 1cm headspace if freezing.",
                                "**Seal & Label**: Close lids tightly to create an airtight barrier; write the food name, storage date, and eat-by date on a label.",
                                "**Refrigerate Promptly**: Place labeled containers inside the refrigerator or freezer within 2 hours of cooking."
                            ]
                        }
                    }
                ],
                # Page 3: Procedure for Composting Kitchen Scraps
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Composting Kitchen Waste",
                        "content": {
                            "title": "Step-by-Step Composting Protocol",
                            "steps": [
                                "**Sort the Scraps**: Separate raw potato peels, eggshells, and carrot tops from cooked oily foods or bones.",
                                "**Add to Compost Bin/Pit**: Place the raw vegetable waste into the outdoor compost pit or garden bin.",
                                "**Layer with Brown Matter**: Cover wet food scraps with a thin layer of dry leaves, grass clippings, or garden soil.",
                                "**Aeration**: Mix and turn the pile once weekly with a garden fork to introduce oxygen, accelerating decomposition."
                            ]
                        }
                    },
                    {
                        "type": "common_mistake",
                        "title": "Common Storage Mistake",
                        "content": {
                            "text": "**Placing steaming hot food directly into a cold refrigerator.** Hot food warms up the air inside the fridge, raising the temperature of other stored foods and causing them to spoil faster! Always allow food to cool to room temperature first."
                        }
                    }
                ],
                # Page 4: Writing the Practical Observation Report
                [
                    {
                        "type": "worked_example",
                        "title": "Practical Report Framework",
                        "content": {
                            "intro": "Record your practical conservation session in your project notebook using this structure:",
                            "steps": [
                                "**Food Item Used**: e.g., Cooked red beans and rice / raw potato peels.",
                                "**Method Applied**: e.g., Refrigeration in airtight plastic container / backyard pit composting.",
                                "**Procedure Followed**: Document the exact steps performed in the kitchen and garden.",
                                "**Challenges & Solutions**: e.g., 'Container lid was loose, so we used a secure rubber band seal.'",
                                "**24-Hour Outcome**: e.g., 'After 24 hours, the beans remained firm, smelled fresh, and had zero mold growth.'"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Cold Storage Procedures",
                        "content": {
                            "question": "Why must warm cooked leftovers be allowed to cool to room temperature before being placed inside a refrigerator?",
                            "options": [
                                "Cooling turns cooked starches into sweet glucose sugars.",
                                "Hot food raises the internal refrigerator temperature, which can cause other stored foods to spoil.",
                                "Cold air destroys the vitamins in hot food.",
                                "Hot containers permanently crack all refrigerator metal shelves."
                            ],
                            "answer": "B",
                            "explanation": "Placing steaming hot pots into a refrigerator warms up the enclosed interior air. This can push other refrigerated items into the temperature danger zone (5°C to 60°C), triggering rapid bacterial growth."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Proper food storage starts with **clean hands and dry, airtight containers**.\n- Cooked food must **cool to room temperature** before cold storage.\n- **Airtight seals and date labels** prevent moisture loss, cross-contamination, and confusion.\n- Composting raw waste requires **layering wet green scraps with dry brown matter**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we have safely stored our leftovers, how do we prepare them when it is time to eat? In the next lesson, we examine the science and golden guidelines of safe food reheating."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Reheating Leftover Food: Methods and Guidelines
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Reheating Leftover Food: Methods and Guidelines",
            "unit_description": "Reheating definition, household heating sources (jiko, stove, microwave), temperature danger zone, uniform heating, and the 5 golden reheating rules.",
            "lesson_title": "Reheating Leftover Food: Methods and Guidelines",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Applying Heat Safely: Kitchen Energy Sources",
                        "content": {
                            "title": "Applying Heat Safely: Kitchen Energy Sources",
                            "caption": "A side-by-side comparison of a traditional Kenyan charcoal jiko and a modern domestic gas stove used for reheating food."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Reheating Science",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **reheating** and explain how it destroys foodborne pathogens.",
                                "Compare household heating energy sources: **charcoal jiko, gas stove, and microwave**.",
                                "Explain the biological risks of the **Temperature Danger Zone (5°C to 60°C)**.",
                                "Apply the **5 golden guidelines of safe reheating** to prevent food poisoning."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Reheating is a Food Safety Step",
                        "content": {
                            "title": "More Than Just Warming Food",
                            "text": "**Reheating** is the process of heating cooked leftover food to make it piping hot, tasty, and safe to eat. Reheating is a critical safety barrier: high heat destroys bacteria and pathogens that may have landed on food during storage!"
                        }
                    }
                ],
                # Page 2: The Temperature Danger Zone & 5 Golden Guidelines
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Temperature Danger Zone & 5 Golden Reheating Rules",
                        "content": {
                            "title": "The Temperature Danger Zone & 5 Golden Reheating Rules",
                            "caption": "Temperature spectrum showing Cold Storage (<4°C), the Danger Zone (5°C-60°C), and the Safe Reheating Zone (>74°C piping hot)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Golden Guidelines for Reheating Leftovers",
                        "content": {
                            "title": "Strict Reheating Safety Protocols",
                            "text": "- **1. Reheat Uniformly**: Stir stews and starches frequently during heating to distribute heat and eliminate cold spots where bacteria survive.\n- **2. Always Cover the Pot**: A tight lid traps steam, retaining moisture so food does not dry out while speeding up heating.\n- **3. Eat Immediately After Reheating**: Never leave reheated food sitting at room temperature; consume it right away.\n- **4. Remove Bones from Meat**: Large bones insulate meat and block heat circulation, leaving unsafe cold pockets.\n- **5. Inspect Spoilable Foods**: Easily-spoilable foods like fish must be checked for sour odors before heating; never attempt to reheat spoiled fish!"
                        }
                    }
                ],
                # Page 3: Comparing Household Reheating Energy Sources
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Household Reheating Equipment",
                        "content": {
                            "title": "Reheating Methods & Operational Characteristics",
                            "headers": ["Heating Method", "Fuel / Energy Source", "Operational Advantage", "Safety Precaution Required"],
                            "rows": [
                                ["Charcoal Jiko / Fire", "Charcoal or firewood", "Affordable and accessible in all rural/urban areas", "Stir constantly to prevent burning the pot bottom"],
                                ["Gas / Electric Stove", "LPG gas or electricity", "Precise flame and heat control for even warming", "Keep pot handles turned inward to avoid spills"],
                                ["Microwave Oven", "Electromagnetic waves", "Extremely fast reheating in minutes", "Cover bowl and stir halfway through to eliminate cold spots"]
                            ]
                        }
                    }
                ],
                # Page 4: Scenario Analysis: Uneven Heating Danger
                [
                    {
                        "type": "worked_example",
                        "title": "Safety Case Study: The Uneven Reheat Risk",
                        "content": {
                            "intro": "Wambui reheats a thick beef stew in a microwave for 2 minutes uncovered. The top feels warm, but the center around the large bone is cold.",
                            "steps": [
                                "**Violation 1 (Uncovered)**: Steam escaped, drying out the stew and slowing heat penetration.",
                                "**Violation 2 (Bone Left In)**: The thick bone blocked microwave waves, leaving cold pockets around the meat.",
                                "**Violation 3 (Not Stirred)**: Failing to stir left the center in the Temperature Danger Zone (5°C to 60°C).",
                                "**Health Consequence**: Surviving bacteria can trigger severe food poisoning and diarrhea.",
                                "**Correct Procedure**: Remove bones, cover bowl, heat until steaming, and stir halfway through."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Reheating Safety Rules",
                        "content": {
                            "question": "Why is it strongly recommended to remove large bones from cooked meat before reheating a leftover stew?",
                            "options": [
                                "Bones absorb all the salt and make the stew taste bland.",
                                "Large bones block heat circulation, leaving cold spots in the meat where bacteria can survive.",
                                "Bones dissolve and turn into toxic chemicals when heated twice.",
                                "Bones cause the metal cooking pot to rust."
                            ],
                            "answer": "B",
                            "explanation": "Dense bones act as thermal insulators that prevent heat from penetrating to the center of thick meat chunks. Removing bones ensures heat circulates uniformly to destroy all pathogens."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Reheating** makes leftovers tasty and destroys harmful food pathogens.\n- The **Temperature Danger Zone is 5°C to 60°C**, where bacteria multiply rapidly.\n- The 5 golden rules: **reheat uniformly, cover the pot, eat immediately, remove bones, and inspect fish/meat**.\n- Reheating food to **piping hot (above 74°C)** ensures complete safety."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we know the safety rules, let us step into the kitchen! In the next lesson, we carry out a practical activity to reheat leftovers safely while observing strict hygiene and burn-prevention protocols."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Practical Activity: Reheating Leftover Food Safely in the Kitchen
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Practical Activity: Reheating Leftover Food Safely in the Kitchen",
            "unit_description": "Hands-on kitchen reheating practical, workspace sanitization, adding moisture with fresh gravy/water, constant stirring, steaming lid, and the single-reheat rule.",
            "lesson_title": "Practical Activity: Reheating Leftover Food Safely in the Kitchen",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Kitchen Safety & Hygiene: Handwashing",
                        "content": {
                            "title": "Kitchen Safety & Hygiene: Handwashing",
                            "caption": "A student wearing a clean kitchen apron washing hands thoroughly with soap under running water before cooking."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: Safe Kitchen Reheating",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Sanitize kitchen countertops and organize clean cooking utensils.",
                                "Restore moisture to cold leftovers using clean water or fresh gravy.",
                                "Reheat food uniformly to a piping-hot steaming temperature using a stove or jiko.",
                                "Enforce the **single-reheat rule** and practice kitchen burn prevention."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Putting Reheating Rules into Action",
                        "content": {
                            "title": "Piping Hot and Delicious",
                            "text": "Today, we become kitchen chefs! Working in safety-equipped teams, we will safely reheat stored leftovers (such as githeri, rice, or stew) to piping-hot perfection."
                        }
                    }
                ],
                # Page 2: Step-by-Step Practical Reheating Protocol
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Operating Procedure: Safe Kitchen Reheating Flowchart",
                        "content": {
                            "title": "Standard Operating Procedure: Safe Kitchen Reheating Flowchart",
                            "caption": "Flowchart showing handwashing, food inspection, moistening with water/gravy, continuous stirring, steaming, and serving."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Reheating Leftovers",
                        "content": {
                            "title": "Step-by-Step Reheating Protocol",
                            "steps": [
                                "**Hygiene & Sanitization**: Wash hands with soap and water; wipe cooking counters and verify utensils are clean.",
                                "**Inspect Food**: Smell and inspect the stored leftovers for any sour odors or mold growth.",
                                "**Moisten the Food**: Put leftovers into a pot and add 2 to 3 tablespoons of clean water, stock, or fresh gravy to restore moisture.",
                                "**Apply Heat & Stir**: Heat over medium flame while stirring constantly to distribute heat and prevent sticking.",
                                "**Cover & Steam**: Place a tight-fitting lid on the pot and simmer for 5 to 10 minutes until steam rises actively throughout.",
                                "**Serve Hot with Pot-Holders**: Use dry kitchen mittens to lift hot pots safely; serve immediately onto clean plates."
                            ]
                        }
                    }
                ],
                # Page 3: The Danger of Multiple Reheating
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Single-Reheat Rule",
                        "content": {
                            "title": "Never Reheat Leftovers More Than Once!",
                            "text": "Every time food is heated and cooled down, it passes through the **Temperature Danger Zone (5°C to 60°C)**:\n\n- Surviving bacterial spores germinate, multiply, and produce heat-resistant toxins that cannot be destroyed by cooking again.\n- **Golden Action Rule**: If you have a large pot of leftover stew, scoop out only the exact portion needed for that meal and reheat it. Keep the remaining stew cold in the refrigerator!"
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Burn Prevention Protocol",
                        "content": {
                            "title": "Turn Pot Handles Inward!",
                            "text": "Always keep pot handles turned toward the back or side of the stove. Handles pointing outward can be caught by sleeves or knocked over, causing dangerous boiling spills!"
                        }
                    }
                ],
                # Page 4: Quality Checks & Practical Reflection
                [
                    {
                        "type": "worked_example",
                        "title": "Sensory Quality Check for Reheated Food",
                        "content": {
                            "intro": "How to verify that your reheated dish is safe and delicious:",
                            "steps": [
                                "**Steam Check**: Vigorous steam must rise from the center of the pot when the lid is removed.",
                                "**Moisture Check**: Grains and legumes should be soft and tender, not dry, hard, or crusty.",
                                "**Temperature Check**: The food must be piping hot throughout with zero cold spots in the middle."
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Reheating Portion Management",
                        "content": {
                            "question": "A family has a large 3-liter pot of leftover bean soup in the refrigerator. What is the safest way to reheat it for dinner?",
                            "options": [
                                "Boil the entire 3-liter pot, eat a small bowl, and return the warm pot to the fridge.",
                                "Scoop out only the exact portion needed for dinner into a small pot and reheat it, leaving the rest cold in the fridge.",
                                "Leave the pot on the kitchen counter for 24 hours to warm up naturally.",
                                "Add cold milk to cool the entire pot down."
                            ],
                            "answer": "B",
                            "explanation": "Scooping only the needed portion preserves the remaining soup cold in the refrigerator. Reheating the entire pot over and over passes the whole batch through the danger zone multiple times, triggering toxic bacterial growth."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Reheating requires **sanitized surfaces, clean utensils, and pot-holders**.\n- Adding a small splash of **clean water or fresh gravy** restores moisture to dry leftovers.\n- **Constant stirring and steaming under a tight lid** ensures uniform, piping-hot heating.\n- Enforce the **single-reheat rule**: only reheat the portion you intend to eat immediately."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Plain reheating warms yesterday's food. But what if we want to transform leftovers into an exciting, completely new dish? In the next lesson, we explore recipe definitions and the art of réchauffé cookery!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Recipe Definitions and the Benefits of Repurposing Leftovers
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Recipe Definitions and the Benefits of Repurposing Leftovers",
            "unit_description": "Recipe components, réchauffé cookery definition, repurposing philosophy, economic savings, and nutritional enhancement by adding fresh ingredients.",
            "lesson_title": "Recipe Definitions and the Benefits of Repurposing Leftovers",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Culinary Creativity: The Power of a Recipe",
                        "content": {
                            "title": "Culinary Creativity: The Power of a Recipe",
                            "caption": "A chef in a clean apron reviewing a recipe book in a bright kitchen with fresh vegetables and cooking ingredients arranged neatly."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Recipes & Réchauffé Cookery",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define a **recipe** and identify its 5 core structural components.",
                                "Define **réchauffé cookery** as the art of repurposing cooked leftovers into new dishes.",
                                "Analyze the **economic, nutritional, and creative benefits** of food repurposing.",
                                "Compare plain reheating versus creative réchauffé repurposing."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Roadmap to Culinary Success",
                        "content": {
                            "title": "What is a Recipe?",
                            "text": "A **recipe** is a structured set of written instructions that describes how to prepare, cook, and serve a specific food dish. Following a recipe ensures ingredients are combined in correct proportions to achieve consistent taste, texture, and nutrition!"
                        }
                    }
                ],
                # Page 2: Recipe Components & Réchauffé Cookery
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Anatomy of a Recipe & Réchauffé Philosophy",
                        "content": {
                            "title": "The 5 Core Components of a Recipe",
                            "text": "- **1. Dish Title**: Name of the meal.\n- **2. Ingredients List**: Exact types and quantities needed (e.g. 2 cups cooked rice, 1 diced carrot).\n- **3. Equipment Needed**: Tools required (pan, spatula, chopping board).\n- **4. Step-by-Step Instructions**: Sequential cooking actions (wash, dice, sauté, stir-fry, garnish).\n- **5. Cooking Time & Yield**: Expected duration and number of servings.\n\n**Réchauffé Cookery** is the culinary art of repurposing cooked leftover foods as primary raw ingredients to invent completely new, delicious, and nutritious meals!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Anatomy of a Professional Recipe & Réchauffé Cookery Framework",
                        "content": {
                            "title": "Anatomy of a Professional Recipe & Réchauffé Cookery Framework",
                            "caption": "Structural diagram illustrating the 5 recipe components and the transformation of cold leftovers into high-value dishes."
                        }
                    }
                ],
                # Page 3: Economic and Nutritional Advantages
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Plain Reheating vs. Réchauffé Repurposing",
                        "content": {
                            "title": "Evaluation: Plain Reheating vs. Creative Repurposing",
                            "headers": ["Evaluation Metric", "Plain Reheating", "Réchauffé Repurposing (New Recipe)"],
                            "rows": [
                                ["Flavor & Taste", "Identical to yesterday's meal; can taste dry or boring", "Fresh herbs, garlic, and seasonings create an exciting new flavor"],
                                ["Nutritional Balance", "Unchanged from original cooked meal", "Enhanced by adding fresh vegetables, greens, eggs, or nuts"],
                                ["Visual Appearance", "Looks like warmed-up old food", "Vibrant, colorful, garnished, and highly appetizing"],
                                ["Culinary Skill", "Simple warming (low skill)", "Builds creativity, ingredient auditing, and kitchen independence"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example: Enhancing Nutrition
                [
                    {
                        "type": "worked_example",
                        "title": "Nutritional Transformation: Upgrading Plain Leftovers",
                        "content": {
                            "intro": "How a student transforms plain leftover white rice into a nutritionally complete meal:",
                            "steps": [
                                "**Base Ingredient**: 2 cups of cold white rice (provides energy carbohydrates).",
                                "**Nutritional Addition 1**: 1/2 cup diced carrots and green peas (adds Vitamin A and dietary fiber).",
                                "**Nutritional Addition 2**: 1 scrambled egg or shredded leftover chicken (adds high-value protein and iron).",
                                "**Aromatic Addition**: Sautéed garlic and onions (adds antioxidants and savory flavor).",
                                "**Result**: A balanced, high-protein, vitamin-rich plate of **Vegetable Fried Rice** made in 10 minutes!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Réchauffé Cookery",
                        "content": {
                            "question": "What does the culinary term 'réchauffé cookery' refer to?",
                            "options": [
                                "Baking fresh bread from newly bought flour.",
                                "The culinary art of repurposing cooked leftover foods into delicious, high-quality new dishes.",
                                "Freezing raw meat in a commercial cold room.",
                                "Composting spoiled organic matter in a garden pit."
                            ],
                            "answer": "B",
                            "explanation": "Réchauffé is a French culinary term referring to the art of reheating and repurposing cooked leftovers into creative, appetizing new dishes (like turning leftover ugali into crispy ugali bites)."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- A **recipe** contains title, ingredients, equipment, sequential steps, time, and yield.\n- **Réchauffé cookery** transforms cold leftovers into exciting new meals.\n- Repurposing saves family money by utilizing ingredients already paid for.\n- Adding fresh vegetables and eggs **boosts vitamins, fiber, and protein** in the diet."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we prepare cold leftovers to fit into these new recipes? In the next lesson, we master physical preparation techniques (dicing, shredding, chopping) and explore 3 classic Kenyan réchauffé recipes!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Adapting Creative Recipes to Minimize Food Wastage
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Adapting Creative Recipes to Minimize Food Wastage",
            "unit_description": "Dicing, shredding, and chopping techniques, fresh gravy moistening, careful seasoning, and adapting ugali bites, vegetable fried rice, and saucy githeri.",
            "lesson_title": "Adapting Creative Recipes to Minimize Food Wastage",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Culinary Techniques: Dicing & Shredding",
                        "content": {
                            "title": "Culinary Techniques: Dicing & Shredding",
                            "caption": "Hands using a kitchen knife to dice carrots and chop onions neatly on a clean wooden cutting board."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Recipe Adaptation",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain how physical techniques (**dicing, shredding, chopping**) alter food texture.",
                                "Describe how to restore moisture using **fresh gravy** and apply seasonings carefully.",
                                "Master the recipe formulations for **ugali bites, vegetable fried rice, and githeri in tomato sauce**.",
                                "Evaluate how shallow frying creates an appetizing crispy texture on stale starches."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Changing Shape to Transform Taste",
                        "content": {
                            "title": "Overcoming Hard, Cold Textures",
                            "text": "When cooked foods sit in storage, they lose water and turn hard or clumped. By changing their physical shape through cutting, we allow heat and seasonings to penetrate deeply, transforming their texture!"
                        }
                    }
                ],
                # Page 2: Physical Preparation Techniques & Flavor Restoration
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dicing, Shredding, and Moistening with Gravy",
                        "content": {
                            "title": "Physical & Flavor Techniques",
                            "text": "- **Dicing**: Cutting dense leftovers (hard ugali, boiled potatoes, meat chunks) into small, uniform cubes so they heat rapidly and evenly.\n- **Shredding**: Tearing cooked meats (beef, chicken) or cabbage into thin fibers that mix smoothly into rice and sauces.\n- **Moistening with Fresh Gravy**: Cold leftovers dry out easily. Adding fresh, flavorful gravy made on that day restores moisture and rich taste.\n- **Careful Flavoring**: Sautéing with fresh onions, garlic, ginger, and spices (curry powder, black pepper) replaces lost flavors."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The 3 Classic Réchauffé Culinary Pathways",
                        "content": {
                            "title": "The 3 Classic Réchauffé Culinary Pathways",
                            "caption": "Branching diagram mapping leftover ugali to crispy ugali bites, leftover rice to vegetable fried rice, and leftover githeri to saucy githeri."
                        }
                    }
                ],
                # Page 3: Three Classic Kenyan Réchauffé Recipes
                [
                    {
                        "type": "comparison_table",
                        "title": "Three Classic Leftover Repurposing Formulations",
                        "content": {
                            "title": "Réchauffé Recipe Formulas",
                            "headers": ["Recipe Name", "Base Leftover Used", "Preparation Method", "Cooking Technique & Result"],
                            "rows": [
                                ["Crispy Ugali Bites", "Leftover hard ugali", "Dice into small 2cm cubes; toss with curry powder & salt", "Shallow fry in hot oil until golden brown and crispy outside, soft inside"],
                                ["Vegetable Fried Rice", "Leftover boiled rice", "Break cold rice clumps; dice carrots, onions & garlic", "Sauté aromatics; add rice and veggies; stir-fry continuously for 5 mins"],
                                ["Githeri in Tomato Sauce", "Leftover plain githeri", "Rinse lightly; prepare fresh tomato paste and gravy", "Sauté onions; add tomato paste & fresh gravy; simmer githeri until saucy"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example: Making Crispy Ugali Bites
                [
                    {
                        "type": "step_process",
                        "title": "Standard Recipe: Crispy Ugali Bites",
                        "content": {
                            "title": "Step-by-Step Ugali Bite Instructions",
                            "steps": [
                                "**Cube the Ugali**: Take cold hard ugali and dice it into neat, uniform 2cm cubes on a clean cutting board.",
                                "**Season**: Toss the cubes in a bowl with a pinch of salt, curry powder, or paprika.",
                                "**Heat Pan**: Heat 3 tablespoons of cooking oil in a shallow frying pan over medium-high heat.",
                                "**Shallow Fry**: Place ugali cubes into the pan and fry for 4 to 6 minutes, turning frequently until all sides are golden and crispy.",
                                "**Drain & Serve**: Remove with a slotted spoon onto a paper towel; serve hot with fresh dipping sauce or tea!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Moisture Restoration",
                        "content": {
                            "question": "Why is freshly prepared gravy added when reheating or repurposing dry leftover foods?",
                            "options": [
                                "To dissolve the metal cooking pan.",
                                "To restore lost moisture and enrich the dish with savory flavor and tenderness.",
                                "To freeze the starch grains instantly.",
                                "To turn the food into sweet sugar."
                            ],
                            "answer": "B",
                            "explanation": "Stored leftovers lose water and dry out. Adding fresh gravy made on that day restores essential moisture, prevents burning, and enriches the meal with savory juices and seasonings."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Dicing, chopping, and shredding** improve heat circulation and texture.\n- **Fresh gravy made that day** restores lost moisture to dry leftovers.\n- **Sautéing with fresh garlic, onions, and spices** restores deep, rich flavor.\n- Stale ugali, rice, and githeri transform easily into **ugali bites, fried rice, and saucy stews**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "It is time to step into the kitchen and cook! In the next lesson, we execute a collaborative cooking practical: preparing Vegetable Fried Rice using leftover rice and fresh vegetables."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Practical Activity: Preparing a New Recipe from Leftover Food
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Practical Activity: Preparing a New Recipe from Leftover Food",
            "unit_description": "Hands-on preparation of Vegetable Fried Rice using leftover rice, mise en place, knife safety, uniform stir-frying, and sensory evaluation.",
            "lesson_title": "Practical Activity: Preparing a New Recipe from Leftover Food",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Finished Dish: Vegetable Fried Rice",
                        "content": {
                            "title": "The Finished Dish: Vegetable Fried Rice",
                            "caption": "A hot, colorful plate of vegetable fried rice with diced carrots, green onions, and golden scrambled egg, garnished with fresh coriander."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: Cooking Fried Rice",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Organize ingredients and tools following the **Mise en Place** principle.",
                                "Execute safe vegetable dicing and knife handling protocols.",
                                "Stir-fry cold leftover rice uniformly with aromatics, carrots, and peas.",
                                "Perform a **sensory evaluation** rating appearance, texture, flavor, and neat presentation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hands-On Kitchen Challenge",
                        "content": {
                            "title": "Transforming Plain Rice into Culinary Gold",
                            "text": "Today, every student team will operate a kitchen station to turn cold, clumped leftover white rice into a steaming, colorful plate of Vegetable Fried Rice!"
                        }
                    }
                ],
                # Page 2: Step-by-Step Practical Stir-Frying Operation
                [
                    {
                        "type": "suggested_diagram",
                        "title": "5-Stage Mise en Place & Stir-Frying Operation Workflow",
                        "content": {
                            "title": "5-Stage Mise en Place & Stir-Frying Operation Workflow",
                            "caption": "Step-by-step workflow from ingredient mise en place to aromatic sauté, hard veggie cooking, rice addition, and garnished plating."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Vegetable Fried Rice",
                        "content": {
                            "title": "Step-by-Step Cooking Instructions",
                            "steps": [
                                "**Mise en Place & Hygiene**: Wash hands with soap; break cold rice clumps gently; dice onions, garlic, and carrots on a clean board.",
                                "**Sauté Aromatics**: Heat 2 tablespoons of oil in a frying pan over medium heat; add onions and garlic, sautéing for 2 minutes until fragrant.",
                                "**Cook Hard Vegetables**: Add diced carrots and peas; stir-fry for 3 minutes until tender-crisp.",
                                "**Add Leftovers & Stir-fry**: Add the leftover cooked rice (and optional scrambled egg/chicken); stir-fry continuously for 5 minutes until steaming hot throughout.",
                                "**Season & Garnish**: Sprinkle salt and spices; serve hot onto clean plates garnished with fresh chopped coriander.",
                                "**Kitchen Clean-up**: Wash knives, cutting boards, and pans immediately with warm soapy water."
                            ]
                        }
                    }
                ],
                # Page 3: Sensory Evaluation Framework
                [
                    {
                        "type": "comparison_table",
                        "title": "Sensory Evaluation Matrix for Fried Rice",
                        "content": {
                            "title": "Sensory Quality Rubric",
                            "headers": ["Evaluation Dimension", "High Quality Standard (Excellent)", "Common Cooking Fault (Needs Improvement)"],
                            "rows": [
                                ["Visual Appearance", "Vibrant colors (orange carrots, green peas, golden rice); neat garnish", "Dull, pale, burnt dark spots, or messy plating"],
                                ["Rice Texture", "Separate, light, fluffy grains with tender-crisp vegetables", "Soggy mushy grains or hard, unchewable dry lumps"],
                                ["Flavor & Aroma", "Balanced savory garlic/onion aroma with pleasant mild seasoning", "Bland (lacks salt/spices) or overly salty/burnt taste"],
                                ["Serving Temperature", "Piping hot throughout (steam actively rising from plate)", "Lukewarm or cold in the center (danger zone!)"]
                            ]
                        }
                    }
                ],
                # Page 4: Practical Reflection
                [
                    {
                        "type": "mini_activity",
                        "title": "Team Sensory Evaluation",
                        "content": {
                            "title": "Rate Your Team's Dish",
                            "instruction": "Taste your completed Vegetable Fried Rice with your team. Grade your dish on a scale of 1 to 5 for Appearance, Texture, and Flavor in your practical logbook."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Dicing for Fried Rice",
                        "content": {
                            "question": "Why is it important to chop vegetables into small, uniform cubes when preparing vegetable fried rice from leftover rice?",
                            "options": [
                                "Small pieces cook quickly at the same rate and blend evenly with the rice grains.",
                                "Small pieces dissolve completely into cooking oil.",
                                "Small cubes make the pan heat up twice as fast.",
                                "Small cubes prevent vegetables from absorbing vitamins."
                            ],
                            "answer": "A",
                            "explanation": "Dicing vegetables into small, uniform cubes ensures they soften quickly and cook at an even pace, mixing smoothly with rice grains to give a colorful, balanced bite."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Mise en Place** (organizing ingredients first) makes cooking fast and stress-free.\n- **Sautéing aromatics** builds a deep flavor foundation for plain leftovers.\n- **Continuous stir-frying** distributes heat evenly and prevents sticking.\n- Immediate **kitchen clean-up and sanitization** prevents accidents and pests."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have created a delicious meal from leftovers! But how do we handle food daily to make sure it never makes our families sick? In our final capstone lesson, we master food safety rules, review an instructional video, and complete the Topic Assessment."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Food Safety in Handling and Storing Leftover Food & Capstone Review
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Food Safety in Handling and Storing Leftover Food",
            "unit_description": "Food safety principles, food poisoning prevention, the 2-hour rule, cross-contamination barriers, instructional video review, and topic-level summative assessment.",
            "lesson_title": "Food Safety in Handling and Storing Leftover Food",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Food Safety & Clean Containers: Protecting Health",
                        "content": {
                            "title": "Food Safety & Clean Containers: Protecting Health",
                            "caption": "A clean kitchen counter showing sealed, airtight food storage containers keeping cooked food separate from raw ingredients."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Food Safety & Capstone Review",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **food safety** and explain how proper handling prevents **foodborne illness (food poisoning)**.",
                                "Apply the **2-Hour Rule** and establish cross-contamination barriers between raw and cooked food.",
                                "Synthesize the entire topic through an **instructional video review**.",
                                "Demonstrate complete mastery by completing the **Topic Summative Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Golden Rule of Kitchen Hygiene",
                        "content": {
                            "title": "Protecting Family Health",
                            "text": "**Food safety** refers to the scientific practices used when handling, storing, and reheating leftovers to prevent food poisoning. Practicing strict food safety protects families from painful illnesses, saves money on medical bills, and prevents wasting edible food!"
                        }
                    }
                ],
                # Page 2: Food Safety Barriers & The 2-Hour Rule
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Kitchen Food Safety Barrier & The 2-Hour Rule Breakdown",
                        "content": {
                            "title": "Kitchen Food Safety Barrier & The 2-Hour Rule Breakdown",
                            "caption": "Diagram detailing the physical separation of raw and cooked foods, clean container sealing, and prompt refrigeration within 2 hours."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Food Safety Principles",
                        "content": {
                            "title": "3 Non-Negotiable Food Safety Rules",
                            "text": "- **1. Use Clean, Dry, Airtight Containers**: Always wash containers with warm soapy water and dry them thoroughly. Tight lids lock out airborne bacteria and prevent drying out.\n- **2. The 2-Hour Rule**: Never let cooked food sit at room temperature for more than **2 hours**. Refrigerate or freeze promptly to halt rapid bacterial multiplication.\n- **3. Prevent Cross-Contamination**: Keep raw meats, poultry, and fish completely separate from cooked leftovers. Never use unwashed cutting boards or tasting spoons in cooked food!"
                        }
                    }
                ],
                # Page 3: Safe vs. Dangerous Kitchen Habits
                [
                    {
                        "type": "comparison_table",
                        "title": "Evaluation: Safe vs. Dangerous Leftover Practices",
                        "content": {
                            "title": "Kitchen Safety Matrix",
                            "headers": ["Kitchen Habit", "Safe Food Practice", "Dangerous Practice (Risk of Food Poisoning!)"],
                            "rows": [
                                ["Cool-Down Timing", "Cool cooked food to room temperature and refrigerate within 2 hours", "Leaving cooked food uncovered on dining table overnight"],
                                ["Container Selection", "Clean, dry, airtight plastic or glass containers with tight lids", "Storing food in open plates or rusted, uncovered pots"],
                                ["Reheating Portions", "Scoop only the portion needed and reheat to piping hot (>74°C)", "Reheating the entire large pot over and over for three days"],
                                ["Spoilage Check", "Smell and inspect food; discard immediately if it smells sour", "Reheating moldy or sour food hoping heat kills the bad taste"],
                                ["Raw/Cooked Separation", "Keep raw meat juices completely away from cooked leftovers", "Placing cooked rice on a board that just held raw chicken"]
                            ]
                        }
                    }
                ],
                # Page 4: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: The 2-Hour Rule",
                        "content": {
                            "question": "Under standard food safety guidelines, what is the maximum amount of time cooked food can safely sit at room temperature before being refrigerated?",
                            "options": [
                                "12 hours",
                                "2 hours",
                                "24 hours",
                                "5 days"
                            ],
                            "answer": "B",
                            "explanation": "The '2-Hour Rule' states that cooked leftovers must be refrigerated within 2 hours of preparation. Leaving food at room temperature longer allows harmful bacteria to multiply rapidly in the danger zone."
                        }
                    }
                ],
                # Page 5: Topic Master Synthesis
                [
                    {
                        "type": "key_takeaway",
                        "title": "Topic 2 Master Summary",
                        "content": {
                            "text": "- **Leftovers** represent paid resources, saved money, and household food security.\n- **Refrigeration (2-3 days)**, **Freezing (months)**, **Pickling (veggies)**, and **Composting (scraps)** form the core conservation toolset.\n- **Reheating to piping hot (>74°C)**, covering pots, and stirring eliminates cold spots and destroys pathogens.\n- **Réchauffé cookery** transforms stale ugali, rice, and githeri into crispy bites, fried rice, and saucy stews.\n- Enforcing the **2-Hour Rule and single-reheat limit** keeps your family safe from food poisoning."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Food Safety - Cooling, Storing and Using Leftovers",
                        "content": {
                            "title": "Topic Video Review: Food Safety - Cooling, Storing and Using Leftovers",
                            "url": "https://www.youtube.com/watch?v=0EErECU8PXU",
                            "resolved_video_id": "0EErECU8PXU",
                            "caption": "Watch this essential food safety demonstration illustrating how to cool, package, store, and reheat leftovers safely to prevent bacterial growth and protect family health."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Things to Observe in the Video",
                        "content": {
                            "title": "Focus Questions for Video Reflection",
                            "text": "- **1. Prompt Cooling**: Notice how food is portioned into shallow containers for rapid cooling.\n- **2. Container Airtightness**: Observe how airtight lids seal in moisture and block contaminants.\n- **3. Uniform Heat**: Watch how food is heated until steaming hot throughout."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Leftover Definition",
                        "content": {
                            "question": "What is defined as food that has been prepared and cooked for a meal but not all eaten at once?",
                            "options": [
                                "Conserved forage",
                                "Leftover food",
                                "Sautéed aromatics",
                                "Organic manure"
                            ],
                            "answer": "B",
                            "explanation": "Leftover food refers to any cooked or prepared food that remains uneaten after a meal is finished. Conserved forage refers to livestock feed."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Financial Benefits",
                        "content": {
                            "question": "Which of the following is a primary financial advantage of conserving leftover food at home?",
                            "options": [
                                "It eliminates the need for any hand hygiene in the kitchen.",
                                "It reduces daily food expenses because ingredients already bought are fully utilized.",
                                "It increases the amount of charcoal fuel required to cook meals.",
                                "It allows families to purchase expensive high-tech kitchen gadgets."
                            ],
                            "answer": "B",
                            "explanation": "Conserving leftovers saves family money because it utilizes food and ingredients already paid for, significantly reducing the need to buy new groceries daily."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 4)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Culinary Terminology",
                        "content": {
                            "question": "What is the French culinary term used to describe the creative art of transforming cold cooked leftovers into delicious new dishes?",
                            "options": [
                                "Mise en place",
                                "Réchauffé cookery",
                                "Composting",
                                "Sautéing"
                            ],
                            "answer": "B",
                            "explanation": "'Réchauffé' is a French culinary term that refers to reheating or repurposing cooked leftovers into high-quality, creative new dishes (such as turning ugali into crispy ugali bites)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Moisture Restoration",
                        "content": {
                            "question": "If you have dry leftover cooked rice, why is it recommended to add a splash of fresh gravy or water when reheating it?",
                            "options": [
                                "To completely freeze the rice grains and stop mold.",
                                "To dissolve any bones that might be mixed into the starch.",
                                "To restore lost moisture and prevent the rice from being dry and hard.",
                                "To turn the starches into sweet glucose sugars."
                            ],
                            "answer": "C",
                            "explanation": "Leftover cooked rice dries out easily during storage. Adding a small splash of clean water or fresh gravy made that day restores moisture, making the rice soft, tender, and delicious."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 5 to 7)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Composting Rules",
                        "content": {
                            "question": "When composting kitchen organic waste, why should cooked oily stews and meats be excluded from a basic compost heap?",
                            "options": [
                                "Cooked meats prevent the pile from absorbing oxygen.",
                                "Cooked foods and oils decompose too fast and turn into liquid water.",
                                "Cooked meats and oils attract rodents like rats and create foul, putrid odors.",
                                "They contain too many nutrients that destroy soil fertility."
                            ],
                            "answer": "C",
                            "explanation": "While raw vegetable peels and eggshells compost cleanly, cooked oily foods and meats attract pests like rats and create terrible rotting smells, so they must be excluded from simple backyard compost heaps."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Cold Storage Selection",
                        "content": {
                            "question": "A student has a large bowl of cooked beef stew that the family plans to eat in three weeks. What is the most appropriate conservation method?",
                            "options": [
                                "Pickling in a jar of vinegar",
                                "Refrigeration in a covered plastic box",
                                "Freezing in a sealed airtight container",
                                "Leaving it on a jiko at room temperature"
                            ],
                            "answer": "C",
                            "explanation": "Freezing stores food below 0°C, which completely halts bacterial growth, making it the best choice for multi-week storage. Refrigeration only keeps food safe for 2 to 3 days."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Refrigerator Thermodynamics",
                        "content": {
                            "question": "Why should cooked hot food be allowed to cool down to room temperature before placing it inside a refrigerator?",
                            "options": [
                                "Placing hot food inside raises the refrigerator's internal temperature, which can spoil other stored foods.",
                                "Cool air in the refrigerator destroys the nutrients of hot food.",
                                "Hot food will crack the refrigerator's metal shelves.",
                                "Hot food prevents the refrigerator from running on electricity."
                            ],
                            "answer": "A",
                            "explanation": "Putting hot steaming food directly into a refrigerator heats up the interior air. This temperature rise can push other refrigerated foods into the danger zone (5°C to 60°C), causing rapid spoilage."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 8 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Safe Room-Temperature Limit",
                        "content": {
                            "question": "Under food safety guidelines, what is the maximum amount of time cooked food should sit at room temperature before being refrigerated?",
                            "options": [
                                "10 hours",
                                "2 hours",
                                "24 hours",
                                "5 days"
                            ],
                            "answer": "B",
                            "explanation": "The '2-Hour Rule' states that cooked leftovers must be refrigerated within 2 hours of cooking. Letting food sit at room temperature longer allows harmful bacteria to multiply rapidly."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Multiple Reheat Danger",
                        "content": {
                            "question": "A cook reheats a large pot of bean soup on Monday, cools it, reheats it Tuesday, cools it, and reheats it Wednesday. Everyone gets sick. What caused the illness?",
                            "options": [
                                "The soup lacked spices and salt, which caused stomach irritation.",
                                "Moving the soup through multiple heating and cooling cycles allowed bacteria to multiply in the danger zone and release heat-resistant toxins.",
                                "The refrigerator was too cold, turning starch into poison.",
                                "The soup absorbed chemicals from being stirred with a wooden spoon."
                            ],
                            "answer": "B",
                            "explanation": "Leftovers should never be reheated more than once or twice. Repeatedly heating and cooling the entire batch passes the food through the temperature danger zone repeatedly, allowing bacteria to multiply and release toxic heat-resistant toxins."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Culinary Dicing Principles",
                        "content": {
                            "question": "Why is dicing hard leftover ugali into small, uniform cubes before frying or sautéing considered an effective culinary technique?",
                            "options": [
                                "It changes physical shape and surface area, allowing pieces to heat uniformly and quickly while creating a crispy, delicious outer layer.",
                                "It turns the starch into liquid water, preventing the dish from drying out.",
                                "Small cubes absorb metal from the frying pan, adding iron nutrients.",
                                "It keeps the ugali soft and wet on the outside while leaving the inside raw."
                            ],
                            "answer": "A",
                            "explanation": "Slicing hard ugali into small, uniform cubes increases surface area. Sautéing or shallow frying these cubes allows heat to circulate quickly and uniformly, transforming stale starch into delicious, crispy ugali bites."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade9_agriculture_topic2(replace: bool = True):
    """Executes the database transaction to ingest Topic 2 into CBC Grade 9 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 9 AGRICULTURE — TOPIC 2")
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
        topic_name = "Conserving Leftover Food (Meaning, Importance, and Household Methods)"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 2,
                "description": "Comprehensive domestic leftover food management, household preservation (refrigeration, freezing, pickling, composting), safe reheating, réchauffé cookery recipes, and food safety hygiene."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        # 3. Ingest Units and Lessons
        curriculum_data = build_topic2_curriculum()
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
                        block_id=f"g9_agri_t2_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Topic 2: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade9_agriculture_topic2(replace=replace_flag)
