"""
VLearn CBC Grade 9 Agriculture — Topic 3: Integrated Farming
Production Ingestion Engine (Phase 1: Content & Card Architecture)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 9 (Level: 9)
Subject: Agriculture
Topic: Integrated Farming (Topic Order: 3)

Decomposed into 11 Learning Units & 11 Published Lessons:
  1. Meaning of Integrated Farming and Its Resource-Conservation Importance (6 Pages, 12 Blocks)
  2. System Components: Crop Production and Nutrient Recycling (6 Pages, 12 Blocks)
  3. System Components: Livestock Integration and Manure Recycling (6 Pages, 12 Blocks)
  4. System Components: Aquaculture (Fish Farming) and Water Nutrient Loops (6 Pages, 12 Blocks)
  5. System Components: Agroforestry, Soil Erosion, and Microclimate Benefits (6 Pages, 12 Blocks)
  6. System Components: Small-Scale Animal Keeping (Rabbit and Poultry) (6 Pages, 12 Blocks)
  7. System Components: Vegetable Production on an Integrated Farm (6 Pages, 12 Blocks)
  8. Relational Benefits of Vegetable Production, Poultry, and Rabbit Keeping (6 Pages, 12 Blocks)
  9. Organic Waste and Water Management Systems (6 Pages, 12 Blocks)
  10. Practical Activity: Designing an Integrated Farm Layout on Manila Paper (6 Pages, 11 Blocks)
  11. Practical Activity: Constructing a 3D Integrated Farm Model & Capstone (10 Pages, 21 Blocks)

Features:
  - Rich typography with bold key terms and structured markdown bullet points.
  - Step-by-step practical process workflows.
  - Formatted comparison tables, classification matrices, and callouts.
  - Formative scenario MCQs and Topic Summative MCQs with educational explanations.
  - Zero citation bracket leaks, zero meta-tag leaks, and zero raw LaTeX.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade9_agriculture_topic3.py [--replace]
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
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 3: Integrated Farming."""
    return [
        # =====================================================================
        # LESSON 1: Meaning of Integrated Farming and Its Resource-Conservation Importance
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Meaning of Integrated Farming and Its Resource-Conservation Importance",
            "unit_description": "Integrated farming system definition, closed-loop recycling, zero-waste philosophy, economic resilience, and household food security.",
            "lesson_title": "Meaning of Integrated Farming and Its Resource-Conservation Importance",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "A Thriving Ecosystem: The Integrated Farm",
                        "content": {
                            "title": "A Thriving Ecosystem: The Integrated Farm",
                            "caption": "A smallholder farm where dairy cattle, poultry, and diverse vegetable crops coexist in a closed-loop system."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Integrated Farming Systems",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **integrated farming** as a system of mutually beneficial agricultural enterprises.",
                                "Explain the fundamental **zero-waste closed-loop philosophy**.",
                                "Analyze the **economic, environmental, and nutritional benefits** of integrated agriculture.",
                                "Trace the core nutrient flow: Crop Residues -> Animal Feed -> Manure -> Soil -> Crops."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Integrated Farming?",
                        "content": {
                            "title": "Farming in Harmony with Nature",
                            "text": "**Integrated farming** is a sustainable agricultural practice that combines multiple farming enterprises (such as crops, livestock, aquaculture, agroforestry, and poultry) on the same plot of land.\n\n- **The Golden Rule**: There is **no waste** in an integrated farm! The byproduct or waste of one enterprise becomes a vital input for another.\n- **Connected Ecosystem**: Instead of treating crops and animals as separate businesses, the farmer manages them as a single circular web of life."
                        }
                    }
                ],
                # Page 2: Core Benefits of Integrated Agriculture
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 4 Main Advantages of Integrated Farming",
                        "content": {
                            "title": "Why Farmers Choose Integrated Systems",
                            "text": "- **1. Environmental Protection**: Eliminates reliance on synthetic chemical fertilizers and toxic pesticides by utilizing organic manure and biological pest control.\n- **2. Long-Term Soil Health**: Continuous organic manure application maintains soil moisture, restores humus, and prevents land degradation.\n- **3. Financial Resilience**: Diverse enterprises provide year-round household income and drastically reduce cash spending on commercial feeds and fertilizers.\n- **4. Balanced Family Nutrition**: Produces a healthy mix of vegetables, fruits, milk, meat, and eggs on a single piece of land."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Single-Enterprise vs. Integrated Farming",
                        "content": {
                            "title": "Farming Systems Comparison",
                            "headers": ["Evaluation Metric", "Single-Crop / Monoculture Farming", "Integrated Closed-Loop Farming"],
                            "rows": [
                                ["External Inputs", "High (Heavy spending on synthetic fertilizers and chemicals)", "Minimal (Uses on-farm recycled animal manure and compost)"],
                                ["Waste Generation", "High (Crop residues and dung are burned or dumped)", "Zero (All byproducts are recycled into adjacent enterprises)"],
                                ["Income Stability", "Vulnerable (One bad harvest can ruin the family financially)", "Resilient (Multiple income streams: milk, eggs, crops, fish)"],
                                ["Environmental Impact", "Soil depletion, water pollution, and chemical runoff", "Enhanced soil fertility, carbon storage, and biodiversity"]
                            ]
                        }
                    }
                ],
                # Page 3: The Closed-Loop Recycling Architecture
                [
                    {
                        "type": "suggested_diagram",
                        "title": "System Nutrients Closed-Loop Flowchart",
                        "content": {
                            "title": "System Nutrients Closed-Loop Flowchart",
                            "caption": "Circular diagram tracing nutrient exchange between crops, livestock, compost, and soil."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Nutrient Loop in Action",
                        "content": {
                            "title": "Continuous Circular Nutrient Flow",
                            "text": "In an integrated farm, resources travel in a continuous cycle:\n\n1. **Crops** produce grain for humans and dry stover/vines for livestock.\n2. **Livestock** eat crop residues and convert them into nutrient-rich dung and urine.\n3. **Composting systems** decompose animal waste with bedding straw into rich manure.\n4. **Soil** absorbs the manure, feeding the next generation of lush, healthy crops!"
                        }
                    }
                ],
                # Page 4: Scenario Analysis: Relational Synergy
                [
                    {
                        "type": "worked_example",
                        "title": "Economic Case Study: The Self-Sustaining Homestead",
                        "content": {
                            "intro": "Farmer Omwamba operates a 1-acre farm. He previously spent 8,000 KES monthly on synthetic fertilizers and dairy feed.",
                            "steps": [
                                "**System Upgrade**: Omwamba integrates a dairy cow shed, 20 kienyeji chickens, and a compost pit next to his vegetable plots.",
                                "**Feed Savings**: He feeds sweet potato vines and maize stover to his cow, cutting commercial feed bills by 70%.",
                                "**Fertilizer Savings**: Cow manure and chicken droppings fertilize his kales and maize, eliminating synthetic fertilizer purchases.",
                                "**Outcome**: Omwamba saves over 6,000 KES monthly while selling fresh milk, eggs, and organic vegetables every week!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Fundamental Principles",
                        "content": {
                            "question": "What is the primary guiding principle of a successful integrated farming system?",
                            "options": [
                                "Every enterprise must rely exclusively on synthetic chemical inputs.",
                                "Waste from one enterprise is recycled to become an input for another enterprise.",
                                "All farm animals and crops must be completely isolated from each other.",
                                "Crop residues must be burned in the field to clear space."
                            ],
                            "answer": "B",
                            "explanation": "The core philosophy of integrated farming is the closed-loop system: there is no waste. The byproduct of one enterprise (such as animal manure or crop stover) serves as a valuable resource for another."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Integrated farming** combines multiple enterprises on one piece of land.\n- The system operates on a **zero-waste closed-loop principle**.\n- It lowers production costs, builds **soil fertility naturally**, and stabilizes household income.\n- Nutrients flow continuously: Crops -> Livestock -> Manure -> Soil -> Crops."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we understand the system framework, let us explore its first major pillar: crop production! In the next lesson, we examine how crops generate biomass and how crop residues are recycled back into the soil."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: System Components: Crop Production and Nutrient Recycling
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "System Components: Crop Production and Nutrient Recycling",
            "unit_description": "Crop production role, biomass generation, maize stover, wheat straw, legume vines, and the 4-stage crop residue decomposition cycle.",
            "lesson_title": "System Components: Crop Production and Nutrient Recycling",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Harvested Fields: The Value of Crop Residues",
                        "content": {
                            "title": "Harvested Fields: The Value of Crop Residues",
                            "caption": "Rows of harvested maize stalks lying on the soil, ready for collection, livestock feeding, or composting."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Crop Biomass & Recycling",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain the role of crop production as a primary organic biomass generator.",
                                "Identify common **crop residues**: maize stover, wheat straw, and legume vines.",
                                "Describe the **4-stage process of crop residue decomposition**.",
                                "Explain why burning crop residues harms soil fertility and pollutes the air."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Crops as Biomass Generators",
                        "content": {
                            "title": "More Than Just Grain",
                            "text": "In an integrated farm, crops serve a double purpose:\n\n- **1. Direct Human Food & Forage**: Produces grains, seeds, and leafy fodder to feed the farm household and livestock.\n- **2. Organic Biomass**: Generates massive volumes of plant leftovers that capture solar carbon and soil minerals for farm recycling."
                        }
                    }
                ],
                # Page 2: Identifying Crop Residues
                [
                    {
                        "type": "concept_explanation",
                        "title": "What are Crop Residues?",
                        "content": {
                            "title": "Valuable Post-Harvest Materials",
                            "text": "**Crop residues** are plant materials remaining in the field after human food has been harvested:\n\n- **Maize Stover**: Dry stalks, leaves, and husks remaining after picking maize ears.\n- **Straw**: Fibrous stems of wheat, barley, and rice left after threshing grains.\n- **Legume Vines**: High-protein leftover foliage of beans, groundnuts, and peas that are exceptionally rich in nitrogen."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Protection",
                        "content": {
                            "title": "Never Burn Crop Residues!",
                            "text": "Burning crop residues destroys valuable organic carbon and nitrogen, turns beneficial soil microbes into ash, and releases choking greenhouse gases. Always chop and compost residues instead!"
                        }
                    }
                ],
                # Page 3: The 4-Stage Residue Decomposition Process
                [
                    {
                        "type": "suggested_diagram",
                        "title": "4-Stage Crop Residue Decomposition Cycle",
                        "content": {
                            "title": "4-Stage Crop Residue Decomposition Cycle",
                            "caption": "Sequential flowchart showing Collection, Chipping with panga, Heaping/Composting, and Nutrient Return to soil."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Residue Recycling",
                        "content": {
                            "title": "Step-by-Step Biomass Decomposition",
                            "steps": [
                                "**Collection**: Gather dry stalks, husks, and vines from the field immediately following harvest.",
                                "**Chipping / Chopping**: Cut tough stalks into 5cm to 10cm pieces using a panga to increase surface area for microbial decay.",
                                "**Piling & Moistening**: Layer chopped residues in a compost pit or heap, mixing with animal dung and water to accelerate rotting.",
                                "**Nutrient Return**: Spread the finished dark organic manure across crop beds to restore essential minerals."
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example: Sorting Plant Residues
                [
                    {
                        "type": "worked_example",
                        "title": "Resource Allocation: Matching Residues to Optimal Uses",
                        "content": {
                            "intro": "How a farmer optimizes different post-harvest residues:",
                            "steps": [
                                "**Green Bean Vines**: Highly digestible and protein-rich -> Feed directly to dairy goats and rabbits.",
                                "**Tough Dry Maize Stover**: Coarse and fibrous -> Chop with panga and mix with cow dung in the compost pit.",
                                "**Clean Dry Wheat Straw**: Absorbent -> Use as clean bedding material on the poultry coop floor.",
                                "**Result**: 100% of harvest biomass is productively utilized with zero waste!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Crop Residues",
                        "content": {
                            "question": "Why is burning crop residues strongly discouraged in integrated farming?",
                            "options": [
                                "It makes the soil too moist and wet for planting.",
                                "It destroys vital organic carbon, nitrogen, and soil organisms while causing air pollution.",
                                "It causes crop seeds to germinate too rapidly.",
                                "It attracts dangerous predators to the farm compound."
                            ],
                            "answer": "B",
                            "explanation": "Burning crop residues releases precious carbon and nitrogen into the air as smoke and kills beneficial soil microbes. Composting residues preserves these nutrients and returns them to the soil."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Crops provide human food, livestock forage, and **organic soil biomass**.\n- Crop residues include **maize stover, wheat straw, and legume vines**.\n- The 4 recycling steps are **Collection -> Chipping -> Heaping -> Nutrient Return**.\n- Composting crop biomass restores humus, nitrogen, and water retention capacity."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we know how crops produce biomass, what happens when we feed these residues to farm animals? In the next lesson, we explore livestock integration and how animals convert feed into rich farmyard manure."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: System Components: Livestock Integration and Manure Recycling
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "System Components: Livestock Integration and Manure Recycling",
            "unit_description": "Livestock role, farmyard manure vs chemical fertilizers, pathogen elimination during composting, and elevated pens for sanitary manure collection.",
            "lesson_title": "System Components: Livestock Integration and Manure Recycling",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Natural Nutrient Factories: Dairy Livestock",
                        "content": {
                            "title": "Natural Nutrient Factories: Dairy Livestock",
                            "caption": "Dairy cows feeding on forage in a clean barn with bedding straw capturing manure for composting."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Livestock & Manure Systems",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain the role of livestock as natural nutrient processors.",
                                "Differentiate between **compost manure, animal manure, and green manure**.",
                                "Describe how composting animal waste destroys **pathogens and weed seeds**.",
                                "Compare the soil-building benefits of organic manure versus synthetic fertilizers."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Animals as Nutrient Converters",
                        "content": {
                            "title": "The Power of Livestock",
                            "text": "Farm animals (cows, goats, sheep, pigs) act as natural nutrient factories! They eat bulky grasses, crop residues, and forage, digest them, and concentrate the nutrients into nitrogen-rich dung and urine."
                        }
                    }
                ],
                # Page 2: Preparing Safe Farmyard Manure
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Composting Raw Dung is Essential",
                        "content": {
                            "title": "The High-Heat Safety Barrier",
                            "text": "Raw animal dung should never be applied directly to young crop plants:\n\n- **Pathogens**: Fresh dung contains bacteria and parasites that can contaminate vegetables.\n- **Weed Seeds**: Undigested weed seeds in fresh manure will sprout and infest crop beds.\n- **Heat of Composting**: Piling dung with bedding straw generates microbial temperatures above 60°C. This intense biological heat **kills pathogens and destroys weed seeds**, making the manure completely safe!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Classification of Organic Manures",
                        "content": {
                            "title": "Types of Organic Manures & Applications",
                            "headers": ["Manure Category", "Raw Materials Used", "Preparation Method", "Primary Soil Benefit"],
                            "rows": [
                                ["Farmyard / Animal Manure", "Dung and urine from cattle, goats, or sheep mixed with bedding", "Piled and composted for 2 to 3 months to kill pathogens", "Highly rich in nitrogen, phosphorus, and potassium"],
                                ["Compost Manure", "Kitchen scraps, garden weedings, and dry crop residues", "Layered in a compost heap or pit and turned regularly", "Adds rich dark humus and improves soil structure"],
                                ["Green Manure", "Young leguminous crops (desmodium, beans, sweet potato vines)", "Grown and plowed directly into moist soil before flowering", "Restores lost nitrogen and feeds active soil microbes"]
                            ]
                        }
                    }
                ],
                # Page 3: Manure vs. Synthetic Fertilizer Architecture
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Organic Manure vs. Synthetic Chemical Fertilizer",
                        "content": {
                            "title": "Organic Manure vs. Synthetic Chemical Fertilizer",
                            "caption": "Comparison diagram contrasting how organic manure builds long-term humus and water retention while chemical fertilizers leach away."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Long-Term Soil Structure Benefits",
                        "content": {
                            "title": "Building Living Soil",
                            "text": "- **Moisture Holding**: Organic manure acts like a sponge, holding soil water during dry periods.\n- **Biological Life**: Feeds earthworms and beneficial bacteria that aerate the root zone.\n- **Zero Leaching**: Nutrients bind to organic humus, preventing them from washing away in heavy rains."
                        }
                    }
                ],
                # Page 4: Sanitary Engineering: Elevated Slatted Pens
                [
                    {
                        "type": "worked_example",
                        "title": "Sanitary Engineering: Elevated Slatted Pens",
                        "content": {
                            "intro": "Why modern integrated farms use raised wooden pens for goats and sheep:",
                            "steps": [
                                "**Design Feature**: Wooden floor with 1.5cm gaps (slats) raised 1 meter above ground.",
                                "**Hygiene Benefit**: Dung and urine fall through the slats immediately, keeping animals dry and disease-free.",
                                "**Collection Efficiency**: The farmer easily sweeps up the accumulated manure beneath the pen for composting.",
                                "**Result**: Maximum animal health and effortless fertilizer harvesting!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Composting Manure",
                        "content": {
                            "question": "Why is it essential to compost raw animal dung before applying it to vegetable crop beds?",
                            "options": [
                                "To turn the animal dung into synthetic chemicals.",
                                "The biological heat generated during composting kills harmful disease pathogens and weed seeds.",
                                "To remove all nitrogen and phosphorus from the manure.",
                                "To prevent the dung from attracting any earthworms."
                            ],
                            "answer": "B",
                            "explanation": "Raw animal waste contains disease-causing pathogens and undigested weed seeds. Composting generates high microbial temperatures (above 60°C) that destroy these harmful organisms, making the manure safe for food crops."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Livestock act as **natural nutrient converters**, turning bulky grass into concentrated manure.\n- **Farmyard manure** must be composted to eliminate pathogens and weed seeds.\n- **Organic manure** improves soil water-holding capacity and structure, outperforming synthetic inputs.\n- **Elevated slatted pens** optimize animal hygiene and simplify manure harvesting."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have integrated crops and land animals. But what happens when we add aquatic life? In the next lesson, we explore aquaculture (fish farming) and how fish waste creates a powerful liquid fertilizer loop!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: System Components: Aquaculture (Fish Farming) and Water Nutrient Loops
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "System Components: Aquaculture (Fish Farming) and Water Nutrient Loops",
            "unit_description": "Aquaculture definition, earthen fish ponds, dissolved nitrogen liquid fertilizer, the 3-way poultry-fish-crop loop, and managing eutrophication.",
            "lesson_title": "System Components: Aquaculture (Fish Farming) and Water Nutrient Loops",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Aquatic Integration: The Earthen Fish Pond",
                        "content": {
                            "title": "Aquatic Integration: The Earthen Fish Pond",
                            "caption": "A smallholder earthen fish pond stocked with tilapia, situated adjacent to organic vegetable crop beds."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Aquaculture Integration",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **aquaculture** and its role in integrated farming.",
                                "Explain how fish waste enriches pond water into **dissolved natural liquid fertilizer**.",
                                "Trace the **3-way Poultry-Aquaculture-Crop integration loop**.",
                                "Identify the dangers of **eutrophication (excess nutrients)** and how to prevent fish suffocation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Aquaculture?",
                        "content": {
                            "title": "Farming in Water",
                            "text": "**Aquaculture** is the practice of breeding and rearing fish (such as tilapia or catfish) in constructed ponds or tanks. In an integrated farm, the fish pond serves as both a source of high-protein food and a reservoir of nutrient-rich irrigation water!"
                        }
                    }
                ],
                # Page 2: The Fish-to-Crop Nutrient Flow
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pond Water as Liquid Fertilizer",
                        "content": {
                            "title": "Natural Liquid Nitrogen",
                            "text": "- **Fish Excretion**: As fish grow, they excrete waste containing dissolved ammonia, nitrogen, and phosphorus directly into the pond water.\n- **Instant Absorption**: When pond water is drained or pumped to irrigate nearby vegetables, plants absorb these pre-dissolved nutrients instantly through their roots.\n- **Water Savings**: Water serves two purposes before evaporating—first rearing fish, then irrigating crops!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "3-Way Poultry-Aquaculture-Crop Water & Nutrient Loop",
                        "content": {
                            "title": "3-Way Poultry-Aquaculture-Crop Water & Nutrient Loop",
                            "caption": "Diagram showing chickens feeding plankton in fish pond, fish pond water irrigating vegetables, and vegetable scraps feeding chickens."
                        }
                    }
                ],
                # Page 3: The 3-Way Poultry-Fish-Crop System
                [
                    {
                        "type": "step_process",
                        "title": "The Tripartite Integration Loop",
                        "content": {
                            "title": "3-Way Synergistic Resource Flow",
                            "steps": [
                                "**1. Poultry to Fish**: Chicken coops are built on stilts over or next to the pond. Droppings fertilize microscopic water plants called **plankton**, providing free fish food.",
                                "**2. Fish to Crops**: Nutrient-rich pond water is drained through gravity channels to irrigate adjacent vegetable plots.",
                                "**3. Crops to Poultry**: Outer kale leaves, damaged tomatoes, and weed trimmings are fed back to the chickens!"
                            ]
                        }
                    },
                    {
                        "type": "common_mistake",
                        "title": "Critical Water Quality Hazard",
                        "content": {
                            "text": "**Eutrophication & Oxygen Depletion**: Dropping too much poultry manure into a fish pond causes rapid algal blooms. When algae die and rot, they consume all dissolved oxygen in the water, causing the fish to suffocate at the surface! Always balance bird numbers with pond volume."
                        }
                    }
                ],
                # Page 4: Scientific Case Study: Irrigation Comparison
                [
                    {
                        "type": "worked_example",
                        "title": "Irrigation Experiment: Tap Water vs. Fish Pond Water",
                        "content": {
                            "intro": "Farmer Juma splits a kale bed into two equal sections under identical sunlight and soil conditions:",
                            "steps": [
                                "**Bed A (Tap Water)**: Watered daily with clean tap water. Kales grow moderately with light green leaves.",
                                "**Bed B (Fish Pond Water)**: Watered daily with nutrient-rich tilapia pond water.",
                                "**Observation after 3 Weeks**: Bed B kales grow 40% larger with thick, glossy, deep dark-green leaves.",
                                "**Conclusion**: Pre-dissolved fish waste acts as a premium organic liquid fertilizer, accelerating crop growth at zero cost!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Aquaculture Benefits",
                        "content": {
                            "question": "How does aquaculture (fish farming) water directly benefit vegetable production on an integrated farm?",
                            "options": [
                                "The water is salty and kills all weeds automatically.",
                                "Fish waste enriches the water with dissolved nitrogen and minerals, serving as a natural liquid fertilizer.",
                                "The water stops rain from reaching the crop roots.",
                                "Fish jump out of the water to eat caterpillars on crop leaves."
                            ],
                            "answer": "B",
                            "explanation": "Fish excrete organic waste into pond water. Draining or pumping this water to irrigate crops delivers pre-dissolved organic nitrogen and minerals directly to plant roots, stimulating rapid growth."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Aquaculture** provides family protein and rich liquid fertilizer.\n- Pond water is enriched with **dissolved nitrogen and phosphorus** from fish waste.\n- The **Poultry-Fish-Crop loop** exchanges plankton feed, irrigation water, and green scraps.\n- Ponds must be managed carefully to avoid **eutrophication and oxygen depletion**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered crops, animals, and aquatic systems. But what protects our farm from harsh winds and hillside erosion? In the next lesson, we explore agroforestry and the microclimate benefits of trees!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: System Components: Agroforestry, Soil Erosion, and Microclimate Benefits
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "System Components: Agroforestry, Soil Erosion, and Microclimate Benefits",
            "unit_description": "Agroforestry definition, soil conservation on contour terraces, deep-root nutrient pumping, and tree microclimate regulation.",
            "lesson_title": "System Components: Agroforestry, Soil Erosion, and Microclimate Benefits",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Protective Canopies: Agroforestry Systems",
                        "content": {
                            "title": "Protective Canopies: Agroforestry Systems",
                            "caption": "Multi-purpose agroforestry trees planted along contour terraces on a sloping farm, protecting crops from wind and soil erosion."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Agroforestry & Microclimates",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **agroforestry** as the combination of trees, crops, and livestock.",
                                "Explain how tree roots and canopies prevent **soil erosion and runoff**.",
                                "Describe how trees act as **deep nutrient pumps** via leaf drop.",
                                "Analyze how tree windbreaks create a protective **cooling microclimate**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Agroforestry?",
                        "content": {
                            "title": "The Triple Integration",
                            "text": "**Agroforestry** is a land-use system that deliberately integrates trees and woody shrubs with agricultural crops and livestock on the same land unit.\n\n- **Agronomy**: Crop cultivation.\n- **Forestry**: Planting multi-purpose woody perennial trees.\n- **Pastoralism**: Grazing animals and poultry beneath the tree canopy."
                        }
                    }
                ],
                # Page 2: Preventing Soil Erosion & Nutrient Runoff
                [
                    {
                        "type": "concept_explanation",
                        "title": "How Trees Anchor and Protect the Soil",
                        "content": {
                            "title": "3 Defensive Layers Against Storms",
                            "text": "- **1. Canopy Cushion**: Leaves and branches intercept falling raindrops, breaking their physical force so water drips gently onto the soil.\n- **2. Root Anchoring Net**: Deep and spreading root systems bind loose soil particles together, physically preventing heavy runoff from carving erosion gullies.\n- **3. Living Contour Barriers**: Planting nitrogen-fixing trees (like calliandra or leucaena) in dense rows along contour terraces traps eroding soil and creates natural terraces over time."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Agroforestry Soil Erosion Prevention & Microclimate Blueprint",
                        "content": {
                            "title": "Agroforestry Soil Erosion Prevention & Microclimate Blueprint",
                            "caption": "Diagram illustrating tree canopy rain interception, root soil binding on terraces, leaf mulch nutrient return, and windbreak cooling."
                        }
                    }
                ],
                # Page 3: Microclimates & Deep Nutrient Pumping
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Farm with Trees vs. Deforested Bare Farm",
                        "content": {
                            "title": "Agroforestry Impact Matrix",
                            "headers": ["Environmental Factor", "Farm with Agroforestry Trees", "Deforested Bare Farm"],
                            "rows": [
                                ["Rainfall Impact", "Canopy breaks velocity; water absorbs gently into soil", "Violent raindrops compact surface, triggering flash runoff"],
                                ["Topsoil Retention", "Deep root net binds soil; zero erosion gullies", "Topsoil washes away, stripping away fertilizers and seeds"],
                                ["Soil Moisture", "Tree shade reduces evaporation; crop roots stay moist and cool", "Hot direct sun dries out topsoil rapidly, wilting crops"],
                                ["Nutrient Cycling", "Deep roots pump minerals to leaves, returning nutrients via mulch", "Nutrients are permanently leached deep beyond crop reach"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example: Sloping Hillside Strategy
                [
                    {
                        "type": "worked_example",
                        "title": "Sloping Hillside Strategy: Contour Hedgerows",
                        "content": {
                            "intro": "Farmer Maina owns a steep hillside farm where heavy rains regularly wash away his bean crops:",
                            "steps": [
                                "**Problem**: High water velocity on bare slope strips topsoil and causes severe erosion.",
                                "**Agroforestry Solution**: Maina plants dense rows of **Calliandra** trees along the natural contour lines of the slope.",
                                "**Multi-Benefit 1**: The tree roots anchor the slope and trap sediment, forming flat, stable terraces.",
                                "**Multi-Benefit 2**: Calliandra is a legume that fixes nitrogen, fertilizing his beans naturally.",
                                "**Multi-Benefit 3**: Pruned tree branches provide high-protein leafy fodder for his dairy goats!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Agroforestry Functions",
                        "content": {
                            "question": "How do agroforestry trees directly help nearby vegetable crops during hot, windy dry seasons?",
                            "options": [
                                "They pump water out of crop roots into the air.",
                                "Their shade and windbreak barriers reduce soil moisture evaporation and keep crop roots cool.",
                                "They prevent any rain from reaching the soil surface.",
                                "They attract strong winds to blow away dust from crop leaves."
                            ],
                            "answer": "B",
                            "explanation": "Trees create a beneficial microclimate by blocking hot, drying winds and providing partial shade. This dramatically lowers evaporation rates, allowing crop roots to retain moisture during dry periods."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Agroforestry** combines trees, crops, and livestock for mutual ecological resilience.\n- Tree roots form an **underground anchor net** that prevents soil erosion and nutrient runoff.\n- Deep roots act as **nutrient pumps**, returning subsoil minerals via fallen leaf mulch.\n- Trees create a **cool microclimate**, acting as windbreaks and conserving soil moisture."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What about small-scale livestock for compact farm compounds? In the next lesson, we look at rabbit keeping and poultry rearing, and how their concentrated manure powers smallholder farms!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: System Components: Small-Scale Animal Keeping (Rabbit and Poultry)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "System Components: Small-Scale Animal Keeping (Rabbit and Poultry)",
            "unit_description": "Rabbit and poultry rearing on small plots, high-nitrogen poultry litter, phosphorus-rich rabbit manure, rabbit urine harvesting, and biological pest control.",
            "lesson_title": "System Components: Small-Scale Animal Keeping (Rabbit and Poultry)",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Compact Powerhouses: Backyard Poultry & Rabbits",
                        "content": {
                            "title": "Compact Powerhouses: Backyard Poultry & Rabbits",
                            "caption": "A raised wooden rabbit hutch with free-range chickens scratching for insects and weeds in the yard below."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Small Animal Enterprises",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain why poultry and rabbits are ideal for small farms with limited land.",
                                "Describe the unique nutritional qualities of **poultry manure and rabbit droppings**.",
                                "Explain how scratching poultry perform **biological weed and pest control**.",
                                "Understand the harvesting of **rabbit urine** as a valuable liquid resource."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Small-Scale Animals?",
                        "content": {
                            "title": "High Yield in Small Spaces",
                            "text": "Rabbits and poultry require very little land, reproduce rapidly, and convert kitchen scraps and garden weeds into high-value meat, eggs, and exceptionally concentrated organic fertilizers!"
                        }
                    }
                ],
                # Page 2: Poultry Contributions: Manure & Biological Pest Control
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Poultry Component",
                        "content": {
                            "title": "Chickens as Garden Workers",
                            "text": "- **Nitrogen-Rich Manure**: Poultry litter has one of the highest nitrogen concentrations among farm manures, supercharging leafy crop growth.\n- **Biological Pest Control**: Free-range chickens actively hunt caterpillars, beetles, cutworms, and grasshoppers, suppressing pests without toxic chemical sprays.\n- **Mechanical Weeding**: Scratching chickens uproot weed seedlings and aerate the topsoil naturally."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Poultry & Rabbit Output-to-Input Resource Conversion Matrix",
                        "content": {
                            "title": "Poultry & Rabbit Output-to-Input Resource Conversion Matrix",
                            "caption": "Diagram displaying how poultry litter, rabbit droppings, and rabbit urine convert into solid fertilizers, liquid foliar feeds, and biological pest control."
                        }
                    }
                ],
                # Page 3: Rabbit Contributions: Manure & Liquid Foliar Feed
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Poultry vs. Rabbit Contributions",
                        "content": {
                            "title": "Small Animal Resource Profiles",
                            "headers": ["Enterprise Characteristic", "Poultry Rearing (Chickens / Ducks)", "Rabbit Keeping"],
                            "rows": [
                                ["Food Products", "Eggs and high-protein meat", "Lean, low-cholesterol meat"],
                                ["Manure Quality", "Very high nitrogen (hot manure, requires full composting)", "High phosphorus and nitrogen (cold manure, fast application)"],
                                ["Special Byproduct", "Poultry litter can be steeped to make compost tea", "Urine collected via gutters to make organic foliar spray"],
                                ["Space & Housing", "Small coop or free-range run in the yard", "Elevated wooden hutches with wire mesh slatted floors"]
                            ]
                        }
                    }
                ],
                # Page 4: Practical Design: The Elevated Gutter Hutch
                [
                    {
                        "type": "worked_example",
                        "title": "Engineering Design: The Dual-Harvest Rabbit Hutch",
                        "content": {
                            "intro": "How to design a rabbit hutch that collects both solid droppings and liquid urine simultaneously:",
                            "steps": [
                                "**Step 1 (Slatted Mesh Floor)**: Wire mesh allows solid pellets and liquid urine to drop through freely.",
                                "**Step 2 (Sloped Collection Sheet)**: A sloped plastic or iron sheet beneath the hutch catches the waste.",
                                "**Step 3 (Separation Mesh)**: Solid pellets roll into a collection bucket for solid composting.",
                                "**Step 4 (Gutter & Bottle)**: Liquid urine drains down the slope through a funnel into a clean storage bottle.",
                                "**Outcome**: Effortless daily collection of pure rabbit urine and dry droppings!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Poultry Pest Control",
                        "content": {
                            "question": "How do free-range chickens in a post-harvest garden directly help reduce crop production expenses for the farmer?",
                            "options": [
                                "They manufacture synthetic chemical sprays.",
                                "They eat destructive insects and uproot weed seedlings, providing free biological pest and weed control.",
                                "They automatically plant seeds while scratching.",
                                "They harvest ripe vegetables with their beaks."
                            ],
                            "answer": "B",
                            "explanation": "Scratching poultry hunt destructive crop pests (caterpillars, beetles) and uproot weed seedlings, acting as natural pest and weed controllers that eliminate the need for expensive agrochemicals."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Poultry and rabbits** fit smallholder farms due to low land and feed needs.\n- **Poultry litter** delivers concentrated nitrogen and natural pest suppression.\n- **Rabbit droppings** provide rich phosphorus, while **rabbit urine** yields organic foliar feed.\n- Dual-harvest hutches collect solid manure and liquid urine separately for maximum efficiency."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do vegetable crops consume these recycled animal nutrients and feed the household? In the next lesson, we explore vegetable production and intercropping synergies on an integrated farm!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: System Components: Vegetable Production on an Integrated Farm
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "System Components: Vegetable Production on an Integrated Farm",
            "unit_description": "Vegetable crops (kales, spinach, beans, tomatoes), intercropping legumes for nitrogen fixation, living mulch canopy, and recycling vegetable trimmings.",
            "lesson_title": "System Components: Vegetable Production on an Integrated Farm",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Nutritious Abundance: The Integrated Kitchen Garden",
                        "content": {
                            "title": "Nutritious Abundance: The Integrated Kitchen Garden",
                            "caption": "Vibrant beds of kales (sukuma wiki), spinach, and climbing beans flourishing with organic farmyard manure."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Vegetable Integration",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Identify suitable vegetables for integrated farming: **kales, spinach, beans, peas, tomatoes**.",
                                "Explain how **intercropping legumes** fixes natural nitrogen into the soil.",
                                "Describe how dense crop canopies conserve **soil moisture and suppress weeds**.",
                                "Sort vegetable byproducts into **animal feed vs. compost manure** pathways."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Role of Vegetables",
                        "content": {
                            "title": "Feeding the Family and the Farm",
                            "text": "Vegetable production (horticulture) is the central consumer of recycled farm nutrients. Fast-maturing crops like kales, spinach, beans, and tomatoes utilize animal manure and fish pond water to provide year-round family nutrition and cash income!"
                        }
                    }
                ],
                # Page 2: Legume Synergies & Soil Conservation
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Legume Advantage: Biological Nitrogen Fixation",
                        "content": {
                            "title": "Natural Soil Fertilizer Factories",
                            "text": "- **Root Nodules**: Leguminous crops (beans, peas, cowpeas) host specialized *Rhizobium* bacteria in their root nodules.\n- **Nitrogen Fixation**: These bacteria pull nitrogen gas from the air and convert it into soluble nitrates in the soil.\n- **Intercropping Synergy**: Planting beans alongside leafy kales (sukuma wiki) provides free nitrogen to the kales, boosting leaf size without chemical fertilizer!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Horticultural Intercropping & Natural Nitrogen Fixation Map",
                        "content": {
                            "title": "Horticultural Intercropping & Natural Nitrogen Fixation Map",
                            "caption": "Diagram showing root nitrogen fixation by climbing beans fertilizing neighboring kale plants, with leafy canopies shading soil."
                        }
                    }
                ],
                # Page 3: The Vegetable Byproduct Recycling Pathway
                [
                    {
                        "type": "comparison_table",
                        "title": "Sorting Vegetable Byproducts: Feed vs. Compost",
                        "content": {
                            "title": "Vegetable Waste Allocation Matrix",
                            "headers": ["Vegetable Leftover Item", "Physical Condition", "Correct Recycling Destination", "Safety & Biological Rationale"],
                            "rows": [
                                ["Outer Kale Leaves & Cabbage Trimmings", "Clean, green, crisp", "Recycled as Animal Feed (Rabbits / Poultry / Goats)", "Provides fresh vitamins, moisture, and fiber safely"],
                                ["Bean Vines & Pea Pods", "Green, healthy foliage", "Recycled as Animal Feed (High-Protein Fodder)", "Rich in plant protein that boosts goat milk and rabbit growth"],
                                ["Rotten, Moldy Tomatoes", "Spoiled with fungal rot", "Recycled to Compost Heap ONLY", "Prevents sickening animals; high heat of compost destroys spores"],
                                ["Weeds Cleared from Garden Paths", "Fibrous root systems", "Recycled to Compost Heap ONLY", "Decomposes into dark organic humus without infesting beds"]
                            ]
                        }
                    }
                ],
                # Page 4: Worked Example: Designing an Intercropped Bed
                [
                    {
                        "type": "worked_example",
                        "title": "Practical Bed Design: Kale and Bean Intercropping",
                        "content": {
                            "intro": "How to arrange an organic vegetable bed for maximum resource efficiency:",
                            "steps": [
                                "**Bed Preparation**: Dig a 1m x 5m raised bed; mix in 2 wheelbarrows of decomposed farmyard manure.",
                                "**Alternating Rows**: Plant 1 row of kales (sukuma wiki), followed by 1 row of climbing beans.",
                                "**Mulching**: Cover bare soil between rows with dry grass mulch to trap moisture.",
                                "**Outcome**: Beans feed nitrogen to kales, kale leaves shade the ground, and mulch blocks weed growth!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Legume Intercropping",
                        "content": {
                            "question": "Why is planting leguminous crops (like beans or peas) alongside leafy vegetables like kales highly recommended?",
                            "options": [
                                "Beans absorb all soil water so the kales don't drown.",
                                "Legumes naturally fix atmospheric nitrogen in the soil, which fertilizes neighboring kales.",
                                "Beans scare away all birds from the garden.",
                                "Kales use bean leaves to climb up toward the sun."
                            ],
                            "answer": "B",
                            "explanation": "Legumes possess root nodules with nitrogen-fixing bacteria that convert atmospheric nitrogen into nitrates, enriching the soil and fertilizing nearby heavy-feeding leafy vegetables naturally."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Kales, spinach, beans, peas, and tomatoes** form the core of integrated kitchen gardens.\n- **Legumes fix atmospheric nitrogen**, fertilizing companion leafy vegetables for free.\n- Dense crop canopies act as **living mulch**, conserving water and suppressing weeds.\n- Clean green trimmings feed animals, while **moldy/diseased scraps go to the compost heap**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do vegetables, rabbits, and poultry interact in a direct 3-way triangular loop? In the next lesson, we map these multi-way flows and learn how to dilute rabbit urine into foliar feed!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Relational Benefits of Vegetable Production, Poultry, and Rabbit Keeping
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Relational Benefits of Vegetable Production, Poultry, and Rabbit Keeping",
            "unit_description": "Triangular relational network (vegetables-poultry-rabbits), rabbit urine foliar feed dilution (1:5 ratio), and circular nitrogen tracing.",
            "lesson_title": "Relational Benefits of Vegetable Production, Poultry, and Rabbit Keeping",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Integrated Backyard Triad",
                        "content": {
                            "title": "The Integrated Backyard Triad",
                            "caption": "An elevated rabbit hutch with urine collection gutters, with chickens scratching below and vegetable plots nearby."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Tripartite Network",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Map the multi-directional resource flows between **vegetables, poultry, and rabbits**.",
                                "Master the exact **1:5 dilution ratio** for preparing rabbit urine foliar feed.",
                                "Explain how diluted rabbit urine acts as both a **leaf fertilizer and pest repellent**.",
                                "Trace a complete circular loop of nitrogen through all three enterprises."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Ultimate Smallholder Triad",
                        "content": {
                            "title": "Three Enterprises, Zero Waste",
                            "text": "Vegetable plots, poultry coops, and rabbit hutches form the most efficient small-scale farming triad in the world. Each component relies directly on the other two to survive and thrive!"
                        }
                    }
                ],
                # Page 2: The Triangular Resource Exchange Network
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Triangular Nitrogen & Feed Exchange Network (Veg-Poultry-Rabbit)",
                        "content": {
                            "title": "Triangular Nitrogen & Feed Exchange Network (Veg-Poultry-Rabbit)",
                            "caption": "Equilateral triangle schematic showing multi-directional flows: vegetable scraps feed animals, poultry litter and rabbit manure fertilize soil, urine sprays foliage, and chickens eat pests."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Multi-Way Synergistic Connections",
                        "content": {
                            "title": "How the Triad Connects",
                            "text": "- **Vegetables -> Animals**: Kale leaves, sweet potato vines, and pea pods provide high-vitamin fodder for rabbits and chickens.\n- **Poultry -> Vegetables**: Chickens produce nitrogen-rich solid manure, scratch up weed seeds, and eat leaf caterpillars.\n- **Rabbits -> Vegetables**: Rabbits supply phosphorus-rich solid manure and concentrated liquid urine for foliar spray.\n- **Rabbits -> Poultry**: Chickens scratch beneath raised rabbit hutches, eating spilled grain and fly larvae to keep the yard sanitary."
                        }
                    }
                ],
                # Page 3: Harvesting & Diluting Liquid Gold (Rabbit Urine)
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Rabbit Urine Foliar Feed",
                        "content": {
                            "title": "The 1:5 Dilution Protocol",
                            "steps": [
                                "**1. Collection**: Channel urine from sloped hutch gutters into clean plastic containers.",
                                "**2. The Danger of Pure Urine**: Undiluted rabbit urine is highly concentrated in nitrogen and will burn crop leaves chemically if applied raw!",
                                "**3. The Golden 1:5 Ratio**: Mix **1 liter of pure rabbit urine with 5 liters of clean water** (e.g. 2L urine + 10L water = 12L foliar feed).",
                                "**4. Cool-Hours Application**: Spray the diluted liquid onto crop leaves early in the morning or late in the evening. It feeds leaves instantly and repels aphids with its strong odor."
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Golden Dilution Formula",
                        "content": {
                            "title": "Remember: 1 Part Urine to 5 Parts Water!",
                            "text": "Formula: Water Needed = Urine Volume × 5. For 3 liters of urine, add 15 liters of water to produce 18 liters of safe organic foliar spray!"
                        }
                    }
                ],
                # Page 4: Tracing the Nitrogen Journey
                [
                    {
                        "type": "worked_example",
                        "title": "Tracing a Nitrogen Molecule Through the Triad",
                        "content": {
                            "intro": "Follow one molecule of nitrogen through this self-sustaining system:",
                            "steps": [
                                "**1. The Bean Plant**: A climbing bean plant pulls nitrogen gas from the air into its leaves.",
                                "**2. The Rabbit**: Farmer feeds bean leaves to the rabbit; the rabbit digests it and excretes nitrogen in urine.",
                                "**3. The Foliar Spray**: Farmer dilutes the urine 1:5 and sprays it on young kale leaves.",
                                "**4. The Kale Growth**: The kale absorbs the nitrogen, growing huge and deep green.",
                                "**5. The Harvest**: The family harvests the kale for dinner, completing the nutrient loop!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Rabbit Urine Dilution",
                        "content": {
                            "question": "Farmer Mary collects 3 liters of pure, concentrated rabbit urine from her hutches. To safely spray this on her spinach as organic foliar feed without burning the leaves, how much water must she add?",
                            "options": [
                                "3 liters of water (1:1 ratio)",
                                "15 liters of water (1:5 ratio)",
                                "150 liters of water (1:50 ratio)",
                                "No water; rabbit urine must always be sprayed pure."
                            ],
                            "answer": "B",
                            "explanation": "Pure rabbit urine has high nitrogen concentration that will scorch crop leaves if applied raw. It must be diluted with water at a 1:5 ratio (3 liters of urine × 5 = 15 liters of water)."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Vegetables, poultry, and rabbits form a **closed-loop backyard triad**.\n- Rabbit droppings supply phosphorus, while poultry litter provides concentrated nitrogen.\n- **Rabbit urine must be diluted 1:5 with water** to prevent burning crop foliage.\n- Diluted rabbit urine acts as both a **rapid foliar fertilizer and natural pest repellent**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we manage water harvesting and farm-wide organic wastes systematically? In the next lesson, we examine farm-wide water harvesting, drip irrigation, and integrated composting systems!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Organic Waste and Water Management Systems
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Organic Waste and Water Management Systems",
            "unit_description": "Rainwater harvesting from rooftops, water storage tanks, gravity drip irrigation pipelines, diverse waste composting, and moisture synergy.",
            "lesson_title": "Organic Waste and Water Management Systems",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Smart Conservation: Rainwater Harvesting & Drip Systems",
                        "content": {
                            "title": "Smart Conservation: Rainwater Harvesting & Drip Systems",
                            "caption": "A large rainwater harvesting tank capturing roof runoff and feeding gravity drip irrigation lines across vegetable beds."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Water & Waste Infrastructure",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Explain how **rainwater harvesting and drip irrigation** prevent water wastage.",
                                "Describe how dung, crop residues, and kitchen waste are systematically composted.",
                                "Analyze how organic compost and drip irrigation create a **moisture synergy**.",
                                "Trace the water flow from rooftop gutters to fish ponds and crop roots."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Lifeblood of the Farm",
                        "content": {
                            "title": "Water and Waste Harmony",
                            "text": "Water is a precious and scarce resource. On an integrated farm, every drop of rainwater is caught from rooftops, stored in tanks, shared with fish ponds, and delivered directly to crop roots through water-saving drip lines!"
                        }
                    }
                ],
                # Page 2: Systematic Water Management Pipeline
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Systematic Farm-Wide Water Harvesting & Drip Pipeline Flow",
                        "content": {
                            "title": "Systematic Farm-Wide Water Harvesting & Drip Pipeline Flow",
                            "caption": "Pipeline schematic showing rooftop gutters channeling rain into storage tanks, overflow replenishing fish ponds, and drip pipes delivering water to crop roots."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The Integrated Water Journey",
                        "content": {
                            "title": "From Cloud to Root Zone",
                            "steps": [
                                "**1. Rooftop Harvesting**: Gutters along house and barn roofs collect clean rainwater and channel it into a large storage tank.",
                                "**2. Fish Pond Replenishment**: Tank overflow replaces evaporated water in the tilapia pond.",
                                "**3. Nutrient Enrichment**: Fish excrete waste, turning the pond water into rich liquid fertilizer.",
                                "**4. Drip Irrigation**: Water flows through small plastic tubes, dripping slowly onto crop roots with zero evaporation waste!"
                            ]
                        }
                    }
                ],
                # Page 3: Systematic Organic Waste Management
                [
                    {
                        "type": "concept_explanation",
                        "title": "Centralized Farm Composting",
                        "content": {
                            "title": "Turning All Wastes into Humus",
                            "text": "Instead of burning or dumping scraps, all biological farm waste is centrally managed in a compost heap or pit:\n\n- **Nitrogen Green Layer**: Fresh animal dung, green crop trimmings, and kitchen peelings.\n- **Carbon Brown Layer**: Dry chopped maize stover, wheat straw, and dry grass.\n- **Regular Turning**: Aerating the pile with a garden fork introduces oxygen, accelerating decomposition into black, sweet-smelling humus in 6 to 8 weeks!"
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Water-Waste Synergy",
                        "content": {
                            "title": "Compost Holds Drip Water Like a Sponge!",
                            "text": "Soil enriched with compost holds 3 times more water than depleted sandy soil. Combining compost manure with drip irrigation means crops stay hydrated using 70% less water!"
                        }
                    }
                ],
                # Page 4: Worked Example: Drought-Proofing a Small Farm
                [
                    {
                        "type": "worked_example",
                        "title": "Farm Design: Drought-Proofing with Integrated Systems",
                        "content": {
                            "intro": "How Farmer Kiprop survived a 3-month dry spell with zero crop loss:",
                            "steps": [
                                "**Step 1 (Water Storage)**: Captured 10,000 liters of rainwater from his metal roof during the rainy season.",
                                "**Step 2 (Drip Lines)**: Installed low-cost gravity drip hoses across his 1/4-acre tomato plot.",
                                "**Step 3 (Heavy Compost Mulch)**: Applied a 5cm layer of compost manure and dry grass mulch around plant stems.",
                                "**Outcome**: Kiprop harvested 50 crates of premium tomatoes during the dry spell when market prices were at their peak!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Water Flow Sequencing",
                        "content": {
                            "question": "What is the most efficient chronological water flow on an integrated farm to maximize resource conservation?",
                            "options": [
                                "Rainwater falls on bare soil -> flows down road as runoff -> pumped into house.",
                                "Rooftop gutters collect rainwater -> storage tank -> fish pond -> drip irrigation to crop roots.",
                                "Pond water is poured onto the roof -> flows into tap -> dumped on the ground.",
                                "Tap water is used to wash cattle -> dumped in a river -> rain falls."
                            ],
                            "answer": "B",
                            "explanation": "Harvesting rainwater from roofs into storage tanks, using it to replenish fish ponds, and then directing the nutrient-rich pond water through drip irrigation pipes represents the gold standard of circular water management."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Rainwater harvesting** captures precious roof water for dry-season resilience.\n- **Drip irrigation** delivers water directly to crop roots with near-zero evaporation loss.\n- Centralized **composting layers green nitrogen wastes with brown carbon stalks**.\n- Composted soil retains moisture, multiplying the efficiency of drip irrigation."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we fit all these components onto a physical plot of land? In the next lesson, we begin our first practical activity: designing an integrated farm layout on Manila paper!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Practical Activity: Designing an Integrated Farm Layout on Manila Paper
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Practical Activity: Designing an Integrated Farm Layout on Manila Paper",
            "unit_description": "2D farm spatial planning on Manila paper, spatial optimization, grouping connected enterprises, and collaborative design critique.",
            "lesson_title": "Practical Activity: Designing an Integrated Farm Layout on Manila Paper",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Collaborative Design: Sketching on Manila Paper",
                        "content": {
                            "title": "Collaborative Design: Sketching on Manila Paper",
                            "caption": "Students working collaboratively in a classroom, drawing and coloring an integrated farm layout map on large Manila paper."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: 2D Layout Design",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Draw a balanced, scaled 2D integrated farm layout on Manila paper.",
                                "Apply **spatial optimization** to position crops, livestock, ponds, and compost pits strategically.",
                                "Draw dashed arrows tracing nutrient and water flows between enterprises.",
                                "Collaborate in teams to critique and refine farm layouts for maximum labor efficiency."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Spatial Planning",
                        "content": {
                            "title": "Mapping Before Building",
                            "text": "A **farm layout** is a detailed 2D blueprint that plans where every building, animal shed, crop plot, and water channel should sit. Smart spatial design groups connected components close together, saving hours of heavy manual transport labor!"
                        }
                    }
                ],
                # Page 2: Spatial Optimization Rules
                [
                    {
                        "type": "suggested_diagram",
                        "title": "2D Spatial Optimization & Transport Labor Layout",
                        "content": {
                            "title": "2D Spatial Optimization & Transport Labor Layout",
                            "caption": "Spatial layout plan showing compost pit positioned directly between animal sheds and vegetable plots to minimize transport labor."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "4 Golden Rules of Farm Layout Design",
                        "content": {
                            "title": "Strategic Component Placement",
                            "text": "- **1. Compost Pit Placement**: Place the compost pit directly between livestock sheds and crop beds to minimize carrying heavy dung and weedings.\n- **2. Fish Pond at Lower Elevation**: Position the fish pond at a lower point so surface runoff and greywater drain into it easily by gravity.\n- **3. Animal Sheds Near House**: Locate chicken coops and rabbit hutches close to the homestead for security against theft and easy feeding.\n- **4. Agroforestry on Borders**: Plant multi-purpose trees along boundary lines to act as protective windbreaks and living fences."
                        }
                    }
                ],
                # Page 3: Step-by-Step Layout Drawing Activity
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Drawing on Manila Paper",
                        "content": {
                            "title": "Step-by-Step Drawing Protocol",
                            "steps": [
                                "**Step 1 (Boundaries & Orientation)**: Use a ruler to draw rectangular plot boundaries and mark the North compass arrow.",
                                "**Step 2 (Homestead & Access Roads)**: Draw the family house and main entrance driveway near the road.",
                                "**Step 3 (Enterprise Zones)**: Sketch zones for the cow barn, rabbit hutch, chicken coop, fish pond, vegetable garden, and crop field.",
                                "**Step 4 (Resource Flow Arrows)**: Draw colored dashed arrows showing nutrient transfers (e.g. green arrow from rabbit hutch to vegetable beds labeled 'Urine Foliar Spray').",
                                "**Step 5 (Clear Labeling & Key)**: Add neat pencil labels and a color key (blue = water, green = crops/trees, brown = compost/manure)."
                            ]
                        }
                    }
                ],
                # Page 4: Practical Critique Exercise
                [
                    {
                        "type": "worked_example",
                        "title": "Design Diagnosis: Spotting Spatial Bottlenecks",
                        "content": {
                            "intro": "A student team reviews a peer's layout drawing:",
                            "steps": [
                                "**Flaw Identified**: The compost pit is drawn at the far top corner of the farm, 150 meters uphill from the cattle barn and vegetable beds.",
                                "**Impact Analysis**: The farmer would have to push heavy wheelbarrows of dung 150 meters uphill every day, wasting immense physical energy.",
                                "**Redesign Solution**: Move the compost pit down between the cow shed and the vegetable garden, cutting transport distance to just 10 meters!"
                            ]
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Spatial Placement",
                        "content": {
                            "question": "Where should the compost pit ideally be positioned on an integrated farm layout to maximize labor efficiency?",
                            "options": [
                                "Directly inside the family living room.",
                                "At the furthest corner of the farm away from all crop plots.",
                                "Centrally located between the livestock sheds (which produce dung) and the crop beds (which consume compost).",
                                "Submerged under the fish pond water."
                            ],
                            "answer": "C",
                            "explanation": "Locating the compost heap between animal sheds and crop beds minimizes the physical distance and labor needed to transport raw dung and crop residues to the pile, and finished manure back to the fields."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- A **farm layout on Manila paper** plans spatial arrangements for maximum balance and efficiency.\n- **Spatial optimization** places connected enterprises close together to cut transport labor.\n- Ponds sit at lower elevations for gravity flow, and **compost pits sit between sheds and gardens**.\n- Peer critiques refine layouts before physical construction begins."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we have drawn our 2D blueprints, let us bring them into 3D! In our final lesson, we construct a physical 3D farm model using cartons, clay, and twigs, review a video tour, and complete the Topic Assessment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Practical Activity: Constructing a 3D Integrated Farm Model & Capstone
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Practical Activity: Constructing a 3D Integrated Farm Model",
            "unit_description": "3D physical modeling from cardboard, clay, twigs, and bottle caps, teamwork roles, video review of Kenyan integrated farm, and 10 topic summative MCQs.",
            "lesson_title": "Practical Activity: Constructing a 3D Integrated Farm Model & Capstone",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Bringing Blueprints to Life: The 3D Farm Model",
                        "content": {
                            "title": "Bringing Blueprints to Life: The 3D Farm Model",
                            "caption": "A completed 3D student model of an integrated farm featuring cardboard barns, clay animals, a plastic-lined fish pond, and twig trees."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Practical Learning Objectives: 3D Model & Capstone",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Construct a representative 3D physical model of an integrated farm using low-cost, local materials.",
                                "Model crops, animals, ponds, and waste systems using cardboard, clay, twigs, and bottle caps.",
                                "Synthesize topic learning through an instructional video review of a Kenyan integrated farm.",
                                "Demonstrate complete curriculum mastery by completing the **Topic Summative Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Building a Miniature World",
                        "content": {
                            "title": "From 2D Blueprint to 3D Reality",
                            "text": "Today, we transform everyday scrap materials (cartons, clay, twigs, bottle caps) into a physical, three-dimensional model showcasing the closed-loop harmony of integrated farming!"
                        }
                    }
                ],
                # Page 2: Material Gathering & Exploded Model Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Exploded Blueprint: 3D Model Cardboard Assembly",
                        "content": {
                            "title": "Exploded Blueprint: 3D Model Cardboard Assembly",
                            "caption": "Exploded structural diagram detailing base foundation cardboard, folded matchbox coops, toothpick stilt hutches, blue plastic ponds, and toothpick label flags."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Mapping Farm Elements to Modeling Materials",
                        "content": {
                            "title": "3D Modeling Materials Guide",
                            "headers": ["Real Farm Component", "Recommended Local Material", "Construction Technique"],
                            "rows": [
                                ["Farm Foundation Base", "Sturdy shipping carton or plywood", "Cut to 50cm x 70cm flat rectangle"],
                                ["Buildings & Animal Coops", "Empty matchboxes, tea cartons, cardboard", "Fold, glue, and cut small doors/windows"],
                                ["Tilapia Fish Pond", "Blue bottle caps or blue paper lined with plastic", "Embed into base cardboard to create depth"],
                                ["Agroforestry Trees & Fences", "Dry twigs, matchsticks, split bamboo", "Glue vertically along farm boundaries"],
                                ["Livestock & Poultry", "Colored modeling clay or paper-mâché", "Mold miniature cows, goats, chickens, and rabbits"],
                                ["Component Identification", "Toothpicks with small paper flags", "Stick into components to label resource flows"]
                            ]
                        }
                    }
                ],
                # Page 3: Step-by-Step 3D Construction Procedure
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: 3D Construction",
                        "content": {
                            "title": "Step-by-Step Assembly Protocol",
                            "steps": [
                                "**Step 1 (Baseplate Setup)**: Cut a flat, rigid carton baseplate and mark zones using your Manila paper layout.",
                                "**Step 2 (Structures & Stilts)**: Build the house, goat pen, and elevated rabbit hutch on matchstick stilts; glue securely to the base.",
                                "**Step 3 (Pond & Irrigation)**: Cut a shallow depression for the fish pond, line with blue paper/wrap, and run wool strings to represent drip pipes.",
                                "**Step 4 (Crops & Trees)**: Glue green paper strips for vegetable beds and stick dry twigs along borders for agroforestry trees.",
                                "**Step 5 (Animals & Labels)**: Place clay animals in their designated pens and insert labeled toothpick flags to identify each enterprise."
                            ]
                        }
                    }
                ],
                # Page 4: Teamwork, Collaboration & Presentation
                [
                    {
                        "type": "mini_activity",
                        "title": "Team Showcase & Presentation",
                        "content": {
                            "title": "Present Your Closed-Loop Model",
                            "instruction": "Present your completed 3D farm model to the class. Use your finger to trace the continuous nutrient loop: show how crop residues feed your clay cow, how cow dung goes to the compost pit, and how compost fertilizes the paper vegetable beds!"
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Topic Master Synthesis
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: 3D Model Labeling",
                        "content": {
                            "question": "Why are toothpicks with small paper flags highly recommended when assembling your 3D integrated farm model?",
                            "options": [
                                "To poke drainage holes in the cardboard baseplate.",
                                "To act as mini boundary fences around the rabbit hutch.",
                                "To clearly label and identify every enterprise component and resource recycling loop for viewers.",
                                "To hold the wet modeling clay animals together."
                            ],
                            "answer": "C",
                            "explanation": "Adding clear paper flag labels on toothpicks allows classmates and teachers to easily identify each designed farm enterprise and trace the circular nutrient and water flows."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 3 Master Summary: The Closed-Loop Farm",
                        "content": {
                            "text": "- **Integrated farming** combines crops, livestock, aquaculture, agroforestry, and small animals into a single harmonious web.\n- **Zero waste philosophy**: every byproduct (dung, urine, stover, pond water) serves as an essential input for another enterprise.\n- **Water & nutrient loops** cut farm expenses by up to 80% and build resilience against drought.\n- **Spatial optimization** minimizes transport labor, creating productive and sustainable family farms."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: How to Start an Integrated Farming System with Zero Waste",
                        "content": {
                            "title": "Topic Video Review: How to Start an Integrated Farming System with Zero Waste",
                            "url": "https://www.youtube.com/watch?v=uFnDdYWgkV8",
                            "resolved_video_id": "uFnDdYWgkV8",
                            "caption": "Watch this comprehensive real-world tour of G-BiACK Kenya demonstrating zero-waste integrated farming, closed-loop nutrient recycling, fish pond irrigation, and rabbit urine harvesting."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Things to Observe in the Video",
                        "content": {
                            "title": "Focus Questions for Video Reflection",
                            "text": "- **1. Physical Proximity**: Notice how the fish pond sits close to the vegetable beds for easy water transfer.\n- **2. Urine Collection**: Observe the sloped gutters beneath rabbit hutches draining into collection containers.\n- **3. Economic Impact**: Note how Kenyan smallholders eliminate fertilizer and feed expenses through circular loops."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Guiding Principle",
                        "content": {
                            "question": "What is the primary guiding principle of a successful integrated farming system?",
                            "options": [
                                "Treating crop production, animal husbandry, and water management as completely separate operations.",
                                "Reducing total land used by keeping large livestock inside the family home.",
                                "Ensuring there is no waste by recycling the byproduct of one enterprise as an input for another.",
                                "Maximizing crop yields by utilizing synthetic chemical pesticides and fertilizers exclusively."
                            ],
                            "answer": "C",
                            "explanation": "The foundational principle of integrated farming is the closed-loop concept: there is no waste. Byproducts like animal manure, crop residues, and pond water are recycled and reused as fertilizers and feeds, creating a self-sustaining system."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Feed Residues",
                        "content": {
                            "question": "Which of the following crop leftovers can be gathered from the field after harvest and recycled directly as feed for rabbits or cows?",
                            "options": [
                                "Dry rotten tomato skins from the compost heap.",
                                "Leftover green bean vines, pea pods, and sweet potato vines.",
                                "Eucalyptus leaves and pine cones from the windbreak border.",
                                "Maize stover that has been burned to ash."
                            ],
                            "answer": "B",
                            "explanation": "Green legume residues (bean vines, pea pods) and sweet potato vines are highly digestible, protein-rich feeds that can be fed directly to livestock and rabbits, saving on commercial feed bills."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Legume Intercropping",
                        "content": {
                            "question": "When establishing a vegetable garden in an integrated farm, why is it highly beneficial to plant beans or peas (legumes) next to leafy kales?",
                            "options": [
                                "Beans block the kales from getting too much hot sunlight.",
                                "Legumes naturally fix atmospheric nitrogen, which enriches and fertilizes the surrounding crop soil.",
                                "Legumes act as a sticky trap that catches and kills all caterpillars.",
                                "Beans absorb soil nitrogen rapidly, leaving more water for the kale roots."
                            ],
                            "answer": "B",
                            "explanation": "Leguminous crops host nitrogen-fixing bacteria in their root nodules that convert atmospheric nitrogen into soil nitrates, fertilizing companion leafy vegetables like kales naturally."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Manure vs. Synthetic Fertilizer",
                        "content": {
                            "question": "What is a major advantage of using decomposed livestock manure to fertilize your crop beds instead of synthetic chemical fertilizers?",
                            "options": [
                                "Organic manure dissolves instantly and leaves no residue in the soil.",
                                "Manure destroys all beneficial soil organisms like earthworms.",
                                "Manure adds organic matter, which improves soil structure and helps the soil hold moisture during dry spells.",
                                "Manure changes the biological family of crop plants to make them grow woody."
                            ],
                            "answer": "C",
                            "explanation": "Unlike synthetic fertilizers, organic decomposed manure adds vital humus. This improves soil physical structure, enhances soil water-holding capacity, and feeds beneficial earthworms and soil microbes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Rabbit Urine Dilution Calculation",
                        "content": {
                            "question": "Farmer Mary collects 3 liters of pure, concentrated rabbit urine from her hutches. To safely spray this on her spinach leaves as organic foliar feed without burning them, how much water should she add?",
                            "options": [
                                "3 liters of water (1:1 ratio)",
                                "15 liters of water (1:5 ratio)",
                                "150 liters of water (1:50 ratio)",
                                "No water; rabbit urine must be sprayed pure."
                            ],
                            "answer": "B",
                            "explanation": "Pure rabbit urine has a high nitrogen concentration that will chemically burn crop leaves if applied raw. It must be diluted with water at a 1:5 ratio (3 liters of urine × 5 = 15 liters of water)."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Aquaculture Water Nutrient Link",
                        "content": {
                            "question": "How does aquaculture (fish farming) water directly support horticultural crop production on an integrated farm?",
                            "options": [
                                "The water carries predatory fish that jump out to eat crop pests.",
                                "The water becomes enriched with organic fish wastes, providing pre-dissolved natural nitrogen fertilizer for vegetables.",
                                "The water is extremely salty, which kills weeds automatically when sprayed.",
                                "Draining the pond water prevents any rain from entering the soil."
                            ],
                            "answer": "B",
                            "explanation": "Tilapia and catfish excrete waste directly into pond water. Draining or pumping this water to irrigate crops delivers pre-dissolved organic nitrogen and minerals that plants absorb instantly."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Layout Spatial Planning",
                        "content": {
                            "question": "When planning your 2D farm layout on Manila paper, why is it highly inefficient to place the compost pit at the furthest corner of the farm away from livestock sheds and vegetable beds?",
                            "options": [
                                "The distance will cause the composting temperature to drop, stopping decomposition.",
                                "Rainwater cannot reach the compost heap if it is placed in a corner.",
                                "It forces the farmer to spend massive amounts of physical labor and time carrying heavy dung and crop leftovers over long distances.",
                                "Animals will feel lonely if the compost pit is too far away."
                            ],
                            "answer": "C",
                            "explanation": "Spatial optimization aims to minimize transport labor. Placing the compost pit between animal sheds (which produce dung) and crop beds (which consume compost) saves hours of heavy manual transport."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Agroforestry Erosion Protection",
                        "content": {
                            "question": "How do agroforestry trees planted along contour terraces protect crop fields during a severe storm?",
                            "options": [
                                "Their leaves absorb and release synthetic nitrogen into the wind.",
                                "Their roots act as an underground anchor net that holds the soil, while their leaves slow down heavy rainwater runoff to reduce nutrient loss.",
                                "They pump all water out of the soil so the crops never get wet.",
                                "They attract lightning away from the farm buildings."
                            ],
                            "answer": "B",
                            "explanation": "Trees have extensive root systems that bind soil particles, physically preventing heavy storm rains from washing away topsoil. Their leafy canopies break raindrop impact, and ground leaf mulch slows surface runoff."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: System Imbalances & Eutrophication",
                        "content": {
                            "question": "A student designs an integrated farm model with a poultry house built on stilts directly over a fish pond. After a few weeks, a thick green algal bloom covers the pond, and the tilapia are gasping at the surface. What caused this problem?",
                            "options": [
                                "The fish are hungry because they dislike chicken droppings.",
                                "Too many chickens are over-shading the pond water.",
                                "Too many poultry droppings fell into the water, causing excessive nutrient enrichment (eutrophication) which depleted dissolved oxygen.",
                                "The chickens are actively swimming in the pond and drinking all the water."
                            ],
                            "answer": "C",
                            "explanation": "While modest bird droppings grow plankton to feed fish, an excessive volume overloads the water with nitrogen and phosphorus (eutrophication). This triggers massive algal blooms that consume dissolved oxygen, suffocating the fish."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Complex Multi-Enterprise Synthesis",
                        "content": {
                            "question": "Farmer Juma has a 2-acre hillside farm in a dry, windy region with sandy soil, rapid runoff, and lack of money for chemical inputs or goat feed. Which integrated design best solves all of Juma's problems simultaneously?",
                            "options": [
                                "Planting a single field of wheat on the slope and purchasing commercial synthetic fertilizers.",
                                "Planting nitrogen-fixing fodder trees along contour slopes to anchor soil, keeping dairy goats in a shed to produce milk and manure, and using composted goat manure on vegetable beds irrigated with harvested rainwater.",
                                "Cutting down all trees to create space for a giant fish pond on top of the hill.",
                                "Rearing 100 free-range chickens randomly on the bare slope without any water harvesting structures."
                            ],
                            "answer": "B",
                            "explanation": "This multi-enterprise system creates complete circular harmony: contour fodder trees anchor sandy soil and feed goats; goats produce milk and rich dung; dung is composted to enrich vegetable beds; and harvested rainwater provides cost-free irrigation."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade9_agriculture_topic3(replace: bool = True):
    """Executes the database transaction to ingest Topic 3 into CBC Grade 9 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 9 AGRICULTURE — TOPIC 3")
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
        topic_name = "Integrated Farming"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 3,
                "description": "Comprehensive integrated farming systems: crop biomass recycling, livestock integration, aquaculture water loops, agroforestry soil protection, small-scale rabbits and poultry, 2D Manila layout design, and 3D farm modeling."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        # 3. Ingest Units and Lessons
        curriculum_data = build_topic3_curriculum()
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
                        block_id=f"g9_agri_t3_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Topic 3: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade9_agriculture_topic3(replace=replace_flag)
