"""
VLearn CBC Grade 10 Agriculture — Topic 13: Tools and Equipment
Production Ingestion Engine (Deep Senior Secondary Pedagogical Edition)

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Agriculture
Topic: Tools and Equipment (Topic Order: 13)

Decomposed into 14 Learning Units & 14 Published Lessons:
  1. Introduction to Farm Tools (4 Pages, 8 Blocks)
  2. Task-Tool Matching and Selection (4 Pages, 8 Blocks)
  3. Gardening Tools - Digging & Preparing (4 Pages, 9 Blocks)
  4. Gardening Tools - Cutting & Pruning (4 Pages, 8 Blocks)
  5. Gardening Tools - Planting & Irrigation (4 Pages, 8 Blocks)
  6. Livestock Tools - Breeding & Identification (4 Pages, 9 Blocks)
  7. Livestock Tools - Health & Feeding (4 Pages, 8 Blocks)
  8. Livestock Tools - Grooming & Harvesting (4 Pages, 8 Blocks)
  9. Assembling Tasks - Threaded Fasteners (4 Pages, 9 Blocks)
  10. Disassembling Tasks - Cutting & Fabricating (4 Pages, 9 Blocks)
  11. Maintenance Practices - Cleaning and Sharpening (4 Pages, 9 Blocks)
  12. Maintenance Practices - Lubrication & Protection (4 Pages, 8 Blocks)
  13. Care, Storage, and Workspace Organization (4 Pages, 9 Blocks)
  14. Accident Prevention, First Aid, and Review (8 Pages, 17 Blocks)
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

def build_topic13_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Topic 13: Tools and Equipment."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Farm Tools
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Farm Tools",
            "unit_description": "Definitions of tools, equipment, machines; 3 power sources (manual, animal-drawn, motorized); historical mechanization timeline.",
            "lesson_title": "Agricultural Mechanics: Classification of Tools, Equipment, Machines, and Power Sources",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Comprehensive Display of Agricultural Hand Tools and Workshop Implements",
                        "content": {
                            "title": "Comprehensive Display of Agricultural Hand Tools and Workshop Implements",
                            "caption": "A collection of essential smallholder farm hand tools and mechanical implements used in crop husbandry, soil cultivation, and livestock management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Farm Tools Introduction",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish **agricultural tools, equipment, and machines** based on mechanical complexity.",
                                "Analyze 3 primary farm power sources: **Manual, Animal-Drawn, and Motorized**.",
                                "Trace the **historical transformation of agricultural productivity** through mechanization.",
                                "Catalog tools by operational domain (**crop production, livestock husbandry, workshop maintenance**)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Definitions in Agricultural Mechanics",
                        "content": {
                            "title": "Tools vs. Equipment vs. Machines",
                            "text": "Understanding technical terminology allows farmers to organize assets and plan capital investments:\n\n- **Agricultural Tool**: A simple, handheld, unpowered implement used to perform physical farm operations using direct human muscle power (e.g., jembe, panga, trowel, secateurs).\n- **Agricultural Equipment**: A moderately complex device containing moving or assembled parts that facilitates specialized tasks, often utilizing leverage or external pressure (e.g., knapsack sprayer, wheelbarrow, drenching gun, hand maize sheller).\n- **Agricultural Machine**: A complex, power-driven assembly designed to convert chemical or electrical energy into heavy mechanical work (e.g., tractor-mounted disc plough, combine harvester, motorized water pump)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Primary Power Sources in Agriculture",
                        "content": {
                            "title": "Energy Pathways on the Farm",
                            "text": "1. **Manual Power**: Human muscular force. Highly accessible, precise for delicate nursery tasks, but physically exhausting with very low work output ($<0.1\\text{ horsepower}$). Limited to small gardens.\n2. **Animal-Drawn Power**: Draft animals (oxen, donkeys, camels) pulling ox-ploughs, ridgers, and carts. Generates moderate speed and power ($0.5\\text{--}1.5\\text{ hp}$), cost-effective for medium holdings, but requires daily feeding, veterinary care, and animal training.\n3. **Motorized Power**: Internal combustion engines (diesel/petrol) or electric motors. Delivers high speed and massive power ($>15\\text{ hp}$), easily tilling heavy clays and pumping water, but requires high startup capital, fossil fuel, and technical repair skills."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Power Sources in Agricultural Implements",
                        "content": {
                            "title": "Power Sources in Agricultural Implements",
                            "caption": "Power taxonomy: 1 Manual Human Muscle (Low output, high precision) | 2 Animal Draft Power (Moderate output, low capital) | 3 Motorized Internal Combustion (High output, high speed, high capital)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison of Agricultural Power Sources",
                        "content": {
                            "title": "Agricultural Power Source Comparison Matrix",
                            "headers": ["Power Source", "Typical Implements Used", "Capital Investment", "Daily Work Output", "Primary Operational Limitation"],
                            "rows": [
                                ["Manual Power", "Jembe, Panga, Spade, Trowel", "Very Low (KES 500–2,000)", "Low (<0.1 ha/day)", "Severe physical fatigue & slow pace"],
                                ["Animal Draft Power", "Ox-plough, Cart, Weed ridger", "Moderate (KES 20,000–50,000)", "Moderate (0.5–1.0 ha/day)", "Requires feed, veterinary care & training"],
                                ["Motorized Power", "Tractor, Power tiller, Motor pump", "High (KES 150,000–3,000,000)", "Very High (>5 ha/day)", "High fuel costs & complex maintenance"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: School Farm Tool and Machine Power Audit",
                        "content": {
                            "title": "Farm Implement Classification Lab",
                            "task": "1. Inspect the school farm tool shed and machinery yard.\n2. Identify 6 different implements.\n3. Classify each as a Tool, Equipment, or Machine.\n4. Record their power sources (Manual vs Animal vs Motorized) and primary operational domain.",
                            "materials": ["Clipboard", "Classification Sheet", "Pen"],
                            "safety": "Do not touch moving machine parts or engine components."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Introduction to Farm Tools",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Tools are simple handheld devices**; **machines are motorized assemblies**.\n- **Manual power provides precision**; **motorized power delivers speed and volume**.\n- **Animal draft power balances cost and output** for medium holdings.\n- **Mechanization eliminates labor bottlenecks** and boosts crop yields."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Power Source Classification",
                        "content": {
                            "question": "Which of the following is the most accurate technical classification for a diesel-powered centrifugal water pump used to irrigate a commercial cabbage field?",
                            "options": [
                                "An agricultural hand tool driven by manual muscle power",
                                "An agricultural machine driven by motorized internal combustion power",
                                "A draft implement driven by animal power",
                                "A biological soil amendment applicator"
                            ],
                            "answer": "B",
                            "explanation": "A motorized centrifugal water pump contains complex mechanical moving parts (impellers, pistons, bearings) and converts fossil fuel chemical energy via an internal combustion engine into hydraulic pressure, classifying it as an agricultural machine."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Task-Tool Matching and Selection
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Task-Tool Matching and Selection",
            "unit_description": "Principles of task-tool matching; physical and economic penalties of tool mismatch; selection criteria (soil texture, crop stage, scale, ergonomics).",
            "lesson_title": "Ergonomics and Mechanical Efficiency: The Science of Task-Tool Matching",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Farmer Cultivating Garden Soil Using a Traditional Agricultural Hoe",
                        "content": {
                            "title": "Farmer Cultivating Garden Soil Using a Traditional Agricultural Hoe",
                            "caption": "A farmer selecting and operating a digging hoe matched precisely to the soil texture and weeding task in a smallholder vegetable plot."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Task-Tool Matching",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the principle of **task-tool matching in agricultural operations**.",
                                "Analyze the **physical, biological, and economic consequences of poor tool selection**.",
                                "Apply 4 selection criteria: **Soil condition, Crop growth stage, Operational scale, and Ergonomics**.",
                                "Prevent operator injuries caused by tool slippage and excessive muscular strain."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Principle of Task-Tool Matching",
                        "content": {
                            "title": "Aligning Form with Function",
                            "text": "**Task-tool matching** is the deliberate selection of the specific implement whose shape, weight, cutting angle, and mechanical advantage are engineered for a particular field operation:\n\n- **Mechanical Advantage**: Every tool is designed to apply force in a specific vector (e.g., slicing vs scooping vs prying).\n- **Economic Dividend**: Correct matching minimizes completion time, preserves worker stamina, prevents tool breakage, and protects delicate crop root systems from collateral damage."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cascading Consequences of Poor Tool Selection",
                        "content": {
                            "title": "The Penalties of Tool Mismatch",
                            "text": "1. **Damage to Tools**: Using a delicate hand trowel to pry out heavy granite boulders bends the steel blade and snaps the handle.\n2. **Pathological Damage to Crops**: Using a heavy, blunt panga instead of sharp secateurs to prune tomato vines crushes the vascular bundle (xylem/phloem), creating ragged wounds that invite fungal blight (*Phytophthora*).\n3. **Physical Injury to Handler**: Using a digging jembe to chop thick tree roots can cause the curved blade to glance off the wood, striking the worker's foot or shins.\n4. **Labor Inefficiency**: Attempting to prepare a 1-acre field with hand trowels exhausts laborers and misses critical rainfall planting windows."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "4 Core Tool Selection Criteria",
                        "content": {
                            "title": "How to Choose the Right Tool",
                            "text": "- **Soil Type and Texture**: Heavy clay soils require strong, heavy-gauge steel tools (heavy jembe, fork jembe); light sandy soils are easily worked with spades.\n- **Crop Growth Stage**: Weeding closely spaced vegetable seedlings requires a narrow hand weeder or light hoe, not a wide digging fork.\n- **Operational Scale**: Nursery beds require hand trowels and watering cans; half-acre plots require animal draft or motorized tillers.\n- **User Ergonomics**: Handle length and tool weight must match the operator's height to prevent lower lumbar back strain."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Task-Tool Matching vs Mismatch Matrix",
                        "content": {
                            "title": "Task-Tool Matching Evaluation Matrix",
                            "headers": ["Field Operation", "Optimal Matched Tool", "Incorrect Mismatched Tool", "Operational Penalty / Risk"],
                            "rows": [
                                ["Pruning soft tomato suckers", "Bypass Secateurs (sharp)", "Blunt Panga / Machete", "Crushed vascular tissue; fungal infection"],
                                ["Scooping & moving dry manure", "Concave Shovel", "Flat Cutting Spade", "Spilled manure; 3x slower loading time"],
                                ["Digging stony / hard clay soil", "Fork Jembe (Tined)", "Flat-bladed Jembe", "Blade bouncing; high user exhaustion"],
                                ["Transplanting delicate seedlings", "Hand Trowel", "Standard Digging Spade", "Destroyed root ball; severe transplant shock"],
                                ["Tightening seized machine bolt", "Ring Spanner", "Pliers / Adjustable wrench", "Slipping jaws; rounded hex bolt corners"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Problem-Solving Simulation: Diagnosing Farm Tool Mismatch",
                        "content": {
                            "title": "Tool Selection Problem-Solving Case",
                            "task": "A worker is using a flat digging spade to weed a row of young capsicum seedlings. He is struggling with deep couch grass roots and accidentally cuts 4 crop stems.\n\n1. Explain why the spade is the wrong tool for this task.\n2. Recommend two optimal alternative implements.\n3. Outline the ergonomic and crop health benefits of the correct tools.",
                            "materials": ["Case Handout", "Pen"],
                            "safety": "Ensure analytical, evidence-based reasoning."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Task-Tool Matching",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Task-tool matching maximizes speed and mechanical efficiency**.\n- **Tool mismatch causes crop disease, tool breakage, and handler injury**.\n- **Select tools based on soil, crop stage, scale, and ergonomics**.\n- **Never use cutting tools for prying, or prying tools for cutting**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Task-Tool Matching",
                        "content": {
                            "question": "Why is it considered dangerous and mechanically incorrect to use a digging fork to clear thick, woody tree brush?",
                            "options": [
                                "Digging forks are too heavy to lift off the ground",
                                "The steel tines of a digging fork are engineered for soil penetration and lifting manure; they have no cutting edges and will bend, snap, or dangerously glance off woody stems, risking severe user injury",
                                "Wood releases toxic acids that melt fork tines",
                                "Digging forks can only be operated with diesel engines"
                            ],
                            "answer": "B",
                            "explanation": "A digging fork is designed for soil loosening and manure lifting. Its blunt, slender tines cannot cut wood. Forcing a fork against woody branches bends the tines, damages the tool, and creates an extreme slip hazard that can strike the operator."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Gardening Tools - Digging & Preparing
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Gardening Tools - Digging & Preparing",
            "unit_description": "Anatomy and functions of Jembe vs Fork Jembe; Spade (cutting/edging) vs Shovel (scooping/moving); Rake tilth leveling and stone clearing.",
            "lesson_title": "Primary Soil Cultivation: Anatomy and Functional Mechanics of Jembes, Spades, Shovels, and Rakes",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Workers Digging and Cultivating Soil with Jembes",
                        "content": {
                            "title": "Agricultural Workers Digging and Cultivating Soil with Jembes",
                            "caption": "Farm workers executing primary land preparation using heavy steel jembes, breaking soil clods and preparing planting rows."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Digging Tools",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the physical parts and functions of the **Jembe, Fork Jembe, Spade, Shovel, and Rake**.",
                                "Analyze the critical functional differences between a **Spade (cutting/edging)** and a **Shovel (scooping/moving)**.",
                                "Execute **secondary seedbed leveling and trash clearing** using a rake.",
                                "Demonstrate safe, ergonomic digging postures to prevent spinal strain."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Jembe (Hoe) and Fork Jembe",
                        "content": {
                            "title": "Primary Cultivation Powerhouses",
                            "text": "1. **The Jembe (Hoe)**: Features a broad, flat carbon steel blade attached to a long wooden or metal handle through a forged eyelet. Used for primary tillage, digging planting holes, weeding, and creating ridges in soft to medium soils.\n2. **The Fork Jembe**: Replaces the solid flat blade with 3 or 4 heavy, thick steel tines. Specially matched to **hard, compacted soils, stony terrain, or ground bound by stubborn rhizomes (couch grass)**. The tines pierce hard crusts easily with minimal surface resistance and do not cake up with sticky clay."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Spade vs. Shovel: Structural and Functional Anatomy",
                        "content": {
                            "title": "Never Confuse a Spade with a Shovel",
                            "text": "- **The Spade**: Flat, rectangular steel blade with a sharp, straight cutting edge and a short **D-handle** (or T-handle). Engineered for **cutting** soil edges, digging clean vertical-walled trenches, slicing turf, and dividing perennial root clumps.\n- **The Shovel**: Broad, concave (curved scoop) steel blade with raised side edges and a long straight handle. Engineered for **scooping, lifting, and moving loose materials** (manure, compost, sand, gravel, harvested grain). Never use a spade for scoop-moving loose materials, or a shovel for cutting hard ground!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Spade vs Shovel Structural & Functional Anatomy",
                        "content": {
                            "title": "Spade vs Shovel Structural & Functional Anatomy",
                            "caption": "Anatomical comparison: Left: Spade (Flat rectangular blade, sharp straight edge, D-handle, used for cutting & edging) | Right: Shovel (Concave scoop blade, curved raised edges, long handle, used for moving loose materials)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Garden Rake: Secondary Tillage and Tilth Preparation",
                        "content": {
                            "title": "Creating the Perfect Seedbed",
                            "text": "The **garden rake** consists of a wide steel head with 12–16 short, sturdy, perpendicular tines mounted on a long wooden shaft:\n\n- **Seedbed Leveling**: Pulled across freshly dug soil in short, controlled strokes to break up fine clods and create a flat, uniform seedbed.\n- **Debris and Stone Removal**: Gathers surface weed trash, roots, and small gravel stones that would obstruct delicate germinating seeds.\n- **Ergonomics**: Keep your back upright, grip with hands wide apart, and pull using arm muscles rather than bending your spine."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Digging and Preparing Tools Comparison Matrix",
                        "content": {
                            "title": "Soil Preparation Implements Matrix",
                            "headers": ["Tool Name", "Blade / Head Structure", "Handle Type", "Primary Soil Operation", "Operational Limitation"],
                            "rows": [
                                ["Jembe (Hoe)", "Broad, flat carbon steel blade", "Long wooden shaft", "Primary digging, weeding, ridging", "Cakes up in sticky, wet clay soils"],
                                ["Fork Jembe", "3 or 4 heavy curved steel tines", "Long wooden shaft", "Digging stony ground & couch grass", "Cannot move loose soil or level beds"],
                                ["Spade", "Flat rectangular blade, sharp edge", "Short D-handle", "Cutting soil edges, digging trenches", "Very poor for scooping loose bulk materials"],
                                ["Shovel", "Concave, scoop-shaped blade", "Long straight shaft", "Scooping & loading manure, sand, soil", "Cannot cut through hard, unploughed soil"],
                                ["Rake", "Horizontal bar with short tines", "Long wooden shaft", "Leveling seedbed, collecting weed trash", "Cannot be used for digging or prying"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Seedbed Tillage, Trenching, and Leveling Lab",
                        "content": {
                            "title": "Soil Tillage and Tool Handling Practicum",
                            "task": "1. In a designated garden plot, use a fork jembe to break compacted soil.\n2. Use a spade to cut a straight 30cm deep edge along the plot boundary.\n3. Use a shovel to transfer 2 wheelbarrows of compost onto the bed.\n4. Use a rake to level the seedbed and clear surface stones.",
                            "materials": ["Fork Jembe", "Spade", "Shovel", "Rake", "Wheelbarrow"],
                            "safety": "Maintain safe 3-meter spacing between student diggers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Digging Tools",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Jembes are for general digging**; **fork jembes conquer stony/clay soils**.\n- **Spades are for cutting clean soil edges**; **shovels are for scooping loose materials**.\n- **Rakes level seedbeds and remove stones** for optimal seed germination.\n- **Maintain a wide, balanced stance** to protect your lower back."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Selecting Between Spade and Shovel",
                        "content": {
                            "question": "A student needs to transfer 500 kg of decomposed cow manure from a compost pit into a wheelbarrow. Which tool should she select for maximum efficiency, and why?",
                            "options": [
                                "A spade, because its sharp flat blade can slice through timber",
                                "A shovel, because its broad, concave scoop-shaped blade is engineered to hold and lift maximum volumes of loose material without spilling",
                                "A rake, because its tines will aerate the manure",
                                "A fork jembe, because it makes the manure dry"
                            ],
                            "answer": "B",
                            "explanation": "A shovel features a deep, concave, bowl-like blade designed specifically for scooping, lifting, and transferring loose bulk materials (manure, sand, compost). Using a flat spade would result in manure constantly spilling off the sides, multiplying labor time."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Gardening Tools - Cutting & Pruning
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Gardening Tools - Cutting & Pruning",
            "unit_description": "Heavy clearing with Panga; precision stem pruning with Secateurs; pruning saw; vascular tissue damage and fungal entry caused by dull blades.",
            "lesson_title": "Vegetative Management: Cutting Implements, Precision Secateurs, and Plant Vascular Health",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Agricultural Worker Pruning Fruit Tree Branches with Bypass Secateurs",
                        "content": {
                            "title": "Agricultural Worker Pruning Fruit Tree Branches with Bypass Secateurs",
                            "caption": "A worker using precision bypass secateurs to make clean, angled cuts on vegetative branches, promoting rapid healing and preventing pathogen entry."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Cutting & Pruning",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Identify the physical properties and uses of the **Panga (Machete), Secateurs (Pruning Shears), and Pruning Saw**.",
                                "Analyze how **dull cutting blades crush plant vascular bundles (xylem/phloem)**, inviting fungal infections.",
                                "Differentiate between **bypass secateurs and anvil secateurs**.",
                                "Execute safe handling, swing clearance, and sharpening protocols for cutting tools."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Panga (Machete): Heavy Clearing and Harvesting",
                        "content": {
                            "title": "The East African Universal Cutting Blade",
                            "text": "- **Structure**: Heavy, broad carbon steel blade with a weighted curved tip and a riveted wooden or plastic handle.\n- **Uses**: Bush clearing, chopping thick stalks (maize/sugarcane), dividing compost material, and sharpening wooden fencing stakes.\n- **Safety Swing Rule**: Always maintain a **$3\\text{--}4\\text{ meter}$ peripheral clearance radius** from other workers when swinging a panga. Never swing towards your legs or supporting hand!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Secateurs and Pruning Saws: Precision Horticultural Surgery",
                        "content": {
                            "title": "Protecting Plant Stems During Pruning",
                            "text": "1. **Secateurs (Bypass Pruning Shears)**: Spring-loaded handheld shears with a sharp curved blade that glides past a thick counter-hook (scissor action). Cuts soft stems up to **$2\\text{ cm}$ diameter** cleanly without crushing delicate bark.\n2. **Pruning Saw**: Compact hand saw with a curved blade and sharp, backward-pointing pull-cut teeth. Used for branches **$>2\\text{ cm}$ diameter** (coffee, avocado, mango) where secateurs would jam or snap."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Blade Sharpness and Plant Vascular Pathology",
                        "content": {
                            "title": "The Biological Link Between Sharp Tools and Disease Defense",
                            "text": "- **Sharp Blade Cut**: Produces a flat, smooth, minimal surface area cut. The plant's cambium layer quickly seals the wound with callus tissue within **24 to 48 hours**.\n- **Dull Blade Cut**: Crushes, tears, and shreds the **xylem and phloem vascular tissue**, creating a ragged, bruised surface with high sap weeping. Fungal spores (*Fusarium*, *Botrytis*) and bacteria easily infect this dead, damp tissue, causing systemic dieback and crop loss!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Cutting and Pruning Implements Matrix",
                        "content": {
                            "title": "Cutting Implement Comparison Matrix",
                            "headers": ["Tool Name", "Cutting Mechanism", "Max Branch Diameter", "Optimal Horticultural Task", "Pathology Risk if Dull"],
                            "rows": [
                                ["Bypass Secateurs", "Scissor-action bypass blade", "Up to 2.0 cm", "Pruning tomato suckers, roses, coffee", "Bark tearing; stem fungal canker"],
                                ["Pruning Saw", "Pull-stroke curved teeth", "2.0 cm to 15.0 cm", "Pruning mature fruit tree limbs", "Jagged bark tearing; heart rot entry"],
                                ["Panga (Machete)", "Heavy momentum impact slash", "Up to 5.0 cm (Woody brush)", "Land clearing, harvesting sugarcane", "Severe stem splintering; dangerous slips"],
                                ["Hedge Shears", "Dual long scissor blades", "Light foliage hedges", "Trimming ornamental & live fences", "Chewed, brown, dying leaf tips"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Microscopic Stem Wound Examination Lab",
                        "content": {
                            "title": "Pruning Quality and Wound Inspection Practicum",
                            "task": "1. Make a cut on a scrap branch using a razor-sharp secateur at a 45° angle just above a bud.\n2. Make a second cut on a similar branch using a blunt panga.\n3. Examine both cut surfaces with a 10x magnifying hand lens.\n4. Sketch the smooth sealed vascular ring vs the shredded crushed fibers.",
                            "materials": ["Sharp Secateur", "Blunt Panga", "Hand Lens", "Branch Scraps"],
                            "safety": "Keep fingers clear of all cutting blades."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Cutting & Pruning",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Pangas are for heavy clearing**; **secateurs are for precision pruning**.\n- **Always maintain a 3m safety swing zone** when using pangas.\n- **Sharp blades make clean cuts that heal rapidly**.\n- **Dull blades crush vascular bundles**, causing fungal stem infections."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Biological Rationale for Sharp Secateurs",
                        "content": {
                            "question": "Why is it strictly recommended in commercial horticulture to prune tomato vines and fruit trees using razor-sharp bypass secateurs rather than a sharp panga?",
                            "options": [
                                "Secateurs make the fruit grow twice as sweet",
                                "Secateurs make clean, scissor-like slices that heal rapidly, whereas pangas exert blunt momentum force that crushes plant vascular tissues and creates jagged wounds where fungal pathogens enter",
                                "Pangas are illegal to use on tomato farms",
                                "Secateurs spray liquid fungicide while cutting"
                            ],
                            "answer": "B",
                            "explanation": "Bypass secateurs act like precision surgical scissors, producing clean, smooth cuts that minimize cellular damage. Pangas rely on impact force, which inevitably crushes the delicate xylem and phloem vessels, causing sap leakage and leaving frayed wounds that invite fungal and bacterial dieback."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Gardening Tools - Planting & Irrigation
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Gardening Tools - Planting & Irrigation",
            "unit_description": "Hand Trowel and root ball preservation against transplanting shock; Watering can with perforated Rose nozzle; Wheelbarrow as Class 2 lever; adjustable hose pipes.",
            "lesson_title": "Establishment and Moisture Engineering: Hand Trowels, Rose Watering Cans, and Wheelbarrows",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Hand Trowels Used for Sowing and Transplanting Vegetable Seedlings",
                        "content": {
                            "title": "Hand Trowels Used for Sowing and Transplanting Vegetable Seedlings",
                            "caption": "Hand trowels with curved scoop blades used to extract delicate nursery seedlings with intact soil root balls, minimizing transplanting shock."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Planting & Irrigation",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how the **hand trowel reduces transplanting shock by preserving intact root balls**.",
                                "Analyze the hydraulic function of the **watering can's perforated rose nozzle** in preventing soil erosion.",
                                "Apply the physics of a **Class 2 lever in safe wheelbarrow operation**.",
                                "Configure **adjustable hose pipe nozzles** for nursery beds vs mature orchards."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Hand Trowel: Preventing Transplanting Shock",
                        "content": {
                            "title": "Surgical Transplanting in Vegetable Nursery Beds",
                            "text": "- **Structure**: Small handheld tool with a curved, scoop-shaped steel blade ($15\\text{ cm}$) and an ergonomic wooden/rubber grip.\n- **The Root Ball Principle**: When moving young seedlings (kale, tomato, capsicum) from a nursery bed, the trowel is plunged deep into the soil to lift the seedling along with its complete, undisturbed **soil root ball**.\n- **Preventing Shock**: Keeping the root ball intact protects the microscopic root hairs from tearing, drying out, or experiencing **transplanting shock**, ensuring immediate vigorous field growth."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Watering Can and Perforated Rose Nozzle",
                        "content": {
                            "title": "Gentle Hydraulic Irrigation",
                            "text": "- **Structure**: Portable galvanized or plastic container (5–10 liters) with a long spout ending in a perforated head called the **Rose**.\n- **Erosion & Washout Prevention**: The rose breaks a heavy water stream into thousands of tiny, gentle, rain-like droplets.\n  - Prevents high-velocity water impact from **washing away fine seeds**.\n  - Prevents splashing soil over tiny leaves or **caking the nursery surface**.\n  - Prevents physical snapping of tender seedling stems."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Wheelbarrow: Class 2 Lever Physics",
                        "content": {
                            "title": "Mechanical Transport on the Farm",
                            "text": "The **wheelbarrow** utilizes the physics of a **Class 2 lever** to move heavy farm loads (manure, rocks, harvested produce, soil):\n- **Fulcrum**: The front wheel axle.\n- **Load**: The heavy hopper in the middle.\n- **Effort**: The long handles lifted by the operator.\n- **Operating Rule**: Place the heaviest load towards the **front near the wheel** (closest to the fulcrum) so the wheel carries most of the weight, not your back!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Planting and Irrigation Tools Matrix",
                        "content": {
                            "title": "Planting & Watering Implement Matrix",
                            "headers": ["Tool Name", "Mechanical / Hydraulic Feature", "Primary Agronomic Task", "Operational Hazard if Misused"],
                            "rows": [
                                ["Hand Trowel", "Curved scoop blade, calibrated depth marks", "Transplanting seedlings with root ball", "Using to pry heavy rocks bends blade"],
                                ["Watering Can (with Rose)", "Perforated multi-hole sprinkler head", "Watering nursery beds & germinating seeds", "Removing rose causes seed washout & erosion"],
                                ["Wheelbarrow", "Class 2 lever (Front wheel fulcrum)", "Transporting bulk manure, soil & crops", "Overloading rear causes back injury & tipping"],
                                ["Hose Pipe (with Nozzle)", "Flexible PVC tube with pressure regulator", "Irrigating orchards & broad field beds", "High pressure directly on nursery blasts seedlings"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Field Practical: Seedling Transplanting and Rose Watering Lab",
                        "content": {
                            "title": "Transplanting and Irrigation Practicum",
                            "task": "1. Using a hand trowel, extract 3 kale seedlings from a nursery bed, keeping root balls intact.\n2. Plant seedlings at correct depth in a prepared garden row and firm the soil.\n3. Water using a watering can fitted with a perforated rose nozzle.\n4. Demonstrate proper wheelbarrow loading (weight centered over wheel).",
                            "materials": ["Hand Trowel", "Watering Can + Rose", "Kale Seedlings", "Wheelbarrow"],
                            "safety": "Keep back straight when lifting wheelbarrow handles."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Planting & Irrigation",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Hand trowels lift intact root balls**, eliminating transplanting shock.\n- **The watering can rose nozzle prevents seed washout** and soil erosion.\n- **Wheelbarrows operate as Class 2 levers**; load heavy weight near the front.\n- **Use fine mist nozzle settings** when watering delicate seedlings."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Watering Can Rose",
                        "content": {
                            "question": "Why is it mandatory to use a perforated rose nozzle when watering delicate vegetable nursery beds?",
                            "options": [
                                "It increases the temperature of the water",
                                "It breaks the heavy water stream into a soft rain-like spray, preventing soil erosion, seed washout, and seedling stem breakage",
                                "It adds chemical fertilizer to the water automatically",
                                "It prevents water from evaporating into the air"
                            ],
                            "answer": "B",
                            "explanation": "A direct stream from an open watering can spout generates high kinetic energy that washes away tiny seeds, erodes topsoil, and crushes delicate seedlings. The rose breaks the stream into a gentle rain, ensuring safe, even moisture infiltration."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Livestock Tools - Breeding & Identification
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Livestock Tools - Breeding & Identification",
            "unit_description": "Burdizzo castrator and bloodless spermatic cord crushing; Elastrator and rubber rings; Ear notchers (standardized code) and tattooing pliers; instrument sterilization.",
            "lesson_title": "Livestock Husbandry I: Bloodless Castration Mechanics, Ear Notching Systems, and Sterilization",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Burdizzo Castrator Tool for Bloodless Livestock Castration",
                        "content": {
                            "title": "Burdizzo Castrator Tool for Bloodless Livestock Castration",
                            "caption": "A heavy-duty Burdizzo castrator used to crush spermatic cords in male livestock through intact scrotal skin, eliminating open wound infections."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Breeding & Identification",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the anatomical and physiological mechanism of **bloodless castration using the Burdizzo**.",
                                "Operate the **elastrator and rubber rings** on young lambs and kids.",
                                "Decode and apply **standardized livestock ear notching codes and tattooing pliers**.",
                                "Enforce **chemical and thermal sterilization protocols** to prevent blood-borne pathogen transmission."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Burdizzo Castrator: Bloodless Castration Mechanics",
                        "content": {
                            "title": "Crushing the Spermatic Cord Through Intact Skin",
                            "text": "- **Structure**: Heavy forged steel compound-lever pincers that generate massive clamping force.\n- **The Mechanism**: The operator isolates the **spermatic cord and testicular blood vessels** inside the scrotum and clamps the Burdizzo jaws for **10 to 15 seconds** per cord.\n- **Pathological Outcome**: Blood supply to the testicle is completely severed without cutting the skin. The testicle atrophies (shrinks and reabsorbs) over several weeks.\n- **Welfare & Health Benefits**: Leaves **zero open wounds**, eliminating external hemorrhaging, bacterial entry, and fly-strike (myiasis)!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Elastrator and Rubber Rings",
                        "content": {
                            "title": "Bloodless Castration in Young Livestock (<2 Weeks)",
                            "text": "- **Structure**: 4-pronged expanding pliers used to stretch strong, thick rubber rings.\n- **Operation**: The stretched rubber ring is slipped over the scrotum (confirming both testicles are descended) and released at the scrotal neck.\n- **Outcome**: The tight rubber ring cuts off blood circulation. The scrotum and testicles shrivel, dry up, and fall off naturally within **2 to 3 weeks**.\n- *Safety*: Must be paired with maternal tetanus antibody coverage or tetanus antitoxin injections."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Livestock Castration Tools: Burdizzo vs Elastrator",
                        "content": {
                            "title": "Livestock Castration Tools: Burdizzo vs Elastrator",
                            "caption": "Comparative castration engineering: Left: Burdizzo Castrator (Heavy compound pincers, crushes spermatic cord in mature animals) | Right: Elastrator (4-prong pliers, expands rubber rings for young lambs/kids)."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Identification Tools: Ear Notchers and Tattooing Pliers",
                        "content": {
                            "title": "Lifetime Farm Record Systems",
                            "text": "1. **Ear Notchers**: Precision pliers that punch small V-shaped notches in specific positions on the pig or sheep ear cartilage. Positions on the upper/lower edges and tip represent numerical values (1, 3, 9, 27, 81), providing permanent, readable individual IDs.\n2. **Tattooing Pliers**: Pliers holding interchangeable needle-pointed digits dipped in black indelible ink, pressed into the inner ear of rabbits, goats, or cattle.\n3. **MANDATORY STERILIZATION**: All notchers and needles must be soaked in **$70\\%$ methylated spirit or chlorine disinfectant** between animals to prevent transmitting viral pathogens (e.g., African Swine Fever, Bovine Leukosis)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Breeding and Identification Tools Matrix",
                        "content": {
                            "title": "Breeding & Identification Implement Matrix",
                            "headers": ["Tool Name", "Working Mechanism", "Target Livestock Category", "Sterilization Protocol Required"],
                            "rows": [
                                ["Burdizzo Castrator", "Crushes spermatic cord through intact skin", "Bulls, rams, bucks (>2 months old)", "Wipe jaws with disinfectant before/after"],
                                ["Elastrator & Rings", "Contracting rubber ring cuts blood supply", "Young lambs and kids (<2 weeks old)", "Disinfect pliers; clean rubber rings"],
                                ["Ear Notchers", "Punches V-shaped notch code in cartilage", "Piglets and breeding swine", "Soak in 70% spirit between every pig!"],
                                ["Tattooing Pliers", "Needle points inject black ink under skin", "Rabbits, dairy calves, pedigree sheep", "Dip needles in disinfectant between animals"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Ear Notching Code Deciphering and Paper Model Lab",
                        "content": {
                            "title": "Ear Notching Systems Practicum",
                            "task": "1. Using a standard 1-3-9-27-81 ear notching chart, decode a pig with ID #47.\n2. Cut cardboard pig ear models and use safety scissors to punch the correct V-notches.\n3. Practice disinfecting surgical instruments using methylated spirit swabs.",
                            "materials": ["Cardboard Ear Templates", "Scissors", "Numbering Chart", "Spirit Swabs"],
                            "safety": "Handle all sharp cutting pliers with care."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Breeding & Identification",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Burdizzo crushes spermatic cords bloodlessly**, preventing open wound infections.\n- **Elastrators are for young animals (<2 weeks)** using rubber rings.\n- **Ear notchers and tattoos provide permanent individual IDs**.\n- **Always sterilize identification tools in 70% spirit** between animals."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Physiological Advantage of the Burdizzo",
                        "content": {
                            "question": "What is the primary physiological and disease-prevention advantage of using a Burdizzo castrator over open surgical knife castration in tropical cattle rearing?",
                            "options": [
                                "The Burdizzo makes the cattle grow horns twice as fast",
                                "The Burdizzo crushes the spermatic cords through intact scrotal skin, eliminating open surgical wounds, external hemorrhaging, and fly-strike (myiasis) infections",
                                "The Burdizzo is fully automated and runs on solar power",
                                "The Burdizzo changes the animal's coat color to white"
                            ],
                            "answer": "B",
                            "explanation": "In tropical and pasture environments, open surgical wounds are highly vulnerable to bacterial contamination and blowfly egg deposition (fly-strike/myiasis). The Burdizzo is a bloodless castrator: it crushes the internal spermatic blood vessels through the skin, leaving no open wound."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Livestock Tools - Health & Feeding
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Livestock Tools - Health & Feeding",
            "unit_description": "Oral drenching gun and horizontal head alignment preventing lethal aspiration pneumonia; Syringes & needle gauge selection (IM vs Sub-Q); Disbudding iron vs Gigli saw wire.",
            "lesson_title": "Livestock Husbandry II: Oral Drenching Dynamics, Syringe Injections, and Disbudding Irons",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Veterinary Officer Administering Vaccination Injection to Livestock",
                        "content": {
                            "title": "Veterinary Officer Administering Vaccination Injection to Livestock",
                            "caption": "A veterinary professional administering an intramuscular injection using a sterile syringe and needle, maintaining proper animal restraint and sterile protocol."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Health & Feeding Tools",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Operate an **oral drenching gun** with correct horizontal head alignment to prevent fatal aspiration pneumonia.",
                                "Select and handle **syringes and needles for Intramuscular (IM) vs Subcutaneous (Sub-Q)** injections.",
                                "Compare **thermal disbudding irons** with **dehorning wire (Gigli wire)**.",
                                "Enforce needle hygiene and dosage calibration standards."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Oral Drenching Gun: Preventing Aspiration Pneumonia",
                        "content": {
                            "title": "Administering Liquid Anthelmintics Safely",
                            "text": "- **Structure**: Calibrated spring-loaded syringe with a long, curved, blunt metal nozzle.\n- **The Nozzle Position**: Insert nozzle into the side of the mouth (the toothless **diastema space**) over the base of the tongue.\n- **THE HORIZONTAL HEAD RULE**: Keep the animal's head **level and horizontal**!\n  - *Danger of Vertical Head Angle*: If the head is pulled vertically towards the sky, the epiglottis cannot close over the windpipe. The liquid floods the **trachea and lungs**, causing acute drowning or fatal **Aspiration Pneumonia** within 48 hours!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Syringes, Needles, and Injection Routes",
                        "content": {
                            "title": "Precision Medication Delivery",
                            "text": "1. **Intramuscular (IM)**: Needle inserted at **$90^\\circ$ straight into deep muscle tissue** (thick neck muscle). Fast absorption via rich blood supply.\n2. **Subcutaneous (Sub-Q)**: Needle inserted at **$45^\\circ$ into the loose skin fold** (tenting the skin behind the shoulder/neck). Slower, sustained vaccine absorption.\n3. **Needle Gauge Rule**: Thick viscous drugs require heavy gauge ($16\\text{--}18\\text{ G}$); small animals/vaccines use finer gauge ($20\\text{--}22\\text{ G}$). Always discard bent or blunt needles!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Disbudding and Dehorning Tools",
                        "content": {
                            "title": "Preventing Horn Growth for Herd Safety",
                            "text": "- **Electric / Hot Iron Disbudder**: Heated copper head applied over the horn bud of calves/kids at **$1\\text{ to }3\\text{ weeks old}$** for 10–15 seconds to cauterize the horn-growing germinal ring. Bloodless and humane.\n- **Dehorning Wire (Gigli Wire)**: Flexible abrasive saw wire used to cut fully grown horns on adult cattle. Causes heavy bleeding; requires immediate hot-iron cauterization.\n- *Conclusion*: Early disbudding is infinitely superior to adult dehorning!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Livestock Health & Feeding Tools Matrix",
                        "content": {
                            "title": "Livestock Health Implement Matrix",
                            "headers": ["Tool Name", "Target Route / Site", "Primary Clinical Purpose", "Critical Safety Rule"],
                            "rows": [
                                ["Drenching Gun", "Oral (Over tongue base)", "Administering liquid dewormers", "Keep head horizontal; never raise vertically!"],
                                ["Hypodermic Syringe & Needle", "Intramuscular (Neck) / Sub-Q", "Injecting vaccines & antibiotics", "Sterilize/replace needle; never inject into veins"],
                                ["Hot Iron Disbudder", "Horn bud of young calf (1–3 wks)", "Cauterizes horn-growing cells bloodlessly", "Apply for only 10–15s to prevent brain damage"],
                                ["Balling Gun / Bolus Applicator", "Oral (Deep pharynx)", "Administering large solid mineral tablets", "Guide over tongue gently without puncturing throat"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Simulation Practical: Safe Drenching Alignment and Syringe Calibration",
                        "content": {
                            "title": "Veterinary Tool Handling Practicum",
                            "task": "1. Using a drenching gun, calibrate the dosage ring to exactly 15ml of water.\n2. On a model animal, practice holding the muzzle level and inserting the nozzle into the diastema.\n3. Practice 'tenting' loose skin to demonstrate a Sub-Q injection angle.\n4. Demonstrate proper needle disposal in a sharps container.",
                            "materials": ["Drenching Gun", "Syringe + Needles", "Model Plush Animal", "Sharps Container"],
                            "safety": "Never practice injections on human classmates."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Health & Feeding Tools",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Hold the head level when drenching** to prevent fatal aspiration pneumonia.\n- **IM injections go deep at 90°**; **Sub-Q injections go under skin folds at 45°**.\n- **Disbud calves early (1–3 weeks)** using a thermal hot iron.\n- **Dispose of used needles in a puncture-proof sharps container**."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Drenching Head Angle Hazard",
                        "content": {
                            "question": "Why is it an extremely dangerous error to lift a sheep's head vertically towards the sky when administering liquid dewormer with a drenching gun?",
                            "options": [
                                "The liquid medicine will leak out of the animal's nostrils",
                                "Lifting the head excessively high prevents the epiglottis reflex from closing over the larynx, allowing the liquid drug to drain into the trachea and lungs, causing fatal aspiration pneumonia",
                                "The sheep will bite and break the metal drenching nozzle",
                                "It causes the sheep's horns to fall off immediately"
                            ],
                            "answer": "B",
                            "explanation": "When an animal's muzzle is elevated vertically, the natural swallowing reflex is paralyzed and the epiglottis cannot close the airway. The drenching fluid pours directly down the open trachea into the lungs, causing acute respiratory distress and fatal aspiration pneumonia."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Livestock Tools - Grooming & Harvesting
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Livestock Tools - Grooming & Harvesting",
            "unit_description": "Hoof cutters preventing *Fusobacterium* hoof rot; Sheep hand shears and piglet tooth clippers; Seamless milking buckets, milk strainers, and dark-bottom Strip Cups for mastitis diagnosis.",
            "lesson_title": "Livestock Husbandry III: Hoof Trimming Shears, Wool Shears, and Hygienic Dairy Utensils",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Steel Sheep Shears Used for Wool Harvesting",
                        "content": {
                            "title": "Traditional Steel Sheep Shears Used for Wool Harvesting",
                            "caption": "Spring-loaded steel hand shears used for humane wool harvesting and fleece trimming in sheep production enterprises."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Grooming & Harvesting",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Operate **hoof trimming shears and knives** to prevent *Fusobacterium necrophorum* hoof rot.",
                                "Execute wool harvesting using **sheep hand shears**.",
                                "Operate **piglet tooth clippers** to prevent sow udder trauma.",
                                "Utilize **seamless milking buckets, milk strainers, and dark-bottom strip cups** for mastitis detection."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hoof Cutters: Halting Bacterial Hoof Rot",
                        "content": {
                            "title": "Podiatry in Ruminant Welfare",
                            "text": "- **The Pathology**: Overgrown keratin hooves curl inward, trapping mud, manure, and moisture against the soft sole. Anaerobic bacteria (*Fusobacterium necrophorum*) proliferate, rotting the hoof tissue and causing severe lameness, pain, and drop in milk yield.\n- **The Operation**: Use heavy-duty hoof shears and a curved hoof knife to trim excess horn wall flat and level with the sole pads, exposing clean, dry keratin."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Wool Shears and Piglet Tooth Clippers",
                        "content": {
                            "title": "Specialized Welfare Implements",
                            "text": "1. **Sheep Hand Shears**: Spring-loaded steel blades that cut wool fibers close to the skin without gouging. Regular shearing prevents wool-matted sweat, which attracts blowflies (**fly-strike**).\n2. **Piglet Tooth Clippers**: Small sharp cutting pincers used within 24 hours of birth to clip the tips of the 8 needle teeth (canines). This prevents piglets from lacerating the sow's teats during suckling (which causes mastitis) and prevents facial wounding during litter fights."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Hygienic Dairy Milking Equipment",
                        "content": {
                            "title": "Harvesting Clean, Pathogen-Free Milk",
                            "text": "- **Seamless Stainless Steel / Aluminum Pail**: Seamless design eliminates microscopic cracks and corners where milk-spoiling bacteria (*Lactobacillus*, *Coliforms*) hide.\n- **Milk Strainer**: Fitted with single-use filter discs to strain physical hairs, straw, and dust before bulk cooling.\n- **The Strip Cup**: A metal cup with a black mesh lid. Squirting the first 2–3 streams of fore-milk onto the black surface allows the milker to visually spot **white clots, flakes, or watery secretions**—the diagnostic clinical indicators of **mastitis**!"
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Grooming and Harvesting Implements Matrix",
                        "content": {
                            "title": "Grooming & Dairy Equipment Matrix",
                            "headers": ["Implement Name", "Material / Structural Feature", "Primary Agronomic Function", "Animal Health / Quality Benefit"],
                            "rows": [
                                ["Hoof Shears / Knife", "Hardened steel cutting jaws", "Trimming overgrown hoof wall flat", "Prevents anaerobic bacterial hoof rot & lameness"],
                                ["Sheep Hand Shears", "Spring-steel bypass blades", "Harvesting clean wool fleece", "Prevents fleece-matted sweat and fly-strike"],
                                ["Tooth Clipper", "Micro-pincer cutting head", "Clipping newborn piglet needle teeth", "Prevents sow teat lacerations & piglet facial cuts"],
                                ["Strip Cup", "Dark/black inner surface mug", "Squirt-testing fore-milk for clots", "Detects mastitis infection before bulk contamination"],
                                ["Milk Strainer", "Stainless sieve + filter disc", "Straining milk before storage", "Removes physical hairs, debris, and dirt particles"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Simulation Practical: Strip Cup Mastitis Diagnostic Test Lab",
                        "content": {
                            "title": "Mastitis Detection Practicum",
                            "task": "1. Set up two milk samples: Sample A (pure white milk) and Sample B (milk containing fine white flour flakes representing mastitic clots).\n2. Squirt Sample A onto the black plate of a strip cup; observe the clean flow.\n3. Squirt Sample B onto the black plate; observe the high-contrast white clots.\n4. Document the protocol for isolating a mastitic cow.",
                            "materials": ["Strip Cup", "Normal Milk", "Simulated Mastitic Milk"],
                            "safety": "Maintain strict food-grade cleanliness with dairy utensils."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Grooming & Harvesting",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Trim hooves flat to prevent bacterial hoof rot** and lameness.\n- **Clip piglet needle teeth within 24h** to protect sow teats from mastitis.\n- **Use seamless stainless steel milking pails** for zero bacterial harbor.\n- **Squirt fore-milk into a dark strip cup** to catch mastitis clots early."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Function of the Dark-Bottom Strip Cup",
                        "content": {
                            "question": "What is the primary diagnostic purpose of squirting the first streams of milk into a dark-bottom strip cup before full machine or hand milking?",
                            "options": [
                                "To measure the exact volume of milk in the udder",
                                "To visually detect white curd clots, flakes, or watery secretions against the black background, diagnosing mastitis infection before contaminated milk enters the clean bulk bucket",
                                "To cool the cow's teats before milking",
                                "To feed the farm barn cats"
                            ],
                            "answer": "B",
                            "explanation": "A strip cup is an essential diagnostic screening tool. Squirting the first milk onto its dark black surface allows the milker to visually spot white flakes, clots, or discoloration that signal clinical mastitis (bacterial udder infection), allowing infected milk to be discarded."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 9: Assembling Tasks - Threaded Fasteners
        # =====================================================================
        {
            "unit_order": 9,
            "unit_name": "Assembling Tasks - Threaded Fasteners",
            "unit_description": "Open-ended spanner vs Ring spanner (multi-point grip preventing corner rounding); adjustable wrenches; flathead vs Phillips screwdrivers; flat washers and thread lubrication.",
            "lesson_title": "Mechanical Assembly: Spanners, Ring Wrenches, Screwdrivers, and Fastener Dynamics",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Mechanic Workshop Tool Set with Spanners and Socket Wrenches",
                        "content": {
                            "title": "Mechanic Workshop Tool Set with Spanners and Socket Wrenches",
                            "caption": "A precision mechanic's tool set displaying combination ring-and-open spanners, socket wrenches, and drivers used for farm machinery and structural assembly."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Fastening & Assembling",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Compare **Open-Ended Spanners vs Ring Spanners vs Adjustable Wrenches**.",
                                "Analyze how **Ring Spanners provide multi-point torque distribution, preventing bolt corner rounding**.",
                                "Select matching **Flathead and Phillips screwdrivers**.",
                                "Apply **flat washers and anti-seize oil** to construct durable, vibration-resistant farm structures."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Spanner Ecosystem: Open-Ended vs Ring Spanner",
                        "content": {
                            "title": "Torque Transmission Physics",
                            "text": "1. **Open-Ended Spanner**: U-shaped jaw that slides onto a hex bolt from the side. Fast in confined spaces, but contacts only **2 flat sides**. Under high torque, the jaws can spread or slip, stripping and **rounding off the bolt corners**!\n2. **Ring Spanner**: Fully enclosed circular ring with 6 or 12 internal broached teeth. Encircles all corners of the hex bolt, distributing rotational torque evenly across all contact points. **Zero slippage risk**—the safest tool for breaking seized bolts!\n3. **Combination Spanner**: Open jaw at one end for fast spinning, ring head at the other end for final high-torque clamping."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Screwdrivers, Pliers, and Washers",
                        "content": {
                            "title": "Precision Fastening Standards",
                            "text": "- **Screwdrivers**: **Flathead (Slotted)** has a single flat wedge; **Phillips (+)** has a cross-recessed head. Using the wrong tip strips the screw head, creating an unextractable burr.\n- **Pliers**: **Combination Pliers** have serrated gripping jaws and wire cutters; **Long-Nose Pliers** reach into tight mechanical housings.\n- **The Rule of Washers**: Always place a **flat steel washer** under both the bolt head and nut. Washers distribute clamping pressure, prevent the bolt from crushing soft wood, and stop nuts from vibrating loose."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Open-Ended vs Ring Spanner Mechanical Torque Distribution",
                        "content": {
                            "title": "Open-Ended vs Ring Spanner Mechanical Torque Distribution",
                            "caption": "Torque mechanics: Left: Open-Ended Spanner (2-point contact, risk of spreading jaws and rounding hex bolt corners) | Right: Ring Spanner (Full multi-tooth enclosed grip, 100% torque distribution, zero slip)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Fastening and Assembly Tools Comparison",
                        "content": {
                            "title": "Assembly & Fastening Tools Matrix",
                            "headers": ["Tool Name", "Grip Mechanism", "Torque Capacity", "Primary Mechanical Task", "Risk if Incorrectly Used"],
                            "rows": [
                                ["Ring Spanner", "Enclosed circular 6/12-point teeth", "Very High", "Tightening/loosening heavy machine bolts", "Cannot slide on from the side in tight gaps"],
                                ["Open-Ended Spanner", "U-shaped dual jaw", "Moderate", "Fast assembly in tight side clearances", "Slips under high torque; rounds bolt corners"],
                                ["Adjustable Wrench", "Worm-screw adjustable jaw", "Moderate", "Versatile matching to non-standard bolts", "Slips if turned toward movable jaw"],
                                ["Phillips Screwdriver", "Cross-shaped (+) driver tip", "Moderate", "Driving cross-recessed machine screws", "Cam-out strips screw head if size is wrong"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Workshop Practical: Safe Bolted Joint Assembly Lab",
                        "content": {
                            "title": "Bolted Joint Mechanical Assembly Practicum",
                            "task": "1. Select two pre-drilled timber pieces.\n2. Apply a drop of oil to a steel bolt thread.\n3. Fit flat washers under both the bolt head and the hex nut.\n4. Use an open-ended spanner to spin the nut and a ring spanner to apply final high torque.",
                            "materials": ["Timber Blocks", "Bolts & Nuts", "Washers", "Combination Spanners"],
                            "safety": "Pull the spanner toward your body; never push away to avoid knuckle injury."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Fastening & Assembling",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Ring spanners distribute torque evenly**, preventing stripped bolt corners.\n- **Open-ended spanners offer speed** in tight side spaces.\n- **Match screwdriver tips precisely** to avoid cam-out stripping.\n- **Always install flat washers** to prevent wood crushing and loose nuts."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Torque Distribution in Ring Spanners",
                        "content": {
                            "question": "Why is a ring spanner strongly preferred over an open-ended spanner when loosening a heavily seized, tight machine bolt on a farm tractor?",
                            "options": [
                                "Ring spanners are made of soft aluminum that bends easily",
                                "The ring spanner fully encloses the hex bolt head, distributing turning torque across all 6 corners simultaneously, preventing slippage and preventing the bolt corners from rounding off",
                                "Open-ended spanners can only turn counter-clockwise",
                                "Ring spanners lubricate the bolt with oil automatically"
                            ],
                            "answer": "B",
                            "explanation": "An open-ended spanner contacts only 2 points and can spread open under extreme torque, rounding off the hex corners. A ring spanner encloses the entire bolt head, distributing force across all six corners, providing maximum grip with zero slip."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 10: Disassembling Tasks - Cutting & Fabricating
        # =====================================================================
        {
            "unit_order": 10,
            "unit_name": "Disassembling Tasks - Cutting & Fabricating",
            "unit_description": "Hand saw mechanics (starter kerf, 45-degree blade angle); wire cutters and tension safety; Crowbars as Class 1 levers (fulcrum, load, effort).",
            "lesson_title": "Mechanical Fabrication: Hand Saw Physics, Wire Shearing, and Class 1 Lever Crowbars",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Swedish Hand Saw Used for Precision Wood Cutting and Carpentry",
                        "content": {
                            "title": "Swedish Hand Saw Used for Precision Wood Cutting and Carpentry",
                            "caption": "A classic timber hand saw with cross-cut teeth, demonstrating proper blade angle, straight handle grip, and wood cutting alignment."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Disassembly & Fabrication",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Execute timber cutting using a **hand saw ($45^\\circ$ angle, starter kerf)**.",
                                "Operate **wire cutters safely with tension control** to prevent eye recoil injuries.",
                                "Apply the physics of a **Class 1 lever using a crowbar / claw hammer**.",
                                "Extract seized nails and disassemble old farm structures without wood splintering."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Hand Saw: Geometry and Cutting Physics",
                        "content": {
                            "title": "Precision Timber Fabrication",
                            "text": "- **Structure**: Broad tempered carbon steel blade with alternating set teeth and a pistol grip.\n- **The 3-Step Sawing Protocol**:\n  1. *Mark the Line*: Draw a clean pencil line across the timber.\n  2. *The Starter Kerf*: Guide the blade with your thumb raised high, drawing the saw **backward 2–3 times** to establish a guide groove (**kerf**).\n  3. *The $45^\\circ$ Stance*: Stand with shoulder, elbow, and blade aligned. Saw at a **$45^\\circ$ angle to the wood surface** using long, rhythmic strokes, letting the weight of the saw do the cutting without forced downward pressure."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Wire Cutters and High-Tensile Tension Safety",
                        "content": {
                            "title": "Shearing Wire Without Recoil Hazards",
                            "text": "- **Mechanical Action**: Concentrates hand force through compound mechanical advantage onto two hardened carbide shear jaws.\n- **The Recoil Hazard**: When cutting fencing wire or cage mesh under tension, the severed ends snap back with extreme velocity.\n- **Safety Protocol**: Always hold the wire firmly on **both sides of the cut** and wear **polycarbonate safety goggles** to protect your eyes from flying wire ends!"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Crowbar: Class 1 Lever Physics",
                        "content": {
                            "title": "Multiplying Human Lifting Force",
                            "text": "A **crowbar (pinch bar)** is a heavy hexagonal steel bar with a wedged tip and a curved claw:\n- **Class 1 Lever Model**: **Fulcrum (Pivot block) in the middle**, Load at the short wedged end, Effort applied at the long handle tip.\n- **Mechanical Advantage**: Placing a small wooden block close to the nail/rock creates a massive force multiplier, popping stubborn $10\\text{ cm}$ nails straight out without bending the steel!"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Hand Saw Cutting Angles & Crowbar Class 1 Lever Mechanics",
                        "content": {
                            "title": "Hand Saw Cutting Angles & Crowbar Class 1 Lever Mechanics",
                            "caption": "Fabrication mechanics: Left: Hand Saw Operation (45° cutting angle, starter kerf groove) | Right: Crowbar Class 1 Lever (Effort -> Fulcrum Pivot Block -> Massive Upward Load Force)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Fabrication and Disassembly Implements Matrix",
                        "content": {
                            "title": "Disassembly & Fabrication Tools Matrix",
                            "headers": ["Tool Name", "Mechanical Action", "Physical Lever Class", "Primary Farm Task", "Essential Safety Rule"],
                            "rows": [
                                ["Hand Saw (Crosscut)", "Toothed cutting edge (Kerf)", "Direct mechanical friction", "Cutting building timber & posts", "Cut at 45° angle; guide kerf carefully"],
                                ["Wire Cutters (Side Nippers)", "Hardened wedge shear", "Class 1 double lever", "Cutting high-tensile wire & mesh", "Hold both sides of wire; wear goggles!"],
                                ["Crowbar / Claw Hammer", "Curved prying wedge", "Class 1 lever (Pivot in center)", "Extracting nails; lifting heavy posts", "Place fulcrum block close to the load"],
                                ["Hacksaw", "Fine replaceable blade", "Tensioned frame shear", "Cutting metal bolts & steel pipes", "Tension blade tightly; cut on forward push"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Workshop Practical: Timber Sawing and Levered Nail Extraction Lab",
                        "content": {
                            "title": "Sawing and Leverage Practicum",
                            "task": "1. Measure and mark a 50cm timber section; clamp in a bench vise.\n2. Cut a starter kerf and complete the cut at a 45° angle.\n3. Hammer a 4-inch nail halfway into scrap wood.\n4. Use a claw hammer with a wooden fulcrum block to extract the nail cleanly.",
                            "materials": ["Hand Saw", "Timber", "Claw Hammer", "4-inch Nails", "Fulcrum Block"],
                            "safety": "Wear safety goggles and keep free hand clear of the saw line."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Disassembly & Fabrication",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Saw timber at a 45° angle** following a starter kerf groove.\n- **Hold both sides of tensioned wire** when cutting to prevent recoil.\n- **Crowbars amplify force as Class 1 levers** using a pivot block.\n- **Wear safety goggles** during all cutting and prying tasks."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Hand Saw Cutting Angle",
                        "content": {
                            "question": "What is the optimal angle at which a carpenter's hand saw should be held relative to the timber surface during standard cross-cutting operations?",
                            "options": [
                                "90 degrees (perfectly vertical to the timber)",
                                "45 degrees (allowing optimal tooth engagement and rhythmic stroke control)",
                                "5 degrees (almost flat against the timber)",
                                "180 degrees (parallel to the grain)"
                            ],
                            "answer": "B",
                            "explanation": "Holding a hand saw at a 45-degree angle to the timber face ensures that the set teeth bite into the wood fibers with optimal cutting geometry, allowing smooth stroke momentum, clean kerf tracking, and minimal binding."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 11: Maintenance Practices - Cleaning and Sharpening
        # =====================================================================
        {
            "unit_order": 11,
            "unit_name": "Maintenance Practices - Cleaning and Sharpening",
            "unit_description": "5 Core pillars of tool care; scraping, washing, drying, and rust scouring; single forward-stroke flat filing at 30-degree bevel; oil whetstone circular stropping.",
            "lesson_title": "Tool Maintenance I: 5 Core Pillars, Rust Scrubbing Chemistry, and Precision Sharpening",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Sharpening a Cutting Blade on an Oil Whetstone",
                        "content": {
                            "title": "Sharpening a Cutting Blade on an Oil Whetstone",
                            "caption": "A workshop technician sharpening a precision cutting blade on an oiled whetstone, maintaining the factory bevel angle to restore razor sharpness."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Cleaning & Sharpening",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "List the **5 core pillars of tool maintenance (Clean, Sharpen, Lubricate, Repair, Store)**.",
                                "Execute **soil scraping, washing, drying, and kerosene rust scouring**.",
                                "Master the **single forward-stroke flat filing technique ($30^\\circ$ bevel angle)**.",
                                "Sharpen fine blades using an **oil whetstone in circular stropping motions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 5 Core Pillars of Tool Maintenance",
                        "content": {
                            "title": "Preventing Rust, Decay, and Premature Breakdown",
                            "text": "Farm tools are exposed to moisture, abrasive soil, acidic plant saps, and corrosive animal dung. Scheduled maintenance preserves asset value:\n\n1. **Cleaning**: Removing dirt, mud, sap, and moisture immediately after every work session.\n2. **Sharpening**: Restoring sharp cutting bevels on jembes, pangas, and secateurs.\n3. **Lubrication**: Applying grease or machine oil to moving joints to eliminate friction and block oxygen.\n4. **Repairing & Tightening**: Tightening loose bolts, driving hardwood wedges into loose handles.\n5. **Proper Storage**: Hanging clean tools vertically in a dry, locked store."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cleaning and Chemical Rust Removal",
                        "content": {
                            "title": "Restoring Bright Metal Surfaces",
                            "text": "1. **Scrape Soil**: Use a wooden scraper or wire brush to remove heavy caked soil.\n2. **Wash with Water**: Rinse away abrasive sand and plant sap.\n3. **Wipe 100% Dry**: Never store a damp tool! Water + oxygen rapidly forms iron oxide ($2\\text{Fe}_2\\text{O}_3 \\cdot 3\\text{H}_2\\text{O}$, rust).\n4. **Rust Scouring**: Dip steel wool or a wire brush in **kerosene / diesel** to scrub away oxidized rust scale until bright steel is exposed, then apply a thin oil film."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sharpening Mechanics: Flat File vs. Oil Whetstone",
                        "content": {
                            "title": "Restoring the Cutting Bevel",
                            "text": "- **Flat Steel File (For Jembes, Pangas, Spades)**: Clamp the tool securely in a bench vise. Push the file across the cutting bevel in a **single forward direction at a $30^\\circ$ angle**, lifting the file on the backward return stroke. (Never saw back and forth, which ruins file teeth!).\n- **Oil Whetstone (For Knives, Secateurs, Scalpels)**: Apply 2–3 drops of light mineral oil. Sweep the blade in a circular figure-8 motion, maintaining the exact factory bevel, then strop on leather to remove fine burrs."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "5 Core Pillars of Agricultural Tool Maintenance",
                        "content": {
                            "title": "5 Core Pillars of Agricultural Tool Maintenance",
                            "caption": "Maintenance cycle: 1 Scrape & Clean -> 2 Precision Sharpen (30° File / Whetstone) -> 3 Lubricate & Grease -> 4 Tighten Fasteners & Handles -> 5 Secure Vertical Storage."
                        }
                    }
                ],
                [
                    {
                        "type": "suggested_video",
                        "title": "Mastering the Art of Tool Sharpening: Files and Whetstones",
                        "content": {
                            "title": "Mastering the Art of Tool Sharpening: Files and Whetstones",
                            "description": "Agronomic workshop video demonstrating clamping jembes, single forward-stroke flat filing at 30 degrees, and whetstone circular stropping.",
                            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Sharpening Tools Comparison Matrix",
                        "content": {
                            "title": "Sharpening Equipment Comparison Matrix",
                            "headers": ["Sharpening Tool", "Abrasive Material", "Motion Protocol", "Matched Farm Implements", "Critical Technique Rule"],
                            "rows": [
                                ["Single-Cut Flat File", "Hardened carbon steel teeth", "Single forward push (Lift on return)", "Jembe, Panga, Spade, Axe", "Maintain 30° bevel; never saw back-and-forth!"],
                                ["Oil Whetstone (Fine)", "Silicon carbide / Novaculite", "Circular / Figure-8 stropping", "Secateurs, Grafting knives, Scalpels", "Lubricate with oil to float away metal filings"],
                                ["Bench Grinder", "High-speed abrasive wheel", "Light, brief touching strokes", "Dressing badly chipped axe/panga blades", "Dip blade in water frequently to prevent detempering"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Workshop Practical: Panga Rust Removal and Flat Filing Lab",
                        "content": {
                            "title": "Rust Removal and Sharpening Practicum",
                            "task": "1. Take a rusty, blunt panga.\n2. Scrub blade with steel wool dipped in kerosene until rust scale clears.\n3. Clamp panga firmly in a bench vise.\n4. Push a flat file across the cutting edge at a 30° bevel in smooth forward strokes until a sharp wire edge forms.",
                            "materials": ["Blunt Panga", "Flat Steel File", "Bench Vise", "Steel Wool", "Kerosene"],
                            "safety": "Wear leather gloves and eye protection; never touch sharp edges with bare fingers."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Cleaning & Sharpening",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Follow the 5 pillars: Clean, Sharpen, Lubricate, Repair, Store**.\n- **Wipe tools 100% dry** and scrub rust with kerosene and wire wool.\n- **Push flat files in a single forward stroke at 30°**; never saw backward.\n- **Use oil on whetstones** to float away microscopic metal shavings."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Single Forward Stroke Filing Rule",
                        "content": {
                            "question": "What is the correct physical technique for sharpening the cutting bevel of a digging jembe or panga with a flat steel file?",
                            "options": [
                                "Saw the file vigorously back and forth across the edge",
                                "Push the file in a single forward stroke across the bevel at a 30-degree angle, lifting the file completely off the metal on the backward return stroke",
                                "Soak the file in engine oil and hit the blade repeatedly",
                                "Rub the wooden handle of the file against the blade"
                            ],
                            "answer": "B",
                            "explanation": "Steel files are manufactured with directional teeth that cut only when pushed forward. Dragging the file backward against the metal bends and dulls the file's teeth and ruins the cutting bevel. Always push forward, lift, and reset."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 12: Maintenance Practices - Lubrication & Protection
        # =====================================================================
        {
            "unit_order": 12,
            "unit_name": "Maintenance Practices - Lubrication & Protection",
            "unit_description": "Lubrication chemistry reducing friction, heat, and rust; tightening loose fasteners and driving hardwood wedges into jembe handles; linseed oil on wood; anti-rust paint on metal.",
            "lesson_title": "Tool Maintenance II: Lubrication Chemistry, Handle Wedging, and Wood Preservation",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Applying Lubricating Grease to Farm Machinery Bearings",
                        "content": {
                            "title": "Applying Lubricating Grease to Farm Machinery Bearings",
                            "caption": "A farm mechanic using a grease gun to apply high-pressure lubricant to wheelbarrow axle bearings and moving tool pivot joints, eliminating friction and corrosion."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Lubrication & Protection",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain how **lubrication reduces friction, dissipates heat, and seals out moisture**.",
                                "Tighten loose fasteners and **secure loose jembe shafts using hardwood/metal wedges**.",
                                "Preserve wooden handles against rot and splinters using **boiled linseed oil**.",
                                "Apply **anti-rust paint** to non-working metal frames for seasonal storage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Chemistry and Physics of Lubrication",
                        "content": {
                            "title": "Eliminating Friction and Corrosion",
                            "text": "**Lubrication** is the application of a viscous fluid (motor oil, machine oil, or lithium grease) between moving mechanical metal surfaces:\n\n- **Friction & Wear Reduction**: Fills microscopic surface peaks and valleys (asperities), creating a hydrodynamic film that prevents direct metal-on-metal abrasion.\n- **Heat Dissipation**: Absorbs and carries away thermal energy generated by rubbing parts.\n- **Hydrophobic Seal**: Creates an airtight barrier that repels water and prevents atmospheric oxygen from reacting with iron to form rust!"
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Securing Loose Handles: The Hardwood Wedge Technique",
                        "content": {
                            "title": "Preventing Catastrophic Tool Separation",
                            "text": "A loose jembe or axe head is a deadly projectile that can fly off mid-swing and strike bystanders:\n- **The Wedging Protocol**: When a wooden handle shrinks and becomes loose inside the forged eyelet of a jembe or hammer, drive a **hardwood or tapered metal wedge** into the top center of the handle grain.\n- **Mechanical Expansion**: The wedge expands the wood fibers tightly against the inner walls of the steel eyelet, permanently locking the head in place."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Preserving Wood and Metal: Linseed Oil and Anti-Rust Paint",
                        "content": {
                            "title": "Sealing Against Environmental Decay",
                            "text": "1. **Wooden Handles**: Wood absorbs moisture and human sweat, causing swelling, rot, drying cracks, and splintering. Rub wooden shafts with **boiled linseed oil**. Linseed oil penetrates deep into wood pores, polymerizes into a tough protective seal, and keeps handles smooth and splinter-free.\n2. **Metal Components**: Paint wheelbarrow frames, mower decks, and tractor chassis with **oil-based anti-rust primer and enamel paint** to seal steel against air and acidic animal dung."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Preservative Coatings and Lubricants Comparison",
                        "content": {
                            "title": "Lubricant & Protective Coating Matrix",
                            "headers": ["Preservative / Lubricant", "Target Component", "Chemical / Physical Action", "Primary Farm Benefit"],
                            "rows": [
                                ["Heavy Lithium Grease", "Wheelbarrow axles, pivot joints, gears", "High-viscosity friction reduction film", "Waterproof lubrication; stops squeaking & wear"],
                                ["Light Machine Oil (3-in-1)", "Secateur pivots, shears, drenching triggers", "Low-viscosity penetrating lubricant", "Smooth spring action; dissolves light rust"],
                                ["Boiled Linseed Oil", "Wooden handles of jembes, spades, axes", "Deeply penetrating drying oil", "Prevents wood rot, cracking, and splinters"],
                                ["Anti-Rust Metal Paint", "Wheelbarrow bodies, tool racks, coop mesh", "Air-tight polymeric paint film barrier", "100% protection against atmospheric oxidation"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Workshop Practical: Driving Handle Wedges and Oiling Secateurs",
                        "content": {
                            "title": "Tool Rehabilitation Practicum",
                            "task": "1. Inspect a loose jembe handle; drive a hardwood wedge into the top grain until firmly locked.\n2. Apply 3 drops of machine oil to the pivot bolt of stiff secateurs.\n3. Wipe down a dry wooden spade handle with boiled linseed oil using a cloth.",
                            "materials": ["Loose Jembe", "Hardwood Wedges", "Machine Oil", "Linseed Oil", "Cloth"],
                            "safety": "Never leave oily rags piled in heaps (fire hazard; lay flat to dry)."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Lubrication & Protection",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Lubrication eliminates metal friction and blocks rust**.\n- **Drive hardwood wedges into handle grains** to lock loose tool heads.\n- **Treat wooden handles with boiled linseed oil** to stop splinters and rot.\n- **Paint metal frames** to seal against environmental corrosion."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Function of Boiled Linseed Oil on Handles",
                        "content": {
                            "question": "Why is it standard agricultural workshop practice to periodically rub boiled linseed oil into the wooden handles of spades, jembes, and rakes?",
                            "options": [
                                "To make the wooden handles turn into steel",
                                "Linseed oil penetrates the wood pores and dries into a tough, flexible moisture-proof seal, preventing the wood from absorbing water, rotting, splitting, and producing painful splinters",
                                "To make the handles taste bitter so termites don't eat them",
                                "To increase the weight of the handle by 50%"
                            ],
                            "answer": "B",
                            "explanation": "Boiled linseed oil is a natural drying oil that penetrates deep into wooden cell structures, polymerizing into a durable, water-resistant barrier. This keeps the wood supple, prevents drying cracks and rot, and maintains a smooth, splinter-free surface."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 13: Care, Storage, and Workspace Organization
        # =====================================================================
        {
            "unit_order": 13,
            "unit_name": "Care, Storage, and Workspace Organization",
            "unit_description": "Indoor storage economics; vertical wall racks (hanging tools head-down); Shadow Board visual inventory; locked farm store security.",
            "lesson_title": "Store Architecture: Tool Racks, Shadow Board Systems, and Farm Security",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Organized Workshop Tool Shed with Wall-Mounted Tool Racks",
                        "content": {
                            "title": "Organized Workshop Tool Shed with Wall-Mounted Tool Racks",
                            "caption": "A professionally organized farm tool store featuring wall-mounted vertical racks, labeled shelves, and clear walkways, illustrating store management."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Storage & Workspace",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Analyze the **economic and safety penalties of improper outdoor tool abandonment**.",
                                "Construct a **vertical wall-mounted tool rack (hanging tools head-down)**.",
                                "Design and implement a **Shadow Board visual inventory system**.",
                                "Enforce **farm store physical security and check-out ledger protocols**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Economics of Proper Indoor Storage",
                        "content": {
                            "title": "Protecting Farm Capital Assets",
                            "text": "- **The Outdoor Abandonment Penalty**: Leaving jembes, pangas, and spades lying in wet pasture grass accelerates rust pitting, rots wooden handles within months, creates dangerous tripping hazards, and attracts theft.\n- **Indoor Storage Mandate**: All tools must be cleaned, dried, and returned to a secure, well-ventilated, dry farm store immediately at the end of each workday."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Vertical Wall Racks and the Head-Down Rule",
                        "content": {
                            "title": "Safe Physical Tool Storage",
                            "text": "- **Vertical Wall Racks**: Mount heavy timber or steel brackets on store walls to hang long-handled tools (jembes, spades, shovels, rakes) vertically.\n- **THE HEAD-DOWN RULE**: Always hang long tools with their **heavy working heads pointing downward**!\n  - *Safety*: Prevents heavy sharp steel blades from falling onto workers' heads.\n  - *Walkways*: Keeps floor walkways 100% clear of tripping and puncture hazards."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Shadow Board Visual Inventory System",
                        "content": {
                            "title": "Instant 5-Second Inventory Verification",
                            "text": "A **Shadow Board** is a wall-mounted wooden board on which the exact silhouette outlines (shadows) of each tool are painted in contrasting bright paint:\n- **Instant Audit**: When a tool is in use, its painted shadow is visible. At 5:00 PM lockup, the farm manager can audit 50 tools in **5 seconds**—any empty shadow immediately signals a missing tool!\n- **Accountability**: Paired with a daily **Tool Check-Out Ledger** requiring student signatures."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Farm Workshop Shadow Board Layout & Vertical Tool Rack",
                        "content": {
                            "title": "Farm Workshop Shadow Board Layout & Vertical Tool Rack",
                            "caption": "Store layout blueprint: Left: Shadow Board Wall (Painted tool silhouettes for instant inventory) | Right: Vertical Wall Rack (Spades, Jembes & Rakes hung head-down for safety)."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Proper Indoor Storage vs Neglectful Outdoor Storage",
                        "content": {
                            "title": "Tool Storage Conditions Impact Matrix",
                            "headers": ["Storage Parameter", "Proper Indoor Shadow Board Storage", "Improper Field / Wet Grass Storage", "Agronomic & Economic Result"],
                            "rows": [
                                ["Moisture Exposure", "Zero (Dry, ventilated room)", "High (Rain, dew, damp soil)", "Rapid rust pitting & rotting handles"],
                                ["Safety Hazard", "Zero (Halt tripping hazards; blades hung down)", "Severe (Sharp blades hidden in grass)", "Puncture wounds, broken bones, tripping"],
                                ["Inventory Control", "Instant 5-second shadow check", "Zero control (Tools scattered in fields)", "Lost tools, delayed farm operations, theft"],
                                ["Asset Lifespan", "10 – 15 Years of active service", "1 – 2 Years before complete breakdown", "10x higher capital replacement cost"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Classroom Practical: Designing and Painting a Workshop Shadow Board",
                        "content": {
                            "title": "Shadow Board Construction Practicum",
                            "task": "1. Lay a plywood sheet on a workbench.\n2. Arrange 5 tools (claw hammer, spanners, secateurs, hand saw, trowel) on the board.\n3. Trace their exact outlines with a pencil.\n4. Paint inside the outlines with bright red/black enamel paint.\n5. Install brass L-hooks to mount tools precisely over their painted shadows.",
                            "materials": ["Plywood Board", "Tools", "Paint & Brush", "L-Hooks", "Screwdriver"],
                            "safety": "Wear aprons and work in a well-ventilated area when painting."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Storage & Workspace",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Store cleaned tools indoors** immediately after use.\n- **Hang long tools vertically with heads pointing down**.\n- **Shadow Boards provide instant 5-second inventory audits**.\n- **Maintain a locked store and check-out ledger** to prevent theft."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Rationale for Hanging Tools Head-Down",
                        "content": {
                            "question": "Why is it an essential workshop safety standard to hang long-handled digging tools (jembes, spades, shovels) on vertical wall racks with their heavy working heads pointing downward rather than upward?",
                            "options": [
                                "It makes the tools look like decorative art",
                                "Positioning heavy sharp heads downward prevents top-heavy instability, keeps sharp cutting blades safely below head level, and ensures that if a tool slips off its hook, it does not strike a worker's head or face",
                                "It allows moisture to run into the handle grain",
                                "It makes the tools lighter to carry"
                            ],
                            "answer": "B",
                            "explanation": "Hanging heavy tools with heads upward creates top-heavy instability where slight bumps can dislodge the tool. Heavy, sharp metal heads falling from high heights cause catastrophic head and facial lacerations. Hanging them head-down keeps the center of gravity low and safe."
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 14: Accident Prevention, First Aid, and Review
        # =====================================================================
        {
            "unit_order": 14,
            "unit_name": "Accident Prevention, First Aid, and Review",
            "unit_description": "Agricultural PPE (gumboots, leather gloves, goggles, dust masks); First Aid emergency protocols (minor cuts/tetanus, 15-20 min chemical eye wash, cold compress); Tool Rehabilitation consulting case study; 8 Summative Topic Assessment MCQs.",
            "lesson_title": "Safety Engineering: Agricultural PPE, First Aid Protocols, and Summative Assessment",
            "pages": [
                [
                    {
                        "type": "suggested_image",
                        "title": "Fully Stocked Agricultural Workshop First Aid Kit",
                        "content": {
                            "title": "Fully Stocked Agricultural Workshop First Aid Kit",
                            "caption": "A wall-mounted emergency first aid box containing sterile bandages, antiseptic lotions, eye wash solutions, burn dressings, and trauma scissors."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Safety & Summative Review",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Synthesize the **complete Tools, Equipment, and Machinery framework**.",
                                "Select specialized **Personal Protective Equipment (PPE)** for specific farm hazards.",
                                "Execute **emergency First Aid protocols (cuts, chemical eye splashes, trauma)**.",
                                "Complete the comprehensive **Summative Topic Assessment** covering all 14 lessons of Topic 13."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Agricultural Personal Protective Equipment (PPE)",
                        "content": {
                            "title": "The First Line of Human Defense",
                            "text": "Every farm worker must be equipped with matched PPE:\n1. **Steel-Toed Gumboots**: Heavy rubber protects against mud, standing water, snakebites, and dropped steel tools.\n2. **Heavy Leather Gloves**: Protects hands from sharp wire ends, wood splinters, thorns, and chemical blisters.\n3. **Polycarbonate Safety Goggles**: Protects eyes from flying wood chips while sawing, metal filings while grinding, and chemical spray mists.\n4. **Particulate Dust Mask / Respirator**: Filters agricultural dusts, fungal spores from deep litter, and chemical pesticide mists."
                        }
                    }
                ],
                [
                    {
                        "type": "concept_explanation",
                        "title": "Emergency First Aid Protocols on the Farm",
                        "content": {
                            "title": "Immediate Response to Workshop Injuries",
                            "text": "1. **Minor Cuts & Lacerations**: Wash immediately under clean running water and mild antiseptic soap. Apply an antiseptic cream and cover with a sterile bandage. (Always verify **Tetanus toxoid vaccination** status to prevent deadly *Clostridium tetani* soil infections!).\n2. **Chemical Eye / Skin Splashes**: Immediately flush eyes/skin with **huge volumes of clean running water for at least 15 to 20 continuous minutes**, holding eyelids open, then seek immediate medical care.\n3. **Blunt Trauma / Fractures**: Immobilize the limb, apply a cold ice compress wrapped in cloth to reduce swelling, and transport to a clinic."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Master Agricultural Tools, Equipment & Safety Lifecycle Matrix",
                        "content": {
                            "title": "Master Agricultural Tools, Equipment & Safety Lifecycle Matrix",
                            "caption": "Master agricultural mechanics lifecycle: 1 Classification & Power -> 2 Task-Tool Matching -> 3 Crop & Livestock Implements -> 4 Assembly & Fabrication -> 5 5-Pillar Maintenance -> 6 Safe Storage, PPE & First Aid."
                        }
                    }
                ],
                [
                    {
                        "type": "comparison_table",
                        "title": "Farm Emergency First Aid Response Guide",
                        "content": {
                            "title": "Farm Emergency Action Matrix",
                            "headers": ["Accident / Injury", "Immediate First Aid Action", "Critical Hazard to Avoid", "Medical Follow-up"],
                            "rows": [
                                ["Laceration from rusty panga / jembe", "Wash with soap & water; apply antiseptic & bandage", "Do not apply cow dung or unsterile soil!", "Administer Tetanus toxoid booster within 24h"],
                                ["Herbicide / Pesticide eye splash", "Flush continuously with clean water for 15–20 min", "Do not rub eyes; do not use chemical neutralizers", "Immediate emergency hospital transport"],
                                ["Blunt crush injury / heavy dropped tool", "Apply cold compress; elevate bruised limb", "Do not apply direct heat or massage fracture", "X-ray imaging if fracture is suspected"],
                                ["Heat exhaustion during land preparation", "Move to cool shade; give cool electrolyte water", "Do not administer icy cold drinks rapidly", "Monitor vital signs; rest until recovery"]
                            ]
                        }
                    }
                ],
                [
                    {
                        "type": "mini_activity",
                        "title": "Performance Task: The 'Kisumu Tool Rehabilitation' Consulting Audit",
                        "content": {
                            "title": "Tool Rehabilitation Consulting Case",
                            "task": "A school farm store contains:\n- 3 rusty, blunt jembes with loose wooden handles\n- A pair of secateurs stuck shut with dried plant sap\n- A wheelbarrow with a squeaking, dry wheel axle\n- A hand saw with a resin-caked blade\n\n**Your Deliverable**: Write a Step-by-Step Tool Rehabilitation Protocol:\n1. Specify exact tools, solvents (kerosene/oil), and sharpening equipment needed for each item.\n2. Detail the hardwood wedging procedure for the loose jembes.\n3. Outline a 5-pillar maintenance schedule and shadow board design.",
                            "materials": ["Case Handout", "Response Template", "Pen"],
                            "safety": "Ensure rigorous, evidence-based recommendations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Core Summary: Safety & First Aid",
                        "content": {
                            "title": "Key Takeaways",
                            "text": "- **Always wear task-matched PPE (gumboots, gloves, goggles, masks)**.\n- **Flush chemical eye splashes for 15–20 minutes with clean water**.\n- **Treat all soil-contaminated cuts for tetanus risk**.\n- **Routine maintenance is human life safety engineering**."
                        }
                    }
                ],
                # Pages 5 to 8: 8 Summative Assessment MCQs
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 1: Distinguishing Spade from Shovel",
                        "content": {
                            "question": "What is the primary anatomical and functional difference between an agricultural spade and a shovel?",
                            "options": [
                                "A spade has a motorized engine, whereas a shovel is driven by draft oxen",
                                "A spade has a flat, rectangular cutting blade with a straight edge for slicing soil edges and trenches, whereas a shovel has a broad concave scoop for lifting and transferring loose bulk materials",
                                "A spade is only used for cutting tree timber",
                                "A shovel is designed exclusively for catching fish"
                            ],
                            "answer": "B",
                            "explanation": "A spade is a cutting implement with a flat blade and straight edge designed for slicing turf and digging vertical trenches. A shovel has a concave, curved bowl profile designed for scooping, lifting, and loading loose granular materials (manure, sand, compost)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 2: Biological Mechanism of Bloodless Burdizzo Castration",
                        "content": {
                            "question": "How does a Burdizzo castrator achieve castration in male livestock without creating an open surgical wound?",
                            "options": [
                                "It injects a chemical hormone that dissolves the testicles",
                                "It uses compound leverage to crush the spermatic cords and blood vessels through the intact scrotal skin, cutting off blood supply so the testicles atrophy without open bleeding or fly-strike risk",
                                "It freezes the testicles using compressed gas",
                                "It removes the scrotum completely with razor blades"
                            ],
                            "answer": "B",
                            "explanation": "The Burdizzo is a bloodless castrator. When clamped, its heavy jaws crush the spermatic cords and testicular artery through the unbroken scrotal skin. Deprived of blood flow, the testicular tissue atrophies, eliminating external hemorrhaging and open wound infections."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 3: Oral Drenching Head Angle and Aspiration Pneumonia",
                        "content": {
                            "question": "Why is it mandatory to keep a sheep or goat's head level and horizontal when administering liquid anthelmintics with an oral drenching gun?",
                            "options": [
                                "If the head is pulled vertically, the liquid flows into the ears",
                                "A vertical head position prevents the epiglottis reflex from closing over the larynx, allowing liquid medicine to pour into the trachea and lungs, causing fatal aspiration pneumonia",
                                "The sheep cannot see the drenching gun nozzle",
                                "The medicine turns into solid powder if the head is lifted"
                            ],
                            "answer": "B",
                            "explanation": "Holding the muzzle level ensures the animal can swallow naturally. Pulling the head vertically impairs the epiglottis, directing the fluid bolus down the trachea into lung alveoli, causing acute chemical drowning or fatal aspiration pneumonia."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 4: Torque Mechanics in Ring vs Open Spanners",
                        "content": {
                            "question": "Why is a ring spanner vastly superior to an open-ended spanner when applying high torque to loosen a tight machine bolt?",
                            "options": [
                                "Ring spanners are powered by batteries",
                                "The ring spanner completely encloses the hexagonal bolt head, contacting all 6 corners simultaneously and distributing torque evenly, preventing jaw spreading and corner stripping",
                                "Open-ended spanners only work on wooden bolts",
                                "Ring spanners cut the bolt in half"
                            ],
                            "answer": "B",
                            "explanation": "Open-ended spanners grip only 2 flat sides and can flex open under high torque, rounding off the hex bolt corners. A ring spanner encircles all corners with 6 or 12 broached teeth, distributing rotational force uniformly with zero slip."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 5: Chemical Eye Splash Emergency First Aid",
                        "content": {
                            "question": "What is the immediate, non-negotiable First Aid response if a concentrated chemical pesticide splashes into an operator's eyes during sprayer cleaning?",
                            "options": [
                                "Rub the eyes vigorously with a leather work glove",
                                "Flush the open eyes immediately with huge volumes of clean running water for at least 15 to 20 continuous minutes, then seek emergency medical care",
                                "Apply warm vegetable cooking oil to the eyes",
                                "Close both eyes tightly and wait for the stinging to pass"
                            ],
                            "answer": "B",
                            "explanation": "Continuous irrigation with clean running water for 15–20 minutes is the global emergency standard for ocular chemical burns. It dilutes and mechanically flushes out caustic chemicals, minimizing permanent corneal damage before hospital treatment."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 6: Function of Boiled Linseed Oil on Wooden Shafts",
                        "content": {
                            "question": "How does applying boiled linseed oil to the wooden handles of spades and jembes preserve them against physical decay?",
                            "options": [
                                "It makes the wooden handle flexible like rubber",
                                "It penetrates deep into wood pores and polymerizes into a water-resistant seal that stops moisture absorption, rot, drying splits, and painful splinters",
                                "It attracts beneficial earthworms to the handle",
                                "It turns the wood into steel"
                            ],
                            "answer": "B",
                            "explanation": "Boiled linseed oil is a drying oil that soaks into the wood cellular structure and cures into a water-repellent polymeric barrier. This prevents moisture-induced rotting, warping, and grain splitting, keeping tool shafts smooth and splinter-free."
                        }
                    }
                ],
                [
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 7: Single Forward Filing Technique",
                        "content": {
                            "question": "Why must a flat steel file be pushed in a single forward direction across a jembe cutting bevel, rather than scrubbed back and forth like a saw?",
                            "options": [
                                "The jembe blade will break in half if filed backward",
                                "Steel files have directional teeth designed to cut only on the forward push stroke; dragging the file backward bends and destroys the file teeth and creates a jagged, uneven tool edge",
                                "Filing backward creates electrical sparks that ignite the grass",
                                "The file only works when wet"
                            ],
                            "answer": "B",
                            "explanation": "File teeth are cut with a forward rake angle. Pushing forward shears metal cleanly. Dragging the file backward under pressure bends and fractures the hardened file teeth and tears the tool's cutting edge. Always push forward, lift, and reset."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Summative MCQ 8: Agricultural Class 2 Lever Mechanics",
                        "content": {
                            "question": "How does a standard wheelbarrow utilize Class 2 lever physics to allow a single farmer to move heavy loads of farm manure easily?",
                            "options": [
                                "The operator acts as the fulcrum in the middle",
                                "The front wheel axle acts as the fulcrum at one end, the heavy load is positioned in the middle hopper, and effort is applied at the long handles at the far end, maximizing mechanical advantage",
                                "The wheelbarrow eliminates gravity completely",
                                "The two rear legs pull the load forward automatically"
                            ],
                            "answer": "B",
                            "explanation": "A wheelbarrow is a classic Class 2 lever where the Load (manure hopper) is positioned between the Fulcrum (front wheel axle) and the Effort (handle grips). Positioning the load near the front wheel ensures the wheel bears most of the weight."
                        }
                    }
                ],
                # Page 8: Capstone Summary
                [
                    {
                        "type": "summary",
                        "title": "Topic 13 Capstone Summary: Tools and Equipment Mastery",
                        "content": {
                            "title": "Mastery Overview: Grade 10 Agricultural Mechanics & Safety",
                            "text": "Congratulations on mastering **Topic 13: Tools and Equipment**!\n\nYou have mastered:\n- **Classification & Power Sources**: Tools vs Equipment vs Machines; Manual vs Animal-Drawn vs Motorized power pathways.\n- **Task-Tool Matching**: Ergonomics, soil texture matching, preventing crop vascular damage, and avoiding operator injuries.\n- **Gardening Implements**: Jembe & fork jembe; spade (cutting) vs shovel (scooping); rakes; precision secateurs vs panga; hand trowels & rose watering cans.\n- **Livestock Implements**: Burdizzo bloodless castration, elastrators, ear notchers & tattooing, oral drenching guns (horizontal head rule), syringes (IM vs Sub-Q), hoof cutters, and dark strip cups for mastitis.\n- **Mechanical Assembly & Fabrication**: Open-ended vs ring spanners (multi-point torque), screwdrivers, washers, hand saws (45° angle, starter kerf), and Class 1 crowbars.\n- **5-Pillar Tool Maintenance**: Clean, Sharpen (single forward-stroke flat filing at 30°), Lubricate (lithium grease/oil), Repair/Wedge handles, and Boiled linseed oil wood preservation.\n- **Storage & Safety**: Vertical wall racks (head-down rule), Shadow Board visual inventory, locked store access, agricultural PPE, and First Aid emergency protocols (15-20 min eye wash, tetanus wound care)."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 13 Final Takeaway",
                        "content": {
                            "title": "The Agricultural Mechanics Maxim",
                            "text": "Match the right tool to the task, maintain razor-sharp bevels, protect moving joints with lubrication, store implements securely on shadow boards, and wear matched PPE. Meticulous tool care protects farm capital, accelerates productivity, and safeguards human life."
                        }
                    }
                ]
            ]
        }
    ]

@transaction.atomic
def ingest_grade10_topic13(replace=False):
    """Executes the complete production ingestion of Grade 10 Agriculture Topic 13: Tools and Equipment."""
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Agriculture — Topic 13: Tools and Equipment")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name__iexact="Agriculture").first()

    assert curriculum and grade and subject, "Curriculum/Grade/Subject not found!"

    topic_name = "Tools and Equipment"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()
    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            description="Comprehensive theoretical and practical training in agricultural mechanics: task-tool matching, garden tillage implements, livestock husbandry tools, mechanical fastening and fabrication, 5-pillar maintenance, shadow board storage, PPE, and workshop first aid.",
            order=13
        )
        print(f"Created Topic 13: {topic.name} (ID: {topic.id})")
    else:
        topic.order = 13
        topic.description = "Comprehensive theoretical and practical training in agricultural mechanics: task-tool matching, garden tillage implements, livestock husbandry tools, mechanical fastening and fabrication, 5-pillar maintenance, shadow board storage, PPE, and workshop first aid."
        topic.save()
        print(f"Resolved Topic 13: {topic.name} (ID: {topic.id})")

    if replace:
        print("Flag --replace active: Clearing existing LearningUnits and Lessons for Topic 13...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    curriculum_data = build_topic13_curriculum()
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
                    "topic_order": 13,
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
                    block_id=f"g10_agri_t13_u{u_order}_p{page_idx}_b{comp_idx}",
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    order=block_order_counter,
                    page_number=page_idx,
                    component_order=comp_idx,
                    page_title=b_title if comp_idx == 1 else None,
                    metadata={"topic_order": 13, "unit_order": u_order, "page": page_idx}
                )
                block_order_counter += 1
                total_blocks += 1

        print(f"  Ingested Unit {u_order}: {u_name} -> Lesson '{l_title}' ({len(pages)} Pages, {block_order_counter - 1} Blocks)")

    print("=" * 80)
    print(f"INGESTION COMPLETE: Topic 13 '{topic.name}'")
    print(f"  Total Units:   {total_units}")
    print(f"  Total Lessons: {total_lessons}")
    print(f"  Total Pages:   {total_pages}")
    print(f"  Total Blocks:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_topic13(replace=replace_flag)
