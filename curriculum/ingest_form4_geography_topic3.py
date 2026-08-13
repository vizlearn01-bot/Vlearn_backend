"""
VLearn Form 4 Geography — Topic 3: Wildlife and Tourism
High-Structure Production Ingestion Engine

Topic: Wildlife and Tourism (Topic Order: 3)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (80 Total Pages):
  1. Foundations of Wildlife and Ecological Distribution Factors (12 Pages)
  2. Protected Area Systems (National Parks, Reserves, and Sanctuaries) (12 Pages)
  3. Wildlife Significance, Threats, and Environmental Management (14 Pages)
  4. Tourism Concepts, Classifications, and Influencing Factors (12 Pages)
  5. Spatial Distribution of Kenya's Coastal and Inland Attractions (14 Pages)
  6. Comparative Analysis (Kenya vs Switzerland) and Strategic Expansion (16 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic3.py [--replace]
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
    """Removes bracket citations [13], [25, 26], [S1, p. 1] and cleans double spaces."""
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

def build_topic3_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 3."""
    return [
        # =====================================================================
        # LESSON 1: Foundations of Wildlife and Ecological Distribution Factors
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Foundations of Wildlife and Ecological Distribution Factors",
            "unit_description": "Foundational concepts of wildlife ecosystems and physical/human factors influencing spatial distribution in East Africa.",
            "lesson_title": "Foundations of Wildlife and Ecological Distribution Factors",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Wildlife Foundations",
                        "content": {
                            "title": "Learning Objectives: Wildlife Foundations",
                            "goals": [
                                "Define the geographical concepts of wildlife, flora, and fauna.",
                                "Examine the five key physical factors governing wildlife distribution in East Africa.",
                                "Analyze how rainfall, mountain aspect, and slope gradients create distinct ecological niches.",
                                "Evaluate human interventions shaping wildlife distribution."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Topic 3: Wildlife and Tourism",
                        "content": {
                            "title": "Welcome to Topic 3: Wildlife and Tourism",
                            "text": "Wildlife—consisting of plants (flora) and animals (fauna) in their natural, undisturbed habitats—is one of East Africa's most valuable heritage assets. Together with tourism, it forms a critical pillar of economic development, foreign exchange earnings, and ecological balance across Kenya, Uganda, and Tanzania."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Geographical Definition of Wildlife",
                        "content": {
                            "term": "Wildlife",
                            "definition": "All plants (flora) and animals (fauna) living in their natural, undisturbed habitats within self-sustaining ecosystems.",
                            "key_points": [
                                "Flora: All indigenous plant life, forests, scrub, and grasses.",
                                "Fauna: All wild animal species, mammals, birds, reptiles, and fish.",
                                "Habitat: The natural ecological environment in which an organism feeds, breeds, and lives."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ecosystem Balance in Wildlife Geography",
                        "content": {
                            "title": "Ecosystem Balance in Wildlife Geography",
                            "text": "Wildlife represents a dynamic, self-sustaining ecological system where organisms continuously interact with their physical environment. Energy flows from primary producers (plants harnessing solar radiation) to herbivores (ungulates like zebras and gazelles) and apex carnivores (lions, cheetahs, and leopards)."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Ecological Factor Web of East African Wildlife Distribution",
                        "content": {
                            "title": "Ecological Factor Web of East African Wildlife Distribution",
                            "caption": "Interconnected Physical and Human Variables Controlling Wildlife Zonation in East Africa",
                            "description": "Comprehensive ecological web illustrating how climate, relief, soils, vegetation, water sources, and human settlements determine spatial fauna distribution."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Factor 1: Climate (Rainfall and Temperature Gradients)",
                        "content": {
                            "title": "Factor 1: Climate (Rainfall and Temperature Gradients)",
                            "text": "Rainfall volume and reliability directly dictate vegetation density and herbivore carrying capacity:\n\n• Heavy Rainfall Zones (>1,200 mm): Support dense tropical and montane rainforests with rich canopy cover, providing ideal habitat for large browsers and herbivores like elephants, buffaloes, and colobus monkeys (e.g., Mount Kenya and Aberdare forests).\n\n• Arid and Semi-Arid Lands (ASALs <500 mm): Support drought-resistant thorny scrub and acacia savannas, occupied by specially adapted animals capable of withstanding water scarcity, such as the gerenuk, hartebeest, and ostrich."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Factor 2: Relief (Aspect and Terrain Gradients)",
                        "content": {
                            "title": "Factor 2: Relief (Aspect and Terrain Gradients)",
                            "text": "Topography influences wildlife distribution through slope orientation (aspect) and ground slope:\n\n1. Aspect (Slope Orientation):\n• Windward slopes receive moist orographic rainfall, nurturing dense montane forests that shelter large mammals.\n• Leeward slopes lie in dry rain shadows with low precipitation, resulting in open savannas where cursorial carnivores hunt migratory herbivores (e.g., Amboseli National Park on the leeward base of Mount Kilimanjaro).\n\n2. Terrain (Slope Gradient):\n• Wide, flat plains and plateaus favor high-speed cursorial hunters like cheetahs, allowing unhindered pursuit of prey without topographical obstacles.\n• Steep, rocky escarpments and mountainous crags provide specialized refuge for rock hyraxes and klipspringers."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Insight: Cursorial Hunters on Savanna Plains",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Insight: Cursorial Hunters on Savanna Plains",
                            "text": "Cheetahs can accelerate from 0 to 100 km/h in three seconds. They depend on expansive, level savanna grasslands devoid of dense thickets or rugged rock outcrops to execute high-speed pursuits."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Relief and Aspect Profile: Windward Forest vs Leeward Rain-Shadow Savanna",
                        "content": {
                            "title": "Relief and Aspect Profile: Windward Forest vs Leeward Rain-Shadow Savanna",
                            "caption": "Cross-Section of Mountain Aspect Creating Contrasting Montane Forest and Savanna Grassland Habitats",
                            "description": "Topographic profile showing moist air rising on windward slopes producing dense cloud forests, descending dry air forming leeward rain-shadow savanna plains."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Rain-Shadow Savanna Microclimates",
                        "content": {
                            "title": "Rain-Shadow Savanna Microclimates",
                            "text": "The rain shadow effect produces open grassland biomes that support the highest biomass of wild ungulates on Earth. The short grasses allow clear visual surveillance for grazing herds, while providing open visibility for ambush predators like lions and leopards."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Factor 3: Soils (Fertility, Depth, and Mineral Drainage)",
                        "content": {
                            "title": "Factor 3: Soils (Fertility, Depth, and Mineral Drainage)",
                            "text": "Soil characteristics directly determine primary plant productivity:\n\n• Deep, fertile volcanic soils (found in highlands and Rift Valley slopes) retain moisture and support dense multi-tier forests.\n\n• Shallow, leached, or saline soils (common in ASALs and rift lake basins) cannot sustain dense tree canopies, fostering open grasslands and saline-tolerant shrubs that attract massive herds of grazing ungulates (zebras, wildebeests) and specialized birds (flamingos)."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "comparison_table",
                        "title": "Vegetation Biomes and Wildlife Niches in East Africa",
                        "content": {
                            "headers": ["Vegetation Zone", "Dominant Plant Species", "Adapted Wildlife Species", "Ecological Adaptation"],
                            "rows": [
                                ["Montane Rainforest", "Camphor, Podocarpus, Bamboo", "Elephant, Buffalo, Colobus Monkey", "Thick skin, arboreal locomotion, browse foliage"],
                                ["Acacia Savanna", "Acacia tortilis, Baobab, Red Oat Grass", "Giraffe, Zebra, Wildebeest, Lion", "Long necks for high browse, herd defense, sprint speed"],
                                ["Semi-Desert Scrub", "Commiphora, Euphorbia, Thorny scrub", "Gerenuk, Oryx, Hartebeest, Ostrich", "Elongated neck, concentrated urine, nocturnal foraging"],
                                ["Freshwater Swamps", "Papyrus reeds, Water lilies", "Hippopotamus, Sitatunga, Crocodile", "Submerged temperature regulation, amphibious locomotion"]
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Thomson's Gazelle in the Open Savanna Plains of Amboseli National Park",
                        "content": {
                            "title": "Thomson's Gazelle in the Open Savanna Plains of Amboseli National Park",
                            "caption": "Fast-running Thomson's gazelle grazing on the open savanna plains of Amboseli National Park with Mount Kilimanjaro on the horizon.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/db/Gacela_de_Thomson_%28Eudorcas_thomsonii%29%2C_parque_nacional_de_Amboseli%2C_Kenia%2C_2024-05-23%2C_DD_11.jpg",
                            "author": "Diego Delso, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Gacela_de_Thomson_(Eudorcas_thomsonii),_parque_nacional_de_Amboseli,_Kenia,_2024-05-23,_DD_11.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ecology of Savanna Herbivores",
                        "content": {
                            "title": "Ecology of Savanna Herbivores",
                            "text": "Thomson's and Grant's gazelles thrive in open savannas where short grasses provide high-energy nutrients and open sightlines allow early detection of approaching predators like cheetahs, hyenas, and lions."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Factor 5: Water Availability and Human Activities",
                        "content": {
                            "title": "Factor 5: Water Availability and Human Activities",
                            "text": "Water availability dictates seasonal migrations and permanent territory boundaries:\n\n• Permanent water bodies (Lake Victoria, Lake Naivasha, River Tana) support permanent semi-aquatic populations of hippos and crocodiles.\n\n• Seasonal waterholes in Tsavo and Amboseli trigger massive dry-season migrations of elephants and wildebeests toward river basins.\n\nHuman Interventions:\n• Negative: Habitat destruction through deforestation, agricultural conversion, urban sprawl, and commercial poaching.\n• Positive: Establishment of protected areas (parks, reserves, sanctuaries) and community conservancies."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Distribution Factor Analysis",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Distribution Factor Analysis",
                            "prompt": "An ecological team is surveying a semi-arid plain located on the dry leeward side of a Kenyan volcanic mountain. The soil is shallow with scattered acacia bushes. Which wildlife community will naturally thrive here?",
                            "options": [
                                "Option A: Elephants, bamboo-feeding primates, and canopy birds.",
                                "Option B: Gerenuks, giraffes, cheetahs, and open grassland ungulates.",
                                "Option C: Amphibious hippos, sitatungas, and dense forest duikers."
                            ],
                            "correct_option": "Option B: Gerenuks, giraffes, cheetahs, and open grassland ungulates.",
                            "explanation": "Gerenuks and giraffes are specialized browsers adapted to dry acacia scrub. Open flat plains provide the necessary terrain for cheetah hunting sprints, whereas montane canopy species require high moisture and dense forests."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Wildlife Distribution",
                        "content": {
                            "question": "Why do flat, open savanna plains favor cursorial predators like cheetahs over mountainous montane forests?",
                            "options": [
                                "Flat plains have higher rainfall that sustains prey herds year-round.",
                                "Level terrain eliminates physical barriers, allowing unhindered high-speed pursuit of prey.",
                                "Montane forests contain higher concentrations of toxic plants.",
                                "Cheetahs require cold mountain temperatures for muscle stamina."
                            ],
                            "correct_answer": 1,
                            "explanation": "Cheetahs rely on high-speed acceleration across unobstructed, flat savanna plains to capture fast ungulates like gazelles."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Foundations of Wildlife: Key Takeaways",
                        "content": {
                            "title": "Foundations of Wildlife: Key Takeaways",
                            "summary_points": [
                                "Wildlife encompasses flora and fauna inhabiting natural, self-sustaining ecosystems.",
                                "Rainfall reliability directly determines forest vs savanna vegetation density and animal biomass.",
                                "Mountain aspect creates windward cloud forests (browsers) and leeward rain shadows (savanna herds & predators).",
                                "Soil depth and drainage determine primary grassland productivity.",
                                "Water availability drives seasonal migration patterns across East African protected ecosystems."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Protected Area Systems (National Parks, Reserves, and Sanctuaries)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Protected Area Systems (National Parks, Reserves, and Sanctuaries)",
            "unit_description": "Legal, administrative, and spatial classifications of National Parks, Game Reserves, and Game Sanctuaries in East Africa.",
            "lesson_title": "Protected Area Systems (National Parks, Reserves, and Sanctuaries)",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Protected Area Systems",
                        "content": {
                            "title": "Learning Objectives: Protected Area Systems",
                            "goals": [
                                "Classify protected areas into National Parks, Game Reserves, and Game Sanctuaries.",
                                "Differentiate protected areas based on legal statutes, managing authorities, and land-use rules.",
                                "Analyze why Maasai Mara is classified as a Game Reserve rather than a National Park.",
                                "Examine the role of specialized game sanctuaries in endangered species conservation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Framework of Protected Ecosystems",
                        "content": {
                            "title": "The Framework of Protected Ecosystems",
                            "text": "To safeguard biodiversity from human encroachment and poaching, East African nations have gazetted extensive protected areas. In Kenya, these conservation zones are divided into three distinct legal and administrative categories: National Parks, Game Reserves, and Game Sanctuaries."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Classification Hierarchy of Protected Areas (Parks, Reserves, Sanctuaries)",
                        "content": {
                            "title": "Classification Hierarchy of Protected Areas (Parks, Reserves, Sanctuaries)",
                            "caption": "Administrative, Legal, and Land-Use Taxonomy of East African Conservation Systems",
                            "description": "Taxonomy tree showing National Parks (National Gov / Single-Use), Game Reserves (Local Authority / Multi-Use), and Game Sanctuaries (Targeted Endangered Species Protection)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Classification Criteria for Conservation Areas",
                        "content": {
                            "title": "Classification Criteria for Conservation Areas",
                            "text": "Protected areas are distinguished by three essential geographical criteria:\n\n1. Legal Authority: Established by national parliamentary statutes vs local county council by-laws.\n2. Management Entity: Direct national government administration (KWS) vs local county council management.\n3. Permitted Land Use: Single-purpose wildlife preservation vs multi-use coexistence with pastoralist grazing."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Category 1: National Parks",
                        "content": {
                            "term": "National Park",
                            "definition": "A large conservation area established strictly by an Act of Parliament, managed directly by the National Government (Kenya Wildlife Service), and exclusively reserved for wildlife protection and tourism.",
                            "key_points": [
                                "Legal Statute: Act of Parliament (National Law).",
                                "Management: Kenya Wildlife Service (KWS) / Paramilitary Wardens.",
                                "Land-Use Rules: Strict Single-Use. No human settlement, farming, logging, or livestock grazing permitted under any circumstances.",
                                "Fencing: Often completely fenced with electric perimeters to mitigate human-wildlife conflict.",
                                "Examples: Tsavo (East & West), Amboseli, Nairobi, Mount Kenya, Lake Nakuru, Mombasa Marine."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Operational Mandate of National Parks",
                        "content": {
                            "title": "Operational Mandate of National Parks",
                            "text": "National parks are designed to preserve regional landscapes, complex biodiversity, and prehistoric/historical sites in their pristine state. Revenue collected from visitor entry fees goes directly to the national treasury and KWS conservation funds."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Zonation and Land-Use Boundaries of a National Park vs Game Reserve",
                        "content": {
                            "title": "Zonation and Land-Use Boundaries of a National Park vs Game Reserve",
                            "caption": "Comparative Spatial Mapping of Strict Single-Use Park Perimeter vs Multi-Use Pastoralist Grazing Buffer",
                            "description": "Spatial zonation diagram contrasting a fenced single-use National Park with a multi-use Game Reserve accommodating managed pastoral cattle grazing."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Boundary Dynamics and Zonation",
                        "content": {
                            "title": "Boundary Dynamics and Zonation",
                            "text": "While National Parks enforce strict physical boundaries with armed paramilitary patrols, Game Reserves often feature open boundary interfaces with surrounding communal pastoral lands, facilitating seasonal wildlife migrations."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "definition_card",
                        "title": "Category 2: Game Reserves",
                        "content": {
                            "term": "Game Reserve",
                            "definition": "A conservation area set aside under local county authority by-laws, managed by the local county government, operating as a multi-use zone where wildlife coexists with regulated seasonal livestock grazing.",
                            "key_points": [
                                "Legal Statute: Local Authority / County Council By-Laws.",
                                "Management: Local County Government (e.g., Narok County for Maasai Mara).",
                                "Land-Use Rules: Multi-Use Conservation. Accommodates wildlife preservation alongside managed dry-season livestock grazing by local pastoralists.",
                                "Fencing: Usually unfenced, allowing natural migration into communal grazing lands.",
                                "Examples: Maasai Mara (Kenya), Samburu Game Reserve (Kenya), Selous Game Reserve (Tanzania)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Socioeconomic Integration in Game Reserves",
                        "content": {
                            "title": "Socioeconomic Integration in Game Reserves",
                            "text": "Game reserves foster community integration by allowing local pastoral communities (such as the Maasai) access to traditional watering points and pastures during severe droughts, while revenue is reinvested in local schools, clinics, and infrastructure."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "definition_card",
                        "title": "Category 3: Game Sanctuaries",
                        "content": {
                            "term": "Game Sanctuary",
                            "definition": "A specialized, highly secure conservation sanctuary set aside specifically for the intensive protection, rehabilitation, and captive breeding of rare or endangered animal species.",
                            "key_points": [
                                "Target Focus: Specialized protection of one or two threatened species (e.g., black rhinos, impalas, orphaned elephants).",
                                "Management: Managed by KWS, research trusts, or private conservation organizations.",
                                "Predator Control: Apex predators (lions, leopards, hyenas) are strictly controlled or excluded to safeguard vulnerable juveniles.",
                                "Breeding & Release: Animals are bred, rehabilitated, and later released into underpopulated national parks.",
                                "Examples: Kisumu Impala Sanctuary, Rhino Sanctuary at Lake Nakuru National Park, Mwaluganje Elephant Sanctuary."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Role of Sanctuaries in Species Recovery",
                        "content": {
                            "title": "Role of Sanctuaries in Species Recovery",
                            "text": "Sanctuaries serve as vital ecological safety nets. By eliminating natural predation and providing veterinary intervention, sanctuaries enable endangered populations (like the black rhino) to multiply beyond the critical extinction threshold."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Specialized Sanctuary Architecture & Captive Breeding Cycle",
                        "content": {
                            "title": "Specialized Sanctuary Architecture & Captive Breeding Cycle",
                            "caption": "Operational Layout of a Rhino Sanctuary: Predator Exclusion, Intensive Care Nursery, and Release Corridors",
                            "description": "Schematic blueprint showing predator-proof perimeter fencing, veterinary nursery, breeding paddocks, and release corridors into wild national parks."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sanctuary Engineering and Veterinary Support",
                        "content": {
                            "title": "Sanctuary Engineering and Veterinary Support",
                            "text": "High-security sanctuaries deploy solar-powered multi-strand electric fences, 24/7 armed ranger surveillance, microchip satellite tracking horns, and specialized veterinary stations for emergency treatment."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Endangered Black Rhinoceros in Lake Nakuru Protected Sanctuary",
                        "content": {
                            "title": "Endangered Black Rhinoceros in Lake Nakuru Protected Sanctuary",
                            "caption": "A protected adult male black rhinoceros (Diceros bicornis) grazing inside the secure Lake Nakuru Rhino Sanctuary in the Great Rift Valley.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Black_Rhino_%28Diceros_bicornis%29_%288290870387%29.jpg",
                            "author": "Bernard DUPONT, Wikimedia Commons",
                            "licensing": "CC BY-SA 2.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Black_Rhino_(Diceros_bicornis)_(8290870387).jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Lake Nakuru Rhino Sanctuary Case Study",
                        "content": {
                            "title": "Lake Nakuru Rhino Sanctuary Case Study",
                            "text": "Lake Nakuru was gazetted as Kenya's first fully enclosed, government-protected rhino sanctuary in 1987. It has successfully raised black and white rhino numbers, serving as a primary breeding bank for translocations across East Africa."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "comparison_table",
                        "title": "Three-Way Comparative Matrix of East African Protected Areas",
                        "content": {
                            "headers": ["Feature", "National Park", "Game Reserve", "Game Sanctuary"],
                            "rows": [
                                ["Legal Authority", "Act of Parliament (National Law)", "Local County Council By-Laws", "Government / Specialized Trust Gazettement"],
                                ["Managing Body", "Kenya Wildlife Service (KWS)", "Local County Government / Councils", "KWS / Private Conservation Trusts"],
                                ["Land Use Status", "Strict Single-Use (Wildlife & Tourism only)", "Multi-Use (Wildlife & Pastoral Grazing)", "Intensive Single-Species Security & Breeding"],
                                ["Livestock Grazing", "Strictly Prohibited & Criminalized", "Permitted on Regulated Seasonal Basis", "Strictly Prohibited"],
                                ["Fencing", "Often fully enclosed with electric fence", "Largely open boundaries to pastoral lands", "Heavily fortified predator-proof perimeters"],
                                ["Prime Objective", "Ecosystem & Scenery Preservation", "Communal Coexistence & Local Revenue", "Species Extinction Prevention & Translocation"]
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Exam Warning: The Maasai Mara Reserve Misconception",
                        "content": {
                            "mistake": "Writing that 'Maasai Mara is Kenya's largest National Park.'",
                            "correction": "Maasai Mara is a Game Reserve, not a National Park.",
                            "reasoning": "Maasai Mara is managed by the Narok County Government (local authority) and permits regulated seasonal cattle grazing by Maasai pastoralists, violating the single-use national definition of a National Park."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "KCSE Marking Guidance",
                        "content": {
                            "type": "warning",
                            "title": "KCSE Marking Guidance",
                            "text": "Examiners will immediately deduct marks if Maasai Mara is cited as an example of a National Park. Use Tsavo, Amboseli, Nairobi, or Lake Nakuru as standard National Park examples."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Protected Area Systems",
                        "content": {
                            "question": "Which of the following characteristics fundamentally distinguishes a Game Reserve from a National Park?",
                            "options": [
                                "Game Reserves are managed directly by the National Parliament.",
                                "Game Reserves allow regulated multi-use seasonal livestock grazing by local pastoralists.",
                                "Game Reserves do not permit international tourists.",
                                "Game Reserves are exclusively dedicated to marine ecosystems."
                            ],
                            "correct_answer": 1,
                            "explanation": "Game reserves are multi-use conservation zones managed by local county councils, permitting regulated seasonal grazing by local pastoral communities alongside wildlife."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Protected Areas: Key Takeaways",
                        "content": {
                            "title": "Protected Areas: Key Takeaways",
                            "summary_points": [
                                "National Parks are single-use ecosystems established by Acts of Parliament and managed by KWS.",
                                "Game Reserves are multi-use zones established under county by-laws that permit regulated pastoral livestock grazing.",
                                "Game Sanctuaries provide specialized security and captive breeding for endangered species (rhinos, impalas).",
                                "Maasai Mara is a Game Reserve managed by Narok County Council.",
                                "Sanctuary predator control and breeding cycles provide stock for replenishing depleted national parks."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Wildlife Significance, Threats, and Environmental Management
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Wildlife Significance, Threats, and Environmental Management",
            "unit_description": "Economic and ecological significance of wildlife, analysis of natural and human threats, and management vs conservation strategies.",
            "lesson_title": "Wildlife Significance, Threats, and Environmental Management",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Significance, Threats & Management",
                        "content": {
                            "title": "Learning Objectives: Significance, Threats & Management",
                            "goals": [
                                "Evaluate the multifaceted economic and ecological value of wildlife to East Africa.",
                                "Examine human-induced and natural threats facing wildlife ecosystems.",
                                "Distinguish between wildlife management measures and wildlife conservation measures.",
                                "Analyze the step-by-step logistics of KWS animal translocation programs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Strategic Role of Wildlife Resources",
                        "content": {
                            "title": "The Strategic Role of Wildlife Resources",
                            "text": "Wildlife is not merely an aesthetic natural asset; it is a primary economic engine, an ecological stabilizer, and a catalyst for rural infrastructure development across Kenya and East Africa."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Eight Dimensions of Wildlife Significance",
                        "content": {
                            "title": "Eight Dimensions of Wildlife Significance",
                            "text": "1. Foreign Exchange Earnings: Wildlife tourism attracts international visitors who pay park entry and lodge accommodation fees in foreign currency, funding national development and import balances.\n\n2. Productive Use of Marginal Lands: Over 80% of Kenya is semi-arid (ASAL) where agriculture is unviable. Wildlife conservation turns these marginal lands into productive, revenue-generating zones.\n\n3. Employment Creation: Directly employs thousands of citizens as KWS rangers, tour guides, safari drivers, and hospitality staff, raising local living standards.\n\n4. Ecological and Water Catchment Protection: Forested wildlife reserves preserve major water towers (Mt. Kenya, Aberdares), reduce soil erosion, and regulate regional precipitation.\n\n5. Infrastructure Stimulus: To access remote parks, governments build tarmac highways, bridges, and airstrips, opening up isolated rural districts.\n\n6. Economic Diversification: Prevents over-reliance on rain-fed agriculture, buffering the national economy against drought and commodity price drops.\n\n7. Medicinal & Traditional Heritage: Wild plant species provide pharmacological compounds and traditional herbal remedies.\n\n8. Educational & Scientific Research: Serves as a global living laboratory for genetics, ecology, and veterinary medicine."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Economic Multiplier: ASAL Land Monetization",
                        "content": {
                            "type": "tip",
                            "title": "Economic Multiplier: ASAL Land Monetization",
                            "text": "Converting dry semi-arid scrublands into wildlife conservancies (e.g., in Samburu and Laikipia) generates substantially higher gross domestic product per hectare than low-yield subsistence farming."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Threat Matrix: Human-Induced vs Natural Pressures on East African Wildlife",
                        "content": {
                            "title": "Threat Matrix: Human-Induced vs Natural Pressures on East African Wildlife",
                            "caption": "Dual-Column Structural Threat Matrix: Anthropogenic Exploitation vs Climatic & Biological Disasters",
                            "description": "Diagram contrasting human-induced threats (poaching, encroachment, pollution, off-road driving) with natural threats (severe drought, bushfires, floods, epidemic diseases)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Human-Induced Pressures on Wildlife",
                        "content": {
                            "title": "Human-Induced Pressures on Wildlife",
                            "text": "• Commercial Poaching: Armed hunting for high-value contraband (elephant ivory tusks, rhino horns, leopard skins) severely depletes breeding populations.\n• Agricultural Encroachment: Rapid human population growth leads to farming expansion into traditional migration corridors, causing severe habitat fragmentation.\n• Human-Wildlife Conflict: Straying elephants destroy crops, while carnivores kill pastoral livestock, leading to retaliatory poisoning of lions and leopards.\n• Tour Vehicle Degradation: Off-road safari driving destroys fragile grass root systems and causes severe acoustic stress to feeding and breeding animals."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "callout",
                        "title": "Case Study: Industrial & Sewage Pollution at Lake Nakuru",
                        "content": {
                            "type": "warning",
                            "title": "Case Study: Industrial & Sewage Pollution at Lake Nakuru",
                            "text": "Untreated domestic sewage and industrial effluent discharged from Nakuru municipality into Lake Nakuru caused catastrophic algal blooms and heavy metal poisoning, leading to the mass mortality and migration of millions of lesser flamingos."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Environmental Audits and Remedial Interventions",
                        "content": {
                            "title": "Environmental Audits and Remedial Interventions",
                            "text": "To counter aquatic pollution, the government and KWS mandate strict environmental impact assessments (EIAs), construct modern municipal sewage treatment works, and monitor factory effluent drainage into the Rift Valley catchment."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Natural Threats: Climatic Shocks, Wildfires, and Diseases",
                        "content": {
                            "title": "Natural Threats: Climatic Shocks, Wildfires, and Diseases",
                            "text": "Wildlife is intensely vulnerable to natural environmental disasters:\n\n1. Prolonged Drought: Dries up rivers, depletes browse, and causes mass starvation and dehydration among herbivores (e.g., Tsavo elephant mortalities during extended droughts).\n\n2. Uncontrolled Bushfires: Triggered by lightning or dry season friction, wildfires incinerate slow-moving animals, destroy thousands of hectares of cover, and expose soils to rapid wind erosion.\n\n3. Flash Floods: Submerge low-lying grasslands and drown terrestrial wildlife in river valleys.\n\n4. Epizootic Diseases: Pathogens such as Rinderpest, Anthrax, and Feline Immunodeficiency Virus (FIV) can decimate entire lion prides and ungulate herds."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The KWS Wildlife Management vs Conservation Strategic Framework",
                        "content": {
                            "title": "The KWS Wildlife Management vs Conservation Strategic Framework",
                            "caption": "Bifurcated Strategic Framework Distinguishing Resource Management (Regulated Use) from Conservation (Strict Preservation)",
                            "description": "Diagram clearly distinguishing active Management policies (education, game farming, translocation, culling) from strict Conservation mandates (anti-poaching, hunting bans, park gazettement)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographical Distinction: Management vs Conservation",
                        "content": {
                            "title": "Geographical Distinction: Management vs Conservation",
                            "text": "• Wildlife Management: Active planning, scientific control, regulated utilization, and ecological manipulation of wildlife and its habitat (e.g., translocation, culling, game farming).\n\n• Wildlife Conservation: Strict legal preservation and protection of species and habitats from destruction, exploitation, or extinction (e.g., anti-poaching paramilitary patrols, absolute hunting bans)."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Wildlife Management Strategies in Action",
                        "content": {
                            "title": "Wildlife Management Strategies in Action",
                            "text": "1. Public Conservation Education: Disseminating conservation awareness via mass media (radio, TV) and establishing Wildlife Clubs in secondary schools.\n\n2. Regulatory Oversight (KWS): The Kenya Wildlife Service coordinates national wildlife policy, ranger deployments, and veterinary units.\n\n3. Game Ranching & Commercial Wildlife Farming: Licensed private farming of ostriches and crocodiles satisfies commercial market demand for meat and skins, reducing pressure on wild populations.\n\n4. Controlled Scientific Culling: Planned harvesting of overaged animals in overstocked parks to prevent habitat overgrazing and soil erosion.\n\n5. Promoting Domestic Tourism: Discounted park fees build national conservation pride and local stakeholder support."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Kenya Wildlife Service (KWS) Ranger Briefing and Conservation Patrols",
                        "content": {
                            "title": "Kenya Wildlife Service (KWS) Ranger Briefing and Conservation Patrols",
                            "caption": "Senior Kenya Wildlife Service (KWS) ranger conducting an operational briefing before high-security conservation and anti-poaching patrols.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Press_listen_to_KWS_Ranger_Simon_Gitau_on_Mount_Kenya_climbing_tips.jpg",
                            "author": "Ronald Robert, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Press_listen_to_KWS_Ranger_Simon_Gitau_on_Mount_Kenya_climbing_tips.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Paramilitary Anti-Poaching Operations",
                        "content": {
                            "title": "Paramilitary Anti-Poaching Operations",
                            "text": "KWS deploys specialized paramilitary rangers equipped with night-vision gear, GPS tracking, and armed air surveillance to neutralize illegal poaching rings and safeguard park frontiers."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Logistics of KWS Animal Translocation Process",
                        "content": {
                            "title": "Step-by-Step Logistics of KWS Animal Translocation Process",
                            "caption": "Five-Stage Engineering and Veterinary Protocol for Capturing, Transporting, and Reintroducing Elephants",
                            "description": "Visual step process showing 1. Overgrazing diagnosis; 2. Spatial mapping of receiving parks; 3. Helicopter darting and sedation; 4. Heavy hydraulic crating & road transport; 5. Release & GPS satellite collar monitoring."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "The KWS Animal Translocation Protocol",
                        "content": {
                            "title": "The KWS Animal Translocation Protocol",
                            "steps": [
                                {"step_number": 1, "title": "Overpopulation Assessment", "description": "Ecological surveys identify excessive herd density causing overgrazing and habitat degradation."},
                                {"step_number": 2, "title": "Recipient Habitat Selection", "description": "Underpopulated national parks with surplus browse and water are mapped and prepared."},
                                {"step_number": 3, "title": "Veterinary Immobilization", "description": "Helicopters guide targeted animals while veterinary officers administer dart sedation."},
                                {"step_number": 4, "title": "Hydraulic Crating & Transit", "description": "Sedated animals are loaded via hydraulic crane onto specialized transport trucks with veterinary monitoring."},
                                {"step_number": 5, "title": "Release & Satellite Tracking", "description": "Animals are revived in the new park and monitored via solar GPS collars to evaluate herd adaptation."}
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "concept_explanation",
                        "title": "Core Wildlife Conservation Mandates",
                        "content": {
                            "title": "Core Wildlife Conservation Mandates",
                            "text": "1. Absolute Ban on Sport Hunting: Passed in Kenya in 1977, eliminating commercial trophy hunting.\n\n2. Absolute Prohibition of Ivory & Trophy Trade: Implemented under the CITES convention, backed by historic presidential ivory burns in Nairobi National Park to destroy market value.\n\n3. Gazettement of Protected Ecosystems: Permanently reserving massive tracts of land under national law to preserve biodiversity corridors.\n\n4. Intensive Sanctuaries: Fortified enclosures dedicated to preventing the extinction of rhinos and impalas."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question: Wildlife Threat Mitigation",
                        "content": {
                            "question": "Explain three measures the government of Kenya has undertaken to reduce human-wildlife conflict around national parks. (6 Marks)",
                            "strategy": "Identify a specific intervention, explain the operational mechanism, and link it directly to conflict reduction.",
                            "solution": [
                                "1. Erection of Electric Perimeter Fences: Constructing solar-powered multi-strand electric fences around parks (such as Shimba Hills and Aberdares) physically blocks large herbivores like elephants from straying into neighbouring farms, preventing crop destruction. (2 Marks)",
                                "2. Establishment of Community Conservancies: Partnering with local pastoral landowners to share tourism revenue gives communities a financial stake in wildlife, reducing retaliatory killings of predators. (2 Marks)",
                                "3. Translocation of Problem Animals: Safely capturing rogue or overpopulated predators and elephants and transporting them to distant, unpopulated reserves eliminates localized threat to human life and livestock. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Wildlife Warden Simulation",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Wildlife Warden Simulation",
                            "prompt": "An isolated national park experiences an elephant population surge, causing severe tree debarking, deforestation, and soil erosion. As chief warden, what is your most sustainable long-term action?",
                            "options": [
                                "Option A: Authorize commercial trophy hunters to shoot 50% of the breeding elephant herd.",
                                "Option B: Organize an animal translocation program to move surplus elephants to an underpopulated savanna reserve.",
                                "Option C: Clear surrounding forests to allow the elephants to expand into private farmland."
                            ],
                            "correct_option": "Option B: Organize an animal translocation program to move surplus elephants to an underpopulated savanna reserve.",
                            "explanation": "Translocation safely relieves localized grazing pressure without destroying valuable breeding stock, adhering to modern conservation and management protocols."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Threats and Conservation",
                        "content": {
                            "question": "Why is animal translocation preferred over large-scale culling when managing localized elephant overpopulation in Kenya?",
                            "options": [
                                "Translocation generates higher meat revenue for local butcheries.",
                                "Translocation preserves the endangered genetic breeding stock while repopulating depleted ecosystems.",
                                "Translocation requires no specialized veterinary personnel.",
                                "Elephants cannot be sedated using tranquilizer darts."
                            ],
                            "correct_answer": 1,
                            "explanation": "Translocation preserves vital endangered genetic stock and replenishes underpopulated ecosystems without resorting to lethal herd reduction."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "summary",
                        "title": "Wildlife Management: Key Takeaways",
                        "content": {
                            "title": "Wildlife Management: Key Takeaways",
                            "summary_points": [
                                "Wildlife drives foreign exchange earnings, monetizes marginal ASAL lands, and creates extensive rural employment.",
                                "Threats include commercial poaching, human encroachment, sewage pollution (Lake Nakuru), drought, and bushfires.",
                                "Management involves active manipulation (education, game ranching, translocation, culling).",
                                "Conservation involves legal preservation (hunting bans, anti-poaching paramilitary units, CITES ivory trade bans).",
                                "KWS animal translocation moves surplus herds from overstocked to underpopulated ecosystems safely."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Tourism Concepts, Classifications, and Influencing Factors
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Tourism Concepts, Classifications, and Influencing Factors",
            "unit_description": "Foundational definitions, the five functional types of tourism, and physical/human factors promoting Kenyan tourism.",
            "lesson_title": "Tourism Concepts, Classifications, and Influencing Factors",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Tourism Foundations",
                        "content": {
                            "title": "Learning Objectives: Tourism Foundations",
                            "goals": [
                                "Define the geographical concept of tourism as an invisible export.",
                                "Classify tourism into its five functional categories (eco-tourism, domestic, mass, green, international).",
                                "Examine the five core operating principles of eco-tourism.",
                                "Analyze the physical and human factors making Kenya a premier global tourism destination."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Tourism as an Invisible Export",
                        "content": {
                            "title": "Tourism as an Invisible Export",
                            "text": "Tourism is defined as the temporary movement of people to destinations outside their normal home and work environment for leisure, recreation, business, or education. In national accounts, tourism is classified as an invisible export because it generates substantial foreign currency without transferring physical commodities across borders."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "The Five Functional Categories of Tourism",
                        "content": {
                            "term": "Functional Types of Tourism",
                            "definition": "Classification of tourism based on travel objectives, environmental impact, participant scale, and geographical boundaries.",
                            "key_points": [
                                "1. Eco-Tourism: Low-impact, environmentally responsible travel that conserves natural ecosystems and sustains local communities.",
                                "2. Domestic Tourism: Citizens traveling within their own country's national borders for leisure and education.",
                                "3. Mass Tourism: Large, organized groups of travelers visiting mainstream destinations simultaneously.",
                                "4. Green Tourism: Travel focused specifically on ecosystem rehabilitation, reforestation, and ecological restoration.",
                                "5. International Tourism: Cross-border travel involving entry into foreign countries for business or holiday."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Emergence of Eco-Tourism and Sustainable Travel",
                        "content": {
                            "title": "Emergence of Eco-Tourism and Sustainable Travel",
                            "text": "To counter the environmental damage caused by traditional mass tourism, the modern global industry has pivoted toward eco-tourism. Eco-tourism minimizes ecological footprints while channeling tourism profits directly into community conservancies."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The Five Pillars of Eco-Tourism Operation",
                        "content": {
                            "title": "The Five Pillars of Eco-Tourism Operation",
                            "caption": "Operational Principles of Sustainable Eco-Tourism: Minimal Impact, Community Benefit, and Ecological Integrity",
                            "description": "Diagram illustrating the 5 eco-tourism rules: designated walking trails, telescope animal observation, low-impact tented camps, vehicle limits, and strict zero-waste regulations."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Operational Rules of Eco-Tourism",
                        "content": {
                            "title": "Operational Rules of Eco-Tourism",
                            "text": "1. Designated Walking Trails: Tourists follow pre-marked footpaths guided by local naturalists, eliminating off-road vehicle soil compaction.\n\n2. Distant Observation: Wildlife is viewed through binoculars and long-range telephoto lenses to prevent behavioral disruption.\n\n3. Low-Impact Tented Camps: Lodging utilizes solar energy, composting toilets, and canvas structures instead of concrete towers.\n\n4. Strict Vehicle Controls: Limits are placed on vehicle engine sizes, numbers, and noise levels within conservancies.\n\n5. Anti-Littering Protocols: Strict zero-waste policies prevent plastic pollution and bushfires."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Domestic Tourism & Off-Peak Economic Resilience",
                        "content": {
                            "title": "Domestic Tourism & Off-Peak Economic Resilience",
                            "text": "Domestic tourism involves citizens exploring local attractions. It is vital for national economic stability:\n\n• Off-Peak Buffer: International tourist arrivals drop steeply in April–May and October–November due to European weather patterns. Domestic tourists sustain hotel occupancy, preventing mass staff layoffs.\n\n• National Integration: Promotes cultural understanding, patriotism, and broad-based appreciation of national heritage.\n\nGovernment Promotion Measures:\n• Heavily discounted park entry fees for Kenyan citizens.\n• Subsidized hotel rates and off-peak family safari packages."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Economic Value of Domestic Tourism",
                        "content": {
                            "type": "tip",
                            "title": "Economic Value of Domestic Tourism",
                            "text": "During global travel crises (such as geopolitical conflicts or pandemics), nations with robust domestic tourism sectors suffer significantly lower economic shocks than those solely dependent on foreign visitors."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physical Factors Attracting Tourists to Kenya",
                        "content": {
                            "title": "Physical Factors Attracting Tourists to Kenya",
                            "text": "Kenya possesses unmatched geographical attractions that drive global tourism:\n\n1. Tropical Climate (Year-Round Sunshine): Located on the Equator, Kenya enjoys warm, sun-drenched weather year-round. This acts as a powerful pull factor for Europeans escaping freezing sub-zero winters.\n\n2. Spectacular Topography & Scenery: The Great Rift Valley escarpments, snow-capped Mount Kenya, active geysers at Lake Bogoria, deep gorges at Hell's Gate, and pristine coastal coral beaches.\n\n3. World-Class Wildlife Diversity: Kenya conserves the iconic 'Big Five' (lion, leopard, elephant, rhino, buffalo) and hosts the world-famous annual wildebeest migration."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Push-Pull Dynamics of International Tourism to Tropical Kenya",
                        "content": {
                            "title": "Push-Pull Dynamics of International Tourism to Tropical Kenya",
                            "caption": "Geographical Push Factors (Freezing Northern Winters) vs Pull Factors (Equatorial Warmth & Savanna Megafauna)",
                            "description": "Thematic diagram showing Northern Hemisphere winter push factors (freezing snow, short daylight) contrasted with Kenyan equatorial pull factors (sunshine, beaches, safari lodges)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographical Push and Pull Interactions",
                        "content": {
                            "title": "Geographical Push and Pull Interactions",
                            "text": "International tourism flows follow clear climatic push-pull gradients. High disposable incomes and generous holiday leave in Western Europe and North America combine with harsh winter conditions to drive travelers toward equatorial destinations like Kenya."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Human and Cultural Factors Driving Tourism",
                        "content": {
                            "title": "Human and Cultural Factors Driving Tourism",
                            "text": "1. Rich Cultural Diversity: Over 40 distinct ethnic groups offering authentic traditional dances, music, colorful attire (e.g., Maasai and Samburu beadwork), and traditional homesteads.\n\n2. Historical & Prehistoric Monuments: World-renowned prehistoric sites (Kariandusi, Olorgesailie) with Stone Age handaxes, alongside ancient Swahili-Arab coastal settlements (Gedi Ruins, Fort Jesus, Vasco da Gama pillar).\n\n3. Political Stability: A stable democratic system assures international travelers of personal security.\n\n4. Modern Hospitality & Infrastructure: Luxury safari lodges, modern highways, international airports (JKIA, Moi), and the Standard Gauge Railway (SGR) ensuring swift connectivity."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Historical Fort Jesus Built in 1593 in Coastal Mombasa",
                        "content": {
                            "title": "Historical Fort Jesus Built in 1593 in Coastal Mombasa",
                            "caption": "The imposing coral-rag ramparts of Fort Jesus, constructed by the Portuguese in 1593 on Mombasa Island to command the Indian Ocean trade route.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Fort_Jesus%2C_Mombasa1.jpg",
                            "author": "Chris huh, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Fort_Jesus,_Mombasa1.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Fort Jesus as a UNESCO World Heritage Attraction",
                        "content": {
                            "title": "Fort Jesus as a UNESCO World Heritage Attraction",
                            "text": "Fort Jesus exemplifies Renaissance military architecture adapted to coastal coral limestone. It attracts hundreds of thousands of historical and cultural tourists annually, generating substantial foreign exchange and employment for Mombasa County."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Infrastructure, Security, and Hospitality Factors",
                        "content": {
                            "title": "Infrastructure, Security, and Hospitality Factors",
                            "text": "High-standard tourist infrastructure underpins visitor satisfaction:\n\n• Air Connectivity: Jomo Kenyatta International Airport (JKIA) connects directly to major European, Asian, and American capitals, while bush airstrips link directly to national park lodges.\n\n• Tourist Police Unit: Specialized security personnel deployed along coastal beaches and urban hubs to eliminate crime against visitors.\n\n• World-Class Hotel Training: The Kenya Utalii College provides standardized professional hospitality and culinary training recognized across Africa."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Tourism Type Identifier",
                        "content": {
                            "activity_type": "matching_challenge",
                            "title": "Interactive Tourism Type Identifier",
                            "prompt": "Match each tourist activity with its correct functional category:\n1. A group of university researchers staying in solar-powered canvas tents and walking on marked footpaths.\n2. A Nairobi family taking advantage of subsidized school-holiday rates at a lodge in Amboseli.\n3. A charter flight of 300 European holidaymakers arriving for a 2-week coastal package tour.",
                            "options": [
                                "Option A: 1-Eco-Tourism, 2-Domestic Tourism, 3-Mass/International Tourism",
                                "Option B: 1-Green Tourism, 2-Mass Tourism, 3-Eco-Tourism",
                                "Option C: 1-Domestic Tourism, 2-Eco-Tourism, 3-Green Tourism"
                            ],
                            "correct_option": "Option A: 1-Eco-Tourism, 2-Domestic Tourism, 3-Mass/International Tourism",
                            "explanation": "Low-impact walking and tented lodging represent Eco-Tourism. Citizen holiday travel represents Domestic Tourism. Large organized international charter groups represent Mass/International Tourism."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Tourism Concepts",
                        "content": {
                            "question": "Why is the promotion of domestic tourism strategically vital for hotel operators in Kenya?",
                            "options": [
                                "Domestic tourists pay in foreign currency rather than local shillings.",
                                "Domestic tourists sustain hotel occupancy and employment during off-peak international arrival seasons (April/October).",
                                "Domestic tourists require no transport infrastructure to reach destinations.",
                                "Domestic tourists only travel to marine parks."
                            ],
                            "correct_answer": 1,
                            "explanation": "Domestic tourism cushions the hospitality sector against severe seasonal drops in international visitors, preventing business closures and worker layoffs."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Tourism Concepts: Key Takeaways",
                        "content": {
                            "title": "Tourism Concepts: Key Takeaways",
                            "summary_points": [
                                "Tourism is an invisible export that generates foreign exchange without physical commodity loss.",
                                "Categories include Eco-Tourism, Domestic, Mass, Green, and International Tourism.",
                                "Eco-Tourism relies on 5 pillars: marked walking trails, telescope viewing, low-impact camps, vehicle limits, and zero litter.",
                                "Domestic tourism buffers hotels during international off-peak seasons (April & October).",
                                "Kenya's premier status is driven by equatorial sunshine, Big Five wildlife, Rift Valley landscapes, and 40+ cultural traditions."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Spatial Distribution of Kenya's Coastal and Inland Attractions
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Spatial Distribution of Kenya's Coastal and Inland Attractions",
            "unit_description": "Geographical zonation of Kenya's premier attractions into the Coastal Strip and Inland Region, economic benefits, and socio-cultural side effects.",
            "lesson_title": "Spatial Distribution of Kenya's Coastal and Inland Attractions",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Spatial Tourist Hubs",
                        "content": {
                            "title": "Learning Objectives: Spatial Tourist Hubs",
                            "goals": [
                                "Analyze the spatial division of Kenya's tourist attractions into Coastal and Inland circuits.",
                                "Examine the major physical, historical, and cultural attractions of the Coastal Strip.",
                                "Evaluate inland attractions including Rift Valley lakes, glaciated mountains, and the Maasai Mara migration.",
                                "Assess the economic multiplier effects and negative socio-cultural side effects of tourism."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spatial Geography of Kenyan Tourism",
                        "content": {
                            "title": "Spatial Geography of Kenyan Tourism",
                            "text": "Kenya's tourist attractions are spatially grouped into two primary geographic circuits: the Coastal Strip (marine, heritage, and sun-sea-sand tourism) and the Inland Region (savanna megafauna, Rift Valley geology, and prehistoric heritage)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Thematic Map of Kenya: Spatial Distribution of Coastal vs Inland Tourist Hubs",
                        "content": {
                            "title": "Thematic Map of Kenya: Spatial Distribution of Coastal vs Inland Tourist Hubs",
                            "caption": "Thematic Distribution Map of Kenya's Premier Coastal Strip and Inland Tourism Circuits",
                            "description": "Spatial map plotting Coastal Hubs (Mombasa, Malindi, Fort Jesus, Gedi Ruins, Shimoni Caves, Kaya Shrines) and Inland Hubs (Maasai Mara, Amboseli, Tsavo, Mt. Kenya, Lake Nakuru, Lake Bogoria, Kariandusi)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Dual Circuit Spatial Connectivity",
                        "content": {
                            "title": "Dual Circuit Spatial Connectivity",
                            "text": "The Coastal and Inland circuits are seamlessly linked by the Nairobi–Mombasa Highway, the Standard Gauge Railway (SGR Madaraka Express), and scheduled domestic flight networks connecting coastal beach resorts with inland safari parks in under one hour."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Coastal Strip: Physical and Cultural Attractions",
                        "content": {
                            "title": "The Coastal Strip: Physical and Cultural Attractions",
                            "text": "1. Pristine Sandy Beaches: White, gently sloping coral sand beaches (Diani, Nyali, Watamu) ideal for sunbathing and swimming.\n\n2. Warm Tropical Marine Waters: Year-round high water temperatures supporting vibrant coral reefs and marine life.\n\n3. Water Recreation: High-thrill water sports including scuba diving, snorkeling in marine parks (Malindi, Kisite-Mpunguti), deep-sea game fishing, and windsurfing.\n\n4. Historical Stone Monuments: Ancient Portuguese and Arab architecture including Fort Jesus (1593), Gedi Ruins, Vasco da Gama Pillar, and Shimoni Slave Caves.\n\n5. Sacred Kaya Forests: Coastal lowland indigenous forests declared UNESCO World Heritage cultural shrines of the Mijikenda people.\n\n6. Mangrove Swamp Estuaries: Salt-tolerant mangrove forests teeming with birdlife and marine crustaceans."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Transect of the Kenyan Coastal Strip: Coral Reefs, Beaches, Mangroves, and Kayas",
                        "content": {
                            "title": "Transect of the Kenyan Coastal Strip: Coral Reefs, Beaches, Mangroves, and Kayas",
                            "caption": "Ecological Transect Profile Across the Kenyan Coastline from Offshore Barrier Reef to Inland Sacred Kaya Shrines",
                            "description": "Cross-sectional profile showing offshore coral reef barrier, shallow turquoise lagoon, white sandy beach, tidal mangrove creek, and inland sacred Kaya forest."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Coastal Marine Ecosystem Transect",
                        "content": {
                            "title": "Coastal Marine Ecosystem Transect",
                            "text": "The offshore fringing coral reef acts as a natural breakwater, dissipating powerful Indian Ocean waves to create calm, safe, turquoise lagoons ideal for swimming, glass-bottom boat excursions, and snorkeling."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Inland Circuit: Savanna Parks, Lakes, and Mountains",
                        "content": {
                            "title": "The Inland Circuit: Savanna Parks, Lakes, and Mountains",
                            "text": "1. Savanna Megafauna Reserves: World-famous national parks including Tsavo (famous for red elephants and Mzima Springs), Amboseli (elephant herds against Mt. Kilimanjaro), and Samburu (rare ASAL species).\n\n2. The Great Wildebeest Migration (Maasai Mara): Annual spectacle where over 1.5 million wildebeests, zebras, and gazelles brave crocodile-infested Mara River crossings from the Serengeti.\n\n3. Great Rift Valley Lakes & Geysers: Lake Nakuru (rhino sanctuary and birdlife), Lake Bogoria (steaming geysers and mineral thermal spas), and Lake Naivasha (freshwater boating and birding).\n\n4. Montane Glacial Landscapes: Snow-capped volcanic peaks, tarns, and hanging valleys of Mount Kenya (5,199 m) and the Aberdare Range."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_image",
                        "title": "The Great Wildebeest Migration in Maasai Mara Game Reserve",
                        "content": {
                            "title": "The Great Wildebeest Migration in Maasai Mara Game Reserve",
                            "caption": "Massive herds of wildebeest and zebras crossing the Mara River during the annual Great Migration in the Maasai Mara Game Reserve.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Maasai_Mara_Wildebeest_Migrations.jpg",
                            "author": "Kidoleeee, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Mara_Wildebeest_Migrations.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Eighth Wonder of the World: Mara Migration",
                        "content": {
                            "title": "The Eighth Wonder of the World: Mara Migration",
                            "text": "The annual July–October wildebeest migration draws tens of thousands of international safari travelers, creating maximum peak-season hotel occupancy and yielding substantial foreign currency earnings for Kenya."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Inland Prehistoric and Cultural Heritage Sites",
                        "content": {
                            "title": "Inland Prehistoric and Cultural Heritage Sites",
                            "text": "• Prehistoric Stone Age Sites: Kariandusi (near Gilgil) and Olorgesailie (near Magadi), showcasing Acheulean handaxe excavation trenches and fossil beds of early hominids.\n\n• Nairobi National Museum & Bomas of Kenya: Central national repository for scientific discoveries, complemented by traditional cultural architecture and daily folk dance performances.\n\n• Maasai & Samburu Pastoral Culture: Traditional bomas, beadwork, and ceremonial lifestyles that offer immersive cultural experiences."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Value of Prehistoric Archaeology",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Value of Prehistoric Archaeology",
                            "text": "Kenya's Rift Valley is globally celebrated as the 'Cradle of Humankind'. Prehistoric sites like Olorgesailie provide unique educational tourism revenue that diversifies the sector beyond wildlife safaris."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Economic Multiplier Effect of Tourism in Kenya",
                        "content": {
                            "title": "Economic Multiplier Effect of Tourism in Kenya",
                            "caption": "Macroeconomic Flowchart: Foreign Exchange Inflows Stimulating Agriculture, Cottage Crafts, Infrastructure, and Public Tax Revenues",
                            "description": "Flowchart illustrating how tourist expenditure cascades from airlines and luxury lodges into local farming produce, Jua Kali handicrafts (Ciondos, soapstone), infrastructure, and national treasury taxes."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Tourism Multiplier Effect",
                        "content": {
                            "title": "The Tourism Multiplier Effect",
                            "text": "Tourism generates powerful backward and forward linkages across the Kenyan economy:\n\n• Direct Revenue: Park entrance fees, hotel VAT, aviation landing taxes, and operator licenses.\n• Agricultural Demand: Safari lodges purchase thousands of tonnes of fresh vegetables, fruits, dairy, and beef directly from local smallholder farmers.\n• Cottage Industry Stimulus: Artisans earn direct income selling hand-woven sisal baskets (Ciondos), Kisii soapstone carvings, and Maasai beadwork."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Infrastructural Growth and Rural Modernization",
                        "content": {
                            "title": "Infrastructural Growth and Rural Modernization",
                            "text": "To connect isolated national parks and coastal resorts, the government paves all-weather tarmac highways, extends the national power grid, drills boreholes, and builds telecommunication masts. These infrastructure upgrades permanently open up remote rural districts to commercial trade and modern services."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "concept_explanation",
                        "title": "Negative Socio-Cultural and Environmental Side Effects",
                        "content": {
                            "title": "Negative Socio-Cultural and Environmental Side Effects",
                            "text": "If unregulated, tourism generates serious socio-cultural and ecological costs:\n\n1. Socio-Cultural Erosion: Exposure to foreign lifestyles can lead local youth to adopt negative behaviors (substance abuse, commercial sex exploitation, and breakdown of traditional norms).\n\n2. School Dropouts: Coastal youths frequently abandon formal schooling to work as informal 'beach boys' or uncertified tour guides seeking quick tourist tips.\n\n3. Sectoral Neglect: Public funds are sometimes disproportionately diverted to luxurious tourist roads and airstrips while neglecting vital agricultural feeder roads, hospitals, and rural schools.\n\n4. Environmental Degradation: Littering, coral reef trampling by reckless divers, and wildlife harassment from off-road safari driving."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Mitigation: Code of Tourist Conduct",
                        "content": {
                            "type": "warning",
                            "title": "Mitigation: Code of Tourist Conduct",
                            "text": "The Ministry of Tourism enforces strict codes of conduct for tour operators, penalizes off-road driving in parks, and conducts community child protection workshops along coastal resort beaches."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question: Spatial Tourist Distributions",
                        "content": {
                            "question": "State four physical attractions found along the Kenyan Coastal Strip that draw international tourists. (4 Marks)",
                            "strategy": "Ensure you specify physical (natural) features rather than human/historical monuments like Fort Jesus.",
                            "solution": [
                                "1. Warm, sunny tropical coastal climate throughout the year. (1 Mark)",
                                "2. Clean, white sandy beaches suitable for sunbathing. (1 Mark)",
                                "3. Warm Indian Ocean waters supporting water sports (surfing, deep-sea fishing). (1 Mark)",
                                "4. Vibrant offshore coral reefs with rich marine ecosystems. (1 Mark)"
                            ]
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Kenya Itinerary Planner",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Kenya Itinerary Planner",
                            "prompt": "An international tour agency wants to design a 7-day 'Heritage and Wildlife' safari combining coastal historical monuments with inland volcanic landscapes. Which itinerary correctly fits this brief?",
                            "options": [
                                "Option A: Fort Jesus & Gedi Ruins (Coast) followed by Lake Bogoria Geysers & Maasai Mara (Inland).",
                                "Option B: Mount Kenya snow climbing followed immediately by tea picking in Kericho.",
                                "Option C: Kisumu Impala Sanctuary followed by Lake Victoria fish market tours only."
                            ],
                            "correct_option": "Option A: Fort Jesus & Gedi Ruins (Coast) followed by Lake Bogoria Geysers & Maasai Mara (Inland).",
                            "explanation": "Option A perfectly integrates coastal historical architecture (Fort Jesus/Gedi) with the inland Rift Valley volcanic geysers (Lake Bogoria) and premier savanna wildlife (Maasai Mara)."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Kenyan Tourist Attractions",
                        "content": {
                            "question": "Which of the following is a socio-cultural hazard directly associated with unregulated coastal tourism in Kenya?",
                            "options": [
                                "Depletion of alpine bamboo forests.",
                                "School dropout rates among coastal youth seeking informal employment as beach boys.",
                                "Excessive volcanic lava flows into marine lagoons.",
                                "Loss of snow cover on Mount Kenya."
                            ],
                            "correct_answer": 1,
                            "explanation": "Coastal tourism can induce school dropouts as youth leave formal education to pursue quick cash tips as informal beach guides."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "summary",
                        "title": "Kenyan Attractions: Key Takeaways",
                        "content": {
                            "title": "Kenyan Attractions: Key Takeaways",
                            "summary_points": [
                                "Kenyan tourism is divided into the Coastal Strip circuit and the Inland Wildlife/Rift Valley circuit.",
                                "Coastal attractions include white sand beaches, coral reefs, Fort Jesus (1593), Gedi Ruins, and sacred Kaya forests.",
                                "Inland attractions feature the Maasai Mara migration, the Big Five, Rift Valley geysers (Lake Bogoria), and Kariandusi prehistoric sites.",
                                "The tourism multiplier stimulates agricultural supply chains, Jua Kali crafts (Ciondos, soapstone), and rural infrastructure.",
                                "Negative impacts include socio-cultural erosion, youth school dropouts, and environmental degradation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Comparative Analysis (Kenya vs Switzerland) and Strategic Expansion
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Comparative Analysis (Kenya vs Switzerland) and Strategic Expansion",
            "unit_description": "Comparative case study between Kenya and Switzerland, analysis of domestic tourism barriers, and Kenya's strategic expansion plan.",
            "lesson_title": "Comparative Analysis (Kenya vs Switzerland) and Strategic Expansion",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Comparative Tourism Systems",
                        "content": {
                            "title": "Learning Objectives: Comparative Tourism Systems",
                            "goals": [
                                "Examine the physical, infrastructural, and institutional factors driving Swiss tourism dominance.",
                                "Conduct a rigorous comparative evaluation of tourism in Kenya and Switzerland (similarities and differences).",
                                "Analyze the socio-economic barriers hindering domestic tourism growth in Kenya.",
                                "Outline Kenya's six-point strategic action plan for sustainable tourism expansion."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Introduction to Comparative Tourism Geographies",
                        "content": {
                            "title": "Introduction to Comparative Tourism Geographies",
                            "text": "To evaluate Kenya's competitive position in the global tourism economy, geography contrasts it with Switzerland—a landlocked, highly industrialized Central European alpine nation where tourism has operated as an advanced economic science for over two centuries."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Switzerland: Physical and Climatic Pull Factors",
                        "content": {
                            "title": "Switzerland: Physical and Climatic Pull Factors",
                            "text": "1. Spectacular Alpine Topography: Over 60% of Switzerland is covered by the Alps, featuring dramatic glaciated landforms—pyramidal peaks (the Matterhorn), U-shaped glacial valleys, hanging troughs, waterfalls, and pristine blue lakes (Lake Geneva, Lake Lucerne).\n\n2. Dual-Season Climate Appeal:\n• Summer: Warm, sunny weather ideal for alpine mountaineering, hiking, and lake cruising, especially in the southern Mediterranean-influenced canton of Ticino.\n• Winter: Heavy snowfall transforms alpine slopes into the world's premier destinations for skiing, snowboarding, ice-skating, and bobsledding.\n\n3. Natural Thermal Spas: Mineral-rich hot springs (St. Moritz, Baden) famous for curative health retreats."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Physical and Technological Infrastructure of Swiss Alpine Tourism",
                        "content": {
                            "title": "Physical and Technological Infrastructure of Swiss Alpine Tourism",
                            "caption": "Integrated High-Altitude Transit Engineering: Electrified Cog Railways, Aerial Cable Cars, and Dual-Season Alpine Resorts",
                            "description": "Isometric cross-section showing glaciated Alpine peaks, hanging valleys, electric cog rail lines, high-capacity cable cars, winter ski slopes, and lakeside thermal spas."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Swiss Alpine Transit Engineering",
                        "content": {
                            "title": "Swiss Alpine Transit Engineering",
                            "text": "Switzerland has mastered mountain accessibility. Electrified cogwheel railways, funiculars, and aerial cable cars ascend vertical mountain precipices directly to summit hotels and ski fields, ensuring year-round access regardless of extreme weather."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Switzerland: Human, Institutional, and Financial Factors",
                        "content": {
                            "title": "Switzerland: Human, Institutional, and Financial Factors",
                            "text": "1. Strategic Central European Location: Located at the heart of Western Europe, bordered by wealthy, densely populated nations (Germany, France, Italy), ensuring short travel times and massive visitor inflows.\n\n2. Traditional Policy of Political Neutrality: Historic neutrality guarantees peaceful international relations, making all global nationalities feel safe.\n\n3. Multilingual Society: Swiss citizens speak German, French, Italian, and Romansh, ensuring seamless multilingual hospitality.\n\n4. Global Diplomatic & Financial Hub: Geneva hosts the UN, WTO, and Red Cross, generating massive high-spending business and conference tourism, while Swiss banking privacy laws attract global financial elites.\n\n5. High Domestic Purchasing Power: Swiss citizens enjoy high disposable incomes, sustaining a powerful domestic holiday market."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Modern Electrified Cable Car Transit Ascending the Swiss Alps with Matterhorn View",
                        "content": {
                            "title": "Modern Electrified Cable Car Transit Ascending the Swiss Alps with Matterhorn View",
                            "caption": "An aerial cable car transporting international tourists and skiers toward high alpine peaks in Zermatt against the backdrop of the iconic Matterhorn.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Cable_car_and_Matterhorn.jpg",
                            "author": "Tiia Monto, Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Cable_car_and_Matterhorn.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Technological Efficiency in Swiss Tourism",
                        "content": {
                            "title": "Technological Efficiency in Swiss Tourism",
                            "text": "High-altitude cable car systems in Zermatt operate continuously in freezing conditions, transporting thousands of skiers per hour to high glaciated trails over 3,800 meters above sea level."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Matrix: Kenya Tropical Savanna vs Switzerland Alpine Ecosystems",
                        "content": {
                            "title": "Comparative Matrix: Kenya Tropical Savanna vs Switzerland Alpine Ecosystems",
                            "caption": "Side-by-Side Thematic Comparison of Physical Environments, Infrastructure, Wildlife Management, and Domestic Travel",
                            "description": "Comparative matrix diagram contrasting Kenya (coastal marine, tropical savanna, open game parks, low domestic tourism) with Switzerland (landlocked, alpine snow, cog railways, high domestic travel)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comprehensive Comparative Matrix: Kenya vs Switzerland",
                        "content": {
                            "headers": ["Feature", "Kenya", "Switzerland"],
                            "rows": [
                                ["Location & Marine Access", "Coastal nation with expansive Indian Ocean beaches and coral reefs", "Entirely landlocked in Central Europe; lacks marine coastlines"],
                                ["Climate Dynamics", "Warm, sunny tropical equatorial climate throughout all seasons", "Marked seasonal variation: warm summers and freezing, snowy winters"],
                                ["Winter Sports", "Lacks snow cover; no winter sports infrastructure", "World-renowned hub for skiing, ice-skating, and winter sports"],
                                ["Wildlife Profile", "Rich in free-ranging tropical savanna megafauna (Big Five)", "Lacks tropical wildlife; native alpine fauna is sparse"],
                                ["Wildlife Enclosures", "Wildlife preserved in vast open National Parks and Reserves", "Animals primarily exhibited in controlled urban Zoos"],
                                ["Transport Network", "Roads, SGR, domestic flights; limited alpine rail integration", "Dense electrified rail, cogwheel trains, and summit cable cars"],
                                ["Domestic Tourism", "Underdeveloped due to low incomes and high seasonal hotel tariffs", "Highly developed; citizens have high savings and travel culture"],
                                ["Revenue & Volume", "Lower total visitor volume; highly vulnerable to international shocks", "Massive annual visitor volume; exceptionally high revenue per capita"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rigorous Analysis of Similarities",
                        "content": {
                            "title": "Rigorous Analysis of Similarities",
                            "text": "Despite structural contrasts, Kenya and Switzerland share vital geographic parallels:\n\n1. Spectacular Scenery: Both feature dramatic physical landscapes (snow-capped mountains, deep rift/glacial valleys, waterfalls, scenic lakes).\n\n2. Foreign Exchange Generation: Tourism is a premier pillar of national revenue and international trade balances for both economies.\n\n3. High-Quality Hospitality: Both have well-established hotel networks offering world-class service.\n\n4. Natural Healing Spas: Both utilize mineral thermal springs for therapeutic tourism (St. Moritz in Switzerland and Lake Bogoria in Kenya).\n\n5. Peaceful Political Climate: Both maintain stable political systems guaranteeing traveler safety.\n\n6. Dedicated Nature Reserves: Both establish formally protected conservation parks (Swiss National Park in Engadine vs Amboseli/Tsavo in Kenya)."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rigorous Analysis of Differences",
                        "content": {
                            "title": "Rigorous Analysis of Differences",
                            "text": "The fundamental differences stem from geography, economic development, and technological capital:\n\n• Marine vs Continental: Kenya exploits warm Indian Ocean coral beaches, while landlocked Switzerland capitalizes on alpine snow slopes.\n\n• Wildlife Handling: Kenya relies on free-ranging wildlife across thousands of square kilometers of unfenced savanna, whereas Switzerland preserves animals in specialized urban zoos.\n\n• Transit Capital: Switzerland deploys multi-billion-dollar electrified cog rail lines climbing vertical mountains, whereas Kenya relies primarily on highways and safari vans.\n\n• Domestic Travel Capacity: Swiss citizens possess the high personal savings required for regular domestic holidays, while most Kenyan families prioritize basic survival needs."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Socioeconomic Barriers to Domestic Tourism in Kenya",
                        "content": {
                            "title": "Socioeconomic Barriers to Domestic Tourism in Kenya",
                            "text": "Five primary factors explain why domestic tourism remains underdeveloped in Kenya:\n\n1. Low Disposable Incomes: The majority of citizens earn modest wages that must cover essential food, housing, healthcare, and school fees, leaving zero surplus for luxury holidays.\n\n2. High Seasonal Accommodation Costs: During peak tourist seasons, hotel room rates escalate beyond the financial reach of local families.\n\n3. High Unemployment Levels: Joblessness deprives youth and families of travel purchasing power.\n\n4. Workplace Leave Constraints: Many private and informal sector employees cannot obtain paid leave for extended leisure travel.\n\n5. Absence of a Leisure Travel Culture: Many families traditionally dedicate holiday periods to visiting rural ancestral homes rather than touring national parks."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Cultural Shift in Domestic Leisure",
                        "content": {
                            "type": "tip",
                            "title": "Cultural Shift in Domestic Leisure",
                            "text": "With the expansion of Kenya's urban middle class, domestic weekend excursions to Naivasha, Nakuru, and Mombasa are steadily rising, spurred by mobile payment savings platforms and discounted group van tours."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Six-Point Strategic Action Plan for Kenyan Tourism Sector Expansion",
                        "content": {
                            "title": "Six-Point Strategic Action Plan for Kenyan Tourism Sector Expansion",
                            "caption": "Comprehensive Hexagonal Strategic Policy Framework for Expanding Kenya's Tourism Industry",
                            "description": "Diagram detailing Kenya's 6 strategic expansion pillars: ASAL transport upgrades, KTB global marketing, domestic off-peak subsidies, enhanced security patrols, F&B tax cuts, and tourism product diversification."
                        }
                    },
                    {
                        "type": "step_process",
                        "title": "Kenya's Strategic Tourism Expansion Framework",
                        "content": {
                            "title": "Kenya's Strategic Tourism Expansion Framework",
                            "steps": [
                                {"step_number": 1, "title": "ASAL Infrastructure Upgrades", "description": "Tarmacking highways and constructing airstrips in remote northern regions to unlock new tourism circuits."},
                                {"step_number": 2, "title": "Aggressive Global Marketing", "description": "Funding the Kenya Tourism Board (KTB) to execute targeted digital campaigns in emerging markets across Asia and Eastern Europe."},
                                {"step_number": 3, "title": "Domestic Off-Peak Subsidies", "description": "Partnering with hoteliers to offer highly discounted accommodation and park fee packages for local families."},
                                {"step_number": 4, "title": "Strengthening National Security", "description": "Deploying the Tourist Police Unit and modern intelligence surveillance to guarantee visitor safety."},
                                {"step_number": 5, "title": "Lowering Tariffs and Taxes", "description": "Reducing hotel VAT, park fees, and landing charges to make Kenyan vacation packages cost-competitive globally."},
                                {"step_number": 6, "title": "Tourism Product Diversification", "description": "Expanding cultural, sports, conference (MICE), and agro-tourism to reduce exclusive dependence on wildlife safaris."}
                            ]
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Exam Pitfalls in Comparative Geography",
                        "content": {
                            "mistake": "Stating that Switzerland has marine beaches or that Kenya has winter skiing resorts.",
                            "correction": "Switzerland is completely landlocked (no marine coast); Kenya has a warm equatorial climate with no winter snowfall or skiing.",
                            "reasoning": "In KCSE comparative questions, students must explicitly pair matching attributes (e.g., 'While Kenya possesses extensive coastal beaches, Switzerland is landlocked with no marine attractions')."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Practice Exam: Structured Questions & Model Answers",
                        "content": {
                            "question": "Explain three factors that make Switzerland's tourism industry earn more revenue than Kenya's. (6 Marks)",
                            "strategy": "State the factor clearly, explain the operational mechanism in Switzerland, and contrast it with Kenya.",
                            "solution": [
                                "1. Advanced Integrated Infrastructure: Switzerland possesses an extensive network of electrified railways, cog trains, and cable cars that carry tourists directly to high mountain summits easily, whereas Kenya relies on roads that are sometimes impassable during rains. (2 Marks)",
                                "2. Strategic Central European Location: Switzerland is situated at the heart of Europe, surrounded by wealthy, densely populated nations with short travel times, resulting in higher annual visitor volumes than Kenya. (2 Marks)",
                                "3. Dual-Season Appeal: Switzerland offers warm summer hiking and cold winter sports (skiing/snowboarding), generating high tourist revenue throughout all twelve months, whereas Kenya experiences off-peak slumps in April and October. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Comparative Reasoning Challenge",
                        "content": {
                            "activity_type": "matching_challenge",
                            "title": "Interactive Comparative Reasoning Challenge",
                            "prompt": "Classify each feature as belonging to Kenya, Switzerland, or Both:\n1. Features world-class snow-skiing slopes and electrified cogwheel summit railways.\n2. Preserves large, free-ranging savanna megafauna in spacious national parks.\n3. Operates healing thermal mineral spas (St. Moritz and Lake Bogoria).",
                            "options": [
                                "Option A: 1-Switzerland, 2-Kenya, 3-Both",
                                "Option B: 1-Both, 2-Switzerland, 3-Kenya",
                                "Option C: 1-Kenya, 2-Both, 3-Switzerland"
                            ],
                            "correct_option": "Option A: 1-Switzerland, 2-Kenya, 3-Both",
                            "explanation": "Winter skiing belongs to Switzerland. Savanna wildlife belongs to Kenya. Natural healing thermal spas exist in both countries (St. Moritz and Lake Bogoria)."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 1: Kenya vs Switzerland",
                        "content": {
                            "question": "Which of the following physical characteristics is found in both Kenya and Switzerland?",
                            "options": [
                                "Expansive marine coral barrier reefs.",
                                "Dramatic mountain scenery and scenic lakes.",
                                "Sub-zero winter blizzards suitable for bobsledding.",
                                "Vast dry acacia savanna scrublands."
                            ],
                            "correct_answer": 1,
                            "explanation": "Both Kenya (Mt. Kenya, Rift Valley lakes) and Switzerland (Alps, Lake Geneva) feature spectacular mountain landscapes, waterfalls, and scenic lakes."
                        }
                    }
                ],
                # Page 15
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 2: Domestic Expansion",
                        "content": {
                            "question": "Which strategy is most effective in eliminating the off-peak slump in Kenya's hotel occupancy during April and October?",
                            "options": [
                                "Closing all game parks until the European winter resumes.",
                                "Offering subsidized, highly discounted accommodation packages to local citizens and domestic families.",
                                "Banning domestic tour vans from national parks.",
                                "Tripling park entry fees for local tourists."
                            ],
                            "correct_answer": 1,
                            "explanation": "Offering subsidized off-peak rates attracts domestic holidaymakers, maintaining hotel occupancy and preserving staff jobs when international arrivals decline."
                        }
                    }
                ],
                # Page 16
                [
                    {
                        "type": "summary",
                        "title": "Topic 3 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 3 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Wildlife distribution is governed by rainfall, aspect, soil fertility, vegetation biomes, water, and human management.",
                                "Protected areas are categorized into National Parks (Government/Single-Use), Game Reserves (Local Council/Multi-Use), and Sanctuaries (Endangered Species).",
                                "Wildlife management (education, game farming, translocation, culling) balances human-ecological needs; conservation enforces legal protection.",
                                "Tourism is an invisible export categorized into Eco-Tourism, Domestic, Mass, Green, and International.",
                                "Kenya's attractions divide into the Coastal Strip (beaches, corals, Fort Jesus) and Inland Region (savanna wildlife, Rift Valley, Mt. Kenya).",
                                "Switzerland outperforms Kenya due to integrated alpine cog rails/cable cars, central European location, dual-season winter sports, and strong domestic travel.",
                                "Kenya's expansion plan focuses on ASAL roads, KTB marketing, domestic subsidies, security, and product diversification."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic3(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 3: Wildlife and Tourism")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        print("[!] Error: Curriculum '844' not found.")
        return

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    if not grade:
        print("[!] Error: Grade 'Form 4' not found.")
        return

    subject = Subject.objects.filter(grade=grade, name="Geography").first()
    if not subject:
        print("[!] Error: Subject 'Geography' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Wildlife and Tourism"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=3,
            description="Comprehensive syllabus on wildlife ecosystems, protected area classification, threats and conservation, tourism geography, and comparative case studies (Kenya vs Switzerland)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic3_curriculum()
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
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

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
    print("[SUCCESS] Form 4 Geography Topic 3 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_geography_topic3(replace=replace_flag)
