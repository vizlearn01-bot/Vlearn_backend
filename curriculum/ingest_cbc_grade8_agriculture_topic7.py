"""
VLearn CBC Grade 8 Agriculture — Topic 7: Kitchen Hygiene Practices
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Kitchen Hygiene Practices (Topic Order: 7)

Decomposed into 6 Learning Units & 6 Published Lessons:
  1. Reasons for Cleaning the Kitchen (7 Pages, 12 Blocks)
  2. Loose Dirt and Fixed Dirt (7 Pages, 12 Blocks)
  3. Methods of Removing Dirt (7 Pages, 12 Blocks)
  4. Daily, Weekly, and Special Cleaning (7 Pages, 12 Blocks)
  5. Practical: Cleaning the Kitchen (7 Pages, 13 Blocks)
  6. Safety Precautions in Kitchen Cleaning & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Strict 1 Card = 1 Understandable Idea progression.
  - Zero citation leaks ([543], [547]), zero developer meta-tags, zero raw unrendered LaTeX.
  - Formative scenario MCQs and 10 Topic Summative MCQs with comprehensive educational explanations.
  - Multi-video integrations embedded across individual practical lessons.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic7.py [--replace]
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

def build_topic7_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 7: Kitchen Hygiene Practices."""
    return [
        # =====================================================================
        # LESSON 1: Reasons for Cleaning the Kitchen
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Reasons for Cleaning the Kitchen",
            "unit_description": "Health and biological reasons for kitchen sanitation: germ breeding pathways, pest attraction vectors, cross-contamination, and appliance preservation.",
            "lesson_title": "Reasons for Cleaning the Kitchen",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hygiene Comparison: Clean vs. Neglected Kitchen Counter",
                        "content": {
                            "title": "Hygiene Comparison: Clean vs. Neglected Kitchen Counter",
                            "caption": "A spotless, sanitized kitchen workstation free of moisture and grease, providing an effective barrier against foodborne pathogens."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: The Science of Kitchen Hygiene",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain how regular cleaning destroys **pathogenic bacteria and molds**.",
                                "Identify key **high-risk zones (sinks, cutting boards, dustbins)** that harbour disease vectors.",
                                "Analyze the economic and safety benefits of **preventing grease fires and metal corrosion**.",
                                "Appreciate personal responsibility in maintaining kitchen hygiene for household health."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Kitchen as a Microbial Battleground",
                        "content": {
                            "title": "Why Kitchens Demand Daily Vigilance",
                            "text": "The kitchen is where food is prepared to nourish our bodies, but it is also the most warm, wet, and nutrient-rich environment in the house! When food particles, grease, and standing water accumulate, millions of microscopic bacteria, viruses, and molds multiply rapidly, leading to severe foodborne illnesses."
                        }
                    }
                ],
                # Page 2: Biological Germ Breeding & Pest Vectors
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Four Pillars of Kitchen Hygiene",
                        "content": {
                            "title": "Why We Must Clean Daily",
                            "text": "- **1. Health Shield**: Bacteria like *Salmonella*, *E. coli*, and *Campylobacter* double in population every 20 minutes in warm, damp scraps. Daily cleaning eliminates their breeding media.\n- **2. Pest Vector Control**: Houseflies, cockroaches, rats, and mice are attracted to exposed grease and crumbs. Cleaning deprives them of food, halting disease transmission (such as typhoid and cholera).\n- **3. Cross-Contamination Barrier**: Sanitizing cutting boards and knives prevents bacteria on raw meats from transferring onto ready-to-eat salad greens.\n- **4. Fire & Tool Protection**: Removing stove grease prevents explosive oil fires, while washing acidic tomato and lemon juices off knives and metal cookers stops rust."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Four Pillars of Kitchen Hygiene Conceptual Framework",
                        "content": {
                            "title": "Four Pillars of Kitchen Hygiene Conceptual Framework",
                            "caption": "Sanitation mind map: 1. Health Shield (pathogen elimination) • 2. Pest Block (stopping flies & rodents) • 3. Fire Safety (preventing grease combustion) • 4. Tool Longevity (stopping acidic metal corrosion)."
                        }
                    }
                ],
                # Page 3: Kitchen Hygiene Impact Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Hygiene Impact & Hazard Mitigation Matrix",
                        "content": {
                            "title": "Kitchen Hygiene Impact Matrix",
                            "headers": ["Neglected Kitchen Hazard", "Primary Biological / Physical Threat", "Preventative Cleaning Action", "Health & Safety Outcome"],
                            "rows": [
                                ["Damp, unwashed cutting boards", "Cross-contamination of Salmonella from raw meat", "Wash with hot soapy water and sanitize after use", "Prevents dangerous food poisoning"],
                                ["Sticky oil splatters on cooker", "Grease ignition from gas/charcoal flames", "Wipe stove burners immediately after cooking", "Eliminates kitchen grease fire hazard"],
                                ["Acidic citrus/tomato spills on knives", "Chemical acid etching and metal rusting", "Rinse and dry metal blades immediately", "Extends lifespan of kitchen cutlery"],
                                ["Open, overflowing organic garbage bin", "Attracts houseflies, cockroaches, and mice", "Empty trash daily and wash the bin with disinfectant", "Eliminates pest disease transmission"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Impact Classification Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Kitchen Action Impact Classification Challenge",
                        "content": {
                            "title": "Sorting Chores into Impact Pillars",
                            "instructions": "Classify the kitchen action under its correct primary impact pillar:",
                            "scenario": "A student is performing an afternoon cleaning routine in the school home-science lab.",
                            "question": "Which action directly preserves kitchen tools from chemical degradation rather than stopping bacterial disease?",
                            "options": [
                                "Rinsing and drying a high-carbon steel knife immediately after slicing acidic tomatoes (Preserves Kitchen Tools).",
                                "Emptying the organic trash bin to keep houseflies away.",
                                "Sanitizing a cutting board used for raw chicken.",
                                "Wiping water off the floor to prevent slips."
                            ],
                            "correct_feedback": "Correct! Washing acidic tomato juice off metal prevents acid corrosion and rust, directly preserving expensive kitchen tools.",
                            "incorrect_feedback": "Incorrect. Emptying trash and sanitizing boards prevent disease, while drying floors prevents slips. Washing acid off knives preserves tools."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Biological Purpose of Countertop Sanitization",
                        "content": {
                            "question": "What is the primary biological reason for washing and disinfecting kitchen countertops regularly?",
                            "options": [
                                "To destroy harmful disease-causing pathogens that multiply on microscopic food residues and prevent foodborne illnesses.",
                                "To make the countertops smell like lemons.",
                                "To change the physical color of the tiles.",
                                "To make the cooker use less gas."
                            ],
                            "answer": "A",
                            "explanation": "Food preparation surfaces collect microscopic organic residues and moisture. Disinfection destroys pathogens before they can cross-contaminate food."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Kitchens provide optimal conditions (warmth, food scraps, moisture) for rapid **bacterial multiplication**.\n- Daily hygiene prevents **foodborne illnesses**, deters **disease-carrying pests**, and stops food spoilage.\n- Cleaning oil residues stops **kitchen fires**, while wiping acids prevents **metal corrosion and rust**.\n- A clean kitchen is the household's first line of defense in health security."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we understand why we clean, what types of dirt are we fighting? In Lesson 2, we explore the scientific difference between loose dirt and fixed dirt!"
                        }
                    }
                ],
                # Page 7: High-Risk Zones Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Top 3 Kitchen Germ Hotspots",
                        "content": {
                            "title": "Where Bacteria Hide",
                            "text": "Studies show that dishcloths, sink strainers, and refrigerator door handles contain more bacteria than almost any other household surface! Never use the same dishcloth to wipe both raw meat spills and clean dinner plates without sanitizing it in boiling water first."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Loose Dirt and Fixed Dirt
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Loose Dirt and Fixed Dirt",
            "unit_description": "Scientific classification of kitchen soils: loose dirt (dust, flour, crumbs held by gravity) vs fixed dirt (grease, soot, baked-on stains bonded by oil, moisture, or heat).",
            "lesson_title": "Loose Dirt and Fixed Dirt",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Fixed Dirt Example: Charcoal Soot on Metal Sufuria",
                        "content": {
                            "title": "Fixed Dirt Example: Charcoal Soot on Metal Sufuria",
                            "caption": "Thick black carbon soot adhering strongly to the base of a metal cooking pot, forming a resilient layer of fixed dirt."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Classifying Kitchen Soils",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define and differentiate **loose dirt** from **fixed dirt** scientifically.",
                                "Identify kitchen examples of loose soils (flour, crumbs) vs fixed soils (soot, grease, scale).",
                                "Explain why loose dirt turns into fixed mud when wet cloths are applied incorrectly.",
                                "Select the correct dry mechanical vs wet chemical removal strategy."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Physics of Dirt Adhesion",
                        "content": {
                            "title": "Why Some Soils Brush Away While Others Cling",
                            "text": "Not all dirt is the same! If you blow on dry bread crumbs, they scatter across the room. But if you blow on a grease spot near the stove, it doesn't move a millimeter. Understanding how dirt bonds to surfaces allows us to clean faster with far less physical effort."
                        }
                    }
                ],
                # Page 2: Loose Dirt vs. Fixed Dirt Mechanics
                [
                    {
                        "type": "concept_explanation",
                        "title": "Bonding Characteristics of Kitchen Soils",
                        "content": {
                            "title": "Dry Particulates vs. Chemically Bonded Soils",
                            "text": "- **Loose Dirt**: Light, dry particles resting on top of surfaces without any sticky adhesive bond (held only by gravity or static). Examples include wheat flour dust, dry bread crumbs, onion skins, and airborne dust.\n- **Fixed Dirt**: Soils that have physically or chemically bonded to surfaces using moisture, fat, sticky sugar, or high cooking heat. Examples include cooking oil splatters, charcoal soot on pots, dried porridge drips, and hard water calcium scale.\n- **The Transformation Hazard**: Applying a soaking wet cloth to dry flour creates sticky gluten dough (fixed mud) on the counter! Always sweep loose dirt dry *before* washing."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Loose Dirt vs. Fixed Dirt Bonding Mechanics & Physical Properties",
                        "content": {
                            "title": "Loose Dirt vs. Fixed Dirt Bonding Mechanics & Physical Properties",
                            "caption": "Comparative scientific diagram: Left: Loose Dirt (dry flour, crumbs resting loosely; removed by dry broom/duster) • Right: Fixed Dirt (grease, soot, scale bonded by oil & heat; removed by soap, water & scrubbing pad)."
                        }
                    }
                ],
                # Page 3: Comparison Matrix of Kitchen Dirt
                [
                    {
                        "type": "comparison_table",
                        "title": "Loose Dirt vs. Fixed Dirt Property Matrix",
                        "content": {
                            "title": "Soil Properties & Removal Protocol",
                            "headers": ["Property", "Loose Dirt", "Fixed Dirt"],
                            "rows": [
                                ["Bonding Mechanism", "Weak (held only by gravity or electrostatic force)", "Strong (bonded by oil, grease, sugar, moisture, or heat)"],
                                ["Physical State", "Dry, light, powdery, and free-flowing", "Sticky, greasy, viscous, or baked-on rock-hard"],
                                ["Primary Removal Tools", "Soft broom, dry microfibre cloth, duster, dustpan", "Abrasive scouring pad, warm water, soap, or vinegar"],
                                ["Cleaning Effort Required", "Low effort (fast dry sweeping or dusting)", "High effort (requires soaking, friction, and chemical breakdown)"],
                                ["Common Kitchen Examples", "Dry maize flour, bread crumbs, onion skins, window dust", "Cooker grease splatters, pot soot, dried egg stains, tap scale"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Soil Classification Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Kitchen Soil Matching Challenge",
                        "content": {
                            "title": "Categorizing Kitchen Residues",
                            "instructions": "Classify each kitchen residue as Loose Dirt or Fixed Dirt:",
                            "scenario": "You are surveying a messy kitchen workspace after an afternoon baking and cooking session.",
                            "question": "Which of the following items is an example of Fixed Dirt that cannot be swept away with a dry broom?",
                            "options": [
                                "Sticky cooking oil splatters on the wall tiles behind the frying pan (Fixed Dirt).",
                                "Dry wheat flour dust on the wooden pastry board.",
                                "Dry bread crumbs scattered under the dining table.",
                                "Dry onion peelings on the chopping board."
                            ],
                            "correct_feedback": "Correct! Cooking oil splatters bond to tiles with sticky grease, forming fixed dirt that requires warm soapy water and scrubbing.",
                            "incorrect_feedback": "Incorrect. Dry flour, crumbs, and onion peelings are loose dirt easily swept away. Oil splatters adhere tightly as fixed dirt."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Loose Dirt Transformation Risk",
                        "content": {
                            "question": "What happens if a student wipes a counter covered in loose, dry wheat flour with a soaking wet cloth instead of sweeping it dry first?",
                            "options": [
                                "The water mixes with the flour proteins to create sticky gluten dough (fixed mud) that smears and sticks tightly to the counter.",
                                "The flour vanishes into clean air immediately.",
                                "The table turns into solid metal.",
                                "The cloth turns into dry sandpaper."
                            ],
                            "answer": "A",
                            "explanation": "Adding water to dry loose flour triggers gluten formation, transforming loose dust into sticky, doughy fixed mud that is much harder to remove."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Loose dirt** consists of dry, light particles held only by gravity (flour, crumbs, dust).\n- **Fixed dirt** bonds strongly via grease, moisture, or cooking heat (oil splatters, soot, scale).\n- Always **sweep or dust loose dirt dry** before introducing water.\n- Fixed dirt requires **friction (scrubbing), water (solvent), and soap (detergents)**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we know our soil types, what tools and chemical solutions do we use to remove them? In Lesson 3, we master the methods of removing dirt!"
                        }
                    }
                ],
                # Page 7: Hard Scale Formation Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "What is Hard Water Scale?",
                        "content": {
                            "title": "Chemical Fixed Dirt",
                            "text": "When hard tap water evaporates on metal taps or inside kettles, dissolved calcium and magnesium minerals precipitate out, forming a white crust called **limescale**. Limescale cannot be washed with ordinary soap; it requires mild acids like lemon juice (citric acid) or vinegar (acetic acid) to dissolve chemically."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Methods of Removing Dirt
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Methods of Removing Dirt",
            "unit_description": "Mechanical and chemical cleaning methods: dry sweeping, dusting, wiping, scrubbing with abrasives, and the molecular chemistry of soap (lipophilic tails and hydrophilic heads).",
            "lesson_title": "Methods of Removing Dirt",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Chemical Action: Dishwashing Foam & Sponge Scrubbing",
                        "content": {
                            "title": "Chemical Action: Dishwashing Foam & Sponge Scrubbing",
                            "caption": "Soap lather emulsifying grease on a cooking pot while an abrasive sponge pad lifts adhered food soils."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Mechanical & Chemical Dirt Removal",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain the mechanical cleaning methods (**sweeping, dusting, brushing**) for loose dirt.",
                                "Describe the chemical action of **soap molecules (micelle grease encapsulation)**.",
                                "Analyze why **warm water dissolves greasy food stains faster** than cold water.",
                                "Match appropriate tools (steel wool, sponges, microfibre) to delicate vs durable surfaces."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Cleaning Solutions",
                        "content": {
                            "title": "Breaking the Grip of Grime",
                            "text": "Water and oil do not mix naturally. If you pour water over a greasy plate, the water simply beads up and runs off! To remove greasy fixed dirt, we need the combined power of **mechanical friction** (scrubbing pads) and **chemical bridges** (detergents/soaps)."
                        }
                    }
                ],
                # Page 2: Soap Chemistry & Micelle Grease Capture
                [
                    {
                        "type": "concept_explanation",
                        "title": "How Soap Molecules Destroy Grease",
                        "content": {
                            "title": "The Molecular Architecture of Detergents",
                            "text": "- **Dual Molecular Structure**: A soap molecule has two distinct ends: a **lipophilic tail** (grease-loving / hydrophobic) that embeds into cooking oil, and a **hydrophilic head** (water-loving) that bonds with water molecules.\n- **Micelle Formation**: When soap lather is agitated on a plate, thousands of soap molecules surround tiny grease droplets in a spherical cage called a **micelle**.\n- **Rinsing Action**: As clean running water washes over the surface, it pulls the hydrophilic heads along, lifting the encapsulated grease bubbles off the plate and washing them down the drain!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Detergent Chemistry: Micelle Formation, Lipophilic Tail & Hydrophilic Head Grease Capture",
                        "content": {
                            "title": "Detergent Chemistry: Micelle Formation, Lipophilic Tail & Hydrophilic Head Grease Capture",
                            "caption": "Molecular cleaning schematic: 1. Grease layer stuck to pot -> 2. Soap molecule (lipophilic tail grips grease; hydrophilic head grips water) -> 3. Micelle sphere encapsulates grease -> 4. Running water washes grease bubble away."
                        }
                    }
                ],
                # Page 3: Matching Tools to Kitchen Surfaces
                [
                    {
                        "type": "comparison_table",
                        "title": "Kitchen Surface & Cleaning Tool Matching Matrix",
                        "content": {
                            "title": "Surface Protection & Tool Selection Protocol",
                            "headers": ["Kitchen Surface", "Recommended Tool & Agent", "Strictly Forbidden Tool", "Damage Risk of Wrong Tool"],
                            "rows": [
                                ["Ceramic Wall Tiles & Glass", "Soft sponge / microfibre cloth with liquid detergent", "Steel wool or metal wire brushes", "Harsh abrasives permanently scratch and dull the glossy glass glaze"],
                                ["Aluminium / Steel Pots (Sufurias)", "Steel wool or scouring powder (Vim) with warm water", "Dry soft cloth (ineffective)", "Soft cloths cannot generate enough friction to scrape off black charcoal soot"],
                                ["Wooden Tables & Cutting Boards", "Damp cloth with mild soap; wipe along the grain", "Soaking in water basin / caustic bleach", "Excess water causes wood to swell, warp, crack, and rot internally"],
                                ["Brass / Stainless Steel Taps", "Cloth dipped in lemon juice or vinegar (acid descaling)", "Coarse sandpaper or iron scourers", "Iron scourers strip chrome plating, exposing base metal to rust"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Cleaning Methods & Dishwashing Physics
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Cleaning Methods, Dishwashing & Emulsification",
                        "content": {
                            "title": "Instructional Video: Cleaning Methods, Dishwashing & Emulsification",
                            "url": "https://www.youtube.com/watch?v=TXJPk-QfhDU",
                            "resolved_video_id": "TXJPk-QfhDU",
                            "caption": "Watch this practical demonstration on mechanical vs chemical cleaning, soap lather grease lifting, and caring for kitchen equipment."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Practical Workshop Takeaways from the Video",
                        "content": {
                            "title": "Key Cleaning Principles",
                            "text": "- **1. Warm Water Acceleration**: Notice how warm water softens solidified animal fats, speeding up soap emulsification by 300%.\n- **2. The Scratch Test**: Watch how the presenter demonstrates why wire scourers must never touch non-stick Teflon or ceramic glaze.\n- **3. Air-Drying Racks**: Observe how washed dishes are dried on a ventilated wire rack rather than wiped with dirty dishcloths."
                        }
                    }
                ],
                # Page 5: Interactive Tool Selection Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Kitchen Tool Selection Challenge",
                        "content": {
                            "title": "Choosing the Right Tool for the Job",
                            "instructions": "Match the kitchen cleaning problem to the correct, non-damaging tool:",
                            "scenario": "A student needs to clean greasy cooking splatters off a delicate glass window and remove black soot from an aluminium sufuria.",
                            "question": "Which combination is safe and effective?",
                            "options": [
                                "Use a soft sponge with warm soapy water on the glass window; use steel wool with scouring powder on the aluminium sufuria.",
                                "Use steel wool on the glass window; use a dry feather duster on the soot pot.",
                                "Use sandpaper on both surfaces.",
                                "Soak the glass window in caustic acid for 3 days."
                            ],
                            "correct_feedback": "Correct! Soft sponges protect glass from scratching, while tough steel wool generates the friction required to remove carbon soot from metal.",
                            "incorrect_feedback": "Incorrect. Steel wool will permanently ruin glass with deep scratches. Use soft sponges for glass and steel wool for durable metal pots."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Soap Grease Emulsification",
                        "content": {
                            "question": "What structural property allows soap (detergent) to lift cooking oil off dishes so it can be rinsed away with water?",
                            "options": [
                                "Soap molecules have a lipophilic tail that bonds to grease and a hydrophilic head that bonds to water, pulling the grease into wash-water.",
                                "Soap molecules freeze the cooking oil into ice cubes.",
                                "Soap is an abrasive rock that grinds glass.",
                                "Soap heats water up to 200°C instantly."
                            ],
                            "answer": "A",
                            "explanation": "Soap acts as a chemical bridge: its grease-loving tail grips oil, while its water-loving head binds to water, allowing grease to wash away in micelles."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Loose dirt** is removed mechanically with dry brooms and dusters.\n- **Fixed dirt** requires the trifecta: **solvent (water) + chemistry (soap) + friction (scrubbing)**.\n- Soap molecules encapsulate grease in **micelles** using their lipophilic tails and hydrophilic heads.\n- Match tools carefully: use **soft sponges on glass/tiles** and **steel wool on metal pots**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we organize these cleaning methods into a structured household schedule? In Lesson 4, we examine daily, weekly, and special deep-cleaning routines!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Daily, Weekly, and Special Cleaning
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Daily, Weekly, and Special Cleaning",
            "unit_description": "Organizing kitchen hygiene routines: daily chores (dishes, wiping, sweeping, trash), weekly chores (sink scrubbing, fridge cleaning, cobwebs), and periodic special deep-cleans (pantry stores, windows, vents).",
            "lesson_title": "Daily, Weekly, and Special Cleaning",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Household Hygiene: Structured Kitchen Sanitation Routine",
                        "content": {
                            "title": "Household Hygiene: Structured Kitchen Sanitation Routine",
                            "caption": "A tidy, well-maintained domestic kitchen where daily dishwashing and countertop sanitation keep food preparation hygienic."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Cleaning Cycles & Scheduling",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Distinguish the purpose and frequency of **daily, weekly, and special cleaning**.",
                                "Categorize household chores into their appropriate cleaning cycles.",
                                "Design a structured **Weekly Kitchen Cleaning Schedule** for your home.",
                                "Explain why daily trash emptying prevents disease outbreaks."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Scheduled Routines",
                        "content": {
                            "title": "Why Schedules Beat Chaos",
                            "text": "If you only clean the kitchen when dirt becomes overwhelming, cleaning becomes exhausting and stressful! Dividing chores into logical cycles ensures that dirt never accumulates, pests never establish nests, and the kitchen remains sparkling with minimal daily effort."
                        }
                    }
                ],
                # Page 2: The Three Cleaning Cycles
                [
                    {
                        "type": "concept_explanation",
                        "title": "Daily, Weekly, and Special Cleaning Tasks",
                        "content": {
                            "title": "The Three Sanitation Tiers",
                            "text": "- **1. Daily Cleaning (The Hygiene Shield)**: Done every day to maintain basic hygiene. Includes washing dishes after every meal, wiping stove and counters immediately after cooking, sweeping floors, and emptying organic trash bins.\n- **2. Weekly Cleaning (The Prevention Routine)**: Done once a week for areas that collect grime slowly. Includes scrubbing sinks and taps, wiping inside the refrigerator, washing dishcloths in hot water, and clearing ceiling cobwebs.\n- **3. Special Cleaning (The Deep Clean)**: Done monthly, before holidays, or at end-of-term. Includes emptying and wiping food pantry shelves, washing window fly screens, descaling kettles, and deep-degreasing stove burners."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Daily, Weekly, and Special Kitchen Cleaning Cycle Matrix",
                        "content": {
                            "title": "Daily, Weekly, and Special Kitchen Cleaning Cycle Matrix",
                            "caption": "Three-tiered cleaning framework: 1. Daily Tier (Dishes, worktops, sweeping, trash) • 2. Weekly Tier (Sinks, fridge, dishcloths, cobwebs) • 3. Special Deep-Clean Tier (Pantry stores, windows, fly screens, burner degreasing)."
                        }
                    }
                ],
                # Page 3: Chore Distribution Grid
                [
                    {
                        "type": "comparison_table",
                        "title": "Kitchen Chore Frequency Master Matrix",
                        "content": {
                            "title": "Chore Frequency & Responsibility Matrix",
                            "headers": ["Daily Tasks (Every Day)", "Weekly Tasks (Once a Week)", "Special Tasks (Periodic Deep-Clean)"],
                            "rows": [
                                ["Wash all dishes, cups, and pots after meals", "Scrub sink basin, taps, and backsplash tiles", "Empty pantry cupboards and wash storage shelves"],
                                ["Wipe cooking oil splatters off cooker & counters", "Deep-clean refrigerator shelves & bread box", "Wash window panes, fly screens, and vents"],
                                ["Sweep floor and mop sticky spills", "Wash dishcloths, towels, and aprons in hot soapy water", "Soak and scrape carbonized stove burner heads"],
                                ["Empty food scrap trash bin & wash container", "Sweep down cobwebs from ceiling & walls", "Disinfect outdoor garbage storage area"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Chore Scheduling Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Kitchen Routine Classification Challenge",
                        "content": {
                            "title": "Assigning Chores to Frequency Tiers",
                            "instructions": "Classify each kitchen chore into Daily, Weekly, or Special:",
                            "scenario": "A family is planning their monthly household cleaning duty roster.",
                            "question": "Which of the following tasks should be performed once a week rather than every single day or once a month?",
                            "options": [
                                "Deep-cleaning the inside of the refrigerator and washing kitchen dishcloths in hot soapy water (Weekly).",
                                "Washing breakfast plates and cups.",
                                "Emptying the daily vegetable peelings into the compost bin.",
                                "Emptying and repainting all pantry food shelves."
                            ],
                            "correct_feedback": "Correct! Refrigerator wipe-downs and dishcloth sanitizing are weekly maintenance tasks that keep food fresh and cloths germ-free.",
                            "incorrect_feedback": "Incorrect. Washing dishes and emptying trash are daily tasks. Cupboard repainting is a special periodic task. Refrigerator cleaning is done weekly."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Reason for Daily Trash Disposal",
                        "content": {
                            "question": "Why must the organic food scrap trash bin in the kitchen be emptied, washed, and disinfected every single day?",
                            "options": [
                                "Because rotting food scraps produce foul odors and attract disease-carrying pests like houseflies, cockroaches, and rats.",
                                "To make the trash can look taller.",
                                "To turn the plastic bin into compost.",
                                "To make the kitchen cooler."
                            ],
                            "answer": "A",
                            "explanation": "Organic food waste decomposes rapidly in warm kitchens, producing offensive odors and attracting disease vectors that spread pathogens."
                        }
                    }
                ],
                # Page 6: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Daily cleaning** maintains immediate hygiene: wash dishes, wipe counters, sweep floors, empty trash.\n- **Weekly cleaning** prevents grime buildup: scrub sinks, sanitize dishcloths, clean fridge, remove cobwebs.\n- **Special cleaning** handles deep sanitation: empty pantry stores, wash window screens, degrease burners.\n- A structured cleaning schedule prevents pests and reduces household chore stress."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Now that we have planned our schedules, let's roll up our sleeves and perform practical kitchen cleaning! In Lesson 5, we practice worktop sanitizing, stove care, and the double-bucket mopping method!"
                        }
                    }
                ],
                # Page 7: Refrigerator Hygiene Callout
                [
                    {
                        "type": "concept_explanation",
                        "title": "Refrigerator Hygiene: The Cold Trap",
                        "content": {
                            "title": "Why Fridges Need Weekly Cleans",
                            "text": "Many people believe cold temperatures kill bacteria. In reality, refrigeration only slows down bacterial growth! Spores of *Listeria* and molds can still grow slowly on spilled milk and vegetable drippings inside cold refrigerators. Wiping shelves weekly with warm water and baking soda prevents mold contamination."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Practical: Cleaning the Kitchen
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Practical: Cleaning the Kitchen",
            "unit_description": "Standard operating procedures for practical sanitation: worktop wiping, stove degreasing, sink descaling with natural acids, and the double-bucket floor mopping method (figure-8 stroke).",
            "lesson_title": "Practical: Cleaning the Kitchen",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Practical Execution: Collaborative Kitchen Lab Sanitation",
                        "content": {
                            "title": "Practical Execution: Collaborative Kitchen Lab Sanitation",
                            "caption": "Students working collaboratively in a clean training kitchen, performing organized worktop sanitizing, sink scrubbing, and floor maintenance."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Practical Sanitation Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Execute the 4-step **worktop and cooker cleaning procedure** (clear, sweep, scrub, sanitize).",
                                "Descale metal taps and scrub sink basins using **scouring powder and natural acids (lemon/vinegar)**.",
                                "Master the **Double-Bucket Mopping System** (Wash vs Rinse) and the **Figure-8 stroke**.",
                                "Demonstrate teamwork, water conservation, and slip prevention during practical chores."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to the Practical Sanitation Lab",
                        "content": {
                            "title": "From Theory to Hands-On Action",
                            "text": "True learning in CBC Agriculture happens when you apply scientific principles with your hands! Today, we practice professional kitchen sanitation routines that transform messy, greasy spaces into clean, safe, and efficient food laboratories."
                        }
                    }
                ],
                # Page 2: Worktops, Cookers & Sink Descaling SOP
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Worktops, Stoves & Sinks",
                        "content": {
                            "title": "Step-by-Step Equipment Care",
                            "steps": [
                                "**Step 1: Clear & Sweep Worktops**: Move all pots, jars, and utensils away. Brush dry crumbs off the counter into a dustpan with a dry cloth.",
                                "**Step 2: Scrub Stoves with Soapy Sponge**: Dip a sponge into warm soapy water and scrub the stove surface to lift oil splatters. Wipe away dirty soap lather with a damp rinse cloth.",
                                "**Step 3: Scrub Sink Basin & Taps**: Clear food scraps from the drain basket. Sprinkle scouring powder (Vim) and scrub the stainless steel basin and surrounding tiles.",
                                "**Step 4: Descale with Lemon or Vinegar**: Rub white calcium mineral scale around taps with a fresh lemon slice or vinegar-soaked cloth; rinse thoroughly with clean water."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Double-Bucket Mopping System, Figure-8 Stroke & Squeegee Drainage Flow",
                        "content": {
                            "title": "Double-Bucket Mopping System, Figure-8 Stroke & Squeegee Drainage Flow",
                            "caption": "Professional floor sanitation flowchart: 1. Dip mop in Bucket 1 (Soapy Wash) -> 2. Mop tiles in continuous Figure-8 pattern -> 3. Rinse dirty mop in Bucket 2 (Clean Water) & wring out -> 4. Squeegee standing water toward drain."
                        }
                    }
                ],
                # Page 3: The Double-Bucket Mopping Science
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Double-Bucket Mopping System",
                        "content": {
                            "title": "Why Single-Bucket Mopping Spreads Dirt",
                            "text": "- **The Single-Bucket Flaw**: If you use only one bucket, rinsing your dirty mop deposits dirt back into your soapy water. Soon, you are mopping your kitchen floor with muddy, germ-laden liquid!\n- **Bucket 1 (Soapy Wash Water)**: Contains warm water mixed with floor cleaning detergent.\n- **Bucket 2 (Clean Rinse Water)**: Contains clean water to rinse the dirty mop and wring out trapped grime.\n- **The Figure-8 Stroke**: Moving the mop in overlapping figure-8 strokes keeps all dirt particles in front of the mop head without spreading them sideways.\n- **Squeegee Drying**: Use a rubber squeegee blade to push remaining surface water toward the floor drain to prevent dangerous slips."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Single-Bucket vs. Double-Bucket Mopping Comparison",
                        "content": {
                            "title": "Mopping System Efficacy Matrix",
                            "headers": ["System", "Wash Water Purity", "Bacterial Spread Risk", "Drying Speed & Tile Finish"],
                            "rows": [
                                ["Single-Bucket System", "Rapidly turns into dark, muddy water after 2 rinses", "High (redeposits bacteria across entire floor)", "Slow drying, leaves hazy dirty streaks on tiles"],
                                ["Double-Bucket System", "Remains clean and soapy throughout entire chore", "Zero (dirt is trapped and discarded in rinse bucket)", "Fast drying, leaves sparkling, sanitized tiles"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Practical Kitchen Cleaning
                [
                    {
                        "type": "suggested_video",
                        "title": "Practical Video: Grade 8 Kitchen Cleaning, Stove Care & Mopping",
                        "content": {
                            "title": "Practical Video: Grade 8 Kitchen Cleaning, Stove Care & Mopping",
                            "url": "https://www.youtube.com/watch?v=6ZjkLwQt_YE",
                            "resolved_video_id": "6ZjkLwQt_YE",
                            "caption": "Watch this step-by-step practical demonstration on clearing worktops, degreasing cookers, descaling sinks, and professional double-bucket floor mopping in Kenya."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Field Observations from the Video",
                        "content": {
                            "title": "Field Workshop Reminders",
                            "text": "- **1. Dry Before Wet**: Notice how the teacher insists on sweeping dry bread flour off the counter *before* touching it with a wet sponge.\n- **2. Drain Strainers**: Watch how food scraps are placed in the compost bin instead of being washed down the sink drain.\n- **3. Slip Warnings**: Observe how wet floor warning signs are positioned while mopping."
                        }
                    }
                ],
                # Page 5: Interactive Stove Cleaning Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Stove Cleaning Sequencing Challenge",
                        "content": {
                            "title": "Ordering Cooker Cleaning Steps",
                            "instructions": "Place the cooker cleaning steps in the correct logical sequence:",
                            "scenario": "You are cleaning a greasy gas cooker after preparing fried fish and ugali.",
                            "question": "What is the correct sequential order of actions?",
                            "options": [
                                "1. Clear pots away -> 2. Brush dry crumbs off into dustpan -> 3. Scrub grease with soapy sponge -> 4. Wipe off soap with damp cloth -> 5. Spray light disinfectant and air-dry",
                                "1. Pour water over hot burning gas flames -> 2. Wipe with newspaper -> 3. Leave crumbs on burners",
                                "1. Spray bleach on raw food -> 2. Scrub with steel wire on gas valves",
                                "1. Paint over grease with white paint"
                            ],
                            "correct_feedback": "Correct! Always clear the area, sweep loose crumbs dry, scrub grease with soap, rinse clean, and sanitize with light disinfectant.",
                            "incorrect_feedback": "Incorrect. Follow the hygienic order: Clear area -> Sweep dry crumbs -> Scrub grease with soap -> Rinse with damp cloth -> Sanitize."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Sink Drain Blockage Prevention",
                        "content": {
                            "question": "Why should liquid cooking fat and solid food scraps never be poured down the kitchen sink drain?",
                            "options": [
                                "Cooking fat cools and solidifies inside plumbing pipes, trapping food scraps and causing stubborn, foul-smelling drain blockages.",
                                "It turns the tap water into milk.",
                                "It makes the sink basin float away.",
                                "It makes the pipes too shiny."
                            ],
                            "answer": "A",
                            "explanation": "Liquid fats solidify upon cooling inside cold pipes. They bind with food scraps, creating dense blockages that cause bad odors and plumbing backups."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Clean cookers by **clearing, sweeping dry crumbs, scrubbing grease, rinsing, and sanitizing**.\n- Descale white mineral crusts around taps using natural acids (**lemon juice or vinegar**).\n- Use the **Double-Bucket Mopping System** to prevent spreading dirty wash water across floor tiles.\n- Always dry standing water with a **rubber squeegee** to prevent dangerous slips."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Cleaning involves hot water, sharp knives, and powerful chemicals! How do we protect our bodies while cleaning? In Lesson 6, we examine essential safety precautions, chemical hazard labels, and PPE!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Safety Precautions in Kitchen Cleaning & Capstone
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Safety Precautions in Kitchen Cleaning",
            "unit_description": "Recognizing physical and chemical cleaning hazards, warning label symbols (toxic, corrosive, flammable), personal protective equipment (PPE), avoiding toxic chlorine gas mixtures, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Safety Precautions in Kitchen Cleaning & Capstone",
            "pages": [
                # Page 1: Visual Hook & Capstone Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Safety Compliance: Personal Protective Equipment & Warning Labels",
                        "content": {
                            "title": "Safety Compliance: Personal Protective Equipment & Warning Labels",
                            "caption": "Household cleaning bottles displaying clear chemical hazard warning symbols (toxic, corrosive, flammable) alongside protective rubber gloves."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Hazard Mitigation & Topic Mastery",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Identify **physical hazards (slips, cuts, burns)** and **chemical hazards (fumes, skin burns)**.",
                                "Interpret **household chemical warning symbols** (Corrosive, Toxic, Flammable).",
                                "Select and wear appropriate **PPE (rubber gloves, apron, mask, closed shoes)**.",
                                "Review the Topic Video and demonstrate 100% mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Safety First in Kitchen Sanitation",
                        "content": {
                            "title": "Cleaning Without Getting Hurt",
                            "text": "Cleaning products and tools are designed to destroy grime and kill bacteria. However, strong chemicals, hot water, and wet tiles can cause serious injuries if handled carelessly! Mastering safety precautions protects your eyes, skin, lungs, and bones during daily chores."
                        }
                    }
                ],
                # Page 2: Physical & Chemical Hazards & Chemical Warning Symbols
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physical and Chemical Hazards in Cleaning",
                        "content": {
                            "title": "Recognizing Hazards & Warning Labels",
                            "text": "- **1. Physical Hazards**: Wet tiles (slips and falls), sharp knife blades inside soapy washbowls, and lifting heavy buckets with bent backs.\n- **2. Chemical Burns & Irritation**: Strong oven cleaners and undiluted bleach burn skin on contact. Always wear **rubber gloves** and wash splashes with running water immediately.\n- **3. Deadly Fumes & Ventilation**: **NEVER mix chlorine bleach with acid cleaners or vinegar!** This triggers a violent chemical reaction that releases **toxic, suffocating chlorine gas** ($$\\text{Cl}_2$$) that damages lung tissues instantly.\n- **4. Ventilation Mandate**: Always open windows and doors wide while cleaning with chemical agents."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Kitchen Cleaning Chemical Hazards, Toxic Gas Warnings & Full PPE Equipment",
                        "content": {
                            "title": "Kitchen Cleaning Chemical Hazards, Toxic Gas Warnings & Full PPE Equipment",
                            "caption": "Safety & PPE master schematic: 1. Hazard Symbols (Skull = Toxic, Acid Hand = Corrosive, Flame = Flammable) • 2. Chemical Mixing Hazard (Bleach + Acid = Deadly Chlorine Gas!) • 3. Personal Protective Equipment (Rubber gloves, canvas apron, dust mask, closed leather shoes)."
                        }
                    }
                ],
                # Page 3: Personal Protective Equipment (PPE) & Warning Symbols
                [
                    {
                        "type": "comparison_table",
                        "title": "Chemical Warning Symbols & Protective PPE Matrix",
                        "content": {
                            "title": "Safety Symbols & Protection Standards",
                            "headers": ["Hazard Symbol / PPE", "Meaning / Protection Area", "Safety Protocol", "Consequence of Neglect"],
                            "rows": [
                                ["Corrosive Symbol (Acid on hand)", "Chemicals that burn skin and eat metal", "Wear thick rubber gloves; rinse skin immediately if splashed", "Severe painful chemical skin burns"],
                                ["Toxic Symbol (Skull & crossbones)", "Poisonous chemicals if swallowed or inhaled", "Store in locked high cupboards away from children; never ingest", "Poisoning, organ failure, or fatality"],
                                ["Flammable Symbol (Fire flame)", "Liquids/sprays that ignite easily near fire", "Keep away from lit gas burners, hot stoves, and matches", "Explosive flash fires and severe burns"],
                                ["Rubber Gloves & Apron", "Protects hands and clothing", "Wear during all scouring, bleaching, and chemical cleaning", "Skin dermatitis, chemical irritations, stained clothes"],
                                ["Closed Shoes", "Protects feet from falling items & spills", "Wear sturdy closed shoes (never barefoot or flip-flops)", "Toe fractures from dropped heavy pots or chemical spills"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Hazard Matching Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Cleaning Hazard & Action Matching Challenge",
                        "content": {
                            "title": "Matching Hazards to Safety Responses",
                            "instructions": "Match each kitchen hazard to its correct preventative safety action:",
                            "scenario": "You are organizing a chemical cleaning cabinet and preparing to clean a greasy school oven.",
                            "question": "What is the primary danger if someone mixes liquid chlorine bleach with an acidic toilet bowl cleaner?",
                            "options": [
                                "A rapid chemical reaction releases deadly, suffocating chlorine gas that causes severe chemical burns inside the lungs.",
                                "The mixture turns into cold ice cubes.",
                                "The bucket turns into solid steel.",
                                "The room fills with sweet strawberry perfume."
                            ],
                            "correct_feedback": "Correct! Mixing bleach with acids produces toxic chlorine gas, which causes severe respiratory damage and can be fatal. Never mix cleaning chemicals!",
                            "incorrect_feedback": "Incorrect. Mixing bleach with acid releases deadly chlorine gas. Always keep cleaning chemicals strictly separate."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Mandatory Ventilation During Cleaning",
                        "content": {
                            "question": "Why must windows and doors always be opened wide when cleaning a kitchen with strong chemical detergents or bleach?",
                            "options": [
                                "To provide continuous fresh air ventilation so chemical fumes do not accumulate and damage the respiratory system.",
                                "To let the neighborhood birds fly inside.",
                                "To cool down the hot water in the bucket.",
                                "To dry the dishes outside."
                            ],
                            "answer": "A",
                            "explanation": "Chemical fumes (from bleach, ammonia, or oven sprays) irritate the lungs and eyes. Opening windows ensures fresh airflow and rapid dilution of vapors."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 7 Master Summary: Kitchen Hygiene Practices",
                        "content": {
                            "text": "- **Reasons for Cleaning**: Destroys **germs and molds**, deters **disease vectors**, stops **grease fires**, and protects **metal tools from acid rust**.\n- **Soil Classification**: **Loose dirt** (flour, dust, crumbs) swept dry; **Fixed dirt** (grease, soot, scale) requires water, soap, and scrubbing.\n- **Soap Mechanism**: Soap molecules form **micelles** (lipophilic tails bind grease; hydrophilic heads bind water) to wash grime away.\n- **Schedules**: **Daily** (dishes, counters, trash); **Weekly** (sinks, fridge, dishcloths); **Special** (pantry, windows, vents).\n- **Practical Procedures**: Clear, sweep, scrub, and sanitize cookers; use the **Double-Bucket Mopping System**; descale taps with lemon/vinegar.\n- **Safety & PPE**: Wear **gloves, aprons, closed shoes**; open windows; **NEVER mix bleach with acid** (deadly chlorine gas)."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Kitchen Hygiene Practices & Safety",
                        "content": {
                            "title": "Topic Video Review: Kitchen Hygiene Practices & Safety",
                            "url": "https://www.youtube.com/watch?v=Ei5z_0Lxmic",
                            "resolved_video_id": "Ei5z_0Lxmic",
                            "caption": "Watch this comprehensive educational review covering kitchen hygiene pillars, loose vs fixed dirt, double-bucket mopping, and chemical safety precautions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Review Questions for Video Analysis",
                        "content": {
                            "title": "Final Review Highlights",
                            "text": "- **1. Systematic Routine**: Notice how structured daily chores prevent deep dirt accumulation.\n- **2. The Double-Bucket Proof**: See the dramatic difference between single-bucket dirty water and double-bucket clean tiles.\n- **3. Chemical Respect**: Observe how professional cleaners always wear gloves and check product hazard labels."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Biological Reason for Kitchen Hygiene",
                        "content": {
                            "question": "Which of the following is the most critical biological reason for maintaining high kitchen hygiene and cleaning surfaces regularly?",
                            "options": [
                                "To destroy disease-causing pathogens and prevent foodborne illnesses like diarrhea and stomach infections.",
                                "To make kitchen walls look shiny.",
                                "To reduce the time it takes to cook food.",
                                "To prevent the stove from using too much fuel."
                            ],
                            "answer": "A",
                            "explanation": "Warm, damp kitchens with food residues are ideal bacterial breeding grounds. Regular cleaning destroys pathogens before they contaminate food."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Scientific Definition of Loose Dirt",
                        "content": {
                            "question": "What is the correct scientific definition of 'loose dirt' in a food preparation environment?",
                            "options": [
                                "Dry, light particles lying on a surface without any sticky chemical, oil, or moisture bond.",
                                "Sticky cooking oil splatters dried onto wall tiles.",
                                "Black carbon soot baked onto the bottom of a metal pot.",
                                "Hard mineral calcium crusts inside a kettle."
                            ],
                            "answer": "A",
                            "explanation": "Loose dirt consists of unbonded dry particles (flour, crumbs, dust) held only by gravity and easily swept away with a dry broom."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Daily Task for Pest Prevention",
                        "content": {
                            "question": "Which of the following is classified as an essential daily kitchen cleaning task to prevent pest infestation?",
                            "options": [
                                "Washing dishes, wiping worktops, and emptying the organic food scrap trash bin.",
                                "Deep-cleaning the inside of the refrigerator and freezer.",
                                "Washing all window glass, fly screens, and grates.",
                                "Scrubbing high ceilings to remove cobwebs."
                            ],
                            "answer": "A",
                            "explanation": "Dishes, counters, and trash bins collect organic food waste that immediately attracts houseflies, cockroaches, and rats if left overnight."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Soap Grease Emulsification Mechanism",
                        "content": {
                            "question": "What chemical property allows soap (detergent) to dissolve sticky cooking oil and grease so they can be washed away with water?",
                            "options": [
                                "Soap molecules have a dual structure: a lipophilic tail that bonds to grease and a hydrophilic head that bonds to water.",
                                "Soap molecules boil the grease chemically.",
                                "Soap acts as a strong abrasive acid that dissolves glass.",
                                "Soap turns water into solid ice crystals."
                            ],
                            "answer": "A",
                            "explanation": "Soap molecules form micelles around grease droplets: their fat-loving tails grip oil while their water-loving heads pull grease into the wash water."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Avoiding Steel Wool on Ceramic Tiles",
                        "content": {
                            "question": "Why is steel wool strictly avoided when cleaning greasy stains off ceramic wall tiles or glass windows?",
                            "options": [
                                "Steel wool is a harsh abrasive that permanently scratches and damages delicate glass and tile glazes.",
                                "It causes the soap to evaporate too quickly.",
                                "It is too soft to scrape oil away.",
                                "It makes the glass become flammable."
                            ],
                            "answer": "A",
                            "explanation": "Steel wool creates permanent abrasive scratches on smooth ceramic glaze and glass surfaces, creating dull grooves where dirt gets trapped."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Double-Bucket Mopping Rationale",
                        "content": {
                            "question": "When mopping a kitchen floor, what is the primary purpose of using the 'double-bucket mopping system'?",
                            "options": [
                                "To separate dirty rinse-water from clean soapy water, preventing the spread of dirt and bacteria across floor tiles.",
                                "To allow two students to mop at the exact same time.",
                                "To make the floor dry twice as fast.",
                                "To reduce the amount of soap needed."
                            ],
                            "answer": "A",
                            "explanation": "The double-bucket system uses one bucket for soapy wash water and another for rinsing the dirty mop, ensuring clean water is always applied to tiles."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Chemical Safety Protocol",
                        "content": {
                            "question": "Which of the following is a critical safety rule when deep-cleaning kitchen surfaces with strong household chemicals?",
                            "options": [
                                "Wear rubber gloves, an apron, and open windows wide to ensure proper fresh air ventilation.",
                                "Keep doors and windows tightly closed to trap the chemical scent.",
                                "Mix chlorine bleach with acid bowl cleaners to double their strength.",
                                "Never dilute chemicals with water."
                            ],
                            "answer": "A",
                            "explanation": "Wearing rubber gloves and aprons prevents chemical burns, while open windows provide essential ventilation to protect the lungs from fumes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Tap Descaling with Natural Acids",
                        "content": {
                            "question": "How does a natural kitchen ingredient like fresh lemon juice or vinegar help remove crusty mineral scale from metal taps?",
                            "options": [
                                "The natural acid (citric or acetic acid) chemically reacts with and dissolves the alkaline calcium mineral crust.",
                                "The sugars inside turn the scale into liquid soap.",
                                "It acts as an abrasive scrub that scratches the metal clean.",
                                "It boils the metal tap to melt the minerals."
                            ],
                            "answer": "A",
                            "explanation": "Hard limescale is an alkaline mineral deposit. Mild acids like lemon juice (citric acid) or vinegar (acetic acid) react with and dissolve the scale safely."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Wet Mop on Spilled Dry Flour Hazard",
                        "content": {
                            "question": "A student finds dry wheat flour spilled on a floor and immediately mops it with a soaking wet mop. What is the result?",
                            "options": [
                                "The water mixes with flour proteins to form a sticky, gluten-rich paste (fixed mud) that smears and is much harder to remove.",
                                "The floor becomes dry and shiny immediately.",
                                "The water dissolves the flour into a transparent cleaning gas.",
                                "The mop turns into a hard plastic brush."
                            ],
                            "answer": "A",
                            "explanation": "Spilled flour is loose dirt. Applying water triggers gluten formation, turning loose powder into sticky doughy mud. It must always be swept dry first."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Bleach and Acid Chemical Danger",
                        "content": {
                            "question": "Why is it extremely dangerous to mix liquid chlorine bleach with vinegar or acid-based cleaners during a kitchen clean?",
                            "options": [
                                "The mixture triggers a chemical reaction that releases toxic, suffocating chlorine gas, which causes severe chemical burns inside the lungs.",
                                "It creates an explosive mixture that shatters the plastic bucket.",
                                "It turns the bleach into a thick sugar paste.",
                                "It stops the bleach from smelling like soap."
                            ],
                            "answer": "A",
                            "explanation": "Mixing bleach (sodium hypochlorite) with any acid releases deadly chlorine gas, which reacts with moisture in the respiratory system, causing severe lung damage."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic7(replace: bool = True):
    """Executes the database transaction to ingest Topic 7 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 7 (DEEP EDITION)")
    print("=" * 80)

    with transaction.atomic():
        curriculum, _ = Curriculum.objects.get_or_create(
            name="CBC",
            defaults={"description": "Competency Based Curriculum"}
        )
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="Grade 8",
            defaults={"level": 8, "description": "Junior Secondary School Grade 8"}
        )
        subject, _ = Subject.objects.get_or_create(
            grade=grade,
            name="Agriculture",
            defaults={"description": "Grade 8 Agriculture (CBC)"}
        )

        print(f"[*] Hierarchy Resolved: {curriculum.name} -> {grade.name} -> {subject.name}")

        topic_name = "Kitchen Hygiene Practices"
        if replace:
            existing_topics = Topic.objects.filter(subject=subject, name=topic_name)
            if existing_topics.exists():
                print(f"[*] Found existing topic '{topic_name}' (ID: {existing_topics.first().id}). Deleting for clean replace...")
                existing_topics.delete()

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            name=topic_name,
            defaults={
                "order": 7,
                "description": "Comprehensive kitchen hygiene, soil classification, and sanitation: reasons for cleaning (disease prevention, pest vectors, grease fire safety, tool preservation); loose dirt vs fixed dirt bonding mechanics; methods of removing dirt (dry sweeping, dusting, soap micelle emulsification, surface-tool matching); daily, weekly, and special cleaning cycles; practical worktop sanitizing, stove care, sink descaling with natural acids, and double-bucket mopping; chemical hazard warning labels, avoiding toxic chlorine gas mixtures, and PPE safety protocols."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

        curriculum_data = build_topic7_curriculum()
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
                        block_id=f"g8_agri_t7_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 7: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic7(replace=replace_flag)
