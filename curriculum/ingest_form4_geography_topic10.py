"""
VLearn Form 4 Geography — Topic 10: Management and Conservation of the Environment
Rich In-Place Production Ingestion Engine (100% Aligned with Lessons.md)

Topic: Management and Conservation of the Environment (Topic Order: 10)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (66 Total Pages):
  1. Foundations of Environmental Management, Conservation, and Ecosystem Services (11 Pages)
  2. Environmental Hazards and Natural Disasters in Kenya and East Africa (12 Pages)
  3. Environmental Degradation: Causes, Pollution Dynamics, and Impact (12 Pages)
  4. Environmental Management Strategies, Legislation, and International Agreements (11 Pages)
  5. Community-Based Environmental Conservation and Rehabilitation Projects in Kenya (12 Pages)
  6. Comparative Case Studies (Kenya vs Japan/Sweden), Topic Synthesis, and KCSE Review (8 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic10.py
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
    """Removes bracket citations and cleans double spaces."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
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

def build_topic10_curriculum():
    """Returns the comprehensive, textbook-grade pedagogical page and block structure for Geography Topic 10."""
    return [
        # =====================================================================
        # LESSON 1: Foundations of Environmental Management, Conservation, and Ecosystem Services (11 Pages)
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Foundations of Environmental Management, Conservation, and Ecosystem Services",
            "unit_description": "Definition of environment, environmental management, conservation, endangered species, and essential ecosystem services.",
            "lesson_title": "Foundations of Environmental Management, Conservation, and Ecosystem Services",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Environmental Management & Conservation",
                        "content": {
                            "title": "Learning Objectives: Environmental Management & Conservation",
                            "goals": [
                                "Define environment, environmental management, and environmental conservation in a geographic context.",
                                "Distinguish between management (planned sustainable utilization) and conservation (preservation from destruction).",
                                "Classify ecosystem services: provisioning, regulating, cultural, and supporting services."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographic Definition of Environment & Management",
                        "content": {
                            "title": "Geographic Definition of Environment & Management",
                            "text": "The Environment refers to the sum total of all physical, biological, and socio-economic conditions surrounding an organism or human community.\n\n• Environmental Management: Refers to the deliberate planning, regulation, and control of human activities to prevent environmental deterioration while ensuring sustainable resource utilization.\n\n• Environmental Conservation: Refers to the protection, preservation, and wise stewardship of natural resources (forests, water catchment towers, soils, wildlife) from destruction, exploitation, or extinction."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Ecosystem Services Taxonomy",
                        "content": {
                            "term": "Ecosystem Services Taxonomy",
                            "definition": "The direct and indirect benefits that human societies derive from natural ecosystems.",
                            "key_points": [
                                "Provisioning Services: Material outputs derived from ecosystems (fresh water, timber, food crops, medicinal plants, fuelwood).",
                                "Regulating Services: Ecological processes that regulate climate and water (carbon sequestration by forests, flood attenuation by wetlands, pollination).",
                                "Cultural Services: Non-material benefits contributing to human well-being (ecotourism, recreational parks, spiritual value).",
                                "Supporting Services: Foundational ecological processes necessary for all other services (soil formation, nutrient cycling, photosynthesis)."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Ecosystem Services & Human Well-Being Cascade Model",
                        "content": {
                            "title": "Ecosystem Services & Human Well-Being Cascade Model",
                            "caption": "Ecosystem Functioning → Provisioning + Regulating + Cultural Services → Sustainable Human Development & National Prosperity",
                            "description": "Flowchart diagram illustrating natural ecosystem processes delivering provisioning, regulating, and cultural services to human society."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Need for Environmental Conservation & Protecting Endangered Species",
                        "content": {
                            "title": "The Need for Environmental Conservation & Protecting Endangered Species",
                            "text": "Geographers advocate for environmental management and conservation due to several vital reasons:\n\n1. Protecting Endangered Species: Safeguarding rare flora (e.g., Meru Oak, Rosewood, Elgon Teak) and endangered fauna (e.g., White Rhino, Black Rhino, Grevy's Zebra) from habitat destruction and extinction.\n\n2. Sustaining Human Survival: Natural ecosystems provide clean air to breathe, fresh drinking water, fertile soil for crop production, and medicinal plants.\n\n3. Sustaining Economic Resources: Key national economic sectors (agriculture, ecotourism, hydroelectric energy generation) rely directly on healthy ecosystems.\n\n4. Mitigating Climate Change: Intact forest catchments absorb atmospheric carbon dioxide, moderating global warming and preventing desertification."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Highland Agricultural Soil Management Zone Visualization",
                        "content": {
                            "title": "Highland Agricultural Soil Management Zone Visualization",
                            "caption": "Intensive agricultural smallholdings in Kiambu illustrating rural land and soil management practices.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "comparison_table",
                        "title": "Environmental Management vs Environmental Conservation Comparison",
                        "content": {
                            "headers": ["Geographic Aspect", "Environmental Management", "Environmental Conservation"],
                            "rows": [
                                ["Core Focus", "Sustainable exploitation and utilization of resources", "Preservation and protection of resources from destruction"],
                                ["Primary Action", "Planning, regulating harvest quotas, EIA auditing", "Establishing national parks, gazetting water towers, banning trade"],
                                ["Human Interaction", "Active controlled human usage (e.g., sustainable logging)", "Strict protection (e.g., zero-logging in water catchments)"],
                                ["Economic Objective", "Ensuring long-term resource supply for industries", "Maintaining ecological balance and biodiversity"]
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Analysis: Why Forests act as Water Catchment Towers",
                        "content": {
                            "question": "Explain three ecological reasons why highland forests (e.g., Mau Complex, Aberdares) must be protected as national water catchment towers. (3 Marks)",
                            "strategy": "State ecological mechanism and explain downstream hydrological benefit.",
                            "solution": [
                                "1. Increasing Rainfall Infiltration (1 Mark): Forest canopy and leaf litter reduce raindrop impact, encouraging rainwater to infiltrate the ground and recharge aquifers.",
                                "2. Regulating River Base Flows (1 Mark): Sub-surface groundwater slowly feeds rivers during dry seasons, preventing perennial rivers from drying up.",
                                "3. Controlling Soil Erosion & Siltation (1 Mark): Tree roots anchor the soil, preventing mudslides and reducing siltation in downstream hydroelectric reservoirs (Seven Forks)."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Ecosystem Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Ecosystem Classifier",
                            "prompt": "Scenario: Forests absorb carbon dioxide from the atmosphere and regulate local rainfall patterns. Which category of ecosystem service does this represent?",
                            "options": [
                                "Option A: Regulating Services (processes that regulate climate and water cycles).",
                                "Option B: Provisioning Services.",
                                "Option C: Cultural Services."
                            ],
                            "correct_option": "Option A: Regulating Services (processes that regulate climate and water cycles).",
                            "explanation": "Climate moderation, carbon sequestration, and flood control are classic Regulating Services."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Environmental Foundations",
                        "content": {
                            "question": "What is the primary difference between environmental management and environmental conservation?",
                            "options": [
                                "Management focuses on sustainable planned utilization; Conservation focuses on preservation from destruction.",
                                "Management means cutting down all trees; Conservation means burning forests.",
                                "Management is for oceans; Conservation is for towns.",
                                "Management is illegal; Conservation is legal."
                            ],
                            "correct_answer": 0,
                            "explanation": "Management guides sustainable resource use; Conservation protects resources from depletion."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Kenya's Five Water Towers",
                        "content": {
                            "text": "Kenya relies on five major mountain forests known as 'Water Towers': Mt. Kenya, Aberdare Range, Mau Forest Complex, Mt. Elgon, and Cherangani Hills. They supply over 75% of national fresh water."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Management vs Preservation",
                        "content": {
                            "mistake": "Assuming environmental management forbids all resource use.",
                            "correction": "Environmental management DOES NOT forbid resource use; it ensures resources are harvested SUSTAINABLY at rates equal to or lower than natural regeneration.",
                            "reasoning": "Preservation locks resources away; Management regulates their wise use."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Environmental Foundations: Key Takeaways",
                        "content": {
                            "title": "Environmental Foundations: Key Takeaways",
                            "summary_points": [
                                "Environmental Management is planned sustainable utilization; Conservation is preservation.",
                                "Protecting endangered species like Meru Oak, Rosewood, and White Rhino maintains biodiversity.",
                                "Ecosystem Services are classified as Provisioning, Regulating, Cultural, and Supporting.",
                                "Forest water towers regulate river flows, prevent dam siltation, and sustain national agriculture."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Environmental Hazards and Natural Disasters in Kenya and East Africa (12 Pages)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Environmental Hazards and Natural Disasters in Kenya and East Africa",
            "unit_description": "Natural vs human-induced hazards, flood causes and management, droughts, lightning, and biological pests.",
            "lesson_title": "Environmental Hazards and Natural Disasters in Kenya and East Africa",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Environmental Hazards",
                        "content": {
                            "title": "Learning Objectives: Environmental Hazards",
                            "goals": [
                                "Distinguish between Natural Environmental Hazards and Human-Induced Hazards.",
                                "Analyze causes, impacts, and engineering management of Floods in Kenya (Kano Plains, Budalangi).",
                                "Examine Drought management, Lightning hazard mitigation in Kakamega/Kisii, and Biological Pest Control (ICIPE tsetse fly program in Lambwe Valley)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographic Definition & Classification of Hazards",
                        "content": {
                            "title": "Geographic Definition & Classification of Hazards",
                            "text": "An Environmental Hazard is an extreme event or condition in the natural or human-modified environment that poses a grave threat to human life, property, infrastructure, and economic activities.\n\n• Natural Hazards: Arise from natural geomorphic, meteorological, or hydrological processes (e.g., floods, droughts, earthquakes, volcanic eruptions, landslides, lightning strikes, pest invasions).\n\n• Human-Induced Hazards: Result directly from human technological failures, industrial negligence, or poor environmental management (e.g., toxic industrial chemical spills, oil tanker spills, nuclear radiation leaks, deforestation-induced soil erosion)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Environmental Hazards Taxonomy: Natural vs Human-Induced",
                        "content": {
                            "title": "Environmental Hazards Taxonomy: Natural vs Human-Induced",
                            "caption": "Hazard Classification: Meteorological (Floods/Droughts) + Geomorphic (Landslides) vs Technological (Oil Spills/Nuclear Accidents)",
                            "description": "Taxonomy diagram categorizing environmental hazards into natural meteorological/geomorphic events vs human technological disasters."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Flood & Drought Hazard Taxonomy",
                        "content": {
                            "term": "Flood & Drought Hazard Taxonomy",
                            "definition": "Hydrological and meteorological hazards causing extreme socio-economic disruption.",
                            "key_points": [
                                "Riverine Flooding: Inundation of low-lying floodplains when river discharge exceeds channel carrying capacity (e.g., River Nzoia in Budalangi, River Nyando in Kano Plains, River Tana in Garissa).",
                                "Flash Flooding: Sudden, rapid urban flooding caused by high-intensity rainfall overflowing paved drainage channels.",
                                "Meteorological Drought: Prolonged deficit of precipitation relative to long-term averages in ASALs.",
                                "Agricultural Drought: Moisture deficit in root zones causing widespread crop failure and livestock starvation."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Flood Formation & Levee Engineering Management Model",
                        "content": {
                            "title": "Flood Formation & Levee Engineering Management Model",
                            "caption": "Flood Control Engineering: Catchment Deforestation → River Siltation & Spillovers → Artificial Dykes/Levees + Dam Storage Control",
                            "description": "Engineering diagram illustrating river channel overflowing and flood control using raised dykes, levees, and dams."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Kisii River Soil Erosion & Flood Siltation Visualization",
                        "content": {
                            "title": "Kisii River Soil Erosion & Flood Siltation Visualization",
                            "caption": "Silt-laden flood waters overflowing river banks in Kisii County following heavy rainfall.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Flood_river_full_of_erosion_in_Daraja_Mbili_Kisii_County_Kenya_East_Africa.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Flood_river_full_of_erosion_in_Daraja_Mbili_Kisii_County_Kenya_East_Africa.jpg"
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Lightning Hazards & Biological Pest Control (ICIPE Case Study)",
                        "content": {
                            "title": "Lightning Hazards & Biological Pest Control (ICIPE Case Study)",
                            "text": "1. Lightning Strikes Hazard: Highly frequent in Kakamega, Kisii, and the Nandi Escarpment due to intense cumulonimbus thunderstorm activity. Mitigation involves installing copper lightning arresters on all school and public building roofs.\n\n2. Biological Pest Control (ICIPE Lambwe Valley Program): Biological pests like tsetse flies in Lambwe Valley degrade agricultural capacity and transmit trypanosomiasis (sleeping sickness). The International Centre of Insect Physiology and Ecology (ICIPE) developed a biological control method: breeding and releasing sterile male tsetse flies to mate with females, crashing the population without chemical DDT pollution."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Drought Resilience & Water Harvesting Cascade",
                        "content": {
                            "title": "Drought Resilience & Water Harvesting Cascade",
                            "caption": "Drought Adaptation: ASAL Rainfall Deficit → Sand Dams + Borehole Drilling + Drought-Tolerant Crops (Sorghum/Millet) → Food Security",
                            "description": "Flowchart showing drought mitigation strategies using sand dams, deep boreholes, and drought-resistant crops."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Turkana Arid Drought Hazard Zone Visualization",
                        "content": {
                            "title": "Turkana Arid Drought Hazard Zone Visualization",
                            "caption": "Dry pastoral landscape in Turkana County during severe drought conditions.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Turkana_woman.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Turkana_woman.jpg"
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "Floods vs Droughts Environmental Hazard Comparison",
                        "content": {
                            "headers": ["Hazard Dimension", "Floods (Hydrological Hazard)", "Droughts (Meteorological Hazard)"],
                            "rows": [
                                ["Speed of Onset", "RAPID / Sudden onset (hours to days)", "SLOW / Incremental onset (months to years)"],
                                ["Primary Physical Cause", "Excess rainfall & high surface runoff", "Prolonged rainfall deficit & high evapotranspiration"],
                                ["Health Consequences", "Water-borne epidemics (cholera, dysentery)", "Malnutrition, kwashiorkor, and starvation"],
                                ["Structural Mitigation", "Artificial dykes, levees, dam reservoirs", "Sand dams, boreholes, strategic grain reserves"],
                                ["Primary Affected Zones in Kenya", "Kano Plains, Budalangi, Tana River Delta", "Northern & Eastern ASALs (Turkana, Wajir, Mandera)"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Analysis: Engineering Measures to Control Budalangi Floods",
                        "content": {
                            "question": "Explain four engineering and land-use measures taken to control recurring floods along River Nzoia in Budalangi. (4 Marks)",
                            "strategy": "Detail physical engineering and catchment management interventions.",
                            "solution": [
                                "1. Construction of Artificial Dykes / Levees (1 Mark): Building raised earthen embankments along River Nzoia banks to contain high flood discharge.",
                                "2. Re-afforestation of Mount Elgon Catchment (1 Mark): Planting trees in river catchments to increase rainfall infiltration and reduce surface runoff.",
                                "3. River Channel Dredging (1 Mark): Removing accumulated silt from the river bed to increase channel depth and carrying capacity.",
                                "4. Construction of Multi-purpose Dams (1 Mark): Building upstream dams to store peak floodwaters for regulated release."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Hazard Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Hazard Classifier",
                            "prompt": "Scenario: ICIPE breeds and releases sterile male tsetse flies in Lambwe Valley to crash the fly population without chemical sprays. Which pest management method is this?",
                            "options": [
                                "Option A: Biological Pest Control Method.",
                                "Option B: Chemical Pesticide Method.",
                                "Option C: Open-Cast Mining Method."
                            ],
                            "correct_option": "Option A: Biological Pest Control Method.",
                            "explanation": "Breeding and releasing sterile males to crash insect populations is a safe Biological Control Method."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Environmental Hazards",
                        "content": {
                            "question": "Which physical hazard is prevalent in Kakamega and Kisii counties due to frequent cumulonimbus thunderstorm activity?",
                            "options": [
                                "Lightning Strikes",
                                "Volcanic Eruption",
                                "Tsunami",
                                "Glacial Avalanche"
                            ],
                            "correct_answer": 0,
                            "explanation": "Kakamega and Kisii experience high lightning hazard occurrences due to intense thunderstorm clouds."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Lightning Arresters in Schools",
                        "content": {
                            "text": "Due to frequent fatal lightning strikes in Kakamega and Kisii highlands, government building codes mandate installing copper lightning arresters on all school roofs."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Hazard vs Disaster",
                        "content": {
                            "mistake": "Using 'Hazard' and 'Disaster' interchangeably in exam essays.",
                            "correction": "A Hazard is the POTENTIAL threat (e.g., heavy rain). A Disaster occurs when the hazard ACTUALLY IMPACTS vulnerable human lives and infrastructure.",
                            "reasoning": "Heavy rain in an uninhabited desert is a hazard; in a city, it becomes a disaster."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Environmental Hazards: Key Takeaways",
                        "content": {
                            "title": "Environmental Hazards: Key Takeaways",
                            "summary_points": [
                                "Hazards are classified as Natural (floods, droughts) or Human-Induced (pollution, oil spills).",
                                "Floods in Kano Plains (River Nyando) and Budalangi (River Nzoia) are managed via dykes, dredging, and afforestation.",
                                "Lightning strikes in Kakamega/Kisii are mitigated using copper lightning arresters.",
                                "ICIPE uses biological control (sterile male tsetse flies) in Lambwe Valley to manage pests safely."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Environmental Degradation: Causes, Pollution Dynamics, and Impact (12 Pages)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Environmental Degradation: Causes, Pollution Dynamics, and Impact",
            "unit_description": "Types of degradation, air/water/soil pollution dynamics (SO2 vs leaded fuel), eutrophication in Lake Victoria, and open-cast mining dereliction.",
            "lesson_title": "Environmental Degradation: Causes, Pollution Dynamics, and Impact",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Environmental Degradation",
                        "content": {
                            "title": "Learning Objectives: Environmental Degradation",
                            "goals": [
                                "Define Environmental Degradation and identify major degradation vectors.",
                                "Analyze dynamics of Air Pollution (SO2 acid rain vs leaded fuel poisoning), Water Pollution, and Open-Cast Mining Land Dereliction.",
                                "Evaluate ecological impacts of Eutrophication in Lake Victoria and solid waste crisis at Dandora Dumpsite."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Degradation & Pollution Vectors",
                        "content": {
                            "title": "Environmental Degradation & Pollution Vectors",
                            "text": "Environmental Degradation refers to the deterioration of the environment through depletion of natural resources (air, water, soil, wildlife), destruction of natural ecosystems, and open-cast mining land dereliction.\n\nPollution is the introduction of harmful contaminants, toxic chemical substances, or energy (heat, noise, radiation) into the natural environment at rates faster than natural ecosystems can neutralize them."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_image",
                        "title": "Urban Drainage Plastic Pollution & Gully Erosion Visualization",
                        "content": {
                            "title": "Urban Drainage Plastic Pollution & Gully Erosion Visualization",
                            "caption": "Urban drainage ditch choked with discarded plastic waste causing urban land degradation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Nature_vs_Neglect-_A_clash_between_nature_and_human_neglect._Erosion_of_a_once_well-intentioned_drainage_system_now_struggles_with_discarded_plastic_bags%2C_figuratively_our_consequences_on_the_environment..jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Nature_vs_Neglect-_A_clash_between_nature_and_human_neglect._Erosion_of_a_once_well-intentioned_drainage_system_now_struggles_with_discarded_plastic_bags%2C_figuratively_our_consequences_on_the_environment..jpg"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Pollution Pathways: Air, Water, and Soil Contamination Network",
                        "content": {
                            "title": "Pollution Pathways: Air, Water, and Soil Contamination Network",
                            "caption": "Pollution Dynamics: SO2 Gas Smoke → Acid Rain | Agrochemical Runoff → Water Eutrophication | Mining Dereliction → Stagnant Mosquito Pits",
                            "description": "Network diagram illustrating interconnected pathways of air, water, and soil pollution."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Pollution Categories & Atmospheric Chemistry Taxonomy",
                        "content": {
                            "term": "Pollution Categories & Atmospheric Chemistry Taxonomy",
                            "definition": "Classification of environmental pollution based on receiving medium and chemical behavior.",
                            "key_points": [
                                "Sulfur Dioxide (SO2) Pollution: Combines with atmospheric water vapor to form Acid Rain ($H_2SO_4$), which corrodes building roofs, acidifies soils, and destroys forests.",
                                "Leaded Fuel Particulates: Inhaled by humans and absorbed by leafy crops near highways, causing severe lead poisoning and neurological brain damage.",
                                "Water Pollution & Eutrophication: Industrial chemical discharge and agricultural NPK fertilizer runoff causing aquatic oxygen depletion (hypoxia).",
                                "Open-Cast Mining Land Dereliction: Excavation of quarry pits removing fertile topsoil, creating dangerous water-filled pits where malaria mosquitoes breed."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Dandora Dumpsite Solid Waste Crisis Visualization",
                        "content": {
                            "title": "Dandora Dumpsite Solid Waste Crisis Visualization",
                            "caption": "Massive accumulation of unsegregated solid municipal waste at the Dandora open dumpsite in Nairobi.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Dandora_1.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Dandora_1.jpg"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Eutrophication Process in Lake Ecosystems Diagram",
                        "content": {
                            "title": "Eutrophication Process in Lake Ecosystems Diagram",
                            "caption": "Eutrophication Sequence: Agrochemical Fertilizer Runoff → Excessive Algae Bloom → Oxygen Depletion (Hypoxia) → Massive Fish Kills",
                            "description": "Ecological diagram showing nutrient enrichment triggering algal blooms and aquatic oxygen starvation."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Case Study: Eutrophication in Lake Victoria",
                        "content": {
                            "title": "Case Study: Eutrophication in Lake Victoria",
                            "text": "Eutrophication is the excessive nutrient enrichment of water bodies, primarily caused by agricultural fertilizer runoff containing nitrates and phosphates, alongside raw municipal sewage discharge.\n\nIn Lake Victoria (Winam Gulf, Kisumu), eutrophication has triggered massive blooms of invasive Water Hyacinth weed (Eichhornia crassipes). The dense weed mat blocks sunlight, depletes dissolved oxygen (hypoxia), kills commercial fish species (Tilapia), blocks lake transport shipping lanes, and impedes municipal water intake pipes."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "SO2 Acid Rain vs Leaded Fuel Particulates Comparison",
                        "content": {
                            "headers": ["Atmospheric Pollutant", "Sulfur Dioxide (SO2)", "Leaded Fuel Particulates"],
                            "rows": [
                                ["Primary Industrial Source", "Coal-fired power plants & copper smelting stacks", "Exhaust fumes from vehicles burning leaded petrol"],
                                ["Atmospheric Reaction", "Combines with water vapor to form Acid Rain ($H_2SO_4$)", "Remains as microscopic heavy metal suspended particles"],
                                ["Environmental Impact", "Corrodes metal roofs, acidifies lakes & destroys forests", "Settles on roadside crops and soils; bioaccumulates"],
                                ["Human Health Impact", "Causes severe respiratory irritation & asthma", "Causes lead poisoning, anemia, and neurological damage"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Analysis: Impact of Open-Cast Mining Land Dereliction",
                        "content": {
                            "question": "Explain three ways in which unrehabilitated open-cast mining pits cause land degradation and human health hazards. (3 Marks)",
                            "strategy": "Connect quarry pit excavation to environmental and health hazards.",
                            "solution": [
                                "1. Destruction of Topsoil & Land Dereliction (1 Mark): Stripping topsoil leaves barren, rocky craters that cannot support agriculture.",
                                "2. Stagnant Water & Disease Breeding (1 Mark): Abandoned quarry pits collect rainwater, creating stagnant pools where malaria mosquitoes breed.",
                                "3. Unstable Slopes & Landslide Risk (1 Mark): Steep, loose overburden heaps create unstable quarry cliffs prone to collapsing on local communities."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Pollution Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Pollution Evaluator",
                            "prompt": "Scenario: Industrial smoke containing sulfur dioxide ($SO_2$) combines with clouds to fall as corrosive precipitation. What chemical phenomenon is this?",
                            "options": [
                                "Option A: Acid Rain.",
                                "Option B: Eutrophication.",
                                "Option C: Ozone Depletion."
                            ],
                            "correct_option": "Option A: Acid Rain.",
                            "explanation": "Sulfur dioxide reacting with water vapor produces Acid Rain ($H_2SO_4$)."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Environmental Degradation",
                        "content": {
                            "question": "What health hazard is caused by inhaling airborne leaded fuel particulates near busy transport highways?",
                            "options": [
                                "Lead poisoning and neurological brain damage",
                                "Sunburn",
                                "Malaria",
                                "Kwashiorkor"
                            ],
                            "correct_answer": 0,
                            "explanation": "Leaded fuel exhaust particulates cause severe heavy metal lead poisoning and neurological damage."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Kenya's Historic Plastic Bag Ban",
                        "content": {
                            "text": "In 2017, Kenya enacted the world's toughest ban on single-use plastic carrier bags, imposing heavy fines to eliminate plastic clogging urban drains and suffocating livestock."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Eutrophication Process",
                        "content": {
                            "mistake": "Claiming that fertilizer directly poisons fish in eutrophication.",
                            "correction": "Fertilizer causes ALGAE OVERGROWTH. When dense algae die, decomposing bacteria CONSUME ALL DISSOLVED OXYGEN, causing fish to suffocate.",
                            "reasoning": "Fish die from OXYGEN DEPLETION (hypoxia), not direct chemical poisoning."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Environmental Degradation: Key Takeaways",
                        "content": {
                            "title": "Environmental Degradation: Key Takeaways",
                            "summary_points": [
                                "SO2 forms Acid Rain; Leaded fuel particulates cause heavy metal neurological poisoning.",
                                "Open-cast mining dereliction creates barren craters and malaria-breeding stagnant pits.",
                                "Eutrophication in Lake Victoria is driven by NPK fertilizer runoff, spawning invasive Water Hyacinth.",
                                "Solid waste crisis at Dandora Dumpsite highlights the need for waste sorting and recycling."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Environmental Management Strategies, Legislation, and International Agreements (11 Pages)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Environmental Management Strategies, Legislation, and International Agreements",
            "unit_description": "NEMA, EMCA 1999, Protected Mijikenda Kayas, EIA audits, and international agreements.",
            "lesson_title": "Environmental Management Strategies, Legislation, and International Agreements",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Management Strategies & Legislation",
                        "content": {
                            "title": "Learning Objectives: Management Strategies & Legislation",
                            "goals": [
                                "Examine the regulatory mandate of NEMA, EMCA 1999, Water Act, and Forest Act.",
                                "Explain why the coastal Kayas of the Mijikenda were declared protected national monuments by presidential decree.",
                                "Detail Environmental Impact Assessments (EIA) and international agreements (Ramsar, CITES, Kyoto Accord, Trans-boundary Chemical Notifications)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "National Legal Framework: NEMA, EMCA 1999 & Protected Mijikenda Kayas",
                        "content": {
                            "title": "National Legal Framework: NEMA, EMCA 1999 & Protected Mijikenda Kayas",
                            "text": "In Kenya, environmental management is legally anchored under the Environmental Management and Coordination Act (EMCA, 1999), supported by the Water Act and Forest Act. NEMA is the statutory body enforcing compliance.\n\nCase Study: Protection of Coastal Mijikenda Kayas:\nThe sacred 'Kayas' (fortified forest settlements) of the Mijikenda along the Kenya coast were declared protected national monuments by presidential decree. Geographers highlight three reasons:\n1. Sacred Cultural Value: Preserving traditional ancestral burial grounds and cultural heritage.\n2. High Biodiversity: Protecting rare, endemic, and endangered species of flora and fauna.\n3. Water Catchment Protection: Serving as critical natural forest barriers protecting coastal groundwater catchments."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "National Environment Management Authority (NEMA) EIA Audit Pipeline",
                        "content": {
                            "title": "National Environment Management Authority (NEMA) EIA Audit Pipeline",
                            "caption": "EIA Process: Project Proposal → Environmental Study → Public Participation → Mitigation Plan → NEMA License Issuance",
                            "description": "Flowchart diagram showing step-by-step Environmental Impact Assessment (EIA) approval pipeline."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Environmental Impact Assessment (EIA) Taxonomy",
                        "content": {
                            "term": "Environmental Impact Assessment (EIA) Taxonomy",
                            "definition": "A systematic study conducted prior to project implementation to identify, predict, and mitigate potential environmental damage.",
                            "key_points": [
                                "Pre-Project Audit: Must be conducted BEFORE construction begins (e.g., SGR Railway, Nairobi Expressway).",
                                "Public Participation: Requires publishing notice in national newspapers soliciting public objections from local communities.",
                                "Environmental Management Plan (EMP): Outlines specific measures the developer will take to prevent pollution and restore degraded land.",
                                "NEMA Licensing: Project cannot legally proceed without a formal NEMA EIA License."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Waste Management Pyramid: Reduce, Reuse, Recycle, Dispose",
                        "content": {
                            "title": "Waste Management Pyramid: Reduce, Reuse, Recycle, Dispose",
                            "caption": "Waste Hierarchy: 1. Reduce (Most Preferred) → 2. Reuse → 3. Recycle → 4. Energy Recovery → 5. Landfill Disposal (Least Preferred)",
                            "description": "Inverted pyramid diagram depicting the environmental hierarchy of waste management strategies."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Industrial Effluent Treatment Plant Flowchart",
                        "content": {
                            "title": "Industrial Effluent Treatment Plant Flowchart",
                            "caption": "Water Treatment: Raw Industrial Effluent → Primary Screening → Secondary Biological Digestion → Tertiary Chlorination → Clean River Discharge",
                            "description": "Process flowchart depicting multi-stage industrial wastewater treatment prior to river discharge."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "International Environmental Accords & Trans-Boundary Assistance",
                        "content": {
                            "title": "International Environmental Accords & Trans-Boundary Assistance",
                            "text": "Because pollution and ecosystems cross national boundaries, Kenya participates in major international treaties:\n\n1. Ramsar Convention on Wetlands (1971): Protects international wetland habitats for migratory waterfowl (e.g., Lake Nakuru, Lake Naivasha).\n2. CITES (1973): Regulates and bans international trade in endangered wild fauna and flora (e.g., ivory trade ban protecting elephants).\n3. Kyoto Accord & Paris Climate Agreement: Global accords committing nations to reduce greenhouse gas emissions.\n4. Trans-Boundary Chemical Notifications & Assistance: International laws requiring governments to immediately notify neighbors of major chemical accidents and provide cross-frontier emergency assistance."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "comparison_table",
                        "title": "Ramsar Convention vs CITES International Treaties Comparison",
                        "content": {
                            "headers": ["Convention Aspect", "Ramsar Convention (1971)", "CITES Convention (1973)"],
                            "rows": [
                                ["Primary Focus", "Conservation & sustainable wise-use of WETLANDS", "Protection of ENDANGERED WILDLIFE SPECIES"],
                                ["Key Target Features", "Lakes, swamps, marshes, estuaries, migratory birds", "Elephants (ivory), rhinos (horn), rare timber species"],
                                ["Kenyan Sites / Target", "Lake Nakuru, Lake Naivasha, Lake Bogoria, Tana Delta", "KWS anti-poaching operations & ivory stock destruction"],
                                ["Global Objective", "Preventing wetland drainage and bio-diversity loss", "Banning commercial trade in endangered species"]
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Analysis: Steps in Conducting an EIA for a Highway",
                        "content": {
                            "question": "Outline four key steps involved in conducting an Environmental Impact Assessment (EIA) for a proposed highway project in Kenya. (4 Marks)",
                            "strategy": "State sequential steps in the NEMA EIA process.",
                            "solution": [
                                "1. Baseline Environmental Survey (1 Mark): Inspecting existing flora, fauna, soil, and drainage along the highway route.",
                                "2. Predicting Potential Environmental Impacts (1 Mark): Identifying potential damage like forest clearing, soil erosion, or noise pollution.",
                                "3. Formulating Mitigation Measures (1 Mark): Outlining plans such as planting replacement trees, constructing culverts, and erecting noise barriers.",
                                "4. Public Participation & NEMA Review (1 Mark): Publishing the EIA report for public comments before NEMA issues an operating license."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Treaty Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Treaty Evaluator",
                            "prompt": "Scenario: Why were the coastal Kayas of the Mijikenda declared protected national monuments by presidential decree?",
                            "options": [
                                "Option A: High sacred cultural value, endemic biodiversity protection, and water catchment conservation.",
                                "Option B: To build a major sea port.",
                                "Option C: To harvest fuelwood."
                            ],
                            "correct_option": "Option A: High sacred cultural value, endemic biodiversity protection, and water catchment conservation.",
                            "explanation": "Kayas are sacred forests protecting cultural heritage, endangered species, and groundwater catchments."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Legislation & Agreements",
                        "content": {
                            "question": "Which international agreement mandates governments to notify neighbors of major chemical accidents and provide cross-frontier emergency assistance?",
                            "options": [
                                "Trans-boundary Chemical Notification Accord",
                                "Maasai Boma Treaty",
                                "Burgess Model Act",
                                "Agricultural Land Title Act"
                            ],
                            "correct_answer": 0,
                            "explanation": "Trans-boundary chemical agreements enforce notifications and assistance during chemical emergencies."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Ramsar Site Lake Nakuru",
                        "content": {
                            "text": "Lake Nakuru was designated Kenya's first Ramsar Site of International Importance in 1990 to protect millions of lesser flamingos feeding on blue-green algae."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: NEMA Role",
                        "content": {
                            "mistake": "Stating that NEMA carries out construction projects.",
                            "correction": "NEMA DOES NOT build infrastructure; it REGULATES, AUDITS, and ISSUES LICENSES to ensure developers comply with environmental laws.",
                            "reasoning": "NEMA is a supervisory regulatory agency."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Legislation & Agreements: Key Takeaways",
                        "content": {
                            "title": "Legislation & Agreements: Key Takeaways",
                            "summary_points": [
                                "EMCA 1999 established NEMA as Kenya's principal environmental regulator.",
                                "Protected Mijikenda Kayas preserve sacred cultural heritage, biodiversity, and coastal water catchments.",
                                "EIA audits predict and mitigate environmental damage before major projects commence.",
                                "International treaties (Ramsar, CITES, Kyoto Accord, Chemical Notification) manage global environmental processes."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Community-Based Environmental Conservation and Rehabilitation Projects in Kenya (12 Pages)
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Community-Based Environmental Conservation and Rehabilitation Projects in Kenya",
            "unit_description": "Green Belt Movement, agroforestry, Haller Park 4-stage quarry reclamation, and gabion soil conservation.",
            "lesson_title": "Community-Based Environmental Conservation and Rehabilitation Projects in Kenya",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Community Conservation & Rehabilitation",
                        "content": {
                            "title": "Learning Objectives: Community Conservation & Rehabilitation",
                            "goals": [
                                "Examine the role of community initiatives: Green Belt Movement (Prof. Wangari Maathai) and Community Forest Associations (CFAs).",
                                "Analyze Agroforestry practices and Soil Conservation methods (contour terracing, gabions, check-dams).",
                                "Evaluate the 4-stage ecological land reclamation case study: Haller Park Quarry Reclamation in Bamburi, Mombasa."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Community Environmental Movements: Green Belt Movement",
                        "content": {
                            "title": "Community Environmental Movements: Green Belt Movement",
                            "text": "Grassroots community participation is essential for long-term environmental protection. The Green Belt Movement, founded in Kenya in 1977 by Nobel Peace Laureate Prof. Wangari Maathai, mobilizes rural women to establish tree nurseries and plant millions of trees across degraded water catchment towers.\n\nCore Contributions of Green Belt Movement:\n1. Environmental Restoration: Planted over 51 million indigenous trees across Kenya's water towers, restoring degraded forests.\n2. Women Empowerment & Rural Livelihoods: Paid rural women small stipends for growing surviving seedlings, combating rural poverty.\n3. Protection of Public Parks: Successfully protested against the construction of a 60-storey skyscraper inside Nairobi's Uhuru Park."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Green Belt Movement Community Reforestation Model",
                        "content": {
                            "title": "Green Belt Movement Community Reforestation Model",
                            "caption": "Community Reforestation: Women Tree Nurseries → Seedling Planting on Deforested Slopes → Water Tower Restoration + Stipend Livelihoods",
                            "description": "Flowchart diagram illustrating community tree nursery establishment leading to forest catchment restoration."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Kibera Slum Environmental Sanitation Strain Visualization",
                        "content": {
                            "title": "Kibera Slum Environmental Sanitation Strain Visualization",
                            "caption": "High-density settlement in Kibera illustrating urban environmental sanitation challenges.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Kibera_aerial_view_western_part.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Kibera_aerial_view_western_part.jpg"
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Soil Conservation & Rehabilitation Taxonomy",
                        "content": {
                            "term": "Soil Conservation & Land Rehabilitation Taxonomy",
                            "definition": "Engineering and biological techniques used to prevent soil erosion and restore degraded landscapes.",
                            "key_points": [
                                "Agroforestry: The deliberate integration of trees and shrubs with agricultural crops and/or livestock on the same farm parcel.",
                                "Gabion Check-Dams: Wire-mesh boxes filled with heavy stones installed across active erosion gullies to trap silt and slow runoff.",
                                "Contour Terracing: Constructing step-like horizontal benches along steep hillsides (Fanya Juu terraces) to stop down-slope soil wash.",
                                "Ecological Land Reclamation: Converting abandoned industrial mining quarries into thriving biodiverse ecosystems (e.g., Haller Park)."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Agroforestry Inter-Cropping & Soil Protection Diagram",
                        "content": {
                            "title": "Agroforestry Inter-Cropping & Soil Protection Diagram",
                            "caption": "Agroforestry Benefits: Nitrogen-Fixing Trees + Food Crops → Windbreak Protection + Leaf Humus Fertility + Fuelwood",
                            "description": "Agricultural diagram showing inter-cropping of leguminous trees with maize crops for soil enrichment and erosion control."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Gully Erosion Control via Gabion Check-Dams Diagram",
                        "content": {
                            "title": "Gully Erosion Control via Gabion Check-Dams Diagram",
                            "caption": "Gully Reclamation: Active Gully Stream → Wire-Mesh Gabion Stone Boxes → Silt Trapping & Vegetation Re-growth",
                            "description": "Engineering diagram illustrating gabion check-dams installed across gullies to trap sediment and slow flood waters."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Peri-Urban Land Conversion & Fringe Degradation Visualization",
                        "content": {
                            "title": "Peri-Urban Land Conversion & Fringe Degradation Visualization",
                            "caption": "Peri-urban settlement expansion on Nairobi's fringe replacing former agricultural land.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Haller Park Quarry Reclamation & Ecological Succession Model",
                        "content": {
                            "title": "Haller Park Quarry Reclamation & Ecological Succession Model",
                            "caption": "Quarry Rehabilitation: Abandoned Coral Quarry → Pioneer Casuarina Trees → Millipede Soil Enrichment → Ecotourism Nature Park",
                            "description": "Ecological succession diagram showing transformation of Bamburi coral quarry into Haller Park ecosystem."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Detailed 4-Stage Rehabilitation of Bamburi Quarry into Haller Park",
                        "content": {
                            "title": "Detailed 4-Stage Rehabilitation of Bamburi Quarry into Haller Park",
                            "text": "Haller Park in Bamburi, Mombasa is an internationally acclaimed case study of industrial quarry rehabilitation spearheaded by Dr. René Haller:\n\n• Stage 1 (Filling & Leveling): Abandoned, desolate coral quarry pits were filled with waste rocks and topped with a layer of fertile soil.\n\n• Stage 2 (Hardy Pioneer Planting): Hardy pioneer tree species (like Casuarina, which withstand high salinity and stony coral rock) were planted.\n\n• Stage 3 (Biological Soil Enrichment): Red-legged millipedes were introduced to feed on tough Casuarina needles, breaking them down into rich organic black humus soil.\n\n• Stage 4 (Fauna & Ecosystem Introduction): Diverse herbivores (giraffes, hippos, tortoises), fish species, and birds were introduced, establishing a thriving, self-sustaining ecotourism forest park."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Analysis: Benefits of Agroforestry to Smallholder Farmers",
                        "content": {
                            "question": "Explain four advantages of agroforestry practices to smallholder farming families in Kenya. (4 Marks)",
                            "strategy": "State benefit covering soil fertility, fuelwood, fodder, and income.",
                            "solution": [
                                "1. Soil Fertility Enrichment (1 Mark): Nitrogen-fixing trees (e.g., Leucaena, Calliandra) naturally add nitrogen to soil, reducing reliance on commercial fertilizers.",
                                "2. Fuelwood & Timber Provision (1 Mark): Farmers harvest firewood and building poles directly from farm trees, protecting natural forests.",
                                "3. Windbreak & Soil Erosion Protection (1 Mark): Tree rows act as windbreaks, reducing wind erosion and protecting delicate crops.",
                                "4. Livestock Fodder Supply (1 Mark): Tree leaves provide protein-rich fodder for dairy cows during dry seasons."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Rehabilitation Evaluator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Rehabilitation Evaluator",
                            "prompt": "Scenario: In Stage 3 of Haller Park's quarry rehabilitation, which biological organism was introduced to consume tough Casuarina tree needles and convert them into organic humus soil?",
                            "options": [
                                "Option A: Red-legged Millipedes.",
                                "Option B: Tsetse Flies.",
                                "Option C: Locusts."
                            ],
                            "correct_option": "Option A: Red-legged Millipedes.",
                            "explanation": "Red-legged millipedes feed on Casuarina needles, turning them into organic black humus soil."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Community Conservation",
                        "content": {
                            "question": "Which Nobel Peace Laureate founded Kenya's Green Belt Movement in 1977 to mobilize women in planting trees?",
                            "options": [
                                "Prof. Wangari Maathai",
                                "Mwai Kibaki",
                                "Dr. René Haller",
                                "Jomo Kenyatta"
                            ],
                            "correct_answer": 0,
                            "explanation": "Prof. Wangari Maathai founded the Green Belt Movement, winning the 2004 Nobel Peace Prize."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Fanya Juu Terracing",
                        "content": {
                            "text": "'Fanya Juu' (Swahili for 'Do Upwards') terracing involves digging a trench along hill contours and throwing the soil UP-SLOPE to form a ridge that traps eroding soil."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Agroforestry vs Reforestation",
                        "content": {
                            "mistake": "Confusing Agroforestry with Afforestation or Reforestation.",
                            "correction": "Agroforestry is combining trees WITH CROPS/LIVESTOCK ON FARMS. Afforestation is planting trees where none existed before.",
                            "reasoning": "Agroforestry is an integrated agricultural farming system."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Community Conservation: Key Takeaways",
                        "content": {
                            "title": "Community Conservation: Key Takeaways",
                            "summary_points": [
                                "Green Belt Movement mobilized women to plant over 51 million trees across Kenya.",
                                "Agroforestry enriches soil nitrogen, provides fuelwood, and stops wind erosion.",
                                "Gabion check-dams and Fanya Juu terraces control active gully erosion.",
                                "Haller Park demonstrates 4-stage biological reclamation (filling, Casuarina planting, millipede humus, fauna introduction)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Comparative Case Studies (Kenya vs Japan/Sweden), Topic Synthesis, and KCSE Review (8 Pages)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Comparative Case Studies (Kenya vs Japan/Sweden), Topic Synthesis, and KCSE Review",
            "unit_description": "Comparative case study (Kenya vs Japan/Sweden waste management), topic synthesis, and KCSE review.",
            "lesson_title": "Comparative Case Studies (Kenya vs Japan/Sweden), Topic Synthesis, and KCSE Review",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Environmental Synthesis",
                        "content": {
                            "title": "Learning Objectives: Environmental Synthesis",
                            "goals": [
                                "Compare environmental management and waste recycling strategies of Kenya and Japan/Sweden.",
                                "Master KCSE 10-mark essay questions on flood management and environmental legislation.",
                                "Complete end-of-topic revision assessment."
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Stockholm Sweden Environmental Urban Sustainability Model Visualization",
                        "content": {
                            "title": "Stockholm Sweden Environmental Urban Sustainability Model Visualization",
                            "caption": "Stockholm urban aerial view illustrating advanced environmental management and zero-waste recycling.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Aerial_view_of_Gamla_Stan%2C_Stockholm.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Aerial_view_of_Gamla_Stan%2C_Stockholm.jpg"
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Comparative Case Study: Kenya vs Japan/Sweden Environmental Management",
                        "content": {
                            "title": "Comparative Case Study: Kenya vs Japan/Sweden Environmental Management",
                            "text": "Comparing Kenya (a developing nation) and Japan/Sweden (highly developed nations) reveals contrasting environmental management paradigms:\n\n1. Waste Recycling Infrastructure: Kenya relies heavily on open unsegregated dumpsites (Dandora), recovering <10% of recyclable waste. Sweden recycles over 99% of household waste, importing garbage from neighboring nations to fuel waste-to-energy power plants.\n\n2. Industrial Emission Enforcement: Kenya faces financial and enforcement constraints monitoring industrial polluters. Japan enforces ultra-strict zero-emission standards using automated sensors on all industrial chimneys.\n\n3. Environmental Public Awareness: Sweden integrates mandatory environmental literacy across all school grades, achieving near-universal public sorting of household waste into 7 distinct bins."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "comparison_table",
                        "title": "Kenya vs Sweden Environmental Management Comparison Matrix",
                        "content": {
                            "headers": ["Environmental Metric", "Kenya Profile", "Sweden Profile"],
                            "rows": [
                                ["Development Category", "Developing Nation", "Developed Post-Industrial Nation"],
                                ["Waste Management System", "Open dumpsites (Dandora); low recycling (<10%)", "Integrated circular economy; 99% waste recycled / converted to energy"],
                                ["Primary Energy Source", "Hydroelectric (HEP) & Geothermal", "Hydroelectric, Wind, & Waste-to-Energy Incineration"],
                                ["Environmental Law Enforcement", "NEMA enforcement hindered by budget/logistics", "Strict automated environmental monitoring & heavy fines"],
                                ["Community Conservation Model", "Green Belt Movement agroforestry & CFAs", "Universal household waste segregation into 7 bins"]
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 1: Causes and Control Measures of River Flooding",
                        "content": {
                            "question": "Explain three physical causes of flooding in the Kano Plains and three management strategies used to control the floods. (6 Marks)",
                            "strategy": "Separate into 3 Physical Causes (3 Marks) and 3 Management Measures (3 Marks).",
                            "solution": [
                                "1. Physical Causes of Flooding (3 Marks):\n   • Heavy Relief Rainfall: Heavy rainfall in the surrounding Nandi Highlands generates massive surface runoff into River Nyando.\n   • Low Flat Topography: Kano Plains feature low, flat relief that retards river flow, causing water to spill over banks.\n   • River Siltation: Erosion in highlands deposits silt on the river bed, reducing channel capacity.",
                                "2. Management Control Measures (3 Marks):\n   • Building Artificial Dykes: Constructing raised embankments along River Nyando to contain floodwaters.\n   • Catchment Afforestation: Planting trees in Nandi Hills to increase infiltration and reduce runoff.\n   • Dredging River Channels: Removing silt from River Nyando bed to deepen carrying capacity."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 2: Environmental Impact Assessment (EIA) and NEMA",
                        "content": {
                            "question": "Discuss five reasons why NEMA requires developers to submit an Environmental Impact Assessment (EIA) before constructing major factories in Kenya. (10 Marks)",
                            "strategy": "Explain 5 statutory objectives of EIA audits (2 Marks each).",
                            "solution": [
                                "1. Identifying Potential Environmental Hazards (2 Marks): Predicting air, water, and soil pollution risks before construction starts.",
                                "2. Formulating Pollution Mitigation Plans (2 Marks): Ensuring developers install effluent treatment plants and electrostatic precipitator scrubbers.",
                                "3. Protecting Public Health (2 Marks): Preventing toxic chemical leaks near residential areas.",
                                "4. Facilitating Public Participation (2 Marks): Solicit input and objections from local communities affected by the factory.",
                                "5. Ensuring Legal Compliance with EMCA 1999 (2 Marks): Verifying that project operations comply with national environmental laws."
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "definition_card",
                        "title": "Master Glossary of Geography Environment Terms",
                        "content": {
                            "term": "Geography Environment Master Glossary",
                            "definition": "Essential textbook definitions required for KCSE Geography Paper 2.",
                            "key_points": [
                                "Environmental Management: Planned sustainable utilization and protection of natural resources.",
                                "Environmental Conservation: Preservation and protection of natural resources from destruction.",
                                "Eutrophication: Nutrient enrichment of water bodies triggering algal blooms and hypoxia.",
                                "Environmental Hazard: Extreme natural or man-made event posing threat to life and property.",
                                "EIA: Environmental Impact Assessment study predicting project ecological impacts.",
                                "NEMA: National Environment Management Authority of Kenya.",
                                "Agroforestry: Combining trees with agricultural crops and livestock on farms.",
                                "Gabion: Wire-mesh stone box installed across gullies to stop soil erosion."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic 10 Mastery Assessment Question",
                        "content": {
                            "question": "Which environmental strategy distinguishes Sweden's waste management paradigm from Kenya's?",
                            "options": [
                                "Sweden recycles over 99% of household waste and converts waste to energy.",
                                "Sweden dumps all waste into open river channels.",
                                "Sweden bans all tree planting.",
                                "Sweden has no environmental laws."
                            ],
                            "correct_answer": 0,
                            "explanation": "Sweden leads the world in waste recycling, converting over 99% of waste into energy."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "summary",
                        "title": "Topic 10 Mastery Synthesis & Review",
                        "content": {
                            "title": "Topic 10 Mastery Synthesis & Review",
                            "summary_points": [
                                "Environmental Management plans sustainable use; Conservation preserves ecosystems.",
                                "Floods and droughts are natural hazards managed via dykes, dams, and sand dams.",
                                "NEMA enforces EMCA 1999 through mandatory Environmental Impact Assessments (EIA).",
                                "Community initiatives (Green Belt Movement, Haller Park 4-stage reclamation, Agroforestry) lead land rehabilitation.",
                                "Form 4 Geography Topic 10 (Management and Conservation of the Environment) Ingestion is 100% Complete & Production Ready!"
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic10():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 10: Management and Conservation of the Environment")
    print("In-Place Production Ingestion Engine (100% Aligned with Lessons.md)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()

    if not subject:
        print("[!] Error: Subject 'Geography' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Management and Conservation of the Environment"

    # Match topic by order or name in-place
    topic = Topic.objects.filter(subject=subject, order=10).first()
    if not topic:
        topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=10,
            description="Comprehensive syllabus on environmental management vs conservation, endangered species (Meru Oak, Rosewood, White Rhino), ecosystem services, natural and human-induced hazards (floods in Budalangi/Kano Plains, droughts, lightning in Kakamega/Kisii, ICIPE biological tsetse control in Lambwe Valley), pollution vectors (SO2 acid rain vs leaded fuel poisoning, Lake Victoria eutrophication, open-cast mining dereliction), NEMA and EMCA 1999 legislation, protected Mijikenda Kayas, Environmental Impact Assessment (EIA), waste management hierarchy, international conventions (Ramsar, CITES, Kyoto, Trans-boundary Chemical Notifications), community initiatives (Green Belt Movement, agroforestry, gabions, 4-stage Haller Park quarry reclamation), and comparative case studies (Kenya vs Sweden/Japan)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        topic.name = topic_name
        topic.order = 10
        topic.description = "Comprehensive syllabus on environmental management vs conservation, endangered species (Meru Oak, Rosewood, White Rhino), ecosystem services, natural and human-induced hazards (floods in Budalangi/Kano Plains, droughts, lightning in Kakamega/Kisii, ICIPE biological tsetse control in Lambwe Valley), pollution vectors (SO2 acid rain vs leaded fuel poisoning, Lake Victoria eutrophication, open-cast mining dereliction), NEMA and EMCA 1999 legislation, protected Mijikenda Kayas, Environmental Impact Assessment (EIA), waste management hierarchy, international conventions (Ramsar, CITES, Kyoto, Trans-boundary Chemical Notifications), community initiatives (Green Belt Movement, agroforestry, gabions, 4-stage Haller Park quarry reclamation), and comparative case studies (Kenya vs Sweden/Japan)."
        topic.save()
        print(f"[*] Preserving existing Topic ID: {topic.id} ({topic.name})")

    curriculum_data = build_topic10_curriculum()
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

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
                lesson.title = lesson_title
                lesson.status = "published"
                lesson.save()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingested Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Page {page_idx}")
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
            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Geography Topic 10 (Management and Conservation of the Environment) Ingested In-Place!")
    print(f"[*] Topic ID Preserved:     {topic.id}")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_form4_geography_topic10()
