"""
VLearn CBC Grade 10 Geography — Topic 8: Vulcanicity
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 8: Vulcanicity
Source: Grade 10 Geography/08_vulcanicity.md

Lessons:
  1. Meaning and Causes of Vulcanicity
  2. Intrusive Vulcanicity and Features
  3. Extrusive Vulcanicity and Lava Types
  4. Volcanic Materials: Solids, Liquids, and Gases
  5. Extrusive Landforms: Shield Volcanoes, Cinder Cones, and Lava Plateaus
  6. Composite Volcanoes (Stratovolcanoes)
  7. Craters, Calderas, and Caldera Lakes
  8. Geysers and Hot Springs
  9. Global Distribution of Volcanic Features
  10. Vulcanicity in Kenya: Distribution and Landscape
  11. Benefits of Vulcanicity to Human Activities
  12. Hazards and Environmental Effects of Vulcanicity
  13. Disaster Preparedness and Volcanic Simulation

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic8.py
"""

import os
import sys
import re
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import (
    Curriculum, Grade, Subject, Topic,
    LearningUnit, Lesson, LessonBlock
)

def clean_text(raw_str):
    """Remove citation brackets ([1], [48], [S1, p. 1]) and normalize whitespace."""
    if not isinstance(raw_str, str):
        return raw_str
    cleaned = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', raw_str)
    cleaned = re.sub(r'[ \t]+', ' ', cleaned)
    return cleaned.strip()

def clean_content_dict(data):
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, list):
        return [clean_content_dict(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_content_dict(v) for k, v in data.items()}
    return data

# =============================================================================
# TOPIC 8 LESSON DEFINITIONS (13 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Meaning and Causes of Vulcanicity
    {
        "unit_order": 1,
        "unit_name": "Meaning and Causes of Vulcanicity",
        "lesson_title": "Meaning and Causes of Vulcanicity",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Introduction to Vulcanicity & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Molten Magma and Volcanic Energy",
                        "content": {"text": "A photograph showing an active volcanic eruption with glowing molten rock and steam in the East African Rift."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Meaning and Causes of Vulcanicity",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define vulcanicity, magma, and lava with scientific accuracy\n"
                                "- Explain the internal and external thermal and tectonic drivers of vulcanicity\n"
                                "- Describe decompression melting at divergent boundaries, flux melting at subduction zones, and mantle hotspots"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Boiling Porridge Pot",
                        "content": {
                            "text": (
                                "Have you ever boiled porridge or ugali in a closed pot? As the heat rises, "
                                "thick bubbles of porridge swell, push upward, and burst through the surface, "
                                "sometimes spilling over the sides of the pot. In a very similar way, molten rock "
                                "deep within the Earth is pressurized by intense heat, forcing its way through cracks "
                                "in the crust to erupt onto the surface!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Vulcanicity, Magma & Lava",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Vulcanicity",
                        "content": {
                            "term": "Vulcanicity",
                            "definition": "The process by which solid, liquid, or gaseous materials are forced out of the Earth's interior into the crust or onto its surface."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Magma",
                        "content": {
                            "term": "Magma",
                            "definition": "Molten rock material containing dissolved gases and crystals while it remains beneath the Earth's surface in the mantle or crust."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Lava",
                        "content": {
                            "term": "Lava",
                            "definition": "Molten rock that has reached and erupted onto the Earth's surface and lost some of its dissolved gases to the atmosphere."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Tectonic & Thermal Drivers of Magma Generation",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Tectonic and Thermal Drivers of Magma Generation",
                        "content": {
                            "caption": "Cross-section showing decompression melting at divergent boundaries, subduction flux melting, and mantle hotspot plumes."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Why Does Rock Melt Inside the Earth?",
                        "content": {
                            "text": (
                                "Magma is generated inside the Earth through three primary mechanisms:\n\n"
                                "1. **Earth's Internal Heat Source:** Residual heat from Earth's formation combined with ongoing radioactive decay of isotopes (uranium, thorium, potassium) maintains superheated mantle conditions.\n"
                                "2. **Decompression Melting at Divergent Boundaries:** When tectonic plates pull apart, confining pressure on the underlying asthenosphere drops suddenly. This reduction in pressure lowers the melting point of hot mantle rocks, causing them to melt into magma without extra heat.\n"
                                "3. **Flux Melting at Subduction Zones:** As a dense oceanic plate sinks beneath continental crust, high temperatures bake water out of oceanic sediments. This water acts as a chemical flux, lowering the melting point of the overlying mantle wedge.\n"
                                "4. **Mantle Hotspots:** Thermal plumes originating deep near the core-mantle boundary melt holes through overlying crustal plates (such as Hawaii and Yellowstone)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Context: East African Rift Vulcanicity",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Kenya and the Great East African Rift Tectonic Engine",
                        "content": {
                            "text": (
                                "Kenya is a globally celebrated natural laboratory for vulcanicity. "
                                "The East African Rift Valley represents an active continental divergent boundary where "
                                "the Nubian and Somali tectonic plates are slowly pulling apart.\n\n"
                                "This tectonic stretching has thinned Kenya's crust, triggering massive decompression melting. "
                                "As a result, an extraordinary volcanic chain stretches along the Kenyan rift floor, "
                                "from Lake Turkana in the north, through Mount Longonot and Menengai Caldera, down to Olkaria and Suswa."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Meaning & Causes",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Magma vs Lava",
                        "content": {
                            "question": "What is the primary difference between magma and lava?",
                            "options": [
                                "Magma is solid rock, while lava is liquid rock.",
                                "Magma is molten rock underground, while lava is molten rock that has erupted onto the surface.",
                                "Magma is cold and unpressurized, while lava is extremely hot.",
                                "Magma forms only under oceans, while lava exists only on land."
                            ],
                            "correct_answer": "Magma is molten rock underground, while lava is molten rock that has erupted onto the surface.",
                            "explanation": "Magma refers to molten rock material beneath the Earth's surface containing dissolved volatile gases. Once it breaches the crust and flows on the surface, it is termed lava."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Decompression Melting Mechanism",
                        "content": {
                            "question": "Which process generates magma at divergent plate boundaries, such as the East African Rift?",
                            "options": [
                                "Intense horizontal compression and folding of crustal rocks.",
                                "Decompression melting, where a drop in pressure lowers the rock's melting point.",
                                "Massive cold ocean water flooding into the outer core.",
                                "Chemical dissolution between limestone and sulfur."
                            ],
                            "correct_answer": "Decompression melting, where a drop in pressure lowers the rock's melting point.",
                            "explanation": "At divergent rifting zones, crustal thinning reduces confining pressure on the hot asthenospheric mantle. This pressure drop (decompression) lowers the rock melting point, generating magma without requiring additional thermal energy."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Intrusive Vulcanicity and Features
    {
        "unit_order": 2,
        "unit_name": "Intrusive Vulcanicity and Features",
        "lesson_title": "Intrusive Vulcanicity and Features",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Intrusive Vulcanicity & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Towering Intrusive Volcanic Plug: Fischer's Tower",
                        "content": {"text": "A photograph of Fischer's Tower standing as a monumental vertical stone spire in Hell's Gate National Park, Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Intrusive (Plutonic) Features",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define intrusive (plutonic) vulcanicity and bedding planes\n"
                                "- Identify, sketch, and describe dykes, sills, batholiths, laccoliths, lopoliths, and volcanic plugs\n"
                                "- Classify intrusive features into concordant (parallel) and discordant (cross-cutting) structures"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Layered Cake Analogy",
                        "content": {
                            "text": (
                                "Imagine baking a multi-layer chocolate cake. If you inject molten chocolate, "
                                "sometimes it spreads flat between the horizontal cake layers, while at other points "
                                "it cuts straight vertically through all the layers and hardens inside without spilling outside. "
                                "Similarly, magma frequently solidifies deep within older rock strata underground, "
                                "forming majestic structures that are only revealed millions of years later through erosion!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Fundamental Concepts: Intrusive Vulcanicity",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Intrusive Vulcanicity (Plutonism)",
                        "content": {
                            "term": "Intrusive Vulcanicity",
                            "definition": "The geological process where magma forces its way into crustal cracks, fissures, and bedding planes, cooling and crystallizing deep underground before ever reaching the surface."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Bedding Plane",
                        "content": {
                            "term": "Bedding Plane",
                            "definition": "The planar boundary surface separating two distinct horizontal layers or strata of sedimentary or volcanic rocks."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Anatomy of Underground Magmatic Features",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Cross-Section of Intrusive Magmatic Features",
                        "content": {
                            "caption": "Comprehensive geological cross-section detailing Batholith, Laccolith, Lopolith, Dyke, Sill, and Volcanic Plug."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Six Key Intrusive Structures",
                        "content": {
                            "text": (
                                "Intrusive bodies are categorized by geometry and relation to host rock strata:\n\n"
                                "1. **Sill (Concordant):** A flat, horizontal tabular sheet of igneous rock formed when magma squeezes parallel between existing sedimentary bedding planes.\n"
                                "2. **Dyke (Discordant):** A vertical or steeply inclined sheet of igneous rock that cuts across the bedding planes of surrounding rock strata.\n"
                                "3. **Batholith (Plutonic Root):** A gigantic, deep-seated igneous mass (usually granite) covering over 100 square kilometers, forming the foundational root of mountain systems.\n"
                                "4. **Laccolith (Mushroom Dome):** A dome-shaped intrusion with a flat horizontal floor, formed when viscous magma arches overlying strata upward.\n"
                                "5. **Lopolith (Saucer Basin):** A large, saucer-shaped intrusion that sags downward in the middle due to the weight of dense cooling magma.\n"
                                "6. **Volcanic Plug (Neck):** A vertical cylindrical column of solidified magma that blocked the central conduit (vent) of an ancient volcano."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Case Study: Fischer's Tower & Mt. Kenya Plug",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Exposed Volcanic Plugs in the Kenyan Landscape",
                        "content": {
                            "text": (
                                "Kenya boasts world-renowned examples of exposed volcanic plugs:\n\n"
                                "- **Fischer's Tower (Hell's Gate National Park):** A spectacular 25-meter columnar volcanic plug standing prominently in the gorge. Millions of years of wind and flash-flood erosion stripped away the soft volcanic ash of the original volcanic cone, leaving the hard, basaltic neck.\n"
                                "- **Mount Kenya Peaks (Batian and Nelion):** The sharp, imposing alpine spires of Mount Kenya represent the deeply eroded, crystallized plug of a massive extinct stratovolcano that was active over 3 million years ago."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Intrusive Structures",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Concordant vs Discordant Intrusions",
                        "content": {
                            "question": "An igneous intrusion that forms a horizontal sheet parallel to the surrounding sedimentary rock layers is called a:",
                            "options": [
                                "Dyke",
                                "Sill",
                                "Batholith",
                                "Laccolith"
                            ],
                            "correct_answer": "Sill",
                            "explanation": "A sill is a concordant intrusion, meaning it intrudes horizontally parallel to pre-existing bedding planes. A dyke is discordant because it cuts across bedding planes."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Batholith Scale and Nature",
                        "content": {
                            "question": "Which intrusive feature is the largest, forming deep underground across hundreds of square kilometers?",
                            "options": [
                                "Lopolith",
                                "Volcanic Plug",
                                "Batholith",
                                "Sill"
                            ],
                            "correct_answer": "Batholith",
                            "explanation": "A batholith is the largest type of plutonic intrusion, typically composed of coarse-grained granite and extending across hundreds of square kilometers beneath mountain ranges."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Extrusive Vulcanicity and Lava Types
    {
        "unit_order": 3,
        "unit_name": "Extrusive Vulcanicity and Lava Types",
        "lesson_title": "Extrusive Vulcanicity and Lava Types",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Extrusive Vulcanicity & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Glowing Lava Channel and Flow",
                        "content": {"text": "A close-up photograph of a dynamic basaltic lava channel overflowing with fluid red-hot molten rock."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Extrusive Vulcanicity & Lava Types",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define extrusive vulcanicity and viscosity\n"
                                "- Differentiate between acidic (felsic) and basic (mafic) lava in terms of silica content, temperature, and gas retention\n"
                                "- Relate lava viscosity to explosive vs effusive volcanic eruption styles"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Rivers of Fire vs Explosive Blasts",
                        "content": {
                            "text": (
                                "Why do some volcanic eruptions flow peacefully like gentle rivers of red-hot syrup (as in Hawaii), "
                                "while others explode catastrophically, pulverizing entire mountain peaks into miles-high ash columns (like Mt. St. Helens)? "
                                "The secret lies in the chemical stickiness or internal friction of molten rock: its **viscosity**!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Extrusive Processes & Viscosity",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Extrusive Vulcanicity (Volcanism)",
                        "content": {
                            "term": "Extrusive Vulcanicity",
                            "definition": "The geological process by which magma breaches the Earth's surface and erupts as lava, solid pyroclasts, and volcanic gases to build landscape relief features."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Viscosity",
                        "content": {
                            "term": "Viscosity",
                            "definition": "A fluid's internal resistance to flow. High-viscosity fluids are thick and sticky (like cold honey), whereas low-viscosity fluids are thin and fluid (like water)."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Acidic vs Basic Lava Flow Dynamics",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Acidic vs Basic Lava Flow Dynamics and Viscosity",
                        "content": {
                            "caption": "Side-by-side comparison of basic low-viscosity lava spreading into wide sheets versus acidic high-viscosity lava forming steep domes."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Comparative Lava Chemistry and Eruption Styles",
                        "content": {
                            "text": (
                                "The behavior of lava is controlled strictly by its silica (SiO2) percentage:\n\n"
                                "### 1. Basic (Mafic) Lava:\n"
                                "- **Silica Content:** Low (45% to 52% SiO2), high in iron (Fe) and magnesium (Mg).\n"
                                "- **Viscosity:** Low — very fluid and runny, capable of flowing tens of kilometers before cooling.\n"
                                "- **Temperature:** Extremely high (1000°C to 1200°C).\n"
                                "- **Gas Content:** Low gas retention; gases bubble out freely, resulting in **effusive (gentle)** eruptions.\n\n"
                                "### 2. Acidic (Felsic) Lava:\n"
                                "- **Silica Content:** High (over 65% SiO2), rich in aluminum and potassium.\n"
                                "- **Viscosity:** High — thick, gummy, and sluggish; builds steep domes right over the vent.\n"
                                "- **Temperature:** Lower (800°C to 1000°C).\n"
                                "- **Gas Content:** Traps high volumes of dissolved steam and gases under immense pressure, triggering **violent explosive eruptions** when released."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Lava Chemistry & Viscosity",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Characteristics of Acidic Lava",
                        "content": {
                            "question": "Lava with high silica content that is thick, sticky, and erupts explosively is classified as:",
                            "options": [
                                "Basic lava",
                                "Acidic lava",
                                "Ultramafic lava",
                                "Carbonatite lava"
                            ],
                            "correct_answer": "Acidic lava",
                            "explanation": "Acidic (felsic) lava contains over 65% silica, making it highly viscous. It traps volcanic gases until explosive pressure shatters the magma into ash and pyroclasts."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Flow Properties of Basic Lava",
                        "content": {
                            "question": "Basic lava flows easily over long distances across the landscape because:",
                            "options": [
                                "It has high viscosity and high silica content.",
                                "It has low viscosity and low silica content.",
                                "It is frozen into solid crystal blocks.",
                                "It contains no minerals or dissolved elements."
                            ],
                            "correct_answer": "It has low viscosity and low silica content.",
                            "explanation": "Basic lava is low in silica, which gives it low viscosity (high fluidity) and high temperature, allowing it to spread far across valleys and plains before solidifying."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Volcanic Materials: Solids, Liquids, and Gases
    {
        "unit_order": 4,
        "unit_name": "Volcanic Materials: Solids, Liquids, and Gases",
        "lesson_title": "Volcanic Materials: Solids, Liquids, and Gases",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Volcanic Materials & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Aerodynamic Volcanic Bomb Ejecta",
                        "content": {"text": "A photograph showing a dense, spindle-shaped volcanic bomb ejected during an explosive volcanic eruption."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Volcanic Solids, Liquids, and Gases",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify the solid, liquid, and gaseous materials ejected during volcanic eruptions\n"
                                "- Differentiate pyroclastic solids by grain size (dust/ash, lapilli, blocks, bombs)\n"
                                "- Distinguish between Pahoehoe and Aa lava flows and identify pyroclastic hazards"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Earth's Pressure Cooker",
                        "content": {
                            "text": (
                                "When an eruptive vent opens, the Earth releases materials across all three states of matter: "
                                "superheated gases, incandescent molten liquids, and solid rocks blasted into the sky. "
                                "Let's explore this complete spectrum of volcanic ejecta!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Gaseous and Liquid Volcanic Materials",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Volcanic Gases & Lava Morphology",
                        "content": {
                            "text": (
                                "### 1. Volcanic Gases (Volatiles):\n"
                                "Over 70% to 90% of volcanic gas emissions consist of **superheated water vapor (steam)**. "
                                "The remaining gases include **carbon dioxide (CO2)**, **sulfur dioxide (SO2)**, **hydrogen sulfide (H2S)**, and chlorine gas.\n\n"
                                "### 2. Liquid Materials (Lava Surface Textures):\n"
                                "- **Pahoehoe Lava:** Highly fluid basaltic lava that cools with a smooth, ropy, satiny, or undulating surface crust.\n"
                                "- **Aa Lava:** More viscous basaltic lava that cools into rough, jagged, sharp, blocky, and spinose rubble."
                            )
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Pahoehoe vs Aa Lava",
                        "content": {
                            "term": "Pahoehoe & Aa",
                            "definition": "Hawaiian terms describing basaltic lava surface textures: Pahoehoe has a smooth ropy skin, whereas Aa has a jagged, sharp, blocky crust."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Solid Volcanic Materials (Pyroclasts / Tephra)",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Classification of Volcanic Ejecta by Size and Phase",
                        "content": {
                            "caption": "Grain-size scale diagram classifying Volcanic Dust/Ash (<2mm), Lapilli (2-64mm), Volcanic Blocks (>64mm), and Volcanic Bombs (>64mm)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Particle Size Hierarchy of Solid Pyroclasts",
                        "content": {
                            "text": (
                                "Solid fragments blown out by expanding gases are called **pyroclasts** (or **tephra**), classified by size:\n\n"
                                "1. **Volcanic Dust & Ash (< 2 mm):** Microscopic rock glass particles that can stay suspended in the upper atmosphere and travel thousands of kilometers.\n"
                                "2. **Lapilli / Cinders (2 mm – 64 mm):** Pea-sized to walnut-sized gravel fragments of hardened lava.\n"
                                "3. **Volcanic Blocks (> 64 mm, Angular):** Massive, sharp-edged angular blocks of pre-existing crustal rock blasted from the volcanic crater walls.\n"
                                "4. **Volcanic Bombs (> 64 mm, Aerodynamic):** Blobs of molten lava hurled into the air that spin, twist, and cool into aerodynamic, football-shaped rocks before striking the ground."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Context: Pumice & Obsidian at Olkaria",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Pumice and Obsidian Resources in Naivasha",
                        "content": {
                            "text": (
                                "The Olkaria and Mount Longonot volcanic complexes in Nakuru County contain massive industrial deposits of unique volcanic rocks:\n\n"
                                "- **Pumice:** A very light, frothy, porous volcanic rock formed when gas-rich felsic lava froths up and cools rapidly. Its high porosity allows it to float on water! Pumice is quarried extensively in Naivasha for lightweight building aggregates and stone-washing textiles.\n"
                                "- **Obsidian:** Natural black volcanic glass formed when high-silica lava chills instantly without crystal growth. Ancient humans in the Rift Valley used obsidian to fashion razor-sharp tools and arrowheads."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Volcanic Materials",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Volcanic Bombs",
                        "content": {
                            "question": "Aerodynamic, rounded blobs of molten lava that cool and solidify while flying through the air are called:",
                            "options": [
                                "Volcanic blocks",
                                "Volcanic bombs",
                                "Lapilli",
                                "Lahars"
                            ],
                            "correct_answer": "Volcanic bombs",
                            "explanation": "Volcanic bombs are thrown out as molten blobs that acquire smooth, aerodynamic, twisted shapes as they spin and cool through the air. Volcanic blocks are angular and were already solid when blasted."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Volcanic Gases & Acid Rain",
                        "content": {
                            "question": "Which gas released during volcanic eruptions is known to form acid rain when combined with atmospheric moisture?",
                            "options": [
                                "Water vapor",
                                "Carbon dioxide",
                                "Nitrogen gas",
                                "Sulfur dioxide"
                            ],
                            "correct_answer": "Sulfur dioxide",
                            "explanation": "Sulfur dioxide (SO2) reacts with atmospheric water and oxygen to produce sulfurous and sulfuric acids, precipitating as corrosive acid rain that harms ecosystems and metal structures."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Extrusive Landforms: Shield Volcanoes, Cinder Cones, and Lava Plateaus
    {
        "unit_order": 5,
        "unit_name": "Extrusive Landforms: Shield Volcanoes, Cinder Cones, and Lava Plateaus",
        "lesson_title": "Extrusive Landforms: Shield Volcanoes, Cinder Cones, and Lava Plateaus",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Extrusive Landforms & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Gentle Slopes of a Shield Volcano: Mauna Loa",
                        "content": {"text": "A wide-angle landscape photograph of basaltic lava fields spreading gently from the massive dome of Mauna Loa."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Shield Volcanoes, Cinder Cones & Plateaus",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Describe the formation and morphology of shield volcanoes, cinder cones, and lava plateaus\n"
                                "- Relate landform shape and slope gradient to eruption mechanics and lava fluidity\n"
                                "- Identify Kenyan examples: Yatta Plateau and Chyulu Hills cinder cones"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Water vs Thick Porridge",
                        "content": {
                            "text": (
                                "If you pour water onto a flat tray, it spreads out instantly into a wide, ultra-thin sheet. "
                                "If you dollop thick porridge, it piles up into a steep, rounded mound. "
                                "This fundamental experiment illustrates why fluid basic lava builds vast, gentle shield volcanoes and plateaus, "
                                "while loose solid cinders stack into steep, conical hills!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions of Key Extrusive Landforms",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Shield Volcano",
                        "content": {
                            "term": "Shield Volcano",
                            "definition": "A broad, gently sloping volcanic mountain built by successive flows of low-viscosity basic basaltic lava, resembling a warrior's shield lying face-up."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Cinder Cone (Scoria Cone)",
                        "content": {
                            "term": "Cinder Cone",
                            "definition": "A small, steep-sided, conical hill built exclusively of loose pyroclastic fragments (scoria, cinders, and ash) ejected from a single central vent."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Lava Plateau",
                        "content": {
                            "term": "Lava Plateau",
                            "definition": "An extensive, flat upland table formed by highly fluid basaltic lava erupting from long crustal fractures (fissures) and flooding wide areas."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Morphological Comparison & Structure",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Comparative Cross-Sections: Shield Volcano, Cinder Cone, Lava Plateau",
                        "content": {
                            "caption": "Cross-sectional comparison contrasting gentle shield basalt layers, steep cinder cone pyroclastic slopes, and fissure-fed flat lava plateaus."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Contrasting Volcanic Landforms",
                        "content": {
                            "text": (
                                "### 1. Shield Volcanoes:\n"
                                "- **Eruption Type:** Effusive, gentle lava fountains.\n"
                                "- **Slope Angle:** Very gentle (2° to 10°), with a wide base spanning hundreds of kilometers.\n"
                                "- **Global Example:** Mauna Loa & Kilauea in Hawaii.\n\n"
                                "### 2. Cinder Cones:\n"
                                "- **Eruption Type:** Explosive gas-driven ejection of scoria cinders.\n"
                                "- **Slope Angle:** Steep (30° to 40°), reaching the angle of repose for loose gravel.\n"
                                "- **Height:** Small, rarely exceeding 300 to 500 meters.\n\n"
                                "### 3. Lava Plateaus:\n"
                                "- **Eruption Type:** Quiet fissure eruptions through linear fault cracks.\n"
                                "- **Geometry:** Broad, horizontal basaltic plains thousands of square kilometers in extent."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Case Studies: Yatta Plateau & Chyulu Hills",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "The World's Longest Lava Flow: The Yatta Plateau",
                        "content": {
                            "text": (
                                "Kenya is home to remarkable global examples of these volcanic features:\n\n"
                                "- **The Yatta Plateau:** Stretches nearly 300 kilometers in eastern Kenya. It is the longest individual lava plateau ridge on Earth! It was formed when fluid phonolite lava flowed down an ancient river valley from Ol Donyo Sabuk. Over millions of years, the softer surrounding terrain eroded away, leaving the hard volcanic plateau standing high as an inverted relief ridge.\n"
                                "- **The Chyulu Hills:** A young volcanic range in southern Kenya consisting of hundreds of black basaltic cinder cones and vast lava tubes formed over the last few thousand years."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Extrusive Landforms",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Slopes of Shield Volcanoes",
                        "content": {
                            "question": "Why do shield volcanoes have exceptionally gentle slope gradients?",
                            "options": [
                                "Because they are built of highly viscous acidic lava that piles up.",
                                "Because they are built by successive layers of highly fluid basic basaltic lava that flows far before solidifying.",
                                "Because they are repeatedly eroded flat by glaciers.",
                                "Because they consist entirely of loose beach sand."
                            ],
                            "correct_answer": "Because they are built by successive layers of highly fluid basic basaltic lava that flows far before solidifying.",
                            "explanation": "Fluid basic lava has low viscosity and travels great distances over the ground. Consequently, the mountain expands outward horizontally rather than upward vertically, creating broad, gentle slopes."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Kenyan Lava Plateau",
                        "content": {
                            "question": "The Yatta Plateau in Kenya is a prime geological example of which volcanic landform?",
                            "options": [
                                "Shield Volcano",
                                "Cinder Cone",
                                "Composite Volcano",
                                "Lava Plateau"
                            ],
                            "correct_answer": "Lava Plateau",
                            "explanation": "The Yatta Plateau is an inverted relief lava plateau formed by fluid lava filling an ancient river valley, creating the world's longest linear lava plateau ridge."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Composite Volcanoes (Stratovolcanoes)
    {
        "unit_order": 6,
        "unit_name": "Composite Volcanoes (Stratovolcanoes)",
        "lesson_title": "Composite Volcanoes (Stratovolcanoes)",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Stratovolcanoes & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Imposing Summit of Mount Longonot",
                        "content": {"text": "A photograph showing the dramatic crater rim and steep gullied flanks of Mount Longonot composite volcano in Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Composite Volcanoes",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the formation, internal architecture, and characteristics of composite volcanoes (stratovolcanoes)\n"
                                "- Describe the alternating sequence of explosive ash and effusive lava eruptions\n"
                                "- Identify features of composite cones: central pipe, crater, parasitic cones, and dykes"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Majestic Mountain Giants",
                        "content": {
                            "text": (
                                "When you picture the iconic, snow-draped volcanic peaks in postcards—like Japan's Mount Fuji, "
                                "Tanzania's Mount Kilimanjaro, or Kenya's Mount Longonot—you are admiring a **Composite Volcano**! "
                                "These towering giants are constructed layer-by-layer over hundreds of thousands of years through a "
                                "dramatic history of alternating explosive ash explosions and flowing lava rivers."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & The Layer-Cake Structure",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Composite Volcano (Stratovolcano)",
                        "content": {
                            "term": "Composite Volcano",
                            "definition": "A large, steep-sided, symmetrical volcanic cone constructed of alternating layers (strata) of hardened lava flows, volcanic ash, cinders, and pyroclastic debris."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Parasitic Cone (Adventive Cone)",
                        "content": {
                            "term": "Parasitic Cone",
                            "definition": "A smaller secondary volcanic cone that forms on the flank or base of a larger volcano, fed by a side branch conduit originating from the main magma pipe."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Stratovolcano Internal Architecture",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Composite Volcano (Stratovolcano) Cross-Section",
                        "content": {
                            "caption": "Detailed cross-section illustrating alternating ash and lava strata, central conduit, magma chamber, parasitic flank cone, and feeder dykes."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "How the Alternating Layers Form",
                        "content": {
                            "text": (
                                "Stratovolcanoes grow through a repeating two-phase eruption cycle:\n\n"
                                "1. **Explosive Ash Phase:** Gas-rich magma explodes through the central vent, blasting ash, pumice, and cinders high into the atmosphere. These materials settle down around the cone, forming a loose, steep pyroclastic layer.\n"
                                "2. **Effusive Lava Phase:** As gas pressure subsides, viscous lava wells up and flows down the mountain slopes. This molten lava cements and armors the loose ash layer, preventing it from washing away during rains.\n"
                                "3. **Conduit Branching & Parasitic Cones:** As the central throat becomes clogged with solidified rock plugs, rising pressurized magma fractures the flank walls. Magma forces its way through side fissures (dykes), breaking out on the mountain side to build **parasitic cones**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Case Study: Mount Longonot",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Mount Longonot: A Classic Rift Valley Stratovolcano",
                        "content": {
                            "text": (
                                "Mount Longonot, located in the central Rift Valley south of Lake Naivasha, is a textbook young stratovolcano:\n\n"
                                "- Rising to an elevation of 2,776 meters, its steep slopes exhibit classic alternating strata of pumice ash, tuff, and trachyte lava flows.\n"
                                "- Its summit holds a massive, circular crater/caldera floor populated by a lush green forest.\n"
                                "- Active geothermal fumaroles (steam vents) along the inner crater walls prove that the underlying magma system is still dormant rather than extinct."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Stratovolcanoes",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Alternating Strata Formation",
                        "content": {
                            "question": "What causes a composite volcano to have alternating layers of ash and lava?",
                            "options": [
                                "The volcano freezes during winter and melts in summer.",
                                "It is built by alternating phases of explosive ash eruptions and effusive lava flows.",
                                "Dust blown by desert winds coats a shield volcano.",
                                "It erupts solely basic lava from fissure cracks."
                            ],
                            "correct_answer": "It is built by alternating phases of explosive ash eruptions and effusive lava flows.",
                            "explanation": "A composite volcano is termed 'composite' because its structure comprises alternating strata of loose ash/tephra (from explosive phases) and hardened lava flows (from effusive phases)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Parasitic Cone Origin",
                        "content": {
                            "question": "What is a 'parasitic cone' on a composite volcano?",
                            "options": [
                                "A rare type of plant growing on the volcano summit.",
                                "A deep depression formed by meteorite impact.",
                                "A secondary volcanic cone that forms on the flank of a larger volcano fed by a side conduit.",
                                "An underground cave containing acidic water."
                            ],
                            "correct_answer": "A secondary volcanic cone that forms on the flank of a larger volcano fed by a side conduit.",
                            "explanation": "When the main central vent of a volcano becomes obstructed, pressurized magma escapes through lateral fractures to erupt on the flanks, forming a smaller secondary (parasitic) cone."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Craters, Calderas, and Caldera Lakes
    {
        "unit_order": 7,
        "unit_name": "Craters, Calderas, and Caldera Lakes",
        "lesson_title": "Craters, Calderas, and Caldera Lakes",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Craters and Calderas & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Vast Basin of Menengai Caldera",
                        "content": {"text": "A panoramic viewpoint photograph overlooking the colossal caldera floor and steep ring walls of Menengai near Nakuru."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Craters, Calderas & Lakes",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Differentiate between craters and calderas by scale and mechanism of formation\n"
                                "- Explain the step-by-step collapse sequence forming a caldera\n"
                                "- Describe caldera lakes and identify Kenyan examples (Menengai Caldera and Lake Simbi)"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Collapsing Soufflé",
                        "content": {
                            "text": (
                                "Imagine baking a large hollow soufflé or cake. If you scoop out the hot filling inside, "
                                "the heavy top crust has no support and suddenly caves in, leaving a wide, steep-sided basin. "
                                "This is precisely how calderas form! When a gigantic eruption empties a subsurface magma chamber, "
                                "the unsupported mountain summit collapses inward along circular ring faults!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Crater vs Caldera",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Crater",
                        "content": {
                            "term": "Crater",
                            "definition": "A relatively small, funnel-shaped depression (typically less than 1 km in diameter) at the top of a volcanic vent formed by explosive blasting of rock."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Caldera",
                        "content": {
                            "term": "Caldera",
                            "definition": "A massive, basin-shaped volcanic depression (often multiple kilometers wide) formed by the inward structural collapse of a volcano's summit into an emptied magma chamber."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Caldera Lake",
                        "content": {
                            "term": "Caldera Lake",
                            "definition": "A deep body of water that accumulates inside a caldera basin when rainfall and groundwater collect on the impermeable volcanic floor."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Step-by-Step Caldera Collapse Sequence",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Three-Stage Caldera Collapse Sequence",
                        "content": {
                            "caption": "Step-by-step sequence: 1) Cataclysmic explosive eruption empties magma chamber; 2) Summit collapses inward along ring faults; 3) Caldera basin fills with water to form a caldera lake."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Stages of Caldera Formation",
                        "content": {
                            "text": (
                                "Calderas are formed through a dramatic structural sequence:\n\n"
                                "1. **Chamber Inflation:** A massive shallow magma chamber fills with gas-rich, highly viscous acidic magma, causing the mountain above to bulge.\n"
                                "2. **Climactic Eruption:** A colossal explosive eruption blasts cubic kilometers of magma out as pyroclastic flows and ash, rapidly evacuating the magma chamber.\n"
                                "3. **Structural Collapse:** Deprived of internal magmatic support, the colossal weight of the volcano summit causes the roof rocks to collapse downward along concentric ring faults.\n"
                                "4. **Caldera Lake Formation:** The resulting wide, flat-bottomed depression collects rainwater and runoff, forming a picturesque **caldera lake** (such as Lake Simbi in Kenya or Crater Lake in Oregon)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Case Studies: Menengai Caldera & Lake Simbi",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Menengai: One of Earth's Largest Calderas",
                        "content": {
                            "text": (
                                "Kenya hosts extraordinary caldera structures:\n\n"
                                "- **Menengai Caldera (Nakuru):** One of the largest preserved calderas in the world. It spans 90 square kilometers with vertical caldera walls plunging up to 500 meters down to the flat floor. The caldera collapsed approximately 29,000 years ago.\n"
                                "- **Lake Simbi (Homa Bay County):** A volcanic maar/crater lake formed by a violent phreatic (steam) explosion when underground water contacted shallow magma. The dense green alkaline lake is famous for visiting flocks of lesser flamingos."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Calderas & Craters",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Primary Mechanism of Caldera Formation",
                        "content": {
                            "question": "The primary geological mechanism behind the formation of a caldera is:",
                            "options": [
                                "Heavy wind erosion scouring out a volcanic vent.",
                                "The inward structural collapse of a volcano summit into an emptied magma chamber.",
                                "A meteorite impact crashing into the top of an active volcano.",
                                "Chemical dissolution of rocks by underground sulfuric acid."
                            ],
                            "correct_answer": "The inward structural collapse of a volcano summit into an emptied magma chamber.",
                            "explanation": "Calderas are collapse depressions. When an enormous eruption rapidly drains the underlying magma chamber, the overlying mountain summit loses structural support and collapses along ring fractures."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Crater vs Caldera Distinction",
                        "content": {
                            "question": "How does a crater differ from a caldera?",
                            "options": [
                                "A crater is much larger than a caldera.",
                                "A crater is formed by lava deposition, while a caldera is formed by wind.",
                                "A crater is a small funnel-shaped vent depression, while a caldera is a massive basin formed by summit collapse.",
                                "A crater is always filled with ocean water, while a caldera is always dry."
                            ],
                            "correct_answer": "A crater is a small funnel-shaped vent depression, while a caldera is a massive basin formed by summit collapse.",
                            "explanation": "Craters are relatively small (usually <1km) vent features carved by explosive blasting. Calderas are vast collapse basins spanning multiple kilometers."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Geysers and Hot Springs
    {
        "unit_order": 8,
        "unit_name": "Geysers and Hot Springs",
        "lesson_title": "Geysers and Hot Springs",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geysers and Hot Springs & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Boiling Hydrothermal Geyser at Lake Bogoria",
                        "content": {"text": "A photograph showing active geysers shooting boiling water and steam columns on the mineral-crusted shores of Lake Bogoria, Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Geysers and Hot Springs",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Differentiate between continuous hot springs and intermittent geysers\n"
                                "- Explain the physics of water superheating under pressure in narrow conduits\n"
                                "- Detail the thermodynamics of geyser eruptions and identify Lake Bogoria hydrothermal systems"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Pressure Whistle Kettle",
                        "content": {
                            "text": (
                                "If you boil water in a tightly sealed whistle kettle, steam cannot escape freely. "
                                "Pressure builds up until steam and boiling water blast violently through the narrow spout! "
                                "Deep inside volcanic terrain, subterranean plumbing channels operate on this exact thermodynamic principle, "
                                "generating majestic geysers that shoot boiling water tens of meters into the air!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Hydrothermal Systems: Hot Springs vs Geysers",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Hot Spring (Thermal Spring)",
                        "content": {
                            "term": "Hot Spring",
                            "definition": "A natural spring where groundwater heated by geothermal energy from deep crustal magma flows quietly and continuously onto the surface."
                        }
                    },
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Geyser",
                        "content": {
                            "term": "Geyser",
                            "definition": "An intermittent hydrothermal vent that periodically erupts a turbulent column of superheated water and pressurized steam through a restricted underground conduit."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Geyser Plumbing Physics & Eruption Thermodynamics",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Hydrothermal Geyser Plumbing and Eruption Cycle",
                        "content": {
                            "caption": "Thermodynamic stages: 1) Deep groundwater superheats under pressure; 2) Steam expansion pushes surface water overflow; 3) Sudden pressure drop causes instantaneous steam flash eruption."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Thermodynamic Phases of a Geyser Eruption",
                        "content": {
                            "text": (
                                "Geysers require three conditions: an abundant water supply, an intense magmatic heat source, and a **constricted underground plumbing system**.\n\n"
                                "1. **Groundwater Infiltration:** Cold surface water seeps deep into twisted vertical fissures near a hot magma body.\n"
                                "2. **Superheating Under Pressure:** The weight of the overlying water column exerts enormous hydrostatic pressure at the bottom. This elevates the boiling point of the deep water well above 100°C (up to 150°C) without boiling.\n"
                                "3. **Steam Bubble Expansion:** As heat continues to rise, the deepest water finally begins to boil. Expanding steam bubbles push some water out of the vent at the surface.\n"
                                "4. **Pressure Drop & Steam Flash:** The overflow of water reduces the weight of the water column. The sudden drop in hydrostatic pressure causes the deep superheated water to flash instantly into steam (expanding 1,600 times in volume), blasting a towering jet of boiling water into the sky!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Case Study: Lake Bogoria Geysers",
                "blocks": [
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "The Natural Fountains of Lake Bogoria",
                        "content": {
                            "text": (
                                "The western shores of **Lake Bogoria** in Baringo County, Kenya, host the most spectacular concentration of geysers and boiling springs in Africa:\n\n"
                                "- Lake Bogoria features over a dozen active geysers that erupt boiling mineral-rich water up to 5 meters into the air at regular intervals.\n"
                                "- The water temperature exceeds 98°C, hot enough to boil eggs in minutes!\n"
                                "- The intense hydrothermal activity is sustained by active tectonic faults and shallow magma chambers associated with the Gregory Rift system."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Geysers & Hot Springs",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Intermittent Eruption Mechanics",
                        "content": {
                            "question": "Why does a geyser erupt intermittently rather than flowing continuously like a standard hot spring?",
                            "options": [
                                "Magma deep underground cools down and reheats every few minutes.",
                                "It has a narrow, restricted plumbing channel where pressure and superheated steam build up before blasting.",
                                "Wind continuously blocks and unblocks the vent opening.",
                                "It is driven strictly by the tidal pull of the Moon."
                            ],
                            "correct_answer": "It has a narrow, restricted plumbing channel where pressure and superheated steam build up before blasting.",
                            "explanation": "Geysers have constricted underground conduits that trap water and prevent free convection. Pressure builds, superheating the water until steam expands, drops the pressure, and triggers a flash eruption. Hot springs have open, unrestricted channels that flow continuously."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Superheated Water Concept",
                        "content": {
                            "question": "Superheated water in a volcanic geyser system is water that:",
                            "options": [
                                "Has frozen into ice under high pressure.",
                                "Is heated past 100°C while remaining liquid because of high confining pressure.",
                                "Has lost all of its hydrogen and oxygen atoms.",
                                "Erupts only in sub-zero polar climates."
                            ],
                            "correct_answer": "Is heated past 100°C while remaining liquid because of high confining pressure.",
                            "explanation": "High confining pressure from the overlying water column raises the boiling point, allowing liquid water to reach temperatures above 100°C without converting to steam until pressure is released."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Global Distribution of Volcanic Features
    {
        "unit_order": 9,
        "unit_name": "Global Distribution of Volcanic Features",
        "lesson_title": "Global Distribution of Volcanic Features",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Global Volcanic Belts & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Submarine Volcano in the Pacific Ring of Fire",
                        "content": {"text": "A photograph showing active underwater volcanic hydrothermal plumes and tectonic fissures along the Pacific Ring of Fire."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Global Volcanic Distribution",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Locate the three primary global volcanic belts: Pacific Ring of Fire, Mid-Ocean Ridges, and Continental Rifts\n"
                                "- Correlate volcanic activity with convergent, divergent, and intra-plate hotspot tectonic boundaries\n"
                                "- Explain why Iceland and the East African Rift are globally significant volcanic zones"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Restless Ring of Fire",
                        "content": {
                            "text": (
                                "Volcanoes are not scattered randomly across the globe. Over 75% of Earth's active volcanoes "
                                "encircle the rim of a single ocean basin in a deadly, horseshoe-shaped belt known as the **Pacific Ring of Fire**! "
                                "Let's investigate how the movements of giant tectonic plates dictate where volcanoes are born."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Three Major Global Volcanic Belts",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Primary Volcanic Belts of the Earth",
                        "content": {
                            "text": (
                                "Volcanic activity is concentrated in three main geological zones:\n\n"
                                "1. **The Pacific Ring of Fire (Circum-Pacific Belt):** A 40,000-kilometer horseshoe-shaped zone encircling the Pacific Plate. It contains over 450 active volcanoes (including Mt. Fuji, Mt. Pinatubo, Krakatoa) formed by oceanic subduction zones.\n"
                                "2. **Mid-Ocean Ridges (Divergent Ocean Belts):** The longest volcanic chain on Earth, running along the sea floor (such as the Mid-Atlantic Ridge). Here, tectonic plates pull apart and basaltic lava erupts along fissures. Iceland is a rare location where this mid-ocean ridge rises above sea level!\n"
                                "3. **Continental Rift Zones & Hotspots:** Active continental breakup zones like the **East African Rift System**, and intraplate mantle plumes like Hawaii and Yellowstone."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Global Volcanic Belts & Plate Tectonics Map",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Pacific Ring of Fire and Global Volcanic Belts Map",
                        "content": {
                            "caption": "World map illustrating the Pacific Ring of Fire, Mid-Atlantic Ridge, East African Rift, and major mantle hotspot locations."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Tectonic Plate Boundaries and Volcano Types",
                        "content": {
                            "text": (
                                "- **Subduction Zones (Ring of Fire):** Yield viscous, gas-rich acidic/andesitic magma, producing violent composite stratovolcanoes and calderas.\n"
                                "- **Divergent Ridges (Mid-Atlantic & East Africa):** Yield fluid basic basaltic magma, producing gentle shield volcanoes, fissure eruptions, and lava plateaus.\n"
                                "- **Intraplate Hotspots (Hawaii):** Stationary thermal plumes melting through moving oceanic lithosphere, forming chains of shield volcanoes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Global Volcanic Belts",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Pacific Ring of Fire",
                        "content": {
                            "question": "Which global region contains over 75% of the world's active volcanoes and is formed primarily by subduction zones?",
                            "options": [
                                "The East African Rift Valley",
                                "The Mid-Atlantic Ridge",
                                "The Pacific Ring of Fire",
                                "The Deccan Traps"
                            ],
                            "correct_answer": "The Pacific Ring of Fire",
                            "explanation": "The Pacific Ring of Fire is a horseshoe-shaped belt surrounding the Pacific Plate where oceanic plates subduct beneath continental plates, generating over three-quarters of Earth's active volcanoes."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Iceland's Unique Setting",
                        "content": {
                            "question": "Iceland is a unique volcanic island because it sits directly on top of which tectonic feature?",
                            "options": [
                                "The Pacific Ring of Fire subduction zone",
                                "The Mid-Atlantic Ridge (a divergent boundary)",
                                "The Himalayan continental collision zone",
                                "The San Andreas transform fault"
                            ],
                            "correct_answer": "The Mid-Atlantic Ridge (a divergent boundary)",
                            "explanation": "Iceland is located on the Mid-Atlantic Ridge where the North American and Eurasian plates diverge, making it one of the rare places where a mid-ocean divergent boundary is exposed on land."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Vulcanicity in Kenya: Distribution and Landscape
    {
        "unit_order": 10,
        "unit_name": "Vulcanicity in Kenya: Distribution and Landscape",
        "lesson_title": "Vulcanicity in Kenya: Distribution and Landscape",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Volcanic Landscapes of Kenya & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Batian and Nelion: The Eroded Volcanic Plug of Mt. Kenya",
                        "content": {"text": "A photograph showing the sharp, jagged rocky peaks of Batian and Nelion on Mount Kenya rising above glaciers and alpine valleys."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Vulcanicity in Kenya",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify Kenyan volcanoes into active, dormant, and extinct categories\n"
                                "- Map the geographic distribution of volcanic landforms across the Kenyan Rift Valley and Highlands\n"
                                "- Describe the landscape features of Mt. Kenya, Mt. Elgon, Mt. Longonot, Menengai Caldera, and Chyulu Hills"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Standing on Volcanic Ground",
                        "content": {
                            "text": (
                                "If you travel across central and western Kenya, almost every landmark you see—from the "
                                "fertile red soils of Kiambu, to the black rocks of Nairobi, to the cliffs of the Rift Valley—was "
                                "shaped by volcanoes! Kenya's capital, Nairobi, sits on the edge of expansive volcanic plains "
                                "built from dark phonolite lava. Let's trace how vulcanicity sculpted our homeland."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Classification: Active, Dormant & Extinct Volcanoes",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Active, Dormant, and Extinct Volcanoes",
                        "content": {
                            "term": "Volcano Life Stages",
                            "definition": "Active volcanoes have erupted in recorded history and show current activity; Dormant volcanoes are currently quiet but have potential to erupt; Extinct volcanoes have not erupted in thousands of years and have no magma supply."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Key Kenyan Volcanic Landforms",
                        "content": {
                            "text": (
                                "### 1. Extinct Volcanoes:\n"
                                "- **Mount Kenya:** Extinct stratovolcano; original cone eroded away leaving towering volcanic plugs (Batian, Nelion).\n"
                                "- **Mount Elgon:** Ancient extinct shield volcano on the Uganda border with a massive summit caldera and expansive caves.\n\n"
                                "### 2. Dormant Volcanoes:\n"
                                "- **Mount Longonot & Menengai Caldera:** Dormant volcanoes with active fumaroles and steam vents.\n"
                                "- **Mount Suswa:** Unique double-caldera shield volcano with subterranean lava tube networks.\n\n"
                                "### 3. Young & Active Volcanic Fields:\n"
                                "- **Chyulu Hills (including Shaitani Cone):** Black basaltic cinder cones formed within the last few hundred years.\n"
                                "- **Olkaria Volcanic Complex:** Active geothermal system with obsidian flows and boiling fumaroles."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Volcanic Landscapes & Distribution of Kenya",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Geographic Distribution of Volcanic Landforms in Kenya",
                        "content": {
                            "caption": "Map of Kenya highlighting the Great Rift Valley fault boundary, Mt. Kenya, Mt. Elgon, Mt. Longonot, Menengai Caldera, Chyulu Hills, Olkaria, and Lake Simbi."
                        }
                    },
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Tectonic Control on Kenyan Volcanism",
                        "content": {
                            "text": (
                                "Notice that over 90% of Kenya's volcanic features lie along the floor or margins of the Great Rift Valley. "
                                "The crustal tension and thinning that opened the rift created deep fault fractures, "
                                "providing pathways for magma to rise and erupt, forming the volcanic highlands that define Kenya's climate and economy."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Kenyan Vulcanicity",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Classification of Mount Kenya",
                        "content": {
                            "question": "Mount Kenya is classified as an **extinct** volcano because:",
                            "options": [
                                "It continues to erupt molten lava every year.",
                                "It has no historical record of eruption and its central conduit has cooled, hardened, and been deeply eroded over millions of years.",
                                "It was completely flattened by tectonic faulting.",
                                "It is composed entirely of sedimentary limestone."
                            ],
                            "correct_answer": "It has no historical record of eruption and its central conduit has cooled, hardened, and been deeply eroded over millions of years.",
                            "explanation": "Mount Kenya is extinct because it has been inactive for over 2 million years, with glacial erosion exposing its core volcanic plug (Batian and Nelion)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Chyulu Hills Cinder Field",
                        "content": {
                            "question": "Which young volcanic range in southern Kenya is composed of hundreds of black basaltic cinder cones and includes the active 'Shaitani' cone?",
                            "options": [
                                "Mount Elgon",
                                "Mount Longonot",
                                "Chyulu Hills",
                                "Aberdare Range"
                            ],
                            "correct_answer": "Chyulu Hills",
                            "explanation": "The Chyulu Hills are a geologically young volcanic range composed of hundreds of cinder cones and lava flows, including the historic Shaitani cone which erupted in the 19th century."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Benefits of Vulcanicity to Human Activities
    {
        "unit_order": 11,
        "unit_name": "Benefits of Vulcanicity to Human Activities",
        "lesson_title": "Benefits of Vulcanicity to Human Activities",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Economic Benefits & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Olkaria Geothermal Power Station V",
                        "content": {"text": "A photograph showing the massive modern industrial cooling towers and steam transmission pipelines of Olkaria Geothermal Power Station in Naivasha, Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Benefits of Vulcanicity",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Analyze the economic advantages of vulcanicity to agriculture, energy, tourism, and construction\n"
                                "- Explain how geothermal energy is harnessed from volcanic steam at Olkaria\n"
                                "- Evaluate the role of mineral-rich volcanic soils in supporting Kenya's tea and coffee farming"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Engine of Kenyan Prosperity",
                        "content": {
                            "text": (
                                "We often view volcanoes as destructive hazards. However, did you know that volcanic fields "
                                "produce over 40% of Kenya's electricity? And that Kenya's world-famous export tea and coffee "
                                "thrive on fertile volcanic soils? Volcanoes are true engines of wealth for our nation!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Four Pillars of Volcanic Wealth",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Economic Value of Volcanic Systems",
                        "content": {
                            "text": (
                                "### 1. Fertile Agricultural Soils (Andosols):\n"
                                "Weathering of volcanic rocks (basalt, phonolite, tuff) releases essential plant nutrients including potassium, phosphorus, calcium, and magnesium. These deep, well-drained volcanic soils support intensive tea, coffee, and horticulture in Central Kenya and the Rift Valley.\n\n"
                                "### 2. Clean Renewable Geothermal Energy:\n"
                                "Deep underground water is superheated by magma bodies. By drilling wells up to 3,000 meters deep, pressurized steam is piped to turbines to generate clean electricity (e.g. Olkaria, Eburru, Menengai).\n\n"
                                "### 3. Thriving Tourism Industry:\n"
                                "Volcanic scenery draws hundreds of thousands of international tourists to Mount Kenya, Hell's Gate, Mount Longonot, and Lake Bogoria geysers, generating vital foreign exchange.\n\n"
                                "### 4. Mineral & Construction Materials:\n"
                                "- **Ballast & Building Stone:** Crushed basalt and phonolite for roads and buildings.\n"
                                "- **Tuff:** Easily quarried volcanic stone for housing blocks.\n"
                                "- **Pumice:** Lightweight aggregate and textile processing."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Olkaria Geothermal Power Generation Cycle",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Olkaria Geothermal Power Generation Process",
                        "content": {
                            "caption": "Engineering flow diagram: Deep production wells tap high-pressure steam from magma-heated aquifer -> Steam-water separator -> Steam turbine and generator produce electricity -> Cooling tower and reinjection well recycle water sustainably."
                        }
                    },
                    {
                        "block_type": "case_study",
                        "component_type": "case_study",
                        "title": "Kenya: Global Leader in Geothermal Energy",
                        "content": {
                            "text": (
                                "Kenya ranks among the top 10 geothermal energy producers in the world! "
                                "The Olkaria Geothermal Complex in Hell's Gate National Park generates over 800 MW of clean, baseload electricity. "
                                "Because geothermal power is unaffected by droughts, it provides stability to Kenya's national electrical grid."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Volcanic Benefits",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Geothermal Energy in Kenya",
                        "content": {
                            "question": "Which clean, renewable energy source is generated in Kenya by drilling deep wells to tap underground volcanic steam?",
                            "options": [
                                "Hydroelectric power (HEP)",
                                "Geothermal energy",
                                "Solar photovoltaic energy",
                                "Coal thermal power"
                            ],
                            "correct_answer": "Geothermal energy",
                            "explanation": "Geothermal power harnesses the natural heat of magma systems deep underground to generate steam and spin electric turbines. Kenya's major facility is at Olkaria, Naivasha."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Volcanic Agricultural Productivity",
                        "content": {
                            "question": "Why are the highlands of Central Kenya and the Rift Valley slopes so highly productive for tea and coffee farming?",
                            "options": [
                                "They are flat desert plains.",
                                "They consist of weathered, mineral-rich volcanic soils (Andosols) that are exceptionally fertile.",
                                "They are coated with solid impermeable volcanic glass.",
                                "They receive zero annual rainfall."
                            ],
                            "correct_answer": "They consist of weathered, mineral-rich volcanic soils (Andosols) that are exceptionally fertile.",
                            "explanation": "Weathering of volcanic rocks releases essential minerals like potassium, magnesium, and iron into deep, well-drained volcanic soils that are ideal for cash crops like tea and coffee."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: Hazards and Environmental Effects of Vulcanicity
    {
        "unit_order": 12,
        "unit_name": "Hazards and Environmental Effects of Vulcanicity",
        "lesson_title": "Hazards and Environmental Effects of Vulcanicity",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Volcanic Hazards & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Explosive Ash Plume and Eruption Column",
                        "content": {"text": "A photograph showing an explosive volcanic eruption with a towering gray ash column rising kilometers into the atmosphere."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Volcanic Hazards & Environment",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify primary volcanic hazards: pyroclastic flows, lava flows, ash falls, and toxic gas emissions\n"
                                "- Explain secondary hazards including lahars (volcanic mudflows) and acid rain\n"
                                "- Analyze how sulfur dioxide aerosols in the stratosphere trigger global climate cooling"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Most Violent Earth Hazard",
                        "content": {
                            "text": (
                                "While volcanoes provide fertile soils and clean energy, an active eruption is one of the most "
                                "destructive phenomena in nature. Superheated avalanches of ash moving faster than race cars "
                                "can incinerate cities in minutes. Let's examine the mechanisms of volcanic hazards and how they affect our planet."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Primary Hazards: Pyroclastic Flows & Lava",
                "blocks": [
                    {
                        "block_type": "definition",
                        "component_type": "definition",
                        "title": "Pyroclastic Flow (Nuée Ardente)",
                        "content": {
                            "term": "Pyroclastic Flow",
                            "definition": "A lethal, superheated (up to 1,000°C) avalanche of volcanic gas, ash, pumice, and rock fragments that races down a volcano's slopes at speeds exceeding 100 to 700 km/h."
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "Destructive Power of Pyroclastic Flows",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=Cvjwt9nnwXY",
                            "caption": "Educational documentary footage illustrating the speed, superheated temperature, and destructive power of volcanic pyroclastic density currents."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Primary Volcanic Eruption Hazards",
                        "content": {
                            "text": (
                                "1. **Pyroclastic Flows:** The deadliest volcanic hazard; leaves zero chance of survival due to extreme heat and speed.\n"
                                "2. **Lava Flows:** Molten rock streams; while usually slow enough for humans to evacuate, they bury farmlands, roads, and settlements under solid rock.\n"
                                "3. **Ash Falls:** Fine glass shards that cause respiratory illness, collapse roofs under heavy accumulation, contaminate water supplies, and choke jet aircraft engines.\n"
                                "4. **Toxic Gases:** Heavy gases like carbon dioxide (CO2) can pool in valleys, suffocating livestock and humans; sulfur dioxide (SO2) causes acute respiratory distress and acid rain."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Secondary Hazards & Atmospheric Climate Impacts",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Volcanic Hazards Matrix and Climate Impact Dispersion",
                        "content": {
                            "caption": "System diagram illustrating primary hazards (pyroclastic flows, lava), secondary hazards (lahars, acid rain), and stratospheric SO2 aerosols reflecting solar radiation to cause global cooling."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Lahars & Volcanic Climate Cooling",
                        "content": {
                            "text": (
                                "### 1. Lahars (Volcanic Mudflows):\n"
                                "When volcanic ash mixes with melting snow, crater lake water, or torrential rain, it creates a fast-moving, high-density slurry resembling wet liquid concrete. Lahars rush down river valleys, burying towns kilometers from the volcano.\n\n"
                                "### 2. Global Climate Cooling:\n"
                                "Massive explosive eruptions inject millions of tons of **sulfur dioxide (SO2)** directly into the stratosphere. SO2 reacts with water vapor to form microscopic sulfuric acid aerosol droplets. These reflective aerosols act like a giant solar shield, reflecting incoming solar radiation back into space and lowering global average surface temperatures for 1 to 3 years!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment: Hazards & Climate",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Superheated Pyroclastic Flows",
                        "content": {
                            "question": "A superheated, fast-moving avalanche of gas, ash, and rock fragments that rushes down a volcano's slopes is called a:",
                            "options": [
                                "Lava flow",
                                "Lahar",
                                "Pyroclastic flow",
                                "Geyser"
                            ],
                            "correct_answer": "Pyroclastic flow",
                            "explanation": "Pyroclastic flows (nuées ardentes) are superheated (up to 1,000°C) mixtures of gas and ash moving at immense velocity, representing the most lethal of all volcanic hazards."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Volcanic Mechanism of Global Cooling",
                        "content": {
                            "question": "How can massive volcanic eruptions trigger temporary global cooling?",
                            "options": [
                                "By releasing cold glacier meltwater onto land.",
                                "Volcanic ash permanently blocks all wind across the planet.",
                                "Sulfur dioxide aerosols injected into the stratosphere reflect incoming solar radiation back into space.",
                                "By absorbing oxygen from the ozone layer."
                            ],
                            "correct_answer": "Sulfur dioxide aerosols injected into the stratosphere reflect incoming solar radiation back into space.",
                            "explanation": "Sulfur dioxide in the stratosphere converts to highly reflective sulfate aerosol droplets that bounce incoming sunlight back into space, reducing global surface temperatures."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 13: Disaster Preparedness and Volcanic Simulation
    {
        "unit_order": 13,
        "unit_name": "Disaster Preparedness and Volcanic Simulation",
        "lesson_title": "Disaster Preparedness and Volcanic Simulation",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Disaster Preparedness & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Volcanic Seismograph Monitoring Station",
                        "content": {"text": "A photograph showing scientific seismic recording instruments and monitoring drum displays in a volcano observatory."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Preparedness & Volcanic Simulation",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Formulate volcanic disaster management and risk mitigation strategies\n"
                                "- Explain the role of scientific instruments (seismographs, tiltmeters, gas spectrometers) in early warning\n"
                                "- Conduct and explain a practical classroom volcanic simulation using safe chemical reactions"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Surviving Nature's Fury",
                        "content": {
                            "text": (
                                "We cannot stop a volcano from erupting, but with modern scientific monitoring, "
                                "hazard mapping, and disciplined evacuation protocols, communities can evacuate before tragedy strikes. "
                                "Let's discover how vulcanologists monitor active volcanoes and test our understanding with a laboratory simulation!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Volcanic Disaster Monitoring & Management",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Scientific Monitoring & Early Warning Systems",
                        "content": {
                            "text": (
                                "Vulcanologists utilize a triad of scientific monitoring techniques:\n\n"
                                "1. **Seismic Monitoring (Seismographs):** Rising magma fractures host rocks, creating characteristic high-frequency harmonic tremors that warn of impending eruption days or weeks in advance.\n"
                                "2. **Ground Deformation (Tiltmeters & GPS):** As magma chambers inflate, the volcano's slopes swell and tilt outward. Electronic tiltmeters detect slope changes as small as one millimeter!\n"
                                "3. **Gas Geochemistry (Spectrometers):** An abrupt surge in sulfur dioxide (SO2) and carbon dioxide (CO2) emission rates indicates fresh magma degassing close to the surface.\n"
                                "4. **Hazard Zonation Mapping:** Delineating high-risk red zones (for lahars and pyroclastic flows) to restrict settlement and plan emergency evacuation routes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Volcanic Hazard Early Warning & Evacuation Matrix",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Volcanic Early Warning System and Evacuation Protocol",
                        "content": {
                            "caption": "Four-tier alert status matrix: Green (Normal/Baseline) -> Yellow (Advisory/Elevated Seismicity) -> Orange (Watch/Ground Swelling & Gas Spikes) -> Red (Warning/Immediate Evacuation of Hazard Zones)."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Hands-On Practical: Volcanic Eruption Simulation",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Classroom Volcano Experiment: Baking Soda & Vinegar",
                        "content": {
                            "text": (
                                "### Practical Activity: Chemical Eruption Model\n\n"
                                "#### Materials Needed:\n"
                                "- Small plastic bottle (e.g., 250 ml)\n"
                                "- Modeling clay or sand on a large plastic tray\n"
                                "- Baking soda (Sodium Bicarbonate, NaHCO3) — 2 tablespoons\n"
                                "- Liquid dishwashing soap — 1 tablespoon\n"
                                "- Red food coloring — 5 drops\n"
                                "- Vinegar (Dilute Acetic Acid, CH3COOH) — 1/2 cup\n\n"
                                "#### Step-by-Step Procedure:\n"
                                "1. Place the bottle in the center of the tray and build a conical volcano of clay or sand around it, keeping the top bottle opening exposed as the crater vent.\n"
                                "2. Add 2 tablespoons of baking soda, 1 tablespoon of dish soap, and 5 drops of red food coloring into the bottle.\n"
                                "3. Quickly pour 1/2 cup of vinegar into the bottle.\n"
                                "4. **Observation:** A frothy, foaming red 'lava' immediately surges out of the vent and streams down the clay flanks!\n\n"
                                "#### Geographical Science Connection:\n"
                                "The acid-base chemical reaction between vinegar and baking soda rapidly generates **carbon dioxide (CO2)** gas. "
                                "Trapped by the dish soap, the gas expands explosively and builds pressure, driving the liquid foam up and out of the vent. "
                                "This accurately models how dissolved expanding gases in real magma chambers power volcanic eruptions!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Formative Assessment: Preparedness & Simulation",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 1: Ground Deformation Monitoring",
                        "content": {
                            "question": "Which scientific instrument is used by vulcanologists to measure the subtle swelling or inflation of a volcano's slopes as magma ascends?",
                            "options": [
                                "Seismograph",
                                "Anemometer",
                                "Tiltmeter",
                                "Barometer"
                            ],
                            "correct_answer": "Tiltmeter",
                            "explanation": "A tiltmeter measures tiny changes in the slope angle of a volcano, enabling scientists to detect ground inflation as magma fills the shallow magma chamber."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Question 2: Simulation Gas Dynamics",
                        "content": {
                            "question": "In the classroom volcanic simulation, what accurately models the expanding volcanic gases that push magma out of a real volcanic vent?",
                            "options": [
                                "The red food coloring dye.",
                                "The carbon dioxide gas bubbles produced by the chemical reaction between vinegar and baking soda.",
                                "The sand used to sculpt the cone.",
                                "The plastic tray catching the foam runoff."
                            ],
                            "correct_answer": "The carbon dioxide gas bubbles produced by the chemical reaction between vinegar and baking soda.",
                            "explanation": "The rapidly expanding carbon dioxide gas generated by the acid-carbonate reaction builds pressure and propels the foam outward, directly demonstrating how dissolved volcanic gases drive real volcanic eruptions."
                        }
                    }
                ]
            }
        ]
    }
]

# =============================================================================
# INGESTION RUNNER
# =============================================================================
def run_ingestion():
    print("=" * 80)
    print("STARTING VLEARN INGESTION: GRADE 10 GEOGRAPHY TOPIC 8 (VULCANICITY)")
    print("=" * 80)

    with transaction.atomic():
        curriculum, _ = Curriculum.objects.get_or_create(
            name="CBC",
            defaults={"country": "Kenya", "description": "Competency-Based Curriculum"}
        )
        grade, _ = Grade.objects.get_or_create(
            curriculum=curriculum,
            name="CBC - Grade 10",
            defaults={"level": 10}
        )
        subject, _ = Subject.objects.get_or_create(
            id=37,
            defaults={"name": "Geography", "grade": grade}
        )
        if subject.grade != grade or subject.name != "Geography":
            subject.grade = grade
            subject.name = "Geography"
            subject.save()

        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=8,
            defaults={
                "name": "Vulcanicity",
                "description": "Strand 2.0: Natural Systems and Processes - Topic 8: Vulcanicity"
            }
        )
        topic.name = "Vulcanicity"
        topic.description = "Strand 2.0: Natural Systems and Processes - Topic 8: Vulcanicity"
        topic.save()

        print(f"Target Topic: [{topic.id}] Order {topic.order}: {topic.name} under Subject: {subject.name} (Grade 10 CBC)")

        total_blocks_created = 0

        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            les_title = clean_text(les_data["lesson_title"])

            unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning unit for {u_name}"}
            )
            unit.name = u_name
            unit.save()

            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": les_title,
                    "status": "published",
                    "version": 1
                }
            )
            lesson.title = les_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            # Clear existing blocks for idempotency
            lesson.blocks.all().delete()

            block_seq = 1
            for page in les_data["pages"]:
                p_num = page["page_number"]
                p_title = clean_text(page["page_title"])

                for comp_order, blk in enumerate(page["blocks"], start=1):
                    b_type = blk["block_type"]
                    c_type = blk.get("component_type", b_type)
                    b_title = clean_text(blk.get("title", p_title))
                    b_content = clean_content_dict(blk.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        page_title=p_title,
                        order=block_seq,
                        component_order=comp_order,
                        block_type=b_type,
                        component_type=c_type,
                        title=b_title,
                        content=b_content
                    )
                    block_seq += 1
                    total_blocks_created += 1

            print(f" -> Ingested Unit {u_order}: {les_title} ({len(les_data['pages'])} pages, {block_seq - 1} blocks)")

    print("=" * 80)
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 8! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
