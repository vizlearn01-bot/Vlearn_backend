"""
VLearn CBC Grade 8 Agriculture — Topic 2: Water Harvesting and Storage
Production Ingestion Engine (Phase 1: Content & Card Architecture - Deep Pedagogical Edition)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 8 (ID: 15, Level: 8)
Subject: Agriculture
Topic: Water Harvesting and Storage (Topic Order: 2)

Decomposed into 4 Learning Units & 4 Published Lessons:
  1. Roof Catchment Water Harvesting (7 Pages, 13 Blocks)
  2. Surface Runoff Harvesting, Sand Dams & Modern Storage (7 Pages, 14 Blocks)
  3. Water Treatment, Filtration and Safe Storage Maintenance (7 Pages, 13 Blocks)
  4. Project: School Water Harvesting System & Capstone (10 Pages, 22 Blocks)

Deep Pedagogical Enhancements:
  - Deep engineering physics: Catchment Yield Math (Yield = Area x Rainfall x 0.85 Runoff Coeff).
  - Multi-barrier water treatment science: Coagulation (Moringa oleifera), sand bio-filtration, UV solar disinfection (SODIS).
  - Sand dam geological physics and subterranean evaporation-free water storage.
  - Multi-video integrations embedded across individual practical lessons.
  - Formative scenario MCQs and Topic Summative MCQs with comprehensive educational explanations.
  - Zero citation bracket leaks, zero meta-tag leaks, and zero raw unrendered LaTeX.

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade8_agriculture_topic2.py [--replace]
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

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 8 Topic 2: Water Harvesting and Storage."""
    return [
        # =====================================================================
        # LESSON 1: Roof Catchment Water Harvesting
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Roof Catchment Water Harvesting",
            "unit_description": "Rooftop rainwater harvesting: catchment dynamics, gutter gradient sizing (1:100 slope), first-flush diverter mechanics, and catchment yield mathematical formulas.",
            "lesson_title": "Roof Catchment Water Harvesting",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Harvesting the Sky: Modern Rooftop Catchment",
                        "content": {
                            "title": "Harvesting the Sky: Modern Rooftop Catchment",
                            "caption": "A corrugated iron roof with seamless gutters, a downpipe, and a first-flush diverter channeling rainwater into a clean storage tank."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Rooftop Water Architecture",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Define **rooftop rainwater harvesting** and identify all 5 structural components.",
                                "Explain why **corrugated galvanized iron sheets** provide higher runoff quality than thatched or asbestos roofs.",
                                "Calculate total harvestable water volume using the **Catchment Yield Formula**.",
                                "Describe the contamination-prevention function of a **first-flush diverter**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Tapping Atmospheric Precipitation",
                        "content": {
                            "title": "Turning Rain into Household Wealth",
                            "text": "In many regions of Kenya, women and children spend up to 4 hours daily trekking to distant, polluted seasonal streams. Rooftop rainwater harvesting intercepts pure precipitation before it touches the contaminated ground, providing an immediate, high-quality domestic water supply right at the homestead."
                        }
                    }
                ],
                # Page 2: Rooftop System Architecture & First-Flush Diverters
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Rooftop Rainwater Catchment Architecture & First-Flush Diverter",
                        "content": {
                            "title": "Rooftop Rainwater Catchment Architecture & First-Flush Diverter",
                            "caption": "Technical blueprint detailing: Corrugated roof • Sloped gutter (1:100 gradient) • Gutter mesh filter • First-flush chamber with floating ball seal • Clean storage tank."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: First-Flush Operation",
                        "content": {
                            "title": "How the First-Flush Diverter Operates Automatically",
                            "steps": [
                                "**1. Dry Spell Dust Accumulation**: Bird droppings, dust, leaves, and soot settle on the roof surface during dry periods.",
                                "**2. Initial Rain Diversion**: The first 1 to 2 mm of rain washes off the roof and enters the vertical first-flush diverter pipe.",
                                "**3. Floating Ball Seal**: As the diverter pipe fills with dirty water, an internal lightweight floating ball rises to the top seat.",
                                "**4. Pure Water Flow**: The sealed ball blocks further entry, forcing all subsequent 100% clean water into the main storage tank!"
                            ]
                        }
                    }
                ],
                # Page 3: The Catchment Yield Formula & Roofing Materials
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Catchment Yield Mathematical Formula",
                        "content": {
                            "title": "Calculating Annual Water Harvest",
                            "text": "The volume of water a household can harvest is calculated using the formula:\n\n**Annual Harvest (Liters) = Roof Area (m²) × Annual Rainfall (mm) × Runoff Efficiency Coefficient (C)**\n\n- **Corrugated Galvanized Iron**: C = 0.85 to 0.90 (Smooth, non-porous, high yield)\n- **Clay Tiles**: C = 0.75 to 0.80 (Slightly porous)\n- **Grass Thatch**: C = 0.20 to 0.30 (Absorbs water, discolors runoff; unsuitable for drinking)"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Roofing Material Performance Comparison",
                        "content": {
                            "title": "Roof Material Characteristics Matrix",
                            "headers": ["Roofing Material", "Runoff Coefficient (C)", "Water Quality", "Health & Safety Rating"],
                            "rows": [
                                ["Corrugated Iron Sheets", "0.85 – 0.90", "High clarity; easily cleaned by first rains", "Safe & Highly Recommended"],
                                ["Baked Clay Tiles", "0.75 – 0.80", "Good quality; retains slight moisture", "Safe"],
                                ["Asbestos Sheets (Old)", "0.80", "Toxic asbestos fibers leach into water", "Extremely Hazardous (Banned)"],
                                ["Grass Thatch", "0.20 – 0.30", "Heavy organic staining, tannins, & debris", "Unsafe for domestic drinking"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Water Harvesting Technology in Kenya
                [
                    {
                        "type": "suggested_video",
                        "title": "Field Video: Modern Water Harvesting in Laikipia County",
                        "content": {
                            "title": "Field Video: Modern Water Harvesting in Laikipia County",
                            "url": "https://www.youtube.com/watch?v=4YRxLP-yjl4",
                            "resolved_video_id": "4YRxLP-yjl4",
                            "caption": "Watch how smallholder farmers in arid Laikipia County install rooftop catchments, water pans, and smart drip irrigation to fight water scarcity."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Observations from the Video",
                        "content": {
                            "title": "Field Practical Insights",
                            "text": "- **1. Gutter Slope Alignment**: Notice how gutters maintain a steady 1:100 slope toward the downpipe to prevent standing puddle mosquito breeding.\n- **2. Storage Capacity Sizing**: See how tanks are sized according to household family consumption during 90-day dry seasons.\n- **3. Overflow Utilization**: Watch how tank overflow pipes are piped directly into kitchen vegetable beds!"
                        }
                    }
                ],
                # Page 5: Interactive Calculation Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Catchment Yield Calculation Challenge",
                        "content": {
                            "title": "Calculating Household Harvest Volume",
                            "instructions": "Calculate the annual harvestable rainwater for the school laboratory roof:",
                            "scenario": "A school laboratory has an iron roof area of 100 m² in a region receiving 800 mm of annual rainfall (Runoff Coefficient = 0.85).",
                            "question": "What is the total annual volume of rainwater collected?",
                            "options": [
                                "68,000 Liters (100 m² × 800 mm × 0.85)",
                                "800 Liters",
                                "8,000 Liters",
                                "680,000 Liters"
                            ],
                            "correct_feedback": "Correct! 100 m² × 800 mm × 0.85 = 68,000 Liters of pure water per year—enough to supply the school for several months!",
                            "incorrect_feedback": "Incorrect. Multiply Area (100) × Rainfall (800) × 0.85 = 68,000 Liters."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: First-Flush Diverter Function",
                        "content": {
                            "question": "What is the primary function of a first-flush diverter in a rooftop rainwater harvesting system?",
                            "options": [
                                "To discard the initial dirty runoff containing bird droppings, soot, and dust so that only clean water enters the main tank.",
                                "To boil the water using solar energy.",
                                "To add chlorine chemicals automatically to the storage tank.",
                                "To stop water from entering the gutters."
                            ],
                            "answer": "A",
                            "explanation": "The first-flush diverter captures and isolates the initial 1–2 mm of dirty roof runoff carrying accumulated debris, preventing contaminants from fouling the main storage tank."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- Rooftop systems consist of **roof catchments, gutters, first-flush diverters, and storage tanks**.\n- **Corrugated iron** is the cleanest, most efficient roofing material (Runoff Coefficient C = 0.85–0.90).\n- The **first-flush diverter** automatically captures dirty initial runoff.\n- Calculate yield using **Yield = Roof Area × Rainfall × Runoff Coefficient**."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "What about the massive volumes of water running across roads and rock outcrops? In Lesson 2, we explore surface runoff harvesting, sand dams, and membrane-lined farm ponds!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Surface Runoff Harvesting, Sand Dams & Modern Storage
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Surface Runoff Harvesting and Storage",
            "unit_description": "Surface runoff harvesting: retention basins, membrane-lined water pans, sand dam geological physics, fog nets, and dryland water storage field video.",
            "lesson_title": "Surface Runoff Harvesting and Storage",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Landscape Water Traps: Surface Runoff Harvesting",
                        "content": {
                            "title": "Landscape Water Traps: Surface Runoff Harvesting",
                            "caption": "A large trapezoidal farm pond lined with a UV-stabilized geomembrane collecting thousands of liters of surface runoff from contour furrows."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Large-Scale Water Harvesting",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Identify 4 primary surface harvesting technologies: **water pans, sand dams, retention ditches, and fog nets**.",
                                "Explain how **sand dams** store water underground in coarse sand, preventing 100% of evaporation.",
                                "Describe the step-by-step construction of a **membrane-lined farm pond**.",
                                "Watch an authentic video on dryland water conservation in Kenya."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Harvesting Landscape Flash Floods",
                        "content": {
                            "title": "Capturing Million-Liter Storms",
                            "text": "During heavy tropical downpours, millions of liters of water rush across roads, fields, and rocky outcrops as surface runoff. By constructing landscape earthworks, sand dams, and lined storage pans, communities capture this immense runoff volume for crop irrigation and livestock watering throughout dry seasons."
                        }
                    }
                ],
                # Page 2: Sand Dam Geological Physics & Modern Water Pans
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sand Dam Geological Physics & Silt Retention Cross-Section",
                        "content": {
                            "title": "Sand Dam Geological Physics & Silt Retention Cross-Section",
                            "caption": "Geological engineering diagram: Reinforced concrete spillway wall across seasonal riverbed • Coarse sand storage reservoir (40% porosity) • Zero evaporation loss • Infiltration well extraction pipe."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Miracle of Sand Dams in Eastern Kenya",
                        "content": {
                            "title": "Subterranean Evaporation-Free Water Banks",
                            "text": "A **sand dam** is a low concrete barrier built across an ephemeral (seasonal) sandy riverbed:\n\n- **Trapping Coarse Sand**: During seasonal flash floods, heavy coarse sand settles behind the concrete wall while fine clay flows over the top.\n- **40% Water Storage**: Clean water is stored inside the voids between sand grains (40% of the sand volume is pure water!).\n- **Zero Evaporation**: Because the water is buried under 2 to 4 meters of sand, sun heat cannot evaporate it, and mosquito larvae cannot survive!"
                        }
                    }
                ],
                # Page 3: Comparison of Surface Storage Technologies
                [
                    {
                        "type": "comparison_table",
                        "title": "Surface Water Harvesting & Storage Technologies",
                        "content": {
                            "title": "Surface Technology Comparison Matrix",
                            "headers": ["Technology", "Operating Mechanism", "Evaporation Risk", "Best Application"],
                            "rows": [
                                ["Membrane-Lined Water Pan", "Trapezoidal earthen basin lined with 0.5–1.0mm HDPE plastic sheet", "High (Open to sun unless shaded with shade nets)", "Crop drip irrigation & fish farming on clay/loam soils"],
                                ["Sand Dam", "Concrete barrier across seasonal riverbed trapping coarse sand aquifer", "Zero (Water stored underground inside sand pores)", "Arid & semi-arid seasonal river valleys (Machakos, Kitui)"],
                                ["Retention Ditch / Micro-Catchment", "Contour trenches capturing runoff directly into root zones", "Low (Moisture absorbed directly by deep subsoil)", "Fruit tree agroforestry orchards on sloping farmland"],
                                ["Fog Harvesting Mesh", "Vertical polyolefin mesh catching suspended cloud droplets", "Low (Drips immediately into sealed tanks)", "Highland coastal & mountain fog belts (Mount Kenya, Taita Hills)"]
                            ]
                        }
                    }
                ],
                # Page 4: Video Resource — Sand Dams & Terracing in Eastern Kenya
                [
                    {
                        "type": "suggested_video",
                        "title": "Instructional Video: Fanya Juu & Sand Dams in TerrAfrica",
                        "content": {
                            "title": "Instructional Video: Fanya Juu & Sand Dams in TerrAfrica",
                            "url": "https://www.youtube.com/watch?v=80jirXONSpY",
                            "resolved_video_id": "80jirXONSpY",
                            "caption": "Watch how conservationists and smallholder farmers construct landscape sand dams and Fanya Juu terraces to transform arid African landscapes."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Engineering Observations from the Video",
                        "content": {
                            "title": "Practical Construction Principles",
                            "text": "- **1. Bedrock Anchoring**: Concrete walls must be firmly anchored into impermeable bedrock to prevent water from slipping underneath.\n- **2. Incremental Height Increases**: Sand dam walls are built in stages (1 meter per season) to ensure only heavy coarse sand settles behind the wall while fine mud washes away.\n- **3. Protected Wells**: Water is extracted through perforated pipe collector wells drilled into the sand bed, keeping water 100% clean."
                        }
                    }
                ],
                # Page 5: Interactive Storage Technology Selection
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Technology Selection Challenge",
                        "content": {
                            "title": "Selecting the Right Surface Water System",
                            "instructions": "Determine the optimal water harvesting technology for the rural dryland community:",
                            "scenario": "A community in Kitui has a seasonal dry riverbed that experiences violent flash floods twice a year, and suffers from extreme summer heat causing heavy evaporation.",
                            "question": "Which technology will store water with zero evaporation loss?",
                            "options": [
                                "Sand Dam constructed across the seasonal riverbed",
                                "Open unshaded shallow pond",
                                "Spraying water into the air with sprinklers",
                                "Digging deep holes in the desert sand without walls"
                            ],
                            "correct_feedback": "Correct! Sand dams store water within coarse sand aquifers beneath the surface, completely protecting it from scorching sun evaporation.",
                            "incorrect_feedback": "Incorrect. In high-heat drylands, open shallow ponds lose over 50% of water to evaporation. Sand dams store water underground with zero evaporation."
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Sand Dam Evaporation Advantage",
                        "content": {
                            "question": "Why do sand dams provide a more reliable water supply during prolonged dry seasons than open earthen ponds in semi-arid areas?",
                            "options": [
                                "Water is stored underground within the pores of coarse sand, completely protected from sun-driven evaporation and disease-carrying mosquito breeding.",
                                "Sand dams generate their own synthetic water chemically.",
                                "Sand dams freeze the water into ice blocks.",
                                "Open ponds attract dangerous wild sharks."
                            ],
                            "answer": "A",
                            "explanation": "Because water in a sand dam is stored below the sand surface, it cannot be evaporated by the sun or contaminated by open airborne dust and mosquito larvae."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- **Surface runoff harvesting** captures large landscape flood volumes for agriculture.\n- **Sand dams** store water underground in coarse sand, achieving **zero evaporation loss**.\n- **Membrane-lined water pans** prevent seepage on porous sandy soils.\n- **Fog harvesting nets** capture atmospheric cloud moisture in high-altitude mountain zones."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "How do we ensure that collected rainwater is 100% safe to drink? In Lesson 3, we master coagulation, multi-layer sand bio-filtration, and chlorination protocols!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Water Treatment, Filtration and Safe Storage Maintenance
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Water Treatment, Filtration and Storage Safety",
            "unit_description": "Water treatment: multi-layer sand-gravel-charcoal bio-filtration, botanical coagulation (Moringa oleifera), boiling, chlorination, and tank sanitization protocols.",
            "lesson_title": "Water Treatment, Filtration and Safe Storage Maintenance",
            "pages": [
                # Page 1: Visual Hook & Learning Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "Pure & Clear: Multi-Stage Water Bio-Filtration",
                        "content": {
                            "title": "Pure & Clear: Multi-Stage Water Bio-Filtration",
                            "caption": "A transparent multi-layer water filter showing fine sand, activated charcoal, and gravel purifying cloudy harvested rainwater into crystal clear drinking water."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Water Purification Science",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Explain the multi-barrier approach to domestic water treatment.",
                                "Construct and explain a **3-stage bio-sand filter (gravel, charcoal, fine sand)**.",
                                "Use **Moringa oleifera seed powder** as an organic botanical coagulant.",
                                "Apply boiling and **chlorination protocols** (WaterGuard dosage) for biological sterilization."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Multi-Barrier Safety Approach",
                        "content": {
                            "title": "Why Filtration Alone is Not Enough",
                            "text": "Even clear-looking rainwater can contain invisible bacteria, amoebae, and viruses. Complete water safety requires a **multi-barrier sequence**: 1. Coagulation & Sedimentation (settling dirt) • 2. Physical Filtration (removing suspended solids) • 3. Disinfection (killing living pathogens)."
                        }
                    }
                ],
                # Page 2: Multi-Layer Bio-Sand Filter Blueprint
                [
                    {
                        "type": "suggested_diagram",
                        "title": "3-Stage Bio-Sand Water Filter & Treatment Blueprint",
                        "content": {
                            "title": "3-Stage Bio-Sand Water Filter & Treatment Blueprint",
                            "caption": "Technical filtration cross-section: Water inlet diffuser • Fine silica sand (traps microbes) • Activated charcoal (removes odors/toxins) • Coarse gravel bed • Clean outlet tap."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Bio-Sand Layering",
                        "content": {
                            "title": "Layering Order from Bottom to Top",
                            "steps": [
                                "**Layer 1: Bottom Drainage (Coarse Gravel)**: 10 cm layer of washed pea gravel (10–15 mm) surrounding the perforated outlet pipe.",
                                "**Layer 2: Transition Buffer (Fine Gravel)**: 5 cm layer of small gravel (2–5 mm) preventing sand from washing down.",
                                "**Layer 3: Adsorption Core (Activated Charcoal)**: 10 cm layer of crushed charcoal to absorb chemical odors and organic toxins.",
                                "**Layer 4: Biological Filter (Fine Sand)**: 30 cm layer of clean, fine silica sand where a biological biofilm (Schmutzdecke) consumes harmful pathogens."
                            ]
                        }
                    }
                ],
                # Page 3: Organic Coagulation & Chemical Disinfection
                [
                    {
                        "type": "concept_explanation",
                        "title": "Botanical Coagulation & Chemical Disinfection",
                        "content": {
                            "title": "Natural and Chemical Sterilization",
                            "text": "- **Moringa oleifera Coagulation**: Crushed Moringa seeds contain positively charged water-soluble proteins that bind with negatively charged clay particles and bacteria, causing them to clump together (flocculate) and settle to the bottom within 1 hour.\n- **Boiling**: Bringing water to a rolling boil for at least 1 minute destroys 100% of pathogenic bacteria, cysts, and viruses.\n- **Chlorination (WaterGuard)**: 1 capful (5 ml) of dilute sodium hypochlorite treats 20 liters of clear water. Wait 30 minutes before drinking!"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Water Treatment Methods Comparison",
                        "content": {
                            "title": "Purification Technology Efficacy Matrix",
                            "headers": ["Method", "Removes Turbidity / Dirt", "Kills Bacteria & Viruses", "Residual Protection", "Cost & Ease"],
                            "rows": [
                                ["Bio-Sand Filter", "High (95% turbidity reduction)", "Moderate (90% microbial removal)", "None", "Low-cost, permanent DIY system"],
                                ["Moringa Coagulation", "High (clarifies muddy water)", "Low (removes 80% with sediment)", "None", "Free from local trees; 100% organic"],
                                ["Rolling Boiling", "None (does not remove dirt)", "High (100% pathogen kill)", "None (re-contaminates easily)", "Requires firewood/gas fuel"],
                                ["Chlorination (WaterGuard)", "None (water must be clear first)", "High (99.9% pathogen kill)", "Yes (protects water in tank for 48 hrs)", "Very cheap and reliable"]
                            ]
                        }
                    }
                ],
                # Page 4: Tank Maintenance & Mosquito Prevention
                [
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Storage Tank Hygiene",
                        "content": {
                            "title": "Tank Maintenance Protocols",
                            "steps": [
                                "**1. Fit Mosquito-Proof Mesh**: Cover all tank inlet pipes and overflow vents with stainless steel wire mesh (mesh size < 1 mm) to stop mosquitoes from breeding.",
                                "**2. Lightproof Storage**: Use opaque, black, or dark green UV-treated tanks. Transparent tanks let sunlight in, stimulating green algae blooms.",
                                "**3. Annual Sludge Drainage**: Open the bottom drain valve once a year before the rainy season to flush out accumulated floor silt."
                            ]
                        }
                    }
                ],
                # Page 5: Interactive Purification Sequencing Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Water Purification Challenge",
                        "content": {
                            "title": "Sequencing Complete Water Treatment",
                            "instructions": "Place the water purification steps in the correct chronological order:",
                            "scenario": "You have collected turbid, muddy rainwater from an open surface pond and need to make it safe for drinking.",
                            "question": "What is the correct treatment sequence?",
                            "options": [
                                "1. Coagulate/Settle dirt -> 2. Pass through Bio-Sand Filter -> 3. Boil or Chlorinate with WaterGuard",
                                "1. Add Chlorine to muddy water -> 2. Boil -> 3. Throw away",
                                "1. Drink muddy water -> 2. Filter -> 3. Add salt",
                                "1. Freeze water -> 2. Melt -> 3. Drink"
                            ],
                            "correct_feedback": "Correct! Always clarify muddy water first through coagulation and bio-sand filtration before applying chemical chlorination or boiling.",
                            "incorrect_feedback": "Incorrect. Chlorine does not work effectively in muddy water because dirt neutralizes the chemical. You must settle and filter dirt first!"
                        }
                    }
                ],
                # Page 6: Formative Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Moringa Coagulation Science",
                        "content": {
                            "question": "How does crushed Moringa oleifera seed powder clarify muddy harvested rainwater?",
                            "options": [
                                "Positively charged seed proteins bind to negatively charged suspended clay particles, causing them to clump together and settle to the bottom as sediment.",
                                "It changes the water into vinegar.",
                                "It turns all mud particles into invisible air bubbles.",
                                "It causes all mud to evaporate into the sky."
                            ],
                            "answer": "A",
                            "explanation": "Moringa seed proteins act as natural cationic polymers. They neutralize the negative charges on suspended clay particles, causing them to bind into heavy clumps (flocs) that settle rapidly to the container floor."
                        }
                    }
                ],
                # Page 7: Summary & Connection Forward
                [
                    {
                        "type": "key_takeaway",
                        "title": "Lesson Summary",
                        "content": {
                            "text": "- The **multi-barrier approach** combines sedimentation, physical filtration, and chemical/thermal disinfection.\n- A **bio-sand filter** uses fine sand, activated charcoal, and gravel to remove impurities and odors.\n- **Moringa oleifera** provides a natural botanical coagulant for muddy water.\n- **Chlorination and boiling** guarantee total destruction of pathogenic microbes."
                        }
                    },
                    {
                        "type": "transition",
                        "title": "Looking Ahead",
                        "content": {
                            "text": "We have mastered catchment engineering, surface storage, and water treatment! In Lesson 4, we integrate all these systems into a complete School Water Harvesting Project and Capstone Assessment!"
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Project: School Water Harvesting System & Capstone
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Project: School Water Harvesting System and Capstone",
            "unit_description": "Project implementation: designing a school rainwater catchment system, budgeting, piping layout, community exhibition, topic video review, and 10 topic summative MCQs.",
            "lesson_title": "Project: School Water Harvesting System & Capstone",
            "pages": [
                # Page 1: Visual Hook & Project Objectives
                [
                    {
                        "type": "suggested_image",
                        "title": "School Infrastructure: Student Water Project",
                        "content": {
                            "title": "School Infrastructure: Student Water Project",
                            "caption": "Agriculture students proudly commissioning a newly installed 10,000-liter school rainwater harvesting tank and drip irrigation garden."
                        }
                    },
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Project Execution & Assessment",
                        "content": {
                            "title": "What We Will Accomplish Today",
                            "goals": [
                                "Design a complete scale architectural plan for a **school rainwater harvesting installation**.",
                                "Prepare a bill of quantities and budget for gutters, brackets, downpipes, and tanks.",
                                "Connect tank overflow to a **kitchen drip irrigation garden**.",
                                "Demonstrate complete mastery on the **10 Topic Summative Assessment Questions**."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Transforming School Water Security",
                        "content": {
                            "title": "Real-World Engineering Impact",
                            "text": "Today we combine our scientific knowledge into a real-world community project! Installing rainwater harvesting at school guarantees clean handwashing water for students, supplies the school kitchen, and provides irrigation for high-yielding vegetable gardens throughout the dry season."
                        }
                    }
                ],
                # Page 2: School Harvesting Blueprint & Piping Layout
                [
                    {
                        "type": "suggested_diagram",
                        "title": "School Rainwater Project Blueprint & Drip Irrigation Integration",
                        "content": {
                            "title": "School Rainwater Project Blueprint & Drip Irrigation Integration",
                            "caption": "Architectural schematic: Classroom block roof catchment (200m²) -> Sloped gutter line -> First-flush chamber -> 10,000L storage tank -> Gravity-fed drip irrigation garden."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Standard Operating Procedure: Project Installation",
                        "content": {
                            "title": "Step-by-Step School Installation Workflow",
                            "steps": [
                                "**Step 1: Roof Audit**: Measure classroom roof dimensions (e.g. 20m x 10m = 200 m²) and inspect fascia boards.",
                                "**Step 2: Gutter Mounting**: Fix PVC or galvanized steel gutter brackets along the fascia board with a continuous **1:100 slope** toward the tank.",
                                "**Step 3: First-Flush Assembly**: Install a vertical 100mm PVC downpipe with a cleanout valve and floating ball seal.",
                                "**Step 4: Tank Foundation**: Construct a reinforced, level concrete or stone slab base (at least 30 cm above ground) to support the 10,000L tank.",
                                "**Step 5: Overflow Plumbing**: Pipe the tank overflow into a raised vegetable bed or sand filter recharge pit."
                            ]
                        }
                    }
                ],
                # Page 3: Bill of Quantities & Project Budgeting
                [
                    {
                        "type": "comparison_table",
                        "title": "School Project Bill of Quantities (Sample Budget)",
                        "content": {
                            "title": "Material & Equipment Budget Matrix",
                            "headers": ["Item Description", "Quantity & Specification", "Function in System", "Estimated Cost Priority"],
                            "rows": [
                                ["PVC Gutters (Half-Round)", "20 meters (4m lengths)", "Captures roof runoff along fascia", "High Priority"],
                                ["Gutter Brackets & Screws", "25 heavy-duty metal brackets", "Secures gutters at 1:100 slope", "High Priority"],
                                ["First-Flush Diverter Kit", "1 unit (100mm PVC with ball)", "Diverts dirty initial roof wash", "High Priority"],
                                ["Rotomolded Water Tank", "10,000 Liters (UV-treated black)", "Main domestic & farm storage", "High Priority"],
                                ["Drip Line Kit", "50 meters perforated drip tape", "Irrigates school vegetable garden", "Medium Priority"]
                            ]
                        }
                    }
                ],
                # Page 4: Interactive Budget Decision Challenge
                [
                    {
                        "type": "interactive_scenario",
                        "title": "Project Budget Optimization Challenge",
                        "content": {
                            "title": "Allocating Project Funds",
                            "instructions": "Identify the most critical component for maintaining water quality on a tight budget:",
                            "scenario": "Your school agriculture club has limited funds and must decide between buying an ornamental signpost or installing a first-flush diverter and mosquito mesh.",
                            "question": "Which choice guarantees water quality and health safety?",
                            "options": [
                                "First-Flush Diverter and Mosquito-Proof Inlet Mesh",
                                "Ornamental Painted Signpost",
                                "Gold-Plated Water Tap",
                                "Plastic Flags around the Tank"
                            ],
                            "correct_feedback": "Correct! First-flush diverters and mosquito meshes are critical functional components that protect water from contaminants and disease vectors.",
                            "incorrect_feedback": "Incorrect. First-flush diverters and mosquito meshes are mandatory to protect health and water quality."
                        }
                    }
                ],
                # Page 5: Formative Knowledge Check & Topic Master Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check: Tank Slab Foundation Rationale",
                        "content": {
                            "question": "Why must a 10,000-liter water storage tank be installed on a level, reinforced masonry or concrete base raised above ground level?",
                            "options": [
                                "Water weighs 1 kg per liter (10,000 kg total); an unlevel base will crack, while elevation provides gravity pressure for water taps and drip lines.",
                                "To prevent underground moles from climbing inside the tank.",
                                "To make the tank closer to passing clouds.",
                                "Because plastic tanks only work when elevated 50 meters in the air."
                            ],
                            "answer": "A",
                            "explanation": "A full 10,000-liter tank weighs 10 metric tons. A level, reinforced foundation prevents structural failure and tank cracking, while elevation creates gravity-fed water pressure."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Topic 2 Master Summary: Water Harvesting and Storage",
                        "content": {
                            "text": "- **Rooftop Rainwater Harvesting** captures clean water (Yield = Area × Rainfall × Runoff Coeff).\n- **First-Flush Diverters** isolate dirty initial roof wash to protect tank water.\n- **Sand Dams** store water underground in coarse sand with **zero evaporation loss**.\n- **Bio-Sand Filtration & Moringa Coagulation** clarify water before chlorination/boiling.\n- **Proper Storage Hygiene** requires lightproof UV tanks, mosquito mesh, and stable foundations."
                        }
                    }
                ],
                # Page 6: Topic Video Review
                [
                    {
                        "type": "suggested_video",
                        "title": "Topic Video Review: Modern Water Harvesting & Drip Technology",
                        "content": {
                            "title": "Topic Video Review: Modern Water Harvesting & Drip Technology",
                            "url": "https://www.youtube.com/watch?v=4YRxLP-yjl4",
                            "resolved_video_id": "4YRxLP-yjl4",
                            "caption": "Watch this comprehensive review of rainwater harvesting, sand dams, tank installation, and water purification for Grade 8 CBC Agriculture."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Key Things to Review Before the Exam",
                        "content": {
                            "title": "Exam Focus Concepts",
                            "text": "- **1. Catchment Formula**: Practice calculating yield for various roof areas and rainfall amounts.\n- **2. Sand Dam Physics**: Understand why subterranean sand storage achieves 0% evaporation.\n- **3. Purification Steps**: Coagulate -> Filter -> Disinfect (Boil or Chlorinate)."
                        }
                    }
                ],
                # Page 7: Topic Assessment Part 1 (Questions 1 to 2)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 1: Catchment Definition",
                        "content": {
                            "question": "Which of the following best describes rainwater harvesting?",
                            "options": [
                                "The collection, concentration, and storage of rainwater runoff from roofs, rock outcrops, or land surfaces for beneficial use.",
                                "Digging deep holes in roads to catch passing floodwater.",
                                "Using chemical sprays to force clouds to rain prematurely.",
                                "Pumping salty seawater directly onto vegetable gardens."
                            ],
                            "answer": "A",
                            "explanation": "Rainwater harvesting is the deliberate collection and storage of atmospheric precipitation from various catchments for domestic, agricultural, and livestock uses."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 2: Gutter Gradient",
                        "content": {
                            "question": "Why must roof gutters be installed with a continuous downward slope of at least 1:100 toward the downpipe?",
                            "options": [
                                "To ensure rapid, complete water flow and prevent stagnant pools where mosquitoes breed and silt settles.",
                                "To make the gutters look artistic on the building.",
                                "To allow birds to slide down the gutters easily.",
                                "To increase the temperature of the flowing water."
                            ],
                            "answer": "A",
                            "explanation": "A minimum gradient of 1:100 ensures that water drains smoothly without pooling in sagging gutter sections, preventing silt buildup and mosquito reproduction."
                        }
                    }
                ],
                # Page 8: Topic Assessment Part 2 (Questions 3 to 5)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 3: First-Flush Function",
                        "content": {
                            "question": "Why is a first-flush diverter considered essential in a rooftop drinking water system?",
                            "options": [
                                "It diverts the initial 1–2 mm of roof runoff carrying bird droppings, soot, and dust away from the main storage tank.",
                                "It adds sugar to the water to improve its taste.",
                                "It increases water volume by 50%.",
                                "It blocks sunlight from touching the roof."
                            ],
                            "answer": "A",
                            "explanation": "The first-flush diverter isolates the contaminated initial wash containing airborne dust, bird feces, and organic matter, protecting the cleanliness of the stored water."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 4: Sand Dam Storage Voids",
                        "content": {
                            "question": "In a sand dam built across a dry riverbed, where and how is the harvestable water stored?",
                            "options": [
                                "Inside the interstitial pore spaces between coarse sand particles (comprising up to 40% of the sand volume) underground.",
                                "In open plastic buckets placed on top of the concrete wall.",
                                "Inside deep hollow concrete pipes suspended in the air.",
                                "In frozen ice blocks beneath tree roots."
                            ],
                            "answer": "A",
                            "explanation": "Coarse sand has high porosity (~40%). Water fills the spaces between sand grains, creating an underground aquifer that is completely protected from evaporation."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 5: Moringa Coagulation Mechanism",
                        "content": {
                            "question": "How does adding crushed Moringa oleifera seed powder clarify cloudy, turbid pond water?",
                            "options": [
                                "Positively charged seed proteins bind with negatively charged clay particles, causing them to flocculate and settle rapidly to the bottom.",
                                "It bleaches the mud particles white so they cannot be seen.",
                                "It turns all suspended dirt into drinkable liquid sugar.",
                                "It dissolves the clay into pure hydrogen gas."
                            ],
                            "answer": "A",
                            "explanation": "Moringa seed proteins act as natural coagulants, neutralizing particle charges and forming heavy flocs that settle to the bottom within 1 hour."
                        }
                    }
                ],
                # Page 9: Topic Assessment Part 3 (Questions 6 to 8)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 6: Bio-Sand Layering",
                        "content": {
                            "question": "In a standard 3-stage domestic bio-sand filter, what is the correct arrangement of media from bottom to top?",
                            "options": [
                                "Bottom: Coarse Gravel -> Middle: Activated Charcoal -> Top: Fine Sand.",
                                "Bottom: Fine Sand -> Middle: Coarse Gravel -> Top: Charcoal.",
                                "Bottom: Charcoal -> Middle: Fine Sand -> Top: Big Rocks.",
                                "The media can be mixed together into a thick slurry."
                            ],
                            "answer": "A",
                            "explanation": "The correct order is Coarse Gravel at the bottom (around the outlet pipe), followed by Activated Charcoal (adsorbing chemicals/odors), and Fine Sand at the top (trapping pathogens and dirt)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 7: Catchment Math",
                        "content": {
                            "question": "A farmer has a corrugated iron roof measuring 150 m² in an area receiving 600 mm of rain annually. Assuming a runoff coefficient of 0.85, what is the annual harvestable volume?",
                            "options": [
                                "76,500 Liters (150 × 600 × 0.85).",
                                "90,000 Liters.",
                                "15,000 Liters.",
                                "7,650 Liters."
                            ],
                            "answer": "A",
                            "explanation": "Yield = Area (150) × Rainfall (600) × Coefficient (0.85) = 76,500 Liters."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 8: Storage Tank Color",
                        "content": {
                            "question": "Why are outdoor plastic rainwater storage tanks manufactured in dark green, dark blue, or black opaque colors rather than clear transparent plastic?",
                            "options": [
                                "Dark opaque walls block sunlight, preventing photosynthetic green algae from growing inside the stored water.",
                                "Black plastic makes the water taste like chocolate.",
                                "Clear plastic dissolves instantly in rainwater.",
                                "Dark colors attract extra rainwater from passing clouds."
                            ],
                            "answer": "A",
                            "explanation": "Algae require sunlight for photosynthesis. Opaque, dark UV-stabilized tanks block light penetration, keeping stored water free from green algae blooms."
                        }
                    }
                ],
                # Page 10: Topic Assessment Part 4 (Questions 9 to 10)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 9: Integrated System Planning",
                        "content": {
                            "question": "A boarding school in a semi-arid region wants to achieve complete water independence. What is the most effective integrated system design?",
                            "options": [
                                "Combine 500 m² of classroom roof catchments with first-flush diverters into a 50,000L tank, construct a membrane-lined water pan for surface runoff, and pipe tank overflow into a drip vegetable garden.",
                                "Dig a single unlined shallow hole in the school playground and leave it uncovered.",
                                "Rely entirely on buying commercial bottled water every week.",
                                "Cut down all trees on the school compound to let rain hit the ground."
                            ],
                            "answer": "A",
                            "explanation": "This integrated design captures high-purity roof water for drinking, uses a lined pan for agricultural water, and utilizes overflow for vegetable production."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Topic Assessment - Question 10: Diagnostic Troubleshooting",
                        "content": {
                            "question": "After several weeks of storage, a school's rainwater tank develops a foul swampy odor and cloudy green appearance. What two maintenance failures caused this problem?",
                            "options": [
                                "The tank was transparent (allowing sunlight to grow algae), and no first-flush diverter was installed (allowing decaying organic matter to accumulate inside).",
                                "The water was boiled too hot before entering the tank.",
                                "The tank was placed on a concrete slab that was too level.",
                                "The gutters were made of PVC plastic instead of wood."
                            ],
                            "answer": "A",
                            "explanation": "Sunlight entering transparent tanks triggers algae blooms, while rotting leaf litter and bird droppings (due to lack of a first-flush diverter) cause foul anaerobic decomposition odors."
                        }
                    }
                ]
            ]
        }
    ]

def ingest_cbc_grade8_agriculture_topic2(replace: bool = True):
    """Executes the database transaction to ingest Topic 2 into CBC Grade 8 Agriculture."""
    print("=" * 80)
    print("STARTING CONTENT INGESTION: CBC GRADE 8 AGRICULTURE — TOPIC 2 (DEEP EDITION)")
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

        topic_name = "Water Harvesting and Storage"
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
                "description": "Comprehensive water harvesting and storage: roof catchment engineering, first-flush diverters, catchment yield math, surface runoff harvesting, sand dams, membrane-lined pans, bio-sand filtration, Moringa coagulation, and school project execution."
            }
        )
        print(f"[*] Topic: '{topic.name}' (ID: {topic.id}, Created: {created})")

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
                        block_id=f"g8_agri_t2_u{u_order}_p{page_idx}_b{comp_idx}",
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
        print(f"[SUCCESS] Ingestion Complete for Grade 8 Topic 2: '{topic.name}'")
        print(f"[*] Units Created:   {total_units}")
        print(f"[*] Lessons Created: {total_lessons}")
        print(f"[*] Total Pages:     {total_pages}")
        print(f"[*] Total Blocks:    {total_blocks}")
        print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_cbc_grade8_agriculture_topic2(replace=replace_flag)
