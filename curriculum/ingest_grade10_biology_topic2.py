"""
VLearn Grade 10 Biology — Topic 2: Anatomy and Physiology of Plants
Production Ingestion Engine (3 Comprehensive Lessons)

Curriculum: CBC (Curriculum ID: 5)
Grade: Grade 10 (Grade ID: 5, Level: 10)
Subject: Biology (Grade 10 CBC)
Topic: Anatomy and Physiology of Plants (Topic Order: 2)

Structured into 3 Comprehensive Learning Units & 3 Published Lessons (35 Concept Cards):
  1. Plant Nutrition and Photosynthesis (12 Pages)
  2. Plant Transport (12 Pages)
  3. Plant Gaseous Exchange and Respiration (11 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_grade10_biology_topic2.py [--replace]
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
    """Removes bracket citations [134, 137], visual prompt text, and cleans double spaces."""
    if not text:
        return ""
    # Remove bracket citations like [134], [134, 137], [image_1]
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

def build_topic2_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Grade 10 Biology Topic 2."""
    return [
        # =====================================================================
        # LESSON 2.1: Plant Nutrition and Photosynthesis
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Plant Nutrition and Photosynthesis",
            "unit_description": "Autotrophic vs heterotrophic plant nutrition, leaf and chloroplast adaptations, light and dark stages of photosynthesis, limiting factors, and leaf starch testing.",
            "lesson_title": "Plant Nutrition and Photosynthesis",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Nutrition & Photosynthesis",
                        "content": {
                            "title": "Learning Focus: Plant Nutrition & Photosynthesis",
                            "goals": [
                                "Compare autotrophic and heterotrophic nutrition in plants.",
                                "Describe parasitic, saprophytic, symbiotic, and insectivorous plant nutrition, explaining their structural adaptations and ecological roles.",
                                "Relate the external and internal physical structures of a leaf to its role in photosynthesis.",
                                "Describe the detailed structure of a chloroplast as seen under an electron microscope.",
                                "Illustrate the chemical reactions and locations of the light and dark stages of photosynthesis.",
                                "Explain how to test a leaf for starch safely using a water bath.",
                                "Explain how limiting factors (light intensity, carbon dioxide concentration, temperature) affect the rate of photosynthesis."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Solar-Powered Food Factory",
                        "content": {
                            "title": "The Solar-Powered Food Factory",
                            "text": "If you look at the towering trees of the Kakamega Forest, you might wonder: where do they get the thousands of kilograms of wood, bark, and leaves that build their bodies? They don't eat soil!\n\nInstead, plants have the incredible ability to manufacture their own food out of thin air, water, and sunlight. In this lesson, we explore autotrophic plant nutrition, compare it with specialized heterotrophic plants (parasites, mutualists, and insect hunters), study leaf and chloroplast anatomy, and trace the molecular stages of **photosynthesis**."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Photosynthesis & Nutrition Terminology",
                        "content": {
                            "term": "Essential Plant Nutrition Vocabulary",
                            "definition": "Key biological terms related to autotrophic and heterotrophic plant energetics.",
                            "key_points": [
                                "Autotrophic Nutrition: A mode of nutrition where an organism manufactures its own organic food molecules from simple inorganic raw materials using light energy.",
                                "Heterotrophic Nutrition: A mode of nutrition where an organism cannot make its own food and must obtain pre-manufactured organic compounds from other organisms.",
                                "Haustorium (plural Haustoria): Specialized root-like sucker organs of parasitic plants that penetrate host plant stems to steal water and manufactured sugars.",
                                "Photolysis: The chemical splitting of water molecules into hydrogen ions, electrons, and oxygen gas using trapped light energy in thylakoids.",
                                "Limiting Factor: Any environmental factor (such as light, $CO_2$, or temperature) that is in shortest supply, directly restricting the rate of a biological process."
                            ]
                        }
                    }
                ],
                # Page 3: Autotrophic vs Heterotrophic Nutrition in Plants
                [
                    {
                        "type": "concept_explanation",
                        "title": "Autotrophic and Heterotrophic Feeding Strategies in Plants",
                        "content": {
                            "title": "Autotrophic and Heterotrophic Feeding Strategies in Plants",
                            "text": "While most plants are autotrophs that manufacture sugars via photosynthesis, several plant species have evolved alternative feeding lifestyles to survive in specialized ecological niches:"
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Heterotrophic Plant Feeding Strategies",
                        "content": {
                            "headers": ["Feeding Strategy", "Representative Species", "Structural Adaptations", "Ecological Mechanism & Impact"],
                            "rows": [
                                ["Parasitic Plants", "Cuscuta (Dodder)", "Yellow, leafless vines lacking chlorophyll; possess penetrating haustoria", "Haustoria penetrate host phloem (to steal sucrose) and xylem (to steal water/minerals), leaving the host crop stunted"],
                                ["Symbiosis (Mutualism)", "Rhizobium in legume root nodules (beans/peas)", "Root nodules housing nitrogen-fixing bacteria", "Mutual benefit: Plant supplies carbohydrates and shelter; bacteria fix atmospheric nitrogen into soluble nitrates for plant protein synthesis"],
                                ["Insectivorous Plants", "Pitcher plant (Nepenthes), Venus Flytrap", "Modified leaf traps secreting digestive protease enzymes", "Grow in acidic, waterlogged, nitrogen-poor soils; digest insects to absorb amino acids as a nitrogen supplement"],
                                ["Saprophytism", "Fungi & saprophytic plants", "Extracellular hyphal enzymes", "Secrete enzymes externally onto dead organic matter, absorbing digested soluble nutrients for nutrient recycling"]
                            ]
                        }
                    }
                ],
                # Page 4: Leaf Structure-Function Adaptations
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Leaf: An Anatomical Masterpiece for Photosynthesis",
                        "content": {
                            "title": "The Leaf: An Anatomical Masterpiece for Photosynthesis",
                            "text": "The foliage leaf is structured to maximize light absorption and gaseous diffusion while minimizing water loss:\n\n- **Flat, Broad Lamina**: Expands surface area for maximum sunlight interception.\n- **Thinness**: Minimizes internal diffusion distance for $CO_2$ gas to reach photosynthesizing cells.\n- **Waxy Cuticle & Transparent Epidermis**: Allows light to penetrate directly to mesophyll while preventing dehydration.\n- **Palisade Mesophyll**: Columnar, tightly packed vertical cells beneath the upper epidermis packed with dense chloroplasts.\n- **Spongy Mesophyll**: Loosely arranged irregular cells with large intercellular air spaces allowing free circulation of $CO_2$ and $O_2$.\n- **Vascular Bundle (Vein)**: **Xylem** delivers water and mineral raw materials; **Phloem** translocates manufactured sugars away to sinks.\n- **Stomatal Pores**: Guard cells control stomatal aperture for $CO_2$ intake and $O_2$ release."
                        }
                    }
                ],
                # Page 5: Leaf 3D Cross-Section & Chloroplast SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Anatomy of a Leaf Cross-Section & Chloroplast Ultrastructure",
                        "content": {
                            "description": "Dual-panel vector diagram. Panel A: 3D cross-section of a dicot leaf showing cuticle, upper epidermis, palisade mesophyll packed with chloroplasts, spongy mesophyll with air spaces, vascular bundle with xylem and phloem, lower epidermis, and stomata. Panel B: Detailed chloroplast ultrastructure showing double outer/inner membrane, thylakoid grana stacks, connecting lamellae, fluid stroma, and starch granules.",
                            "caption": "Anatomical integration between the multi-layered tissue architecture of a leaf and the sub-cellular chloroplast organelle."
                        }
                    }
                ],
                # Page 6: Molecular Stages of Photosynthesis
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Two Molecular Stages of Photosynthesis",
                        "content": {
                            "title": "The Two Molecular Stages of Photosynthesis",
                            "text": "Photosynthesis is divided into two sequential biochemical pathways occurring in distinct chloroplast compartments:\n\n1. **The Light-Dependent Stage (in Thylakoid Grana)**:\n- Chlorophyll pigments trap photon light energy.\n- Light energy splits water molecules ($H_2O$) via **photolysis**:\n$$2\\text{H}_2\\text{O} \\xrightarrow{\\text{Light Energy}} 4\\text{H}^+ + 4e^- + \\text{O}_2\\text{ (gas)}$$\n- Hydrogen ions ($H^+$) and electrons are transferred to coenzymes (NADPH) for the next stage.\n- Oxygen gas ($O_2$) is released as a metabolic by-product.\n- ATP energy is generated via photophosphorylation.\n\n2. **The Light-Independent Stage / Dark Stage (in Stroma)**:\n- Light is not directly required; it can proceed in light or darkness as long as ATP and $H^+$ are present.\n- $CO_2$ from air combines with hydrogen ions ($H^+$) using ATP energy in a process called **carbon dioxide fixation**.\n- Simple carbohydrates (glucose) are synthesized and rapidly converted into insoluble **starch** granules for storage."
                        }
                    }
                ],
                # Page 7: Limiting Factors of Photosynthesis
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Limiting Factors Governing Photosynthetic Rate",
                        "content": {
                            "headers": ["Limiting Factor", "Physiological Role in Photosynthesis", "Effect of Increase", "Saturation / Extreme Plateau Effect"],
                            "rows": [
                                ["Light Intensity", "Drives photolysis of water and ATP generation in grana", "Rate increases steadily as more chlorophyll molecules absorb photons", "Curve plateaus when another factor (like $CO_2$ or temperature) becomes the limiting factor"],
                                ["Carbon Dioxide ($CO_2$) Concentration", "Carbon substrate for dark stage glucose synthesis in stroma", "Rate increases as more $CO_2$ is fixed by stromal enzymes", "Plateaus when stromal enzyme active sites become fully saturated with $CO_2$"],
                                ["Temperature", "Governs kinetic energy of enzyme-catalyzed dark stage reactions", "Rate doubles for every 10°C rise up to optimum (~35–40°C)", "Above optimum, high heat denatures stromal enzymes; photosynthetic rate plunges to zero"]
                            ]
                        }
                    }
                ],
                # Page 8: Practical Investigation: Testing a Leaf for Starch
                [
                    {
                        "type": "step_process",
                        "title": "Practical Protocol: Testing a Leaf for Starch (Proof of Photosynthesis)",
                        "content": {
                            "title": "Practical Protocol: Testing a Leaf for Starch (Proof of Photosynthesis)",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Boil in Water (Kill Protoplasm)",
                                    "description": "Dip leaf in boiling water for 5 minutes. This stops all metabolic enzyme reactions and breaks cell membranes, making them permeable to chemical reagents."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Boil in Ethanol in Water Bath (Decolorization)",
                                    "description": "Place leaf into a tube of ethanol inside a hot water bath. (NEVER heat ethanol directly over flame!). Ethanol dissolves and removes green chlorophyll, turning leaf white/pale."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Rinse in Warm Water (Softening)",
                                    "description": "Dip brittle leaf in warm water to wash away alcohol and restore softness."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Add Iodine on White Tile",
                                    "description": "Spread pale leaf on white tile and add brown-yellow Iodine solution. The leaf turns blue-black, confirming starch produced during photosynthesis."
                                }
                            ]
                        }
                    }
                ],
                # Page 9: Starch Test Photographic Result
                [
                    {
                        "type": "suggested_image",
                        "title": "Testing a Leaf for Starch: Iodine Blue-Black Proof of Photosynthesis",
                        "content": {
                            "description": "Photographic result of a starch test on a green leaf and a variegated leaf, showing dark blue-black staining where photosynthesis occurred and yellow-brown unstained areas where light or chlorophyll was absent.",
                            "caption": "Diagnostic Iodine starch test result: blue-black coloration confirms localized photosynthetic starch synthesis."
                        }
                    }
                ],
                # Page 10: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Nutrition, Photosynthesis, and Starch Testing",
                        "content": {
                            "description": "Comprehensive video guide covering light and dark stages of photosynthesis, chloroplast ultrastructure, limiting factors, and the step-by-step leaf starch practical."
                        }
                    }
                ],
                # Page 11: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Destarching and Light Requirement",
                        "content": {
                            "question": "A student destarches a potted plant by keeping it in a dark cupboard for 48 hours. He then covers a middle section of one leaf tightly with black paper on both sides, leaving the rest of the leaf exposed. He places the plant in sunlight for 6 hours, detaches the leaf, and performs the starch test. What color changes will occur?",
                            "options": [
                                "The entire leaf turns blue-black.",
                                "The covered section turns blue-black, while the exposed sections remain brown-yellow.",
                                "The covered section remains brown-yellow, while the exposed sections turn blue-black.",
                                "The entire leaf remains brown-yellow."
                            ],
                            "correct_answer": "C",
                            "explanation": "Destarching ensures no pre-existing starch remains in the leaf. The black paper blocks sunlight from reaching the covered middle section, preventing photolysis and the light-dependent stage. The exposed outer sections receive sunlight, perform photosynthesis, and synthesize starch, turning blue-black with iodine."
                        }
                    }
                ],
                # Page 12: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Nutrition & Photosynthesis",
                        "content": {
                            "title": "Lesson Summary: Plant Nutrition & Photosynthesis",
                            "points": [
                                "Plants are primarily autotrophs; specialized heterotrophs include parasitic Cuscuta, mutualistic Rhizobium, and insectivorous pitcher plants.",
                                "Leaves are adapted for light capture (palisade mesophyll) and gas diffusion (spongy mesophyll air spaces, stomata).",
                                "Photosynthesis proceeds in two stages: Light-dependent photolysis in thylakoid grana ($2H_2O \\rightarrow 4H^+ + 4e^- + O_2$) and Light-independent $CO_2$ fixation in the stroma.",
                                "Photosynthetic rates are governed by limiting factors (light, $CO_2$, temperature).",
                                "Starch testing requires boiling in water, ethanol decolorization in a water bath, and iodine staining (yellow-brown $\\rightarrow$ blue-black)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2.2: Plant Transport
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Plant Transport",
            "unit_description": "Vascular anatomy of monocot and dicot stems and roots, mechanisms of water uptake (active transport, root pressure, capillarity, transpiration pull), transpiration factors, potometer measurements, and phloem translocation.",
            "lesson_title": "Plant Transport",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Transport Systems",
                        "content": {
                            "title": "Learning Focus: Plant Transport Systems",
                            "goals": [
                                "Explain why multicellular plants require specialized internal transport systems.",
                                "Identify xylem and phloem vascular arrangement in monocotyledonous and dicotyledonous roots and stems.",
                                "Explain mechanisms of water and mineral uptake from soil to leaves (root pressure, capillarity, active transport, transpiration pull).",
                                "Describe factors affecting the rate of transpiration and demonstrate how to measure it using a potometer.",
                                "Describe the mechanism of translocation of manufactured sugars through phloem and interpret the bark-ringing experiment."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Transporting Fluids Without a Heart",
                        "content": {
                            "title": "Transporting Fluids Without a Heart",
                            "text": "A towering 50-meter tree must deliver water and mineral salts absorbed by its underground roots all the way to its topmost leaves, while simultaneously transporting sugars manufactured in the leaves down to the roots.\n\nHow does a plant achieve this massive fluid movement without a muscular pump? Plants rely on specialized vascular tissues (**xylem** and **phloem**) driven by physical evaporation forces and active cellular loading."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Plant Vascular Transport Vocabulary",
                        "content": {
                            "term": "Essential Vascular Terminology",
                            "definition": "Key concepts in plant transport physiology and vascular anatomy.",
                            "key_points": [
                                "Transpiration: The evaporation and diffusion of water vapor from plant leaves to the atmosphere, primarily through stomatal pores.",
                                "Translocation: The active movement of manufactured organic food substances (sucrose) through phloem sieve tubes from sources to sinks.",
                                "Xylem: Vascular tissue composed of dead, hollow, lignified vessels and tracheids adapted to transport water and dissolved minerals upward.",
                                "Phloem: Living vascular tissue composed of sieve tube elements and companion cells adapted to transport organic sugars bidirectional (upward and downward).",
                                "Transpiration Pull: A continuous upward suction tension generated in leaf xylem vessels as evaporating water molecules pull on the cohesive column of water below."
                            ]
                        }
                    }
                ],
                # Page 3: Monocot vs Dicot Vascular Arrangement
                [
                    {
                        "type": "comparison_table",
                        "title": "Vascular Arrangement: Monocotyledonous vs Dicotyledonous Plants",
                        "content": {
                            "headers": ["Plant Organ", "Dicotyledonous Structure", "Monocotyledonous Structure", "Functional Significance"],
                            "rows": [
                                ["Stem", "Vascular bundles organized in a neat outer circular ring; cambium present between xylem and phloem", "Vascular bundles scattered randomly throughout ground tissue; no cambium", "Cambium in dicots allows secondary growth (wood thickening); monocots remain herbaceous"],
                                ["Root", "Xylem forms a central cross or star shape; phloem bundles nested between arms of the star", "Xylem and phloem arranged in a ring surrounding a central soft pith", "Central dicot star provides strong tensile strength to resist pulling forces during wind storms"]
                            ]
                        }
                    }
                ],
                # Page 4: 4-Panel Comparative Vascular Anatomy SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Vascular Anatomy: Monocot vs. Dicot (Stems & Roots)",
                        "content": {
                            "description": "Four-panel vector cross-section diagram: 1. Dicot Stem (vascular bundles arranged in an outer ring with cambium, xylem inner, phloem outer). 2. Monocot Stem (vascular bundles scattered randomly across parenchyma). 3. Dicot Root (central star-shaped xylem with phloem in between). 4. Monocot Root (circular vascular ring surrounding central pith).",
                            "caption": "Microscopic cross-sections contrasting vascular bundle organization across dicot and monocot stems and roots."
                        }
                    }
                ],
                # Page 5: Mechanisms of Water and Mineral Uptake
                [
                    {
                        "type": "step_process",
                        "title": "The Upward Pathway of Water from Soil to Leaves",
                        "content": {
                            "title": "The Upward Pathway of Water from Soil to Leaves",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Active Transport at Root Hairs",
                                    "description": "Root hair cells actively pump mineral ions from soil into cytoplasm using ATP energy. This lowers root water potential, drawing water inward from soil via osmosis."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Root Pressure (Base Push)",
                                    "description": "Accumulation of water in root cortex builds hydrostatic pressure that pushes water slightly upward into the basal xylem vessels."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Capillarity (Adhesion & Cohesion)",
                                    "description": "Xylem vessels are microscopic narrow tubes. Water climbs due to cohesion (hydrogen bonding between water molecules) and adhesion (attraction to cellulose xylem walls)."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Transpiration Pull (Primary Suction Force)",
                                    "description": "Evaporation of water from leaf mesophyll creates high suction tension that pulls the unbroken cohesive water column upward all the way from root tips."
                                }
                            ]
                        }
                    }
                ],
                # Page 6: Microscopic Stem Section Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Helianthus Dicot Stem Vascular Bundles under Microscope",
                        "content": {
                            "description": "High-clarity stained microscopic cross-section of a dicot stem (Helianthus), showing clear ring arrangement of vascular bundles, thick-walled xylem vessels, active vascular cambium, and outer phloem sieve tubes.",
                            "caption": "Dicot stem cross-section displaying the organized ring of vascular bundles with lignified xylem vessels, cambium, and phloem."
                        }
                    }
                ],
                # Page 7: Transpiration and Controlling Environmental Factors
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Factors Governing Transpiration Rate",
                        "content": {
                            "headers": ["Environmental Factor", "Environmental Change", "Effect on Transpiration Rate", "Physical / Physiological Explanation"],
                            "rows": [
                                ["Temperature", "Increase (Warmth)", "Increases Rate", "Increases kinetic energy of water molecules, accelerating evaporation from mesophyll cell walls"],
                                ["Wind Speed", "Increase (Breezy)", "Increases Rate", "Blows away the humid boundary layer of water vapor around stomata, maintaining a steep diffusion gradient"],
                                ["Humidity", "Increase (Muggy/Wet)", "Decreases Rate", "Saturates air outside stomata with water vapor, flattening the diffusion gradient between leaf interior and atmosphere"],
                                ["Light Intensity", "Increase (Bright Sun)", "Increases Rate", "Triggers guard cells to open stomatal pores wide for photosynthesis, facilitating water vapor escape"]
                            ]
                        }
                    }
                ],
                # Page 8: Potometer & Bark-Ringing Mechanics SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Experimental Tools: Capillary Potometer & Bark-Ringing Translocation",
                        "content": {
                            "description": "Dual-panel diagram. Panel A: Labeled capillary potometer setup showing leafy shoot fitted in airtight rubber stopper, water reservoir with tap, calibrated millimeter ruler, capillary tube, and air bubble. Panel B: Classic bark-ringing (girdling) experiment on a woody stem showing swollen callus tissue above the girdle ring due to accumulated phloem sucrose, while tissue below remains unswollen.",
                            "caption": "Bubble potometer setup for measuring transpiration rates alongside bark-ringing evidence of phloem translocation."
                        }
                    }
                ],
                # Page 9: Phloem Translocation Mechanics & Bark-Ringing Evidence
                [
                    {
                        "type": "concept_explanation",
                        "title": "Phloem Translocation & Girdling Evidence",
                        "content": {
                            "title": "Phloem Translocation & Girdling Evidence",
                            "text": "Unlike xylem water transport (which is passive and strictly upward), **translocation** in phloem is an active, multi-directional process moving manufactured sugars from **Source** to **Sink**:\n\n- **Source**: Photosynthesizing leaves where sugars are manufactured.\n- **Sink**: Roots, growing shoots, buds, or fruits where sugars are consumed or stored.\n\n**The Classic Bark-Ringing (Girdling) Experiment**:\n1. A complete outer ring of bark (containing phloem) is stripped from a woody stem, leaving deeper xylem intact.\n2. Over several weeks, a prominent **swelling** develops directly **above the cut ring**, while the stem below remains thin.\n3. **Scientific Explanation**: Sugars manufactured in leaves travel downward through phloem. When they reach the severed ring, transport is blocked. Accumulated sucrose stimulates rapid cell division and tissue swelling. The roots below eventually starve, proving phloem transports organic food downward."
                        }
                    }
                ],
                # Page 10: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Transport — Xylem, Phloem, Transpiration, and Translocation",
                        "content": {
                            "description": "Detailed video exploration of xylem and phloem adaptations, transpiration pull, cohesion-tension theory, potometer operation, and phloem mass flow translocation."
                        }
                    }
                ],
                # Page 11: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Potometer Environmental Responses",
                        "content": {
                            "question": "A student sets up a bubble potometer in a classroom and measures the air bubble movement as 10 mm per minute. She then places a fan blowing air directly onto the leafy plant shoot. What bubble movement and what physical explanation do you expect?",
                            "options": [
                                "Bubble movement drops below 10 mm/min because wind closes stomata.",
                                "Bubble movement remains at 10 mm/min because potometers are not affected by wind.",
                                "Bubble movement increases above 10 mm/min because wind removes water vapor from the leaf surface, maintaining a steep diffusion gradient.",
                                "Bubble movement increases above 10 mm/min because wind increases the humidity of the classroom."
                            ],
                            "correct_answer": "C",
                            "explanation": "Wind sweeps away the humid water vapor boundary layer resting directly outside stomatal pores, replacing it with drier ambient air. This steepens the concentration gradient of water vapor between the moist leaf interior and the dry exterior, accelerating evaporation. As transpiration accelerates, stronger transpiration pull draws water out of the potometer faster, moving the bubble quicker."
                        }
                    }
                ],
                # Page 12: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Transport Systems",
                        "content": {
                            "title": "Lesson Summary: Plant Transport Systems",
                            "points": [
                                "Plants require vascular systems to move water from roots to leaves and sugars from leaves to sinks.",
                                "Dicot stems feature an organized vascular ring with cambium; monocot stems have scattered bundles. Dicot roots have star-shaped xylem; monocot roots have a vascular ring around central pith.",
                                "Water uptake is driven by active mineral transport at root hairs, root pressure, xylem capillarity (cohesion/adhesion), and transpiration pull.",
                                "Transpiration rate increases with temperature, wind speed, and light, but decreases with high humidity.",
                                "Phloem translocates sucrose from sources to sinks, as proven by swelling above the cut in bark-ringing experiments."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2.3: Plant Gaseous Exchange and Respiration
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Plant Gaseous Exchange and Respiration",
            "unit_description": "Sites of gaseous exchange (stomata, lenticels, cuticle, pneumatophores), habitat stomatal adaptations, theories of stomatal opening/closing (K+ ion pump), aerobic vs anaerobic respiration, and biogas digester construction.",
            "lesson_title": "Plant Gaseous Exchange and Respiration",
            "pages": [
                # Page 1: Introduction & Learning Focus
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Focus: Plant Gaseous Exchange & Respiration",
                        "content": {
                            "title": "Learning Focus: Plant Gaseous Exchange & Respiration",
                            "goals": [
                                "Identify cuticle, lenticels, stomata, and pneumatophores and relate them to gaseous exchange in terrestrial and aquatic plants.",
                                "Explain the mechanisms of stomatal opening and closing (photosynthetic, starch-sugar, and potassium-ion theories).",
                                "Compare the number, size, and distribution of stomata on leaves from hydrophytic, xerophytic, and mesophytic habitats.",
                                "Compare aerobic and anaerobic respiration in plants.",
                                "Describe the economic importance of anaerobic respiration and outline a hands-on biogas production project."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Plants Breathe Without Lungs",
                        "content": {
                            "title": "How Plants Breathe Without Lungs",
                            "text": "Plants, like animals, must breathe to live. They require **Oxygen** for cellular respiration to break down glucose and release ATP energy, and they require **Carbon (IV) Oxide** for photosynthesis.\n\nHowever, plants lack lungs, gills, or blood circulation. Instead, they rely on specialized surface pores distributed across leaves, woody stems, and breathing roots to exchange gases with their surroundings."
                        }
                    }
                ],
                # Page 2: Key Terms
                [
                    {
                        "type": "definition_card",
                        "title": "Gaseous Exchange & Fermentation Vocabulary",
                        "content": {
                            "term": "Essential Respiratory Terminology",
                            "definition": "Key concepts in plant gaseous exchange, stomatal dynamics, and anaerobic energetics.",
                            "key_points": [
                                "Lenticel: Small, raised slits of loosely packed cork cells on woody stems and roots that permit gas exchange.",
                                "Pneumatophore (Breathing Root): Specialized erect, aerial roots of coastal mangrove plants that grow upward out of waterlogged mud into air to absorb oxygen.",
                                "Turgidity: The swollen, high-pressure state of guard cells when filled with water, which forces the stomatal pore to bow open.",
                                "Fermentation: The anaerobic breakdown of glucose by plants or yeast to yield cellular ATP energy, carbon dioxide, and ethanol."
                            ]
                        }
                    }
                ],
                # Page 3: Sites of Gaseous Exchange and Habitat Adaptations
                [
                    {
                        "type": "comparison_table",
                        "title": "Sites of Gaseous Exchange & Habitat Stomatal Adaptations",
                        "content": {
                            "headers": ["Plant Habitat / Structure", "Anatomical Site", "Structural Adaptation", "Physiological Function"],
                            "rows": [
                                ["Mesophytes (Terrestrial plants - Bean/Maize)", "Leaf Stomata", "Stomata concentrated primarily on lower epidermis", "Minimizes direct exposure to sun and wind, reducing excessive transpiration while enabling $CO_2$ intake"],
                                ["Hydrophytes (Aquatic plants - Water lily)", "Leaf Stomata", "Stomata located ONLY on upper leaf epidermis", "Allows gas exchange with air above water; submerged lower surface has no stomata"],
                                ["Xerophytes (Arid plants - Cactus/Aloe)", "Leaf Stomata", "Few stomata, sunken in deep pits lined with fine epidermal hairs", "Traps a humid micro-climate near stomata to drastically reduce water loss in arid environments"],
                                ["Woody Stems & Roots", "Lenticels", "Loosely packed cork cells with large intercellular air spaces", "Allows oxygen to diffuse into inner living cambium and cortex cells of woody bark"],
                                ["Coastal Mangroves", "Pneumatophores", "Erect aerial roots growing vertically out of waterlogged mud", "Pneumatophores project above anaerobic mud to absorb atmospheric oxygen through lenticels for root respiration"]
                            ]
                        }
                    }
                ],
                # Page 4: Mangrove Pneumatophores Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Mangrove Pneumatophores (Breathing Roots) in Coastal Mangrove Swamps",
                        "content": {
                            "description": "High-resolution photograph of coastal mangrove trees showing hundreds of pencil-like vertical pneumatophore breathing roots projecting upward through waterlogged coastal mud into the air.",
                            "caption": "Mangrove pneumatophores (breathing roots) projecting above waterlogged, oxygen-depleted coastal mud to absorb atmospheric oxygen for root cellular respiration."
                        }
                    }
                ],
                # Page 5: Theories of Stomatal Opening and Closing
                [
                    {
                        "type": "concept_explanation",
                        "title": "Theories of Stomatal Opening and Closing",
                        "content": {
                            "title": "Theories of Stomatal Opening and Closing",
                            "text": "Stomatal opening is governed by changes in guard cell **turgor pressure**. Guard cells have **thick, rigid inner walls** and **thin, elastic outer walls**. When water enters, the outer walls stretch and bow outward, pulling the thick inner walls apart to open the pore.\n\nThree scientific theories explain how guard cells regulate this water movement:\n\n1. **Photosynthetic Theory**: Daytime photosynthesis produces soluble glucose in guard cells, lowering water potential. Water enters via osmosis, making guard cells turgid and opening the stoma.\n2. **Starch-Sugar Interconversion Theory**: In dark, accumulated $CO_2$ lowers pH, converting soluble sugar into insoluble starch. Water potential rises, water exits via osmosis, and guard cells become flaccid, closing the stoma. In light, $CO_2$ is consumed, pH rises, starch converts to soluble glucose, water enters, and the stoma opens.\n3. **Potassium-Ion ($K^+$) Theory (Modern Accepted Theory)**: In daylight, light stimulates membrane active transport pumps to pump **$K^+$ ions** into guard cells. This drastic accumulation of $K^+$ sharply lowers water potential. Water rapidly rushes in via osmosis, swelling guard cells and opening the pore. In darkness, $K^+$ diffuses out, water exits, and guard cells become flaccid, closing the stoma."
                        }
                    }
                ],
                # Page 6: Stomatal Opening & Closing SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Stomatal Opening and Closing Mechanics: K+ Influx and Guard Cell Turgor",
                        "content": {
                            "description": "Comparative vector diagram showing side-by-side: 1. Open Stoma: Two turgid kidney-shaped guard cells bowing outward with an open central pore, arrows showing active K+ influx and water osmosis, labeled thick inner wall and thin stretched outer wall. 2. Closed Stoma: Two flaccid guard cells collapsed tightly together with no central pore, arrows showing K+ efflux and water loss.",
                            "caption": "Biomechanical regulation of stomatal aperture governed by potassium ion (K+) active transport, water osmosis, and differential cell wall elasticity."
                        }
                    }
                ],
                # Page 7: Aerobic Respiration vs Anaerobic Fermentation
                [
                    {
                        "type": "concept_explanation",
                        "title": "Plant Respiration and Industrial Fermentation",
                        "content": {
                            "title": "Plant Respiration and Industrial Fermentation",
                            "text": "Plants perform cellular respiration day and night to power active transport, protein synthesis, and growth:\n\n- **Aerobic Respiration**: In the presence of oxygen, glucose is fully oxidized in mitochondria to yield 36-38 ATP, water, and $CO_2$.\n- **Anaerobic Respiration (Alcoholic Fermentation)**: In the absence of oxygen, glucose is partially broken down in cytoplasm into **Ethanol**, **Carbon (IV) Oxide**, and only 2 ATP:\n$$\\text{Glucose} \\rightarrow 2\\text{Ethanol} + 2\\text{CO}_2 + 2\\text{ ATP}$$\n\n**Economic Applications of Fermentation**:\n1. **Baking**: $CO_2$ gas bubbles produced by yeast leaven dough, creating light, porous bread.\n2. **Brewing**: Yeast ferment cereal grains and fruits to produce alcoholic beverages (beer, wine).\n3. **Biogas Energy**: Methanogenic bacteria ferment livestock manure and crop waste anaerobically to produce methane fuel ($CH_4$) for cooking and lighting."
                        }
                    }
                ],
                # Page 8: Practical Project: Small-Scale Biogas Digester
                [
                    {
                        "type": "step_process",
                        "title": "Practical Activity: Constructing a Recycled Biogas Digester",
                        "content": {
                            "title": "Practical Activity: Constructing a Recycled Biogas Digester",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "title": "Digester Construction & Sealing",
                                    "description": "Bore a snug hole in the cap of a 20-liter plastic jerrycan. Insert a flexible gas tube and seal airtight with silicone glue."
                                },
                                {
                                    "step_number": 2,
                                    "title": "Slurry Preparation",
                                    "description": "Mix fresh cow dung with water in a 1:1 ratio to create a microbial slurry containing methanogenic bacteria. Add chopped kitchen vegetable scraps."
                                },
                                {
                                    "step_number": 3,
                                    "title": "Fill & Seal Headspace",
                                    "description": "Pour slurry into the container leaving 20% headspace for gas accumulation. Screw cap tightly and attach a control valve to the tube end."
                                },
                                {
                                    "step_number": 4,
                                    "title": "Fermentation & Gas Testing",
                                    "description": "Place in warm sunlight for 7-14 days. Anaerobic bacteria ferment waste into methane ($CH_4$). When tested outdoors, gas burns with a clean blue flame."
                                }
                            ]
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Financial Literacy & Environmental Benefit",
                        "content": {
                            "title": "Financial Literacy & Environmental Benefit",
                            "text": "Constructing an improvised biogas digester from recycled containers costs less than $150\\text{ KES}$, saving thousands compared to commercial steel units. Furthermore, the digested bio-slurry leftover serves as high-grade nitrogen-rich organic fertilizer for vegetable gardens."
                        }
                    }
                ],
                # Page 9: Deep Dive Educational Video
                [
                    {
                        "type": "suggested_video",
                        "title": "Deep Dive: Plant Gaseous Exchange, Stomatal Regulation, and Respiration",
                        "content": {
                            "description": "Video exploration of stomatal anatomy, potassium ion transport mechanics, xerophytic/hydrophytic leaf adaptations, and plant respiration vs biogas fermentation."
                        }
                    }
                ],
                # Page 10: Knowledge Check
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Mangrove Pneumatophore Function",
                        "content": {
                            "question": "Mangrove trees grow in waterlogged coastal muds along the Kenyan coast. A developer clears a section of mangroves and fills the mud with heavy, dry sand to build a resort. After a few months, the remaining mangroves in that sand-filled zone wither and die. What is the most likely biological explanation?",
                            "options": [
                                "The sand was too dry, preventing water absorption.",
                                "Mangroves cannot grow in sand; they require mud.",
                                "The heavy sand covered and blocked the waxy cuticle of the leaves.",
                                "The heavy sand blocked air access to the vertical pneumatophores, preventing oxygen from diffusing to the roots and halting root cellular respiration."
                            ],
                            "correct_answer": "D",
                            "explanation": "Mangroves survive in waterlogged anaerobic muds because they possess vertical pneumatophores (breathing roots) projecting above the mud to absorb atmospheric oxygen. Covering them with sand severed oxygen diffusion, halting aerobic respiration in root cells and preventing ATP generation needed for active transport water and mineral uptake."
                        }
                    }
                ],
                # Page 11: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson Summary: Plant Gaseous Exchange & Respiration",
                        "content": {
                            "title": "Lesson Summary: Plant Gaseous Exchange & Respiration",
                            "points": [
                                "Plants exchange gases through leaf stomata, stem lenticels, waxy cuticle, and coastal mangrove pneumatophores.",
                                "Stomatal opening is governed by guard cell turgor: active $K^+$ influx draws in water via osmosis, bowing the thick inner walls apart.",
                                "Stomatal distribution reflects habitat: upper surface only in hydrophytes, sunken pits in xerophytes, lower surface in mesophytes.",
                                "Aerobic respiration generates 36-38 ATP in mitochondria; anaerobic fermentation generates 2 ATP, ethanol, and $CO_2$ (utilized in baking, brewing, and biogas production)."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_grade10_biology_topic2(replace=False):
    """Executes the database ingestion for Grade 10 Biology Topic 2."""
    print("=" * 80)
    print("VLearn Grade 10 Biology — Ingestion Engine")
    print("Topic 2: Anatomy and Physiology of Plants (CBC Curriculum ID: 5)")
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

    # 4. Resolve Topic 2
    topic_name = "Anatomy and Physiology of Plants"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Performing clean replacement of child units/lessons...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()
    elif not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=2,
            description="Comprehensive syllabus on plant nutrition, photosynthesis, vascular transport (xylem and phloem), transpiration, gaseous exchange, and respiration."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic2_curriculum()
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
    print("[SUCCESS] Grade 10 Biology Topic 2 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages/Cards:      {total_pages}")
    print(f"[*] Total Blocks Created:   {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_grade10_biology_topic2(replace=replace_flag)
