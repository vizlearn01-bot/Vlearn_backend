"""
VLearn CBC Grade 8 Agriculture — Topic 1: Soil Conservation Measures
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Soil Conservation Measures (Topic Order: 1)

Decomposed into 8 Learning Units & 8 Published Lessons:
  1. Introduction to Soil Conservation and Strip Cropping (7 Pages, 13 Blocks)
  2. Practical: Carrying out Strip Cropping in the School Farm (7 Pages, 13 Blocks)
  3. Grassed Waterways (7 Pages, 13 Blocks)
  4. Stone Lines and Trash Lines (7 Pages, 13 Blocks)
  5. Practical: Preparing Stone Lines and Trash Lines (7 Pages, 13 Blocks)
  6. Soil Bunds: Meaning and Practical Preparation (7 Pages, 14 Blocks)
  7. Project Part 1: Model Planning and Design (7 Pages, 13 Blocks)
  8. Project Part 2: Model Construction and Presentation & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Deep scientific mechanisms of soil physics, raindrop impact kinetic energy, soil aggregate stability.
  - Worked agronomic engineering calculations (slope %, runoff velocity reduction, water storage capacity).
  - Authentic Kenyan regional case studies (Machakos terracing revolution, Baringo rangeland bunds, Murang'a waterways).
  - Multiple curated video blocks embedded across key practical lessons.
  - Formative scenario MCQs and Topic Summative MCQs with comprehensive educational explanations.
  - Zero citation bracket leaks, zero meta-tag leaks, and zero raw unrendered LaTeX.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic1.py [--replace]
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

def build_topic1_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 1: Soil Conservation Measures."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Soil Conservation and Strip Cropping
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Soil Conservation and Strip Cropping",
            "unit_description": "Soil conservation definitions, environmental importance, soil physics, threats (slash & burn, agrochemicals, overgrazing), strip cropping mechanics, and introductory instructional video.",
            "lesson_title": "Introduction to Soil Conservation and Strip Cropping",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Living Contours: The Power of Strip Cropping",
                        "content": {
                            "title": "Living Contours: The Power of Strip Cropping",
                            "caption": "A sloping agricultural hillside arranged in alternating, colorful crop strips following natural contour lines to prevent soil erosion."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Soil Protection Principles",
                        "content": {
                            "title": "What We Will Learn Today",
                            "goals": [
                                "Define **soil conservation** and explain why protecting fertile topsoil sustains national food security.",
                                "Analyze the 3 major destructive human threats to soil: **slash-and-burn clearing, excessive chemical contamination, and overgrazing**.",
                                "Explain how **strip cropping** alternates open row crops with dense ground cover to decelerate runoff velocity by up to 75%.",
                                "Watch and reflect on an authentic field video lesson on soil conservation measures in Kenya."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Living Skin of the Earth",
                        "content": {
                            "title": "Why Soil is Our Most Precious Asset",
                            "text": "Topsoil is the thin, fertile upper layer of the Earth (averaging only 15 to 20 cm) that contains organic humus, beneficial microbes, and plant nutrients. It takes over **500 years for nature to form just 2.5 cm of fertile topsoil**, yet a single violent rainstorm can wash it away in minutes if land is left bare.\n\n- **Soil Conservation** is the scientific practice of protecting soil from physical loss by water and wind erosion, preserving its fertility and biological structure for future generations."
                        }
                    }
                ],
                # Page 2: Destructive Threats & Soil Degradation Physics
                [
                    {
                        "type": "concept_explanation",
                        "title": "The 3 Major Human Threats to Soil",
                        "content": {
                            "title": "How Human Activities Destroy Soil Structure",
                            "text": "- **1. Slash-and-Burn Clearing**: Burning vegetation destroys protective organic litter, incinerates beneficial soil microorganisms, and leaves bare ground vulnerable to raindrop impact.\n- **2. Agrochemical Overuse**: Excessive application of synthetic fertilizers and pesticides acidifies soil, kills earthworms, and breaks down natural crumb aggregates into fine, easily erodible dust.\n- **3. Overgrazing & Livestock Trampling**: Too many livestock strip grass cover bare, while heavy hooves compact the subsoil, creating an impermeable crust where rainwater cannot infiltrate and rushes away as destructive surface runoff."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Human Practices vs Soil Ecological Impact",
                        "content": {
                            "title": "Threats and Soil Health Matrix",
                            "headers": ["Destructive Practice", "Soil Physics Mechanism", "Long-Term Damage", "Sustainable Remedy"],
                            "rows": [
                                ["Slash & Burn", "Destroys organic canopy and scorches microbial life", "Massive splash erosion and humus loss", "Mulching, agroforestry, minimum tillage"],
                                ["Over-fertilization", "Alters soil pH and destroys earthworm populations", "Soil crusting, nutrient runoff into rivers", "Compost manure, bio-fertilizers, crop rotation"],
                                ["Overgrazing", "Removes root network; hoof pressure seals soil pores", "Severe sheet wash and gully formation", "Rotational grazing, paddocking, zero-grazing"]
                            ]
                        }
                    }
                ],
                # Page 3: Strip Cropping Mechanics & Physics
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Strip Cropping Slope Flow & Runoff Deceleration Architecture",
                        "content": {
                            "title": "Strip Cropping Slope Flow & Runoff Deceleration Architecture",
                            "caption": "Engineering diagram showing alternating bands of tall row crops (maize) and dense cover crops (beans/grass) slowing runoff velocity across natural contours."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Strip Cropping Stops Erosion",
                        "content": {
                            "title": "The Alternating Band Principle",
                            "text": "**Strip cropping** divides a sloping farm into alternating horizontal bands planted across the contour lines:\n\n- **Erosion-Permitting Strips**: Wide-spaced row crops like maize, sorghum, or cassava where soil is partially exposed.\n- **Erosion-Resisting Strips**: Dense close-growing cover crops like beans, cowpeas, sweet potatoes, or Napier grass.\n\n**The Hydrodynamic Barrier**: As rainwater rushes down through the maize strip, it hits the dense cover crop strip, which acts as a living sieve. Water velocity drops from 2.0 m/s to 0.4 m/s, dropping its sediment load and soaking deep into the subsoil!"
                        }
                    }
                ],
                # Page 4: Video Resource — Soil Conservation in Kenya
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Lesson: Soil Conservation Measures for Grade 8 CBC",
                        "content": {
                            "title": "Video Lesson: Soil Conservation Measures for Grade 8 CBC",
                            "url": "https://www.youtube.com/watch?v=UhCX8MM6qjk",
                            "resolved_video_id": "UhCX8MM6qjk",
                            "caption": "Watch Ask Mwalimu Steve CBC Kenya demonstrate soil conservation measures, the importance of vegetation cover, and strip cropping on sloping land."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Observations from the Field Video",
                        "content": {
                            "title": "Video Reflection Points",
                            "text": "- **1. Topsoil Loss**: Notice how bare slopes shed muddy brown water while grass-covered slopes discharge crystal clear runoff.\n- **2. Contour Alignment**: Observe how conservation barriers MUST run perpendicular to slope flow, never downhill!\n- **3. Crop Synergy**: See how combining cereals with nitrogen-fixing legumes preserves soil fertility naturally."
                        }
                    }
                ],
                # Page 5: Interactive Classification Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Agricultural Practice Classification Challenge",
                        "content": {
                            "title": "Distinguishing Destructive vs Conserving Farming",
                            "instructions": "Evaluate the farm practice and classify its impact on soil stability:",
                            "scenario": "Farmer Kiprono plows straight down a 12% hillside slope and burns all crop stalks after harvesting his maize.",
                            "question": "How should this farming practice be classified?",
                            "options": [
                                "Highly Destructive Practice (Accelerates Severe Gully Erosion)",
                                "Sustainable Soil Conservation Practice"
                            ],
                            "correct_feedback": "Correct! Plowing down slopes creates artificial drainage channels for runoff, and burning crop residue leaves topsoil unprotected from heavy raindrops.",
                            "incorrect_feedback": "Incorrect. Plowing downhill and burning crop residues are classic triggers of severe soil erosion and nutrient depletion."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Strip Cropping Mechanics",
                        "content": {
                            "question": "How does alternating row crops with dense cover crops across the contour prevent hillside soil erosion?",
                            "options": [
                                "Dense cover strips act as living barriers that slow runoff velocity, trap eroded soil particles, and promote water infiltration.",
                                "Cover crops absorb all solar heat so that soil stays permanently dry.",
                                "Row crops reflect heavy raindrops back into the clouds.",
                                "The alternating colors confuse insect pests and make them fly away."
                            ],
                            "answer": "A",
                            "explanation": "Dense cover crop strips act as living physical filters across the slope. They decelerate the speed of flowing water, allow suspended soil particles to settle, and give moisture time to infiltrate the ground."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Soil conservation** protects vital topsoil from water and wind degradation.\n- **Slash-and-burn, chemical overuse, and overgrazing** rapidly destroy soil aggregates and humus.\n- **Strip cropping** alternates row crops with dense cover crops across contour lines.\n- It **reduces runoff velocity, traps silt, and increases soil moisture infiltration**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we layout and establish strip cropping on our actual school farm? In Lesson 2, we grab our tools and master the A-frame contour surveying technique!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Practical: Carrying out Strip Cropping in the School Farm
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Practical: Carrying out Strip Cropping in the School Farm",
            "unit_description": "Practical field procedures: A-frame calibration, contour line pegging, strip width calculation based on slope percentage, seedbed preparation, and companion planting.",
            "lesson_title": "Practical: Carrying out Strip Cropping in the School Farm",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Precision Farming: Strip Cropping in the Field",
                        "content": {
                            "title": "Precision Farming: Strip Cropping in the Field",
                            "caption": "Agriculture students laying out contour pegs and planting alternating strips of maize and legumes on a school slope."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Field Implementation Skills",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Calibrate and operate an **A-frame tool** to mark exact horizontal contour lines.",
                                "Calculate appropriate **strip widths** based on field slope percentage (gentle vs steep).",
                                "Execute seedbed preparation and plant alternating cereal/legume strips.",
                                "Follow personal safety standards when using farm implements (hoes, pangas, measuring tapes)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Science of Contour Pegging",
                        "content": {
                            "title": "Finding True Horizontal Lines",
                            "text": "Water always flows perpendicular to contour lines (straight down the steepest path). By aligning our crop strips exactly along contour lines (lines connecting points of equal elevation), we ensure that running water is met by a level, uniform barrier that never allows water to concentrate into violent gullies."
                        }
                    }
                ],
                # Page 2: A-Frame Calibration & Slope Surveying Workflow
                [
                    {
                        "type": "suggested_diagram",
                        "title": "4-Step Practical Field Workflow for Strip Cropping",
                        "content": {
                            "title": "4-Step Practical Field Workflow for Strip Cropping",
                            "caption": "Step-by-step field methodology: 1. Survey & Peg Contours with A-frame • 2. Measure Strip Widths • 3. Prepare Seedbed • 4. Plant Alternating Strips."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Operating the A-Frame",
                        "content": {
                            "title": "A-Frame Calibration & Field Pegging Protocol",
                            "steps": [
                                "**1. Construct the Frame**: Lash three poles together into an 'A' shape. Hang a plumb-bob or stone from the apex.",
                                "**2. Calibrate Center Mark**: Place legs on level ground, mark where the string rests on the crossbar. Reverse legs 180 degrees. The exact midpoint between the two string marks is the level center line.",
                                "**3. Walk the Contour**: Place Leg A on the slope, pivot Leg B until the plumb string aligns with the center mark. Drive a wooden peg at both legs.",
                                "**4. Pivot Forward**: Keep Leg B fixed, swing Leg A forward across the hill until the plumb string hits center again. Drive the next peg. Repeat across the field!"
                            ]
                        }
                    }
                ],
                # Page 3: Strip Width Engineering Formulas
                [
                    {
                        "type": "concept_explanation",
                        "title": "Calculating Strip Widths by Slope Gradient",
                        "content": {
                            "title": "Why Slope Governs Strip Spacing",
                            "text": "The steeper the hill slope, the faster runoff accelerates due to gravity, and the narrower each crop strip must be to stop water from building destructive momentum."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Slope Gradient vs Strip Width Specification",
                        "content": {
                            "title": "Engineering Standards for Strip Widths",
                            "headers": ["Hillside Slope Gradient", "Slope Category", "Recommended Strip Width", "Crop Pairing Example"],
                            "rows": [
                                ["0% to 4%", "Gentle Slope", "20 to 30 meters wide", "Maize (Row) + Beans (Cover)"],
                                ["5% to 8%", "Moderate Slope", "15 to 20 meters wide", "Sorghum (Row) + Cowpeas (Cover)"],
                                ["9% to 15%", "Steep Slope", "10 to 15 meters wide", "Maize (Row) + Desmodium / Sweet Potatoes (Cover)"],
                                ["> 15%", "Very Steep Slope", "< 10 meters (requires Terracing)", "Perennial Napier grass + Agroforestry trees"]
                            ]
                        }
                    }
                ],
                # Page 4: Practical Planting Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Seedbed & Planting",
                        "content": {
                            "title": "Planting Alternating Strips",
                            "steps": [
                                "**Step 1: Land Tillage**: Till soil along the pegged contour lines. Never till up-and-down the slope.",
                                "**Step 2: Strip 1 (Row Crops)**: Plant maize at 75 cm x 25 cm spacing along the first 15m strip.",
                                "**Step 3: Strip 2 (Cover Crops)**: Plant beans or groundnuts at close 30 cm x 15 cm spacing along the next 15m strip.",
                                "**Step 4: Rotate Next Season**: Swap crop positions next season to break pest cycles and replenish nitrogen!"
                            ]
                        }
                    }
                ],
                # Page 5: Interactive Strip Width Calculation Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Engineering Decision: Setting Strip Widths",
                        "content": {
                            "title": "Slope-Based Width Planning",
                            "instructions": "Calculate the correct strip width for the school's steep hillside:",
                            "scenario": "The school farm committee measures a slope gradient of 12% on the eastern field block.",
                            "question": "What is the recommended strip width for this 12% steep slope?",
                            "options": [
                                "10 to 15 meters wide",
                                "50 to 60 meters wide",
                                "100 meters wide",
                                "2 meters wide"
                            ],
                            "correct_feedback": "Correct! On a steep 12% slope, strips must be narrowed to 10–15 meters to prevent water from building destructive velocity.",
                            "incorrect_feedback": "Incorrect. On steep slopes (9–15%), wide strips (50m+) allow runoff to gain high velocity. 10–15m is the agronomically recommended standard."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: A-Frame Center Mark Function",
                        "content": {
                            "question": "When walking across a hillside with an A-frame, what does it mean when the plumb line hangs precisely over the calibrated center mark?",
                            "options": [
                                "Both feet of the A-frame are resting on points of exactly equal elevation on a horizontal contour line.",
                                "The slope is completely flat with 0% gradient.",
                                "The soil beneath the feet is completely waterlogged.",
                                "The A-frame is leaning directly downhill."
                            ],
                            "answer": "A",
                            "explanation": "When the plumb-bob aligns with the center mark on the crossbar, it confirms that both feet of the A-frame are resting on points at the exact same elevation, establishing a true horizontal contour line."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- An **A-frame tool** allows farmers to peg accurate horizontal contour lines without expensive laser surveying.\n- Steeper slopes require **narrower strip widths (10–15m)** to arrest fast runoff.\n- Always **till and plant along the contour lines**, never vertically downhill.\n- Alternating cereals with legumes preserves soil nitrogen and suppresses pests."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What happens when heavy storm runoff collects into concentrated channels? In Lesson 3, we explore the engineering of grassed waterways to safely discharge excess floodwater!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Grassed Waterways
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Grassed Waterways",
            "unit_description": "Grassed waterways definition, hydrodynamic mechanics, parabolic cross-section engineering, grass species selection (Kikuyu, Star, Vetiver), gully healing, and field video demo.",
            "lesson_title": "Grassed Waterways",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "The Green Drainage Highway: Grassed Waterway",
                        "content": {
                            "title": "The Green Drainage Highway: Grassed Waterway",
                            "caption": "A wide, shallow, grass-carpeted depression safely conducting heavy storm runoff down a slope without causing soil erosion."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Waterway Engineering",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **grassed waterway** and explain how it prevents destructive gully erosion.",
                                "Describe the hydrodynamic function of a **wide parabolic (saucer-shaped) cross-section**.",
                                "Select ideal grass species based on **rhizome density, deep sod, and submergence tolerance**.",
                                "Watch an authentic engineering video demonstration on constructing stabilized waterways."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Grassed Waterway?",
                        "content": {
                            "title": "Nature's Safe Drainage Highway",
                            "text": "A **grassed waterway** is a broad, shallow, gently sloping parabolic drainage channel stabilized with dense perennial sod grass. It is designed to receive concentrated runoff from diversion ditches, terraces, and road culverts, conducting it safely down a slope to a natural river or farm pond without carving gullies."
                        }
                    }
                ],
                # Page 2: Gully vs Grassed Waterway Hydrodynamics
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Grassed Waterway vs Destructive Bare Gully",
                        "content": {
                            "title": "Grassed Waterway vs Destructive Bare Gully",
                            "caption": "Cross-sectional engineering comparison: Bare V-shaped gully with turbulent scour (left) vs. wide parabolic grassed channel with lamina flow (right)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Physics of Parabolic Flow",
                        "content": {
                            "title": "Why Saucer-Shaped Channels Prevent Erosion",
                            "text": "- **V-Shaped Bare Gully**: Forces water into a narrow, deep channel. High water depth generates immense friction and turbulent energy that rips soil particles from the bed, carving deep trenches.\n- **Parabolic Grassed Waterway**: Spreads floodwater out into a very wide, thin sheet (depth < 10 cm). The dense turf blades create gentle surface resistance, converting destructive turbulence into smooth, non-erosive laminar flow."
                        }
                    }
                ],
                # Page 3: Ideal Grass Species Selection
                [
                    {
                        "type": "comparison_table",
                        "title": "Grass Species for Waterway Stabilization",
                        "content": {
                            "title": "Grass Species Characteristics & Environmental Fit",
                            "headers": ["Grass Species", "Root Architecture", "Water Tolerance", "Best Agro-Ecological Zone"],
                            "rows": [
                                ["Kikuyu Grass (Pennisetum clandestinum)", "Dense underground rhizomes forming thick sod mattress", "High water & silt tolerance", "Highland fertile zones (Central, Rift Valley)"],
                                ["Star Grass (Cynodon dactylon)", "Fast-spreading stolons that root at nodes", "Drought tolerant; recovers rapidly after floods", "Medium altitude & drylands (Eastern, Coast)"],
                                ["Vetiver Grass (Chrysopogon zizanioides)", "Massive vertical roots (up to 3m deep) anchoring subsoil", "Survives complete submersion & severe drought", "All zones, steep drainage outlets & riverbanks"],
                                ["Paspalum (Paspalum notatum)", "Tough low-growing carpet resistant to heavy livestock", "High flood tolerance", "Humid lake basins & coastal plains"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Demonstration — Waterway Construction
                [
                    {
                        "type": "suggested_video",
                        "title": "Field Video: Building a Waterway with Grade Stabilization",
                        "content": {
                            "title": "Field Video: Building a Waterway with Grade Stabilization",
                            "url": "https://www.youtube.com/watch?v=KU5ru2xXqgY",
                            "resolved_video_id": "KU5ru2xXqgY",
                            "caption": "Watch conservation engineers shape a broad parabolic waterway, install grade stabilization structures, and establish dense turf grass to prevent gully erosion."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Engineering Lessons from the Video",
                        "content": {
                            "title": "Critical Construction Rules",
                            "text": "- **1. Shape Before Seeding**: Waterways must have wide, flat-bottomed parabolic profiles. Triangular or sharp V-bottoms will fail.\n- **2. Establish Grass Before Diverting Water**: Never divert storm runoff into a newly dug channel until the grass sod has formed a 100% dense root carpet!\n- **3. Check Dams During Establishment**: Use small temporary stone checks to slow water while grass sprouts grow."
                        }
                    }
                ],
                # Page 5: Interactive Grass Selection Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Grass Selection Challenge",
                        "content": {
                            "title": "Matching Soil Stabilization Needs",
                            "instructions": "Select the best grass species for stabilizing a newly excavated waterway in a highland school with heavy rainfall:",
                            "scenario": "A school in Meru has a parabolic channel receiving heavy storm runoff from 4 hectares of farmland.",
                            "question": "Which grass species provides the densest sod mattress to prevent bed scouring?",
                            "options": [
                                "Kikuyu Grass or Vetiver Grass",
                                "Erect Bunch Grass with sparse roots",
                                "Maize Stalks planted in rows",
                                "Castor Oil Plants"
                            ],
                            "correct_feedback": "Correct! Kikuyu grass forms a continuous interlocking sod mattress, and Vetiver anchors deep roots, providing elite erosion protection.",
                            "incorrect_feedback": "Incorrect. Bunch grasses and row crops leave bare exposed soil channels. Dense sod-forming grasses like Kikuyu and Vetiver are required."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Waterway Cross-Section Design",
                        "content": {
                            "question": "Why are grassed waterways constructed with a wide, shallow parabolic (saucer) cross-section rather than a narrow V-shape?",
                            "options": [
                                "Parabolic shapes spread flowing water into a thin, wide sheet, reducing its depth and velocity to prevent bed scouring.",
                                "A V-shape is impossible to dig with standard shovels.",
                                "Parabolic shapes prevent frogs from laying eggs in the channel.",
                                "A V-shape causes water to evaporate too quickly."
                            ],
                            "answer": "A",
                            "explanation": "Spreading water across a wide, shallow parabolic channel drastically reduces the hydraulic depth and velocity of runoff. The dense grass creates resistance that maintains non-erosive laminar flow."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Grassed waterways** conduct concentrated runoff safely downhill without gully formation.\n- They feature **wide parabolic cross-sections** that spread water into thin, slow sheets.\n- **Sod-forming perennial grasses** (Kikuyu, Star, Vetiver) provide dense subterranean root anchors.\n- Never divert floodwater into a waterway until grass sod is **fully established**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What if our farm is located in an arid or stony region where digging waterways is difficult? In Lesson 4, we examine how stone lines and trash lines trap sediment using locally available materials!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Stone Lines and Trash Lines
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Stone Lines and Trash Lines",
            "unit_description": "Stone lines and trash lines: semi-permeable barrier physics, sediment deposition, progressive natural terracing, material sourcing, and dryland soil conservation video.",
            "lesson_title": "Stone Lines and Trash Lines",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Defenders of the Drylands: Stone and Trash Lines",
                        "content": {
                            "title": "Defenders of the Drylands: Stone and Trash Lines",
                            "caption": "Carefully constructed stone lines and dry crop residue trash lines running horizontally across semi-arid farmland to trap soil."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Semi-Permeable Barriers",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **stone lines** and **trash lines** as semi-permeable conservation structures.",
                                "Explain how semi-permeable barriers allow water to filter through while trapping 100% of eroded sediment.",
                                "Describe how trapped sediment creates **progressive natural terraces** over several seasons.",
                                "Analyze a video lesson on soil conservation in dryland agriculture."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Semi-Permeable Barriers",
                        "content": {
                            "title": "Why Total Dams Fail in Drylands",
                            "text": "In arid and semi-arid lands (ASALs), solid impermeable walls often burst under sudden flash floods. **Stone lines** and **trash lines** are semi-permeable barriers: they slow runoff down, allow clean water to seep through gently, but catch all the fertile soil particles, creating nutrient-rich micro-basins behind them."
                        }
                    }
                ],
                # Page 2: Mechanics of Semi-Permeable Filtration
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Contour vs Downhill Barrier Alignment Dynamics",
                        "content": {
                            "title": "Contour vs Downhill Barrier Alignment Dynamics",
                            "caption": "Hydrodynamic comparison: Horizontal contour barrier trapping sediment (left) vs. incorrect downhill barrier funneling runoff into gullies (right)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Progressive Natural Terracing",
                        "content": {
                            "title": "How Barriers Evolve into Terraces",
                            "text": "Over 2 to 4 rainy seasons, sediment builds up behind each stone or trash line, gradually leveling the ground between lines. What started as a simple line of rocks transforms naturally into a series of **flat, fertile bench terraces** without requiring back-breaking excavation!"
                        }
                    }
                ],
                # Page 3: Comparison: Stone Lines vs Trash Lines
                [
                    {
                        "type": "comparison_table",
                        "title": "Stone Lines vs Trash Lines Matrix",
                        "content": {
                            "title": "Material & Operational Comparison",
                            "headers": ["Feature", "Stone Lines", "Trash Lines"],
                            "rows": [
                                ["Primary Materials", "Volcanic or field stones, rocks, gravel", "Dry maize stalks, sorghum residues, pruned twigs, dry grass"],
                                ["Durability & Lifespan", "Permanent (lasts decades with minor maintenance)", "Temporary (1 to 2 seasons; decomposes into organic humus)"],
                                ["Best Agro-Ecological Zone", "Stony hillsides, semi-arid regions (Kitui, Machakos, Turkana)", "Cultivated crop farms with abundant post-harvest residue"],
                                ["Soil Biology Benefit", "Provides shelter for beneficial predatory insects", "Adds rich organic matter and feeds earthworms as it rots"],
                                ["Termite Susceptibility", "Completely immune to termites and fires", "Vulnerable to termites and dry-season bushfires"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Dryland Soil Conservation
                [
                    {
                        "type": "suggested_video",
                        "title": "Video Lesson: Soil Conservation in Drylands",
                        "content": {
                            "title": "Video Lesson: Soil Conservation in Drylands",
                            "url": "https://www.youtube.com/watch?v=32GAiA33nt8",
                            "resolved_video_id": "32GAiA33nt8",
                            "caption": "Watch how agriculturalists in Kenya utilize stone lines, trash lines, and contour barriers to rehabilitate degraded dryland soils."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Field Takeaways from the Video",
                        "content": {
                            "title": "Practical Observations",
                            "text": "- **1. Large Stones Downhill, Small Stones Uphill**: Always place large foundation rocks on the downhill side, backing them with smaller gravel on the uphill side to create an effective silt filter.\n- **2. Termite Management for Trash Lines**: Mix thorny branches or non-palatable crop residues (like sunflower stalks) to deter termites from eating trash lines too quickly.\n- **3. Spacing Rule**: Space lines 10 to 20 meters apart depending on slope steepness."
                        }
                    }
                ],
                # Page 5: Interactive Material Sourcing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Material Selection Challenge",
                        "content": {
                            "title": "Selecting the Right Barrier for the Farm",
                            "instructions": "Determine the ideal barrier for the following dryland farm scenario:",
                            "scenario": "A farm in Machakos has a rocky 8% hillside littered with surface stones and suffers from frequent dry-season bushfires.",
                            "question": "Which conservation barrier should the farmer establish?",
                            "options": [
                                "Stone Lines (Clears rocks from fields and resists fire completely)",
                                "Plastic Sheet Barriers",
                                "Trash Lines made of dry grass (High fire risk)",
                                "Bare Soil Ridges without grass"
                            ],
                            "correct_feedback": "Correct! Stone lines clear stones from the cultivation zone and are 100% fireproof, making them the optimal choice for rocky semi-arid slopes.",
                            "incorrect_feedback": "Incorrect. In fire-prone rocky areas, stone lines are ideal because they clear the farm of stones and cannot burn."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Semi-Permeable Filtration",
                        "content": {
                            "question": "Why are stone lines described as 'semi-permeable' rather than 'impermeable' barriers?",
                            "options": [
                                "They allow excess water to filter through slowly without bursting, while trapping suspended soil and organic particles on the uphill side.",
                                "They dissolve completely when exposed to rainwater.",
                                "They suck water into underground magnetic reservoirs.",
                                "They only let rocks pass through while stopping water."
                            ],
                            "answer": "A",
                            "explanation": "Semi-permeable barriers slow down runoff velocity so water can filter through the stone gaps safely, while stopping the eroded topsoil and creating fertile sediment deposits behind the line."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Stone lines and trash lines** are affordable, low-tech semi-permeable conservation barriers.\n- They **decelerate runoff, trap fertile topsoil, and increase water infiltration**.\n- Over time, trapped silt creates **progressive natural terraces** across the slope.\n- Stone lines are permanent and fireproof; trash lines decompose into organic humus."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we construct stone lines and trash lines step-by-step in the field? In Lesson 5, we grab our gloves, tape measures, and materials for hands-on construction!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Practical: Preparing Stone Lines and Trash Lines
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Practical: Preparing Stone Lines and Trash Lines",
            "unit_description": "Practical construction: trenching, stone sorting (large downhill, gravel uphill), trash line dimensions (30cm height x 50cm width), wooden staking, and maintenance.",
            "lesson_title": "Practical: Preparing Stone Lines and Trash Lines",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Hands-on Engineering: Building Contour Lines",
                        "content": {
                            "title": "Hands-on Engineering: Building Contour Lines",
                            "caption": "Students working collaboratively to peg contours, stack stones, and compact trash lines along a school slope."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Construction Standards",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Peg contour lines accurately across a field using an A-frame.",
                                "Construct a stone line using the **interlocking pyramid method (large stones downhill)**.",
                                "Build a standard trash line to precise dimensions (**30–40 cm height, 50 cm base width**).",
                                "Anchor trash lines using wooden pegs to prevent flood dislodgement."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Precision Construction Matters",
                        "content": {
                            "title": "Building Barriers That Last",
                            "text": "A poorly built stone line or loose trash line can easily be breached by a sudden heavy storm. When a barrier breaks, water rushes through the breach at high speed, creating a dangerous concentrated jet that carves deep gullies. Careful construction to exact engineering dimensions guarantees barrier strength."
                        }
                    }
                ],
                # Page 2: Engineering Blueprint for Trash Lines
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Standard Trash Line Cross-Section & Dimensions Blueprint",
                        "content": {
                            "title": "Standard Trash Line Cross-Section & Dimensions Blueprint",
                            "caption": "Technical diagram specifying: 50cm base width, 35cm height, supporting wooden stakes at 1m intervals, and trapped sediment deposition zone on the uphill side."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Building a Stone Line",
                        "content": {
                            "title": "Step-by-Step Stone Line Construction",
                            "steps": [
                                "**Step 1: Mark Contours**: Use an A-frame to drive wooden pegs along the contour at 10m to 15m intervals down the slope.",
                                "**Step 2: Shallow Trenching**: Dig a shallow foundation furrow (5 to 10 cm deep) along the peg line to anchor the base rocks.",
                                "**Step 3: Base Rock Layer**: Place largest, heaviest flat stones on the downhill side of the furrow.",
                                "**Step 4: Backfill with Small Gravel**: Pack smaller stones and gravel on the uphill side to form a tight, permeable silt filter."
                            ]
                        }
                    }
                ],
                # Page 3: Step-by-Step Trash Line Construction Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Building a Trash Line",
                        "content": {
                            "title": "Step-by-Step Trash Line Construction",
                            "steps": [
                                "**Step 1: Gather Materials**: Collect dry maize stalks, sorghum stubble, pruned twigs, and dry weeds after harvest.",
                                "**Step 2: Drive Support Stakes**: Drive wooden pegs (50 cm tall) in pairs along the contour line, spaced 1 meter apart.",
                                "**Step 3: Pack Residues**: Lay crop stalks tightly between the pegs, alternating stem orientations to interlock fibers.",
                                "**Step 4: Compact to Dimensions**: Press down firmly until the line reaches **30–40 cm height and 50 cm width**.",
                                "**Step 5: Anchor with Soil**: Throw a light shovel of soil over the uphill edge to weigh the trash line down against strong winds."
                            ]
                        }
                    }
                ],
                # Page 4: Safety and Maintenance Protocols
                [
                    {
                        "type": "concept_explanation",
                        "title": "Safety & Post-Storm Maintenance",
                        "content": {
                            "title": "Keeping Barriers Functional",
                            "text": "- **Personal Safety**: Wear thick leather gloves when handling rough rocks and thorny branches. Lift heavy stones with bent knees, keeping your back straight.\n- **Post-Rain Inspection**: Walk the contour lines after every heavy storm. If stones have shifted or trash lines have settled, add fresh material immediately to maintain the 35 cm height."
                        }
                    }
                ],
                # Page 5: Interactive Construction Step Sequencing
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Stone Line Construction Sequencing",
                        "content": {
                            "title": "Ordering Stone Line Construction Steps",
                            "instructions": "Place the stone line assembly steps in chronological order:",
                            "scenario": "Your agriculture club has stones gathered and pegs ready.",
                            "question": "Which activity must be performed immediately BEFORE laying the base stones?",
                            "options": [
                                "Digging a shallow 5–10 cm foundation furrow along the contour pegs",
                                "Pouring concrete over the slope",
                                "Planting maize seeds inside the stone pile",
                                "Painting the stones white"
                            ],
                            "correct_feedback": "Correct! Digging a shallow foundation furrow anchors the base rocks and prevents water from undercutting the stone line.",
                            "incorrect_feedback": "Incorrect. Before placing stones, you must excavate a shallow foundation trench to anchor the stones firmly in place."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Stone Placement Rule",
                        "content": {
                            "question": "When constructing a stone line across a hillside, where should the largest stones be placed, and why?",
                            "options": [
                                "On the downhill side of the line, to form a sturdy foundation that supports smaller stones and resists the push of flowing runoff.",
                                "Balanced precariously on top of the pile.",
                                "Scattered randomly across the field.",
                                "Buried 2 meters deep under the subsoil."
                            ],
                            "answer": "A",
                            "explanation": "Placing the largest, heaviest stones on the downhill side creates a strong structural barrier that resists the hydrostatic push of floodwaters and supports the smaller filter gravel on the uphill side."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Stone lines require a **shallow 5–10 cm trench** with **large stones downhill** and small gravel uphill.\n- Trash lines should be built to **30–40 cm height and 50 cm width**, anchored with wooden stakes.\n- Regular inspection after storms ensures continuous sediment trapping.\n- Always observe **lifting ergonomics and hand safety** when moving rocks."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What if our slope is steep and we want to harvest large volumes of water while stopping erosion? In Lesson 6, we examine the powerful engineering of soil bunds and Fanya Juu / Fanya Chini terraces!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Soil Bunds: Meaning and Practical Preparation
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Soil Bunds: Meaning and Practical Preparation",
            "unit_description": "Soil bunds: definitions, Fanya Juu vs Fanya Chini mechanics, trench-and-embankment engineering, stabilizing grass planting, and field instructional video.",
            "lesson_title": "Soil Bunds: Meaning and Practical Preparation",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Earthworks of Resilience: Soil Bunds & Terraces",
                        "content": {
                            "title": "Earthworks of Resilience: Soil Bunds & Terraces",
                            "caption": "Impressive earthen soil bunds stabilized with lush green Napier grass lining the contours of a Kenyan hillside."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Soil Bund Engineering",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **soil bunds** and explain their dual function: **stopping erosion and harvesting water**.",
                                "Contrast **Fanya Juu terraces** (soil thrown uphill) with **Fanya Chini structures** (soil thrown downhill).",
                                "Calculate dimensions for channel trenches (60 cm wide x 60 cm deep) and earthen embankments (50 cm high).",
                                "Watch field video demonstrations on soil bund digging and rangeland greening in Kenya."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "What is a Soil Bund?",
                        "content": {
                            "title": "Major Earthen Conservation Structures",
                            "text": "A **soil bund** (or contour earth bank) is an artificial ridge of earth constructed along the contour by digging an adjacent trench and heaping the excavated soil into a compact embankment. Soil bunds are among the most powerful conservation structures in East Africa, transforming dry, eroded slopes into fertile, moisture-rich farming terraces."
                        }
                    }
                ],
                # Page 2: Fanya Juu vs Fanya Chini Engineering
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Soil Bund Cross-Section & Embankment Engineering",
                        "content": {
                            "title": "Soil Bund Cross-Section & Embankment Engineering",
                            "caption": "Cross-sectional engineering diagram: 60cm x 60cm excavation trench, 50cm high compacted soil ridge, stabilizing grass planted on ridge crest, and deep moisture infiltration zone."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Fanya Juu vs Fanya Chini Comparison",
                        "content": {
                            "title": "Terracing Structure Mechanics",
                            "headers": ["Feature", "Fanya Juu ('Throw Up')", "Fanya Chini ('Throw Down')"],
                            "rows": [
                                ["Soil Placement", "Excavated soil is thrown on the **uphill side** of the trench", "Excavated soil is thrown on the **downhill side** of the trench"],
                                ["Primary Function", "Rapidly develops into a level bench terrace; traps maximum sediment", "Acts as a retention/diversion ditch to convey excess storm runoff away"],
                                ["Slope Suitability", "Medium to steep slopes (5% to 20%)", "Gentle slopes (< 5%) with high waterlogging risk"],
                                ["Water Harvesting", "High: water ponds in trench below the terrace step", "Medium: trench conveys water across gentle gradients"],
                                ["Grass Stabilization", "Napier grass or Vetiver planted on top of the uphill ridge", "Grass planted on the downhill ridge"]
                            ]
                        }
                    }
                ],
                # Page 3: Step-by-Step Soil Bund Construction Protocol
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Excavating Soil Bunds",
                        "content": {
                            "title": "Step-by-Step Bund Excavation",
                            "steps": [
                                "**Step 1: Peg the Contour**: Use an A-frame to peg horizontal lines spaced 10m to 20m apart down the slope.",
                                "**Step 2: Mark Trench Width**: Mark two parallel lines 60 cm apart along the contour pegs.",
                                "**Step 3: Excavate Trench**: Dig out topsoil and subsoil to a depth of **60 cm**, throwing all soil to the uphill side (for Fanya Juu).",
                                "**Step 4: Compact the Ridge**: Shape the heaped soil into a trapezoidal ridge **50 cm high with a 1m base**, beating it firm with the flat of a shovel.",
                                "**Step 5: Plant Stabilizing Grass**: Immediately plant Napier grass, Vetiver, or Guinea grass along the ridge crest to lock soil with roots."
                            ]
                        }
                    }
                ],
                # Page 4: Video Resources — Fanya Juu & Soil Bund Digging in Kenya
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Fanya Juu & Fanya Chini Terracing in Kenya",
                        "content": {
                            "title": "Instructional Video: Fanya Juu & Fanya Chini Terracing in Kenya",
                            "url": "https://www.youtube.com/watch?v=dj8palecLKE",
                            "resolved_video_id": "dj8palecLKE",
                            "caption": "Watch Justdiggit demonstrate the step-by-step construction of Fanya Juu and Fanya Chini terraces and semi-circular bunds to green degraded lands in Kenya."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Field Demonstration: Greening Kenya's Arid Lands with Soil Bunds",
                        "content": {
                            "title": "Field Demonstration: Greening Kenya's Arid Lands with Soil Bunds",
                            "url": "https://www.youtube.com/watch?v=TN2juOT9pNQ",
                            "resolved_video_id": "TN2juOT9pNQ",
                            "caption": "See how community farmers dig extensive soil bunds in Kenya's arid rangelands to capture flash flood runoff and restore pastures for livestock."
                        }
                    }
                ],
                # Page 5: Interactive Structure Choice Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Terracing Selection Challenge",
                        "content": {
                            "title": "Choosing Between Fanya Juu and Fanya Chini",
                            "instructions": "Determine the ideal structure for the following farm scenario:",
                            "scenario": "A farm on a steep 15% hillside in Machakos suffers from heavy soil loss during rains and needs to form level bench terraces quickly.",
                            "question": "Which earthwork structure should the farmer construct?",
                            "options": [
                                "Fanya Juu Terraces (Soil thrown uphill to rapidly form bench terraces)",
                                "Fanya Chini (Soil thrown downhill)",
                                "Deep vertical drainage trenches running down the slope",
                                "Flat unplowed plots"
                            ],
                            "correct_feedback": "Correct! On steep hillsides, Fanya Juu is the gold standard because throwing soil uphill rapidly accelerates natural bench terrace development.",
                            "incorrect_feedback": "Incorrect. On steep slopes, Fanya Juu (throwing soil uphill) is specifically designed to create level bench terraces and trap soil."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Napier Grass Function on Bunds",
                        "content": {
                            "question": "Why is it mandatory to plant perennial grasses like Napier or Vetiver along the crest of a newly dug soil bund embankment?",
                            "options": [
                                "Dense root networks bind the loose earthen ridge together, preventing the embankment from washing away during heavy downpours.",
                                "Grass makes the bund invisible to wild animals.",
                                "Grass blocks the sun so the soil bund does not dry out.",
                                "Grass changes the chemical composition of the air above the bund."
                            ],
                            "answer": "A",
                            "explanation": "Newly excavated soil ridges are loose and vulnerable to erosion. Planting sod-forming grasses binds the soil with dense roots, stabilizing the ridge and providing valuable livestock fodder."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Soil bunds** consist of an excavated trench (60x60 cm) and an earthen embankment (50 cm high).\n- **Fanya Juu** (soil uphill) is best for medium/steep slopes to form bench terraces.\n- **Fanya Chini** (soil downhill) is used on gentle slopes for water diversion.\n- Always **stabilize ridges with Napier grass or Vetiver** to prevent bank collapse."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered strip cropping, waterways, stone lines, trash lines, and soil bunds! In Lesson 7, we synthesize all these structures into a comprehensive 3D Model Farm Planning Project!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7: Project Part 1: Model Planning and Design
        # =====================================================================
        {
            "unit_order": 7,
            "unit_name": "Project Part 1: Model Planning and Design",
            "unit_description": "Project-based learning: designing a 3D physical model of a conserved farm layout, topographic zoning, scaling, and material budgeting.",
            "lesson_title": "Project Part 1: Model Planning and Design",
            "pages": [
                # Page 1: Visual Hook & Project Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Master Blueprints: 3D Model Farm Planning",
                        "content": {
                            "title": "Master Blueprints: 3D Model Farm Planning",
                            "caption": "Agriculture students collaborating over a scale blueprint diagram of an integrated soil-conserved farm layout."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Farm Model Architecture",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Design a 2D scale blueprint layout incorporating **all 5 conservation structures**.",
                                "Zone farm structures logically by slope elevation (**Upper, Mid, Lower Slopes**).",
                                "Create a budget and collection plan for recycled model materials (cardboard, papier-mâché, gravel, twigs).",
                                "Establish collaborative group roles for the model construction phase."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Art of Integrated Landscape Planning",
                        "content": {
                            "title": "Connecting Conservation Structures",
                            "text": "A single conservation structure alone cannot protect a farm. True resilience comes from an **integrated landscape design** where structures support one another: cut-off drains divert excess road runoff into grassed waterways, while contour bunds, strip cropping, and stone lines slow down water across fields."
                        }
                    }
                ],
                # Page 2: Topographic Zoning Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Topographic Farm Blueprint: 5 Integrated Structures",
                        "content": {
                            "title": "Topographic Farm Blueprint: 5 Integrated Structures",
                            "caption": "Top-down scale blueprint diagram zoning: Upper slope (Tree belts & Cut-off drain), Mid slope (Strip cropping & Stone lines), Lower slope (Soil bunds & Grassed waterway discharge)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Topographic Slope Zoning Matrix",
                        "content": {
                            "title": "Slope Elevation & Structure Allocation",
                            "headers": ["Slope Zone", "Gradient & Risk", "Allocated Structures", "Engineering Rationale"],
                            "rows": [
                                ["Upper Slope (Crest)", "Steep, rocky, high runoff origin", "Afforestation trees, cut-off drains, stone lines", "Intercepts runoff before it enters crop fields"],
                                ["Mid Slope (Cultivation)", "Moderate slope, primary crop zone", "Strip cropping (maize/legumes), trash lines", "Slows sheet wash and maintains soil fertility"],
                                ["Lower Slope (Valley)", "Gentle slope, high water accumulation", "Fanya Juu soil bunds, grassed waterway, farm pond", "Stores infiltrated water and safely discharges flood runoff"]
                            ]
                        }
                    }
                ],
                # Page 3: Material Sourcing & Model Engineering Standards
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Material Preparation",
                        "content": {
                            "title": "Model Material Sourcing Protocol",
                            "steps": [
                                "**1. Base Board**: Sturdy corrugated cardboard or plywood base (60 cm x 40 cm).",
                                "**2. Topography Shaping**: Build 3D hillside slopes using papier-mâché, clay, or styrofoam layers.",
                                "**3. Miniature Structures**: Use aquarium gravel/small pebbles for stone lines; dried matchsticks/twigs for trash lines.",
                                "**4. Green Turf**: Use dyed green sawdust or felt for grassed waterways and Napier grass bund crests.",
                                "**5. Crop Strips**: Color-coded painted seeds for maize (yellow) and legumes (green)."
                            ]
                        }
                    }
                ],
                # Page 4: Group Role Allocation Framework
                [
                    {
                        "type": "concept_explanation",
                        "title": "Collaborative Team Structure",
                        "content": {
                            "title": "Team Roles for Model Building",
                            "text": "- **Chief Architect**: Oversees scale measurements and contour accuracy.\n- **Landscape Engineer**: Shapes 3D slope contours and excavates waterways.\n- **Materials Manager**: Collects, cleans, and prepares gravel, clay, and twigs.\n- **Agronomist**: Attaches miniature crop strips and labels all structures."
                        }
                    }
                ],
                # Page 5: Interactive Landscape Zoning Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Model Zoning Challenge",
                        "content": {
                            "title": "Allocating Conservation Structures by Elevation",
                            "instructions": "Place the structure in its correct topographic slope zone:",
                            "scenario": "Your group is assigning model locations for a Cut-off Drain and a Grassed Waterway.",
                            "question": "Where should the Cut-off Drain be positioned on the 3D model hillside?",
                            "options": [
                                "At the upper crest of the slope above the crop fields (to intercept incoming hillside runoff)",
                                "At the very bottom in the valley basin",
                                "In the middle of the maize strip",
                                "Underneath the cardboard base"
                            ],
                            "correct_feedback": "Correct! Cut-off drains are placed at the top of the slope to intercept external runoff before it can damage cultivated fields below.",
                            "incorrect_feedback": "Incorrect. Cut-off drains belong at the top/upper slope to protect fields below from incoming floodwater."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Integrated Landscape Design",
                        "content": {
                            "question": "Why is an integrated combination of soil conservation measures more effective than relying on a single structure alone?",
                            "options": [
                                "Different structures target different slope zones and water dynamics: upper drains intercept floods, mid-slope strips slow sheet wash, and waterways safely discharge excess volume.",
                                "Using multiple structures guarantees government cash grants.",
                                "A single structure always dissolves during rain.",
                                "Multiple structures prevent sunshine from touching the ground."
                            ],
                            "answer": "A",
                            "explanation": "An integrated system creates multiple lines of defense. Upper drains stop external runoff, field strips decelerate surface water, and grassed waterways provide a safe outlet, providing 100% landscape protection."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- 3D models require **topographic zoning (Upper, Mid, Lower Slopes)**.\n- Combine **cut-off drains, stone lines, strip crops, soil bunds, and waterways** into an integrated system.\n- Use **recycled materials** (cardboard, papier-mâché, pebbles, twigs, dyed sawdust).\n- Effective teamwork and clear role allocation guarantee project success."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "Our blueprints and materials are ready! In Lesson 8, we build our 3D physical models, present our work, and tackle the comprehensive Topic Summative Assessment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 8: Project Part 2: Model Construction, Presentation & Capstone
        # =====================================================================
        {
            "unit_order": 8,
            "unit_name": "Project Part 2: Model Construction and Presentation",
            "unit_description": "3D physical model construction, labeling, rubric evaluation, presentation delivery, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Project Part 2: Model Construction and Presentation & Capstone",
            "pages": [
                # Page 1: Visual Hook & Practical Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Showcasing Excellence: 3D Conserved Farm Model",
                        "content": {
                            "title": "Showcasing Excellence: 3D Conserved Farm Model",
                            "caption": "A beautifully detailed, multi-tiered 3D model of a conserved agricultural landscape with realistic soil bunds, stone lines, and waterways."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Model Assembly & Assessment",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Assemble a complete **3D physical farm model** showing all 5 soil conservation measures.",
                                "Label all structures with clear, waterproof indicator flags.",
                                "Deliver an oral group presentation defending your landscape engineering decisions.",
                                "Demonstrate total mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Bringing Blueprints to Life",
                        "content": {
                            "title": "Precision Construction & Peer Review",
                            "text": "Today we transform our 2D blueprints into tangible 3D landscapes! Constructing physical models allows us to test water flow paths, understand slope geometry, and clearly communicate sustainable farming principles to our school community."
                        }
                    }
                ],
                # Page 2: 3D Model Exploded Assembly Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "3D Model Farm Exploded Assembly & Layering Blueprint",
                        "content": {
                            "title": "3D Model Farm Exploded Assembly & Layering Blueprint",
                            "caption": "Exploded assembly layout showing: Base board foundation • Tiered contour slope shaping • Miniature stone lines, trash lines, & bunds • Labeled flag posts."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Model Assembly",
                        "content": {
                            "title": "Step-by-Step Model Assembly",
                            "steps": [
                                "**Step 1: Build Hillside Base**: Shape tiered slope layers from papier-mâché on cardboard. Let dry completely.",
                                "**Step 2: Paint & Texture**: Paint slope with brown/ochre tempera paint; sprinkle fine sand for realistic soil texture.",
                                "**Step 3: Install Barriers**: Glue small stones for stone lines, dry grass bundles for trash lines, and clay ridges for soil bunds.",
                                "**Step 4: Carpet the Waterway**: Glue bright green felt along the central drainage depression.",
                                "**Step 5: Attach Labels**: Pin flag labels identifying each structure and its slope percentage."
                            ]
                        }
                    }
                ],
                # Page 3: Model Assessment Rubric Matrix
                [
                    {
                        "type": "comparison_table",
                        "title": "Model Evaluation Rubric Matrix",
                        "content": {
                            "title": "Assessment Standards for Farm Models",
                            "headers": ["Evaluation Criteria", "Exceeding Expectations (4)", "Meeting Expectations (3)", "Approaching Expectations (2)"],
                            "rows": [
                                ["Contour & Slope Accuracy", "All 5 structures follow precise contours on realistic slopes", "3 to 4 structures correctly aligned on slope", "Structures placed incorrectly down the slope"],
                                ["Material Craftsmanship", "Sturdy construction with neat, realistic recycled materials", "Good assembly with minor loose elements", "Fragile model with messy, unscaled materials"],
                                ["Technical Labeling", "All structures clearly labeled with purpose and dimensions", "All structures labeled with names only", "Missing labels or incorrect names"],
                                ["Oral Defense", "Clear, confident explanation of hydrodynamic principles", "Accurate explanation with occasional hesitation", "Unable to explain how structures stop erosion"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Peer Review Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Peer Model Evaluation Challenge",
                        "content": {
                            "title": "Auditing a 3D Farm Model",
                            "instructions": "Evaluate the peer group's model design and identify the engineering flaw:",
                            "scenario": "Group B presents a model where stone lines run straight up-and-down the hillside slope rather than across the contours.",
                            "question": "What feedback should you provide to Group B?",
                            "options": [
                                "Stone lines must run horizontally along contour lines; running downhill funnels runoff into destructive erosion gullies.",
                                "The model looks great; stones should always run downhill.",
                                "Paint the stones blue to make them waterproof.",
                                "Add live worms to the model."
                            ],
                            "correct_feedback": "Correct! Running barriers downhill turns them into runoff chutes that accelerate erosion. They MUST run horizontally across contours.",
                            "incorrect_feedback": "Incorrect. Barriers placed downhill accelerate water flow and carve gullies. They must follow horizontal contour lines."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Topic Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Physical Modeling Purpose",
                        "content": {
                            "question": "Why is constructing a 3D scale model an effective way to learn agricultural engineering concepts?",
                            "options": [
                                "It allows learners to visualize complex spatial slope dynamics, test water flow interactions, and master landscape design hands-on.",
                                "It replaces the need to ever farm on real soil.",
                                "It guarantees that actual rain will fall on the school farm.",
                                "It is used exclusively for art competitions."
                            ],
                            "answer": "A",
                            "explanation": "3D physical modeling transforms abstract topographical concepts into concrete spatial experiences, allowing students to understand how water interacts with contour barriers across diverse slope elevations."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 1 Master Summary: Soil Conservation Measures",
                        "content": {
                            "text": "- **Soil Conservation** is vital to protect topsoil humus, preserve food security, and halt desertification.\n- **Strip Cropping** alternates row crops with dense cover crops across contours to decelerate runoff.\n- **Grassed Waterways** use wide parabolic channels and sod grass to safely discharge storm floods.\n- **Stone & Trash Lines** act as semi-permeable filters that trap silt and form progressive terraces.\n- **Soil Bunds (Fanya Juu/Chini)** provide heavy-duty terracing and water harvesting on hill slopes.\n- **Integrated Farm Design** combines all measures into an unbreakable multi-tiered defense system."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Soil Conservation Measures & Farm Models",
                        "content": {
                            "title": "Topic Video Review: Soil Conservation Measures & Farm Models",
                            "url": "https://www.youtube.com/watch?v=32GAiA33nt8",
                            "resolved_video_id": "32GAiA33nt8",
                            "caption": "Watch this comprehensive review of soil conservation structures, A-frame surveying, strip cropping, and farm project execution for Grade 8 CBC Agriculture."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Things to Review Before the Exam",
                        "content": {
                            "title": "Exam Preparation Points",
                            "text": "- **1. Slope and Width Rules**: Remember narrower strips (10–15m) for steep slopes; wide parabolic channels for waterways.\n- **2. Soil Placement in Bunds**: Fanya Juu = soil uphill (bench terracing); Fanya Chini = soil downhill (diversion).\n- **3. Semi-Permeable Physics**: Stone and trash lines let clean water seep through while trapping fertile sediment."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Soil Conservation Definition",
                        "content": {
                            "question": "Which of the following best defines soil conservation?",
                            "options": [
                                "The proper management and protection of soil against water and wind erosion to maintain its fertility and structure.",
                                "Digging deep holes across farmland to bury plastic waste.",
                                "Applying large amounts of synthetic chemical fertilizers every week.",
                                "Allowing livestock to graze freely until all grass is consumed."
                            ],
                            "answer": "A",
                            "explanation": "Soil conservation refers to the sustainable management practices that protect soil from physical loss by erosion, nutrient depletion, and chemical degradation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Threat Identification",
                        "content": {
                            "question": "Which human activity destroys soil organic matter and kills beneficial soil microbes through high heat?",
                            "options": [
                                "Slash-and-burn land clearing.",
                                "Mulching with dry grass.",
                                "Strip cropping with beans.",
                                "Constructing stone lines along contours."
                            ],
                            "answer": "A",
                            "explanation": "Slash-and-burn agriculture incinerates protective surface litter and scorches the upper soil layer, destroying humus and killing beneficial bacteria, fungi, and earthworms."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: Strip Cropping Dynamics",
                        "content": {
                            "question": "In a strip cropping system on a sloping field, why are dense cover crops (like beans or sweet potatoes) planted in alternating bands between wide-spaced row crops (like maize)?",
                            "options": [
                                "Dense cover crops act as living barriers that slow runoff velocity, trap eroded soil, and increase moisture infiltration.",
                                "Cover crops make the field smell sweet to attract pollinating birds.",
                                "Row crops cannot grow unless shaded by taller cover crops.",
                                "Cover crops absorb all rainwater so maize roots stay dry."
                            ],
                            "answer": "A",
                            "explanation": "Dense cover crops provide 100% soil canopy and ground cover, breaking the speed of rushing surface runoff and filtering out eroded topsoil particles."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Grassed Waterway Cross-Section",
                        "content": {
                            "question": "Why is a grassed waterway designed with a broad, shallow parabolic cross-section instead of a steep V-shape?",
                            "options": [
                                "It spreads flowing water into a wide, thin sheet with low hydraulic depth, preventing bed scouring and gully formation.",
                                "A parabolic channel is easier for farm tractors to drive across during floods.",
                                "A V-shape causes water to freeze at high temperatures.",
                                "Parabolic shapes prevent soil from absorbing any water."
                            ],
                            "answer": "A",
                            "explanation": "A wide parabolic channel spreads runoff thinly across a broad turf surface, minimizing water velocity and hydraulic shear stress to prevent gully carving."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Grass Species Selection",
                        "content": {
                            "question": "Which grass species is best suited for stabilizing grassed waterways in fertile highland areas due to its dense sod-forming underground rhizomes?",
                            "options": [
                                "Kikuyu Grass (Pennisetum clandestinum).",
                                "Erect Bunch Grass.",
                                "Sorghum Stalks.",
                                "Blackjack Weeds."
                            ],
                            "answer": "A",
                            "explanation": "Kikuyu grass forms an interlocking, turf-forming mattress with dense stolons and rhizomes that firmly anchor channel beds against fast runoff."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Semi-Permeable Function",
                        "content": {
                            "question": "What is the primary operational mechanism of stone lines and trash lines constructed across a contour?",
                            "options": [
                                "They act as semi-permeable filters that slow runoff, let clean water filter through, and trap fertile silt on the uphill side.",
                                "They form solid, impermeable concrete dams that hold water indefinitely.",
                                "They direct water straight down the hill at high speed.",
                                "They reflect heat to accelerate crop ripening."
                            ],
                            "answer": "A",
                            "explanation": "Stone and trash lines are semi-permeable: they resist the destructive rush of runoff, allowing water to seep through safely while capturing fertile eroded topsoil."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Progressive Natural Terracing",
                        "content": {
                            "question": "How do stone lines and trash lines gradually develop into level bench terraces over several farming seasons?",
                            "options": [
                                "Sediment carried by runoff continuously deposits on the uphill side of the barrier, progressively flattening the slope gradient between lines.",
                                "Heavy rocks sink into the earth and push the ground upward from below.",
                                "Earthquakes naturally flatten the land between stone lines.",
                                "Farmers dig out all the soil between the lines with bulldozers."
                            ],
                            "answer": "A",
                            "explanation": "As runoff drops its sediment load behind the barrier each season, soil builds up against the uphill side of the line, naturally leveling the slope into bench terraces."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Fanya Juu Mechanics",
                        "content": {
                            "question": "During the construction of a Fanya Juu terrace, in which direction is the excavated trench soil thrown?",
                            "options": [
                                "Uphill (above the trench) to form a ridge that catches soil and water, accelerating bench terrace formation.",
                                "Downhill (below the trench) to divert water into neighboring roads.",
                                "Evenly scattered across the entire field.",
                                "Transported off the farm in wheelbarrows."
                            ],
                            "answer": "A",
                            "explanation": "In Fanya Juu ('throw up' in Swahili), soil is thrown uphill from the trench, creating a high contour ridge that rapidly captures moving soil and forms a level bench terrace."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Integrated Landscape Planning",
                        "content": {
                            "question": "A farmer on a steep hillside in Machakos experiences severe topsoil loss from heavy storm runoff coming from a public road above her farm. What is the most effective integrated conservation strategy?",
                            "options": [
                                "Construct an upper cut-off drain to divert road runoff into a grassed waterway, establish Fanya Juu bunds with Napier grass on the mid-slope, and lay trash lines across cultivated strips.",
                                "Plow the entire hillside vertically downhill to speed up water drainage.",
                                "Clear all grass and trees from the upper hillside to see the road clearly.",
                                "Apply heavy synthetic pesticides across the bare slope."
                            ],
                            "answer": "A",
                            "explanation": "This integrated plan combines upper interception (cut-off drain), safe conveyance (grassed waterway), slope terracing (Fanya Juu), and field-level protection (trash lines)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Diagnostic Troubleshooting",
                        "content": {
                            "question": "During a farm inspection, you notice a deep gully forming right in the middle of a stone line. What was the most likely engineering error in the barrier's construction?",
                            "options": [
                                "The stone line was laid incorrectly with a low sag point, or not aligned along a true horizontal contour, causing runoff to concentrate and breach the low spot.",
                                "The stones were too small to be seen by the water.",
                                "The stone line was built using volcanic rocks instead of limestone.",
                                "Napier grass was planted too far away from the stones."
                            ],
                            "answer": "A",
                            "explanation": "If a barrier is not aligned precisely along a horizontal contour, water flows toward the lowest sag point. The concentrated volume builds immense pressure, breaching the stones and carving a deep gully."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic1(replace: bool = True):
    """Executes the database transaction to ingest Topic 1 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 1 (DEEP EDITION)")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Hierarchy
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

        # 2. Resolve Topic
        topic_name = "Soil Conservation Measures"
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
                "description": "Comprehensive soil conservation measures: soil physics, threats, strip cropping mechanics, A-frame contour surveying, grassed waterways, stone lines, trash lines, Fanya Juu/Chini soil bunds, and 3D farm model engineering."
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
                        block_id=f"g8_agri_t1_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 1: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic1(replace=replace_flag)
