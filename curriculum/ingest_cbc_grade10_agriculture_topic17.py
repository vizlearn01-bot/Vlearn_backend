"""
VLearn CBC Grade 10 Agriculture — Topic 17: Composting
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Composting (Topic Order: 17)

Decomposed into 10 Learning Units & 10 Published Lessons:
  1. Introduction to Composting and Organic Manures (4 Pages, 9 Blocks)
  2. Factors Determining Compost Quality (4 Pages, 9 Blocks)
  3. Siting and Material Preparation for Conventional Composting (4 Pages, 9 Blocks)
  4. Conventional Composting — The Four-Pit Method (Layering) (4 Pages, 10 Blocks)
  5. Conventional Composting — Turning and Managing the Pits (4 Pages, 9 Blocks)
  6. Above-Ground Heap (Stack) Composting (4 Pages, 9 Blocks)
  7. Innovative Composting — Vermicomposting (4 Pages, 10 Blocks)
  8. Innovative Composting — Containerized (Bin) Composting (4 Pages, 9 Blocks)
  9. The Role of Composting in Soil Improvement (4 Pages, 9 Blocks)
  10. Practical Field Application, Advocacy & Topic Review (8 Pages, 17 Blocks)
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

def build_topic17_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 17: Composting."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Composting and Organic Manures
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Composting and Organic Manures",
            "unit_description": "Biological decomposition, aerobic conditions, organic manure vs synthetic fertilizer, physical maturity indicators.",
            "lesson_title": "Soil Microbiology: Biological Decomposition and Physical Indicators of Mature Compost",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Finished Dark Crumbly Compost for Agricultural Soil Enrichment",
                        "content": {
                            "title": "Finished Dark Crumbly Compost for Agricultural Soil Enrichment",
                            "caption": "Rich, dark brown, crumbly mature organic compost ready for field application, showing complete biological stabilization."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Introduction to Composting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **composting** as a controlled aerobic biological decomposition process.",
                                "Compare the agricultural benefits of **organic manure vs. synthetic chemical fertilizers**.",
                                "Identify the **4 physical indicators of fully mature compost** (Color, Texture, Odor, Temperature).",
                                "Explain why immature compost burns crop roots through heat and nitrogen tie-up."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Biology of Composting",
                        "content": {
                            "title": "Nature's Microscopic Recycling Engineers",
                            "text": "**Composting** is the natural, biological decomposition and stabilization of organic waste by beneficial microorganisms (bacteria, fungi, and actinomycetes) under controlled, aerobic (oxygen-rich) conditions:\n\n- Rather than allowing organic wastes to rot randomly in uncontrolled dumps, composting directs their breakdown into a nutrient-rich, dark, soil-like humus called **organic manure**.\n- Microorganisms consume carbon-rich and nitrogen-rich raw materials, converting them into cellular energy, heat, carbon dioxide, water, and stable organic matter."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Organic Manure vs Synthetic Chemical Fertilizers",
                        "content": {
                            "title": "Building Long-Term Soil Fertility",
                            "text": "- **Organic Manure**: Recycled from crop residues and animal wastes. It provides slow-release multi-nutrients, permanently improves physical soil structure, boosts water-holding capacity, and feeds beneficial soil microbes.\n- **Synthetic Fertilizers (e.g., DAP, CAN, Urea)**: Fast-acting chemical salts supplying concentrated primary nutrients. However, they add zero organic matter, acidify soil over time, kill beneficial soil microbes, and leach into groundwater.\n- **Agribusiness Advantage**: On-farm composting recycles zero-cost waste, drastically slashing farm expenses on chemical fertilizers."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Physical Indicators of Fully Mature Compost",
                        "content": {
                            "title": "Physical Indicators of Fully Mature Compost",
                            "caption": "Maturity Quad: 1 Dark Brown/Jet Black Color | 2 Fine Crumbly Texture (No raw pieces) | 3 Clean Earthy Forest Smell (Zero ammonia/rotten eggs) | 4 Cool Ambient Temperature (Thermophilic phase complete)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Organic Compost vs Synthetic Chemical Fertilizer",
                        "content": {
                            "title": "Agronomic and Environmental Comparison",
                            "headers": ["Parameter", "Organic Compost Manure", "Synthetic Chemical Fertilizer (e.g. DAP/CAN)"],
                            "rows": [
                                ["Nutrient Release", "Slow-release (Continuous feeding over 2-3 seasons)", "Fast-acting (Rapid spike, rapid depletion)"],
                                ["Organic Matter", "Extremely High (Adds permanent humus)", "Zero organic matter"],
                                ["Soil Physical Structure", "Dramatically improves porosity & water retention", "No structural improvement; causes soil crusting"],
                                ["Soil Microbial Life", "Feeds and multiplies beneficial bacteria/fungi", "High chemical salts can kill earthworms & microbes"],
                                ["Production Cost", "Virtually zero (Recycled farm wastes)", "Very high cash expenditure per bag"],
                                ["Leaching & Pollution", "Minimal leaching (Nutrients held by humus CEC)", "High risk of nitrogen/phosphorus water runoff"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Lab Practicum: Evaluating Compost Maturity Across 3 Organic Samples",
                        "content": {
                            "title": "Compost Maturity Sensory Evaluation",
                            "task": "Observe 3 samples on paper trays:\n- Sample 1: Fresh raw kitchen peels\n- Sample 2: Half-decayed pit material\n- Sample 3: Finished farmyard compost\nRecord Color, Texture, Odor, and Temperature. Deduce maturity status.",
                            "materials": ["Gloves", "Paper Trays", "3 Organic Samples"],
                            "safety": "Wear rubber gloves and avoid inhaling raw mold."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Composting Biology",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Composting is aerobic biological decomposition into stable humus**.\n- **Mature compost is dark black, crumbly, earthy-smelling, and cool**.\n- **Immature compost burns plant roots and immobilizes soil nitrogen**.\n- **Compost permanently builds soil structure and cuts fertilizer costs**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Why Immature Compost Burns Roots",
                        "content": {
                            "question": "Why must a farmer wait for compost to become completely cool, dark brown, and crumbly before incorporating it into a vegetable seedbed?",
                            "options": [
                                "Raw undecomposed materials are too heavy for jembes to lift",
                                "Active decomposition of immature compost generates intense heat (thermophilic stage) and consumes surrounding soil oxygen and nitrogen, scorching young crop roots and causing nitrogen starvation",
                                "Finished compost must be hot to release nitrogen into the soil",
                                "Cool compost attracts destructive aphids to the farm"
                            ],
                            "answer": "B",
                            "explanation": "Immature compost is still undergoing active microbial decay, generating intense heat and consuming available nitrogen and oxygen from surrounding soil (nitrogen immobilization). Applying it too early scorches tender root tissues and starves plants of nitrogen."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Factors Determining Compost Quality
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Factors Determining Compost Quality",
            "unit_description": "C:N ratio (30:1 golden ratio, browns vs greens), moisture (50-60% sponge test), aeration, thermophilic sanitizing temperature (55-65°C), pH (6.0-7.0).",
            "lesson_title": "Biochemical Optimization: Carbon-to-Nitrogen (C:N) Ratios, Moisture, Aeration, and Temperature",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Checking Internal Thermophilic Temperature of a Compost Pile",
                        "content": {
                            "title": "Checking Internal Thermophilic Temperature of a Compost Pile",
                            "caption": "A compost dial thermometer inserted into a steaming organic pile, monitoring the 55°C–65°C thermophilic sanitizing temperature range."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Factors Determining Compost Quality",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the **Carbon-to-Nitrogen (C:N) Ratio** and the **30:1 Golden Rule**.",
                                "Differentiate **Carbon Browns vs. Nitrogen Greens**.",
                                "Apply the **50%–60% Moisture 'Sponge Test'**.",
                                "Analyze **Thermophilic Sanitization (55°C–65°C)** for killing weed seeds and crop pathogens."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Carbon-to-Nitrogen (C:N) Ratio",
                        "content": {
                            "title": "The Microscopic Balanced Diet",
                            "text": "Microorganisms require Carbon (C) for cellular energy and Nitrogen (N) for protein synthesis and population growth:\n\n- **The Golden Ratio**: Fast, hot composting occurs at an initial overall **C:N ratio of 30:1** (30 parts carbon to 1 part nitrogen).\n- **Carbon Browns (C:N 50:1 to 500:1)**: Dry maize stalks, straw, dry leaves, wood shavings, sawdust, cardboard. (Provide structural porosity and energy).\n- **Nitrogen Greens (C:N 10:1 to 20:1)**: Fresh green grass, vegetable trimmings, legume residues, animal manure. (Provide moisture and rapid microbial food).\n- **Imbalance Hazards**: Too much carbon $\\rightarrow$ decay takes months or years. Too much nitrogen $\\rightarrow$ pile turns wet, anaerobic, and loses nitrogen as foul ammonia gas."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Moisture, Aeration, Temperature, and pH",
                        "content": {
                            "title": "The 4 Physical Drivers of Aerobic Decomposition",
                            "text": "1. **Moisture (50%–60%)**: Decomposers live in a microscopic water film. *The Sponge Test*: Squeezing a handful of compost should feel like a wrung-out sponge—damp, releasing only 1–2 drops of water under hard pressure.\n2. **Aeration (Oxygen)**: Composting must remain aerobic. If water fills all pore spaces, oxygen is expelled, triggering smelly **anaerobic decay** that releases methane and foul hydrogen sulfide (rotten eggs).\n3. **Temperature Stages**:\n   - *Mesophilic Stage (20°C–40°C)*: Initial breakdown by moderate microbes.\n   - *Thermophilic Stage (55°C–65°C)*: Intense microbial heat that **kills weed seeds, fungal spores, and enteric pathogens (E. coli)**! (Must not exceed 70°C).\n4. **pH Level (6.0–7.0)**: Slightly acidic to neutral range is optimal. Excessive wood ash causes extreme alkalinity and nitrogen gas loss."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Key Factors Determining Compost Quality & Microbial Activity",
                        "content": {
                            "title": "Key Factors Determining Compost Quality & Microbial Activity",
                            "caption": "Biochemical Optimization Matrix: 1 C:N Ratio (30:1 Golden Balance) | 2 Moisture (50-60% Wrung-Out Sponge) | 3 Aeration (Aerobic Oxygen via Turning) | 4 Temperature (55-65°C Sanitizing Hot Zone) | 5 pH (6.0-7.0 Neutral Buffering)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Carbon Browns vs Nitrogen Greens Composition Matrix",
                        "content": {
                            "title": "Common Farm Materials C:N Classification",
                            "headers": ["Raw Organic Material", "Classification", "Approximate C:N Ratio", "Primary Function in Compost"],
                            "rows": [
                                ["Dry Wood Sawdust / Shavings", "High Carbon (Brown)", "400:1 to 500:1", "High energy, structural aeration bulk"],
                                ["Dry Maize Stalks / Straw", "High Carbon (Brown)", "80:1 to 100:1", "Pore aeration, prevents compaction"],
                                ["Dry Fallen Tree Leaves", "Moderate Carbon (Brown)", "50:1 to 60:1", "Balanced carbon breakdown"],
                                ["Fresh Green Grass Clippings", "Nitrogen (Green)", "15:1 to 20:1", "Moisture, rapid bacterial fuel"],
                                ["Kitchen Vegetable Scraps", "Nitrogen (Green)", "12:1 to 18:1", "Rapid microbial nutrient release"],
                                ["Fresh Chicken Manure", "High Nitrogen (Green)", "10:1 to 12:1", "Concentrated nitrogen & microbial starter"],
                                ["Cattle / Goat Dung", "Balanced Green / Starter", "20:1 to 25:1", "Rumen bacteria inoculant & nitrogen"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: The Wrung-Out Sponge Moisture Test",
                        "content": {
                            "title": "Moisture & Squeeze Test Practicum",
                            "task": "Take 3 handfuls of compost materials at different water levels:\n- Squeeze firmly in hand.\n- Sample A: Crumples and dusts apart (Too dry, <30%)\n- Sample B: Water streams out between fingers (Too wet, >70%)\n- Sample C: Feels damp, yields 1-2 drops under maximum grip (Perfect 50-60%)\nRecord results and calculate water adjustment.",
                            "materials": ["Compost Samples", "Gloves", "Watering Can"],
                            "safety": "Wash hands with soap after handling compost."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Compost Quality Factors",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Initial pile needs a 30:1 C:N ratio for rapid heating**.\n- **Moisture must be 50–60% (wrung-out sponge standard)**.\n- **Aerobic conditions prevent rotten egg odors and methane**.\n- **Thermophilic heat (55–65°C) pasteurizes weeds and pathogens**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing High C:N Failure",
                        "content": {
                            "question": "A student group sets up a compost heap using only dry maize stalks and pine wood sawdust. After six weeks, the heap has not changed in appearance, has zero heat, and shows no decay. What is the scientific diagnosis?",
                            "options": [
                                "The C:N ratio is too low; excessive nitrogen has sterilized the bacteria",
                                "Pine sawdust contains toxic anti-matter",
                                "The C:N ratio is excessively high (>100:1); there is a severe shortage of nitrogen to feed bacterial multiplication and protein synthesis",
                                "The pile was exposed to moonlight which halts microbial enzymes"
                            ],
                            "answer": "C",
                            "explanation": "Dry stalks and sawdust are exceptionally high in carbon and lack nitrogen. Without nitrogen, bacteria cannot synthesize proteins or multiply, halting decomposition. Mixing in nitrogen greens (fresh grass, poultry manure) lowers the C:N ratio to 30:1, restarting rapid decay."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Siting and Material Preparation for Conventional Composting
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Siting and Material Preparation for Conventional Composting",
            "unit_description": "Siting criteria (drainage, shade, proximity, accessibility), sorting browns/greens/inoculants/ash, banned materials (meat, dairy, diseased crops, noxious weeds).",
            "lesson_title": "Site Selection and Material Sorting: Siting Criteria and Waste Segregation Protocols",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Sorting Kitchen Scraps and Organic Farm Waste for Composting",
                        "content": {
                            "title": "Sorting Kitchen Scraps and Organic Farm Waste for Composting",
                            "caption": "Separating clean fruit peels and vegetable trimmings into designated organic collection containers, demonstrating proper waste segregation."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Siting and Material Preparation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Evaluate **4 critical siting factors (Drainage, Shade/Wind, Proximity, Accessibility)**.",
                                "Sort organic wastes into **Coarse Base, Fine Browns, Fresh Greens, Inoculants, and Ash**.",
                                "Identify **materials strictly banned from compost** and understand why.",
                                "Execute a farmyard waste segregation protocol."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Siting the Composting Unit",
                        "content": {
                            "title": "Strategic Farm Placement",
                            "text": "Selecting the location for a composting system is a vital sanitary and operational decision:\n\n1. **Good Drainage**: Must be situated on a gently sloping, well-drained area. Low-lying waterlogged depressions must be avoided, as stagnant water floods pits and kills aerobic bacteria.\n2. **Wind and Shade Protection**: Placing compost under shade trees shields it from direct hot sun and strong winds, reducing evaporation and conserving water.\n3. **Proximity**: Located close to crop gardens and livestock barns for easy transport, yet at least 10–15 meters away from human houses and clean water wells to prevent nuisance odors or runoff.\n4. **All-Weather Accessibility**: Reachable by wheelbarrow or cart in both dry and rainy seasons."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Sorting Organic Materials into Functional Layers",
                        "content": {
                            "title": "Material Classification Pipeline",
                            "text": "- **Coarse Browns (Drainage Base)**: Woody twigs, maize stalks, sunflower stems (15–20 cm at pit base for aeration and drainage).\n- **Fine Browns (Carbon source)**: Dry leaves, chopped straw, dry grass, sawdust.\n- **Fresh Greens (Nitrogen source)**: Vegetable trimmings, kitchen scraps, fresh weeds (before seed set).\n- **Microbial Inoculants**: Fertile topsoil or mature compost (supplies billions of active decomposer microbes).\n- **Mineral Ash**: Wood ash dusting (supplies potassium and buffers organic acids)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Materials Strictly Banned from the Compost Pile",
                        "content": {
                            "title": "Sanitary and Agronomic Exclusions",
                            "text": "- **Meat, Bones, Fats, Oils, Dairy**: Decompose via putrefaction pathways, producing cadaverine odors that attract houseflies, rats, and stray dogs.\n- **Diseased Plants (Bacterial Wilt, Late Blight)**: Pathogens survive in cool piles and reinfect future crops.\n- **Noxious Weeds with Seeds/Rhizomes (Couch Grass, Blackjack)**: Seeds survive cool composting and spread across fields.\n- **Plastics, Metals, Glass, Battery Casings**: Non-biodegradable toxic soil pollutants."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Permitted vs Banned Composting Materials Guide",
                        "content": {
                            "title": "Organic Waste Sorting Protocol",
                            "headers": ["Material Name", "Category", "Composting Status", "Scientific Reason / Impact"],
                            "rows": [
                                ["Dry Maize Stalks & Twigs", "Coarse Carbon Base", "Permitted (Mandatory Base)", "Creates bottom air drainage channels"],
                                ["Fruit Peels & Cabbage Leaves", "Fresh Nitrogen Green", "Permitted", "Feeds bacteria with moisture & nitrogen"],
                                ["Cow Dung & Chicken Manure", "Inoculant / Nitrogen", "Permitted", "Supplies active rumen bacteria & nitrogen"],
                                ["Wood Ash from Firewood", "Mineral Buffer", "Permitted (Light Dusting)", "Adds potassium and balances acidic pH"],
                                ["Cooked Meat & Chicken Bones", "Animal Protein / Fat", "Strictly Banned", "Attracts rats, flies, dogs; foul cadaverine odor"],
                                ["Late Blight Tomato Leaves", "Diseased Crop Residue", "Strictly Banned", "Spreads fungal spores to future crops"],
                                ["Couch Grass Rhizomes & Seeds", "Noxious Weed", "Strictly Banned", "Survives decay; infests crop seedbeds"],
                                ["Plastic Bags & Bottle Tops", "Inorganic Synthetic", "Strictly Banned", "Non-biodegradable; pollutes soil"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Waste Sorting Practicum: Sorting 4 Buckets of School Waste",
                        "content": {
                            "title": "Organic Waste Segregation Lab",
                            "task": "Take mixed school farm waste:\n- Sort into Bucket A (Browns), Bucket B (Greens), Bucket C (Inoculants), and Bucket D (Banned Waste).\n- Provide scientific justification for each item in Bucket D.",
                            "materials": ["4 Labeled Buckets", "Mixed Farm Waste", "Gloves", "Masks"],
                            "safety": "Use tongs/gloves when handling sharp bones or broken glass."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Siting & Sorting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Site compost in shaded, well-drained spots 10–15m from houses**.\n- **Coarse woody stalks form the essential bottom aeration base**.\n- **Strictly ban meat, dairy, diseased crops, and seed-bearing weeds**.\n- **Topsoil and manure inoculate new piles with millions of microbes**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Why Meat and Dairy are Banned",
                        "content": {
                            "question": "Why should agricultural students strictly exclude cooked meat scraps, animal bones, and dairy residues from their school compost pit?",
                            "options": [
                                "Meat scraps are too acidic and will permanently lower compost pH to 2.0",
                                "Meat decomposes so rapidly that it freezes the compost heap",
                                "Meat and dairy produce foul putrefaction odors (cadaverine/putrescine) that attract disease vectors like flies, rats, and stray dogs",
                                "Dairy products contain calcium which dissolves organic humus"
                            ],
                            "answer": "C",
                            "explanation": "Animal proteins and fats decay via putrefaction pathways, releasing foul odors that attract disease vectors like houseflies and rodents, and draw stray dogs that tear open compost heaps, creating severe hygiene hazards."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Conventional Composting — The Four-Pit Method (Layering)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Conventional Composting — The Four-Pit Method (Layering)",
            "unit_description": "Four-pit layout (1.2m x 1.2m x 1.2m), sequential layering in Pit 1 (drainage base, browns, greens, manure, ash, topsoil), stick test monitoring.",
            "lesson_title": "The Four-Pit System: Structural Layout, Sequential Layering, and Diagnostic Stick Monitoring",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Excavation and Structural Preparation of a Below-Ground Compost Pit",
                        "content": {
                            "title": "Excavation and Structural Preparation of a Below-Ground Compost Pit",
                            "caption": "A 1.2m x 1.2m x 1.2m below-ground composting pit dug in well-drained soil, ready for sequential material layering."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Four-Pit System",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Describe the structural layout of a standard **Four-Pit Composting System**.",
                                "Execute the **scientific 7-step layering sequence inside Pit 1**.",
                                "Deploy the **Stick Test** to monitor internal temperature and moisture.",
                                "Differentiate between normal thermophilic heat and anaerobic failure."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Layout and Architecture of the Four-Pit System",
                        "content": {
                            "title": "Continuous Manure Production Pipeline",
                            "text": "The **Four-Pit Composting System** is an organized conventional method designed to deliver a continuous supply of fully mature organic manure:\n\n- **Dimensions**: Four adjacent square pits dug in a straight line, each measuring **1.2 meters wide by 1.2 meters long by 1.2 meters deep**, spaced 0.5 meters apart.\n- **Directional Flow**: Raw organic wastes are layered ONLY in **Pit 1**. Materials are turned into Pit 2, then Pit 3, and harvested as finished manure from Pit 4!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Scientific Layering Sequence (Pit 1)",
                        "content": {
                            "title": "7-Step Layering Architecture",
                            "text": "1. **Drainage Base (15–20 cm)**: Coarse maize stalks, sunflower stems, or woody branches. (Allows excess water drainage and bottom airflow).\n2. **Carbon Brown Layer (10 cm)**: Dry grass, dry leaves, or chopped straw.\n3. **Nitrogen Green Layer (10 cm)**: Fresh green weeds, kitchen vegetable trimmings, or legume leaves.\n4. **Animal Manure Layer (5 cm)**: Cattle dung, goat manure, or poultry litter.\n5. **Mineral Ash Layer (Dusting)**: Light dusting of wood ash to supply potassium and buffer acidity.\n6. **Microbial Topsoil Layer (2 cm)**: Fertile topsoil or mature compost to inoculate microbes.\n7. **Water Sprinkle**: Sprinkle water until damp (wrung-out sponge standard). Repeat sequence to 30 cm above ground level."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Four-Pit Composting System Layout & Directional Flow",
                        "content": {
                            "title": "Four-Pit Composting System Layout & Directional Flow",
                            "caption": "Four-Pit Layout: Pit 1 (Raw Material Layering) -> Shift at Week 3 -> Pit 2 (First Heat Cycle) -> Shift at Week 6 -> Pit 3 (Curing & Breakdown) -> Shift at Week 9 -> Pit 4 (Harvest Fully Mature Compost at Week 12)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Diagnostic Stick Test",
                        "content": {
                            "title": "Checking the Compost Vital Signs",
                            "text": "- Drive a long, pointed, dry wooden stick vertically into the center of Pit 1.\n- Pull the stick out after 3–5 days and weekly thereafter, feeling the tip:\n  - *Hot & Moist*: Active thermophilic decomposition (Perfect!).\n  - *Cold & Waterlogged*: Anaerobic decay (Drain and turn!).\n  - *Cold & Bone-Dry*: Dehydrated microbes (Add water and nitrogen greens!)."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Building a High-Quality Four-Pit Compost System",
                        "content": {
                            "title": "Building a High-Quality Four-Pit Compost System",
                            "description": "Educational video demonstrating site layout, pit digging, and sequential layering of coarse base, browns, greens, manure, ash, and soil on a Kenyan farm.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Practical Field Construction: Building Pit 1 Layer by Layer",
                        "content": {
                            "title": "Four-Pit Construction Practicum",
                            "task": "1. Dig Pit 1 (1.2m x 1.2m x 1.2m).\n2. Place 15cm coarse stalk drainage base.\n3. Add 10cm dry leaves (Browns), 10cm green weeds (Greens), 5cm manure, ash dusting, and 2cm topsoil.\n4. Water lightly and drive a central monitoring stick into the core.",
                            "materials": ["Jembes", "Spades", "Tape Measure", "Monitoring Stick", "Organic Materials"],
                            "safety": "Wear boots and lift heavy soil with bent knees."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Four-Pit Layering",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Four-pit dimensions are 1.2m x 1.2m x 1.2m in sequential line**.\n- **Layering builds a 30:1 balance of coarse base, browns, greens, manure, ash, and soil**.\n- **The stick test acts as a thermometer to monitor microbial health**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Cold Dry Compost",
                        "content": {
                            "question": "During a weekly inspection of Pit 1, a student pulls out the central monitoring stick and finds it is completely cold, bone-dry, and covered in white powdery webs. What is the diagnosis and required corrective action?",
                            "options": [
                                "The pile decayed too fast; add ice blocks to cool it",
                                "The pile lacks moisture and nitrogen, causing bacteria to go dormant while dry actinomycete fungi dominate; add water and nitrogen greens/manure to restart aerobic decay",
                                "The white webs are toxic spider venom; burn the pit immediately",
                                "Cold and dry indicates fully finished compost; no action needed"
                            ],
                            "answer": "B",
                            "explanation": "Microbes require 50–60% moisture. When a compost pile dries out, bacteria become dormant, and dry-loving actinomycetes form white powdery webs. Adding water and nitrogen-rich green waste/manure rehydrates the microbes and restarts aerobic heat generation."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Conventional Composting — Turning and Managing the Pits
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Conventional Composting — Turning and Managing the Pits",
            "unit_description": "Turning science (aeration, uniform decay, weed/pathogen destruction), 12-week shifting schedule (Pit 1 -> 2 -> 3 -> 4), pit pros/cons.",
            "lesson_title": "Pit Management: Aeration Science, Chronological Turning Schedules, and Pit Trade-offs",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Aerating and Turning Organic Compost with Garden Tools",
                        "content": {
                            "title": "Aerating and Turning Organic Compost with Garden Tools",
                            "caption": "Turning and aerating organic compost with ventilation tubes and garden forks to introduce fresh oxygen and mix cool outer layers into the hot core."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Turning and Managing Pits",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the scientific purpose of **turning compost (Aeration, Uniform Decay, Pathogen Destruction)**.",
                                "Execute the **12-week chronological shifting schedule (Pit 1 -> 2 -> 3 -> 4)**.",
                                "Analyze the **advantages and disadvantages of below-ground pit composting**.",
                                "Prevent pit waterlogging and anaerobic odor failure."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Turning Compost",
                        "content": {
                            "title": "Why Moving Materials Multiplies Decomposition Speed",
                            "text": "**Turning** refers to physically shoveling and shifting materials from one pit to the next:\n\n1. **Aeration**: Breaks up compacted pockets and introduces fresh oxygen into the pile core, sustaining fast aerobic decomposition.\n2. **Uniform Decomposition**: Moves cool, dry outer layers into the hot, moist center so that all materials decay evenly.\n3. **Weed and Pathogen Destruction**: Forces outer weed seeds and disease spores into the hot thermophilic center (55°C–65°C) to be pasteurized."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Chronological Shifting Schedule (The 12-Week Cycle)",
                        "content": {
                            "title": "Continuous Pipeline Rotation",
                            "text": "- **Weeks 1–3**: Pit 1 is filled and undergoes its initial thermophilic heat cycle.\n- **Week 4 (First Shift)**: Contents of Pit 1 are turned into **Pit 2**. Pit 1 is reloaded with new raw waste.\n- **Week 7 (Second Shift)**: Contents of Pit 2 are turned into **Pit 3**. Pit 1 is turned into Pit 2. Pit 1 is reloaded.\n- **Week 10 (Third Shift)**: Contents of Pit 3 are turned into **Pit 4** for final curing and cooling.\n- **Week 12 (Harvest)**: Pit 4 contains fully mature, black, crumbly manure ready for field application!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Chronological Shifting Schedule of the Four-Pit System",
                        "content": {
                            "title": "Chronological Shifting Schedule of the Four-Pit System",
                            "caption": "12-Week Shifting Schedule: Week 1 (Fill Pit 1) -> Week 4 (Shift Pit 1 to 2) -> Week 7 (Shift Pit 2 to 3, 1 to 2) -> Week 10 (Shift Pit 3 to 4) -> Week 12 (Harvest Mature Compost from Pit 4)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Advantages and Disadvantages of Below-Ground Pit Composting",
                        "content": {
                            "title": "Pit Composting Trade-Offs",
                            "headers": ["Aspect", "Advantages of Pit Composting", "Disadvantages of Pit Composting"],
                            "rows": [
                                ["Moisture Retention", "Excellent (Shielded below ground from drying wind/sun)", "Can become waterlogged in heavy rainfall"],
                                ["Watering Needs", "Requires very little supplemental watering", "Excess rain cannot drain easily from clay soils"],
                                ["Tidiness & Aesthetics", "Neat, contained, wind cannot blow leaves around", "Digging 4 pits requires high initial manual labor"],
                                ["Turning Effort", "Structured stepwise progression across 4 pits", "Heavy physical labor lifting material up out of 1.2m pit"],
                                ["Climate Suitability", "Ideal for dry, arid, or windy regions", "Poor for flat, flooded areas with high water tables"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Agribusiness Practical: Executing a First Pit Shifting (Pit 1 to Pit 2)",
                        "content": {
                            "title": "Pit Shifting and Aeration Practicum",
                            "task": "1. Shovel contents of Pit 1 into Pit 2, ensuring outer cool edges are placed into the center.\n2. Check moisture with sponge test and sprinkle water if dry.\n3. Reload Pit 1 with freshly sorted school farm wastes.\n4. Drive monitoring stick into Pit 2.",
                            "materials": ["Spades", "Fork Jembes", "Watering Can", "Monitoring Stick"],
                            "safety": "Wear masks to prevent inhaling dust and fungal spores."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Pit Management",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Turning compost re-aerates the pile and pasteurizes weed seeds**.\n- **The four-pit schedule rotates every 3–4 weeks across a 12-week cycle**.\n- **Pits excel at moisture retention in dry climates but risk flooding in clay flats**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Pit Composting in Heavy Clay Flats",
                        "content": {
                            "question": "A school farm is located on flat land with heavy black cotton clay soil and severe seasonal flooding. Why should the agriculture teacher advise students AGAINST constructing a below-ground pit composting system?",
                            "options": [
                                "Clay soil contains high acidity that melts organic compost",
                                "During heavy rains, impermeable clay prevents drainage, flooding the pit and cutting off oxygen, turning the compost into a smelly anaerobic sludge",
                                "Pits in clay soil attract burrowing mole rats",
                                "Clay soils are too soft to dig 1.2m deep"
                            ],
                            "answer": "B",
                            "explanation": "Black cotton clay soil has exceptionally low drainage. In flat, flood-prone areas, a below-ground pit acts as a water reservoir, drowning aerobic bacteria and triggering foul anaerobic decomposition. Above-ground heaps are far superior in wet clay areas."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Above-Ground Heap (Stack) Composting
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Above-Ground Heap (Stack) Composting",
            "unit_description": "Heap design (1.0m x 1.0m x 1.2m), step-by-step construction, biological ventilation base, insulating cover (gunny sacks/soil), heap pros/cons.",
            "lesson_title": "Above-Ground Stack Composting: Structure, Ventilated Base Construction, and Moisture Protection",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Above-Ground Compost Heap Enclosed in Wooden Slats",
                        "content": {
                            "title": "Above-Ground Compost Heap Enclosed in Wooden Slats",
                            "caption": "An above-ground compost heap built on a 1.0m x 1.0m base with wooden slatted supports, demonstrating above-ground aeration and drainage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Above-Ground Heap Composting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Describe the structural dimensions of an **above-ground compost heap (1.0m x 1.0m x 1.2m)**.",
                                "Construct an above-ground stack using a **ventilated coarse base and alternating layers**.",
                                "Explain why covering with **gunny sacks or topsoil** prevents moisture loss and leaching.",
                                "Compare heap composting vs. pit composting in wet vs. dry climates."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Architecture of the Compost Heap (Stack)",
                        "content": {
                            "title": "Above-Ground Aeration and Construction",
                            "text": "The **Heap Composting Method** (or Stack Method) involves building organic piles entirely above ground level, making it ideal for wet climates, heavy clay soils, or rocky terrain where digging is impractical:\n\n- **Dimensions**: Base of **1.0 meter wide by 1.0 meter long** (or 1.5m x 1.5m), built to a height of **1.0 to 1.2 meters**.\n- **Height Limits**: Under 1.0m $\\rightarrow$ cannot generate or retain enough thermophilic heat. Over 1.2m $\\rightarrow$ heavy weight compacts the bottom, squeezing out oxygen."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Heap Construction and Protection",
                        "content": {
                            "title": "The 6-Step Stack Protocol",
                            "text": "1. **Mark & Loosen**: Mark 1.0m x 1.0m and loosen soil slightly with a fork jembe.\n2. **Biological Ventilator Base (15–20 cm)**: Coarse woody branches and maize stalks to draw in air from underneath.\n3. **Alternate Browns & Greens**: Layer 10 cm dry leaves/straw and 10 cm fresh green grass/manure.\n4. **Inoculate & Dust**: Sprinkle fertile topsoil and dust lightly with wood ash.\n5. **Moisten**: Water each layer to the wrung-out sponge standard.\n6. **Insulate & Cover**: Cover the completed dome with **old gunny sacks, dry grass, or breathable canvas** to trap heat and prevent rain leaching."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Above-Ground Compost Heap Architecture",
                        "content": {
                            "title": "Step-by-Step Above-Ground Compost Heap Architecture",
                            "caption": "Above-Ground Stack Architecture: 1 Protective Gunny Sack Cover (Prevents Drying & Leaching) | 2 Alternating Layers of Browns & Greens with Ash/Topsoil | 3 15-20cm Coarse Woody Base (Biological Ventilator) | Height: 1.0-1.2m."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Heap Composting vs Pit Composting Comparative Matrix",
                        "content": {
                            "title": "Heap vs Pit Method Comparison",
                            "headers": ["Feature", "Above-Ground Heap (Stack) Method", "Below-Ground Four-Pit Method"],
                            "rows": [
                                ["Ideal Climate / Soil", "Wet regions, heavy clay soils, high water tables", "Dry / arid regions, sandy well-drained soils"],
                                ["Ease of Turning", "Very Easy (Shovel sideways without lifting up)", "Demanding (Must lift material out of deep pit)"],
                                ["Aeration Rate", "Superior (Exposed to air on all 4 sides)", "Moderate (Limited side aeration)"],
                                ["Moisture Loss Risk", "High (Wind & sun cause rapid drying; needs sacks)", "Very Low (Underground walls shield moisture)"],
                                ["Waterlogging Risk", "Zero (Water drains freely away from base)", "High during heavy seasonal downpours"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Constructing a 1m x 1m Covered Compost Stack",
                        "content": {
                            "title": "Compost Stack Construction Lab",
                            "task": "1. Measure a 1.0m x 1.0m square.\n2. Lay 20cm coarse stalk base.\n3. Build alternating 10cm layers of dry grass and fresh greens/manure.\n4. Water to damp sponge standard.\n5. Cover with gunny sacks and insert monitoring stick.",
                            "materials": ["Tape Measure", "Fork Jembes", "Gunny Sacks", "Organic Wastes", "Watering Can"],
                            "safety": "Ensure stable vertical stacking to prevent collapse."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Heap Composting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Standard heap dimensions are 1.0m x 1.0m x 1.2m height**.\n- **Heaps provide superior aeration and zero flooding risk**.\n- **Protective gunny sack covers stop wind drying and rain nutrient leaching**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Purpose of Gunny Sack Cover",
                        "content": {
                            "question": "Why is it mandatory to cover an above-ground compost heap with old gunny sacks, dry grass, or a breathable sheet rather than leaving it completely bare?",
                            "options": [
                                "Exposure to sunlight instantly kills all organic matter",
                                "Covering prevents wind from rapidly evaporating moisture and protects the heap from heavy rainfall that would leach away soluble nutrients and cause waterlogging",
                                "Gunny sacks release carbon dioxide needed to freeze compost",
                                "Bare heaps attract wild animals that eat dry carbon leaves"
                            ],
                            "answer": "B",
                            "explanation": "Above-ground heaps lose moisture quickly to wind and sun. An insulating cover of gunny sacks or dry grass conserves internal moisture and heat while acting as an umbrella to prevent heavy rains from washing out soluble nutrients."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Innovative Composting — Vermicomposting
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Innovative Composting — Vermicomposting",
            "unit_description": "Vermicomposting biology (Red Wigglers *Eisenia fetida*), bin setup, damp paper bedding, feeding rules, worm castings nutritional advantage, migration harvest.",
            "lesson_title": "Vermiculture Engineering: Red Wiggler Biology, Bin Architecture, and Worm Castings Harvesting",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Red Wiggler Earthworms (Eisenia fetida) in Moist Compost Bedding",
                        "content": {
                            "title": "Red Wiggler Earthworms (Eisenia fetida) in Moist Compost Bedding",
                            "caption": "Active Red Wiggler earthworms (Eisenia fetida) consuming organic matter in moist shredded bedding, demonstrating vermicomposting biology."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Vermicomposting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **vermicomposting** and identify **Red Wigglers (*Eisenia fetida*)**.",
                                "Construct a vermicomposting bin with **drainage, air vents, and damp bedding**.",
                                "Formulate a **worm feeding schedule** and ban toxic citrus/onions.",
                                "Harvest **worm castings (vermicompost)** using the **Migration Method**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Vermicomposting",
                        "content": {
                            "title": "Harnessing Earthworm Digestion",
                            "text": "**Vermicomposting** is an innovative, high-efficiency biotechnology using specialized epigeic earthworm species to rapidly convert organic wastes into premium biofertilizer:\n\n- **The Master Decomposer**: Uses the **Red Wiggler (*Eisenia fetida*)**, a surface-dwelling worm that feeds voraciously on decaying vegetable waste, tolerates wide temperatures, and reproduces rapidly.\n- **Worm Castings**: The excreted digestive manure—dark, granular, odorless, and loaded with plant-available nutrients, beneficial microbes, and natural growth hormones (auxins & cytokinins)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Setting Up and Managing the Vermi-Bin",
                        "content": {
                            "title": "Creating the Ideal Worm Habitat",
                            "text": "1. **Container**: Plastic crate or wooden box with bottom drainage holes and top ventilation holes.\n2. **Moist Bedding (10–15 cm)**: Shredded newspaper, cardboard, or coconut coir soaked in water and wrung out (wrung-out sponge standard).\n3. **Stocking**: Add 0.5–1.0 kg of active Red Wigglers.\n4. **Feeding**: Raw vegetable peels, fruit scraps, crushed eggshells, coffee grounds (buried slightly under bedding).\n5. **Banned Worm Foods**: **Citrus peels (toxic limonin)**, onions, garlic, hot peppers, meats, dairy, and oils!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Vermicomposting Bin Ecosystem (Red Wigglers & Castings)",
                        "content": {
                            "title": "Vermicomposting Bin Ecosystem (Red Wigglers & Castings)",
                            "caption": "Vermi-Bin Architecture: Top Ventilation Holes -> Damp Shredded Paper Bedding -> Red Wigglers (Eisenia fetida) -> Vegetable Scrap Feeding Layer -> Dark Granular Worm Castings -> Bottom Drainage Holes (Worm Tea Collection)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Migration Harvesting Method and Nutritional Power",
                        "content": {
                            "title": "Harvesting Castings without Harming Worms",
                            "text": "- **The Migration Method**: Stop feeding for 1 week. Place fresh bedding and sweet food scraps (banana peels) on only one side of the bin. Within 4–6 days, all worms migrate to the food side, leaving pure, worm-free castings on the other side ready to scoop!\n- **Nutritional Superiority**: Worm castings contain 5x more available nitrogen, 7x more phosphorus, and 11x more potassium than standard topsoil, alongside plant growth regulators."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Vermicomposting 101: How to Set Up a Red Wiggler Worm Bin",
                        "content": {
                            "title": "Vermicomposting 101: How to Set Up a Red Wiggler Worm Bin",
                            "description": "Educational video showing container drilling, damp paper bedding preparation, stocking Red Wigglers, feeding protocols, and harvesting pure castings.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Laboratory Practical: Setting Up a 50L Classroom Vermicomposting Unit",
                        "content": {
                            "title": "Classroom Vermi-Bin Setup Practicum",
                            "task": "1. Drill 10 base drainage holes and 15 lid air holes in a plastic bin.\n2. Shred newspapers, soak in water, and wring out to form a 15cm damp bedding.\n3. Introduce 200 Red Wigglers.\n4. Add 1 cup of chopped fruit peels and cover with damp cardboard.",
                            "materials": ["50L Plastic Bin", "Drill", "Shredded Newspaper", "Water", "Red Wigglers", "Kitchen Scraps"],
                            "safety": "Keep bin in shaded, cool indoor area away from direct sunlight."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Vermicomposting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Red Wigglers (*Eisenia fetida*) are the premier composting worms**.\n- **Bedding must remain moist like a wrung-out sponge at neutral pH**.\n- **Never feed worms citrus peels, onions, meat, or oily foods**.\n- **Worm castings are rich in bio-available NPK and root hormones**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Diagnosing Worm Bin Escape",
                        "content": {
                            "question": "A student observes that several Red Wiggler worms are crawling up the bin walls and trying to escape. The bedding smells strongly of sour onions and citrus peels and is bone dry. What is the cause and remedy?",
                            "options": [
                                "Worms naturally escape during full moons; no action needed",
                                "The bin environment has become toxic due to dehydration and acidic toxic foods (citrus/onions); replace with fresh damp neutral bedding and remove acidic foods",
                                "The worms are seeking sunlight to warm their blood",
                                "The bin is too cold; place it over a fire"
                            ],
                            "answer": "B",
                            "explanation": "Earthworms breathe through moist skin. Dry bedding suffocates them, and acidic foods like citrus (containing limonin) and onions irritate their skin, making the environment lethal and forcing worms to escape."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Innovative Composting — Containerized (Bin) Composting
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Innovative Composting — Containerized (Bin) Composting",
            "unit_description": "Upcycled bin/tumbler designs, ventilation/drainage holes, conventional vs innovative comparison matrix.",
            "lesson_title": "Urban Agri-Tech: Containerized Composting, Upcycled Tumblers, and Space Optimization",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Plastic Garden Container Compost Bin for Smallholder and Urban Composting",
                        "content": {
                            "title": "Plastic Garden Container Compost Bin for Smallholder and Urban Composting",
                            "caption": "A compact, enclosed plastic composting container installed on a small plot, demonstrating neat, pest-proof urban waste recycling."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Containerized Composting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Define **containerized (bin) composting** for urban and space-constrained areas.",
                                "Construct an **upcycled composting tumbler** from plastic drums or buckets.",
                                "Manage aeration and drainage inside enclosed composting bins.",
                                "Compare **conventional pit/heap methods against innovative containerized systems**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is Containerized Composting?",
                        "content": {
                            "title": "Composting in Urban Spaces and Balconies",
                            "text": "**Containerized composting** (or bin composting) uses enclosed physical containers to manage decomposition in urban gardens, paved school compounds, or residential estates where open heaps are unfeasible:\n\n- **Upcycling Materials**: Fabricated from perforated plastic drums, wooden pallets, wire mesh cylinders, or 20L paint buckets.\n- **Advantages**: Highly contained, odor-controlled, pest-proof, retains heat exceptionally well, and operates directly on paved concrete surfaces!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Operating Bins and Rotating Tumblers",
                        "content": {
                            "title": "Managing Enclosed Composting Units",
                            "text": "1. **Ventilation & Drainage**: Drill 1.5–2.0 cm air holes around sides and drainage holes in base.\n2. **Layering Balance**: Load with 3 parts carbon browns (shredded cardboard/dry leaves) to 1 part green kitchen waste.\n3. **Aeration via Tumbling**: Use a rotating **compost tumbler** (drum on a stand) rolled twice weekly to aerate without shovels.\n4. **Base Harvest Door**: High-efficiency bins feature a lower sliding trapdoor to harvest mature compost from the bottom while fresh waste decays at top."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Conventional vs Innovative Composting Methods Matrix",
                        "content": {
                            "title": "Composting Methods Comparison",
                            "headers": ["Parameter", "Conventional Pit / Heap Methods", "Innovative Vermi / Containerized Systems"],
                            "rows": [
                                ["Space Footprint", "Large open land required (Farm fields)", "Ultra-compact (Fits balconies, courtyards, indoors)"],
                                ["Initial Setup Cost", "Zero (Only manual tools to dig/pile)", "Low to Moderate (Cost of bins, worms, drums)"],
                                ["Labor Demand", "High (Heavy manual shoveling to turn pits)", "Very Low (Simple rolling tumbler or worm activity)"],
                                ["Decomposition Speed", "3 to 6 months (Climate dependent)", "Fast: 4 to 8 weeks (High microbial control)"],
                                ["Nutrient Density", "Standard organic compost manure", "Exceptional (Ultra-concentrated castings & humus)"],
                                ["Aesthetics & Hygiene", "Can attract flies/pests if open", "Neat, pest-proof, completely odorless"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Engineering Practical: Prototyping an Upcycled 20L Bucket Compost Tumbler",
                        "content": {
                            "title": "DIY Compost Tumbler Lab",
                            "task": "1. Clean an empty 20L paint bucket.\n2. Drill 20 air holes around upper sides and 5 drainage holes at base.\n3. Load with chopped dry grass and kitchen peels (3:1 ratio).\n4. Roll bucket on ground for 1 minute twice weekly to aerate.",
                            "materials": ["20L Bucket with Lid", "Drill / Hot Nail", "Organic Waste"],
                            "safety": "Ensure adult supervision when using electric drills or hot nails."
                        }
                    }
                ],
                [
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Containerized Composting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Containerized composting thrives on paved and urban concrete sites**.\n- **Rotating tumblers eliminate heavy manual shoveling**.\n- **Enclosed bins are pest-proof and odor-controlled**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Choosing Method for Concrete Courtyards",
                        "content": {
                            "question": "An urban school has 100% concrete courtyards and zero open soil. The school wishes to recycle food waste from the student cafeteria into organic manure. Which composting method should the agriculture teacher choose?",
                            "options": [
                                "Below-ground Four-Pit Composting Method",
                                "Open un-contained farmyard heap",
                                "Innovative Containerized Tumbler / Bin Composting",
                                "Forest leaf litter degradation"
                            ],
                            "answer": "C",
                            "explanation": "Pits require open soil to dig, and open heaps leach dark runoff onto concrete surfaces. Containerized bin systems are self-contained, sit cleanly on concrete, contain odors, and prevent pests, making them ideal for urban paved compounds."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: The Role of Composting in Soil Improvement
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "The Role of Composting in Soil Improvement",
            "unit_description": "Physical conditioning (aggregating clay, increasing sandy water-holding), chemical benefits (CEC negative charge, nutrient storage, pH buffering), biological vitality (microbes, mycorrhizae, earthworms).",
            "lesson_title": "Soil Science Dynamics: Physical Conditioning, Cation Exchange Capacity (CEC), and Living Soil Ecosystems",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Fertile Humus-Rich Agricultural Soil Held in Farmer Hands",
                        "content": {
                            "title": "Fertile Humus-Rich Agricultural Soil Held in Farmer Hands",
                            "caption": "Dark, crumbly, fertile topsoil rich in humus and organic matter, demonstrating aggregate structure and enhanced soil health."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Role of Compost in Soil Improvement",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how compost improves the **physical structure of clay and sandy soils**.",
                                "Analyze the chemical benefits of **Cation Exchange Capacity (CEC) and pH buffering**.",
                                "Describe the **biological role of humus in feeding soil microbes and mycorrhizae**.",
                                "Evaluate why organic compost prevents nutrient leaching."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Physical Soil Structure Transformation",
                        "content": {
                            "title": "Conditioning Both Sand and Clay",
                            "text": "Compost fundamentally transforms the physical physics of agricultural soils:\n\n- **In Sandy Soils**: Sandy soils have huge pores and poor water retention, causing water and nutrients to drain away instantly. Compost acts like a microscopic sponge, binding sand grains together and boosting water-holding capacity by up to $300\\%$.\n- **In Heavy Clay Soils**: Clay soils are compact, heavy, and easily waterlogged. Compost breaks up tight clay plates, forming loose, crumbly soil aggregates that improve aeration and root penetration."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Chemical Soil Fertility & Cation Exchange Capacity (CEC)",
                        "content": {
                            "title": "The Soil's Electrical Nutrient Bank",
                            "text": "- **Cation Exchange Capacity (CEC)**: Humus particles in compost carry high **negative electrical charges**. These charges act like microscopic magnets, attracting and securely holding positively charged nutrient cations ($Ca^{2+}, Mg^{2+}, K^{+}, NH_4^{+}$), preventing them from being washed away (leached) during heavy rains!\n- **pH Buffering**: Compost naturally stabilizes soil pH toward the neutral 6.0–7.0 zone, preventing nutrient lockout in acidic soils.\n- **Complete Micro-Nutrition**: Supplies essential trace minerals (Zinc, Boron, Copper, Iron, Manganese) absent in standard synthetic fertilizers."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Soil Structure Transformation: Before vs After Compost Addition",
                        "content": {
                            "title": "Soil Structure Transformation: Before vs After Compost Addition",
                            "caption": "Soil Structure Transformation: Before Compost (Compact Cracking Clay / Water-Draining Sand, Stunted Roots) vs After Compost (Rich Crumbly Porous Humus Aggregates, High Water-Holding, Massive Deep Root System)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biological Soil Vitality & Living Ecosystems",
                        "content": {
                            "title": "Feeding the Underground Soil Food Web",
                            "text": "Compost transforms dead dirt into a thriving living ecosystem:\n- **Microbial Inoculation**: Introduces and feeds billions of beneficial bacteria, actinomycetes, and mycorrhizal fungi.\n- **Mycorrhizal Networks**: Symbiotic fungi weave through plant roots, extending their reach to absorb phosphorus and water from deep soil zones.\n- **Earthworm Habitat**: Attracts deep-burrowing earthworms that aerate the soil profile and excrete nutrient-rich castings."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Soil Improvement Mechanisms of Organic Compost",
                        "content": {
                            "title": "Physical, Chemical, and Biological Benefits",
                            "headers": ["Domain", "Mechanism of Action", "Agronomic Benefit to Crops"],
                            "rows": [
                                ["Physical", "Aggregate formation & sponge humus", "Increases drought tolerance in sand; improves drainage in clay"],
                                ["Chemical", "High negative surface charge (High CEC)", "Prevents nutrient leaching; securely stores K+, Ca2+, Mg2+"],
                                ["Chemical", "Natural pH buffering capacity", "Stabilizes pH at 6.0–7.0, unlocking fixed soil Phosphorus"],
                                ["Biological", "Provides carbon food for soil microbes", "Stimulates mycorrhizae fungi and natural disease suppression"],
                                ["Biological", "Attracts earthworm populations", "Continuous biological aeration and soil profile mixing"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Soil Lab Practicum: Water-Holding Capacity Comparison (Sand vs Compost-Sand)",
                        "content": {
                            "title": "Soil Water Retention Practicum",
                            "task": "1. Fill Funnel A with 100g pure sand.\n2. Fill Funnel B with 50g sand + 50g sifted mature compost.\n3. Pour 100ml water into each.\n4. Measure drainage water collected in measuring cylinders after 5 minutes.\n5. Calculate percentage water retained.",
                            "materials": ["Funnels", "Filter Paper", "Sand", "Compost", "Measuring Cylinders", "Water"],
                            "safety": "Handle glassware carefully."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Soil Improvement",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Compost loosens clay and increases water retention in sand**.\n- **High CEC magnetically holds plant nutrients to stop leaching**.\n- **Humus buffers soil pH to neutral (6.0–7.0)**.\n- **Feeds mycorrhizal fungi and earthworms for living soil health**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Humus as a Nutrient Bank",
                        "content": {
                            "question": "Why is organic compost referred to as a 'chemical buffering agent' and an 'electrical nutrient bank' in agricultural soil science?",
                            "options": [
                                "It increases the speed of wind erosion across sandy fields",
                                "It sterilizes soil bacteria to stop organic decay",
                                "It stabilizes soil pH toward neutral, and its high negative Cation Exchange Capacity (CEC) electrically attracts and stores essential nutrient cations, preventing leaching",
                                "It converts chemical fertilizers into insoluble stones"
                            ],
                            "answer": "C",
                            "explanation": "Compost contains humus with a high Cation Exchange Capacity (CEC). Its strong negative electrical charges bind positively charged nutrient cations (K+, Ca2+, Mg2+, NH4+), preventing them from leaching into groundwater while stabilizing soil pH."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Practical Field Application, Advocacy & Topic Review
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Practical Field Application, Advocacy & Topic Review",
            "unit_description": "Application methods (incorporation, sidedressing ring/band, potting mix 1:2:1), application rate calculations (kg/m2), circular economy advocacy, 8 Summative MCQs.",
            "lesson_title": "Field Deployment & Circular Stewardship: Application Methods, Dosage Mathematics, and Summative Review",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Farmer Applying Mature Organic Compost Manure to Vegetable Garden Bed",
                        "content": {
                            "title": "Farmer Applying Mature Organic Compost Manure to Vegetable Garden Bed",
                            "caption": "Applying and incorporating rich organic compost into a crop seedbed, demonstrating field application and agronomic dosage."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Application, Advocacy & Review",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Master the 3 primary application methods: **Incorporation, Sidedressing, and Potting Blends (1:2:1)**.",
                                "Calculate **exact compost application weights ($kg/m^2$)** for garden beds.",
                                "Advocate for the **Circular Economy and Organic Soil Stewardship**.",
                                "Complete the comprehensive **Summative Topic Assessment**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Methods of Applying Compost to Crops",
                        "content": {
                            "title": "Field Delivery Techniques",
                            "text": "1. **Incorporation (Broadcasting & Tilling)**: Spreading compost evenly across the field surface and tilling it into the top 10–15 cm of soil during secondary land preparation before planting.\n2. **Sidedressing (Ring & Band Placement)**: Applying compost around existing, growing crops. Placed in a circular ring 10 cm from the plant stem along the drip line, or along crop rows, and lightly worked into the soil.\n3. **Potting Mix Formulation**: Mixing sifted mature compost with clean topsoil and coarse sand in a **1:2:1 volume ratio** for nursery seedling trays, potting bags, or sack gardens."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Application Dosage Mathematics",
                        "content": {
                            "title": "Calculating Field Compost Requirements",
                            "text": "- **Standard Agronomic Rate**: General vegetable beds require **5 to 10 kg of mature compost per square meter ($m^2$)** (equivalent to 50–100 tonnes/ha).\n- **Bed Calculation Formula**:\n  $$\\text{Bed Area} = \\text{Length (m)} \\times \\text{Width (m)}$$\n  $$\\text{Total Compost (kg)} = \\text{Area} (m^2) \\times \\text{Rate} (kg/m^2)$$\n- *Example*: For an 8m x 2m bed at 6 kg/$m^2$:\n  $$\\text{Area} = 8.0 \\times 2.0 = 16.0 \\text{ m}^2$$\n  $$\\text{Total Compost} = 16.0 \\times 6 = 96.0 \\text{ kg}$$"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Composting Techniques & Organic Soil Management Lifecycle",
                        "content": {
                            "title": "Master Composting Techniques & Organic Soil Management Lifecycle",
                            "caption": "Master Organic Management Lifecycle: 1 Organic Farm Waste Segregation -> 2 Siting & 30:1 C:N Balancing -> 3 Method Execution (Four-Pit, Heap, Vermi, Container) -> 4 Aerobic Thermophilic Pasteurization -> 5 Maturity Testing -> 6 Field Incorporation & Circular Wealth."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Composting in the Circular Economy and Ecological Stewardship",
                        "content": {
                            "title": "Closing the Agricultural Nutrient Loop",
                            "text": "- **Zero-Waste Circular Agriculture**: Composting diverts organic waste from dumpsites, eliminating anaerobic methane greenhouse gas emissions while recycling essential plant nutrients back into the soil.\n- **Farm Economic Independence**: Self-made compost drastically cuts reliance on expensive imported synthetic fertilizers, keeping farm profits in local communities.\n- **Biodiversity Conservation**: Organic manures nurture earthworms and mycorrhizal networks, safeguarding soil resilience against climate extremes."
                        }
                    },
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The 'Wanjiku Compost Pit Remediation Challenge'",
                        "content": {
                            "title": "Wanjiku Compost Pit Remediation Practicum",
                            "task": "Farmer Wanjiku loaded a pit with raw chicken manure, kitchen scraps, and stale bread, watered it daily in flat clay soil, and got a cold, smelly, black sludge with flies.\n1. Identify 3 critical scientific mistakes.\n2. Diagnose the microbial cause of the rotten egg odor.\n3. Formulate a 6-step Compost Recovery Action Plan (mixing browns, coarse base, ash, turning schedule).",
                            "materials": ["Case Handout", "Notebook", "Pen"],
                            "safety": "Ensure rigorous biochemical problem solving."
                        }
                    }
                ],
                # Pages 4 to 7: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Biological Definition and Aerobic Respiration",
                        "content": {
                            "question": "What is the primary biological difference between controlled aerobic composting and uncontrolled open waste rotting?",
                            "options": [
                                "Aerobic composting uses beneficial oxygen-breathing microorganisms that convert organic matter into heat, water, and stable humus without foul gases, whereas anaerobic rotting lacks oxygen and produces methane and foul hydrogen sulfide",
                                "Composting freezes organic waste to prevent decay",
                                "Uncontrolled rotting requires adding synthetic urea",
                                "Aerobic composting converts plant matter into plastic"
                            ],
                            "answer": "A",
                            "explanation": "Aerobic composting relies on oxygen-breathing bacteria and fungi that efficiently break down organic matter into stable humus and heat. In the absence of oxygen, anaerobic microbes take over, producing noxious gases like methane and foul hydrogen sulfide (rotten eggs)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: The 30:1 C:N Ratio Golden Rule",
                        "content": {
                            "question": "Why is an initial Carbon-to-Nitrogen (C:N) ratio of 30:1 considered the optimal standard for rapid, high-temperature composting?",
                            "options": [
                                "It provides 30 parts of water to 1 part of soil",
                                "Microorganisms require 30 parts of carbon for cellular energy to every 1 part of nitrogen for protein synthesis and rapid population reproduction",
                                "Carbon creates toxic acid that speeds up burning",
                                "Nitrogen is poisonous to bacteria in large amounts"
                            ],
                            "answer": "B",
                            "explanation": "Microorganisms use carbon as their primary energy fuel for respiration, and nitrogen to build cellular proteins and multiply. A 30:1 C:N ratio supplies the exact biological balance needed for rapid microbial multiplication and fast heating."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Thermophilic Temperature Pasteurization",
                        "content": {
                            "question": "What critical agronomic benefit occurs when a compost pile enters the thermophilic stage (55°C to 65°C)?",
                            "options": [
                                "The heat melts rocks into liquid minerals",
                                "The high temperature pasteurizes the pile, destroying weed seeds, fungal spores (e.g. blight), and enteric pathogens (e.g. E. coli)",
                                "The heat turns all carbon into nitrogen gas",
                                "The pile freezes solid, halting all microbial decay"
                            ],
                            "answer": "B",
                            "explanation": "Temperatures between 55°C and 65°C kill harmful plant pathogens (like tomato bacterial wilt), enteric bacteria from manure (like E. coli), and weed seeds, ensuring the resulting organic manure is clean and safe for field crops."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Layering Architecture in the Four-Pit System",
                        "content": {
                            "question": "Why is a 15–20 cm layer of coarse, woody twigs and maize stalks always placed at the very bottom of Pit 1 before adding fine leaves and kitchen greens?",
                            "options": [
                                "To attract termites that eat the wood",
                                "To create an open drainage foundation that prevents waterlogging and allows fresh air to circulate into the base of the pile",
                                "To prevent earthworms from entering the pit",
                                "To make the pit shallow and easy to harvest"
                            ],
                            "answer": "B",
                            "explanation": "Coarse woody residues at the base act as a biological ventilator. They create open pore spaces that facilitate drainage of excess moisture and allow fresh oxygen to enter the bottom of the pile, maintaining aerobic conditions."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Red Wiggler Earthworm Species in Vermicomposting",
                        "content": {
                            "question": "Which earthworm species is the premier choice for innovative vermicomposting bins due to its surface-dwelling habits and voracious appetite for organic waste?",
                            "options": [
                                "Common Deep Burrowing Earthworm (Lumbricus terrestris)",
                                "Red Wiggler Earthworm (Eisenia fetida)",
                                "African Giant Snail (Achatina fulica)",
                                "Tapeworm (Taenia solium)"
                            ],
                            "answer": "B",
                            "explanation": "The Red Wiggler (Eisenia fetida) is an epigeic (surface-dwelling) earthworm that thrives in decaying organic matter, tolerates high stocking densities and fluctuating temperatures, and reproduces rapidly, producing nutrient-dense worm castings."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Cation Exchange Capacity (CEC) in Soil Chemistry",
                        "content": {
                            "question": "How does adding mature compost improve the chemical fertility of sandy soils prone to severe nutrient leaching?",
                            "options": [
                                "Compost increases the speed at which rainwater washes nutrients into deep aquifers",
                                "Humus particles in compost carry high negative electrical charges (high CEC) that attract and securely hold positively charged nutrient cations (K+, Ca2+, Mg2+, NH4+), preventing leaching",
                                "Compost turns sandy soils into pure sulfuric acid",
                                "Compost eliminates all chemical elements from the soil"
                            ],
                            "answer": "B",
                            "explanation": "Humus particles have a high Cation Exchange Capacity (CEC) with abundant negative surface charges. These act as microscopic magnets that bind essential positively charged nutrient cations, holding them securely in the root zone against rainwater leaching."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Compost Application Rate Calculation",
                        "content": {
                            "question": "A student group is preparing a 6.0m long by 1.5m wide raised garden bed for spinach. If the recommended compost application rate is 8.0 kg per square meter, what is the total weight of mature compost required?",
                            "options": [
                                "9.0 kilograms",
                                "72.0 kilograms",
                                "48.0 kilograms",
                                "120.0 kilograms"
                            ],
                            "answer": "B",
                            "explanation": "Bed Area = 6.0m x 1.5m = 9.0 m^2. Total Compost = 9.0 m^2 x 8.0 kg/m^2 = 72.0 kg of mature compost."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Formulating Nursery Potting Soil Blends",
                        "content": {
                            "question": "What is the standard, agronomically recommended volumetric ratio for blending mature sifted compost, clean topsoil, and coarse sand to fill seedling nursery trays?",
                            "options": [
                                "10 parts compost : 1 part sand : 0 parts topsoil",
                                "1 part compost : 2 parts topsoil : 1 part sand (1:2:1 ratio)",
                                "5 parts compost : 5 parts pure chemical fertilizer",
                                "1 part compost : 10 parts ash"
                            ],
                            "answer": "B",
                            "explanation": "A 1:2:1 volume blend (1 part mature compost, 2 parts clean fertile topsoil, and 1 part coarse sand) creates the ideal potting medium, offering balanced moisture retention, fertility, and porous root aeration for young seedlings."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 17 Capstone Summary: Composting Techniques Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Composting Techniques",
                            "text": "Congratulations on mastering **Topic 17: Composting Techniques**!\n\nYou have mastered:\n- **Biological Decomposition**: Controlled aerobic breakdown converting raw waste into nutrient-dense, dark, crumbly organic manure.\n- **Quality Drivers**: Maintaining a 30:1 C:N ratio, 50–60% moisture (sponge test), regular aeration, and sanitizing thermophilic heat (55–65°C).\n- **Conventional Systems**: Designing and layering the Four-Pit System (1.2m x 1.2m x 1.2m) with coarse drainage bases and executing 12-week shifting schedules; constructing ventilated above-ground stacks with protective gunny sack covers.\n- **Innovative Agri-Tech**: Vermicomposting with Red Wigglers (*Eisenia fetida*) for high-potency worm castings; building upcycled containerized tumblers for urban and paved spaces.\n- **Soil Science Transformation**: Conditioning clay aggregates and sandy water retention; boosting Cation Exchange Capacity (CEC) to stop nutrient leaching; fostering mycorrhizal networks and earthworms.\n- **Field Deployment & Agronomic Calculations**: Calculating exact compost dosages ($kg/m^2$), sidedressing growing crops, blending 1:2:1 potting soil, and driving circular agricultural stewardship."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 17 Final Takeaway & Grade 10 Agriculture Milestone",
                        "content": {
                            "title": "The Organic Soil Stewardship Maxim",
                            "text": "Feed the soil, and the soil will feed the crop. Composting closes the agricultural nutrient loop, turning zero-cost organic wastes into living soil fertility. By mastering composting alongside all 17 topics of Grade 10 Agriculture, you have built the scientific knowledge, technical skills, and entrepreneurial mindset to transform agriculture into a sustainable, climate-smart, and highly profitable enterprise."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic17(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 17: Composting."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 17: Composting")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Composting"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive vocational, scientific, and practical mastery in composting techniques: aerobic biological decomposition, C:N ratios and moisture optimization, siting and material preparation, the Four-Pit conventional system and shifting schedules, above-ground stack composting, innovative vermicomposting with Red Wigglers (Eisenia fetida), containerized urban tumblers, physical and chemical soil conditioning (CEC), and field dosage applications.",
            order=17
        )
        print(f"Created Topic 17: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 17
        topic.description = "Comprehensive vocational, scientific, and practical mastery in composting techniques: aerobic biological decomposition, C:N ratios and moisture optimization, siting and material preparation, the Four-Pit conventional system and shifting schedules, above-ground stack composting, innovative vermicomposting with Red Wigglers (Eisenia fetida), containerized urban tumblers, physical and chemical soil conditioning (CEC), and field dosage applications."
        topic.save()
        print(f"Resolved Topic 17: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 17...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic17_curriculum()
    total_units = 0
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    for item in curriculum_data:
        u_order = item["unit_order"]
        u_name = item["unit_name"]
        u_desc = item["unit_description"]
        l_title = item["lesson_title"]
        pages = item["pages"]

        unit, u_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not u_created:
            unit.name = u_name
            unit.description = u_desc
            unit.save()
        total_units += 1

        lesson, l_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": l_title,
                "status": "published",
                "version": 1,
                "immutable_metadata": {
                    "author": "VLearn Senior Curriculum Agent",
                    "grade": "Grade 10",
                    "subject": "Agriculture",
                    "topic_order": 17,
                    "unit_order": u_order
                }
            }
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

        lesson.blocks.all().delete()
        total_lessons += 1

        block_order_counter = 1
        for page_idx, page_blocks in enumerate(pages, start=1):
            total_pages += 1
            for comp_idx, block_def in enumerate(page_blocks, start=1):
                b_type = block_def["type"]
                b_title = clean_text(block_def.get("title", ""))
                b_content = clean_dict(block_def.get("content", {}))

                LessonBlock.objects.create(
                    lesson=lesson,
                    block_id=f"g10_agri_t17_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 17, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 17 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic17(replace=replace_flag)
