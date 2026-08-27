"""
VLearn CBC Grade 10 Geography — Topic 5: Rocks
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10 CBC, Subject ID: 37)
Topic 5: Rocks
Source: Grade 10 Geography/05_rocks.md

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic5.py
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
    """Remove citation brackets ([170], [181], [S1, p. 1]) and normalize whitespace."""
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
# TOPIC 5 LESSON DEFINITIONS (18 LESSONS)
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: Introduction to Rocks and Minerals
    {
        "unit_order": 1,
        "unit_name": "Introduction to Rocks and Minerals",
        "lesson_title": "Introduction to Rocks and Minerals",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Earth's Building Blocks & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Rock and Mineral Crystalline Specimens",
                        "content": {"text": "A close-up view of crystalline minerals and rock specimens showing distinct textures, colors, and crystal habits."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Rocks and Minerals",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define 'rock' and 'mineral' with scientific accuracy\n"
                                "- Distinguish clearly between rocks and minerals based on chemical composition and structure\n"
                                "- Identify the primary physical criteria used to observe and describe rock specimens"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Variety of Stones",
                        "content": {
                            "text": (
                                "Think about the pebbles you see along a dry riverbed, a rocky path in Machakos, or a road construction site in Kenya. "
                                "Why are some stones shiny and crystalline, some dull and crumbly, and others dark and extremely heavy? "
                                "These variations exist because of the unique mineral building blocks that make up our Earth's crust."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Physical Observation Criteria",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Geological Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Rock",
                                    "definition": "A consolidated natural aggregate composed of grains of one or more minerals.",
                                    "simple": "A rock is like a cake, made of a mixture of different ingredients."
                                },
                                {
                                    "term": "Mineral",
                                    "definition": "A naturally occurring, inorganic substance with a definite chemical composition, physical properties, and an ordered crystalline structure.",
                                    "simple": "A mineral is like a single pure ingredient—such as flour or sugar—that has its own distinct properties."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Physical Criteria for Describing Rocks",
                        "content": {
                            "text": (
                                "Geographers and geologists use four primary physical criteria to describe rock specimens:\n\n"
                                "1. **Color**: The outward hue of the rock (e.g., white, black, pink, or multicolored).\n"
                                "2. **Texture**: The grain size, shape, and arrangement of mineral crystals (e.g., coarse, fine, or glassy).\n"
                                "3. **Hardness**: The resistance of the rock or mineral to scratching, measured using the Mohs Hardness Scale.\n"
                                "4. **Luster**: The way the surface reflects light (e.g., metallic, glassy, dull, or pearly)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Rock vs. Mineral Structure & Kenyan Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Comparison of a Rock and a Mineral",
                        "content": {
                            "caption": "Granite rock specimen composed of an aggregate of quartz, feldspar, and mica minerals."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Minerals in Our Landscape",
                        "content": {
                            "text": (
                                "In Kenya, the dry hills around Kitui and Machakos are rich in crystalline minerals like feldspar and quartz, "
                                "while the coastal sands of Kwale are world-famous for titanium-bearing mineral sands (rutile and ilmenite) "
                                "washed down from weathered interior rocks over millions of years."
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Common Misconceptions Alert",
                        "content": {
                            "text": (
                                "Do not confuse a rock with a mineral! A mineral is a single, chemically uniform substance with a fixed crystal structure. "
                                "A rock is almost always a mixture (aggregate) of different minerals. For example, common coal is a rock, whereas diamonds "
                                "are pure mineral carbon."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Pure Mineral vs. Rock",
                        "content": {
                            "question": "Which of the following is a pure mineral with a definite chemical composition, rather than a rock?",
                            "options": [
                                "Granite",
                                "Basalt",
                                "Quartz",
                                "Sandstone"
                            ],
                            "correct_answer": "Quartz",
                            "explanation": "Quartz is a pure mineral composed of silicon dioxide (SiO2). Granite, basalt, and sandstone are all rocks composed of mixtures of multiple minerals."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Geological Meaning of Texture",
                        "content": {
                            "question": "What does a geographer mean when describing a rock's 'texture'?",
                            "options": [
                                "Whether the rock feels warm or cold to the touch",
                                "The size, shape, and arrangement of mineral grains in the rock",
                                "The weight of the rock compared to its volume",
                                "The exact depth underground where the rock formed"
                            ],
                            "correct_answer": "The size, shape, and arrangement of mineral grains in the rock",
                            "explanation": "Texture refers to the physical size, shape, and pattern of arrangement of the constituent mineral grains, which reveals cooling rates and depositional environments."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: The Rock Cycle
    {
        "unit_order": 2,
        "unit_name": "The Rock Cycle",
        "lesson_title": "The Rock Cycle",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Earth's Recycling Machine & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Geological Rock Formations in Nature",
                        "content": {"text": "A dramatic geological landscape showing stratified sedimentary layers, exposed igneous intrusions, and metamorphic foldings."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: The Rock Cycle",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the rock cycle as a continuous, dynamic geological recycling process\n"
                                "- Identify the main stages and pathways connecting igneous, sedimentary, and metamorphic rocks\n"
                                "- Describe the roles of internal heat, tectonic pressure, weathering, and lithification in rock transformations"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: No Rock is Permanent",
                        "content": {
                            "text": (
                                "If you squeeze clay in your hands, it compacts. If you heat plastic near a fire, it melts and reshapes. "
                                "Similarly, planet Earth is a giant rock recycling machine. Given millions of years, the hard black volcanic stone "
                                "of Mount Kenya can weather into sand on a Mombasa beach, compress into hard sandstone, bake into metamorphic quartzite, "
                                "and eventually melt back into hot magma inside the mantle!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & The Two Driving Engines",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Rock Cycle Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Rock Cycle",
                                    "definition": "A continuous geological process by which rocks are constantly being created, transformed, destroyed, and reformed from one type to another over geological time.",
                                    "simple": "The planetary pathway that recycles old rocks into new ones using heat, pressure, weathering, and melting."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Driving Engines of the Rock Cycle",
                        "content": {
                            "text": (
                                "The rock cycle is powered by two fundamental engines:\n\n"
                                "1. **The Internal Engine (Endogenic Forces)**: Driven by Earth's internal geothermal heat and radioactive decay, causing mantle convection, melting, volcanism, and tectonic metamorphism.\n"
                                "2. **The External Engine (Exogenic Forces)**: Driven by solar energy and gravity, powering rainfall, wind, river flow, weathering, erosion, and sedimentation."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Dynamic Cycle Pathways & Multimedia",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Dynamic Rock Cycle Pathways",
                        "content": {
                            "caption": "Complete pathways connecting Magma, Igneous Rocks, Sediments, Sedimentary Rocks, and Metamorphic Rocks."
                        }
                    },
                    {
                        "block_type": "video",
                        "component_type": "video",
                        "title": "The Rock Cycle in Motion",
                        "content": {
                            "url": "https://www.youtube.com/watch?v=swKBi6hHHMA",
                            "caption": "Animated overview of geological transformations across igneous, sedimentary, and metamorphic stages."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Volcanic Soils of the Highlands",
                        "content": {
                            "text": (
                                "The rich red soils of Kiambu and Nyeri were once hard volcanic lavas. Over thousands of years, atmospheric weathering "
                                "and rain broke these rocks down into fine, fertile sediment, illustrating the rock-to-sediment transition of the rock cycle in action."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Lithification Process",
                        "content": {
                            "question": "Which geological process is responsible for turning loose deposited sand into solid sandstone?",
                            "options": [
                                "Metamorphic recrystallization",
                                "Surface chemical weathering",
                                "Magmatic melting",
                                "Compaction and cementation (Lithification)"
                            ],
                            "correct_answer": "Compaction and cementation (Lithification)",
                            "explanation": "Lithification involves the squashing (compaction) of sediments under weight and the gluing (cementation) of grains by mineral solutions."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Exogenic Driving Forces",
                        "content": {
                            "question": "What is the primary driving energy source behind surface weathering and erosion in the rock cycle?",
                            "options": [
                                "Mantle convection currents",
                                "Solar energy and gravity",
                                "Radioactive decay of isotopes",
                                "Volcanic ash eruptions"
                            ],
                            "correct_answer": "Solar energy and gravity",
                            "explanation": "Surface (exogenic) processes are driven by solar energy, which fuels the water cycle and weather, combined with gravity pulling materials downhill."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Formation of Igneous Rocks
    {
        "unit_order": 3,
        "unit_name": "Formation of Igneous Rocks",
        "lesson_title": "Formation of Igneous Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Fire-Born Rocks & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Active Lava Flow Cooling into Basalt",
                        "content": {"text": "A volcanic eruption showing glowing red basaltic lava flowing over the ground and cooling into solid black volcanic rock."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Formation of Igneous Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define 'igneous rock' and distinguish clearly between magma and lava\n"
                                "- Explain how the rate of cooling dictates mineral crystal size in molten materials\n"
                                "- Compare the fundamental geological settings of intrusive and extrusive igneous rocks"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Crystal Growth Rates",
                        "content": {
                            "text": (
                                "If you boil water with dissolved sugar and cool it very slowly in a warm room, large crystals grow. "
                                "If you plunge it into ice immediately, it hardens rapidly into a smooth glassy solid. "
                                "Similarly, molten rock cooling deep underground has ample time to grow large crystals, while lava erupting onto the cold surface hardens in minutes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & The Golden Cooling Rule",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Igneous Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Igneous Rock",
                                    "definition": "A rock formed when molten material (magma or lava) cools and solidifies on or beneath the Earth's surface.",
                                    "simple": "Rocks formed by fire; solidified molten rock."
                                },
                                {
                                    "term": "Magma",
                                    "definition": "Molten rock material located beneath the Earth's surface.",
                                    "simple": "Liquid underground rock."
                                },
                                {
                                    "term": "Lava",
                                    "definition": "Molten rock material after it breaches and flows onto the Earth's surface.",
                                    "simple": "Molten rock pouring out onto the land."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Golden Rule of Igneous Geology",
                        "content": {
                            "text": (
                                "The fundamental law governing igneous rock texture states that **crystal size is inversely proportional to cooling rate**:\n\n"
                                "- **Slow cooling deep underground** -> Mineral atoms have time to migrate and bond into **large, visible coarse crystals** (Phaneritic texture).\n"
                                "- **Rapid cooling on the Earth's surface** -> Molten rock freezes rapidly, trapping atoms in **microscopic fine crystals** (Aphanitic texture) or forming non-crystalline **volcanic glass**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Intrusive vs. Extrusive Environments & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Intrusive vs. Extrusive Cooling Environments",
                        "content": {
                            "caption": "Cross-section comparing slow subterranean cooling in magma chambers versus fast atmospheric surface cooling on volcanic cones."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Rift Valley Igneous Rocks",
                        "content": {
                            "text": (
                                "The Great Rift Valley in Kenya was formed by tectonic rifting that allowed massive volumes of magma to ascend. "
                                "Consequently, extrusive rocks like basalt, phonolite, and obsidian dominate the Rift floor, while ancient intrusive granites "
                                "are exposed in western Kenya due to millions of years of surface erosion."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Crystal Size Control",
                        "content": {
                            "question": "Which factor directly determines the size of mineral crystals in an igneous rock?",
                            "options": [
                                "The color of the molten rock",
                                "The rate at which the molten rock cools",
                                "The amount of rain falling on the vent",
                                "The latitude of the volcanic mountain"
                            ],
                            "correct_answer": "The rate at which the molten rock cools",
                            "explanation": "Slow cooling allows minerals to grow large, visible crystals, whereas rapid cooling results in fine-grained or glassy textures."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Microscopic Crystal Texture",
                        "content": {
                            "question": "An igneous rock specimen exhibits microscopic mineral grains invisible to the naked eye. What does this indicate?",
                            "options": [
                                "It cooled very slowly deep within a batholith",
                                "It is a plutonic intrusive rock",
                                "It formed when lava solidified rapidly on the Earth's surface",
                                "It was subjected to intense tectonic folding"
                            ],
                            "correct_answer": "It formed when lava solidified rapidly on the Earth's surface",
                            "explanation": "Microscopic (aphanitic) crystals are proof of rapid cooling on the surface in an extrusive volcanic environment."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Intrusive Igneous Rocks
    {
        "unit_order": 4,
        "unit_name": "Intrusive Igneous Rocks",
        "lesson_title": "Intrusive Igneous Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Subterranean Rocks & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Coarse-Grained Granite Outcrop and Boulders",
                        "content": {"text": "A massive granite rock exposure showing large interlocking crystals of pink feldspar, clear quartz, and black mica."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Intrusive Igneous Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify intrusive igneous rocks into plutonic and hypabyssal groups\n"
                                "- Describe the coarse-grained phaneritic texture characteristic of subterranean cooling\n"
                                "- Identify granite, diorite, and gabbro and state their practical economic uses in Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Giant Tors of Western Kenya",
                        "content": {
                            "text": (
                                "If you travel to Kakamega, Vihiga, or Kisumu, you will observe massive rounded rock hills (granitic tors) rising above the landscape. "
                                "These giant boulders did not fall from the sky. They formed deep underground under immense pressure and were exposed "
                                "after millions of years of surface weathering and erosion."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Plutonic vs. Hypabyssal Rocks",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Intrusive Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Intrusive Igneous Rock",
                                    "definition": "Rocks formed when magma cools and solidifies slowly below the Earth's surface.",
                                    "simple": "Underground rocks that hardened slowly inside the crust."
                                },
                                {
                                    "term": "Plutonic Rocks",
                                    "definition": "Intrusive rocks that crystallize deep within the Earth's crust over millions of years (e.g., granite, gabbro).",
                                    "simple": "Deep-seated rocks with large, coarse crystals."
                                },
                                {
                                    "term": "Hypabyssal Rocks",
                                    "definition": "Intrusive rocks that solidify at shallow depths within cracks and fissures (e.g., dolerite, porphyry).",
                                    "simple": "Medium-grained rocks formed in subsurface fractures."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Plutonic Rock Varieties and Mineral Composition",
                        "content": {
                            "text": (
                                "Plutonic rocks are classified by their silica content and mineral mix:\n\n"
                                "- **Granite**: Light-colored, silica-rich (acidic) rock containing quartz, feldspar, and biotite mica.\n"
                                "- **Diorite**: Intermediate rock with equal parts light feldspar and dark amphibole ('salt-and-pepper' appearance).\n"
                                "- **Gabbro**: Dark, dense, basic rock rich in pyroxene and calcium-rich plagioclase."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Intrusive Structures & Kenyan Case Study",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Geological Cross-Section of Intrusive Bodies",
                        "content": {
                            "caption": "Cross-section displaying massive Batholiths, discordant vertical Dykes, and concordant horizontal Sills."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Ikhonga-Murwe (Weeping Rock)",
                        "content": {
                            "text": (
                                "The famous **Ikhonga-Murwe (Weeping Rock of Kakamega)** is a prominent granitic monument carved by differential weathering "
                                "from an ancient plutonic batholith. Granites from western Kenya are heavily quarried for high-strength building ballast and decorative stone."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Deep-Seated Plutonic Example",
                        "content": {
                            "question": "Which of the following is a classic example of a coarse-grained plutonic intrusive rock?",
                            "options": [
                                "Obsidian",
                                "Basalt",
                                "Pumice",
                                "Granite"
                            ],
                            "correct_answer": "Granite",
                            "explanation": "Granite is the quintessential coarse-grained plutonic rock formed by slow cooling of silica-rich magma deep underground."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Discordant Intrusions",
                        "content": {
                            "question": "What is a vertical or steeply inclined sheet of hypabyssal rock that cuts across surrounding rock layers called?",
                            "options": [
                                "Sill",
                                "Dyke",
                                "Laccolith",
                                "Lopolith"
                            ],
                            "correct_answer": "Dyke",
                            "explanation": "A dyke is a discordant wall-like intrusion cutting across existing bedding planes, whereas a sill runs parallel (concordant) between layers."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: Extrusive Igneous Rocks
    {
        "unit_order": 5,
        "unit_name": "Extrusive Igneous Rocks",
        "lesson_title": "Extrusive Igneous Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Volcanic Surface Rocks & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Volcanic Glass Obsidian and Porous Pumice",
                        "content": {"text": "A comparative specimen showing shiny black glassy obsidian alongside pale, highly porous vesicular pumice."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Extrusive Igneous Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the characteristics of extrusive igneous rocks (fine-grained, glassy, vesicular)\n"
                                "- Distinguish between effusive lava flows and explosive pyroclastic ejecta\n"
                                "- Identify basalt, obsidian, pumice, and volcanic tuff with real Kenyan examples"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Stone That Floats",
                        "content": {
                            "text": (
                                "If you have ever used a rough, lightweight grey stone to scrub your feet, you have used **pumice**! "
                                "Pumice is so light that it actually floats on water. It is literally frozen volcanic froth filled with thousands of trapped gas bubbles."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Extrusive Textures",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Extrusive Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Extrusive Igneous Rock",
                                    "definition": "Rocks formed when lava or volcanic ejecta cools and solidifies rapidly on the Earth's surface.",
                                    "simple": "Volcanic rocks formed out in the open air or underwater."
                                },
                                {
                                    "term": "Pyroclasts (Volcanic Ejecta)",
                                    "definition": "Fragmented rock materials, volcanic ash, and cinders violently expelled during explosive eruptions.",
                                    "simple": "Airborne volcanic fragments that settle into solid rock."
                                },
                                {
                                    "term": "Lava Flow",
                                    "definition": "Molten lava that pours smoothly across the land surface before hardening.",
                                    "simple": "Hardened rivers of volcanic rock."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Three Distinct Extrusive Textures",
                        "content": {
                            "text": (
                                "Rapid cooling in contact with air or water produces three classic textures:\n\n"
                                "1. **Fine-Grained (Aphanitic)**: Microscopic crystals formed from fluid lava flows (e.g., **Basalt**, **Phonolite**).\n"
                                "2. **Glassy**: Instantaneous quenching preventing any crystal formation (e.g., **Obsidian**).\n"
                                "3. **Vesicular**: Spongy, porous rock containing cavities left by escaping volcanic gas (e.g., **Pumice**, **Scoria**)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Eruption Types & Kenyan Case Studies",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Extrusive Rock Textures & Volcanic Ejecta",
                        "content": {
                            "caption": "Comparison of Basalt lava flows, Glassy Obsidian, Vesicular Pumice, and Stratified Volcanic Ash Tuff."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Chyulu Hills & Hell's Gate",
                        "content": {
                            "text": (
                                "The **Chyulu Hills** in southeastern Kenya are composed of young basalt lava fields and porous volcanic cinder cones. "
                                "In **Hell's Gate National Park** near Naivasha, ancient lava flows produced abundant natural black **obsidian**, "
                                "which prehistoric humans gathered to craft razor-sharp stone tools."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Vesicular Texture Origin",
                        "content": {
                            "question": "Why does pumice have a unique vesicular texture filled with thousands of tiny cavities?",
                            "options": [
                                "It was dissolved by underground acidic water",
                                "It was crushed under tectonic pressure",
                                "Expanding gas bubbles were trapped as frothy lava cooled rapidly in the air",
                                "It is composed of compressed sea animal shells"
                            ],
                            "correct_answer": "Expanding gas bubbles were trapped as frothy lava cooled rapidly in the air",
                            "explanation": "Pumice forms from gas-rich, frothy volcanic ejecta that freezes mid-air, locking in countless empty gas vesicles."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Rift Valley Volcanic Rock",
                        "content": {
                            "question": "Which dark, fine-grained extrusive rock covers extensive parts of the Kenyan Rift Valley floor?",
                            "options": [
                                "Granite",
                                "Basalt",
                                "Diorite",
                                "Marble"
                            ],
                            "correct_answer": "Basalt",
                            "explanation": "Basalt is the most abundant extrusive igneous rock formed from fluid lava flows that spread across rift valley plains."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Formation of Sedimentary Rocks
    {
        "unit_order": 6,
        "unit_name": "Formation of Sedimentary Rocks",
        "lesson_title": "Formation of Sedimentary Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Layered Earth Archives & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Horizontal Sedimentary Rock Strata and Bedding Planes",
                        "content": {"text": "A towering geological cliff face displaying distinct horizontal layers of sedimentary rock separated by flat bedding planes."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Formation of Sedimentary Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Trace the five sequential geological stages of lithification\n"
                                "- Describe the defining characteristics of sedimentary rocks, including stratification and fossils\n"
                                "- Explain what bedding planes are and how they record ancient environmental changes"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Settling Layers in Water",
                        "content": {
                            "text": (
                                "If you shake sand, pebbles, and mud in a jar of water and let it stand, the heavy gravel settles first, followed by sand, "
                                "and finally fine mud in neat horizontal layers. Over millions of years, as thousands of meters of sediment pile up, "
                                "the lower layers are squashed and cemented into solid stone. This is how sedimentary rocks are born!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & The Lithification Pipeline",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Sedimentary Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Sedimentary Rock",
                                    "definition": "Rocks formed through the deposition, compaction, and cementation of mineral particles or organic remains in successive layers.",
                                    "simple": "Layered rocks made from squashed and glued sediments."
                                },
                                {
                                    "term": "Lithification",
                                    "definition": "The complex geological process of converting loose, unconsolidated sediment into solid rock through compaction and cementation.",
                                    "simple": "Turning soft mud or sand into solid stone."
                                },
                                {
                                    "term": "Strata & Bedding Planes",
                                    "definition": "Strata are the horizontal sedimentary rock layers; bedding planes are the flat dividing surfaces separating individual layers.",
                                    "simple": "The natural stripes and layer boundaries in a cliff face."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The 5-Stage Sedimentary Pipeline",
                        "content": {
                            "text": (
                                "1. **Weathering**: Pre-existing rocks are broken down into fragments.\n"
                                "2. **Transportation**: Rivers, wind, or glaciers move sediments downhill.\n"
                                "3. **Deposition**: Sediments settle in low-lying basins or ocean floors.\n"
                                "4. **Compaction**: Overlying weight presses grains together, expelling water.\n"
                                "5. **Cementation**: Dissolved minerals (calcite, silica, iron oxide) precipitate in pore spaces, bonding grains into solid rock."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Unique Characteristics & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Steps of Lithification",
                        "content": {
                            "caption": "Three-stage transition from loose sediment with pore water to compressed grains and mineral-cemented solid rock."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Coastal Sedimentary Strip",
                        "content": {
                            "text": (
                                "The entire **coastal belt of Kenya** (Mombasa, Kilifi, Malindi, Kwale) consists of thick sedimentary strata—such as Mazeras sandstones, "
                                "shales, and fossilized coral limestones—formed when ancient oceans submerged the continental margin."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Correct Lithification Sequence",
                        "content": {
                            "question": "What is the correct sequential order of processes that turns an exposed mountain rock into a sedimentary rock?",
                            "options": [
                                "Melting -> Crystallization -> Deposition -> Compaction",
                                "Weathering -> Transportation -> Deposition -> Compaction -> Cementation",
                                "Heat -> Pressure -> Folding -> Recrystallization",
                                "Volcanic eruption -> Rapid cooling -> Cementation"
                            ],
                            "correct_answer": "Weathering -> Transportation -> Deposition -> Compaction -> Cementation",
                            "explanation": "Sedimentary rock formation starts with weathering and transport, followed by deposition in a basin, and concludes with compaction and cementation."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Unique Sedimentary Traits",
                        "content": {
                            "question": "Which of the following characteristics is found almost exclusively in sedimentary rocks?",
                            "options": [
                                "Coarse interlocking crystalline texture",
                                "Foliated mineral bands",
                                "The presence of fossils and distinct horizontal strata",
                                "Vesicles formed by escaping volcanic gas"
                            ],
                            "correct_answer": "The presence of fossils and distinct horizontal strata",
                            "explanation": "Only sedimentary rocks form in cool surface depositional environments where dead organic matter can be preserved as fossils without being incinerated or crushed."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Mechanically and Organically Formed Sedimentary Rocks
    {
        "unit_order": 7,
        "unit_name": "Mechanically and Organically Formed Sedimentary Rocks",
        "lesson_title": "Mechanically and Organically Formed Sedimentary Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Clastic & Biological Rocks & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Fossiliferous Marine Limestone and Clastic Sandstone",
                        "content": {"text": "A geological formation showing exposed fossilized coral limestone alongside fine-grained clastic sandstone strata."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Clastic and Organic Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Classify mechanically formed (clastic) sedimentary rocks based on particle grain size\n"
                                "- Categorize organically formed sedimentary rocks into calcareous, carbonaceous, siliceous, and ferruginous groups\n"
                                "- Identify sandstone, shale, coral limestone, coal, and diatomite with Kenyan examples"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The White Cliffs of Kariandusi",
                        "content": {
                            "text": (
                                "At the Kariandusi prehistoric site near Gilgil, you will see blindingly white cliffs of **diatomite**. "
                                "This chalky rock is composed of trillions of microscopic silica shells from single-celled algae (diatoms) "
                                "that lived in an ancient Rift Valley lake millions of years ago!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Clastic vs. Organic Types",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Clastic & Organic Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Mechanically Formed (Clastic) Rocks",
                                    "definition": "Sedimentary rocks formed from the physical accumulation, compaction, and cementation of weathered rock fragments.",
                                    "simple": "Rocks made of broken stone fragments (sand, mud, pebbles)."
                                },
                                {
                                    "term": "Organically Formed Rocks",
                                    "definition": "Sedimentary rocks formed from the accumulated and compressed remains of once-living plants or animals.",
                                    "simple": "Rocks built from dead biological remains."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Clastic Grain-Size Classification",
                        "content": {
                            "text": (
                                "Mechanically formed rocks are grouped by their sediment size:\n\n"
                                "- **Conglomerate**: Rounded pebbles cemented in sand (riverbeds).\n"
                                "- **Breccia**: Sharp, angular fragments cemented together.\n"
                                "- **Sandstone**: Medium sand grains (quartz) compacted together.\n"
                                "- **Shale & Mudstone**: Microscopic clay and silt particles compressed into thin, flaky sheets."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Four Classes of Organic Rocks & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Classification of Organically Formed Rocks",
                        "content": {
                            "caption": "Breakdown of Organic Sedimentary Rocks into Calcareous (Limestone/Chalk), Carbonaceous (Coal), Siliceous (Diatomite), and Ferruginous groups."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Bamburi Limestone",
                        "content": {
                            "text": (
                                "At **Bamburi in Mombasa**, extensive ancient coral reefs (calcareous limestone) are quarried by Bamburi Cement "
                                "to produce Portland cement, forming the backbone of Kenya's modern construction industry."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Diatomite Classification",
                        "content": {
                            "question": "Kariandusi diatomite is an organic sedimentary rock formed from microscopic algae shells rich in silica. Which group does it belong to?",
                            "options": [
                                "Calcareous",
                                "Carbonaceous",
                                "Siliceous",
                                "Mechanically formed"
                            ],
                            "correct_answer": "Siliceous",
                            "explanation": "Diatomite is classified as a siliceous organic rock because diatoms build their microscopic cell walls out of silica."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Fine-Grained Clastic Rock",
                        "content": {
                            "question": "Which mechanically formed rock is composed of microscopic clay particles compacted into thin, fissile sheets?",
                            "options": [
                                "Sandstone",
                                "Shale",
                                "Conglomerate",
                                "Coral limestone"
                            ],
                            "correct_answer": "Shale",
                            "explanation": "Shale is formed by the compaction of fine silt and clay muds, giving it a delicate texture that splits easily along flat planes."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Chemically Formed Sedimentary Rocks
    {
        "unit_order": 8,
        "unit_name": "Chemically Formed Sedimentary Rocks",
        "lesson_title": "Chemically Formed Sedimentary Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Precipitated Minerals & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Lake Magadi Salt Crust and Trona Evaporites",
                        "content": {"text": "A wide aerial view of Lake Magadi in Kenya showing a thick, pinkish-white crystalline crust of trona (soda ash) across the dry lake bed."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Chemically Formed Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how chemical precipitation and evaporation form sedimentary evaporite rocks\n"
                                "- Classify chemical sedimentary rocks into carbonates, sulphates, chlorides, silicates, and ironstones\n"
                                "- Describe the formation and economic extraction of trona at Lake Magadi in Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Salt Crusts in the Sun",
                        "content": {
                            "text": (
                                "If you leave a shallow dish of saltwater under the hot Kenyan sun, the water evaporates into the air, "
                                "leaving behind a white crust of pure salt crystals. On a grand scale, this exact evaporation process occurs in saline Rift Valley lakes, "
                                "producing thick deposits of soda ash (trona) and rock salt (halite)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Five Chemical Classes",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Chemical Evaporite Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Chemically Formed Sedimentary Rock",
                                    "definition": "Rocks formed when dissolved mineral compounds in water react chemically or precipitate out of supersaturated solution upon evaporation.",
                                    "simple": "Rocks created when dissolved minerals crystallize as water dries up."
                                },
                                {
                                    "term": "Evaporite",
                                    "definition": "A chemical sedimentary rock formed in arid or semi-arid basins when high evaporation rates cause dissolved mineral salts to precipitate in thick layers.",
                                    "simple": "A solid crust of mineral salts left behind after water evaporates."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Five Classes of Chemical Sedimentary Rocks",
                        "content": {
                            "text": (
                                "1. **Carbonates**: Precipitated carbonate salts (e.g., **Trona** [sodium sesquicarbonate], **Dolomite**, travertine).\n"
                                "2. **Sulphates**: Precipitated sulphate minerals (e.g., **Gypsum**).\n"
                                "3. **Chlorides**: Precipitated chlorine salts (e.g., **Halite** [common rock salt, NaCl]).\n"
                                "4. **Silicates**: Silica chemically precipitated from groundwater (e.g., **Flint**, chert).\n"
                                "5. **Ironstones**: Chemical iron compounds deposited in bogs (e.g., **Haematite**, limonite)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formation of Trona at Lake Magadi",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Formation of Trona at Lake Magadi",
                        "content": {
                            "caption": "Diagram showing groundwater leaching sodium from volcanic rocks, hot springs discharging into Lake Magadi, intense solar evaporation, and crystallization of Trona."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Lake Magadi Soda Ash",
                        "content": {
                            "text": (
                                "**Lake Magadi** in southern Kenya is an inland drainage basin where extreme solar heat evaporates alkaline hot spring water, "
                                "forming a renewable crust of **trona (soda ash)**. Tata Chemicals Magadi dredges and refines this trona to export worldwide "
                                "for the manufacture of glass, soap, and detergents."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Trona Chemical Group",
                        "content": {
                            "question": "Which chemically formed sedimentary rock is mined at Lake Magadi as a major source of soda ash?",
                            "options": [
                                "Halite",
                                "Gypsum",
                                "Trona",
                                "Dolomite"
                            ],
                            "correct_answer": "Trona",
                            "explanation": "Trona (sodium sesquicarbonate) is a chemical carbonate evaporite rock that crystallizes out of Lake Magadi's saturated alkaline brine."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Halite Classification",
                        "content": {
                            "question": "To which chemical class of sedimentary rocks does common rock salt (halite) belong?",
                            "options": [
                                "Carbonates",
                                "Sulphates",
                                "Chlorides",
                                "Silicates"
                            ],
                            "correct_answer": "Chlorides",
                            "explanation": "Halite is sodium chloride (NaCl) and belongs to the chloride group of chemical evaporite rocks."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 9: Formation of Metamorphic Rocks
    {
        "unit_order": 9,
        "unit_name": "Formation of Metamorphic Rocks",
        "lesson_title": "Formation of Metamorphic Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Transformed Earth & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Folded Metamorphic Rock Outcrop in Mountain Terrain",
                        "content": {"text": "An outcrop of metamorphic rock showing intense folding, contorted bands, and recrystallized mineral grains formed under immense heat and pressure."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Metamorphic Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Define 'metamorphism' and explain solid-state mineral recrystallization\n"
                                "- Identify the three primary agents of metamorphism (heat, pressure, chemically active fluids)\n"
                                "- Explain how metamorphic rocks differ physically and chemically from their original parent rocks"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Baking Dough into Chapati",
                        "content": {
                            "text": (
                                "Think about making chapatis. You mix soft white flour, water, and oil into dough, roll it flat, and place it on a scorching pan. "
                                "The intense heat transforms the sticky dough into a firm, golden chapati. The chapati can never be turned back into flour! "
                                "Similarly, Earth takes existing rocks and bakes and squashes them underground, permanently changing their structure and minerals without melting them."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Solid-State Recrystallization",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Metamorphic Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Metamorphic Rock",
                                    "definition": "Rocks that have undergone physical and chemical transformation from pre-existing rocks due to extreme heat, intense pressure, and hot fluids.",
                                    "simple": "Recycled rocks baked and squeezed into new, tougher rocks."
                                },
                                {
                                    "term": "Metamorphism",
                                    "definition": "The structural and mineralogical alteration of a pre-existing solid rock in response to changes in temperature, pressure, and chemical conditions.",
                                    "simple": "A solid-state makeover for rocks underground."
                                },
                                {
                                    "term": "Parent Rock (Protolith)",
                                    "definition": "The original pre-existing igneous, sedimentary, or older metamorphic rock before it underwent metamorphism.",
                                    "simple": "The starting rock material before baking and squeezing."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Three Agents of Metamorphism",
                        "content": {
                            "text": (
                                "1. **Heat**: Originating from Earth's geothermal gradient or adjacent magma chambers, heat weakens mineral bonds and accelerates recrystallization.\n"
                                "2. **Pressure**:\n"
                                "   - *Confining (Lithostatic) Pressure*: Equal squeezing from all sides due to burial depth.\n"
                                "   - *Directed (Differential) Pressure*: Unequal tectonic stress that flattens and aligns minerals into parallel bands.\n"
                                "3. **Chemically Active Hydrothermal Fluids**: Superheated groundwater rich in dissolved ions that speeds up chemical reactions and transfers new mineral elements."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Agents of Metamorphism & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Agents of Metamorphism",
                        "content": {
                            "caption": "Three-panel graphic displaying Thermal Magma Baking (Heat), Tectonic Collision Stress (Directed Pressure), and Hydrothermal Fluid Circulation."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Precambrian Basement System",
                        "content": {
                            "text": (
                                "Metamorphic rocks form the solid geological foundation of Kenya, known as the **Precambrian Basement System**. "
                                "These ancient rocks are exposed across Machakos, Kitui, and Taita-Taveta, where intense regional metamorphism produced "
                                "high-grade metamorphic rocks that host world-famous gemstone deposits like tsavorite garnets and rubies."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Non-Agent of Metamorphism",
                        "content": {
                            "question": "Which of the following is NOT an agent of metamorphism?",
                            "options": [
                                "Directed tectonic pressure",
                                "Extreme subterranean heat",
                                "Surface wind and river transportation",
                                "Chemically active hydrothermal fluids"
                            ],
                            "correct_answer": "Surface wind and river transportation",
                            "explanation": "Wind and river transport are exogenic agents of surface sedimentary erosion, not endogenic agents of metamorphic alteration."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Solid-State Transformation",
                        "content": {
                            "question": "What happens to a rock's minerals during true metamorphism?",
                            "options": [
                                "They melt completely into liquid magma",
                                "They recrystallize in a solid state, forming new and denser mineral structures",
                                "They dissolve in rainwater and evaporate into gas",
                                "They are ground into loose beach sand"
                            ],
                            "correct_answer": "They recrystallize in a solid state, forming new and denser mineral structures",
                            "explanation": "Metamorphism is strictly a solid-state process; if temperature rises high enough to melt the rock into liquid, it enters the igneous cycle upon cooling."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 10: Types of Metamorphism
    {
        "unit_order": 10,
        "unit_name": "Types of Metamorphism",
        "lesson_title": "Types of Metamorphism",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geological Settings of Transformation & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Metamorphic Aureole and Tectonic Deformation",
                        "content": {"text": "A geological formation showing a dark baked metamorphic zone surrounding an intrusive igneous contact zone."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Types of Metamorphism",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Compare Contact (thermal), Dynamic, and Regional metamorphism\n"
                                "- Explain how metamorphic aureoles form adjacent to subterranean magma intrusions\n"
                                "- Describe regional metamorphism as a continental-scale mountain-building process"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Bonfires vs. Widespread Storms",
                        "content": {
                            "text": (
                                "If you stand near a blazing bonfire, you only feel intense heat right next to the flames. "
                                "This is like **contact metamorphism**—only the rocks touching the hot magma body are baked. "
                                "But when a massive storm hits an entire county, everything across hundreds of square kilometers is affected. "
                                "This is like **regional metamorphism**, which crushes and cooks whole mountain belts during tectonic collisions!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Metamorphic Types",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Metamorphism Types",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Contact (Thermal) Metamorphism",
                                    "definition": "Localized metamorphism caused primarily by intense heat from an invading subterranean body of magma baking surrounding country rocks.",
                                    "simple": "Baking of rocks directly touching hot underground magma."
                                },
                                {
                                    "term": "Dynamic Metamorphism",
                                    "definition": "Metamorphism occurring along fault zones driven primarily by intense directional mechanical pressure and shearing.",
                                    "simple": "Mechanical crushing and grinding of rocks along earthquake fault lines."
                                },
                                {
                                    "term": "Regional Metamorphism",
                                    "definition": "Widespread metamorphism occurring over vast areas of the crust during major tectonic plate collisions, driven by both high heat and intense directed pressure.",
                                    "simple": "Massive mountain-scale squeezing and baking during continental collisions."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Comparative Summary of Metamorphic Environments",
                        "content": {
                            "text": (
                                "| Metamorphism Type | Primary Agent | Spatial Scale | Typical Setting |\n"
                                "| :--- | :--- | :--- | :--- |\n"
                                "| **Contact** | Extreme Heat | Localized (meters to km) | Around magma chambers, dykes, sills (Aureole) |\n"
                                "| **Dynamic** | Directed Pressure | Narrow fault zones | Major active fault planes (Mylonites) |\n"
                                "| **Regional** | Heat + Pressure | Massive (1,000s of km²) | Mountain-building continental collision zones |"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Contact vs. Regional Settings & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Contact vs. Regional Metamorphism Settings",
                        "content": {
                            "caption": "Comparison of a localized thermal bake zone (Contact Aureole) around a pluton vs. crustal deformation across a continental collision zone (Regional)."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: The Taita Hills Gneisses",
                        "content": {
                            "text": (
                                "The ancient metamorphic rock formations of the **Taita Hills** in southern Kenya formed during the Mozambique Orogenic Belt collision "
                                "over 500 million years ago. Intense regional metamorphism folded and recrystallized ancient sedimentary and volcanic rocks into high-grade gneisses."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Magma Aureole Formation",
                        "content": {
                            "question": "Which type of metamorphism is localized and occurs when surrounding rocks are baked by an invading body of magma?",
                            "options": [
                                "Regional Metamorphism",
                                "Contact Metamorphism",
                                "Dynamic Metamorphism",
                                "Evaporative Metamorphism"
                            ],
                            "correct_answer": "Contact Metamorphism",
                            "explanation": "Contact (thermal) metamorphism occurs locally in the zone (aureole) immediately surrounding an intrusive magma body where extreme heat is the main transforming agent."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Continental-Scale Metamorphism",
                        "content": {
                            "question": "Regional metamorphism operates on a massive geographic scale and is characterized by which conditions?",
                            "options": [
                                "Only cool groundwater circulating in cracks",
                                "Simultaneous intense heat and high directed pressure during continental plate collisions",
                                "Solar evaporation of saltwater in desert basins",
                                "Quick cooling of lava on volcanic cones"
                            ],
                            "correct_answer": "Simultaneous intense heat and high directed pressure during continental plate collisions",
                            "explanation": "Regional metamorphism is driven by deep tectonic compression and high geothermal heat during mountain-building events, affecting thousands of square kilometers."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 11: Metamorphic Textures and Parent Rocks
    {
        "unit_order": 11,
        "unit_name": "Metamorphic Textures and Parent Rocks",
        "lesson_title": "Metamorphic Textures and Parent Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Banded Textures & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Foliated Banded Gneiss Specimen",
                        "content": {"text": "A close-up view of a gneiss rock specimen displaying distinct alternating dark biotite and light quartz-feldspar foliation bands."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Metamorphic Textures and Protoliths",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish between foliated and non-foliated metamorphic textures\n"
                                "- Explain how directed tectonic pressure produces foliation banding\n"
                                "- Match metamorphic rocks directly to their respective parent rocks (protoliths)"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Squeezing Playing Cards",
                        "content": {
                            "text": (
                                "If you stack playing cards loosely and squeeze them from the sides, they all align parallel to each other, forming tight flat sheets. "
                                "Similarly, when a rock contains flat mineral flakes (like mica) and is squeezed under directed tectonic pressure, "
                                "the minerals rotate and grow in parallel stripes perpendicular to the stress. This is called **foliation**!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Foliated vs. Non-Foliated",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Texture Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Foliation",
                                    "definition": "The parallel alignment of platy or elongated mineral grains in a metamorphic rock, produced by directed differential pressure.",
                                    "simple": "Banding or striping in metamorphic rocks."
                                },
                                {
                                    "term": "Non-Foliated Texture",
                                    "definition": "Metamorphic rocks that lack a banded structure, typically composed of interlocking crystals of a single mineral (e.g., calcite or quartz).",
                                    "simple": "Uniform, unstriped metamorphic rocks formed without directed pressure."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Foliated vs. Non-Foliated Varieties",
                        "content": {
                            "text": (
                                "- **Foliated Rocks** (Ordered by increasing metamorphic grade):\n"
                                "  1. *Slate*: Very fine grains, splits along flat sheets (from Shale).\n"
                                "  2. *Schist*: Medium grains with visible glittering mica flakes.\n"
                                "  3. *Gneiss*: Coarse alternating light (quartz/feldspar) and dark (biotite/amphibole) bands (from Granite).\n\n"
                                "- **Non-Foliated Rocks**:\n"
                                "  1. *Marble*: Interlocking calcite crystals, fizzes with acid (from Limestone).\n"
                                "  2. *Quartzite*: Extremely hard interlocking quartz grains (from Sandstone)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Parent Rock Matrix & Kenya Case Study",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Parent Rocks and Metamorphic Transformation Matrix",
                        "content": {
                            "caption": "Direct mapping connecting Granite -> Gneiss, Shale -> Slate, Limestone -> Marble, and Sandstone -> Quartzite."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Kajiado Marble",
                        "content": {
                            "text": (
                                "In **Kajiado County**, ancient sedimentary limestones within the Precambrian Basement were subjected to high-grade "
                                "thermal and regional metamorphism, transforming them into high-purity **marble**. This marble is quarried and processed "
                                "in Athi River for architectural tiles, decorative stone, and industrial lime."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Limestone Protolith Transformation",
                        "content": {
                            "question": "Which metamorphic rock is formed when sedimentary limestone is subjected to high temperature and recrystallizes?",
                            "options": [
                                "Slate",
                                "Gneiss",
                                "Quartzite",
                                "Marble"
                            ],
                            "correct_answer": "Marble",
                            "explanation": "Marble is the non-foliated metamorphic rock produced by the thermal recrystallization of parent limestone (calcium carbonate)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Cause of Foliation",
                        "content": {
                            "question": "Foliation is a banded rock texture produced primarily by which metamorphic agent?",
                            "options": [
                                "Acidic groundwater dissolution",
                                "Directed differential tectonic pressure",
                                "Gentle subterranean heating without stress",
                                "Evaporation of mineral-rich saltwater"
                            ],
                            "correct_answer": "Directed differential tectonic pressure",
                            "explanation": "Foliation requires directed pressure (differential stress) to squash and orient mineral grains perpendicular to the direction of compressive force."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 12: Classification of Rocks by Geological Age
    {
        "unit_order": 12,
        "unit_name": "Classification of Rocks by Geological Age",
        "lesson_title": "Classification of Rocks by Geological Age",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geological Time & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Geological Stratigraphy Column in Rock Cliff",
                        "content": {"text": "A geological stratigraphy outcrop displaying successive chronological layers representing ancient geological eras."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Geological Age of Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain the Geological Time Scale and distinguish between relative and absolute dating\n"
                                "- Describe the four primary geological eras: Precambrian, Paleozoic, Mesozoic, and Cenozoic\n"
                                "- Correlate major rock formations in Kenya with their respective geological eras"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Reading the Rock Archive",
                        "content": {
                            "text": (
                                "How do we know the age of an ancient castle? We can read municipal records or check the date carved into its cornerstone. "
                                "For planet Earth, the rock layers are the pages of a giant history book. Fossils act as illustrations, "
                                "and radioactive isotopes in minerals act as precise digital date stamps!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & The Four Geological Eras",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Geological Time Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Geological Time Scale",
                                    "definition": "A calendar of Earth's 4.6-billion-year history dividing geological time into eons, eras, periods, and epochs based on stratigraphy and fossil records.",
                                    "simple": "The chronological timeline of Earth's history."
                                },
                                {
                                    "term": "Relative Dating",
                                    "definition": "Determining whether a rock layer is older or younger than another using principles of stratigraphy (such as Superposition: lower layers are older).",
                                    "simple": "Knowing which rock came first without giving an exact number."
                                },
                                {
                                    "term": "Absolute Dating",
                                    "definition": "Measuring the precise numerical age of a rock in millions of years using the radiometric decay rates of radioactive isotopes.",
                                    "simple": "Finding the exact calendar age of a rock in years."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Four Major Geological Eras",
                        "content": {
                            "text": (
                                "1. **Precambrian Era (Over 541 Million Years Ago)**: Ancient continental basement rocks; highly folded metamorphic rocks and granites lacking complex fossils.\n"
                                "2. **Paleozoic Era (541 to 252 Million Years Ago)**: Era of early life; ancient marine sandstones, shales, and limestones containing early marine fossils.\n"
                                "3. **Mesozoic Era (252 to 66 Million Years Ago)**: 'Age of Reptiles'; sedimentary rocks including coastal sandstones, shales, and coal beds.\n"
                                "4. **Cenozoic Era (66 Million Years Ago to Present)**: 'Age of Mammals'; young rocks including Rift Valley volcanics (basalt, phonolite) and recent lake/river sediments."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Stratigraphy Pillar & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "The Geological Stratigraphy Pillar",
                        "content": {
                            "caption": "Vertical column illustrating the 4 major geological eras from deep Precambrian basement to surface Cenozoic volcanic strata."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Relevance: Spanning Geological Eras",
                        "content": {
                            "text": (
                                "Kenya's rocks span these eras beautifully:\n\n"
                                "- **Precambrian**: Basement System metamorphic rocks and western granites (over 500 million years old).\n"
                                "- **Mesozoic**: Coastal sandstones in the Mombasa hinterland.\n"
                                "- **Cenozoic**: Rift Valley volcanic rocks, Mount Kenya basalts, and Lake Magadi evaporites (very young in geological terms)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Youngest Rocks in Kenya",
                        "content": {
                            "question": "Which geological era is associated with the youngest rocks in Kenya, including the volcanic rocks of the Rift Valley?",
                            "options": [
                                "Precambrian",
                                "Paleozoic",
                                "Mesozoic",
                                "Cenozoic"
                            ],
                            "correct_answer": "Cenozoic",
                            "explanation": "The Cenozoic era covers the last 66 million years to the present and includes all volcanic rocks associated with the Great Rift Valley rifting in Kenya."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Absolute Dating Method",
                        "content": {
                            "question": "How do geologists determine the absolute numerical age of a rock specimen in millions of years?",
                            "options": [
                                "By counting the number of visible strata in a cliff",
                                "By analyzing the radioactive decay rate of isotopes within mineral crystals",
                                "By measuring how smooth the rock surface has become",
                                "By estimating how deeply the rock was buried"
                            ],
                            "correct_answer": "By analyzing the radioactive decay rate of isotopes within mineral crystals",
                            "explanation": "Radiometric dating measures the known half-life decay of radioactive parent isotopes to stable daughter isotopes, providing an absolute age in years."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 13: Distribution of Rocks in Kenya - Part 1
    {
        "unit_order": 13,
        "unit_name": "Distribution of Rocks in Kenya - Part 1",
        "lesson_title": "Distribution of Rocks in Kenya - Part 1",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Ancient Foundation & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Precambrian Basement System Rocks in Kenya",
                        "content": {"text": "A panoramic view of ancient rocky hills and granite tor outcrops in the eastern plains of Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Rock Distribution - Part 1",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify the geographical distribution of ancient Precambrian Basement System rocks across Kenya\n"
                                "- Describe the metamorphic rock types characteristic of the Kenyan Basement System\n"
                                "- Locate major granitic plutonic intrusions in western Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Bedrock of the Nation",
                        "content": {
                            "text": (
                                "Imagine travelling from Mombasa up through Taru and Taita, across to Machakos, Kitui, and western Kenya. "
                                "Across these wide expanses, you see hard, grey, banded metamorphic hills. If you drilled deep below Nairobi's young volcanic stones, "
                                "you would strike these exact same ancient rocks. They form Kenya's deep geological 'basement floor'!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Basement System Geology",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Basement Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Basement System Rocks",
                                    "definition": "Ancient Precambrian metamorphic and igneous rocks (over 500 million years old) forming the deep crustal foundation of Kenya.",
                                    "simple": "The ancient geological bedrock beneath Kenya."
                                },
                                {
                                    "term": "Granitic Pluton",
                                    "definition": "Massive bodies of granite magma that intruded the ancient crust, cooled slowly, and have been exposed by subsequent erosion.",
                                    "simple": "Giant plugs of underground granite now visible at the surface."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Distribution of Precambrian Provinces in Kenya",
                        "content": {
                            "text": (
                                "1. **Precambrian Basement System Rocks**:\n"
                                "   - *Eastern & Central*: Machakos, Kitui, Makueni, and Embu hills.\n"
                                "   - *Northern*: Northern Turkana, Marsabit, and Samburu plains.\n"
                                "   - *Coast Hinterland*: Taita Hills and Taru Desert.\n"
                                "   - *Dominant Rocks*: Gneisses, schists, marbles, quartzites, and granulites.\n\n"
                                "2. **Plutonic Intrusive Granites**:\n"
                                "   - *Western Kenya*: Kakamega, Vihiga, Kisumu, and Lake Victoria basin.\n"
                                "   - *Dominant Rocks*: Coarse-grained granites and syenites forming dramatic tor landforms."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Geological Mapping & Kisii Soapstone Case Study",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Kenya Geological Map: Precambrian Basement & Plutons",
                        "content": {
                            "caption": "Map highlighting extensive eastern, northern, and coastal hinterland Precambrian Basement exposures alongside western Kenya Plutonic Granites."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Kisii Soapstone (Tabaka)",
                        "content": {
                            "text": (
                                "In the **Kisii Highlands (Tabaka)**, ancient volcanic rocks within the Precambrian system underwent hydrothermal alteration, "
                                "forming a unique, soft, dense metamorphic rock known as **soapstone (Kisii stone)**. Local artisans quarry and carve it "
                                "into world-renowned sculptures and ornaments, supporting thousands of rural livelihoods."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Exposed Basement Regions",
                        "content": {
                            "question": "In which of the following Kenyan regions are ancient Precambrian Basement System gneisses and schists extensively exposed?",
                            "options": [
                                "The floor of the Nakuru Rift Valley",
                                "The summit of Mount Longonot",
                                "The dry highlands of Machakos and Kitui",
                                "The sandy beaches of Malindi"
                            ],
                            "correct_answer": "The dry highlands of Machakos and Kitui",
                            "explanation": "Machakos and Kitui represent the classic eastern exposure of Kenya's ancient Precambrian metamorphic basement floor."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Ballast Granite Classification",
                        "content": {
                            "question": "The massive granitic tors quarried for construction ballast around Kisumu and Kakamega belong to which rock class?",
                            "options": [
                                "Cenozoic Volcanic Extrusive",
                                "Plutonic Intrusive",
                                "Marine Organically Formed Sedimentary",
                                "Mesozoic Chemical Evaporite"
                            ],
                            "correct_answer": "Plutonic Intrusive",
                            "explanation": "These granites are plutonic igneous intrusions that cooled slowly deep within the crust and were subsequently unroofed by surface erosion."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 14: Distribution of Rocks in Kenya - Part 2
    {
        "unit_order": 14,
        "unit_name": "Distribution of Rocks in Kenya - Part 2",
        "lesson_title": "Distribution of Rocks in Kenya - Part 2",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Volcanic Zones & Sedimentary Belts & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Great Rift Valley Escarpment and Volcanic Cones",
                        "content": {"text": "A dramatic view of the Great Rift Valley escarpment showing volcanic cones, flat lava plains, and lake sedimentary basins."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Rock Distribution - Part 2",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Map the distribution of Cenozoic volcanic rocks along the Rift Valley and central highlands\n"
                                "- Describe the distribution of coastal marine, inland lake, and Karoo sedimentary belts in Kenya\n"
                                "- Synthesize a comprehensive geological distribution map of Kenya"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Standing on the Rift Edge",
                        "content": {
                            "text": (
                                "When you stand on the Limuru Escarpment looking across the Rift Valley floor, you are looking at a geological masterpiece. "
                                "The volcanic mountains (Longonot, Suswa), the black basaltic lava flows, and the soft ash plains were all created "
                                "by Cenozoic volcanic activity associated with the tearing apart of the African tectonic plate!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Volcanic/Sedimentary Belts",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Province Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Volcanic Province",
                                    "definition": "The central geographical belt of Kenya associated with the East African Rift Valley covered by young Cenozoic extrusive igneous rocks.",
                                    "simple": "The central corridor of volcanic lavas and mountains in Kenya."
                                },
                                {
                                    "term": "Sedimentary Basin",
                                    "definition": "Low-lying regional depressions where thick layers of marine, lacustrine (lake), or fluvial (river) sediments have accumulated.",
                                    "simple": "Coastal and lake basins containing layered sedimentary rocks."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Two Major Geological Provinces in Part 2",
                        "content": {
                            "text": (
                                "1. **Cenozoic Volcanic Rocks (Central Corridor)**:\n"
                                "   - *Key Areas*: Rift Valley floor, Aberdare Range, Mount Kenya, Mau Escarpment, and Chyulu Hills.\n"
                                "   - *Dominant Rocks*: Basalt, phonolite, trachyte, obsidian, pumice, and volcanic tuff.\n\n"
                                "2. **Sedimentary Rock Belts**:\n"
                                "   - *Coastal Sedimentary Belt*: Marine sandstones, shales, and coral limestones (Mombasa, Kilifi, Kwale).\n"
                                "   - *Rift & Lake Basins*: Lacustrine clays and diatomites (Lake Victoria basin, Kariandusi, Lake Magadi).\n"
                                "   - *Karoo Sediments*: Ancient Permian-Triassic sandstone/shale beds at Maji ya Chumvi."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Comprehensive Kenya Rock Map & Yatta Plateau",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Comprehensive Geological Map of Kenya",
                        "content": {
                            "caption": "Complete nationwide map showing Central Rift Volcanics, Coastal Sedimentary Strip, Eastern/Northern Basement System, and Western Granites/Sediments."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: The Yatta Plateau",
                        "content": {
                            "text": (
                                "The **Yatta Plateau** is a globally unique volcanic geological formation. Stretching for 290 kilometers from Ol Donyo Sabuk "
                                "to Tsavo, it is the longest continuous lava flow in the world! Fluid Cenozoic phonolitic lava flowed down an ancient river valley; "
                                "over millions of years, the surrounding soft land eroded away, leaving the hardened lava valley standing as a high elevated plateau."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Volcanic Highland Range",
                        "content": {
                            "question": "Which of the following Kenyan highland ranges is made primarily of Cenozoic volcanic rocks associated with the Rift Valley?",
                            "options": [
                                "Taita Hills",
                                "Aberdare Ranges",
                                "Kisii Highlands",
                                "Kitui Hills"
                            ],
                            "correct_answer": "Aberdare Ranges",
                            "explanation": "The Aberdare Ranges, Mount Kenya, and the Mau Escarpment are Cenozoic volcanic formations, whereas Taita and Kitui are ancient Precambrian basement hills."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Marine Sedimentary Belt Location",
                        "content": {
                            "question": "Where in Kenya are Mesozoic and Cenozoic marine sedimentary rocks (like coral limestone and sandstones) most prominent?",
                            "options": [
                                "Along the shores of Lake Victoria",
                                "On the summits of Mount Elgon",
                                "Along the Indian Ocean coastal strip",
                                "On the floor of the Kerio Valley"
                            ],
                            "correct_answer": "Along the Indian Ocean coastal strip",
                            "explanation": "The Kenyan coastal strip contains extensive marine sedimentary deposits formed during ancient sea transgressions."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 15: Economic Significance of Rocks in Kenya
    {
        "unit_order": 15,
        "unit_name": "Economic Significance of Rocks in Kenya",
        "lesson_title": "Economic Significance of Rocks in Kenya",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Powering Development & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Hell's Gate Volcanic Cliffs and Olkaria Geothermal Steam",
                        "content": {"text": "Geothermal power plant steam plumes rising against towering volcanic rock cliffs in the Kenyan Rift Valley."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Economic Significance of Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify essential construction and building materials extracted from Kenyan rocks\n"
                                "- Explain how subterranean volcanic rocks power Kenya's geothermal energy sector\n"
                                "- Analyze the vital role of rocks in fertile soil formation and groundwater aquifers"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: The Foundation of Modern Cities",
                        "content": {
                            "text": (
                                "Look around your school and neighborhood: concrete walls, cemented floors, gravel driveways, and asphalt highways—where did they all come from? "
                                "They are crushed, cut, and processed rocks! Modern cities like Nairobi, Mombasa, and Kisumu literally rest on rock foundations."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Key Economic Sectors",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Economic Geology Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Geothermal Reservoir",
                                    "definition": "Permeable subterranean volcanic rock formations that trap superheated groundwater and steam capable of spinning electrical turbines.",
                                    "simple": "Hot underground rocks that boil water into electricity-generating steam."
                                },
                                {
                                    "term": "Aquifer",
                                    "definition": "An underground layer of permeable rock, sand, or gravel that stores and transmits usable supplies of groundwater to wells and boreholes.",
                                    "simple": "An underground rock sponge that holds drinking water."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Economic Applications of Kenyan Rocks",
                        "content": {
                            "text": (
                                "1. **Construction Materials**:\n"
                                "   - *Ballast*: Crushed basalt, phonolite, and granite for concrete, railways (SGR), and tarmac roads.\n"
                                "   - *Building Blocks*: Soft volcanic tuffs quarried around Nairobi and Machakos.\n"
                                "   - *Cement*: Coastal and Athi River limestones crushed and fired in kilns.\n\n"
                                "2. **Agriculture & Soils**:\n"
                                "   - Weathering of basic volcanic basalts creates nutrient-rich red agricultural soils in the Kenya Highlands.\n\n"
                                "3. **Clean Energy & Water**:\n"
                                "   - *Olkaria Geothermal Power*: Underground heat in Rift volcanic rocks generates over 800 MW of clean electricity.\n"
                                "   - *Aquifers*: Permeable sandstones and fractured basalts provide clean water for rural and urban boreholes."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Energy & Industrial Cycles & Kenya Context",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Economic Applications of Rocks: Geothermal Power & Infrastructure",
                        "content": {
                            "caption": "Diagram linking underground geothermal steam generation at Olkaria, rock quarrying for cement and ballast, and aquifer groundwater storage."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Athi River Cement Hub",
                        "content": {
                            "text": (
                                "The town of **Athi River** is Kenya's industrial cement manufacturing hub. Factories like Bamburi Cement, Savannah Cement, "
                                "and East African Portland Cement depend entirely on limestone and gypsum rocks transported from regional deposits "
                                "to supply the nation's rapid infrastructure boom."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Raw Material for Cement",
                        "content": {
                            "question": "Which rock type is the most critical mineral raw material for the manufacturing of cement in Kenya?",
                            "options": [
                                "Granite",
                                "Basalt",
                                "Limestone",
                                "Obsidian"
                            ],
                            "correct_answer": "Limestone",
                            "explanation": "Limestone (calcium carbonate) is the indispensable chemical raw material heated in cement kilns to make clinker and cement."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Geothermal Electricity Generation",
                        "content": {
                            "question": "How do underground volcanic rocks contribute to Kenya's leading renewable energy sector at Olkaria?",
                            "options": [
                                "Volcanic ash is burned as coal in furnaces",
                                "Deep volcanic heat superheats groundwater into high-pressure steam that spins turbines",
                                "Obsidian crystals are polished to generate solar electricity",
                                "Pumice blocks are used to construct hydroelectric dams"
                            ],
                            "correct_answer": "Deep volcanic heat superheats groundwater into high-pressure steam that spins turbines",
                            "explanation": "Olkaria harnesses subterranean volcanic heat stored in permeable rocks to produce high-pressure steam that powers electrical turbines."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 16: Environmental, Tourism, and Cultural Significance of Rocks
    {
        "unit_order": 16,
        "unit_name": "Environmental, Tourism, and Cultural Significance of Rocks",
        "lesson_title": "Environmental, Tourism, and Cultural Significance of Rocks",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Scenic Heritage & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Kit Mikayi Balancing Rock Tor in Kisumu",
                        "content": {"text": "A towering view of Kit Mikayi granitic balancing rocks rising above the green landscape of western Kenya."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Cultural and Tourism Value of Rocks",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how scenic rock landforms drive international and domestic tourism in Kenya\n"
                                "- Describe the cultural, spiritual, and historical significance of sacred rock monuments\n"
                                "- Analyze the role of rock shelters and caves in preserving prehistoric archaeological evidence"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Fischer's Tower and Folklore",
                        "content": {
                            "text": (
                                "At Hell's Gate National Park in Naivasha, a 25-meter-tall volcanic rock pillar called **Fischer's Tower** stands guard over the gorge. "
                                "Local Maasai traditions tell folklore of a petrified maiden turned to stone. Beyond geology, rocks inspire human stories, art, and national heritage!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Scenic / Cultural Value",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Geomorphology & Heritage Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Tor",
                                    "definition": "A prominent, free-standing rocky outcrop or tower, typically composed of jointed granite, formed by subsurface chemical weathering followed by erosion of surrounding saprolite.",
                                    "simple": "A dramatic natural stack of balancing granite boulders."
                                },
                                {
                                    "term": "Rock Shelter",
                                    "definition": "A shallow, cave-like opening beneath an overhanging rock cliff used by early prehistoric humans for living quarters and ceremonial art.",
                                    "simple": "A natural overhanging rock cliff used as a prehistoric home."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Tourism and Cultural Pillars",
                        "content": {
                            "text": (
                                "1. **Scenic Eco-Tourism**:\n"
                                "   - *Mount Kenya Peaks*: Batian and Nelion volcanic plugs attract mountaineers worldwide.\n"
                                "   - *Hell's Gate Gorges*: Spectacular volcanic cliffs popular with rock climbers and hikers.\n"
                                "   - *Granitic Tors*: Kakamega, Vihiga, and Kisumu balancing rocks.\n\n"
                                "2. **Cultural & Archaeological Heritage**:\n"
                                "   - *Sacred Sites*: Kit Mikayi and local shrines used for community prayer, rainmaking ceremonies, and meditation.\n"
                                "   - *Archaeological Archives*: Caves in sedimentary and volcanic strata (e.g., Kariandusi, Lewa) preserve stone age tools and early hominid fossils."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Geomorphology Infographic & Kit Mikayi Case Study",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Tourism and Cultural Heritage of Kenyan Rock Formations",
                        "content": {
                            "caption": "Infographic showing scenic granitic tors (Kit Mikayi), volcanic canyon walls (Hell's Gate), and prehistoric rock shelter caves."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenyan Case Study: Kit Mikayi National Monument",
                        "content": {
                            "text": (
                                "**Kit Mikayi** (meaning 'the stone of the first wife' in Dholuo) is a world-famous granitic tor near Kisumu. "
                                "Officially gazetted as a UNESCO-inscribed national cultural monument, it attracts thousands of tourists while serving "
                                "as a revered spiritual shrine for local communities, exemplifying how geology and human culture intertwine."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Sacred Granitic Tor",
                        "content": {
                            "question": "Which spectacular granitic tor near Kisumu is both a major tourist attraction and a protected cultural shrine for local communities?",
                            "options": [
                                "Fischer's Tower",
                                "Kit Mikayi",
                                "The Yatta Plateau",
                                "Menengai Crater"
                            ],
                            "correct_answer": "Kit Mikayi",
                            "explanation": "Kit Mikayi is a renowned granitic tor in Seme, Kisumu County, celebrated for its unique balancing boulders and deep cultural heritage."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Archaeological Value of Rock Shelters",
                        "content": {
                            "question": "Why are rock shelters and caves in sedimentary and volcanic strata highly valued by geographers and historians?",
                            "options": [
                                "They contain vast pools of refined petrol",
                                "They naturally protect and preserve archaeological fossils, stone tools, and ancient rock art from weathering",
                                "They produce commercial pumice scrubbing stones",
                                "They stop tectonic earthquakes from occurring"
                            ],
                            "correct_answer": "They naturally protect and preserve archaeological fossils, stone tools, and ancient rock art from weathering",
                            "explanation": "Rock shelters shield delicate prehistoric artifacts, fossilized bones, and rock paintings from rain and wind erosion."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 17: Field Study - Planning and Sampling Rocks in Your Locality
    {
        "unit_order": 17,
        "unit_name": "Field Study - Planning and Sampling Rocks in Your Locality",
        "lesson_title": "Field Study - Planning and Sampling Rocks in Your Locality",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geological Fieldwork & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Geology Field Study Equipment and Sampling",
                        "content": {"text": "A student geographer equipped with safety goggles, geological hammer, hand lens, and labeled sample bags sampling a rock outcrop."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Fieldwork Planning and Sampling",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Formulate a comprehensive equipment checklist for safe geological rock sampling\n"
                                "- Identify suitable, safe field sampling sites and adhere strictly to field safety protocols\n"
                                "- Record systematic geological observations (color, texture, mineral grains, coordinates) in a field notebook"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Becoming Field Geologists",
                        "content": {
                            "text": (
                                "True geographers don't just read about rocks in textbooks—they step outside into the field! "
                                "A nearby dry stream bed, a roadside rock cut, or a school quarry is an open geological laboratory. "
                                "Today, we learn how to prepare, conduct, and safely execute a scientific rock-sampling inquiry."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Equipment / Safety Protocols",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Fieldwork Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Geological Field Inquiry",
                                    "definition": "The systematic on-site collection, observation, spatial recording, and physical testing of rock and landform data in the field.",
                                    "simple": "Scientific outdoor fieldwork to study and collect real rock specimens."
                                },
                                {
                                    "term": "Outcrop",
                                    "definition": "A visible exposure of solid bedrock projecting through the overlying soil or vegetation on the Earth's surface.",
                                    "simple": "Exposed natural bedrock visible above ground."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Equipment Checklist & Mandatory Safety Rules",
                        "content": {
                            "text": (
                                "1. **Essential Gear Checklist**:\n"
                                "   - Geological hammer & chisel (to expose fresh, unweathered rock surfaces).\n"
                                "   - Hand lens (10x magnifying glass to inspect mineral grains).\n"
                                "   - Labeled sample bags, permanent marker, and masking tape.\n"
                                "   - Safety goggles (mandatory eye protection) and heavy work gloves.\n"
                                "   - Field notebook, pencil, GPS receiver, and First Aid kit.\n\n"
                                "2. **Field Safety Protocols**:\n"
                                "   - **Always wear safety goggles** when striking rocks with a hammer.\n"
                                "   - **Stay clear of unstable active quarry walls** or steep loose talus slopes.\n"
                                "   - **Never touch overgrown crevices** with bare hands where snakes or scorpions might hide.\n"
                                "   - **Never taste unknown mineral specimens**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Field Sampling Guide & Data Recording",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Geologist's Fieldwork Equipment & Safety Protocol Guide",
                        "content": {
                            "caption": "Guide illustrating proper field attire, geological hammer technique with eye goggles, specimen bagging, and notebook data recording."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Systematic Field Data Recording",
                        "content": {
                            "text": (
                                "For every specimen collected, record in your field notebook:\n"
                                "- **Sample Number**: (e.g., Specimen G10-01)\n"
                                "- **Exact Location**: GPS coordinates and physical description (e.g., riverbank, 50m west of bridge)\n"
                                "- **Fresh Surface Color vs Weathered Outer Color**\n"
                                "- **Texture**: (Grain size, rough, smooth, crystalline, or layered)\n"
                                "- **Bedding / Joint Orientation**: (Horizontal strata, vertical fracture)"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Mandatory Eye Protection",
                        "content": {
                            "question": "Which piece of personal protective equipment is most critical when breaking rock specimens with a geological hammer?",
                            "options": [
                                "A 10x hand lens",
                                "Safety goggles (protective eyewear)",
                                "A digital camera",
                                "A plastic sample bag"
                            ],
                            "correct_answer": "Safety goggles (protective eyewear)",
                            "explanation": "Striking rocks with a steel hammer produces high-velocity, razor-sharp rock chips that can cause permanent eye damage without safety goggles."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Recording Field Location",
                        "content": {
                            "question": "Why is recording the precise spatial location and context of each rock specimen essential during a geological inquiry?",
                            "options": [
                                "To prevent classmates from borrowing the sample",
                                "To ensure rocks can be returned to their exact spots after class",
                                "To map spatial distribution and connect rock types with underlying geological formations",
                                "To calculate the retail selling price of the rock"
                            ],
                            "correct_answer": "To map spatial distribution and connect rock types with underlying geological formations",
                            "explanation": "Spatial context allows geographers to map geological formations, trace strata continuity, and understand regional environmental history."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 18: Field Study - Classification, Display, and Topic Review
    {
        "unit_order": 18,
        "unit_name": "Field Study - Classification, Display, and Topic Review",
        "lesson_title": "Field Study - Classification, Display, and Topic Review",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Laboratory Analysis & Learning Goals",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Geological Rock and Mineral Collection Display Case",
                        "content": {"text": "A partitioned wooden rock collection display case with neatly labeled compartments for igneous, sedimentary, and metamorphic rock specimens."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Rock Classification and Display",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Apply a dichotomous identification key to classify collected field specimens into major rock groups\n"
                                "- Construct an organized, professionally labeled school rock display case\n"
                                "- Synthesize the complete Grade 10 Rocks topic through a structured review"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: From Raw Field Bags to School Museum",
                        "content": {
                            "text": (
                                "Now that we have safely returned from our field sampling with bags of raw rock specimens, how do we make sense of our collection? "
                                "We wash them, inspect fresh surfaces under a hand lens, perform simple diagnostic tests, classify them scientifically, "
                                "and curate a permanent school geology display!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Core Definitions & Dichotomous Identification Key",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Essential Lab Analysis Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Classification Key",
                                    "definition": "A step-by-step diagnostic guide used to identify rock classes and species based on observable physical traits (texture, crystal habit, reaction to acid).",
                                    "simple": "A decision tree to identify mystery rocks."
                                },
                                {
                                    "term": "Rock Display Case",
                                    "definition": "A partitioned cabinet or box designed to house, organize, protect, and exhibit labeled geological specimens for teaching and reference.",
                                    "simple": "A school rock museum box."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The 3-Step Dichotomous Identification Key",
                        "content": {
                            "text": (
                                "1. **Does the rock have visible layers (strata) or clastic grains?**\n"
                                "   - *Yes* -> **Sedimentary**\n"
                                "   - *Test*: Fizzes with dilute acid? -> **Limestone**; Visible sand grains? -> **Sandstone**; Muddy/crumbly? -> **Shale**.\n\n"
                                "2. **Is it crystalline/glassy without layers or foliation?**\n"
                                "   - *Yes* -> **Igneous**\n"
                                "   - *Test*: Coarse large crystals? -> **Granite** (Intrusive); Dark fine grains? -> **Basalt** (Extrusive); Glassy/porous? -> **Obsidian / Pumice**.\n\n"
                                "3. **Does it display parallel mineral banding (foliation) or hard crystalline recrystallization?**\n"
                                "   - *Yes* -> **Metamorphic**\n"
                                "   - *Test*: Banded light and dark stripes? -> **Gneiss**; Splits into hard flat sheets? -> **Slate**; Sugary calcite crystals? -> **Marble**."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Curating Display Cases & Laboratory Standards",
                "blocks": [
                    {
                        "block_type": "diagram",
                        "component_type": "diagram",
                        "title": "Scientific Rock Display Case & Dichotomous Key",
                        "content": {
                            "caption": "Curated display box partitioned into Igneous, Sedimentary, and Metamorphic sections with standardized museum index labels."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Standard Specimen Labeling Requirements",
                        "content": {
                            "text": (
                                "Every rock displayed in the school laboratory must have a neat index card with four mandatory fields:\n"
                                "1. **Assigned Rock Name**: (e.g., Basalt)\n"
                                "2. **Major Rock Class**: (e.g., Extrusive Igneous)\n"
                                "3. **Collection Site & County**: (e.g., Athi River Bed, Machakos County)\n"
                                "4. **Collector's Name & Date**: (e.g., Grade 10 Geography Class, March 2026)"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Check Your Understanding",
                "blocks": [
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Acid Effervescence Diagnostic Test",
                        "content": {
                            "question": "A student applies a drop of dilute hydrochloric acid (or lemon juice) to a grey rock specimen, and it immediately effervesces (fizzes). What is the rock most likely to be?",
                            "options": [
                                "Sandstone",
                                "Basalt",
                                "Limestone",
                                "Granite"
                            ],
                            "correct_answer": "Limestone",
                            "explanation": "Limestone is made of calcium carbonate (CaCO3), which reacts vigorously with acids to release carbon dioxide gas bubbles (effervescence)."
                        }
                    },
                    {
                        "block_type": "multiple_choice_question",
                        "component_type": "multiple_choice_question",
                        "title": "Formative Assessment: Value of Curated Rock Displays",
                        "content": {
                            "question": "What is the primary educational purpose of curating a permanent, labeled rock display case in the school geography laboratory?",
                            "options": [
                                "To sell specimens to road construction companies",
                                "To provide a permanent, structured physical reference for learners to master rock identification",
                                "To clear away discarded stones from the school playing fields",
                                "To decorate classroom window sills"
                            ],
                            "correct_answer": "To provide a permanent, structured physical reference for learners to master rock identification",
                            "explanation": "Curated displays serve as invaluable physical reference libraries, allowing students to touch and inspect real geological specimens."
                        }
                    }
                ]
            }
        ]
    }
]

def run_ingestion():
    print("=" * 80)
    print("VLearn Ingestion Engine: Grade 10 Geography — Topic 5: Rocks")
    print("=" * 80)

    with transaction.atomic():
        # 1. Verify Hierarchy
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        if not curriculum:
            raise RuntimeError("Curriculum 'CBC' not found!")

        grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
        if not grade:
            raise RuntimeError("Grade 10 not found under CBC!")

        subject = Subject.objects.filter(grade=grade, name="Geography").first()
        if not subject:
            raise RuntimeError("Subject 'Geography' not found under Grade 10!")

        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=5,
            defaults={
                "name": "Rocks",
                "description": "Comprehensive study of rocks and minerals, the rock cycle, igneous, sedimentary, and metamorphic rocks, geological time scale, distribution of rocks in Kenya, economic significance, and field study."
            }
        )
        topic.name = "Rocks"
        topic.description = "Comprehensive study of rocks and minerals, the rock cycle, igneous, sedimentary, and metamorphic rocks, geological time scale, distribution of rocks in Kenya, economic significance, and field study."
        topic.save()

        print(f"Target Topic: [{topic.id}] Grade 10 Geography - Topic 5: {topic.name}")

        # 2. Ingest 18 Lessons & Units
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
    print(f"Ingestion completed successfully for Grade 10 Geography Topic 5! (Total Blocks: {total_blocks_created})")
    print("=" * 80)

if __name__ == "__main__":
    run_ingestion()
