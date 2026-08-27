"""
VLearn CBC Grade 10 Geography — Topic 1: Introduction to Geography
Direct Programmatic Source-Driven Ingestion Engine

Subject: Geography (Grade 10, CBC)
Topic 1: Introduction to Geography
Source: Grade 10 Geography/01_introduction_to_geography.md

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade10_geography_topic1.py
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
    """Remove citation brackets ([1], [37], [S1, p. 1]) and normalize whitespace."""
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
# TOPIC 1 LESSON DEFINITIONS
# =============================================================================
LESSONS_DATA = [
    # Lesson 1: What is Geography?
    {
        "unit_order": 1,
        "unit_name": "What is Geography?",
        "lesson_title": "What is Geography?",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Exploring the World Through Geography",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Great Rift Valley: Landscape and Human Spatial Interaction",
                        "content": {"text": "A breathtaking panorama of the Great Rift Valley in Kenya, illustrating physical escarpments, volcanic terrain, and human settlements."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: What is Geography?",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Understand the definition and etymological origin of the term 'Geography'\n"
                                "- Explain the comprehensive scope of Geography as a field of spatial study\n"
                                "- Identify and describe the six key themes of Geography: Place, Space, Environment, Time, Movement, and Region\n"
                                "- Apply the six key themes to analyze your local Kenyan environment"
                            )
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Prerequisite Spark: Why and Where?",
                        "content": {
                            "text": (
                                "Think about your journey to school today. You passed hills, valleys, roads, market stalls, and farms. "
                                "Why are commercial shops positioned along major transport corridors rather than atop steep ridges? "
                                "Why do farmers cultivate maize in fertile volcanic highlands while pastoralists graze livestock in arid plains? "
                                "Geography is the scientific discipline that answers these fundamental 'where', 'why there', and 'what does it mean' questions!"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Etymology and Fundamental Definitions",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Core Geographical Definitions",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Geography",
                                    "definition": "The study of the Earth as the home of humankind, focusing on the dynamic spatial relationships between people and their physical and human environments.",
                                    "simple": "The scientific study of where features exist on Earth, why they are located there, and how humans interact with the planet."
                                },
                                {
                                    "term": "Space (Spatial Extent)",
                                    "definition": "A continuous expanse or area within which physical and cultural phenomena are distributed, positioned, and interact.",
                                    "simple": "The physical gap, interval, or distribution pattern between geographic features across the Earth's surface."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "The Greek Origins of Geography",
                        "content": {
                            "text": (
                                "The word **Geography** originates from two ancient Greek root words:\n\n"
                                "- **Geo** meaning the 'Earth'\n"
                                "- **Graphein** meaning 'to write about, describe, or map'\n\n"
                                "Ancient scholars like Eratosthenes first coined this term to describe systematic accounts of Earth's varied lands, climates, and peoples."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "The Six Key Themes of Geography",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Pillars of Spatial Thinking",
                        "content": {
                            "text": (
                                "Modern geographical inquiry is structured around **six fundamental themes**:\n\n"
                                "1. **Place**: Every location has distinctive physical characteristics (landforms, climate, soils) and human characteristics (settlements, languages, economic activities).\n"
                                "2. **Space & Spatial Distribution**: The arrangement and clustering of phenomena across the landscape—whether nucleated, linear, or dispersed.\n"
                                "3. **Environment**: The structure and natural functioning of the lithosphere (rocks), atmosphere (weather), hydrosphere (water), and biosphere (living organisms).\n"
                                "4. **Time**: The temporal evolution of landscapes. Geography examines historical changes to forecast future environmental and urban transformations.\n"
                                "5. **Movement**: The spatial flow and relocation of people, commodities, capital, and ideas, forging regional interdependence.\n"
                                "6. **Region**: Spatial areas unified by common physical, climatic, administrative, or socio-economic criteria."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Concept Map: The Six Pillars of Geographical Analysis",
                        "content": {
                            "text": "Interactive concept map illustrating how Place, Space, Environment, Time, Movement, and Region link to central Geographical Inquiry."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Kenyan Context & Real-World Synthesis",
                "blocks": [
                    {
                        "block_type": "real_world_example",
                        "component_type": "real_world_example",
                        "title": "Kenyan Case Study: Spatial Themes in the Great Rift Valley",
                        "content": {
                            "text": (
                                "Kenya's **Great Rift Valley** provides a vivid synthesis of all six geographical themes:\n\n"
                                "- **Place**: Features steep western and eastern escarpments, caldera volcanoes (Longonot, Suswa), and soda lakes (Nakuru, Bogoria).\n"
                                "- **Environment**: Unique geothermal reservoirs harnessed at Olkaria for clean electricity generation.\n"
                                "- **Movement**: Millions of lesser flamingos migrating between alkaline lakes, and freight flowing along the Northern Corridor.\n"
                                "- **Region**: Forms a distinct geological and agro-ecological belt dividing western and central Kenya."
                            )
                        }
                    },
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "Comparison: Tourist View vs. Geographer's Spatial Analysis",
                        "content": {
                            "headers": ["Aspect", "Tourist Observation", "Geographer's Spatial Analysis"],
                            "rows": [
                                ["Landscape", "Scenic view from the viewpoint", "Tectonic faulting and graben subsidence mechanism"],
                                ["Farming", "Green lush tea fields", "High altitude, volcanic soils, and orographic rainfall correlation"],
                                ["Settlement", "Busy highway town", "Linear settlement driven by transport nodal accessibility"],
                                ["Climate", "Cold morning air", "Adiabatic cooling associated with highland altitude (lapse rate)"]
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Visual Exploration & Demonstrations",
                "blocks": [
                    {
                        "block_type": "suggested_video",
                        "component_type": "suggested_video",
                        "title": "Introduction to Spatial Thinking and Geographic Inquiry",
                        "content": {
                            "resolved_video_id": "rCz_bY_n79Y",
                            "youtube_url": "https://www.youtube.com/watch?v=rCz_bY_n79Y",
                            "description": "Educational guide on how geographers analyze spatial distribution patterns, scale, and human-environment interactions."
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Key Takeaways from the Video",
                        "content": {
                            "text": "Observe how spatial thinking shifts our perspective from simply listing facts to uncovering root environmental causes and human adaptations."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Common Misconceptions & Exam Insights",
                "blocks": [
                    {
                        "block_type": "common_misconception",
                        "component_type": "common_misconception",
                        "title": "Common Exam Trap: Geography is Just Memorization",
                        "content": {
                            "misconception": "Geography is merely memorizing lists of capital cities, mountain heights, and national borders.",
                            "reality": "Geography is an analytical spatial science focused on explaining natural processes, cause-and-effect relationships, and spatial planning solutions."
                        }
                    },
                    {
                        "block_type": "key_takeaway",
                        "component_type": "key_takeaway",
                        "title": "Lesson 1 Summary",
                        "content": {
                            "text": "Geography bridges the physical Earth and human civilization through the analytical lens of Place, Space, Environment, Time, Movement, and Region."
                        }
                    }
                ]
            },
            {
                "page_number": 7,
                "page_title": "Knowledge Check & Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Geographic Theme of Movement",
                        "content": {
                            "question": "Which of the following scenarios best exemplifies the geographical theme of 'Movement'?",
                            "options": [
                                "A. The steep, glaciated peaks and alpine vegetation of Mount Kenya",
                                "B. The bulk transport of Kericho tea by road and railway to Mombasa port for export",
                                "C. The administrative demarcation of Kenya into 47 county governments",
                                "D. The presence of basaltic volcanic rocks across the central Rift Valley floor"
                            ],
                            "correct_answer": "B",
                            "explanation": "Movement describes the translocation of goods, people, and information across physical space. The transit of tea from Kericho to Mombasa is a clear manifestation of movement."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Analyzing Historical Urban Expansion",
                        "content": {
                            "question": "When a spatial researcher maps the outward growth of Nairobi city from 1970 to the present day, which theme is being analyzed alongside 'Space'?",
                            "options": [
                                "A. Region",
                                "B. Time",
                                "C. Lithosphere",
                                "D. Meteorology"
                            ],
                            "correct_answer": "B",
                            "explanation": "Examining chronological expansion across decades introduces the dimension of Time into spatial analysis."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 2: The Two Great Branches of Geography
    {
        "unit_order": 2,
        "unit_name": "The Two Great Branches of Geography",
        "lesson_title": "The Two Great Branches of Geography",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Structure of Geographical Science",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Highland Agricultural Landscapes in Kericho",
                        "content": {"text": "Rolling tea plantations in Kericho illustrating the interplay between volcanic soils (Physical Geography) and commercial agriculture (Human Geography)."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: The Great Branches",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Distinguish clearly between Physical Geography and Human & Economic Geography\n"
                                "- Classify specialized sub-fields (Geomorphology, Climatology, Pedology, Demography, etc.) under their parent branches\n"
                                "- Explain how physical factors determine human economic choices in real-world scenarios"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Physical vs Human Geography Defined",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "The Two Main Disciplines",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Physical Geography",
                                    "definition": "The branch of geography that investigates natural landforms, atmospheric processes, water systems, soils, and living ecosystems of the Earth.",
                                    "simple": "The study of the natural world and earth processes without human intervention."
                                },
                                {
                                    "term": "Human and Economic Geography",
                                    "definition": "The branch of geography that analyzes human populations, cultural practices, settlements, and the spatial utilization of natural resources for economic livelihoods.",
                                    "simple": "The study of human activities, where people live, and how they utilize resources."
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Sub-fields of Physical & Human Geography",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Specialized Sub-fields of Geography",
                        "content": {
                            "text": (
                                "### 1. Physical Geography Sub-fields\n"
                                "- **Geomorphology**: The study of the origin, development, and evolution of landforms shaped by internal and external forces.\n"
                                "- **Climatology**: The study of long-term atmospheric patterns, climate classifications, and climate change trends.\n"
                                "- **Hydrology**: The study of the global water cycle, including rivers, lakes, aquifers, and oceans.\n"
                                "- **Pedology**: The study of soil formation, classification, and chemical/physical properties.\n"
                                "- **Biogeography**: The spatial distribution of flora and fauna across ecosystems.\n\n"
                                "### 2. Human & Economic Geography Sub-fields\n"
                                "- **Population Geography (Demography)**: Population distribution, density, fertility, and migration patterns.\n"
                                "- **Settlement Geography**: Spatial organization and growth of rural and urban settlements.\n"
                                "- **Agricultural Geography**: Spatial distribution of farming systems, cropping patterns, and livestock rearing.\n"
                                "- **Economic Geography**: Location of industries, trade flows, transport systems, mining, and energy resources."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Geography Tree: Classification of Specialized Sub-fields",
                        "content": {
                            "text": "Vector diagram illustrating the Geography Tree with its two major trunks (Physical and Human) branching into specialized disciplines."
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Interaction of Branches in Kenyan Real Life",
                "blocks": [
                    {
                        "block_type": "real_world_example",
                        "component_type": "real_world_example",
                        "title": "Case Example: Tea Production in the Central Kenya Highlands",
                        "content": {
                            "text": (
                                "The production of tea in Murang'a, Kiambu, and Nyeri perfectly showcases the continuous interplay between both branches:\n\n"
                                "1. **Physical Foundation**: Deep, well-drained, acidic volcanic soils (**Pedology**) and cool, reliable orographic rainfall exceeding 1,500 mm annually (**Climatology**).\n"
                                "2. **Human Response**: Smallholder farmers establish KTDA cooperatives (**Agricultural Geography**), build access feeder roads (**Transport Geography**), and supply international export markets (**Economic Geography**)."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 5,
                "page_title": "Common Misconceptions Alert",
                "blocks": [
                    {
                        "block_type": "common_misconception",
                        "component_type": "common_misconception",
                        "title": "Climatology vs Meteorology Distinction",
                        "content": {
                            "misconception": "Climatology and Meteorology are the exact same subject.",
                            "reality": "Meteorology analyzes short-term, day-to-day atmospheric conditions and forecasts, whereas Climatology studies long-term statistical atmospheric trends averaged over 30 or more years."
                        }
                    }
                ]
            },
            {
                "page_number": 6,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Identifying Physical Sub-fields",
                        "content": {
                            "question": "A researcher is conducting a field study on the rate of soil degradation and nutrient depletion on the slopes of the Aberdare Ranges. Which sub-field is this primary aligned with?",
                            "options": [
                                "A. Geomorphology",
                                "B. Pedology",
                                "C. Hydrology",
                                "D. Demography"
                            ],
                            "correct_answer": "B",
                            "explanation": "Pedology is the specific scientific study of soils, their formation, properties, and degradation processes."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Categorizing Human Economic Phenomena",
                        "content": {
                            "question": "Which of the following topics represents an investigation within Human and Economic Geography?",
                            "options": [
                                "A. The travel times of seismic P and S waves across the East African rift",
                                "B. The spatial relationship between transport corridors and industrial establishment in Athi River",
                                "C. The chemical weathering of granitic tors by carbonation in western Kenya",
                                "D. The hydrological discharge rate of the Tana River during flash floods"
                            ],
                            "correct_answer": "B",
                            "explanation": "Industrial locations, transport links, and commercial enterprise are human economic activities studied in Economic Geography."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 3: Geography's Connections with Other Disciplines
    {
        "unit_order": 3,
        "unit_name": "Geography's Connections with Other Disciplines",
        "lesson_title": "Geography's Connections with Other Disciplines",
        "pages": [
            {
                "page_number": 1,
                "page_title": "The Interdisciplinary Nature of Geography",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "The Standard Gauge Railway: An Engineering and Spatial Milestone",
                        "content": {"text": "A modern passenger train on the Standard Gauge Railway crossing elevated bridges in Kenya, representing the integration of geology, physics, economics, and ecology."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Interdisciplinary Bridges",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain why Geography is considered an interdisciplinary bridge subject\n"
                                "- Identify direct connections between Geography and Mathematics, Physics, Chemistry, Biology, History, Agriculture, Economics, and Computer Science\n"
                                "- Explain how other disciplines enrich spatial problem-solving in real-life infrastructure projects"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Connections with the Sciences and Humanities",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "How Geography Links with Other Subjects",
                        "content": {
                            "text": (
                                "Geography serves as an **intellectual crossroads**, drawing methods and principles from multiple fields:\n\n"
                                "- **Mathematics & Statistics**: Calculates map scale, bearings, vertical exaggeration, area calculation, and statistical indices.\n"
                                "- **History**: Provides temporal background for past settlement patterns, colonial boundaries, and industrial heritage.\n"
                                "- **Physics**: Supplies laws of thermodynamics, gravity, seismic waves, and atmospheric pressure dynamics.\n"
                                "- **Chemistry**: Explains chemical weathering of rock minerals (oxidation, carbonation) and soil pH chemistry.\n"
                                "- **Biology**: Informs biogeography through ecosystem energy flows, food webs, and floral/faunal adaptations.\n"
                                "- **Agriculture**: Shares knowledge of soil types, crop agronomy, agroforestry, and land husbandry.\n"
                                "- **Economics**: Guides industrial location models, transport cost-benefit analysis, and international trade balance.\n"
                                "- **Computer Science**: Powers digital Geographic Information Systems (GIS), satellite image processing, and spatial databases."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Interdisciplinary Hub: Geography as the Integrator",
                        "content": {
                            "text": "Vector diagram illustrating Geography at the center connecting with Mathematics, Sciences, Humanities, and Information Technology."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Case Study: The Standard Gauge Railway (SGR)",
                "blocks": [
                    {
                        "block_type": "real_world_example",
                        "component_type": "real_world_example",
                        "title": "Multi-Disciplinary Planning in the Standard Gauge Railway",
                        "content": {
                            "text": (
                                "Building Kenya's SGR required a synthesis of multiple disciplines:\n\n"
                                "- **Computer Science & GIS**: Route optimization and digital elevation modelling.\n"
                                "- **Geomorphology & Physics**: Stabilizing deep cuts through the Rift Valley escarpment.\n"
                                "- **Biology & Ecology**: Designing elevated wildlife underpasses across Tsavo National Park to protect migratory corridors.\n"
                                "- **Economics**: Forecasting trade freight volumes between Mombasa Port and inland dry ports."
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Computer Science Integration",
                        "content": {
                            "question": "What is the primary manifestation of Computer Science in modern geographic practice?",
                            "options": [
                                "A. Drawing hand-made sketch maps in a field diary",
                                "B. Utilizing Geographic Information Systems (GIS) and remote sensing software for digital spatial modeling",
                                "C. Recording oral historical interviews with village elders",
                                "D. Measuring soil pH using litmus paper strips"
                            ],
                            "correct_answer": "B",
                            "explanation": "GIS software, GPS navigation, and satellite imagery analysis represent the direct technological fusion of Computer Science with Geography."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Chemistry Connection",
                        "content": {
                            "question": "The chemical breakdown of olivine and feldspar minerals in volcanic basalt through hydrolysis and oxidation connects Geography with which subject?",
                            "options": [
                                "A. History",
                                "B. Economics",
                                "C. Chemistry",
                                "D. Mathematics"
                            ],
                            "correct_answer": "C",
                            "explanation": "Hydrolysis, carbonation, and oxidation are chemical reactions altering rock minerals, linking Chemistry directly with Physical Geography."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 4: Geography in Daily Life and Sustainable Development
    {
        "unit_order": 4,
        "unit_name": "Geography in Daily Life and Sustainable Development",
        "lesson_title": "Geography in Daily Life and Sustainable Development",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Geography for Sustainable Living",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Gura Waterfalls and Highland Catchments in the Aberdares",
                        "content": {"text": "A pristine waterfall flowing through the Aberdare forest, illustrating the function of highland water towers."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Daily Life & Sustainability",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Explain how geographical awareness informs daily decisions (weather, navigation, housing)\n"
                                "- Define sustainable development from an environmental perspective\n"
                                "- Explain the critical ecological role of Kenya's five Water Towers\n"
                                "- Propose geographic solutions for flood mitigation and environmental management"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Daily Applications and Sustainable Development",
                "blocks": [
                    {
                        "block_type": "definition_card",
                        "component_type": "definition_card",
                        "title": "Sustainability Concepts",
                        "content": {
                            "definitions": [
                                {
                                    "term": "Sustainable Development",
                                    "definition": "Development that meets the socio-economic needs of the present generation without compromising the ability of future generations to meet their own needs.",
                                    "simple": "Managing resources wisely today so that our children and grandchildren will still have clean water, fertile soil, and forests tomorrow."
                                }
                            ]
                        }
                    },
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Kenya's Five Water Towers",
                        "content": {
                            "text": (
                                "Kenya relies heavily on **five primary highland water towers**:\n\n"
                                "1. **Mau Forest Complex**\n"
                                "2. **Mount Kenya**\n"
                                "3. **Aberdare Mountain Range**\n"
                                "4. **Mount Elgon**\n"
                                "5. **Cherangani Hills**\n\n"
                                "These forested montane catchments sponge torrential rainfall, replenish underground aquifers, and slowly release water into vital rivers like the Tana, Athi, Nyando, and Mara throughout the dry seasons."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "The Hydrological Cycle and Highland Water Catchments",
                        "content": {
                            "text": "Vector diagram illustrating how highland forest canopies capture cloud moisture, recharge groundwater aquifers, and sustain downstream rivers."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Flood Risk Management: The Kano Plains",
                "blocks": [
                    {
                        "block_type": "real_world_example",
                        "component_type": "real_world_example",
                        "title": "Geographical Flood Mitigation in the Nyando Basin",
                        "content": {
                            "text": (
                                "In the low-lying **Kano Plains** near Lake Victoria, seasonal torrential downpours frequently trigger River Nyando to breach its banks. "
                                "Geographers apply spatial contour analysis to:\n\n"
                                "- Identify high-risk flood inundation zones\n"
                                "- Design dykes and designated overflow retention basins\n"
                                "- Recommend safer elevated ground for homesteads and schools"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Kenya's Water Towers",
                        "content": {
                            "question": "Why are mountainous regions like the Aberdares and Mau Complex termed 'Water Towers'?",
                            "options": [
                                "A. They feature large steel tanks constructed by county governments",
                                "B. They are high-altitude forest ecosystems that catch precipitation, sponge water into soil, and regulate perennial river flows",
                                "C. They receive the lowest rainfall in Kenya and require artificial water pumping",
                                "D. They are flat floodplains that submerge during monsoons"
                            ],
                            "correct_answer": "B",
                            "explanation": "Highland forested catchments naturally capture precipitation and gradually recharge the nation's major river networks."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Flood-Resilient Site Selection",
                        "content": {
                            "question": "A community in Garissa plans a new settlement. Geographers advise building on an elevated alluvial terrace rather than the active riverbank. This is an application of geography in:",
                            "options": [
                                "A. Mineral prospecting",
                                "B. Disaster risk reduction and hazard avoidance",
                                "C. International maritime trade",
                                "D. Soil acidity neutralization"
                            ],
                            "correct_answer": "B",
                            "explanation": "Elevated site selection in flood-prone river basins minimizes disaster vulnerability through spatial planning."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 5: The Geographer's Toolbox
    {
        "unit_order": 5,
        "unit_name": "The Geographer's Toolbox",
        "lesson_title": "The Geographer's Toolbox",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Instruments and Methods of Spatial Inquiry",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Geodetic Surveying and Spatial Data Collection",
                        "content": {"text": "A land surveyor using a digital total station and optical level tripod to record topographic elevations."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: The Geographer's Toolkit",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify essential physical and digital tools used by geographers\n"
                                "- Explain the unique functions of Maps, Fieldwork, Photographs, Statistics, GIS/GPS, and Surveying\n"
                                "- Select the most appropriate geographical tool for various real-world inquiry scenarios"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Core Tools of Geography",
                "blocks": [
                    {
                        "block_type": "comparison_table",
                        "component_type": "comparison_table",
                        "title": "The Geographer's Essential Toolkit",
                        "content": {
                            "headers": ["Tool / Method", "Primary Purpose", "Practical Real-World Application"],
                            "rows": [
                                ["Direct Observation", "First-hand visual and sensory assessment", "Noting gully erosion along roadside slopes"],
                                ["Topographical Maps", "Scale-reduced representation of relief and culture", "Navigating terrain and calculating gradient"],
                                ["Fieldwork", "Collection of primary field data", "Collecting soil and rock specimens in a quarry"],
                                ["Aerial / Satellite Imagery", "Macro-level land cover monitoring", "Tracking forest canopy change in the Mau Complex"],
                                ["Statistical Methods", "Numerical quantification and trend analysis", "Analyzing annual crop harvest volumes"],
                                ["GPS & GIS Software", "Precise coordinate capture and multi-layer analysis", "Mapping water borehole locations across a sub-county"],
                                ["Surveying Instruments", "Measuring angles, distances, and elevations", "Determining slope gradients for road construction"]
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Infographic: The Modern Geographer's Toolkit",
                        "content": {
                            "text": "Vector infographic displaying compass, topographic map, digital GPS unit, rain gauge, measuring tape, and field notebook."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Selecting Tools for Spatial Analysis",
                        "content": {
                            "question": "A county team wishes to pinpoint the exact GPS coordinates of all clean-water boreholes and overlay them with road networks to identify underserved villages. Which tool combination is required?",
                            "options": [
                                "A. A Stevenson screen and a rain gauge",
                                "B. GPS receivers for coordinate recording and GIS software for spatial overlay analysis",
                                "C. A magnetic compass and historical diary",
                                "D. An optical microscope and litmus paper"
                            ],
                            "correct_answer": "B",
                            "explanation": "GPS records exact ground coordinates while GIS overlays multiple thematic layers (boreholes, roads, villages) for spatial planning."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: First-Hand Data Gathering",
                        "content": {
                            "question": "Which method is best suited for gathering fresh, primary geographical data directly from an active farm?",
                            "options": [
                                "A. Reading a secondary textbook written in 1980",
                                "B. Active fieldwork and direct on-site observation",
                                "C. Viewing an unrelated documentary video",
                                "D. Copying data from another student"
                            ],
                            "correct_answer": "B",
                            "explanation": "Fieldwork and direct observation provide unmediated, primary data directly from the physical environment."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 6: Career Pathways in Geography
    {
        "unit_order": 6,
        "unit_name": "Career Pathways in Geography",
        "lesson_title": "Career Pathways in Geography",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Professional Horizons in Geography",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Atmospheric Observation Instruments at a Meteorological Station",
                        "content": {"text": "A certified meteorologist checking anemometers and thermometers inside a weather station instrument enclosure."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Careers in Geography",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Identify modern professional careers rooted in geographical science\n"
                                "- Map geographic sub-fields to specialized job markets (e.g. Climatology -> Meteorology, Demography -> Urban Planning)\n"
                                "- Evaluate career opportunities in public agencies like NEMA, KMD, KWS, and the Survey of Kenya"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "Diverse Career Paths in the 21st Century",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Career Specializations in Geography",
                        "content": {
                            "text": (
                                "1. **GIS Analyst & Remote Sensing Specialist**: Digitizing, analyzing satellite imagery, and building spatial databases for logistics, agriculture, and government planning.\n"
                                "2. **Urban & Regional Planner**: Designing town zoning masterplans, public transport routes, green parks, and municipal waste infrastructure.\n"
                                "3. **Meteorologist & Climate Modeler**: Analyzing atmospheric radar and satellite feeds at the Kenya Meteorological Department to forecast weather for aviation and farming.\n"
                                "4. **Environmental Impact Assessment (EIA) Officer**: Working with NEMA to audit industrial developments and protect wetlands, soils, and air quality.\n"
                                "5. **Land Surveyor & Cartographer**: Measuring cadastral property boundaries, plotting topographical maps, and guiding highway construction.\n"
                                "6. **Wildlife & Tourism Conservationist**: Managing habitats, mapping migration corridors, and promoting eco-tourism with KWS."
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Career Pathways Flowchart in Geography",
                        "content": {
                            "text": "Vector flowchart showing pathways branching into Geospatial Tech, Environmental Management, Urban Planning, Aviation/Surveying, and Academia."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Atmospheric Science Career",
                        "content": {
                            "question": "Which professional specializes in analyzing atmospheric data to provide storm warnings and flight route forecasts for pilots at JKIA?",
                            "options": [
                                "A. Pedologist",
                                "B. Meteorologist",
                                "C. Cartographer",
                                "D. Geochemist"
                            ],
                            "correct_answer": "B",
                            "explanation": "Meteorologists specialize in atmospheric thermodynamics and weather forecasting for aviation, agriculture, and maritime operations."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Geospatial Information Roles",
                        "content": {
                            "question": "A student strong in computer programming and spatial analysis wishes to build digital map layers for disaster response. Which career is ideal?",
                            "options": [
                                "A. Agricultural Extension Worker",
                                "B. GIS Specialist / Spatial Data Analyst",
                                "C. Historical Archivist",
                                "D. Traditional Tour Guide"
                            ],
                            "correct_answer": "B",
                            "explanation": "A GIS Specialist combines computational database tools with spatial analysis to build digital mapping systems."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 7: Local Geographical Inquiry: Mapping Your Community
    {
        "unit_order": 7,
        "unit_name": "Local Geographical Inquiry: Mapping Your Community",
        "lesson_title": "Local Geographical Inquiry: Mapping Your Community",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Conducting a Local Field Inquiry",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Fieldwork and Sketch Mapping in Geography",
                        "content": {"text": "Geography students carrying clipboards, measuring instruments, and drawing sketch maps during an outdoor field audit."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Lesson Objectives: Community Mapping",
                        "content": {
                            "text": (
                                "By the end of this lesson, you will be able to:\n\n"
                                "- Plan and execute a systematic local geographical audit of your school or village\n"
                                "- Classify local physical assets (slopes, trees, drainage) and human assets (buildings, tanks, roads)\n"
                                "- Draw a clean, accurate sketch map conforming to the TACKS cartographic standard\n"
                                "- Adhere strictly to field safety protocols"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Four Phases of a Field Audit",
                "blocks": [
                    {
                        "block_type": "step_process",
                        "component_type": "step_process",
                        "title": "Step-by-Step Local Inquiry Methodology",
                        "content": {
                            "steps": [
                                {"step_number": 1, "title": "Planning & Objectives", "description": "Formulate a clear inquiry question (e.g. 'Mapping school physical assets and erosion hazards') and assemble clipboards, pencils, and GPS receivers."},
                                {"step_number": 2, "title": "Field Observation", "description": "Traverse the designated area safely, classifying natural features (slopes, trees) and artificial features (classrooms, water points)."},
                                {"step_number": 3, "title": "Data Recording & Pacing", "description": "Record relative bearings and measure approximate boundary distances using pacing (calibrated walking strides)."},
                                {"step_number": 4, "title": "Sketch Map Cartography", "description": "Draw the final sketch map incorporating all TACKS elements: Title, Arrow (North), Compass/Key, Frame (Border), and Scale (Approximate)."}
                            ]
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Standardized Sketch Map TACKS Framework Visualizer",
                        "content": {
                            "text": "Vector diagram illustrating the TACKS cartographic checklist: Title, North Arrow, Key, Frame border, and Scale bar."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Field Safety Protocols & Misconceptions",
                "blocks": [
                    {
                        "block_type": "callout",
                        "component_type": "callout",
                        "title": "Safety Guidelines During Outdoor Fieldwork",
                        "content": {
                            "text": (
                                "- Always remain within the teacher-defined spatial boundaries\n"
                                "- Avoid hazardous steep quarry faces, unstable escarpments, and slippery riverbanks\n"
                                "- Do not handle or drink water from open drainage trenches\n"
                                "- Wear protective footwear and stay alert in tall grass to prevent snake or insect encounters"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 4,
                "page_title": "Formative Knowledge Check",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 1: Essential Map Frame",
                        "content": {
                            "question": "When drawing a sketch map of a school compound, a student draws a neat outer rectangular box enclosing all features. Which TACKS element is this?",
                            "options": [
                                "A. The Key / Legend",
                                "B. The North Arrow",
                                "C. The Frame / Border",
                                "D. The Mathematical Grid"
                            ],
                            "correct_answer": "C",
                            "explanation": "The frame (or border) is the neat outer boundary enclosing all cartographic elements on a map."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Question 2: Classifying Field Assets",
                        "content": {
                            "question": "Which of the following is classified as a 'human asset' during a school geographical audit?",
                            "options": [
                                "A. A natural outcrop of granite rocks",
                                "B. A gentle grassy hillside",
                                "C. A 10,000-litre rainwater harvesting tank and masonry gutter system",
                                "D. A seasonal natural stream channel"
                            ],
                            "correct_answer": "C",
                            "explanation": "Rainwater harvesting tanks and gutters are artificial structures constructed by humans, classifying them as human assets."
                        }
                    }
                ]
            }
        ]
    },

    # Lesson 8: Topic Review, Synthesis, and Checkpoint
    {
        "unit_order": 8,
        "unit_name": "Topic Review, Synthesis, and Checkpoint",
        "lesson_title": "Topic Review, Synthesis, and Checkpoint",
        "pages": [
            {
                "page_number": 1,
                "page_title": "Comprehensive Topic Synthesis",
                "blocks": [
                    {
                        "block_type": "suggested_image",
                        "component_type": "suggested_image",
                        "title": "Batian and Nelion Peaks of Mount Kenya: Grandeur of Physical Geography",
                        "content": {"text": "A breathtaking high-altitude view of Mount Kenya peaks, showcasing the pinnacle of physical landforms and ecological zones."}
                    },
                    {
                        "block_type": "learning_goal",
                        "component_type": "learning_goal",
                        "title": "Topic 1 Mastery Objectives",
                        "content": {
                            "text": (
                                "By completing this review checkpoint, you will:\n\n"
                                "- Synthesize all core pillars: 6 Themes, 2 Great Branches, Interdisciplinary links, Daily applications, Tools, and Careers\n"
                                "- Demonstrate mastery of geographic terminology with 100% confidence\n"
                                "- Complete the summative checkpoint assessment with at least 80% score"
                            )
                        }
                    }
                ]
            },
            {
                "page_number": 2,
                "page_title": "The Big Picture Synthesis",
                "blocks": [
                    {
                        "block_type": "concept_explanation",
                        "component_type": "concept_explanation",
                        "title": "Synthesized Conceptual Hierarchy",
                        "content": {
                            "text": (
                                "Let's review the interconnected architecture of Geography:\n\n"
                                "```\n"
                                "                          INTRODUCTION TO GEOGRAPHY\n"
                                "                                      |\n"
                                "     +--------------------------------+--------------------------------+\n"
                                "     |                                |                                |\n"
                                "FOUNDATIONS                        BRANCHES                        PRACTICE\n"
                                "- 6 Themes (Place, Space,          - Physical (Geomorphology,      - Tools (Maps, Fieldwork,\n"
                                "  Environment, Time, Movement,       Climatology, Hydrology,         Photos, Stats, GIS, GPS)\n"
                                "  Region)                            Pedology, Biogeography)       - Careers (GIS, Planner,\n"
                                "- Earth as home of humankind       - Human & Economic (Demography,   Meteorologist, NEMA)\n"
                                "                                     Settlement, Agriculture)      - Sustainability & Towers\n"
                                "```"
                            )
                        }
                    },
                    {
                        "block_type": "suggested_diagram",
                        "component_type": "suggested_diagram",
                        "title": "Master Synthesis Mind Map for Topic 1",
                        "content": {
                            "text": "Vector mind map interconnecting all 8 lessons of Introduction to Geography into a single unified knowledge structure."
                        }
                    }
                ]
            },
            {
                "page_number": 3,
                "page_title": "Summative Checkpoint Assessment",
                "blocks": [
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Checkpoint Question 1: Spatial Planning",
                        "content": {
                            "question": "A county urban planner must position a new solid waste recycling plant so it is accessible by paved roads, away from residential neighborhoods, and downstream from water intakes. Which core geographical theme governs this decision?",
                            "options": [
                                "A. Time",
                                "B. Space (Spatial analysis and location)",
                                "C. Historical Geography",
                                "D. Biogeographical taxonomy"
                            ],
                            "correct_answer": "B",
                            "explanation": "Evaluating optimal relative placement in relation to transport links, residences, and water sources is a core problem of Space and spatial analysis."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Checkpoint Question 2: Sustainable Resource Principles",
                        "content": {
                            "question": "Which statement best embodies the principle of Sustainable Development?",
                            "options": [
                                "A. Clearing indigenous highland forests to maximize short-term timber export profits",
                                "B. Halting all economic industrial activity completely across the entire nation",
                                "C. Managing forest and water resources responsibly today to drive economic prosperity without compromising their availability for future generations",
                                "D. Exporting all raw mineral ores without domestic environmental safeguards"
                            ],
                            "correct_answer": "C",
                            "explanation": "Sustainable development balances contemporary economic welfare with the long-term conservation of ecological systems for future generations."
                        }
                    },
                    {
                        "block_type": "knowledge_check",
                        "component_type": "knowledge_check",
                        "title": "Checkpoint Question 3: Interdisciplinary Biology Connection",
                        "content": {
                            "question": "Which specialized geographical sub-field forms the direct bridge with Biology by analyzing the spatial distribution of flora and fauna across ecological zones?",
                            "options": [
                                "A. Pedology",
                                "B. Biogeography",
                                "C. Geomorphology",
                                "D. Micro-climatology"
                            ],
                            "correct_answer": "B",
                            "explanation": "Biogeography investigates the spatial distribution patterns of plant and animal species, bridging Geography with Biological sciences."
                        }
                    }
                ]
            }
        ]
    }
]

def ingest_topic_1():
    print("=== Starting Ingestion for Grade 10 Geography — Topic 1: Introduction to Geography ===")
    
    cbc = Curriculum.objects.filter(name__iexact="CBC").first()
    if not cbc:
        raise ValueError("Curriculum 'CBC' not found in database.")
    
    grade10 = Grade.objects.filter(curriculum=cbc, name__icontains="10").first()
    if not grade10:
        raise ValueError("Grade 10 not found under CBC.")
    
    subject, _ = Subject.objects.get_or_create(grade=grade10, name="Geography", defaults={"description": "CBC Grade 10 Geography"})
    print(f"Target Subject: {subject.name} (ID: {subject.id}, Grade: {grade10.name})")

    with transaction.atomic():
        topic, _ = Topic.objects.get_or_create(
            subject=subject,
            order=1,
            defaults={"name": "Introduction to Geography", "description": "Foundations, branches, tools, daily applications, and career pathways in Geography."}
        )
        topic.name = "Introduction to Geography"
        topic.description = "Foundations, branches, tools, daily applications, and career pathways in Geography."
        topic.save()
        print(f"Topic configured: {topic.name} (ID: {topic.id})")

        total_blocks_created = 0

        for lesson_data in LESSONS_DATA:
            u_order = lesson_data["unit_order"]
            u_name = lesson_data["unit_name"]
            l_title = lesson_data["lesson_title"]

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
                defaults={"title": l_title, "status": "published", "version": 1}
            )
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()

            # Clean existing blocks for idempotent ingestion
            lesson.blocks.all().delete()

            block_seq = 1
            for page in lesson_data["pages"]:
                p_num = page["page_number"]
                p_title = page["page_title"]

                for c_order, block_dict in enumerate(page["blocks"], start=1):
                    cleaned_content = clean_content_dict(block_dict.get("content", {}))
                    LessonBlock.objects.create(
                        lesson=lesson,
                        block_type=block_dict["block_type"],
                        component_type=block_dict.get("component_type", block_dict["block_type"]),
                        title=clean_text(block_dict.get("title", "")),
                        content=cleaned_content,
                        page_number=p_num,
                        page_title=p_title,
                        order=block_seq,
                        component_order=c_order
                    )
                    block_seq += 1
                    total_blocks_created += 1

            print(f"  Ingested Unit {u_order}: {u_name} ({len(lesson_data['pages'])} pages, {block_seq-1} blocks)")

        print(f"\nSuccessfully ingested Topic 1: 8 Lessons, {total_blocks_created} Blocks.")

if __name__ == "__main__":
    ingest_topic_1()
