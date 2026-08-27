"""
VLearn CBC Grade 10 Geography — Topic 6: Earth Movements
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 6: Earth Movements
Source: Grade 10 Geography/06_earth_movements.md

Lessons:
  1. Meaning and Categories of Earth Movements
  2. Causes of Internal Earth Movements
  3. Types of Crustal Movements
  4. Slow vs. Rapid Earth Movements
  5. Faulting and Crustal Blocks
  6. Effects of Earth Movements and Synthesis

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic6.py
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
# TOPIC 6 LESSON DEFINITIONS (6 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Meaning and Categories of Earth Movements
    {
        "unit_order": 1,
        "unit_name": "Meaning and Categories of Earth Movements",
        "lesson_title": "Meaning and Categories of Earth Movements",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Earth Dynamics & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Dynamic Great Rift Valley of Kenya",
                        "content": {"text": "A panoramic landscape view of the Great Rift Valley in Kenya showing steep tectonic escarpments and broad plains."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Categories of Earth Movements",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify Earth movements into endogenic (internal) and exogenic (external) categories\n"
                                "- Define endogenic and exogenic movements and identify the main forces responsible for crustal deformation\n"
                                "- Differentiate between internal forces building relief and external forces leveling the landscape"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Rising Loaf Analogy",
                        "content": {
                            "text": (
                                "If you have ever baked a loaf of bread, you know that as the dough rises, "
                                "the outer crust cracks and stretches. If you push the bread down, it compresses. "
                                "Our Earth has a solid, brittle crust that behaves similarly. It is constantly being pushed, "
                                "pulled, stretched, and folded by powerful forces, some working deep inside the planet and others on its very surface."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions: Earth Movements",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Fundamental Geological Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Earth Movements",
                                    "definition": "Displacements and deformations of the Earth's crust caused by internal and external geological forces.",
                                    "simple": "The physical shifts, bending, breaking, and shaping of the Earth's crust."
                                },
                                {
                                    "term": "Endogenic Movements",
                                    "definition": "Crustal movements caused by internal forces originating from deep within the Earth's interior.",
                                    "simple": "Internal processes powered by geothermal heat that build mountains and rift valleys."
                                },
                                {
                                    "term": "Exogenic Movements",
                                    "definition": "Surface changes caused by external forces originating from outside the Earth, driven primarily by solar energy and gravity.",
                                    "simple": "External processes like rain, wind, and rivers that wear down and level the landscape."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Endogenic vs. Exogenic Force Dynamic",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Endogenic vs. Exogenic Forces Dynamic",
                        "content": {
                            "caption": "Contrast between Endogenic Forces (internal heat and magma pushing crust upward into fold mountains) and Exogenic Forces (weathering, erosion, and deposition wearing relief down)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Opposing Forces Shaping Earth's Relief",
                        "content": {
                            "text": (
                                "The Earth's landscape is a constant battlefield between two opposing forces:\n\n"
                                "1. **Endogenic (Internal) Forces (Constructional)**:\n"
                                "- Originate from deep geothermal heat and radioactive decay in the core and mantle.\n"
                                "- **Vertical Movements (Diastrophism/Epeirogenesis)**: Cause large-scale uplift or subsidence of the crust without bending rock strata into folds.\n"
                                "- **Horizontal Movements (Orogenesis)**: Cause lateral compression or tension, leading to folding (bending) and faulting (fracturing) of rock layers, creating mountain belts.\n\n"
                                "2. **Exogenic (External) Forces (Destructional / Denudation)**:\n"
                                "- Leveling forces powered by solar energy, atmospheric processes, and gravity that wear down elevated relief.\n"
                                "- **Weathering**: The in situ breakdown of rocks in their original location.\n"
                                "- **Erosion**: The wearing away and active transport of rock materials by water, wind, or ice.\n"
                                "- **Mass Wasting**: The downslope movement of soil and rock under gravity.\n"
                                "- **Deposition**: Silt, sand, and pebbles settling in low-lying basins and coastlines."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Context & Common Misconceptions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Endogenic vs Exogenic Landscapes",
                        "content": {
                            "text": (
                                "In Kenya, both forces are vividly visible:\n\n"
                                "- **Endogenic Power**: The **Great Rift Valley of Kenya** is a massive example of internal tensional forces stretching and fracturing the crust over millions of years.\n"
                                "- **Exogenic Leveling**: The **Mombasa coastline and Diani beaches** are created by exogenic forces—marine wave action and river deposition carrying eroded sediments washed down from the highland interior."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Common Misconceptions Alert: Weathering vs Erosion",
                        "content": {
                            "text": (
                                "⚠️ **Be Careful**: Do not confuse weathering with erosion.\n\n"
                                "- **Weathering** breaks rocks apart right where they are (*in situ*) through chemical, physical, or biological action without transporting them.\n"
                                "- **Erosion** involves the physical removal and transportation of those broken rock fragments to new locations by running water, wind, glaciers, or ocean waves."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Classifying Earth Movements",
                        "content": {
                            "question": "Which of the following is an example of an endogenic (internal) earth movement?",
                            "options": [
                                "River erosion carving out a deep valley",
                                "Wind carrying sand particles to form coastal dunes",
                                "Horizontal compression folding rock layers into mountains",
                                "A glacier depositing moraine ridges in a valley"
                            ],
                            "correct_answer": "Horizontal compression folding rock layers into mountains",
                            "explanation": "Horizontal compression originates from internal tectonic forces (endogenic), whereas rivers, wind, and glaciers are surface agents of denudation and deposition (exogenic)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Vertical Crustal Movements",
                        "content": {
                            "question": "What type of internal earth movement causes broad landmasses to rise or sink vertically without bending the rocks into folds?",
                            "options": [
                                "Orogenesis",
                                "Weathering",
                                "Diastrophism (Vertical movements / Epeirogenesis)",
                                "Mass wasting"
                            ],
                            "correct_answer": "Diastrophism (Vertical movements / Epeirogenesis)",
                            "explanation": "Diastrophism and epeirogenesis cause large-scale vertical uplift or subsidence of entire regional landmasses, forming plateaus or basins without folding the rock strata."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: Causes of Internal Earth Movements
    {
        "unit_order": 2,
        "unit_name": "Causes of Internal Earth Movements",
        "lesson_title": "Causes of Internal Earth Movements",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Internal Heat Engine & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Thermal Convection Currents in the Earth's Interior",
                        "content": {"text": "A geological cutaway simulation showing thermal convection cells circulating within the semi-solid mantle below the lithosphere."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Causes of Internal Movements",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the mechanical and thermal causes of endogenic movements within the Earth's interior\n"
                                "- Explain how mantle convection currents drive tectonic plate motion\n"
                                "- Describe the mechanics of ridge push and slab pull at plate boundaries\n"
                                "- Describe the role of radioactive decay in maintaining the Earth's internal heat engine"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Boiling Porridge (Uji) Analogy",
                        "content": {
                            "text": (
                                "If you boil a pot of thick maize meal porridge (Uji), you notice that hot porridge rises "
                                "in the center, spreads outward across the top, cools slightly, and sinks back down at the cooler edges. "
                                "This circular thermal circulation is called convection. Deep below our feet, the hot rock of the Earth's mantle "
                                "behaves exactly like that boiling pot of porridge over millions of years!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Definitions & Driving Engines",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Key Geological Drivers",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Tectonic Plates",
                                    "definition": "Large, rigid segments of the Earth's lithosphere (crust and uppermost solid mantle) that float on the semi-fluid asthenosphere beneath.",
                                    "simple": "Massive interlocking jigsaw pieces of crust drifting across the planet."
                                },
                                {
                                    "term": "Mantle Convection",
                                    "definition": "The circular movement of hot, semi-fluid rock in the Earth's mantle driven by immense geothermal heat from the core.",
                                    "simple": "The slow churning thermal current inside Earth that drags continental plates along."
                                },
                                {
                                    "term": "Isostatic Adjustment",
                                    "definition": "The vertical rising or sinking of the crust to restore gravitational equilibrium between the buoyant continental crust and the dense mantle.",
                                    "simple": "The crust balancing like a loaded boat floating on water."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Three Mechanical Engines of Plate Motion",
                        "content": {
                            "text": (
                                "Tectonic plate motion is driven by three interconnected mechanical and thermal engines:\n\n"
                                "1. **Mantle Convection Currents**:\n"
                                "The Earth's core remains extremely hot due to residual heat from planetary formation and the ongoing decay of radioactive isotopes (uranium, thorium, potassium-40). Hot mantle rock rises, diverges beneath the crust, and creates lateral drag forces.\n\n"
                                "2. **Plate Boundary Forces**:\n"
                                "- **Ridge Push**: At mid-ocean ridges, hot rising magma creates elevated oceanic ridges. Gravitational force pushes the newly formed, buoyant lithosphere downslope away from the ridge crest.\n"
                                "- **Slab Pull**: In subduction zones, cold, dense oceanic lithosphere sinks into the asthenosphere under gravity, pulling the trailing tectonic plate behind it like a sinking anchor.\n\n"
                                "3. **Isostatic Adjustment**:\n"
                                "When heavy loads (ice sheets, sediment piles) weigh down the crust, it subsides into the mantle. When the load is removed (ice melting, erosion), the crust rebounds upward."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Tectonic Driving Forces & Dynamics",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Tectonic Plate Driving Forces",
                        "content": {
                            "caption": "Cross-section of the Earth's mantle and crust illustrating mantle convection cells, mid-ocean ridge push, and subduction zone slab pull powered by core geothermal heat."
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "Mantle Convection and Tectonic Plates in Action",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=ryrXAGY1lAA",
                            "caption": "3D visualization of geothermal heat rising from the core, slow convective flow of mantle rock, and the resulting collision, separation, and subduction of tectonic plates."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "East African Rifting & Misconceptions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Splitting of the African Plate",
                        "content": {
                            "text": (
                                "The **Great Rift Valley of East Africa** is one of the world's most spectacular active continental rifts. "
                                "Beneath East Africa, a massive mantle upwelling (magma plume) is spreading laterally in two opposite directions. "
                                "This diverges the continental lithosphere, gradually splitting the African continent into two separate plates: "
                                "the **Nubian Plate** to the west and the **Somali Plate** to the east."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Common Misconceptions Alert: The State of the Mantle",
                        "content": {
                            "text": (
                                "⚠️ **Be Careful**: Do not imagine that tectonic plates float on a completely liquid ocean of liquid magma.\n\n"
                                "The mantle is composed almost entirely of **solid rock**. However, under extreme temperatures (over 1,000°C) "
                                "and tremendous lithostatic pressure, the solid rock behaves as a **viscous, ductile plastic solid**—capable "
                                "of flowing slowly at rates of a few centimeters per year over millions of years."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Source of Internal Earth Heat",
                        "content": {
                            "question": "What is the primary source of thermal energy that keeps the Earth's interior hot enough to drive mantle convection?",
                            "options": [
                                "Intense solar radiation absorbed by the crust over millennia",
                                "Gravitational tidal friction from the Moon's orbit",
                                "Residual heat from Earth's planetary formation and radioactive decay of isotopes",
                                "Friction generated by ocean waves and river currents"
                            ],
                            "correct_answer": "Residual heat from Earth's planetary formation and radioactive decay of isotopes",
                            "explanation": "Earth's internal geothermal heat engine is sustained by primordial heat trapped during planetary accretion combined with the continuous radioactive decay of isotopes such as uranium, thorium, and potassium in the core and mantle."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Gravity-Driven Plate Forces",
                        "content": {
                            "question": "Which plate-driving mechanism occurs when a cold, dense oceanic plate sinks into the subduction trench and pulls the trailing plate along?",
                            "options": [
                                "Ridge push",
                                "Isostatic uplift",
                                "Slab pull",
                                "Dynamic folding"
                            ],
                            "correct_answer": "Slab pull",
                            "explanation": "Slab pull is the powerful gravity-driven force operating at subduction zones, where the sinking edge of a cold, dense oceanic plate pulls the rest of the lithosphere into the asthenosphere."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Types of Crustal Movements
    {
        "unit_order": 3,
        "unit_name": "Types of Crustal Movements",
        "lesson_title": "Types of Crustal Movements",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Crustal Stresses & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Buckled and Folded Rock Strata",
                        "content": {"text": "Exposed geological rock layers exhibiting intense folding, synclines, and anticlines caused by horizontal compression."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Types of Crustal Movements",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish between vertical (epeirogenic) and horizontal (orogenic) crustal movements\n"
                                "- Explain the mechanical differences between tension, compression, and shear forces\n"
                                "- Identify the distinctive landforms produced by vertical uplift/subsidence and horizontal deformation"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Sponge Demonstration",
                        "content": {
                            "text": (
                                "If you take a soft kitchen sponge and pull it gently from both ends, it stretches and eventually tears down the middle. "
                                "This is tension. If you push the sponge inwards from both ends, it wrinkles, buckles, and humps upward in folds. "
                                "This is compression. The solid rock strata of our Earth's crust respond to lateral tectonic stresses in the exact same manner!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Tectonic Stresses: Tension, Compression & Shear",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Key Stress Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Tensional Force",
                                    "definition": "A horizontal tectonic stress that pulls rock layers apart in opposite directions, thinning and fracturing the crust.",
                                    "simple": "A pulling-apart force that cracks and faults the crust."
                                },
                                {
                                    "term": "Compressional Force",
                                    "definition": "A horizontal tectonic stress that pushes rock layers together from opposite directions, shortening and buckling the crust.",
                                    "simple": "A squeezing-together force that folds and wrinkles rocks into mountains."
                                },
                                {
                                    "term": "Shear Force",
                                    "definition": "Lateral forces that slide adjacent rock masses past each other in opposite horizontal directions along a plane.",
                                    "simple": "A side-by-side rubbing force that tears rocks horizontally."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Vertical vs. Horizontal Displacements",
                        "content": {
                            "text": (
                                "Endogenic movements deform rocks through two distinct spatial vectors:\n\n"
                                "1. **Vertical Movements (Epeirogenic / Diastrophic)**:\n"
                                "- Gentle, broad vertical shifts affecting large continental sectors without folding rock strata.\n"
                                "- **Uplift**: Elevates land surfaces into high tablelands/plateaus and causes **coastal emergence** (exposed marine terraces, raised sea cliffs, raised beaches).\n"
                                "- **Subsidence**: Lowers land surfaces into broad depressions/crustal basins and causes **coastal submergence** (forming rias, drowned valleys, and fjords).\n\n"
                                "2. **Horizontal Movements (Orogenic / Mountain Building)**:\n"
                                "- Intense lateral forces acting across narrower mobile belts.\n"
                                "- **Compression** $\\rightarrow$ Causes rocks to buckle and wrinkle into wave-like **folds** (anticlines and synclines).\n"
                                "- **Tension** $\\rightarrow$ Causes brittle rocks to stretch, fracture, and slip along fracture planes, producing **faults**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Visualizing Crustal Deformation",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Horizontal Orogenic vs. Vertical Epeirogenic Movements",
                        "content": {
                            "caption": "Comparison of Tensional pulling forces creating fault fractures, Compressional squeezing forces creating folded anticlines and synclines, and Vertical Epeirogenic uplift and subsidence."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Yatta Plateau vs. Rift Escarpments",
                        "content": {
                            "text": (
                                "Kenya's diverse relief clearly shows both movement types:\n\n"
                                "- **Vertical Uplift**: The **Yatta Plateau** and the extensive high plains of eastern and central Kenya experienced broad epeirogenic uplift, raising vast flat landscapes thousands of feet above sea level without crushing them into folded mountains.\n"
                                "- **Horizontal Tension**: The **Mau and Kerio Escarpments** bordering the Rift Valley were created by intense horizontal tensional forces that pulled the continental crust apart, causing huge fault blocks to drop downwards."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Misconceptions: Uplift vs Mountain Building",
                        "content": {
                            "text": (
                                "⚠️ **Be Careful**: Do not confuse broad vertical uplift (epeirogenesis) with mountain building (orogenesis).\n\n"
                                "- **Epeirogenesis** lifts entire regional landmasses vertically as uniform blocks, maintaining horizontal rock strata to form flat-topped **plateaus** and elevated plains.\n"
                                "- **Orogenesis** involves intense horizontal compression that actively crumples, crushes, folds, and overthrusts sedimentary strata into complex, jagged **fold mountain ranges**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Folding Stress Force",
                        "content": {
                            "question": "Which horizontal tectonic force is directly responsible for compressing rock strata to form folded mountain ranges?",
                            "options": [
                                "Tensional force",
                                "Compressional force",
                                "Isostatic subsidence",
                                "Shear dilatation"
                            ],
                            "correct_answer": "Compressional force",
                            "explanation": "Compressional force is a lateral squeezing stress that pushes rock strata together, causing them to shorten and buckle into folds."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Coastal Emergence Evidence",
                        "content": {
                            "question": "The presence of raised marine beaches and exposed sea cliffs high above current sea level is primary evidence of which type of movement?",
                            "options": [
                                "Horizontal crustal compression",
                                "Broad vertical uplift (Epeirogenesis)",
                                "Strike-slip faulting",
                                "Exogenic river deposition"
                            ],
                            "correct_answer": "Broad vertical uplift (Epeirogenesis)",
                            "explanation": "Vertical uplift elevates coastal land relative to sea level, exposing ancient wave-cut terraces, sea caves, and beaches as dry land above the modern shoreline."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Slow vs. Rapid Earth Movements
    {
        "unit_order": 4,
        "unit_name": "Slow vs. Rapid Earth Movements",
        "lesson_title": "Slow vs. Rapid Earth Movements",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geological Timescales & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "San Andreas Fault Zone Surface Trace",
                        "content": {"text": "An aerial view of the San Andreas Fault in the Carrizo Plain showing offset stream channels and sudden seismic fault traces."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Movement Velocities",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Differentiate between slow and rapid earth movements based on temporal scales and geological processes\n"
                                "- Identify examples of slow tectonic creep versus sudden seismic catastrophes\n"
                                "- Explain the role of Elastic Rebound Theory in generating sudden earthquakes\n"
                                "- Compare the human and infrastructure impacts of slow versus rapid earth movements"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Bending Stick Analogy",
                        "content": {
                            "text": (
                                "If you take a dry wooden stick and slowly bend it, it flexes gradually and silently without breaking. "
                                "This represents slow earth movements. But if you continue pushing harder, the stored elastic strain exceeds "
                                "the wood's breaking limit, and it suddenly snaps with a loud crack, releasing all its energy in a millisecond! "
                                "This sudden fracture perfectly mirrors rapid seismic earth movements like earthquakes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Temporal Scales of Geological Movement",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Speed Classification Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Slow Earth Movements",
                                    "definition": "Continuous, gradual tectonic processes that operate imperceptibly over thousands or millions of years (rates of millimeters to centimeters per year).",
                                    "simple": "Gradual continental drift, mountain folding, and isostatic rebound taking millions of years."
                                },
                                {
                                    "term": "Rapid Earth Movements",
                                    "definition": "Sudden, violent geological events that occur in seconds or minutes, releasing massive accumulated strain energy.",
                                    "simple": "Violent earthquakes, volcanic explosions, and catastrophic landslides happening in seconds."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Comparing Slow Creep vs. Rapid Seismic Events",
                        "content": {
                            "text": (
                                "Geological processes operate on drastically different temporal scales:\n\n"
                                "1. **Slow Earth Movements (Tectonic Creep & Orogeny)**:\n"
                                "- **Continental Drift**: Tectonic plates glide across the asthenosphere at rates of 2 to 10 cm per year.\n"
                                "- **Orogenesis**: Sedimentary rock layers slowly buckle over tens of millions of years to build mountain chains like the Alps and Himalayas.\n"
                                "- **Isostatic Uplift**: Continents slowly rebound upwards over thousands of years after heavy ice sheets melt.\n\n"
                                "2. **Rapid Earth Movements (Seismic & Volcanic Events)**:\n"
                                "- **Earthquakes**: Sudden displacement along locked fault zones releasing decades or centuries of elastic strain in seconds.\n"
                                "- **Volcanic Eruptions**: Explosive ejection of magma, pyroclastic flows, and ash clouds when chamber pressure exceeds lithostatic resistance.\n"
                                "- **Catastrophic Landslides**: Sudden mass wasting of hillsides triggered by rain saturation or seismic shaking."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Elastic Rebound Theory & Seismic Release",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Elastic Rebound Theory & Rupture Cycle",
                        "content": {
                            "caption": "Three-stage sequence of Elastic Rebound: (1) Unstressed rock along a locked fault plane, (2) Frictional locking causes rocks to bend elastically storing strain energy, (3) Sudden rupture and snap-back releasing seismic shockwaves."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Gradual Rifting vs Sudden Fractures",
                        "content": {
                            "text": (
                                "Kenya provides living proof of both timescales:\n\n"
                                "- **Slow Rifting**: The East African Rift is widening steadily and silently at an average rate of **2.5 centimeters per year**, an imperceptible drift over human lifespans.\n"
                                "- **Rapid Subsidence & Tremors**: In regions like **Naivasha, Suswa, and Solai**, sudden ground fissures and seismic tremors occasionally tear open within seconds following heavy rains or minor earthquakes, fracturing roads, severing railway lines, and damaging buildings."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Misconceptions: The Link Between Slow and Rapid Movements",
                        "content": {
                            "text": (
                                "⚠️ **Be Careful**: Do not view slow movements and rapid movements as completely separate, independent phenomena.\n\n"
                                "They are two sides of the same mechanical coin. It is the **slow, relentless drift** of tectonic plates over centuries "
                                "that builds up immense elastic stress along friction-locked fault boundaries. When that frictional lock finally fails, "
                                "the stored slow energy is released in a single catastrophic instant as a **rapid earthquake**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Identifying Slow Earth Movements",
                        "content": {
                            "question": "Which of the following geological processes is classified as a slow earth movement?",
                            "options": [
                                "An explosive volcanic eruption ejecting pyroclastic flows",
                                "A sudden mudslide sweeping down a steep hillside",
                                "The widening of a continental rift basin over millions of years",
                                "A magnitude 7.2 earthquake shaking a city in seconds"
                            ],
                            "correct_answer": "The widening of a continental rift basin over millions of years",
                            "explanation": "Continental rifting and plate motion occur gradually at rates of centimeters per year over millions of years, whereas landslides, volcanic explosions, and earthquakes occur in seconds or minutes."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Cause of Rapid Earthquakes",
                        "content": {
                            "question": "According to the Elastic Rebound Theory, what directly triggers a rapid earthquake?",
                            "options": [
                                "High seasonal winds blowing across volcanic craters",
                                "The sudden slippage and release of accumulated elastic strain along a locked fault",
                                "Rivers slowly depositing silt into a delta basin",
                                "The gravitational pull of ocean tides during a full moon"
                            ],
                            "correct_answer": "The sudden slippage and release of accumulated elastic strain along a locked fault",
                            "explanation": "Earthquakes occur when rocks along a friction-locked fault bend elastically under tectonic stress until their breaking strength is exceeded, causing sudden rupture and radiating seismic waves."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Faulting and Crustal Blocks
    {
        "unit_order": 5,
        "unit_name": "Faulting and Crustal Blocks",
        "lesson_title": "Faulting and Crustal Blocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Fault Mechanics & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Vertical Fault Scarp Cliff Exposure",
                        "content": {"text": "A distinct fault scarp exposed along an active geological fault line showing clear vertical displacement between rock blocks."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Faulting Mechanics",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify the structural components of a fault: hanging wall, footwall, fault plane, and fault scarp\n"
                                "- Classify and compare normal, reverse (thrust), and strike-slip faults based on the forces involved\n"
                                "- Explain the formation of horst (block mountains) and graben (rift valleys) landforms"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Rough Wooden Blocks",
                        "content": {
                            "text": (
                                "If you take two blocks of wood with sandpaper surfaces, press them tightly together, and try to slide "
                                "them past each other, friction locks them in place. When you push with sufficient force to overcome that friction, "
                                "they suddenly jerk forward. The fracture between those two blocks is a **fault plane**, and the displacement "
                                "creates a vertical step called a **fault scarp**!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Anatomy of a Geological Fault",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Fault Terminology",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Fault",
                                    "definition": "A fracture or crack in crustal rocks along which significant relative displacement of rock blocks has occurred.",
                                    "simple": "A crack in the crust where one block of land has slipped past another."
                                },
                                {
                                    "term": "Hanging Wall",
                                    "definition": "The block of crustal rock that lies vertically above an inclined fault plane.",
                                    "simple": "The rock block resting on top of the sloping crack."
                                },
                                {
                                    "term": "Footwall",
                                    "definition": "The block of crustal rock that lies vertically beneath an inclined fault plane.",
                                    "simple": "The rock block supporting the hanging wall from underneath."
                                },
                                {
                                    "term": "Fault Scarp (Escarpment)",
                                    "definition": "The steep cliff face exposed on the surface when vertical displacement occurs along a fault line.",
                                    "simple": "A tall, steep cliff created when one side of a fault drops or rises."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Three Primary Types of Faults",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Three Primary Fault Types & Crustal Blocks",
                        "content": {
                            "caption": "Three-panel comparative block diagram: (1) Normal Fault (Tensional pulling, hanging wall drops), (2) Reverse Fault (Compressional squeezing, hanging wall rises), and (3) Strike-Slip Fault (Shear sliding past horizontally), with Horst and Graben block structures."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Classification of Faults by Stress Force",
                        "content": {
                            "text": (
                                "Faults are classified by the tectonic stress and relative block displacement:\n\n"
                                "1. **Normal Fault (Tensional Stress)**:\n"
                                "- Caused by **pulling-apart** tensional forces.\n"
                                "- The **hanging wall slides downward** relative to the footwall.\n"
                                "- Creates rift valleys (grabens) and steep escarpments.\n\n"
                                "2. **Reverse / Thrust Fault (Compressional Stress)**:\n"
                                "- Caused by **squeezing-together** compressional forces.\n"
                                "- The **hanging wall is pushed upward** relative to the footwall.\n"
                                "- Shortens and thickens the crust.\n\n"
                                "3. **Strike-Slip / Transform Fault (Shear Stress)**:\n"
                                "- Caused by **lateral horizontal shear** forces.\n"
                                "- Blocks slide past each other horizontally with little or no vertical displacement (e.g., San Andreas Fault).\n\n"
                                "4. **Crustal Block Landforms**:\n"
                                "- **Horst (Block Mountain)**: An elevated block of crust bounded by normal faults on both sides (e.g., Ruwenzori Mountains).\n"
                                "- **Graben (Rift Valley)**: A dropped central crustal block between parallel normal faults (e.g., Gregory Rift Valley)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Escarpments & Common Misconceptions",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: The Great Elgeyo Escarpment",
                        "content": {
                            "text": (
                                "The **Elgeyo Marakwet Escarpment** in western Kenya is one of the most magnificent normal fault scarps on Earth. "
                                "Tectonic tension pulled the crust apart, causing the Kerio Valley floor (graben) to subside, leaving the footwall block "
                                "standing as an awe-inspiring, near-vertical rock cliff towering over **1,500 meters** above the valley floor."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Common Misconceptions Alert: Normal vs Reverse Faults",
                        "content": {
                            "text": (
                                "⚠️ **Be Careful**: Do not confuse normal faults with reverse faults.\n\n"
                                "- **Normal Faults**: Pulling forces (tension) cause the hanging wall to **drop down** along the slope.\n"
                                "- **Reverse Faults**: Squeezing forces (compression) force the hanging wall to **climb up** over the footwall."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Normal Fault Mechanics",
                        "content": {
                            "question": "Which type of fault is formed when tensional forces pull the crust apart, causing the hanging wall to slide downward relative to the footwall?",
                            "options": [
                                "Reverse Fault",
                                "Thrust Fault",
                                "Normal Fault",
                                "Strike-Slip Fault"
                            ],
                            "correct_answer": "Normal Fault",
                            "explanation": "Normal faults are produced by tensional stress pulling the crust apart, which causes the hanging wall block to slide downward along the fault plane."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Fault Scarp Landform",
                        "content": {
                            "question": "What name is given to the steep cliff exposed on the surface when crustal blocks are vertically displaced along a fault?",
                            "options": [
                                "Anticline ridge",
                                "Fault Scarp (Escarpment)",
                                "Syncline trough",
                                "Batholith dome"
                            ],
                            "correct_answer": "Fault Scarp (Escarpment)",
                            "explanation": "A fault scarp (or escarpment) is a steep cliff or slope formed on the Earth's surface by vertical offset along a fault line."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Effects of Earth Movements and Synthesis
    {
        "unit_order": 6,
        "unit_name": "Effects of Earth Movements and Synthesis",
        "lesson_title": "Effects of Earth Movements and Synthesis",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Earth System Synthesis & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Flamingos and Alkaline Rift Lakes in Kenya",
                        "content": {"text": "Flocks of flamingos feeding along the shallow alkaline waters of Lake Nakuru in the floor of the Great Rift Valley."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Effects and Synthesis",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Synthesize the causal cascade from deep mantle convection to surface topography and drainage\n"
                                "- Explain how earth movements modify river drainage systems and form tectonic lake basins\n"
                                "- Evaluate the economic opportunities (soils, minerals, geothermal power, tourism) and hazards (earthquakes, landslides) of earth movements"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Connecting Deep Earth to Daily Life",
                        "content": {
                            "text": (
                                "We have studied the forces, causes, velocities, and fault structures of Earth movements. "
                                "Now, let's step back and view the complete picture: How does a slow convection current circulating "
                                "hundreds of kilometers below our feet influence Kenya's electricity supply, rich volcanic soils, "
                                "freshwater lakes, tourist economy, and earthquake hazards today?"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Effects on Topography & Drainage Systems",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Impact Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Drainage Alteration",
                                    "definition": "The diversion, reversal, damming, or capture of river systems caused by tectonic uplift, faulting, or volcanic lava barriers.",
                                    "simple": "When Earth movements change the direction rivers flow or create new lake basins."
                                },
                                {
                                    "term": "Tectonic Hazard",
                                    "definition": "Natural catastrophic events directly triggered by rapid endogenic earth movements, including earthquakes, tsunamis, and volcanic eruptions.",
                                    "simple": "Disasters caused by sudden shifts in the Earth's crust."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Topography and Drainage Transformations",
                        "content": {
                            "text": (
                                "Earth movements fundamentally transform planetary geography:\n\n"
                                "1. **Landform Generation**:\n"
                                "- Endogenic movements create fold mountains (Himalayas, Andes), tectonic rift valleys (East African Rift), block mountains (Ruwenzori), and volcanic peaks (Mt. Kenya, Kilimanjaro).\n"
                                "- Exogenic weathering and erosion immediately begin sculpting and carving these elevated landforms into valleys, gorges, and plains.\n\n"
                                "2. **Drainage System Modifications**:\n"
                                "- **Crustal Downwarping**: Gentle warping created massive shallow depressions, forming huge inland bodies of water such as **Lake Victoria**.\n"
                                "- **Fault-Guided Drainage**: Rivers exploit zones of crushed rock along fault lines to carve straight river valleys (e.g., Kerio and Ewaso Ng'iro rivers).\n"
                                "- **River Reversal & Damming**: Tectonic uplift can tilt the slope of land, reversing ancient river flow or impounding streams to form lakes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Earth System Cascade",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Earth System Cascade & Rift Synthesis",
                        "content": {
                            "caption": "Integrated systems flowchart tracing heat from radioactive decay and core -> mantle convection currents -> tectonic plate divergence/convergence -> folding, faulting & volcanism -> landscape evolution, drainage reorganization, geothermal power & ecosystems."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Economic Opportunities vs. Tectonic Hazards",
                        "content": {
                            "text": (
                                "Earth movements create both immense resources and serious hazards for human societies:\n\n"
                                "1. **Economic Opportunities**:\n"
                                "- **Fertile Soils**: Volcanic ash and weathered igneous rocks form deep, highly fertile volcanic soils supporting intensive agriculture in the Kenya Highlands.\n"
                                "- **Geothermal Energy**: Deep fracturing along the Rift Valley allows underground water to contact hot magma, providing clean geothermal steam tapped at **Olkaria** to generate over 40% of Kenya's electricity.\n"
                                "- **Mineral Resources**: Hydrothermal activity deposits valuable minerals (trona at Lake Magadi, fluorspar in Kerio Valley).\n"
                                "- **Tourism**: Magnificent escarpments, hot springs (Lake Bogoria), and flamingo-rich alkaline lakes (Lake Nakuru) generate billions in tourism revenue.\n\n"
                                "2. **Geological Hazards**:\n"
                                "- **Earthquake Damage**: Seismic ground shaking can collapse infrastructure and trigger destructive landslides on steep escarpments.\n"
                                "- **Surface Rupturing**: Tension cracks and sudden subsidence can sever highways, pipelines, and agricultural land."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Context & Big Picture Synthesis",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: The Rift Valley Laboratory",
                        "content": {
                            "text": (
                                "Kenya's Gregory Rift Valley is recognized globally as a living geological laboratory. "
                                "Step faulting has created a chain of specialized lake basins (Lakes Baringo, Bogoria, Nakuru, Elmenteita, Naivasha, and Magadi). "
                                "The geothermal reservoirs beneath Hell's Gate and Olkaria produce renewable green energy, while the fertile slopes of Mt. Kenya "
                                "and the Aberdares feed the nation."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Common Misconceptions Alert: Are Earth Movements Purely Destructive?",
                        "content": {
                            "text": (
                                "⚠️ **Be Careful**: Do not think that earth movements are purely destructive natural disasters.\n\n"
                                "Without the continuous endogenic uplift of our planet's crust, exogenic weathering, erosion, and rivers "
                                "would have worn down all continental landmasses into flat, submerged underwater plains millions of years ago! "
                                "Endogenic movements constantly renew the dry land that makes terrestrial life possible."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Tectonic Drainage Alteration",
                        "content": {
                            "question": "Which of the following is an example of tectonic alteration of a regional drainage system?",
                            "options": [
                                "A river depositing silt into an ocean delta",
                                "Crustal downwarping creating a large basin that fills with water to form Lake Victoria",
                                "A river flowing straight over a sand dune",
                                "Acid rain dissolving limestone surface rock"
                            ],
                            "correct_answer": "Crustal downwarping creating a large basin that fills with water to form Lake Victoria",
                            "explanation": "Regional crustal downwarping and faulting create depressions that trap water and reverse ancient river channels, fundamentally altering continental drainage."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Agricultural Benefits of Endogenic Forces",
                        "content": {
                            "question": "How do slow endogenic earth movements indirectly support human agriculture in Kenya over long periods?",
                            "options": [
                                "By causing rapid landslides that wash away farm plots",
                                "By uplifting crust and driving volcanism that weathers into deep, fertile volcanic soils",
                                "By permanently draining all highland river catchments",
                                "By causing high underground radiation"
                            ],
                            "correct_answer": "By uplifting crust and driving volcanism that weathers into deep, fertile volcanic soils",
                            "explanation": "Tectonic uplift and associated volcanism bring nutrient-rich minerals to the surface, which weather over time into rich, fertile volcanic soils ideal for farming."
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
    print("VLearn Direct Ingestion Engine: Grade 10 Geography — Topic 6: Earth Movements")
    print("=" * 80)

    with transaction.atomic():
        # 1. Resolve Curriculum Hierarchy
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise RuntimeError("Curriculum 'CBC' not found!")

        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise RuntimeError("Grade 10 not found under CBC!")

        subject = Subject.objects.filter(id=37).first()
        if not subject:
            subject = Subject.objects.filter(grade=grade, name="Geography").first()
        if not subject:
            raise RuntimeError("Subject 'Geography' (ID: 37) not found!")

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=6,
            defaults={
                "name": "Earth Movements",
                "description": "Classification of endogenic and exogenic movements, internal heat engine and mantle convection, crustal stresses and deformation, slow vs rapid movements, faulting mechanics, and topographic/drainage synthesis."
            }
        )
        topic.name = "Earth Movements"
        topic.description = "Classification of endogenic and exogenic movements, internal heat engine and mantle convection, crustal stresses and deformation, slow vs rapid movements, faulting mechanics, and topographic/drainage synthesis."
        topic.save()

        print(f"Target Topic: [{topic.id}] Grade 10 Geography - Topic 6: {topic.name}")

        # 2. Ingest 6 Lessons & Units
        total_blocks_created = 0
        for les_data in LESSONS_DATA:
            u_order = les_data["unit_order"]
            u_name = clean_text(les_data["unit_name"])
            les_title = clean_text(les_data["lesson_title"])

            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": f"Learning unit for {u_name}"}
            )
            unit.name = u_name
            unit.save()

            lesson, l_created = Lesson.objects.get_or_create(
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

            # Clean previous blocks for idempotency
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
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 6! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
