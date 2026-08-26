"""
VLearn Grade 10 Biology — Topic 7: Plant Gaseous Exchange and Respiration
Production Ingestion Engine (4 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Plant Gaseous Exchange and Respiration (Topic Order: 7)

Structured into 4 Comprehensive Learning Units & 4 Published Lessons (39 Concept Cards):
  1. Gaseous Exchange Sites and Plant Adaptations (9 Pages)
  2. Opening and Closing of Stomata (10 Pages)
  3. Aerobic and Anaerobic Respiration in Plants (10 Pages)
  4. Fermentation Project and Economic Applications (10 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic7.py [--replace]
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
    """Removes bracket citations [133, 221], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [133], [133, 221], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    # Remove internal visual generation tags
    text = re.sub(r'\[VISUAL:\s*[^\]]+\]', '', text, flags=re.IGNORECASE)
    # Normalize unicode bullets into markdown list dashes
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    text = re.sub(r'[ \t]+', ' ', text)
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
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 7."""
    return [
        # =====================================================================
        # LESSON 7.1: Gaseous Exchange Sites and Plant Adaptations
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Gaseous Exchange Sites and Plant Adaptations",
            "unit_description": "Sites of gaseous exchange (stomata, lenticels, cuticle) and ecological adaptations in mesophytes, hydrophytes, and coastal mangrove pneumatophores.",
            "lesson_title": "Gaseous Exchange Sites and Plant Adaptations",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Gaseous Exchange Sites",
                        "content": {
                            "title": "Learning Focus: Plant Gaseous Exchange Sites",
                            "goals": [
                                "Identify the primary gaseous exchange sites in plants: stomata, lenticels, and cuticle.",
                                "Describe how terrestrial, aquatic (hydrophytic), and halophytic plants are adapted for gaseous exchange.",
                                "Compare the gaseous exchange mechanisms of terrestrial plants with specialized plants like coastal mangroves."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Plant Breathing Without Lungs",
                        "content": {
                            "title": "Plant Breathing Without Lungs",
                            "text": "While humans actively inhale air into lungs using muscular diaphragms, plants must exchange gases with their environment without any pump.\n\nEvery living plant cell requires Oxygen ($O_2$) for cellular respiration and releases Carbon (IV) oxide ($CO_2$). Simultaneously, during daylight hours, photosynthetic cells absorb $CO_2$ and release $O_2$. Each plant organ coordinates its own gaseous exchange through specialized microscopic structures."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Respiration & Gas Exchange Vocabulary",
                        "content": {
                            "term": "Essential Gaseous Exchange Terminology",
                            "definition": "Key concepts in plant respiratory anatomy and environmental adaptations.",
                            "key_points": [
                                "Gaseous Exchange: The physical process by which respiratory gases diffuse across a moist surface between an organism and its external environment.",
                                "Stoma (plural Stomata): A microscopic epidermal pore bounded by two guard cells, facilitating gas and water vapor exchange.",
                                "Lenticel: A raised, porous corky opening on woody stems and roots that allows the diffusion of oxygen and carbon dioxide.",
                                "Pneumatophore: Specialized 'breathing roots' produced by mangrove plants that grow vertically upward out of waterlogged saline mud to absorb oxygen from the air."
                            ]
                        }
                    }
                ],
                # Page 3: Primary Sites of Gaseous Exchange
                [
                    {
                        "type": "concept_explanation",
                        "title": "Primary Sites of Gaseous Exchange in Terrestrial Plants",
                        "content": {
                            "title": "Primary Sites of Gaseous Exchange in Terrestrial Plants",
                            "text": "1. **Stomata (Leaves & Herbaceous Green Stems)**:\n- The most active sites of gaseous exchange.\n- Open directly into intercellular air spaces in the spongy mesophyll, allowing gases to dissolve in the moist surface film before diffusing into cells.\n\n2. **Lenticels (Woody Stems & Mature Roots)**:\n- In woody stems, impermeable suberized cork blocks diffusion.\n- Lenticels consist of loosely arranged, unsuberized cork cells with large intercellular spaces, permitting oxygen to diffuse into deep wood tissues.\n\n3. **Cuticle (Epidermis)**:\n- A very minor amount of direct diffusion occurs across the thin waxy cuticle of young leaves."
                        }
                    }
                ],
                # Page 4: Gaseous Exchange Structures SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Plant Gaseous Exchange Structures & Habitat Adaptations",
                        "content": {
                            "description": "Three-panel comparative diagram: 1. Transverse section of dicot leaf showing stomatal gas diffusion pathways (CO2 in, O2 out) through intercellular spongy air spaces; 2. Floating aquatic water lily leaf with stomata restricted entirely to the upper epidermis and extensive aerenchyma air spaces; 3. Coastal mangrove tree in waterlogged mud showing upward-growing pneumatophore breathing roots covered with lenticels.",
                            "caption": "Structural and ecological adaptations for gaseous exchange across terrestrial, floating aquatic, and halophytic mangrove plants."
                        }
                    }
                ],
                # Page 5: Environmental Adaptations Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Ecological Adaptations for Gaseous Exchange in Diverse Habitats",
                        "content": {
                            "headers": ["Plant Habitat Group", "Representative Example", "Key Structural Adaptations", "Physiological Mechanism for Gaseous Exchange"],
                            "rows": [
                                ["Terrestrial Mesophytes", "Bean, Maize, Hibiscus", "Stomata concentrated on shaded lower leaf epidermis", "Balances rapid daytime $CO_2$ absorption with minimized sunlight-induced evaporative transpiration"],
                                ["Floating Hydrophytes", "Water Lily (Nymphaea)", "Stomata restricted entirely to upper epidermis; large internal **aerenchyma** chambers", "Exchanges gases directly with the atmosphere above water; aerenchyma provides buoyancy and internal oxygen storage"],
                                ["Submerged Hydrophytes", "Elodea, Ceratophyllum", "Completely lack stomata; ultra-thin delicate epidermal cell walls", "Dissolved $CO_2$ and $O_2$ diffuse directly across thin epidermal membranes from surrounding water"],
                                ["Halophytes (Mangroves)", "Avicennia, Rhizophora (Coast)", "Upright **pneumatophores** (breathing roots) covered in **lenticels** and internal aerenchyma", "Pneumatophores project above waterlogged, anaerobic tidal mud, absorbing atmospheric oxygen and channeling it down to submerged roots"]
                            ]
                        }
                    }
                ],
                # Page 6: Mangrove Pneumatophore Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Mangrove Aerial Pneumatophore Breathing Roots",
                        "content": {
                            "description": "High-clarity photograph of a coastal mangrove swamp at low tide showing hundreds of pencil-like vertical pneumatophore roots projecting upward out of anaerobic saline mud, displaying visible white lenticel breathing pores.",
                            "caption": "Mangrove pneumatophore breathing roots projecting out of oxygen-deficient tidal mud, absorbing atmospheric oxygen through lenticels."
                        }
                    }
                ],
                # Page 7: Common Misconception: 24-Hour Gaseous Exchange
                [
                    {
                        "type": "common_misconception",
                        "title": "Misconception: Plants Only Perform Gaseous Exchange in Sunlight",
                        "content": {
                            "misconception": "Plants only absorb and release gases during the daytime when they are actively photosynthesizing.",
                            "correction": "Plants perform gaseous exchange 24 hours a day! While photosynthesis occurs only in light, cellular respiration is a continuous, non-stop process occurring day and night. At night, plants continuously absorb oxygen and release carbon dioxide."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Gaseous Exchange and Environmental Adaptations",
                        "content": {
                            "description": "Comprehensive video guide covering stomatal gas diffusion, lenticel anatomy, hydrophyte aerenchyma, and mangrove pneumatophore breathing root adaptations."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mangrove Oil Spill Physiological Impact",
                        "content": {
                            "question": "An oil spill occurs in a mangrove forest along the Kenyan coast near Mombasa, coating the aerial roots (pneumatophores) of the trees with thick black oil. What is the immediate physiological consequence for these plants?",
                            "options": [
                                "Photosynthesis in the leaves stops immediately because water cannot be absorbed.",
                                "The underground root system suffocates because the oil blocks the lenticels on the pneumatophores, preventing oxygen from diffusing down to the roots for cellular respiration.",
                                "The plants begin absorbing nitrogen gas directly from the oil to compensate.",
                                "The leaves drop off because stomata are blocked by the rising tide."
                            ],
                            "correct_answer": "B",
                            "explanation": "Pneumatophores are specialized breathing roots that absorb oxygen from the air through lenticels. If oil coats these roots, the lenticels are physically blocked, halting oxygen diffusion to the submerged root cells. Without oxygen, the roots cannot perform aerobic respiration, leading to tissue suffocation and tree death."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Gaseous Exchange Sites",
                        "content": {
                            "title": "Lesson Summary: Plant Gaseous Exchange Sites",
                            "points": [
                                "Gaseous exchange occurs through stomata on leaves, lenticels on woody stems, and pneumatophores in waterlogged mud.",
                                "Mesophytes have lower stomata; floating hydrophytes have upper stomata and aerenchyma; submerged hydrophytes use direct diffusion.",
                                "Mangroves produce pneumatophores covered in lenticels to breathe in oxygen-poor tidal mud.",
                                "Gaseous exchange operates 24/7 because cellular respiration continues day and night."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7.2: Opening and Closing of Stomata
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Opening and Closing of Stomata",
            "unit_description": "Guard cell structural adaptations (uneven wall thickness, radial micellation) and movement theories (photosynthetic, starch-sugar, and modern potassium ion K+ accumulation theory).",
            "lesson_title": "Opening and Closing of Stomata",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Stomatal Regulation Mechanics",
                        "content": {
                            "title": "Learning Focus: Stomatal Regulation Mechanics",
                            "goals": [
                                "Explain how the structural adaptations of guard cells enable stomatal opening and closing.",
                                "Describe and compare the classical and modern scientific theories of stomatal movement.",
                                "Outline the biochemical role of proton pumps, potassium ions (K+), and abscisic acid (ABA) in regulating guard cell turgor."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Smart Microscopic Valves",
                        "content": {
                            "title": "The Smart Microscopic Valves",
                            "text": "If stomata remained permanently open, a plant would rapidly desiccate and die from excessive transpiration. If they remained permanently closed, the plant would starve from lack of Carbon (IV) oxide.\n\nTo balance these competing demands, plants evolved 'smart' microscopic valves: **guard cells**. Guard cells open and close dynamically in response to light, $CO_2$ levels, and water stress."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Stomatal Physiology Vocabulary",
                        "content": {
                            "term": "Essential Stomatal Regulatory Terms",
                            "definition": "Key concepts in guard cell biophysics and ionic signaling.",
                            "key_points": [
                                "Guard Cells: A pair of specialized crescent-shaped epidermal cells that regulate the aperture of a stomatal pore.",
                                "Turgor Pressure: The hydrostatic pressure exerted by fluid inside the cell vacuole against the surrounding cell wall.",
                                "Proton Pump: An ATP-powered active transport membrane protein that pumps hydrogen ions ($H^+$) out of guard cells.",
                                "Water Potential ($\\Psi$): The chemical tendency of water to move down an osmotic gradient from high potential (dilute) to low potential (concentrated)."
                            ]
                        }
                    }
                ],
                # Page 3: Structural Adaptations of Guard Cells
                [
                    {
                        "type": "step_process",
                        "title": "Three Key Structural Adaptations of Guard Cells",
                        "content": {
                            "title": "Three Key Structural Adaptations of Guard Cells",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Uneven Wall Thickness",
                                    "description": "The inner cell wall facing the stomatal pore is thick, rigid, and inelastic, while the outer wall is thin, flexible, and highly elastic."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Radial Micellation",
                                    "description": "Cellulose microfibrils are oriented radially around the cell, preventing lateral widening and forcing guard cells to expand lengthwise into crescent curves."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Presence of Chloroplasts",
                                    "description": "Unlike standard epidermal cells, guard cells contain chloroplasts to synthesize ATP and sugars locally to power active transport pumps."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Guard Cell Mechanics & K+ Theory SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Stomatal Guard Cell Mechanics & Potassium Ion (K+) Theory",
                        "content": {
                            "description": "Dual-panel comparative diagram. Left (Open Stoma - Day): Guard cells swollen and turgid, showing ATP proton pump exporting H+ ions, influx of K+ and Cl- ions, water entering by osmosis, thin outer wall ballooning outward, and thick inner wall bowing open. Right (Closed Stoma - Night / Drought): Guard cells flaccid and collapsed, showing ABA hormone triggering K+ efflux, water exiting by osmosis, and thick inner walls touching to seal the pore.",
                            "caption": "Biophysical and ionic mechanisms of stomatal opening and closing via potassium ion (K+) accumulation."
                        }
                    }
                ],
                # Page 5: Classical Theories of Stomatal Movement
                [
                    {
                        "type": "comparison_table",
                        "title": "Classical Theories of Stomatal Movement",
                        "content": {
                            "headers": ["Theory Name", "Daytime Trigger & Opening Mechanism", "Nighttime Trigger & Closing Mechanism", "Scientific Limitation"],
                            "rows": [
                                ["Photosynthetic Theory (Old)", "Guard cell photosynthesis produces soluble glucose $\\rightarrow$ lowers water potential $\\rightarrow$ water enters $\\rightarrow$ turgid open pore", "Photosynthesis halts $\\rightarrow$ glucose converted to insoluble starch $\\rightarrow$ water exits $\\rightarrow$ flaccid closed pore", "Glucose synthesis in guard cells is too slow to account for rapid stomatal opening at dawn"],
                                ["Starch-Sugar Interconversion Theory", "Photosynthesis consumes $CO_2 \\rightarrow$ pH rises (alkaline) $\\rightarrow$ activates phosphorylase enzyme converting starch to sugar $\\rightarrow$ osmosis $\\rightarrow$ open pore", "Respiration accumulates $CO_2 \\rightarrow$ pH drops (acidic) $\\rightarrow$ converts sugar back to starch $\\rightarrow$ water leaves $\\rightarrow$ closed pore", "Fails to explain rapid stomatal responses to blue light wavelengths independent of $CO_2$ levels"]
                            ]
                        }
                    }
                ],
                # Page 6: Modern Potassium Ion (K+) Accumulation Theory
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Modern Potassium Ion (K+) Accumulation Theory",
                        "content": {
                            "title": "The Modern Potassium Ion (K+) Accumulation Theory",
                            "text": "The modern, scientifically validated explanation for stomatal movement operates via active ion flux:\n\n1. **Opening Mechanism (In Sunlight)**:\n- Blue light triggers ATP-powered **proton pumps** on the guard cell membrane to pump $H^+$ ions **out** into adjacent cells.\n- Potassium ions ($K^+$) and chloride ions ($Cl^-$) are actively pumped **into** the guard cells.\n- This massive ionic influx sharply lowers the guard cells' water potential.\n- Water rushes in by **osmosis**; the thin elastic outer walls stretch outward, pulling the thick inelastic inner walls apart, **opening the stomatal pore**.\n\n2. **Closing Mechanism (At Night or Under Drought Stress)**:\n- In darkness or drought, the plant produces **Abscisic Acid (ABA)**.\n- ABA triggers rapid efflux of $K^+$ and $Cl^-$ ions out of guard cells.\n- Water potential rises; water exits by osmosis; guard cells become **flaccid**, closing the pore."
                        }
                    }
                ],
                # Page 7: Micrograph of Open/Closed Stomata
                [
                    {
                        "type": "suggested_image",
                        "title": "High-Magnification Micrograph of Open and Closed Stomatal Guard Cells",
                        "content": {
                            "description": "Scanning Electron Micrograph (SEM) showing a wide open stomatal pore with turgid, curved crescent guard cells alongside a fully closed stoma with collapsed, flattened flaccid guard cells.",
                            "caption": "Scanning electron micrograph (SEM) showing turgid open stomata versus flaccid closed stomata on a leaf epidermis."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Mechanisms of Stomatal Opening and Closing (K+ Ion Theory)",
                        "content": {
                            "description": "Video animation detailing the biophysics of uneven guard cell walls, proton pump ATP export, K+ ion influx, osmotic swelling, and ABA-mediated closure."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Guard Cell ATP Inhibition",
                        "content": {
                            "question": "A plant physiologist treats a leaf with a metabolic inhibitor that completely halts the production of ATP in guard cells. What will happen to the stomata when this leaf is moved from the dark into bright sunlight?",
                            "options": [
                                "The stomata will open wider because glucose will accumulate faster.",
                                "The stomata will remain closed because active transport of potassium ions (K+) requires ATP to pump protons (H+) out of the guard cells.",
                                "The stomata will open immediately due to the passive diffusion of starch.",
                                "The stomata will open and close rapidly at random intervals."
                            ],
                            "correct_answer": "B",
                            "explanation": "According to the Potassium Ion Accumulation Theory, stomatal opening requires the active pumping of H+ ions out of the guard cell via ATP-powered proton pumps. If ATP production is blocked, K+ ions cannot be actively accumulated, water potential will not drop, and water will not enter by osmosis. Thus, the stomata remain closed."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Stomatal Regulation",
                        "content": {
                            "title": "Lesson Summary: Stomatal Regulation",
                            "points": [
                                "Guard cells have thick inelastic inner walls and thin elastic outer walls that bow outward when turgid.",
                                "Sunlight activates ATP proton pumps to export $H^+$ and import $K^+$, driving osmotic water influx to open the pore.",
                                "Darkness and drought hormone ABA cause $K^+$ efflux, osmotic water loss, flaccidity, and stomatal closure.",
                                "Stomatal opening enables photosynthetic $CO_2$ uptake while balancing transpirational water loss."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7.3: Aerobic and Anaerobic Respiration in Plants
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Aerobic and Anaerobic Respiration in Plants",
            "unit_description": "Biochemical pathways of aerobic respiration (38 ATP) and anaerobic alcoholic fermentation (2 ATP), chemical equations, and the vacuum flask heat experiment.",
            "lesson_title": "Aerobic and Anaerobic Respiration in Plants",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Cellular Respiration",
                        "content": {
                            "title": "Learning Focus: Plant Cellular Respiration",
                            "goals": [
                                "Define and compare aerobic and anaerobic respiration in plant tissues.",
                                "State the word and balanced chemical equations for aerobic respiration and alcoholic fermentation.",
                                "Describe and interpret the vacuum flask experiment investigating heat release during seed respiration."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Extracting Energy from Food",
                        "content": {
                            "title": "Extracting Energy from Food",
                            "text": "How do plants obtain energy to grow roots, synthesize proteins, and pump mineral ions? They do so through **cellular respiration**.\n\nJust like animals, plants break down glucose to produce ATP, the universal energy currency of life. While plants prefer aerobic respiration with oxygen, they can switch to emergency anaerobic pathways in waterlogged soils."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Cellular Respiration Vocabulary",
                        "content": {
                            "term": "Essential Bioenergetics Terms",
                            "definition": "Key concepts in plant catabolic metabolism and energy release.",
                            "key_points": [
                                "Cellular Respiration: The biochemical oxidation of organic food molecules (glucose) to synthesize ATP energy.",
                                "Aerobic Respiration: Complete breakdown of glucose in the presence of oxygen, yielding $CO_2$, $H_2O$, and 38 ATP.",
                                "Anaerobic Respiration (Alcoholic Fermentation): Incomplete breakdown of glucose in the absence of oxygen, yielding ethanol, $CO_2$, and 2 ATP.",
                                "Mitochondrion: The double-membraned organelle where aerobic respiration stages (Krebs cycle and oxidative phosphorylation) occur."
                            ]
                        }
                    }
                ],
                # Page 3: Aerobic vs. Anaerobic Pathways & Equations
                [
                    {
                        "type": "concept_explanation",
                        "title": "Biochemical Equations of Plant Respiration",
                        "content": {
                            "title": "Biochemical Equations of Plant Respiration",
                            "text": "1. **Aerobic Respiration (Oxygen Present)**:\n$$\\text{Glucose} + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 38\\text{ ATP (Energy)}$$\n- Highly efficient: complete oxidation of glucose yielding 38 ATP molecules per glucose molecule.\n\n2. **Anaerobic Respiration / Alcoholic Fermentation (Oxygen Absent)**:\n$$\\text{Glucose} \\rightarrow 2\\text{C}_2\\text{H}_5\\text{OH (Ethanol)} + 2\\text{CO}_2 + 2\\text{ ATP (Energy)}$$\n- Inefficient: incomplete breakdown yielding only 2 ATP molecules per glucose, producing toxic ethanol that accumulates in waterlogged root tissues."
                        }
                    }
                ],
                # Page 4: Respiration Pathways & Thermos Experiment SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Plant Respiration Pathways & Thermos Flask Experiment",
                        "content": {
                            "description": "Dual-panel diagram. Left panel: Biochemical pathway comparison showing Aerobic Respiration (Glycolysis + Mitochondria -> 38 ATP + CO2 + H2O) vs Anaerobic Alcoholic Fermentation (Cytoplasm -> 2 ATP + Ethanol + CO2). Right panel: Vacuum flask experiment setup showing Flask A with germinating seeds and thermometer reading 30°C vs Flask B with boiled seeds soaked in disinfectant and thermometer reading constant room temperature (20°C).",
                            "caption": "Biochemical equations of aerobic/anaerobic respiration alongside the classical vacuum flask thermogenesis experiment."
                        }
                    }
                ],
                # Page 5: Comparison Table: Aerobic vs. Anaerobic
                [
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Aerobic vs. Anaerobic Respiration in Plants",
                        "content": {
                            "headers": ["Feature", "Aerobic Respiration", "Anaerobic Respiration (Alcoholic Fermentation)"],
                            "rows": [
                                ["Oxygen Requirement", "Strictly required ($O_2$ is final electron acceptor)", "Occurs in complete absence of oxygen ($O_2$)"],
                                ["Subcellular Site", "Glycolysis in cytoplasm, Krebs cycle in mitochondria", "Occurs entirely in the cytoplasm"],
                                ["Degree of Glucose Breakdown", "Complete oxidation into simple inorganic molecules", "Incomplete/partial breakdown of glucose"],
                                ["Energy Yield per Glucose", "High energy yield: **38 ATP** molecules", "Very low energy yield: **2 ATP** molecules"],
                                ["End Products Formed", "Carbon (IV) oxide ($CO_2$) and Water ($H_2O$)", "Ethanol ($C_2H_5OH$) and Carbon (IV) oxide ($CO_2$)"],
                                ["Toxicity to Plant Tissues", "End-products are completely harmless", "Accumulated ethanol is toxic and lethal to plant cells"]
                            ]
                        }
                    }
                ],
                # Page 6: Practical Investigation: Heat in Respiration
                [
                    {
                        "type": "step_process",
                        "title": "Practical Protocol: Measuring Heat Released in Respiration",
                        "content": {
                            "title": "Practical Protocol: Measuring Heat Released in Respiration",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Flask A (Germinating Seeds)",
                                    "description": "Place actively germinating bean seeds in vacuum Flask A. Insert a thermometer packed in cotton wool."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Flask B (Boiled & Disinfected Control)",
                                    "description": "Boil bean seeds to kill them. Soak in 10% formalin disinfectant to kill decomposing bacteria, then place in Flask B."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Temperature Monitoring",
                                    "description": "Record daily temperatures for 4 days. Observation: Flask A temperature rises (from 20°C to 28–30°C); Flask B remains steady at 20°C."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Biological Conclusion",
                                    "description": "Active cellular respiration in germinating seeds is an exothermic metabolic process that releases energy as heat."
                                }
                            ]
                        }
                    }
                ],
                # Page 7: Germinating Seeds Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Germinating Bean Seeds Respiration and Thermogenesis",
                        "content": {
                            "description": "High-clarity photograph of germinating bean seeds showing emerging radicles and plumules inside an experimental apparatus measuring respiratory oxygen consumption and metabolic heat release.",
                            "caption": "Actively germinating bean seeds undergoing rapid cellular respiration to power rapid cell division and seedling emergence."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Cellular Respiration — Aerobic vs. Anaerobic",
                        "content": {
                            "description": "Educational presentation comparing aerobic mitochondrial respiration with cytoplasmic fermentation, and demonstrating the vacuum flask seed thermogenesis experiment."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Disinfectant in Control Flask",
                        "content": {
                            "question": "Why is it absolutely critical to soak the boiled seeds in a disinfectant (like formalin) before placing them in the control flask (Flask B) of the vacuum flask respiration experiment?",
                            "options": [
                                "To make the seeds absorb water faster.",
                                "To prevent bacterial respiration, which would generate its own heat and invalidate the control.",
                                "To help the dead seeds start photosynthesizing.",
                                "To turn the seed starch into glucose."
                            ],
                            "correct_answer": "B",
                            "explanation": "Dead seeds are readily colonized by bacteria and fungi. As these decomposers feed on dead tissue, they respire and generate heat, causing a temperature rise in the control flask. Soaking the boiled seeds in disinfectant sterilizes them, ensuring that any heat measured is due solely to the living seeds in Flask A."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Respiration",
                        "content": {
                            "title": "Lesson Summary: Plant Respiration",
                            "points": [
                                "Aerobic respiration breaks down glucose completely with $O_2$, yielding 38 ATP, $CO_2$, and $H_2O$.",
                                "Anaerobic fermentation occurs without $O_2$, producing 2 ATP, $CO_2$, and toxic ethanol.",
                                "Vacuum flask experiments prove that active cellular respiration releases measurable heat energy.",
                                "Disinfectant in control flasks prevents microbial heat generation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 7.4: Fermentation Project and Economic Applications
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Fermentation Project and Economic Applications",
            "unit_description": "Yeast anaerobic fermentation lab assay, industrial applications (brewing, baking), domestic 20-liter biogas digester construction, and financial payback budgeting.",
            "lesson_title": "Fermentation Project and Economic Applications",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Biogas & Fermentation Biotechnology",
                        "content": {
                            "title": "Learning Focus: Biogas & Fermentation Biotechnology",
                            "goals": [
                                "Describe a laboratory assay demonstrating anaerobic alcoholic fermentation in yeast using limewater.",
                                "Explain industrial and agricultural applications of anaerobic respiration (baking, brewing, biogas).",
                                "Plan, construct, and budget a domestic 20-liter plastic bottle biogas digester for rural energy independence."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Power of Anaerobic Biotechnology",
                        "content": {
                            "title": "The Power of Anaerobic Biotechnology",
                            "text": "Anaerobic respiration is not just an emergency pathway for waterlogged roots—it is one of the most economically valuable biochemical processes in human history.\n\nHumans harness anaerobic fermentation to bake bread, brew beverages, and produce fermented foods. Today, we also use anaerobic methanogenic bacteria to convert agricultural animal waste into **clean, renewable biogas** for domestic cooking."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Biotechnology & Biogas Vocabulary",
                        "content": {
                            "term": "Essential Biotechnology Terms",
                            "definition": "Key concepts in anaerobic digestion and renewable bio-energy.",
                            "key_points": [
                                "Biogas: A renewable combustible gas mixture (primarily methane $CH_4$ and carbon dioxide $CO_2$) produced by anaerobic decomposition of organic waste.",
                                "Anaerobic Digestion: Biological breakdown of organic biodegradable material by specialized bacteria in the complete absence of oxygen.",
                                "Slurry: A semi-liquid mixture of organic waste (cow dung, food scraps) and water fed into a biogas digester.",
                                "Limewater: A clear solution of Calcium Hydroxide ($Ca(OH)_2$) that turns cloudy white/milky in the presence of $CO_2$ gas."
                            ]
                        }
                    }
                ],
                # Page 3: Lab Demonstration: Yeast Fermentation
                [
                    {
                        "type": "step_process",
                        "title": "Laboratory Protocol: Yeast Anaerobic Fermentation Assay",
                        "content": {
                            "title": "Laboratory Protocol: Yeast Anaerobic Fermentation Assay",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "De-Oxygenate Glucose Solution",
                                    "description": "Boil glucose solution to expel dissolved oxygen, then cool to 35°C to protect yeast enzymes."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Add Yeast & Paraffin Oil Barrier",
                                    "description": "Mix active yeast powder and pour a thin layer of paraffin oil on top to block atmospheric oxygen entry, ensuring strictly anaerobic conditions."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Gas Delivery to Limewater",
                                    "description": "Fit a delivery tube leading from the reaction tube into a test tube of clear limewater ($Ca(OH)_2$)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Observations & Results",
                                    "description": "Gas bubbles turn limewater cloudy white (confirming $CO_2$ evolution), ethanol aroma is detected, and temperature rises slightly."
                                }
                            ]
                        }
                    }
                ],
                # Page 4: Yeast Assay & 20L Biogas Digester SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Yeast Anaerobic Fermentation Apparatus & Domestic 20L Biogas Digester",
                        "content": {
                            "description": "Dual-panel diagram. Left panel: Laboratory yeast fermentation setup showing test tube with glucose + yeast, paraffin oil oxygen barrier layer, delivery tube, and test tube of cloudy limewater precipitate. Right panel: Hands-on domestic 20-liter biogas digester schematic showing 20L bottle filled with 1:1 cow dung slurry, 5L gas headspace, airtight silicone-sealed cap, PVC tubing, brass control valve, and expanding inflatable gas storage bag producing combustible methane.",
                            "caption": "Laboratory yeast fermentation apparatus alongside a domestic 20-liter low-cost biogas digester engineering design."
                        }
                    }
                ],
                # Page 5: Hands-On Biogas Digester Construction
                [
                    {
                        "type": "step_process",
                        "title": "Engineering Protocol: Constructing a 20-Liter Biogas Digester",
                        "content": {
                            "title": "Engineering Protocol: Constructing a 20-Liter Biogas Digester",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Cap Drilling & Tubing Insertion",
                                    "description": "Drill a hole matching PVC tube diameter in the 20L container cap. Insert tube 2 cm into headspace."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Gas-Tight Silicone Sealing",
                                    "description": "Apply silicone sealant generously around cap-tube joints. Airtight sealing is mandatory to prevent methane leaks and keep out oxygen."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Valve & Gas Storage Attachment",
                                    "description": "Connect the outer tube end to a brass control valve and attach to an inflatable gas storage bag."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Slurry Loading & Warm Incubation",
                                    "description": "Mix 5 kg fresh cow dung with 5 L water (1:1 ratio). Pour into bottle leaving 5 L headspace. Seal tightly and incubate in a warm spot (30–37°C)."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Project Budgeting & Financial Literacy
                [
                    {
                        "type": "comparison_table",
                        "title": "Domestic 20L Biogas Digester Budget & Payback Analysis (KES)",
                        "content": {
                            "headers": ["Item / Material", "Estimated Cost (KES)", "Economic Contribution & Savings"],
                            "rows": [
                                ["20-Liter Plastic Container (Recycled)", "150 KES", "Airtight anaerobic digester fermentation tank"],
                                ["Flexible PVC Tubing (2 meters)", "100 KES", "Methane gas delivery conduit"],
                                ["Brass Gas Control Valve", "350 KES", "Gas flow control and leak prevention"],
                                ["Silicone Sealant (1 Tube)", "450 KES", "Guarantees 100% gas-tight anaerobic seal"],
                                ["Feedstock (Cow Dung / Scraps)", "0 KES", "Free, locally sourced zero-cost organic farm waste"],
                                ["Improvised Gas Burner Head", "500 KES", "Safe, clean combustion for domestic cooking"],
                                ["**TOTAL CAPITAL STARTUP COST**", "**1,550 KES**", "**Payback Period: ~1.03 Months against 1,500 KES/month charcoal costs!**"]
                            ]
                        }
                    }
                ],
                # Page 7: Domestic Biogas Plant Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Domestic Rural Biogas Digester Plant and Clean Methane Flame",
                        "content": {
                            "description": "High-resolution photograph of a rural smallholder farm biogas installation showing the digester tank connected to a kitchen stove burning a smokeless, clean blue methane flame.",
                            "caption": "Domestic biogas digester utilizing animal dung to produce clean, smokeless methane gas for household cooking."
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: How to Build a DIY Domestic Biogas Digester",
                        "content": {
                            "description": "Step-by-step video guide demonstrating the construction, slurry loading, airtight sealing, and gas testing of a low-cost plastic bottle biogas digester."
                        }
                    }
                ],
                # Page 9: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Biogas Digester Airtight Sealing",
                        "content": {
                            "question": "Why is it strictly crucial to keep the biogas digester bottle completely sealed, with absolutely no air leaks?",
                            "options": [
                                "To prevent oxygen from entering, which would inhibit anaerobic methanogenic bacteria, and to prevent flammable methane gas from escaping.",
                                "To keep the temperature inside the bottle below 10°C.",
                                "To allow aerobic respiration to occur faster.",
                                "To turn the cow dung slurry into glucose starch."
                            ],
                            "correct_answer": "A",
                            "explanation": "Biogas production depends strictly on obligate anaerobic methanogenic bacteria. If air leaks in, oxygen inhibits and kills these bacteria, halting methane production. Furthermore, methane is highly flammable, so leaks create fire hazards and cause valuable fuel to escape."
                        }
                    }
                ],
                # Page 10: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Fermentation & Biogas",
                        "content": {
                            "title": "Lesson Summary: Fermentation & Biogas",
                            "points": [
                                "Yeast fermentation decomposes glucose into ethanol and $CO_2$ under an anaerobic paraffin oil seal.",
                                "Anaerobic digestion transforms organic waste into combustible methane biogas and nutrient-rich fertilizer.",
                                "A domestic 20L biogas digester costs ~1,550 KES and pays for itself within one month by replacing charcoal.",
                                "Airtight sealing is mandatory to protect anaerobic bacteria and prevent methane loss."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic7(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 7."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 7: Plant Gaseous Exchange and Respiration (CBC Curriculum ID: 5)")
    print("=" * 80)

    # 1. Resolve Curriculum
    curriculum = Curriculum.objects.filter(name="CBC").first() or Curriculum.objects.filter(id=5).first()
    if not curriculum:
        print("[!] Fatal: Curriculum 'CBC' (ID: 5) not found in database!")
        return

    print(f"[*] Curriculum: {curriculum.name} (ID: {curriculum.id})")

    # 2. Resolve Grade
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first() or Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        print("[!] Fatal: Grade 'Grade 10' under CBC not found in database!")
        return

    print(f"[*] Grade: {grade.name} (ID: {grade.id}, Level: {grade.level})")

    # 3. Resolve Subject under Grade 10 CBC (Strict Scope Isolation)
    subject, created = Subject.objects.get_or_create(
        grade=grade,
        name="Biology",
        defaults={"description": "Grade 10 Biology Curriculum under CBC senior secondary science pathway."}
    )
    print(f"[*] Subject: {subject.name} under {grade.name} (ID: {subject.id})")

    # 4. Resolve Topic 7
    topic_name = "Plant Gaseous Exchange and Respiration"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=7,
            description="Comprehensive syllabus on gaseous exchange sites and adaptations (stomata, lenticels, pneumatophores), stomatal regulation (K+ ion theory), aerobic vs anaerobic respiration, and domestic biogas biotechnology projects."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic7_curriculum()
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

            learning_unit.name = unit_name
            learning_unit.description = unit_desc
            learning_unit.save()

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
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (Lesson ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Concept Card {page_idx}")
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
            print(f"      [OK] Ingested {lesson_page_count} Concept Cards for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Grade 10 Biology Topic 7 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic7(replace=replace_flag)
