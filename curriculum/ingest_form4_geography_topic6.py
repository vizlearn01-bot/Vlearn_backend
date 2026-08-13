"""
VLearn Form 4 Geography — Topic 6: Transport and Communication
High-Structure Production Ingestion Engine

Topic: Transport and Communication (Topic Order: 6)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (80 Total Pages):
  1. Foundations of Transport & Communication and Traditional Land Transport (12 Pages)
  2. Modern Land Transport: Road and Railway Networks in Africa (12 Pages)
  3. Water, Pipeline, and Air Transport & Containerisation (14 Pages)
  4. Major Inland Waterway Case Study: The St. Lawrence Seaway Project (12 Pages)
  5. Telecommunication Systems & Economic Development (14 Pages)
  6. Transport Barriers in Africa, Worked KCSE Essays, and Topic Assessment (16 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic6.py [--replace]
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
    """Removes bracket citations [63], [67], [74] and cleans double spaces."""
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

def build_topic6_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 6."""
    return [
        # =====================================================================
        # LESSON 1: Foundations of Transport & Communication and Traditional Land Transport
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Foundations of Transport & Communication and Traditional Land Transport",
            "unit_description": "Geographical definitions, governing network factors (surplus/deficit, infrastructure, politics), traditional human porterage, and draught animal transport.",
            "lesson_title": "Foundations of Transport & Communication and Traditional Land Transport",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Foundations & Traditional Transport",
                        "content": {
                            "title": "Learning Objectives: Foundations & Traditional Transport",
                            "goals": [
                                "Define the geographical terms 'transport' and 'communication'.",
                                "Explain four core factors dictating network density and layout (surplus/deficit, alternative sources, infrastructure, political decisions).",
                                "Analyze traditional land transport modes including human porterage and draught animals.",
                                "Evaluate animal adaptations across biomes (oxen, horses, donkeys, camels, elephants) and assess traditional transport pros and cons."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Topic 6: Transport and Communication",
                        "content": {
                            "title": "Welcome to Topic 6: Transport and Communication",
                            "text": "Transport and communication act as the circulatory system of modern economies. Transport facilitates the physical movement of people, raw materials, and manufactured goods across space, while communication enables the rapid exchange of information, ideas, and financial capital."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Geographical Definitions: Transport vs Communication",
                        "content": {
                            "term": "Transport vs Communication",
                            "definition": "Transport is the act of moving physical items (cargo, raw materials, finished products) and people from one geographical location to another. Communication is the process of transferring information, data, and signals between individuals, groups, and places.",
                            "key_points": [
                                "Transport moves physical mass across geographical distance.",
                                "Communication moves intellectual data, voices, and digital signals across spatial channels.",
                                "Together, they bridge spatial friction between supply nodes and demand markets."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Bridging Spatial Friction",
                        "content": {
                            "title": "Bridging Spatial Friction",
                            "text": "Distance creates friction that restricts human interaction and trade. Efficient transport and communication networks reduce transit times and transport costs, effectively compressing geographical space."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Surplus-Deficit Economic Gradient & Transport Flow Model",
                        "content": {
                            "title": "Surplus-Deficit Economic Gradient & Transport Flow Model",
                            "caption": "Spatial Interaction Model Displaying How Commodity Surpluses Flow Along Transport Corridors to Regional Deficit Markets",
                            "description": "Flowchart displaying Region A (Agricultural Surplus) connecting via Transport Corridor (Infrastructure Node) to Region B (Urban Market Deficit)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Four Governing Factors of Network Layout",
                        "content": {
                            "title": "Four Governing Factors of Network Layout",
                            "text": "The density and layout of transport networks are dictated by four spatial variables:\n\n1. Surplus and Deficit (Supply and Demand): Movement only occurs along economic gradients connecting commodity surplus regions with commodity deficit markets.\n\n2. Alternative Sources: The presence of a closer alternative supplier hinders the establishment of long-distance transport routes to distant producers.\n\n3. Infrastructure Quality: High-quality nodes (ports, terminals, depots) and links (highways, rail lines) reduce transit friction and costs.\n\n4. Political Decisions: Government policies direct state investment into regional transport corridors or restrict cross-border routes for security."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "State Infrastructure Provision vs Political Barriers",
                        "content": {
                            "title": "State Infrastructure Provision vs Political Barriers",
                            "text": "Governments frequently construct loss-making rural roads to integrate remote farming communities into national markets. Conversely, political hostility between neighboring states can lead to closed borders and severed transport links."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Principle: Complementarity & Intervening Opportunity",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Principle: Complementarity & Intervening Opportunity",
                            "text": "Transport flows require spatial complementarity between a supplier and a buyer. An intervening opportunity (a closer supplier) cancels long-distance transport demand."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Camel Caravan in Desert Terrains",
                        "content": {
                            "title": "Traditional Camel Caravan in Desert Terrains",
                            "caption": "Camel caravan traversing sand dunes in the Sahara Desert, demonstrating traditional draught animal adaptation to hyper-arid environments.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Camel_caravan_going_through_sand_in_the_Sahara_Desert.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Camel_caravan_going_through_sand_in_the_Sahara_Desert.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Traditional Land Transport: Human & Animal Power",
                        "content": {
                            "title": "Traditional Land Transport: Human & Animal Power",
                            "text": "Prior to internal combustion engines, transport relied on muscle power:\n\n• Human Porterage: Carrying goods on backs, heads, or using bicycles, handcarts, and wheelbarrows. Essential for last-mile delivery in dense urban slums and steep mountain paths.\n\n• Animal Transport (Draught Power): Domesticated animals carrying loads or pulling carts, tailored to specific biomes."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Ecological Adaptations of Traditional Animal Transport",
                        "content": {
                            "title": "Comparative Ecological Adaptations of Traditional Animal Transport",
                            "caption": "Ecological Matrix Matching Animal Species to Specific Terrain and Climatic Transport Adaptations",
                            "description": "Comparative diagram illustrating Camels (Sahara Desert dunes), Donkeys (rugged mountain slopes), Oxen (agricultural farm ploughing), and Elephants (tropical forest timber hauling)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Ecological Specialization of Draught Animals",
                        "content": {
                            "title": "Ecological Specialization of Draught Animals",
                            "text": "Draught animals represent specialized ecological adaptations:\n\n• Camels ('Ships of the Desert'): Wide padded hooves and water retention adapt them to Sahara and Chalbi sand dunes.\n• Donkeys: Sure-footed stability adapts them to steep, rocky, unpaved mountain tracks in Kenya's Rift Valley.\n• Oxen: High muscle traction for pulling heavy crop carts in agricultural farming zones.\n• Elephants: Heavy haulage in tropical forests (India, Burma) dragging heavy timber logs where wheeled trucks cannot penetrate."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Detailed Advantages of Traditional Transport",
                        "content": {
                            "title": "Detailed Advantages of Traditional Transport",
                            "text": "1. Cost-Efficient: Requires no expensive petroleum fuels or complex engines.\n2. Low Maintenance: Animals feed on locally available grass and shrubs.\n3. Zero Carbon Emissions: Environmentally friendly with no greenhouse gas or noise pollution.\n4. Extreme Flexibility: Can traverse narrow, unpaved, steep, or muddy paths impassable to motorized trucks."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Disadvantages of Traditional Transport",
                        "content": {
                            "title": "Disadvantages of Traditional Transport",
                            "text": "1. Extremely Slow: Tedious transit speeds make it unsuited for urgent deliveries or long-distance trade.\n2. Small Payload Capacity: Humans and animals tire easily, making them incapable of moving heavy industrial machinery.\n3. Exposure to Elements: Goods suffer damage from rain, heat, and theft during slow transit.\n4. Urban Traffic Obstruction: Slow handcarts cause severe congestion when entering modern urban streets."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Rural Geography Insight: Last-Mile Connectivity",
                        "content": {
                            "type": "tip",
                            "title": "Rural Geography Insight: Last-Mile Connectivity",
                            "text": "In mountainous rural areas lacking tarmac roads, donkeys and bicycles remain the only viable transport mode to move milk and kale from farms to highway collection centers."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Traditional vs Modern Transport Efficiency & Payload Matrix",
                        "content": {
                            "title": "Traditional vs Modern Transport Efficiency & Payload Matrix",
                            "caption": "Comparative Radar Framework Contrasting Speed, Payload Capacity, Fuel Cost, and Infrastructure Requirements",
                            "description": "Comparative chart contrasting Traditional (Low Speed, 100 kg Payload, Zero Fuel, Narrow Tracks) with Modern Motorized (High Speed, 30 Ton Payload, Petroleum Fuel, Tarmac Highways)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Traditional vs Modern Land Transport",
                        "content": {
                            "headers": ["Feature", "Traditional Animal/Human Transport", "Modern Motorized Road/Rail Transport"],
                            "rows": [
                                ["Energy Source", "Human & Animal Muscle (Zero Fuel)", "Petroleum, Diesel, & Electricity"],
                                ["Transit Speed", "Extremely Slow (3 - 6 km/h)", "High Speed (60 - 120 km/h)"],
                                ["Payload Capacity", "Highly Limited (50 kg - 500 kg)", "Massive (10 Tons - 5,000 Tons per train)"],
                                ["Infrastructure", "Narrow unpaved tracks & mountain footpaths", "Engineered tarmac highways & steel rails"],
                                ["Environmental Impact", "Zero carbon emissions; eco-friendly", "Exhaust fumes, greenhouse gases, & noise"]
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Traditional Mode Selection Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Traditional Mode Selection Challenge",
                            "prompt": "A conservation team in a remote, heavily forested mountain pocket in Kenya needs to transport delicate medical supplies 15 km over 35% muddy slopes after a rainstorm. No paved roads exist. Which mode is most appropriate?",
                            "options": [
                                "Option A: Pack Donkeys (High stability on steep, slippery unpaved paths; safe controlled pace).",
                                "Option B: Heavy Diesel Truck (Will get stuck in deep mud on 35% slopes).",
                                "Option C: Motorbike (Tires will slip on steep muddy rocks, risking sample destruction)."
                            ],
                            "correct_option": "Option A: Pack Donkeys (High stability on steep, slippery unpaved paths; safe controlled pace).",
                            "explanation": "Pack donkeys possess sure-footed stability on steep, muddy, unpaved tracks where motorized vehicles slip or get stuck."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Foundations & Traditional Transport",
                        "content": {
                            "question": "Which draught animal is uniquely adapted to hauling heavy timber logs through dense tropical forests where wheeled vehicles cannot penetrate?",
                            "options": [
                                "Elephant",
                                "Camel",
                                "Horse",
                                "Donkey"
                            ],
                            "correct_answer": 0,
                            "explanation": "Elephants are used in dense tropical forests (such as in Asia) to drag heavy timber logs through thick vegetation where wheeled vehicles cannot enter."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Transport Foundations: Key Takeaways",
                        "content": {
                            "title": "Transport Foundations: Key Takeaways",
                            "summary_points": [
                                "Transport moves physical matter and people across space; communication transfers digital signals and spatial information.",
                                "Network layouts depend on surplus-deficit economic gradients, alternative suppliers, infrastructure quality, and political policies.",
                                "Traditional transport uses human porterage and draught animals (camels in deserts, donkeys on mountains, elephants in forests).",
                                "Traditional transport is cheap, eco-friendly, and flexible, but limited by slow speeds, low payload capacity, and weather exposure."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Modern Land Transport: Road and Railway Networks in Africa
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Modern Land Transport: Road and Railway Networks in Africa",
            "unit_description": "Road classifications, four trans-continental African highways, railway mechanics, advantages/disadvantages, and fragmented rail networks.",
            "lesson_title": "Modern Land Transport: Road and Railway Networks in Africa",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Modern Land Transport in Africa",
                        "content": {
                            "title": "Learning Objectives: Modern Land Transport in Africa",
                            "goals": [
                                "Classify roads into all-weather, dry-weather, and motorable tracks.",
                                "Trace the four primary trans-continental highway corridors across Africa.",
                                "Analyze the economic advantages and disadvantages of road vs rail transport.",
                                "Evaluate five historical and political causes of fragmented railway gauge networks in Africa."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Modern Land Transport Networks",
                        "content": {
                            "title": "Modern Land Transport Networks",
                            "text": "Modern land transport relies on internal combustion engines and electric locomotives operating along engineered highways and steel railways. They form the backbone of national commerce, moving bulk agricultural produce and industrial goods."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Four Principal Trans-Continental Highway Corridors Across Africa",
                        "content": {
                            "title": "Four Principal Trans-Continental Highway Corridors Across Africa",
                            "caption": "Thematic Map Displaying the Great North Road, Trans-Africa Highway, Dakar-Djamena, and Trans-Sahara Corridors",
                            "description": "Map plotting 1. Great North Road (Cape Town to Cairo); 2. Trans-Africa Highway (Mombasa to Dakar); 3. Dakar-Djamena Highway (West Africa); 4. Trans-Sahara Highway (Lagos to Tripoli)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Classification of Roads & Trans-African Highways",
                        "content": {
                            "title": "Classification of Roads & Trans-African Highways",
                            "text": "Roads are categorized by engineered surface durability:\n\n• All-Weather Roads: Paved tarmac or high-grade murrum usable year-round regardless of rainfall.\n• Dry-Weather Roads: Unpaved earthen roads that become muddy and impassable during heavy rains.\n• Motorable Tracks: Unengineered paths worn into soil by repeated vehicle passage.\n\nMajor Trans-African Corridors:\n1. Great North Road: Cape Town to Cairo.\n2. Trans-Africa Highway: Mombasa (Kenya) to Dakar (Senegal).\n3. Trans-Sahara Highway: Lagos (Nigeria) to Tripoli (Libya)."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Road Network Classification Taxonomy",
                        "content": {
                            "term": "All-Weather vs Dry-Weather Roads",
                            "definition": "All-weather roads feature waterproof bituminised tarmac or thick compacted murrum designed for year-round heavy traffic. Dry-weather earthen roads deteriorate into impassable mud during rainy seasons.",
                            "key_points": [
                                "All-Weather: Mombasa-Nairobi-Malaba highway, Thika Superhighway.",
                                "Dry-Weather: Rural feeder roads connecting remote farms to market centers.",
                                "Impact: Poor roads cause agricultural crop spoilage before reaching markets."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Advantages and Disadvantages of Road Transport",
                        "content": {
                            "title": "Advantages and Disadvantages of Road Transport",
                            "text": "• Advantages: 1. Door-to-door delivery flexibility; 2. Faster than rail over short-to-medium distances; 3. Cheaper initial construction cost than railway tracks; 4. Incremental paving and repair.\n\n• Disadvantages: 1. Traffic congestion in cities; 2. Uneconomical for moving very heavy, bulky cargo over 500+ km; 3. Atmospheric pollution from exhaust gases; 4. Vulnerability to rain and fog hazards."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Kenya SGR Madaraka Express Freight Train",
                        "content": {
                            "title": "Kenya SGR Madaraka Express Freight Train",
                            "caption": "Kenya Standard Gauge Railway (SGR) freight train hauling heavy containerized cargo between Mombasa Port and Nairobi Inland Container Depot.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Railway Transport Mechanics & Economics",
                        "content": {
                            "title": "Railway Transport Mechanics & Economics",
                            "text": "Rail transport utilizes trains running along fixed steel rails. It is the most economical mode for transporting heavy, bulky cargo (grain, cement, oil, minerals) over long distances because a single freight train can haul up to 5,000 tons per trip."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "High-Volume Economy & Dedicated Safety",
                        "content": {
                            "title": "High-Volume Economy & Dedicated Safety",
                            "text": "Operating on dedicated tracks eliminates traffic jams and scheduling delays. Advanced signaling systems make trains significantly safer and less accident-prone than highway trucks."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Economic Rule: Long-Distance Rail Economies",
                        "content": {
                            "type": "tip",
                            "title": "Economic Rule: Long-Distance Rail Economies",
                            "text": "Per-ton freight costs decrease sharply as railway haulage distance increases. Rail is up to 60% cheaper than road trucks for heavy freight over 500 km."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Road vs Rail Cost Efficiency Curves Over Distance",
                        "content": {
                            "title": "Road vs Rail Cost Efficiency Curves Over Distance",
                            "caption": "Cost-Distance Graph Illustrating the Crossover Point Where Railway Transport Becomes Cheaper Than Road Transport",
                            "description": "Graph plotting Freight Cost per Ton against Transit Distance, showing Road cheaper for distances under 300 km, and Rail significantly cheaper for distances over 300 km."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Road vs Rail Distance Crossover",
                        "content": {
                            "title": "The Road vs Rail Distance Crossover",
                            "text": "For short distances (under 300 km), road transport is cheaper because it avoids railway terminal loading fees. Beyond 300 km, rail's massive payload capacity outweighs terminal costs, making it far cheaper."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Fragmented Railway Networks in Africa",
                        "content": {
                            "title": "Fragmented Railway Networks in Africa",
                            "text": "African countries possess fragmented, poorly integrated railway lines that run from inland mines/farms straight to coastal ports, lacking cross-border lateral connections."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Five Causes of African Rail Fragmentation",
                        "content": {
                            "title": "Five Causes of African Rail Fragmentation",
                            "text": "1. Colonial Partition: Railways were built by rival European powers to haul raw materials from inland colonies to sea ports, not to connect neighboring African nations.\n\n2. Incompatible Rail Gauges: Different powers laid different track widths (Cape Gauge 1067 mm, Meter Gauge 1000 mm, Standard Gauge 1435 mm), preventing cross-border train transfers.\n\n3. Political Hostility: Post-independence border disputes discouraged joint railway expansion.\n\n4. Low Interstate Trade: Neighboring nations produce similar agricultural crops, creating weak trade incentives.\n\n5. High Capital Costs: Massive capital required to engineer lines across steep Rift Valleys and mountains."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Historical Causes of Fragmented Railway Gauge Networks in Africa",
                        "content": {
                            "title": "Historical Causes of Fragmented Railway Gauge Networks in Africa",
                            "caption": "Spatial Diagram Displaying Colonial Penetration Lines Connecting Inland Mines to Coastal Ports without Cross-Border Lateral Links",
                            "description": "Map displaying perpendicular colonial rail lines running inland to coast, highlighting broken gauge barriers between Meter Gauge and Cape Gauge systems."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Solution: Rail Standardisation",
                        "content": {
                            "type": "warning",
                            "title": "Geographical Solution: Rail Standardisation",
                            "text": "African nations are adopting Standard Gauge Railway (1435 mm SGR) corridors under AU treaties to integrate regional rail freight from Mombasa to Kampala and Kigali."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Road vs Rail Cargo Selection Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Road vs Rail Cargo Selection Simulator",
                            "prompt": "A mining firm needs to move 500 tons of heavy copper plates 800 km from Eldoret to Mombasa Port. SGR rail and highway exist. Which mode is most geographically appropriate?",
                            "options": [
                                "Option A: Railway Transport (Designed to haul heavy, bulky cargo over long distances in one trip at low per-ton cost).",
                                "Option B: Road Trucking (Moving 500 tons requires 15+ heavy trucks, incurring high fuel costs, traffic jams, and road wear).",
                                "Option C: Air Freight (Prohibitively expensive for heavy, low-value mineral plates)."
                            ],
                            "correct_option": "Option A: Railway Transport (Designed to haul heavy, bulky cargo over long distances in one trip at low per-ton cost).",
                            "explanation": "Moving 500 tons over 800 km is far cheaper and more efficient by freight train, eliminating road wear and high fuel bills."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Road & Rail Networks in Africa",
                        "content": {
                            "question": "What is the primary historical reason why many African nations inherited fragmented railway networks lacking cross-border connections?",
                            "options": [
                                "Colonial powers built independent lines running strictly from inland resource sites to coastal export ports without lateral links.",
                                "African rivers completely blocked all train engines.",
                                "Railways were banned by international trade treaties.",
                                "Trains could only operate in desert environments."
                            ],
                            "correct_answer": 0,
                            "explanation": "Colonial railways were built to extract inland minerals and crops straight to sea ports, neglecting inter-state links."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Modern Land Transport: Key Takeaways",
                        "content": {
                            "title": "Modern Land Transport: Key Takeaways",
                            "summary_points": [
                                "Roads offer door-to-door flexibility and speed for short distances, classified into all-weather, dry-weather, and motorable tracks.",
                                "Major African highways include the Great North Road, Trans-Africa Highway, and Trans-Sahara Highway.",
                                "Railways provide high-volume economy over long distances (300+ km) for bulky industrial freight.",
                                "African rail networks suffer from colonial export fragmentation, gauge incompatibilities, and high mountain capital costs."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Water, Pipeline, and Air Transport & Containerisation
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Water, Pipeline, and Air Transport & Containerisation",
            "unit_description": "Pipeline mechanics (KPC), ocean shipping (Liners vs Tramps), intermodal containerisation, air freight exports, and cargo mode selection decision models.",
            "lesson_title": "Water, Pipeline, and Air Transport & Containerisation",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Specialized & Oceanic Transport",
                        "content": {
                            "title": "Learning Objectives: Specialized & Oceanic Transport",
                            "goals": [
                                "Analyze pipeline transport mechanics, safety, and Kenya Pipeline Corporation (KPC) infrastructure.",
                                "Distinguish between ocean Liners and Tramps in international sea trade.",
                                "Evaluate four major advantages of intermodal containerisation in global shipping.",
                                "Justify transport mode selection for contrasting industrial and agricultural cargoes (copper vs French beans)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Specialized and Global Transport Systems",
                        "content": {
                            "title": "Specialized and Global Transport Systems",
                            "text": "Beyond roads and railways, specialized transport modes—pipelines for fluids, ocean vessels for bulk international trade, and aircraft for high-value perishable exports—form the pillars of modern international trade."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pipeline Transport Flow & Storage Infrastructure",
                        "content": {
                            "title": "Pipeline Transport Flow & Storage Infrastructure",
                            "caption": "Pumping Station Flow Model Displaying Refined Petroleum Movement from Mombasa Changamwe Refinery to Inland Depots",
                            "description": "Diagram illustrating Mombasa Changamwe Marine Terminal -> KPC High-Pressure Pumping Station -> Nairobi Depot -> Nakuru -> Eldoret -> Kisumu."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Pipeline Transport & Kenya Pipeline Corporation (KPC)",
                        "content": {
                            "title": "Pipeline Transport & Kenya Pipeline Corporation (KPC)",
                            "text": "Pipelines move liquid fluids (crude oil, refined petrol, diesel, jet fuel, water) and gases through sealed underground pipes using high-pressure pumping stations.\n\n• Kenya Pipeline Corporation (KPC): Operates the trunk pipeline carrying refined petroleum products from Changamwe in Mombasa to depots in Nairobi, Nakuru, Eldoret, and Kisumu.\n\n• Advantages: 1. Continuous 24/7 flow unaffected by surface weather or traffic jams; 2. Lowest operating cost for liquids; 3. Eliminates tanker accidents and road wear.\n• Disadvantages: 1. High initial capital laying cost; 2. Inflexible (cannot transport solids); 3. Vulnerable to underground leaks and sabotage."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Petroleum Pipeline Construction",
                        "content": {
                            "title": "Commercial Petroleum Pipeline Construction",
                            "caption": "Underground steel petroleum pipeline installation establishing continuous fluid transport infrastructure.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Pipeline_work.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pipeline_work.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Fluid Dynamics & Environmental Safety",
                        "content": {
                            "title": "Fluid Dynamics & Environmental Safety",
                            "text": "Underground pipelines avoid heavy oil tanker trucks on highways, preventing major road collisions and curbing diesel exhaust emissions."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Water Transport: Liners vs Tramps",
                        "content": {
                            "title": "Water Transport: Liners vs Tramps",
                            "text": "Water transport is the cheapest mode for moving heavy, bulky international cargo across oceans. Ocean vessels fall into two distinct operational classes:\n\n• Ocean Liners: Ships operating along fixed geographical routes on rigid time schedules, carrying passengers and containerized cargo at fixed tariff rates.\n\n• Ocean Tramps: Merchant ships with no fixed routes or set schedules. They charter wherever bulk cargo (grain, coal, iron ore) is offered, charging negotiable freight rates based on market demand."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Exam Distinction: Liners vs Tramps",
                        "content": {
                            "type": "tip",
                            "title": "Exam Distinction: Liners vs Tramps",
                            "text": "Remember: Liners are like scheduled city buses (fixed routes, fixed times, fixed fares). Tramps are like charter taxis (no fixed routes, flexible schedules, negotiable fares)."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Ocean Shipping Structure: Liners vs Tramps Comparison",
                        "content": {
                            "title": "Ocean Shipping Structure: Liners vs Tramps Comparison",
                            "caption": "Comparative Dual Taxonomy Matrix Contrasting Operational Schedules, Routes, Fares, and Cargo Types",
                            "description": "Comparative matrix contrasting Liners (Fixed Schedule, Fixed Route, Standard Tariffs, Containerized Goods) with Tramps (No Fixed Schedule, Flexible Charter Route, Negotiable Freight, Bulk Coal/Grain)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison: Ocean Liners vs Ocean Tramps",
                        "content": {
                            "headers": ["Feature", "Ocean Liners", "Ocean Tramps"],
                            "rows": [
                                ["Routes & Schedules", "Operate along fixed routes on rigid timetables", "No fixed routes or set timetables (charter)"],
                                ["Tariff Fares", "Charge fixed, published freight rates", "Freight rates are negotiable based on supply/demand"],
                                ["Cargo Type", "High-value containerized goods & passengers", "Bulky raw materials (coal, iron ore, wheat)"],
                                ["Speed & Quality", "Fast, modern vessels with premium service", "Slower merchant vessels focused on low cost"]
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_image",
                        "title": "Container Shipping Port Terminal & Gantry Cranes",
                        "content": {
                            "title": "Container Shipping Port Terminal & Gantry Cranes",
                            "caption": "Modern deep-water container terminal featuring gantry cranes loading standardized TEU steel containers onto an ocean ship.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Container-Terminal_Bremerhaven_02.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Container-Terminal_Bremerhaven_02.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Containerisation Revolution",
                        "content": {
                            "title": "The Containerisation Revolution",
                            "text": "Containerisation is the practice of packing cargo into standardized, sealed steel boxes (Twenty-Foot Equivalent Units - TEUs) for seamless transfer between ships, trains, and trucks.\n\n• Key Advantages: 1. Security (sealed boxes prevent theft and weather damage); 2. Speed (automated gantry cranes load ships 10x faster than manual labor); 3. Reduced Port Congestion (ships spend less time docked); 4. Intermodal Efficiency (containers move directly onto SGR trains)."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Intermodal Containerisation Value Chain & Automated Handling",
                        "content": {
                            "title": "Intermodal Containerisation Value Chain & Automated Handling",
                            "caption": "Intermodal Flow Model: Factory Packing → Sealed Container Truck → Port Gantry Crane → Ocean Container Ship → SGR Freight Train",
                            "description": "Flowchart showing sealed container packed at factory, moved by truck to port, lifted by gantry crane onto ship, shipped across ocean, transferred directly onto SGR train."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Air Transport: Speed & Perishable Exports",
                        "content": {
                            "title": "Air Transport: Speed & Perishable Exports",
                            "text": "Air transport is the fastest transport mode over long distances, operating along international sky corridors.\n\n• Key Role in Kenya: Cargo planes from Jomo Kenyatta International Airport (JKIA) export high-value, highly perishable horticultural produce (fresh flowers, French beans, snow peas) directly to European markets (London, Amsterdam) within 12 hours."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Air Freight Cargo Aircraft Loader Operations",
                        "content": {
                            "title": "Air Freight Cargo Aircraft Loader Operations",
                            "caption": "High-speed motorized ULD cargo loader loading palleted freight into a commercial cargo jet aircraft.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Aircraft_cargo_%28ULD%29_loader_in_operaton.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Aircraft_cargo_(ULD)_loader_in_operaton.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Advantages and Constraints of Air Freight",
                        "content": {
                            "title": "Advantages and Constraints of Air Freight",
                            "text": "• Advantages: 1. Unmatched transit speed; 2. Overcomes physical land barriers (mountains, oceans); 3. High security for precious items (gold, diamonds, medicine).\n\n• Constraints: 1. Extremely expensive freight rates per kg; 2. Strict payload weight/volume limits; 3. High fuel consumption and airport infrastructure costs."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Mode Selection Decision Tree for Industrial Cargo",
                        "content": {
                            "title": "Mode Selection Decision Tree for Industrial Cargo",
                            "caption": "Geographical Decision Tree Pairing Cargo Perishability, Weight, and Value to Optimal Transport Modes",
                            "description": "Decision tree diagram: Heavy/Bulky + Non-Perishable (500 Tons Copper) -> Railway; Light + Highly Perishable (5 Tons French Beans) -> Air Freight; Fluid (Crude Oil) -> Pipeline."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Mode Selection Model Reasoning: Eldoret Exports",
                        "content": {
                            "question": "Justify the transport mode for: (a) 500 tons of heavy copper sheets from Eldoret to Mombasa Port; (b) 5 tons of fresh French beans from Eldoret to London, UK.",
                            "strategy": "Analyze cargo perishability, weight, distance, and relative transport costs.",
                            "solution": [
                                "(a) 500 Tons Copper Sheets (Eldoret to Mombasa): Use RAILWAY TRANSPORT. Copper is extremely heavy and non-perishable. Moving 500 tons 800 km by rail yields maximum cost savings and avoids heavy road wear. (3 Marks)",
                                "(b) 5 Tons Fresh French Beans (Eldoret to London): Use AIR TRANSPORT. French beans are highly perishable and lightweight. Air freight reaches London within 12 hours, preserving freshness and market value. (3 Marks)"
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "concept_explanation",
                        "title": "Cargo Characteristics Dictating Transport Choice",
                        "content": {
                            "title": "Cargo Characteristics Dictating Transport Choice",
                            "text": "Geographers evaluate three cargo rules when selecting transport:\n1. Weight & Bulk: Heavy minerals require rail or ocean freight.\n2. Perishability: Fresh flowers and vegetables require air freight.\n3. Physical State: Liquids and gases require pipelines."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Cargo Transport Selection Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Cargo Transport Selection Challenge",
                            "prompt": "Which mode of transport is most geographically appropriate for exporting 2 tons of fresh cut roses from Naivasha farms to flower markets in Amsterdam, Netherlands?",
                            "options": [
                                "Option A: Air Freight (Unmatched speed delivers delicate perishable roses to European markets in under 12 hours).",
                                "Option B: Ocean Cargo Ship (Takes 3 weeks; roses will decay and lose all commercial value).",
                                "Option C: Railway Freight (Cannot cross the Mediterranean Sea)."
                            ],
                            "correct_option": "Option A: Air Freight (Unmatched speed delivers delicate perishable roses to European markets in under 12 hours).",
                            "explanation": "Fresh cut roses are highly perishable and high-value, requiring high-speed air freight to reach European florists fresh."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Water, Pipeline, Air & Containers",
                        "content": {
                            "question": "What is the key operational distinction between an Ocean Liner and an Ocean Tramp?",
                            "options": [
                                "Liners operate along fixed routes on rigid timetables, while Tramps have no set routes or schedules and charter wherever cargo is offered.",
                                "Liners can only sail on rivers, while Tramps sail on oceans.",
                                "Tramps carry passengers, while Liners only carry crude oil.",
                                "Liners use animal power, while Tramps use solar panels."
                            ],
                            "correct_answer": 0,
                            "explanation": "Liners operate on fixed routes with published timetables, whereas Tramps charter flexibly without set routes or schedules."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "summary",
                        "title": "Modern Transport Modes: Key Takeaways",
                        "content": {
                            "title": "Modern Transport Modes: Key Takeaways",
                            "summary_points": [
                                "Pipelines move petroleum and gas continuously 24/7 at low cost, operated in Kenya by KPC.",
                                "Ocean Liners run on fixed schedules/routes; Ocean Tramps charter flexibly for bulk raw materials.",
                                "Containerisation provides security, speed, reduced port congestion, and intermodal ship-to-rail transfer.",
                                "Air transport delivers unmatched speed for high-value perishable horticultural exports (flowers, French beans) to Europe."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Major Inland Waterway Case Study: The St. Lawrence Seaway Project
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Major Inland Waterway Case Study: The St. Lawrence Seaway Project",
            "unit_description": "The St. Lawrence Seaway, natural navigation obstacles, three major engineering solutions (dredging, dams, locks), and economic benefits to USA and Canada.",
            "lesson_title": "Major Inland Waterway Case Study: The St. Lawrence Seaway Project",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: St. Lawrence Seaway Project",
                        "content": {
                            "title": "Learning Objectives: St. Lawrence Seaway Project",
                            "goals": [
                                "Describe the geographic location of the Great Lakes and St. Lawrence River waterway.",
                                "Analyze seven natural obstacles that hindered navigation prior to the seaway project.",
                                "Examine three major engineering solutions (dredging, dams, canals & locks like Welland/Soo).",
                                "Evaluate five economic benefits of the Seaway to the USA and Canada."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The St. Lawrence Seaway Engineering Marvel",
                        "content": {
                            "title": "The St. Lawrence Seaway Engineering Marvel",
                            "text": "The St. Lawrence Seaway is a joint North American engineering masterpiece constructed by Canada and the USA. Opened in 1959, it links the five interior Great Lakes (Superior, Huron, Michigan, Erie, Ontario) to the Atlantic Ocean, creating a 3,700 km deep-water shipping highway into the heart of the continent."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Physical Topographic Profile of the St. Lawrence Seaway",
                        "content": {
                            "title": "Physical Topographic Profile of the St. Lawrence Seaway",
                            "caption": "Step-Down Elevation Profile Showing Water Level Drops from Lake Superior (183m) Through Niagara Falls (99m Drop) to Atlantic Sea Level",
                            "description": "Elevation cross-section showing Lake Superior (183 m elevation) -> St. Mary's Rapids -> Lake Huron/Michigan -> Lake Erie -> Niagara Falls (99 m drop) -> Lake Ontario -> St. Lawrence River -> Atlantic Ocean."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Seven Natural Obstacles Hindering Early Navigation",
                        "content": {
                            "title": "Seven Natural Obstacles Hindering Early Navigation",
                            "text": "Prior to 1959, ocean ships could not penetrate the Great Lakes due to seven severe natural barriers:\n\n1. Waterfalls & Drop-offs: Niagara Falls (99 m sheer drop between Erie and Ontario) blocked all navigation.\n2. Dangerous Rapids: St. Mary's Rapids and Lachine Rapids threatened to smash wooden ship hulls.\n3. Shallow Channels: Water depths were too shallow for deep-draft ocean cargo freighters.\n4. Rocky Islands: Thousands of granite rocky islands in the St. Lawrence River choked narrow channels.\n5. Severe Winter Freezing: Waterways froze completely for 3 to 4 months (December to April).\n6. Dense Fog: Persistent thick fog over Atlantic river mouths reduced visibility.\n7. Narrow River Sections: Restricted vessel maneuvering."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Elevation Barrier: Niagara Falls",
                        "content": {
                            "title": "The Elevation Barrier: Niagara Falls",
                            "text": "The 99-meter water elevation drop over Niagara Falls created an absolute physical wall between Lake Erie and Lake Ontario, completely sealing the upper Great Lakes from ocean shipping."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Miracle: Drowning the Rapids",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Miracle: Drowning the Rapids",
                            "text": "Engineers constructed massive hydroelectric dams (Moses-Saunders Dam) across fast rivers, raising water levels into deep artificial lakes that completely drowned dangerous rapids."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Vessel Passing Through St. Lawrence Seaway Lock",
                        "content": {
                            "title": "Vessel Passing Through St. Lawrence Seaway Lock",
                            "caption": "Large ocean freight vessel navigating a concrete lock chamber along the St. Lawrence Seaway.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/6/68/St._Lawrence_Seaway_lock_scenes_%28I0015590%29.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:St._Lawrence_Seaway_lock_scenes_(I0015590).jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Three Major Engineering Solutions",
                        "content": {
                            "title": "Three Major Engineering Solutions",
                            "text": "Canada and the USA executed three massive engineering projects:\n\n1. Deepening & Dredging: Massive underwater blasting and dredging deepened river channels to a minimum 8.2-meter ocean draft.\n\n2. Dam Construction: Massive hydro-dams flooded turbulent rapids into navigable calm reservoirs.\n\n3. Canals and Locks Construction: Built artificial canals fitted with concrete lock chambers to step ships up and down elevation drops:\n   • Welland Canal (8 locks): Bypasses Niagara Falls between Lake Erie and Lake Ontario.\n   • Soo Locks (Sault Ste. Marie): Bypasses St. Mary's Rapids between Lake Superior and Lake Huron."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Engineering Lock Mechanism Functioning in Canal Navigation",
                        "content": {
                            "title": "Engineering Lock Mechanism Functioning in Canal Navigation",
                            "caption": "Step-by-Step Water Equalization Model Demonstrating How Canal Locks Raise and Lower Ocean Vessels Across Elevation Steps",
                            "description": "Three-stage lock mechanism diagram showing Stage 1: Ship enters lower lock chamber; Stage 2: Lock gates close and water fills chamber from upper reservoir; Stage 3: Ship rises to upper canal level and sails out."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "How Canal Locks Function",
                        "content": {
                            "title": "How Canal Locks Function",
                            "text": "A lock is an enclosed water chamber with watertight gates. To lift a ship uphill:\n1. The ship enters the lock chamber at lower water level.\n2. The lower gates close watertight.\n3. Valves open, allowing water from the upper lake to fill the chamber by gravity, floating the ship upward.\n4. When water levels equalize, the upper gates open, allowing the ship to sail out into the higher lake."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Welland Canal and Soo Locks Engineering",
                        "content": {
                            "title": "Welland Canal and Soo Locks Engineering",
                            "text": "The Welland Canal features 8 gigantic locks that raise ships 99 meters over the Niagara Escarpment. The Soo Locks handle millions of tons of iron ore shipping out of Lake Superior mines."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Socio-Economic Impact Network of the St. Lawrence Seaway",
                        "content": {
                            "title": "Socio-Economic Impact Network of the St. Lawrence Seaway",
                            "caption": "Economic Value Network Linking Great Lakes Agricultural Prairies, Iron Ore Mines, Hydroelectric Power, and Global Shipping",
                            "description": "Concept network showing Canadian Wheat Prairies & Mesabi Iron Mines -> Seaway Water Transport -> Great Lakes Industrial Steel Hubs (Chicago, Detroit, Toronto) -> Global Atlantic Exports."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Five Economic Benefits to USA and Canada",
                        "content": {
                            "title": "Five Economic Benefits to USA and Canada",
                            "text": "1. Cheap Bulk Freight: Cut transport costs by 70% for moving bulk Canadian wheat and Mesabi iron ore.\n2. Industrialisation Hubs: Triggered massive steel and automobile manufacturing in inland ports (Chicago, Detroit, Cleveland, Toronto, Montreal).\n3. Hydroelectric Power: Dams generate billions of kilowatt-hours of cheap HEP for industrial grids.\n4. Employment Creation: Created thousands of jobs for dockers, sailors, lock operators, and factory workers.\n5. International Trade Stimulus: Opened interior North American grain and steel directly to European ocean markets."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Industrial Growth in Inland Ports",
                        "content": {
                            "title": "Industrial Growth in Inland Ports",
                            "text": "Inland cities located thousands of kilometers from the ocean (Chicago, Detroit, Toronto) became major ocean shipping ports, receiving imported raw materials and exporting manufactured cars and steel directly."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Challenge: Invasive Species",
                        "content": {
                            "type": "warning",
                            "title": "Environmental Challenge: Invasive Species",
                            "text": "Ocean freighters discharging ballast water introduced invasive zebra mussels into the Great Lakes, causing ecological damage to native fish species."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Canal Lock Engineering Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Canal Lock Engineering Simulator",
                            "prompt": "How did engineers solve the 99-meter vertical water drop at Niagara Falls to allow ocean ships to sail from Lake Ontario into Lake Erie?",
                            "options": [
                                "Option A: Constructed the Welland Canal featuring 8 concrete locks that step ships up 99 meters using gravity water filling.",
                                "Option B: Built giant helicopter cranes to lift ships over the falls.",
                                "Option C: Blasted Niagara Falls completely flat with explosives."
                            ],
                            "correct_option": "Option A: Constructed the Welland Canal featuring 8 concrete locks that step ships up 99 meters using gravity water filling.",
                            "explanation": "The Welland Canal bypasses Niagara Falls by using 8 locks to gradually lift and lower ships 99 meters between Ontario and Erie."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: St. Lawrence Seaway Project",
                        "content": {
                            "question": "Which specific canal was constructed to bypass Niagara Falls and connect Lake Erie with Lake Ontario?",
                            "options": [
                                "Welland Canal",
                                "Soo Canal",
                                "Suez Canal",
                                "Panama Canal"
                            ],
                            "correct_answer": 0,
                            "explanation": "The Welland Canal features 8 locks that bypass Niagara Falls, connecting Lake Erie and Lake Ontario."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "St. Lawrence Seaway Case Study: Key Takeaways",
                        "content": {
                            "title": "St. Lawrence Seaway Case Study: Key Takeaways",
                            "summary_points": [
                                "The 3,700 km St. Lawrence Seaway connects the five interior Great Lakes to the Atlantic Ocean.",
                                "Natural obstacles included Niagara Falls, rapids, rocky islands, shallow channels, winter freezing, and fog.",
                                "Engineering solutions included channel dredging, hydro-dams, and canals/locks (Welland Canal bypassing Niagara, Soo Locks).",
                                "Economic benefits include cheap bulk wheat/iron ore shipping, Great Lakes industrial growth (Chicago, Detroit, Toronto), HEP generation, and employment."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Telecommunication Systems & Economic Development
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Telecommunication Systems & Economic Development",
            "unit_description": "Evolution of communication media (traditional to fiber-optic/satellites), economic impacts (M-Pesa, e-commerce, trade transparency), and digital constraints.",
            "lesson_title": "Telecommunication Systems & Economic Development",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Telecommunications & Development",
                        "content": {
                            "title": "Learning Objectives: Telecommunications & Development",
                            "goals": [
                                "Distinguish between traditional communication media and modern telecommunications.",
                                "Analyze the physical architecture of undersea fiber-optic cables and satellite networks.",
                                "Evaluate the macroeconomic impacts of mobile money (M-Pesa) and e-commerce in Kenya.",
                                "Examine physical, technical, and human constraints on modern telecommunications."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Telecommunications Revolution",
                        "content": {
                            "title": "The Telecommunications Revolution",
                            "text": "Telecommunications is the electronic transmission of signals, data, words, and images over long distances via wire, radio, optical fiber, or electromagnetic systems. It has transformed global trade by enabling instantaneous information exchange."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Taxonomy of Communication Systems",
                        "content": {
                            "term": "Traditional vs Modern Telecommunications",
                            "definition": "Traditional communication relies on physical paper dispatch (postal mail, telegrams, printed newspapers). Modern telecommunications utilizes electronic signals sent through subsea fiber-optic cables, cellular towers, and space satellites.",
                            "key_points": [
                                "Traditional: Postal letters, landline telegraphs, smoke signals, horn blowing.",
                                "Modern: Mobile smart phones, internet fiber-optics, satellite GPS, video conferencing.",
                                "Impact: Eliminates physical travel for information exchange, slashing transaction costs."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Subsea Cables and Space Satellites",
                        "content": {
                            "title": "Subsea Cables and Space Satellites",
                            "text": "High-speed internet traffic crosses oceans via subsea fiber-optic cables (e.g., TEAMS, SEACOM landing at Mombasa port). Space satellites in geostationary orbit relay broadcast signals to remote rural regions lacking physical cables."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Undersea Fiber Optic Cable & Satellite Communication Architecture",
                        "content": {
                            "title": "Undersea Fiber Optic Cable & Satellite Communication Architecture",
                            "caption": "Global Telecommunication Network Displaying Subsea Fiber Cables (SEACOM/TEAMS) Landing at Mombasa to Feed Cellular Towers and Satellites",
                            "description": "Network architecture diagram showing Ocean Subsea Fiber Cable -> Mombasa Landing Station -> Terrestrial Fiber Grid -> Rural Cellular Towers & Geostationary Satellites."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Mombasa Subsea Cable Landing Gateway",
                        "content": {
                            "title": "Mombasa Subsea Cable Landing Gateway",
                            "text": "Mombasa serves as East Africa's primary digital gateway. International fiber optic cables (SEACOM, TEAMS, LION) land at Mombasa sea port, feeding high-speed internet inland to Nairobi, Kampala, and Kigali."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Mobile Cellular Telecommunication Network Tower",
                        "content": {
                            "title": "Mobile Cellular Telecommunication Network Tower",
                            "caption": "High-gain cellular telecommunication tower relaying 4G/5G mobile signals across urban and rural landscapes.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Cell_Tower_Ciudad_del_Carmen2020.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Cell_Tower_Ciudad_del_Carmen2020.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Mobile Banking Revolution: M-Pesa",
                        "content": {
                            "title": "Mobile Banking Revolution: M-Pesa",
                            "text": "Kenya is a global pioneer in mobile financial technology. M-Pesa enables millions of citizens to transfer funds, pay bills, and secure loans instantly via mobile phones without needing formal bank branches."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "M-Pesa & Mobile Banking Economic Velocity Model",
                        "content": {
                            "title": "M-Pesa & Mobile Banking Economic Velocity Model",
                            "caption": "Financial Velocity Flow Demonstrating How Mobile Money Transfers Accelerate Rural-Urban Capital Movement",
                            "description": "Flowchart showing Urban Worker -> Instant M-Pesa Transfer -> Rural Farmer -> Merchant Purchase -> Financial Velocity & Business Growth."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Economic Benefits of Modern Telecommunications",
                        "content": {
                            "title": "Economic Benefits of Modern Telecommunications",
                            "text": "1. Market Price Transparency: Farmers check real-time crop prices in Nairobi via SMS, avoiding middleman exploitation.\n2. E-Commerce Expansion: Online marketplaces connect small businesses directly to global buyers.\n3. Financial Inclusion: Mobile banking integrates unbanked rural populations into formal commerce.\n4. Reduced Travel Friction: Video conferencing and digital billing eliminate expensive business travel."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Constraints Facing Telecommunications",
                        "content": {
                            "title": "Constraints Facing Telecommunications",
                            "text": "• Physical Constraints: Steep mountain relief blocks line-of-sight wireless signals; solar flare activity disrupts satellite broadcasts.\n• Technical & Financial Constraints: High capital costs for laying fiber-optic cables in sparse rural counties; frequent power outages.\n• Security Threats: Cybercrime, hacking, data privacy breaches, and physical cable vandalism."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Digital Divide Challenge",
                        "content": {
                            "type": "warning",
                            "title": "Digital Divide Challenge",
                            "text": "The gap between internet-connected urban towns and off-grid rural villages creates economic inequality, requiring government universal service funding."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Telecommunication Economic Model",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Telecommunication Economic Model",
                            "prompt": "How does mobile money technology (M-Pesa) directly accelerate trade in rural Kenyan agricultural communities?",
                            "options": [
                                "Option A: Provides instant, secure mobile financial transfers, allowing farmers to receive crop payments immediately without traveling to distant urban banks.",
                                "Option B: Replaces all agricultural crops with digital computer chips.",
                                "Option C: Prevents farmers from selling produce."
                            ],
                            "correct_option": "Option A: Provides instant, secure mobile financial transfers, allowing farmers to receive crop payments immediately without traveling to distant urban banks.",
                            "explanation": "Mobile money enables instant, secure cash transfers directly to farmers' phones, eliminating costly travel to distant bank branches."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Telecommunications & Development",
                        "content": {
                            "question": "Which East African sea port serves as the primary landing gateway for international subsea fiber-optic cables (SEACOM, TEAMS)?",
                            "options": [
                                "Mombasa Port",
                                "Kisumu Port",
                                "Dar es Salaam Port",
                                "Cape Town Port"
                            ],
                            "correct_answer": 0,
                            "explanation": "Mombasa sea port is East Africa's primary landing site for international subsea fiber-optic cables."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "summary",
                        "title": "Telecommunications: Key Takeaways",
                        "content": {
                            "title": "Telecommunications: Key Takeaways",
                            "summary_points": [
                                "Telecommunications transmits electronic voice, data, and video signals across space, replacing physical paper mail.",
                                "Mombasa acts as East Africa's digital landing gateway for high-speed subsea fiber cables (SEACOM, TEAMS).",
                                "Mobile technology (M-Pesa) drives financial inclusion, market price transparency, and e-commerce.",
                                "Constraints include high rural infrastructure costs, mountain signal blocking, power cuts, and cyber security threats."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Transport Barriers in Africa, Worked KCSE Essays, and Topic Assessment
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Transport Barriers in Africa, Worked KCSE Essays, and Topic Assessment",
            "unit_description": "Physical barriers to African river transport, strategic solutions, worked KCSE essay solutions, and topic mastery assessment.",
            "lesson_title": "Transport Barriers in Africa, Worked KCSE Essays, and Topic Assessment",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: African Transport Synthesis & KCSE Mastery",
                        "content": {
                            "title": "Learning Objectives: African Transport Synthesis & KCSE Mastery",
                            "goals": [
                                "Analyze four physical barriers hindering river navigation in Africa (volume drops, rapids, siltation, floating weeds).",
                                "Formulate strategic geographical and engineering solutions for African inland transport.",
                                "Master KCSE essay writing strategies for transport barriers, railway fragmentation, and mode selection.",
                                "Complete comprehensive end-of-topic revision exams."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "African Transport Synthesis",
                        "content": {
                            "title": "African Transport Synthesis",
                            "text": "Despite vast river systems, river transport in Africa remains poorly developed due to severe physical barriers. Overcoming these natural obstacles requires targeted engineering investments and international regional cooperation."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Four Physical Barriers to River Transport in Africa",
                        "content": {
                            "title": "Four Physical Barriers to River Transport in Africa",
                            "caption": "Hydrological Obstacle Matrix Displaying Water Fluctuation, Plateau Waterfalls, River Siltation, and Weed Choking",
                            "description": "Diagram displaying 1. Seasonal Water Fluctuation (volume drops in dry season); 2. Waterfalls & Rapids (plateau drop-offs); 3. River Siltation (shallow sandbars); 4. Floating Vegetation (water hyacinth choking propellers)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Four Physical Barriers to River Transport in Africa",
                        "content": {
                            "title": "Four Physical Barriers to River Transport in Africa",
                            "text": "1. Seasonal Water Volatility: Rivers pass through semi-arid zones where water levels drop severely during dry seasons, grounding vessels.\n\n2. Waterfalls and Rapids: Africa's steep interior plateau drop-offs create dangerous rapids and waterfalls (Livingstone Falls, Victoria Falls) that block ship movement.\n\n3. Siltation: Deforestation causes soil erosion, filling river beds with shallow silt and sandbars.\n\n4. Floating Vegetation: Invasive weeds (water hyacinth on Lake Victoria) choke navigation channels and entangle boat propellers."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_image",
                        "title": "River Rapids Navigation Barrier",
                        "content": {
                            "title": "River Rapids Navigation Barrier",
                            "caption": "Turbulent river rapids demonstrating steep rocky drop-offs that obstruct commercial vessel navigation in African rivers.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/45/Klondikers_in_boat_navigating_Whitehorse_Rapids%2C_probably_1898_%28AL%2BCA_639%29.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Klondikers_in_boat_navigating_Whitehorse_Rapids,_probably_1898_(AL%2BCA_639).jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Strategic Engineering Solutions for African Rivers",
                        "content": {
                            "title": "Strategic Engineering Solutions for African Rivers",
                            "text": "• Dredging: Continuous underwater excavation to clear shallow silt sandbars.\n• Dam & Reservoir Construction: Flooding rapids into calm deep reservoirs.\n• Canal Locks: Constructing bypass locks around waterfalls.\n• Mechanical Weed Harvesters: Clearing water hyacinth mats from Lake Victoria ports."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Strategic Engineering Interventions for African River Navigation",
                        "content": {
                            "title": "Strategic Engineering Interventions for African River Navigation",
                            "caption": "Engineering Intervention Model Pairing Physical River Obstacles with Source-Grounded Solutions",
                            "description": "Dual matrix pairing Siltation -> Dredging Vessels; Waterfalls -> Dam Reservoirs & Lock Canals; Water Hyacinth -> Mechanical Weed Harvesters; Seasonal Volume -> Storage Reservoirs."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Six-Point National Strategy for Integrated Transport & Communication",
                        "content": {
                            "title": "Six-Point National Strategy for Integrated Transport & Communication",
                            "caption": "Hexagonal Framework Displaying SGR Rail Expansion, Subsea Fiber Grid, Port Automation, BRT Bus Lanes, Air Freight Expansion, and Transit Treaties",
                            "description": "Hexagonal policy framework for 1. SGR rail expansion; 2. Rural fiber optic rollout; 3. Mombasa port automation; 4. Urban BRT lanes; 5. JKIA air cargo expansion; 6. EAC regional transit treaties."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 1: Transport & Communication Definitions",
                        "content": {
                            "question": "(a) Distinguish between transport and communication. (2 Marks)\n(b) State three advantages of containerisation in ocean trade. (3 Marks)",
                            "strategy": "Define physical mass movement vs electronic data transfer, then list container benefits.",
                            "solution": [
                                "(a) Transport is the physical movement of people and cargo from one place to another, whereas communication is the electronic transfer of information and signals between places. (2 Marks)",
                                "(b) 1. High Security: Sealed steel containers protect cargo from theft and weather damage. (1 Mark)\n2. Rapid Handling: Automated gantry cranes load ships much faster than manual dockers. (1 Mark)\n3. Reduced Port Congestion: Ships spend less time docked at sea ports. (1 Mark)"
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 2: St. Lawrence Engineering Solutions",
                        "content": {
                            "question": "Describe three engineering solutions implemented during the St. Lawrence Seaway Project to improve navigability. (6 Marks)",
                            "strategy": "Detail dredging, dam building, and canals/locks.",
                            "solution": [
                                "1. Dredging: Deepened shallow sections of the Great Lakes and river channel to a minimum 8.2-meter ocean draft. (2 Marks)",
                                "2. Dam Construction: Constructed massive hydro-dams (Moses-Saunders Dam) that drowned dangerous rapids into deep reservoirs. (2 Marks)",
                                "3. Canals and Locks Construction: Built Welland Canal (8 locks) to bypass Niagara Falls and Soo Locks to bypass St. Mary's Rapids. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 3: Fragmented African Railway Reasons",
                        "content": {
                            "question": "Analyze five reasons why many African countries have highly fragmented, non-integrated railway networks. (10 Marks)",
                            "strategy": "Detail colonial export partition, gauge incompatibilities, political hostility, trade patterns, and terrain capital costs.",
                            "solution": [
                                "1. Colonial Partition: Railways were built independently by rival European powers to haul raw materials straight from inland mines/farms to coastal export ports without cross-border lateral links. (2 Marks)",
                                "2. Incompatible Rail Gauges: Different colonial powers laid different track widths (Cape Gauge vs Meter Gauge vs Standard Gauge), preventing cross-border train transfers. (2 Marks)",
                                "3. Political Hostility: Post-independence border disputes and ideological conflicts between neighboring states discouraged joint railway expansion. (2 Marks)",
                                "4. Low Interstate Trade: Neighboring African nations produce similar agricultural crops and minerals, creating weak trade incentives for inter-state rail lines. (2 Marks)",
                                "5. High Capital Costs & Terrain Barriers: Massive capital required to engineer rail tracks across steep Rift Valleys, mountains, and dense swamps. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 4: Cargo Transport Mode Selection",
                        "content": {
                            "question": "An exporter needs to move 500 tons of heavy copper sheets from Eldoret to Mombasa Port, and 5 tons of fresh French beans from Eldoret to London, UK. Justify the transport mode for each cargo. (6 Marks)",
                            "strategy": "Pair cargo weight and perishability directly with rail vs air.",
                            "solution": [
                                "1. Copper Sheets (Eldoret to Mombasa): Select RAILWAY TRANSPORT. Copper is extremely heavy (500 tons) and non-perishable. Moving 500 tons 800 km by freight train yields maximum cost savings and avoids heavy highway wear. (3 Marks)",
                                "2. Fresh French Beans (Eldoret to London): Select AIR TRANSPORT. French beans are highly perishable and lightweight (5 tons). Air freight reaches London within 12 hours, preserving freshness and market value. (3 Marks)"
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps: Liners vs Tramps & Rail Gauge Errors",
                        "content": {
                            "mistake": "Confusing Ocean Liners with Ocean Tramps or stating that 'African railways were built to connect African villages'.",
                            "correction": "Liners operate along fixed schedules/routes, while Tramps charter flexibly. Colonial African railways were built strictly to extract inland resources to coastal sea ports for export to Europe.",
                            "reasoning": "In KCSE essays, candidates must emphasize the colonial export orientation of African rail networks."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Integrated Transport Strategy Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Integrated Transport Strategy Challenge",
                            "prompt": "How can African nations eliminate railway transit delays caused by different colonial rail gauges at border crossings?",
                            "options": [
                                "Option A: Adopt a standardized regional Standard Gauge Railway (1435 mm SGR) corridor under AU treaties.",
                                "Option B: Offload all train cargo onto draught donkeys at every border.",
                                "Option C: Shut down all railway lines completely."
                            ],
                            "correct_option": "Option A: Adopt a standardized regional Standard Gauge Railway (1435 mm SGR) corridor under AU treaties.",
                            "explanation": "Standardizing track widths to SGR allows freight trains to cross national borders seamlessly without offloading cargo."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 1: African River Barriers",
                        "content": {
                            "question": "Which physical barrier prevents continuous year-round river navigation in semi-arid African river basins?",
                            "options": [
                                "Seasonal volume fluctuation caused by dry-season droughts.",
                                "Excessive snow fall choking river channels.",
                                "Volcanic lava flows filling all rivers every month.",
                                "High ocean tides lifting river beds."
                            ],
                            "correct_answer": 0,
                            "explanation": "Seasonal rainfall causes river volumes to drop severely during dry seasons, grounding vessels."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 2: KCSE Exam Requirements",
                        "content": {
                            "question": "Why is air transport chosen over ocean shipping for exporting fresh cut flowers from Kenya to Europe?",
                            "options": [
                                "Cut flowers are highly perishable and require high-speed air transport to reach florists in peak condition within 12 hours.",
                                "Air freight is cheaper than ocean freight for heavy coal.",
                                "Ocean ships are banned from carrying flowers.",
                                "Airplanes do not use fuel."
                            ],
                            "correct_answer": 0,
                            "explanation": "Fresh cut flowers decay quickly; high-speed air freight ensures delivery to European markets fresh within hours."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "summary",
                        "title": "Topic 6 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 6 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Transport moves matter/people; communication transfers electronic signals across spatial channels.",
                                "Networks depend on surplus-deficit economic gradients, infrastructure quality, alternative suppliers, and state policies.",
                                "Roads offer door-to-door flexibility; railways provide long-distance bulk economy; pipelines carry fluids 24/7.",
                                "Liners sail on fixed schedules/routes; Tramps charter flexibly; Containerisation enables fast intermodal ship-to-rail transfer.",
                                "The St. Lawrence Seaway bypassed Niagara Falls via Welland Canal locks, transforming Great Lakes cities (Chicago, Detroit, Toronto) into ocean ports.",
                                "Mobile technology (M-Pesa) and subsea fiber cables (Mombasa gateway) drive African financial inclusion and trade velocity."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic6(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 6: Transport and Communication")
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

    topic_name = "Transport and Communication"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=6,
            description="Comprehensive syllabus on transport modes (road, rail, pipeline, water, air), containerisation, St. Lawrence Seaway project, telecommunications (M-Pesa, fiber optics), and African transport barriers."
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
    print("[SUCCESS] Form 4 Geography Topic 6 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_geography_topic6(replace=replace_flag)
