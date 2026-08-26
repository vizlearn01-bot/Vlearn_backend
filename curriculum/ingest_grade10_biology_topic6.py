"""
VLearn Grade 10 Biology — Topic 6: Plant Transport
Production Ingestion Engine (5 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Plant Transport (Topic Order: 6)

Structured into 5 Comprehensive Learning Units & 5 Published Lessons (45 Concept Cards):
  1. Transport Systems in Plants and External Adaptations (9 Pages)
  2. Monocotyledonous and Dicotyledonous Vascular Arrangement (9 Pages)
  3. Uptake and Upward Movement of Water and Mineral Salts (9 Pages)
  4. Transpiration and Factors Affecting Its Rate (9 Pages)
  5. Translocation of Manufactured Food (9 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic6.py [--replace]
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
    """Removes bracket citations [220, 244], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [220], [220, 244], [image_1]
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

def build_topic6_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 6."""
    return [
        # =====================================================================
        # LESSON 6.1: Transport Systems in Plants and External Adaptations
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Transport Systems in Plants and External Adaptations",
            "unit_description": "Necessity of transport systems in multicellular plants (SA:V ratio, diffusion limitations) and external anatomical adaptations of roots, stems, and root hair cells.",
            "lesson_title": "Transport Systems in Plants and External Adaptations",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Transport & Absorption",
                        "content": {
                            "title": "Learning Focus: Plant Transport & Absorption",
                            "goals": [
                                "Explain why large multicellular plants require specialized vascular transport systems while simple plants do not.",
                                "Identify the external transport organs of a plant: roots, stems, and leaves.",
                                "Relate the microscopic structural adaptations of root hair cells to their vital role in water and mineral absorption."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 100-Meter Eucalyptus Challenge",
                        "content": {
                            "title": "The 100-Meter Eucalyptus Challenge",
                            "text": "Think of a massive, 100-meter-tall eucalyptus tree. It has leaves baking in the blazing sun at the canopy, and roots buried deep in the dark, damp soil below.\n\nHow does water from the soil travel all the way up against gravity to reach those high leaves without any mechanical pump like a heart? Large multicellular plants cannot rely on simple diffusion because their cells are too far apart. They require an elegant, vascular highway system."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Transport Vocabulary",
                        "content": {
                            "term": "Essential Vascular Transport Terms",
                            "definition": "Key concepts in plant bio-transport and root absorption physiology.",
                            "key_points": [
                                "Diffusion: The passive movement of particles down a concentration gradient from high to low concentration.",
                                "Vascular Bundle: A specialized longitudinal strand containing xylem (water transport) and phloem (sugar translocation) tissues.",
                                "Piliferous Layer: The specialized epidermal layer of young roots that produces root hair extensions.",
                                "Root Hair: A microscopic, single-celled, elongated extension of an epidermal cell that absorbs water and mineral salts from the soil."
                            ]
                        }
                    }
                ],
                # Page 3: Why Plants Need Transport Systems
                [
                    {
                        "type": "concept_explanation",
                        "title": "Why Multicellular Plants Require Transport Systems",
                        "content": {
                            "title": "Why Multicellular Plants Require Transport Systems",
                            "text": "1. **Surface Area to Volume Ratio ($SA:V$)**:\n- Tiny plants (algae, mosses) have a high $SA:V$ ratio and thin bodies in direct contact with water. Simple diffusion across membranes is fast enough to distribute nutrients.\n- Large plants (trees, maize, sugarcane) have a very small $SA:V$ ratio and complex, thick tissues. Most interior cells are far from the surface.\n\n2. **Long Transport Distances**:\n- Diffusion is effective only over distances of a few micrometers. It would take decades for water absorbed in roots to reach tree leaves by diffusion alone! Specialized **xylem** and **phloem** bridge this gap."
                        }
                    }
                ],
                # Page 4: Root Hair Cell SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Root Hair Cell Soil Interface & Absorption Adaptations",
                        "content": {
                            "description": "High-detail biological diagram of a single root hair cell penetrating soil particles. Labels: Soil particles with thin capillary water film, very thin cell wall, selectively permeable cell membrane, cytoplasm, large central vacuole packed with concentrated cell sap (high osmotic pressure / low water potential), and nucleus.",
                            "caption": "Microscopic adaptations of the root hair cell maximizing water absorption via osmosis and mineral uptake via active transport."
                        }
                    }
                ],
                # Page 5: Root Hair Adaptations
                [
                    {
                        "type": "step_process",
                        "title": "Four Core Adaptations of Root Hair Cells",
                        "content": {
                            "title": "Four Core Adaptations of Root Hair Cells",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Elongated, Narrow Extension",
                                    "description": "Slender tubular outgrowth that penetrates tight micro-crevices between soil particles to access thin capillary water films."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Enormous Surface Area",
                                    "description": "Millions of root hairs collectively increase the root's absorption surface area by up to 1,000-fold."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Ultra-Thin Cell Wall",
                                    "description": "Permeable, single-cell-thick wall minimizing diffusion distance for incoming water and mineral ions."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Dense Vacuolar Solutes",
                                    "description": "Concentrated cell sap maintains high osmotic pressure (lower water potential than soil water), ensuring continuous water influx via osmosis."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Root Hair Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Micrograph of Root Hair Epidermis Absorbing Soil Water",
                        "content": {
                            "description": "Light microscope photograph showing a young plant root tip with hundreds of delicate, elongated root hairs radiating outwards from the piliferous epidermal zone.",
                            "caption": "Photomicrograph of root hair zone showing extensive epidermal hair outgrowths that expand the absorptive root surface area."
                        }
                    }
                ],
                # Page 7: Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Transport in Simple Bryophytes vs. Higher Vascular Plants",
                        "content": {
                            "headers": ["Characteristic", "Simple Bryophytes (Mosses, Liverworts)", "Higher Tracheophytes (Trees, Maize, Beans)"],
                            "rows": [
                                ["Body Size & $SA:V$ Ratio", "Microscopic or very small; massive $SA:V$ ratio", "Large multicellular bodies; very small $SA:V$ ratio"],
                                ["Primary Transport Mechanism", "Direct diffusion and cytoplasmic streaming across cells", "Specialized bulk-flow vascular bundles (Xylem and Phloem)"],
                                ["Absorption Mechanism", "Rhizoids and direct epidermal surface diffusion", "Extensive root networks with millions of solute-dense root hairs"],
                                ["Environmental Dependency", "Restricted to permanently damp, shaded micro-habitats", "Can grow tall and thrive in diverse terrestrial environments"]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Transport Systems & Root Hair Absorption",
                        "content": {
                            "description": "Comprehensive video guide covering surface area to volume limitations, external plant anatomy, root hair soil interactions, and cellular water absorption."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Surface Area to Volume Limitation",
                        "content": {
                            "question": "Mosses can survive without any xylem or phloem tissues, whereas sugarcane plants will quickly die without them. Which biological principle explains why sugarcane requires these specialized vascular tissues?",
                            "options": [
                                "Mosses perform a different type of photosynthesis that does not require water.",
                                "Sugarcane has a small surface area to volume ratio and cells located far from water sources, making simple diffusion too slow to sustain life.",
                                "Mosses have root hairs that absorb water much faster than sugarcane.",
                                "Sugarcane cells are completely impermeable to diffusion."
                            ],
                            "correct_answer": "B",
                            "explanation": "Mosses are small plants with a large SA:V ratio where diffusion distances are negligible. Sugarcane is a large multicellular plant with a small SA:V ratio; because most of its photosynthetic and metabolic cells are located far from root absorption sites, it must rely on specialized vascular transport systems."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Transport Systems",
                        "content": {
                            "title": "Lesson Summary: Plant Transport Systems",
                            "points": [
                                "Large plants require vascular systems because diffusion is too slow over long distances due to low $SA:V$ ratios.",
                                "Roots absorb water/minerals, stems provide vertical conduits, and leaves coordinate photosynthesis/transpiration.",
                                "Root hair cells are specialized with elongated shapes, thin walls, massive surface area, and concentrated vacuolar sap.",
                                "Water enters root hairs passively by osmosis down a water potential gradient."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6.2: Monocotyledonous and Dicotyledonous Vascular Arrangement
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Monocotyledonous and Dicotyledonous Vascular Arrangement",
            "unit_description": "Comparative anatomical organization of xylem, phloem, cambium, cortex, and pith in monocotyledon and dicotyledon stems and roots.",
            "lesson_title": "Monocotyledonous and Dicotyledonous Vascular Arrangement",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Vascular Tissue Organization",
                        "content": {
                            "title": "Learning Focus: Vascular Tissue Organization",
                            "goals": [
                                "Compare the vascular tissue arrangements of monocotyledonous and dicotyledonous stems.",
                                "Compare the internal anatomical organization of monocotyledonous and dicotyledonous roots.",
                                "Identify and label xylem, phloem, vascular cambium, cortex, pith, and Casparian strips on plant cross-sections."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Vascular Fingerprint of Plants",
                        "content": {
                            "title": "The Vascular Fingerprint of Plants",
                            "text": "If you slice open a plant's stem or root and examine it under a microscope, you will find organized patterns of transport tubes.\n\nThese arrangements act as a taxonomic fingerprint. By reading these patterns, you can instantly distinguish a **monocot** (maize, grass) from a **dicot** (beans, sunflower, coffee)."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Anatomy Vocabulary",
                        "content": {
                            "term": "Essential Anatomical Terms",
                            "definition": "Key concepts in monocot and dicot internal tissue organization.",
                            "key_points": [
                                "Monocotyledon: A flowering plant with a single cotyledon, parallel leaf venation, and scattered stem vascular bundles.",
                                "Dicotyledon: A flowering plant with two cotyledons, net-like venation, and ring-arranged stem vascular bundles.",
                                "Vascular Cambium: Meristematic tissue between xylem and phloem in dicots responsible for secondary growth (thickening).",
                                "Cortex: Ground tissue parenchyma between epidermis and vascular cylinder in stems and roots.",
                                "Casparian Strip: A waxy, waterproof suberin band in root endodermal cell walls regulating water entry into xylem."
                            ]
                        }
                    }
                ],
                # Page 3: Stem Vascular Arrangement
                [
                    {
                        "type": "concept_explanation",
                        "title": "Stem Vascular Organization: Monocots vs. Dicots",
                        "content": {
                            "title": "Stem Vascular Organization: Monocots vs. Dicots",
                            "text": "1. **Monocotyledon Stem (e.g. Maize)**:\n- Vascular bundles are **scattered** throughout ground tissue.\n- No distinct division into cortex or central pith.\n- Lacks vascular cambium $\\rightarrow$ cannot undergo secondary thickening (no true woody bark).\n\n2. **Dicotyledon Stem (e.g. Bean, Sunflower)**:\n- Vascular bundles arranged in a neat, concentric **ring**.\n- Distinct outer **cortex** and central **pith** (storage parenchyma).\n- Possesses **vascular cambium** sandwiched between xylem and phloem, producing new xylem inward and phloem outward for woody growth."
                        }
                    }
                ],
                # Page 4: Quad-Panel Vascular SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Plant Vascular Cross-Sections: Monocots vs Dicots",
                        "content": {
                            "description": "Quad-split comparative diagram: 1. Monocot Stem (scattered bundles resembling faces); 2. Dicot Stem (neat ring of bundles with vascular cambium dividing lines, cortex, and central pith); 3. Monocot Root (ring of xylem and phloem bundles around a central pith); 4. Dicot Root (central X-shaped/star xylem with phloem in corners, surrounded by endodermis).",
                            "caption": "Anatomical comparison of vascular bundle arrangements across monocot and dicot stems and roots."
                        }
                    }
                ],
                # Page 5: Root Vascular Arrangement & Endodermis
                [
                    {
                        "type": "concept_explanation",
                        "title": "Root Vascular Organization & The Casparian Checkpoint",
                        "content": {
                            "title": "Root Vascular Organization & The Casparian Checkpoint",
                            "text": "1. **Monocot Root**:\n- Xylem and phloem bundles are arranged in an alternating **ring** around a central storage **pith**.\n\n2. **Dicot Root**:\n- No central pith. Xylem forms a solid **central 'X-shape' or star** in the core.\n- Phloem groups are located in the angles/corners between the arms of the xylem star.\n\n3. **Endodermis & Casparian Strip**:\n- A single layer of cells (endodermis) surrounds the vascular cylinder.\n- The **Casparian strip** (waxy suberin) blocks passive apoplastic water flow along cell walls, forcing water across selectively permeable cell membranes into the xylem."
                        }
                    }
                ],
                # Page 6: Dicot Stem Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Light Micrograph of Dicot Stem Vascular Ring at 100x",
                        "content": {
                            "description": "Stained cross-section of a Helianthus dicot stem showing outer epidermis, cortex layer, distinct concentric ring of vascular bundles with visible cambium lines, and central parenchyma pith.",
                            "caption": "Light micrograph of a dicot stem cross-section showing orderly ring arrangement of vascular bundles and distinct vascular cambium."
                        }
                    }
                ],
                # Page 7: Comparison Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Anatomical Comparison: Monocots vs. Dicots",
                        "content": {
                            "headers": ["Plant Organ & Feature", "Monocotyledonous Structure", "Dicotyledonous Structure"],
                            "rows": [
                                ["Stem Vascular Bundles", "Scattered randomly throughout ground tissue", "Arranged in a regular concentric ring near outer edge"],
                                ["Stem Vascular Cambium", "Absent (no secondary growth)", "Present between xylem and phloem (secondary woody growth)"],
                                ["Stem Cortex & Pith", "No distinct cortex or pith", "Distinct outer cortex and central storage pith"],
                                ["Root Xylem Core", "Arranged in a ring around a central pith", "Solid central 'X-shaped' or star-like xylem core (no pith)"],
                                ["Root Phloem Location", "Alternates with xylem in a ring", "Tucked into the corners between the arms of the xylem star"]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Monocot and Dicot Anatomy — Stems and Roots",
                        "content": {
                            "description": "Video presentation exploring the microscopic histology of monocot and dicot stems and roots, vascular cambium secondary growth, and Casparian strip checkpoints."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Vascular Cambium Identification",
                        "content": {
                            "question": "A student collecting plant specimens slices a thin cross-section of a stem and observes it under a microscope. She notes that the vascular bundles are arranged in a neat outer ring, with a clear dividing line running through each bundle between the inner xylem and outer phloem. What type of plant is this, and what is the dividing line?",
                            "options": [
                                "Monocotyledon; endodermis",
                                "Dicotyledon; Casparian strip",
                                "Dicotyledon; vascular cambium",
                                "Monocotyledon; pith"
                            ],
                            "correct_answer": "C",
                            "explanation": "In dicot stems, vascular bundles form an orderly concentric ring. The dividing line within each bundle is the vascular cambium, an actively dividing meristematic layer that generates new xylem inward and new phloem outward during secondary growth."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Vascular Arrangements",
                        "content": {
                            "title": "Lesson Summary: Vascular Arrangements",
                            "points": [
                                "Monocot stems have scattered vascular bundles and lack cambium.",
                                "Dicot stems have ring-arranged vascular bundles with vascular cambium enabling secondary growth.",
                                "Monocot roots have vascular bundles in a ring around a central pith.",
                                "Dicot roots feature a solid central X-shaped xylem star with phloem nestled in the corners."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6.3: Uptake and Upward Movement of Water and Mineral Salts
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Uptake and Upward Movement of Water and Mineral Salts",
            "unit_description": "Physiology of passive water uptake (osmosis) vs active mineral ion transport (ATP), radial root pathways, and the four physical forces driving upward xylem ascent.",
            "lesson_title": "Uptake and Upward Movement of Water and Mineral Salts",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Water & Mineral Ascent",
                        "content": {
                            "title": "Learning Focus: Water & Mineral Ascent",
                            "goals": [
                                "Distinguish between the passive uptake of water and the active transport of mineral salts.",
                                "Trace the radial pathway of water from the soil to the central xylem vessels.",
                                "Explain the four physical forces driving upward xylem water transport: transpiration pull, cohesion-adhesion, capillarity, and root pressure."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Pumping Without Electricity",
                        "content": {
                            "title": "Pumping Without Electricity",
                            "text": "To move thousands of liters of water to the top of a skyscraper, engineers need massive electric pumps. Yet a giant forest tree lifts tons of water every single day without using a single watt of electricity.\n\nInstead, it harnesses chemical active transport in the roots and powerful physical forces in the xylem."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Xylem Transport Vocabulary",
                        "content": {
                            "term": "Essential Xylem Physiology Terms",
                            "definition": "Key concepts in water potential gradients and vertical fluid dynamics.",
                            "key_points": [
                                "Active Transport: Movement of substances across a cell membrane against a concentration gradient using ATP energy.",
                                "Cohesion: The intermolecular attraction between identical molecules (water molecules sticking to each other via H-bonds).",
                                "Adhesion: The attractive force between different molecules (water sticking to cellulose/lignin xylem walls).",
                                "Transpiration Pull: The powerful negative tension (suction) created at the leaves by water evaporation, pulling the xylem water column upward.",
                                "Capillarity: The spontaneous rise of liquid inside narrow micro-tubes due to surface tension."
                            ]
                        }
                    }
                ],
                # Page 3: Passive Water vs. Active Mineral Uptake
                [
                    {
                        "type": "concept_explanation",
                        "title": "Passive Osmosis vs. Active Mineral Transport",
                        "content": {
                            "title": "Passive Osmosis vs. Active Mineral Transport",
                            "text": "1. **Water Uptake (Passive Osmosis)**:\n- Soil water has low solute concentration (high water potential).\n- Root hair cell sap has high solute concentration (low water potential).\n- Water enters **passively down the water potential gradient** by osmosis across the selectively permeable membrane without consuming ATP.\n\n2. **Mineral Salt Uptake (Active Transport)**:\n- The concentration of mineral ions inside root hair cytoplasm is higher than in the surrounding soil water.\n- Minerals cannot diffuse inward passively; root cells must use **cellular energy (ATP)** from respiration to pump ions **against their concentration gradient** via active transport."
                        }
                    }
                ],
                # Page 4: Radial Pathway & 4 Forces SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Radial Pathway of Water & Mineral Uptake + 4 Xylem Upward Forces",
                        "content": {
                            "description": "Dual-panel diagram. Left: Radial root cross-section tracing water (blue arrows) and minerals (red dots) from soil water -> root hair -> cortex parenchyma -> endodermis (Casparian strip) -> xylem vessels. Right: Vertical xylem pipe illustrating the 4 upward forces: 1. Transpiration pull suction at leaf; 2. Cohesion-adhesion unbroken water column; 3. Capillarity in narrow lumen; 4. Root pressure pushing from below.",
                            "caption": "Integration of radial root absorption pathways with the vertical physical forces driving xylem ascent."
                        }
                    }
                ],
                # Page 5: Step-by-Step Radial Pathway
                [
                    {
                        "type": "step_process",
                        "title": "The Step-by-Step Radial Pathway Across the Root",
                        "content": {
                            "title": "The Step-by-Step Radial Pathway Across the Root",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Root Hair Influx",
                                    "description": "Water enters root hair cell sap by osmosis, diluting the cytoplasm and raising its water potential."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Cortex Osmotic Cascade",
                                    "description": "Water moves down a cell-to-cell water potential gradient across the cortical parenchyma cells."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Casparian Strip Checkpoint",
                                    "description": "At the endodermis, waxy Casparian strips block cell-wall flow, forcing water through living cytoplasm for selective filtering."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Xylem Vessel Loading",
                                    "description": "Water discharges into hollow, dead xylem vessels, ready for vertical ascent to the foliage canopy."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Lignified Xylem Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "High-Resolution Micrograph of Lignified Xylem Vessels",
                        "content": {
                            "description": "High-magnification stained light micrograph of longitudinal and transverse xylem vessels showing thick, lignified secondary cell walls with annular and spiral reinforcement rings.",
                            "caption": "Dead, hollow xylem vessels reinforced with spiral lignin rings that prevent tube collapse under powerful negative transpiration pull tension."
                        }
                    }
                ],
                # Page 7: The Four Upward Forces in Xylem
                [
                    {
                        "type": "comparison_table",
                        "title": "The Four Forces Driving Vertical Xylem Water Ascent",
                        "content": {
                            "headers": ["Physical Force", "Mechanism of Action", "Magnitude & Relative Contribution"],
                            "rows": [
                                ["Transpiration Pull", "Evaporation of water from leaf mesophyll generates powerful suction tension at top of xylem", "Primary force; lifts water hundreds of meters against gravity in tall trees"],
                                ["Cohesion and Adhesion", "Cohesion (H-bonds between water molecules) forms continuous water column; Adhesion (water-lignin attraction) prevents downward slippage", "Essential structural force maintaining continuous unbroken water column in xylem"],
                                ["Capillarity", "Surface tension causes liquids to rise spontaneously in microscopic narrow tubes", "Minor supplementary force operating over short distances in narrow vessels"],
                                ["Root Pressure", "Active accumulation of mineral ions in root xylem draws water in via osmosis, generating positive hydrostatic push", "Minor bottom-up pushing force (responsible for early morning guttation)"]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Uptake and Upward Movement of Water and Minerals",
                        "content": {
                            "description": "Educational animation exploring root osmosis, ATP-driven active mineral ion transport, Casparian strip filtration, and cohesion-tension xylem ascent."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Root Metabolic Inhibition",
                        "content": {
                            "question": "If you apply a metabolic poison (which halts cellular ATP production from respiration) to a plant's roots, which process will be severely and immediately disrupted first, and why?",
                            "options": [
                                "Water absorption; because osmosis requires massive quantities of cellular ATP.",
                                "Mineral ion absorption; because plants rely on active transport against a concentration gradient, which requires cellular ATP energy.",
                                "Transpiration pull; because evaporation from leaves is powered directly by root ATP.",
                                "Capillarity; because water molecules require ATP to stick to xylem walls."
                            ],
                            "correct_answer": "B",
                            "explanation": "Mineral salt absorption is an active process that relies on active transport protein pumps, which require ATP energy from cellular respiration. Osmosis, transpiration pull, cohesion-adhesion, and capillarity are passive physical processes that do not consume ATP."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Water & Mineral Ascent",
                        "content": {
                            "title": "Lesson Summary: Water & Mineral Ascent",
                            "points": [
                                "Water enters passively via osmosis; minerals enter actively using ATP energy.",
                                "Water traverses root hairs, cortex, and endodermis (Casparian strip) to enter xylem.",
                                "Transpiration pull is the primary suction force lifting water up xylem vessels.",
                                "Cohesion and adhesion keep the water column unbroken and anchored against gravity."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6.4: Transpiration and Factors Affecting Its Rate
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Transpiration and Factors Affecting Its Rate",
            "unit_description": "Routes of transpiration (stomatal, cuticular, lenticular), environmental regulatory factors (temperature, humidity, wind, light), and xerophytic morphological adaptations.",
            "lesson_title": "Transpiration and Factors Affecting Its Rate",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Transpiration Dynamics",
                        "content": {
                            "title": "Learning Focus: Transpiration Dynamics",
                            "goals": [
                                "Explain the three routes of transpiration in plants: stomatal, cuticular, and lenticular.",
                                "Analyze how environmental factors (temperature, humidity, wind speed, light intensity) regulate the rate of transpiration.",
                                "Describe the structural and anatomical adaptations of xerophytic plants that minimize water loss in arid environments."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Inevitable Evaporative Loss",
                        "content": {
                            "title": "The Inevitable Evaporative Loss",
                            "text": "Did you know that over 99% of the water absorbed by a plant is lost to the atmosphere as water vapor? Less than 1% is used for photosynthesis and growth.\n\nThis continuous evaporative loss is called **transpiration**. While it sounds wasteful, transpiration is vital: it generates the transpiration pull that lifts soil minerals and provides evaporative cooling under intense sunlight."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Transpiration Vocabulary",
                        "content": {
                            "term": "Essential Transpiration Terms",
                            "definition": "Key concepts in plant evaporative dynamics and arid adaptations.",
                            "key_points": [
                                "Transpiration: The evaporation of water from plant surfaces (mainly leaves) into the surrounding atmosphere.",
                                "Stomatal Transpiration: Water loss through stomata, accounting for 80% to 90% of total transpiration.",
                                "Lenticel: A porous slit-like opening in the bark of woody stems for gas exchange and minor water loss.",
                                "Xerophyte: A plant adapted morphologically and physiologically to survive in dry, arid habitats."
                            ]
                        }
                    }
                ],
                # Page 3: The Three Routes of Transpiration
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Three Routes of Transpiration",
                        "content": {
                            "title": "The Three Routes of Transpiration",
                            "text": "Water evaporates from wet mesophyll cells into leaf air spaces, escaping via three pathways:\n\n1. **Stomatal Transpiration (80%–90%)**: The dominant route. When stomata open to absorb $CO_2$ for photosynthesis, water vapor inevitably diffuses out down a humidity gradient.\n2. **Cuticular Transpiration (5%–15%)**: Evaporation directly across the waxy cuticle layer. Thick cuticles reduce this loss to near zero.\n3. **Lenticular Transpiration (1%–2%)**: Minor water vapor loss through loose lenticels on woody tree bark."
                        }
                    }
                ],
                # Page 4: Transpiration & Xerophytes SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Transpiration Routes, Environmental Regulators & Xerophyte Adaptations",
                        "content": {
                            "description": "Composite diagram. Top panel: The 3 transpiration routes (Stomatal 90%, Cuticular, Lenticular). Middle panel: 4 environmental rate graphs (Temperature rise, Humidity plunge, Wind rise, Light rise). Bottom panel: Xerophytic leaf adaptations (Thick waxy cuticle, sunken stomata inside hairy crypt pits, and rolled leaf margins).",
                            "caption": "Routes of water loss, environmental rate determinants, and xerophytic adaptations."
                        }
                    }
                ],
                # Page 5: Environmental Factors Affecting Transpiration
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Regulators of Transpiration Rate",
                        "content": {
                            "headers": ["Environmental Factor", "Condition Producing High Transpiration", "Physical Mechanism Governing Rate"],
                            "rows": [
                                ["Temperature", "Hot, sunny days", "High heat increases kinetic energy of water molecules, accelerating evaporation, and increases saturation deficit of air"],
                                ["Atmospheric Humidity", "Dry, arid days (low humidity)", "Low ambient moisture creates a steep water vapor concentration gradient between leaf interior and atmosphere"],
                                ["Wind Speed / Air Currents", "Breezy or windy weather", "Air currents blow away accumulated moist boundary layers at leaf surfaces, maintaining a steep diffusion gradient"],
                                ["Light Intensity", "Bright daylight", "Light triggers guard cells to become turgid, opening stomata fully for photosynthesis, increasing water vapor exit"]
                            ]
                        }
                    }
                ],
                # Page 6: Xerophytic Needle Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Transverse Micrograph of Xerophytic Pine Needle with Sunken Stomata",
                        "content": {
                            "description": "Light microscope cross-section of a xerophytic pine needle showing extremely thick waxy cuticle, compact hypodermis, sunken stomatal pits with protective trichome hairs, and reduced surface area.",
                            "caption": "Micrograph of a xerophytic leaf cross-section showing sunken stomata and heavy cuticle that minimize transpiration."
                        }
                    }
                ],
                # Page 7: Structural Adaptations in Xerophytes
                [
                    {
                        "type": "comparison_table",
                        "title": "Morphological Adaptations of Xerophytes to Drought",
                        "content": {
                            "headers": ["Xerophytic Adaptation", "Representative Plant Example", "Physiological Mechanism to Limit Water Loss"],
                            "rows": [
                                ["Thick Waxy Cuticle", "Sisal, Euphorbia, Rubber plant", "Forms an impermeable waterproof barrier that stops cuticular transpiration"],
                                ["Sunken Stomata in Pits", "Pine, Oleander, Marram grass", "Stomata sheltered inside recessed pits trap humid air, reducing the diffusion gradient"],
                                ["Reduced Leaf Area (Spines)", "Cactus, Acacia", "Leaves reduced to thorns or needles, drastically minimizing surface area for evaporation"],
                                ["Rolled Leaves with Hairs", "Marram grass, Olive tree", "Leaves roll inward during heat, trapping moist air inside rolls and deflecting dry winds"]
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Transpiration — Routes, Factors, and Xerophyte Adaptations",
                        "content": {
                            "description": "Comprehensive video exploration of stomatal transpiration dynamics, potometer measurement techniques, environmental rate curves, and xerophytic desert adaptations."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Transpiration Rate on Windy Days",
                        "content": {
                            "question": "On a hot, dry, and windy afternoon in Machakos, which of the following describes the rate of transpiration and the physical reasons behind it?",
                            "options": [
                                "Low; because wind closes the stomata to conserve water.",
                                "High; because high temperature increases water molecule kinetic energy, dry air maintains a steep diffusion gradient, and wind sweeps away escaped water vapor from leaf surfaces.",
                                "Constant; because environmental factors do not affect physical evaporation.",
                                "Low; because dry air decreases the saturation deficit."
                            ],
                            "correct_answer": "B",
                            "explanation": "All three environmental conditions synergistically maximize transpiration: high temperature increases water molecule kinetic energy, dry air (low humidity) creates a steep concentration gradient, and wind continuously sweeps away saturated air from the leaf boundary layer."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Transpiration Dynamics",
                        "content": {
                            "title": "Lesson Summary: Transpiration Dynamics",
                            "points": [
                                "Transpiration occurs via stomatal (80-90%), cuticular, and lenticular routes.",
                                "Transpiration rate increases with higher temperature, lower humidity, faster wind, and bright light.",
                                "Transpiration cools leaves and powers the transpiration stream.",
                                "Xerophytes utilize thick cuticles, sunken stomata, rolled leaves, and spines to survive drought."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6.5: Translocation of Manufactured Food
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Translocation of Manufactured Food",
            "unit_description": "Phloem transport mechanisms (source to sink, multidirectional flow), sieve tube and companion cell adaptations, and the classical bark girdling experiment.",
            "lesson_title": "Translocation of Manufactured Food",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Phloem Translocation Mechanics",
                        "content": {
                            "title": "Learning Focus: Phloem Translocation Mechanics",
                            "goals": [
                                "Define translocation and identify the organic substances transported through the phloem.",
                                "Describe the structural and functional adaptations of sieve tubes and companion cells.",
                                "Analyze and interpret the classic bark ringing (girdling) experiment as evidence for phloem transport."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Delivering Solar Energy Throughout the Plant",
                        "content": {
                            "title": "Delivering Solar Energy Throughout the Plant",
                            "text": "Once a leaf has manufactured glucose, the job is only half done. Those sugars must be transported down to nourish roots, sideways to build stems, and upward to fill fruits.\n\nThis mass transport of soluble organic food is called **translocation**. In this lesson, we explore how phloem moves viscous sap and investigate the historic bark ringing experiment."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Translocation Vocabulary",
                        "content": {
                            "term": "Essential Phloem Translocation Terms",
                            "definition": "Key concepts in source-to-sink organic transport.",
                            "key_points": [
                                "Translocation: The transport of soluble organic products of photosynthesis (sucrose, amino acids) through the phloem from source to sink.",
                                "Source: A plant organ (like a mature green leaf) that manufactures or exports organic nutrients.",
                                "Sink: A plant organ (like growing root tips, fruits, or tubers) that consumes or stores organic nutrients.",
                                "Sieve Tube: An elongated living phloem cell arranged end-to-end with perforated end walls (sieve plates), lacking nuclei to allow sap flow.",
                                "Companion Cell: A nucleated cell packed with mitochondria alongside a sieve tube, providing ATP for active phloem loading."
                            ]
                        }
                    }
                ],
                # Page 3: Principles of Translocation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Source-to-Sink Dynamics and Multidirectional Transport",
                        "content": {
                            "title": "Source-to-Sink Dynamics and Multidirectional Transport",
                            "text": "1. **Soluble Substances Transported**:\n- Glucose is converted to **sucrose** (a non-reducing disaccharide) for transport, alongside amino acids and vitamins.\n\n2. **Multidirectional Flow**:\n- Unlike xylem water transport (which is strictly upward / unidirectional), phloem translocation is **multidirectional**.\n- Sap flows downward from mature leaves to roots, upward from leaves to developing flowers/fruits, or from storage tubers up to sprouting shoots in spring."
                        }
                    }
                ],
                # Page 4: Phloem & Bark Girdling SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Phloem Longitudinal Ultrastructure & Bark Girdling Sequence",
                        "content": {
                            "description": "Dual-panel diagram. Left panel: Longitudinal section of phloem tissue showing hollowed-out sieve tube element, perforated sieve plate with pores, cytoplasmic strands, companion cell with large nucleus, dense mitochondria, and connecting plasmodesmata. Right panel: 3-step bark ringing experiment showing: 1. Intact woody stem; 2. Bark ring stripped (phloem removed, xylem intact); 3. Swollen bulge developing above ring due to accumulated downward sugars, with lower stem thinning and root starvation.",
                            "caption": "Phloem cellular adaptations for translocation alongside the classical bark ringing experimental evidence."
                        }
                    }
                ],
                # Page 5: Sieve Tube & Companion Cell Adaptations
                [
                    {
                        "type": "comparison_table",
                        "title": "Structural & Physiological Adaptations of Phloem Cells",
                        "content": {
                            "headers": ["Phloem Cell Component", "Structural Adaptation", "Functional Contribution to Translocation"],
                            "rows": [
                                ["Sieve Tube Element", "Elongated cells joined end-to-end; loses nucleus, vacuole, and ribosomes during maturity", "Provides an open, hollowed-out lumen with low resistance for mass bulk flow of viscous sugar sap"],
                                ["Sieve Plate with Pores", "Perforated horizontal cross-walls between adjacent sieve elements", "Allows cytoplasmic strands to pass through, maintaining continuous pressurized sap transport"],
                                ["Companion Cell", "Retains large nucleus and dense concentration of **mitochondria**", "Generates abundant ATP energy required for active loading of sucrose into sieve tubes against a gradient"],
                                ["Plasmodesmata", "Microscopic cytoplasmic channels connecting companion cells to sieve tubes", "Facilitates direct intercellular transfer of ATP, enzymes, and loaded sucrose molecules"]
                            ]
                        }
                    }
                ],
                # Page 6: Phloem Micrograph Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Transverse Section of Phloem Sieve Tubes & Companion Cells Micrograph",
                        "content": {
                            "description": "High-magnification stained light micrograph of plant phloem showing large, open sieve tube elements paired with smaller, densely stained companion cells containing prominent nuclei.",
                            "caption": "Micrograph of phloem tissue showing open sieve tube elements paired with dense, nucleated companion cells."
                        }
                    }
                ],
                # Page 7: Bark Girdling (Ringing) Experiment
                [
                    {
                        "type": "step_process",
                        "title": "The Classical Bark Girdling (Ringing) Experiment",
                        "content": {
                            "title": "The Classical Bark Girdling (Ringing) Experiment",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Bark Ring Removal",
                                    "description": "A complete ring of outer bark (containing phloem) is carefully peeled away from a woody tree stem, leaving the deep wood (xylem) intact."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Leaves Remain Healthy & Turgid",
                                    "description": "Leaves above the ring remain green and healthy for weeks because the inner xylem continues delivering water and minerals upward."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Upper Bulge Formation",
                                    "description": "Downcoming manufactured sugars hit the severed phloem block, cannot pass, and accumulate, causing cells directly above the ring to divide and swell into a prominent bulge."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Root Starvation & Tree Death",
                                    "description": "Roots below the ring receive no translocated sugars, run out of respiratory substrate, starve, and die, eventually killing the entire tree."
                                }
                            ]
                        }
                    }
                ],
                # Page 8: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Translocation in Phloem and the Girdling Experiment",
                        "content": {
                            "description": "Educational presentation detailing pressure-flow hypothesis, sieve tube and companion cell cytology, active sucrose loading, and bark ringing experiments."
                        }
                    }
                ],
                # Page 9: Knowledge Check & Summary
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Bark Ringing Observations",
                        "content": {
                            "question": "In a classical bark ringing experiment, the leaves of the tree remain green and healthy for several weeks, but a prominent swollen bulge develops directly above the peeled ring. Why do the leaves stay healthy, and what causes the bulge?",
                            "options": [
                                "Xylem is located in the outer bark and was removed, forcing leaves to synthesize more sugars.",
                                "Phloem is located in the inner wood and was left intact, while xylem in the bark accumulated sugars.",
                                "Xylem in the inner wood was left undamaged, allowing water to reach leaves; the bulge is caused by the accumulation of translocating sugars blockaded above the severed phloem bark.",
                                "The tree is growing new roots from the bark to bypass the cut."
                            ],
                            "correct_answer": "C",
                            "explanation": "The outer bark contains the phloem, while the deeper wood contains xylem. Leaving the xylem intact allows uninterrupted water delivery to the leaves. However, removing the phloem blocks downward sugar translocation, causing sugars to pile up above the girdle and trigger tissue swelling."
                        }
                    },
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Phloem Translocation",
                        "content": {
                            "title": "Lesson Summary: Phloem Translocation",
                            "points": [
                                "Translocation moves manufactured sugars (sucrose) and amino acids multidirectionally from sources to sinks.",
                                "Sieve tubes are hollowed out for fluid flow; companion cells provide ATP for active sugar loading.",
                                "Bark ringing removes phloem while leaving xylem intact, causing sugar accumulation and swelling above the girdle.",
                                "Roots eventually starve due to lack of translocated food, proving phloem is the conduit for organic nutrients."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic6(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 6."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 6: Plant Transport (CBC Curriculum ID: 5)")
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

    # 4. Resolve Topic 6
    topic_name = "Plant Transport"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=6,
            description="Comprehensive syllabus on plant transport systems (root absorption, monocot/dicot vascular histology, xylem water ascent, transpiration dynamics, xerophytic adaptations, and phloem translocation)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic6_curriculum()
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
    print("[SUCCESS] Grade 10 Biology Topic 6 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic6(replace=replace_flag)
