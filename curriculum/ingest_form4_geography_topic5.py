"""
VLearn Form 4 Geography — Topic 5: Industry
High-Structure Production Ingestion Engine

Topic: Industry (Topic Order: 5)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (80 Total Pages):
  1. Industrial Location Factors, Industrial Inertia, and Classification (12 Pages)
  2. Spatial Distribution of Kenya's Formal & Informal Sectors (Jua Kali & Cottage) (12 Pages)
  3. Industrialisation in Kenya: Significance, 11 Core Problems, and Solutions (14 Pages)
  4. Case Study 1: Cottage Industry in India & Comparative Analysis (12 Pages)
  5. Case Study 2 & 3: Germany's Ruhr Heavy Industry & Japan's High-Tech Sector (14 Pages)
  6. Industrial Synthesis, Worked KCSE Essays, and Topic Assessment (16 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic5.py [--replace]
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
    """Removes bracket citations [52], [55], [60] and cleans double spaces."""
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

def build_topic5_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 5."""
    return [
        # =====================================================================
        # LESSON 1: Industrial Location Factors, Industrial Inertia, and Classification
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Industrial Location Factors, Industrial Inertia, and Classification",
            "unit_description": "Principles of industrial location, raw materials, power, markets, industrial inertia, and three-tier industry classification.",
            "lesson_title": "Industrial Location Factors, Industrial Inertia, and Classification",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Industrial Location & Classification",
                        "content": {
                            "title": "Learning Objectives: Industrial Location & Classification",
                            "goals": [
                                "Define the terms 'industry', 'industrialisation', and 'industrialised nation'.",
                                "Analyze nine physical, human, and economic factors dictating industrial location.",
                                "Explain the crucial geographical concept of 'industrial inertia' using the German Ruhr Region.",
                                "Classify industries using three-tier taxonomy (Primary, Secondary, Tertiary) and scale of operation."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Topic 5: Industry",
                        "content": {
                            "title": "Welcome to Topic 5: Industry",
                            "text": "Industry represents the cornerstone of modern economic development, transforming raw natural resources into high-value consumer goods and services. Industrial location is governed by deliberate spatial decision-making by industrialists seeking to minimize transport costs and maximize profitability."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Geographical Definitions: Industry vs Industrialisation",
                        "content": {
                            "term": "Industry & Industrialisation",
                            "definition": "Industry refers to any economic activity through which people produce goods and services. Industrialisation is the process through which a nation builds manufacturing capacity to make manufactured goods its dominant economic activity.",
                            "key_points": [
                                "Primary Production: Extracting or initial processing of natural resources (posho mills, coffee pulp, sawmills).",
                                "Secondary Production: Manufacturing finished, consumer-ready products from semi-processed goods (cement, refineries, bakeries).",
                                "Tertiary Services: Non-tangible commercial services (banking, transport, education, tourism)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Economic Transformation through Manufacturing",
                        "content": {
                            "title": "Economic Transformation through Manufacturing",
                            "text": "Developing nations that rely heavily on exporting unprocessed raw agricultural materials suffer from fluctuating global commodity prices. Industrialisation enables domestic value addition, creating high-paying jobs and economic stability."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Industrial Location Inputs, Processes, and Market Pull Matrix",
                        "content": {
                            "title": "Industrial Location Inputs, Processes, and Market Pull Matrix",
                            "caption": "Spatial Input-Output Model Displaying How Physical Inputs, Human Factors, and Market Pull Converge on a Central Factory Node",
                            "description": "Concept web showing Raw Materials, Power, Water, Land, Skilled Labour, Capital, Government Incentives, and Market Proximity converging on a central manufacturing plant."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spatial Factors Influencing Industrial Location",
                        "content": {
                            "title": "Spatial Factors Influencing Industrial Location",
                            "text": "Industrialists analyze multiple physical and human variables before selecting a factory site:\n\n1. Raw Materials: Bulky or weight-losing raw materials force factories to locate near raw material sources to cut heavy freight costs (e.g., sugar mills in sugarcane belts).\n\n2. Bulky Imports: Factories using heavy imported materials locate at coastal sea ports (e.g., Changamwe oil refinery in Mombasa).\n\n3. Power Supply: Energy-intensive plants locate near major power stations to reduce long-distance transmission losses (e.g., Jinja industries near Owen Falls Dam)."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Market Demand, Labour, and Water Supply Factors",
                        "content": {
                            "title": "Market Demand, Labour, and Water Supply Factors",
                            "text": "4. Market Demand: Factories producing perishable goods (bread, milk) or fragile goods (glass, tiles, bricks) locate near urban consumer markets to prevent spoilage and breakage.\n\n5. Labour Supply: Labour-intensive manufacturing requires dense population centers providing cheap, abundant labor, while complex plants require highly skilled technical managers.\n\n6. Water Supply: Industries requiring massive processing or cooling water locate along permanent rivers (e.g., Mumias Sugar on River Nzoia, Sony Sugar on River Migori)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Rule: Perishability & Fragility Market Pull",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Rule: Perishability & Fragility Market Pull",
                            "text": "Fragile items like ceramic tiles or glass bottles incur severe breakage losses during rough long-distance transport, pulling factories directly to metropolitan consumer markets."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Rukuriri Tea Processing Factory in Embu, Kenya",
                        "content": {
                            "title": "Rukuriri Tea Processing Factory in Embu, Kenya",
                            "caption": "Agricultural tea processing factory located directly inside the tea-growing highlands of Embu to process green leaves immediately after picking.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/2009.12-363-1125ap_tea%2Cprocessing%28withering%29%2Cstirring_Rukuriri_Tea_Factory%2Ctea-zone_N_of_Embu%28C_Highlands%29%2CKE_mon14dec2009-1242h.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:2009.12-363-1125ap_tea,processing(withering),stirring_Rukuriri_Tea_Factory,tea-zone_N_of_Embu(C_Highlands),KE_mon14dec2009-1242h.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Raw Material Proximity in Agricultural Processing",
                        "content": {
                            "title": "Raw Material Proximity in Agricultural Processing",
                            "text": "Tea leaves begin fermenting immediately after plucking. KTDA tea factories like Rukuriri in Embu are established right inside tea farms to minimize transit time and preserve leaf quality."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Government Decentralisation Policies",
                        "content": {
                            "title": "Government Decentralisation Policies",
                            "text": "Governments actively use tax incentives, land subsidies, and protective tariffs to encourage industrialists to set up factories in rural or underdeveloped regions. This decentralisation balances regional economic growth, creates rural jobs, checks rural-urban migration, and avoids urban slum congestion (e.g., EPZ Athi River)."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Industrial Inertia Mechanics in Historic Industrial Regions",
                        "content": {
                            "title": "Industrial Inertia Mechanics in Historic Industrial Regions",
                            "caption": "Conceptual Model Explaining Why Factories Remain Locked in Original Locations Long After Initial Raw Material Resources Deplete",
                            "description": "Diagram illustrating Sunk Capital Costs, Specialized Skilled Labour Pools, and Infrastructural Lock-in anchoring heavy steel mills in Germany's Ruhr Region after coal mine closures."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Crucial Concept: Industrial Inertia",
                        "content": {
                            "title": "Crucial Concept: Industrial Inertia",
                            "text": "Industrial inertia is the tendency of an industry to remain established in a particular geographic place even when the original locating factors that drew it there no longer exist.\n\n• Primary Example: Heavy steel mills in Germany's Ruhr Region remain firmly in Essen and Duisburg despite local coal seam depletion and reliance on imported coal.\n\n• Causes: 1. High sunk capital costs (relocating massive blast furnaces is prohibitively expensive); 2. Highly specialized local skilled labor pool; 3. Well-established, pre-existing railway, canal, and power infrastructure."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Capital, Land Cost, and Investor Decisions",
                        "content": {
                            "title": "Capital, Land Cost, and Investor Decisions",
                            "text": "High land costs in metropolitan centers (Nairobi Industrial Area) act as a powerful geographic push factor, forcing new factories to relocate to satellite towns like Ruiru, Kitengela, and Athi River. Additionally, investors sometimes make personal decisions based on security or home-town philanthropy."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Exam Insight: Industrial Inertia vs Relocation",
                        "content": {
                            "type": "tip",
                            "title": "Exam Insight: Industrial Inertia vs Relocation",
                            "text": "KCSE questions frequently test why heavy industries refuse to move after raw materials run out. Always cite sunk building costs, specialized labor, and pre-existing transport networks."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Three-Tier Industrial Classification Taxonomy",
                        "content": {
                            "title": "Three-Tier Industrial Classification Taxonomy",
                            "caption": "Classification Framework Categorizing Primary Processing, Secondary Manufacturing, and Tertiary Service Sectors",
                            "description": "Taxonomy chart illustrating Primary (coffee pulping, sawmills), Secondary (cement, oil refineries, car assembly), and Tertiary (banking, transport, tourism) sectors."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Classification by Weight and Scale",
                        "content": {
                            "term": "Heavy vs Light Industries",
                            "definition": "Heavy industries use bulky raw materials, require massive capital investments, and produce heavy goods (steel rolling, shipbuilding, vehicle assembly). Light industries produce low-weight consumer goods using lighter machinery (textiles, cosmetics, electronics).",
                            "key_points": [
                                "Heavy Industry Examples: Changamwe Oil Refinery, Athi River Cement, AVA Mombasa Car Assembly.",
                                "Light Industry Examples: Ruaraka Breweries, BAT Cigarettes, Bata Shoe Company Limuru.",
                                "Service Industry Examples: KCB Banking, Matatu Transport, Maasai Mara Tourism."
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Industrial Location Decision Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Industrial Location Decision Simulator",
                            "prompt": "An industrialist plans to build a factory producing highly fragile glass bottles. Clay and sand quarries are 200 km away, while Nairobi city center has 3 million consumers. Where should the plant locate?",
                            "options": [
                                "Option A: 5 km outside Nairobi near the urban market (Fragility requires short transport to consumers).",
                                "Option B: Directly inside the sand quarry 200 km away.",
                                "Option C: In a remote desert border post."
                            ],
                            "correct_option": "Option A: 5 km outside Nairobi near the urban market (Fragility requires short transport to consumers).",
                            "explanation": "Fragile finished products incur severe breakage during long-distance transport, pulling factories close to major urban consumer markets."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Location Factors & Inertia",
                        "content": {
                            "question": "What is the primary cause of industrial inertia in heavy manufacturing regions like Germany's Ruhr Valley?",
                            "options": [
                                "High sunk capital costs in pre-existing factory plants, specialized labor, and dense transport networks.",
                                "Proximity to tropical rain forests.",
                                "Continuous discovery of new surface coal mines every year.",
                                "Complete absence of ocean shipping routes."
                            ],
                            "correct_answer": 0,
                            "explanation": "Industrial inertia occurs because massive sunk capital investments, specialized labor, and transport lock-in make relocating prohibitively expensive."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Industrial Foundations: Key Takeaways",
                        "content": {
                            "title": "Industrial Foundations: Key Takeaways",
                            "summary_points": [
                                "Industrial location is dictated by raw materials, power, transport, market demand, labor, water, and government policies.",
                                "Perishable and fragile goods are pulled to consumer markets; weight-losing raw materials pull factories to raw material sites.",
                                "Industrial inertia keeps factories locked in historic sites long after original raw materials deplete.",
                                "Industries are classified into Primary (processing), Secondary (manufacturing), and Tertiary (services), as well as Heavy vs Light."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Spatial Distribution of Kenya's Formal & Informal Sectors (Jua Kali & Cottage)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Spatial Distribution of Kenya's Formal & Informal Sectors (Jua Kali & Cottage)",
            "unit_description": "Spatial distribution of agricultural and non-agricultural industries in Kenya, Cottage sector characteristics, and Jua Kali informal sector.",
            "lesson_title": "Spatial Distribution of Kenya's Formal & Informal Sectors (Jua Kali & Cottage)",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Kenyan Industrial Distribution",
                        "content": {
                            "title": "Learning Objectives: Kenyan Industrial Distribution",
                            "goals": [
                                "Map the spatial distribution of agricultural and non-agricultural formal manufacturing in Kenya.",
                                "Examine the characteristics, products, and localization of Kenya's traditional Cottage industries.",
                                "Analyze the informal Jua Kali sector, open-air Nyayo sheds, and metal reprocessing value chains.",
                                "Evaluate five government initiatives promoting Jua Kali and its socio-economic significance."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Kenyan Industrial Dualism",
                        "content": {
                            "title": "Kenyan Industrial Dualism",
                            "text": "Kenya's industrial landscape exhibits structural dualism: formal large-scale manufacturing (concentrated in Nairobi, Mombasa, Thika, and Eldoret) operates alongside a vibrant, informal cottage and Jua Kali sector spread across both urban centers and rural villages."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Spatial Distribution Map of Kenya's Formal Manufacturing Centers",
                        "content": {
                            "title": "Spatial Distribution Map of Kenya's Formal Manufacturing Centers",
                            "caption": "Thematic Map Displaying Formal Industrial Hubs and Agricultural Processing Belts Across Kenya",
                            "description": "Map plotting Nairobi (steel, assembly, pharmaceuticals), Thika (Del Monte canning), Athi River (cement, meat), Limuru (Bata shoes), Webuye (paper), Eldoret (dairies, grain), Mombasa (refinery, cement, AVA assembly)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Spatial Pattern of Formal Manufacturing in Kenya",
                        "content": {
                            "title": "Spatial Pattern of Formal Manufacturing in Kenya",
                            "text": "1. Agricultural Food Processing: KTDA tea factories in central/rift highlands; sugar mills in Western Kenya (Mumias, Chemelil, Sony); milk dairies in Eldoret, Nakuru, Kiganjo; Del Monte fruit canning in Thika; EABL brewery at Ruaraka.\n\n2. Agricultural Non-Food: Bata Shoe Company in Limuru; Webuye Paper Mills near Turbo pine forests; Kisumu Cotton Mills (KICOMI).\n\n3. Non-Agricultural Heavy Industries: Athi River & Bamburi Cement; Changamwe Oil Refinery in Mombasa; Kasarani Central Glass; General Motors Nairobi car assembly."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Raw Material Clustering of Agro-Industries",
                        "content": {
                            "title": "Raw Material Clustering of Agro-Industries",
                            "text": "Agricultural processing factories must locate close to farms to process perishable harvests immediately. Sugarcane loses sucrose rapidly after cutting, requiring sugar mills to sit within 30 km of farms."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Geographical Insight: Changamwe Refinery Location",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Insight: Changamwe Refinery Location",
                            "text": "Crude petroleum is an extremely bulky imported raw material. Refining it at Changamwe in Mombasa avoids transporting heavy crude inland before fractionating it into light fuels."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Non-Agricultural Heavy Manufacturing Clusters",
                        "content": {
                            "title": "Non-Agricultural Heavy Manufacturing Clusters",
                            "text": "Heavy non-agricultural factories cluster in Nairobi and Mombasa to access dense urban labor markets, high-voltage power lines, container rail terminals, and massive local consumer demand."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Informal Jua Kali Fabricator Sheds in Kenya",
                        "content": {
                            "title": "Informal Jua Kali Fabricator Sheds in Kenya",
                            "caption": "Informal Jua Kali metal fabricators reprocessing scrap metal under open-air Nyayo sheds in an urban Kenyan workshop.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cottage Industries in Kenya",
                        "content": {
                            "title": "Cottage Industries in Kenya",
                            "text": "Cottage industries manufacture goods in homes or small workshops using hands and simple tools. Key characteristics include reliance on local raw materials, minimal invested capital, family/informal labor, small output volume, and unique artistic craftsmanship."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "definition_card",
                        "title": "Characteristics of Cottage & Jua Kali Sectors",
                        "content": {
                            "term": "Cottage vs Jua Kali Industry",
                            "definition": "Cottage industries are small, home-based craft enterprises utilizing local raw materials and simple tools. The Jua Kali sector represents Kenya's broader informal artisanal economy working in open-air sheds.",
                            "key_points": [
                                "Pottery & Ceramics: Clay pots and vases made in Murang'a and Kwale.",
                                "Wood & Stone Carving: Akamba wood carvings in Machakos/Kitui; Kisii soapstone carvings.",
                                "Weaving & Basketry: Agikuyu sisal Ciondos and coastal palm-leaf mats/baskets.",
                                "Jua Kali Reprocessing: Converting scrap oil drums into metal boxes, wheelbarrows, gutters, and Jiko stoves."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Types and Geography of Kenyan Cottage Crafts",
                        "content": {
                            "title": "Types and Geography of Kenyan Cottage Crafts",
                            "text": "Kenyan cottage crafts are geographically localized:\n\n• Kisii Soapstone: Carved from soft metamorphic soapstone in Tabaka, Kisii, forming high-value tourist exports.\n• Machakos Wood Carving: Akamba artisans carve hardwood wildlife souvenirs.\n• Ciondo Basketry: Sisal fiber weaving practiced by rural women's groups in Central and Eastern Kenya."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Jua Kali Reprocessed Cooking Pots",
                        "content": {
                            "title": "Jua Kali Reprocessed Cooking Pots",
                            "caption": "Durable, low-cost aluminum cooking pots manufactured by Jua Kali artisans from recycled scrap metals.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_cooking_pots.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Informal Jua Kali Sector Mechanics",
                        "content": {
                            "title": "The Informal Jua Kali Sector Mechanics",
                            "text": "The Jua Kali sector ('under the hot sun') encompasses shoe repairers, tailors, carpenters, mechanics, and metal artisans working in informal open-air sheds across every Kenyan town. Its core activity is metal reprocessing—turning discarded iron sheets, steel drums, and wire into cheap, durable household goods."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Informal Jua Kali Metal Reprocessing Value Chain",
                        "content": {
                            "title": "Informal Jua Kali Metal Reprocessing Value Chain",
                            "caption": "Resource Recovery Flow: Scrap Metal Collection → Nyayo Shed Cold Hammering → Metal Box/Jiko Fabrication → COMESA Regional Export",
                            "description": "Flowchart showing discarded scrap steel collection, manual cutting/cold hammering in Nyayo sheds, fabrication into metal boxes, Jikos, wheelbarrows, and distribution to local/COMESA markets."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Government Support for the Jua Kali Sector",
                        "content": {
                            "title": "Government Support for the Jua Kali Sector",
                            "text": "Recognizing Jua Kali's massive job-creation capacity, the Kenyan government supports it through five key initiatives:\n\n1. Ministry Department: Dedicated informal sector department in the Ministry of Trade & Industry.\n2. Financial Loans: Kenya Industrial Estates (KIE) provides micro-credit to buy tools.\n3. Nyayo Sheds: KIE constructs protective metal sheds for low-rent artisan work.\n4. Land Allocation: Municipalities set aside public land for informal workshops.\n5. Cooperatives: Artisans form marketing SACCOs to buy raw materials and export goods."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "concept_explanation",
                        "title": "Socio-Economic Significance of Jua Kali",
                        "content": {
                            "title": "Socio-Economic Significance of Jua Kali",
                            "text": "• Job Creation: Absorbs millions of youth, curbing urban unemployment and poverty.\n• Resource Recovery: Recycler of industrial scrap metal and waste tires.\n• Affordable Consumer Goods: Delivers low-cost, durable tools to low-income households.\n• Foreign Exchange: Exports items to regional COMESA markets (Uganda, Rwanda, South Sudan)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Environmental Role: Industrial Waste Recycling",
                        "content": {
                            "type": "tip",
                            "title": "Environmental Role: Industrial Waste Recycling",
                            "text": "Jua Kali artisans recycle over 60% of Kenya's metallic scrap waste, preventing urban environmental pollution while generating wealth from discarded trash."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Kenya's Formal & Jua Kali Sectors",
                        "content": {
                            "question": "Which government agency in Kenya provides micro-credit loans and constructs protective open-air 'Nyayo Sheds' for Jua Kali artisans?",
                            "options": [
                                "Kenya Industrial Estates (KIE)",
                                "National Environment Management Authority (NEMA)",
                                "Kenya Revenue Authority (KRA)",
                                "Kenya Ports Authority (KPA)"
                            ],
                            "correct_answer": 0,
                            "explanation": "Kenya Industrial Estates (KIE) provides cheap credit and constructs permanent Nyayo sheds to support informal Jua Kali artisans."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Kenyan Industrial Distribution: Key Takeaways",
                        "content": {
                            "title": "Kenyan Industrial Distribution: Key Takeaways",
                            "summary_points": [
                                "Agro-processing plants (tea, sugar, milk, canning) cluster inside farming regions to process perishable raw crops.",
                                "Heavy non-agricultural factories (cement, oil refining, steel, car assembly) concentrate in Nairobi and Mombasa.",
                                "Cottage crafts utilize local raw materials (Kisii soapstone, Machakos wood carvings, Agikuyu ciondos).",
                                "The informal Jua Kali sector reprocesses scrap metal into metal boxes, Jiko stoves, and wheelbarrows under KIE Nyayo sheds."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Industrialisation in Kenya: Significance, 11 Core Problems, and Solutions
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Industrialisation in Kenya: Significance, 11 Core Problems, and Solutions",
            "unit_description": "Economic importance of manufacturing, 11 primary structural problems facing Kenyan industrialisation, and source-grounded geographical solutions.",
            "lesson_title": "Industrialisation in Kenya: Significance, 11 Core Problems, and Solutions",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Industrialisation Barriers & Solutions",
                        "content": {
                            "title": "Learning Objectives: Industrialisation Barriers & Solutions",
                            "goals": [
                                "Analyze eleven economic benefits of industrialisation to Kenya's national economy.",
                                "Examine eleven structural problems hindering manufacturing growth in Kenya.",
                                "Formulate source-grounded geographical solutions for capital, raw material, energy, and market bottlenecks.",
                                "Master the KCSE distinction between problem causes and economic consequences."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Imperative for Industrialisation",
                        "content": {
                            "title": "The Imperative for Industrialisation",
                            "text": "Industrialisation is essential for Kenya to transition from a low-income agrarian economy into a prosperous industrial nation. Expanding manufacturing generates foreign exchange, creates employment, and stabilizes national revenue against agricultural droughts."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Eleven Dimensions of Industrial Significance",
                        "content": {
                            "title": "Eleven Dimensions of Industrial Significance",
                            "text": "1. Foreign Exchange Earnings: Exporting manufactured tea, cement, and textiles earns foreign currency.\n2. Employment Creation: Absorbs job seekers into steady wage manufacturing.\n3. Infrastructure Stimulus: Spurs all-weather roads, electricity grids, and water systems.\n4. Agricultural Linkage: Creates a reliable market for raw farm produce, raising rural farm incomes.\n5. Economic Diversification: Buffers national revenue against agricultural crop failures.\n6. SACCO Development: Industrial worker SACCOs pool savings to provide affordable credit."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Macroeconomic Linkage: Balance of Trade",
                        "content": {
                            "type": "tip",
                            "title": "Macroeconomic Linkage: Balance of Trade",
                            "text": "Manufacturing domestic goods reduces expensive foreign imports while increasing export values, helping correct Kenya's chronic balance of trade deficit."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Macroeconomic Linkages of Industrialisation in Developing Economies",
                        "content": {
                            "title": "Macroeconomic Linkages of Industrialisation in Developing Economies",
                            "caption": "Inter-Sectoral Economic Linkages Connecting Agriculture, Manufacturing, SACCO Capital, and Infrastructure",
                            "description": "Flowchart showing Farm Produce -> Agro-Factory -> Manufactured Exports -> Foreign Exchange -> SACCO Savings -> Infrastructure & Urban Growth."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Inter-Sectoral Linkages",
                        "content": {
                            "title": "Inter-Sectoral Linkages",
                            "text": "Manufacturing does not exist in isolation. It creates powerful forward and backward linkages: purchasing raw crops from farmers (backward linkage) and supplying packaged food, clothing, and construction cement to markets (forward linkage)."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Commercial Heavy Industrial Cement Kiln Operations",
                        "content": {
                            "title": "Commercial Heavy Industrial Cement Kiln Operations",
                            "caption": "Massive rotary cement kiln factory demonstrating heavy manufacturing infrastructure in Kenya.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Cement_kiln_in_Gorazdze_Cement_plant.JPG",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Cement_kiln_in_Gorazdze_Cement_plant.JPG"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Heavy Manufacturing Infrastructure",
                        "content": {
                            "title": "Heavy Manufacturing Infrastructure",
                            "text": "Heavy plants like Athi River and Bamburi Cement process raw limestone rock in giant rotary kilns, supplying essential construction material for Kenya's building sector."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "The 11 Industrial Bottlenecks & Strategic Policy Intervention Matrix",
                        "content": {
                            "title": "The 11 Industrial Bottlenecks & Strategic Policy Intervention Matrix",
                            "caption": "Comparative Dual Matrix Mapping 11 Structural Manufacturing Problems to Source-Grounded Geographical Solutions",
                            "description": "Dual-column matrix pairing problems (Capital shortage, Mitumba competition, High energy costs, Brain drain, Pollution) with solutions (Tax incentives, EAC trade, Geothermal grid, TVETs, Waste laws)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Analyzing Kenya's 11 Industrial Problems & Solutions",
                        "content": {
                            "title": "Analyzing Kenya's 11 Industrial Problems & Solutions",
                            "text": "1. Inadequate Capital: Lenders charge high interest rates → Government offers investor tax exemptions and affordable credit.\n2. Raw Material Shortage: Droughts cause crop failures → Import raw inputs and enforce catchment afforestation.\n3. Limited Market: Low local purchasing power → Expand into EAC/COMESA regional trade blocks and lower import tariffs on raw inputs."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Problems 4–6: Brain Drain, Import Competition, and Energy Costs",
                        "content": {
                            "title": "Problems 4–6: Brain Drain, Import Competition, and Energy Costs",
                            "text": "4. Shortage of Skilled Labour (Brain Drain): Skilled managers migrate abroad → Establish TVET institutes and improve local salaries.\n5. Competition from Cheap Imports / Mitumba: Second-hand clothes cripple textile mills → Impose protective import tariffs and curb customs smuggling.\n6. High Energy Costs: Volatile imported crude inflates factory running costs → Develop cheap domestic geothermal, solar, and HEP grids."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Problems 7–9: Environmental Degradation, Agricultural Neglect, Unemployment",
                        "content": {
                            "title": "Problems 7–9: Environmental Degradation, Agricultural Neglect, Unemployment",
                            "text": "7. Environmental Degradation: Toxic smoke and chemical effluents pollute air/water → Enact strict NEMA effluent laws and rehabilitate open quarry pits.\n8. Neglect of Agriculture: Youth abandon farms for factory jobs → Offer high, guaranteed food crop prices and educate farmers.\n9. Technological Unemployment: Factory automation replaces manual labor → Retrain retrenched workers for self-employed Jua Kali enterprises."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Policy Defense: Protecting Domestic Textiles",
                        "content": {
                            "type": "warning",
                            "title": "Policy Defense: Protecting Domestic Textiles",
                            "text": "Massive imports of cheap second-hand clothes (mitumba) caused the collapse of Kisumu Cotton Mills (KICOMI) and Rivatex in Eldoret during the 1990s, highlighting the need for protective tariffs."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Problems 10–11: Displacement & Rural-Urban Migration",
                        "content": {
                            "title": "Problems 10–11: Displacement & Rural-Urban Migration",
                            "text": "10. Population Displacement: Mining and factory sites force compulsory relocation → Fairly compensate and resettle displaced families in planned towns.\n11. Uncontrolled Rural-Urban Migration: Concentrating factories in Nairobi creates urban slums → Offer tax incentives for rural-based industries and provide rural electricity."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Industrial Decentralisation & Urban-Rural Rebalancing",
                        "content": {
                            "title": "Industrial Decentralisation & Urban-Rural Rebalancing",
                            "caption": "Spatial Model Demonstrating How EPZ Zones and Tax Incentives Divert Factories to Rural Counties",
                            "description": "Diagram illustrating factory push away from congested Nairobi to satellite EPZ zones in Athi River, Ruiru, and Kitengela, reducing urban slum growth."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Geography of Industrial Decentralisation",
                        "content": {
                            "title": "The Geography of Industrial Decentralisation",
                            "text": "Decentralisation diverts new factories to rural towns (e.g., Athi River EPZ, Mariakani steel), spreading infrastructure, creating regional employment, and reducing urban slum pressure in capital cities."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Mistake: Cause vs Effect",
                        "content": {
                            "mistake": "Writing that 'rural-urban migration is a problem facing factories'.",
                            "correction": "Rural-urban migration is a social consequence of urban factory concentration. A real problem facing factories is 'high energy costs from imported crude oil inflating production costs'.",
                            "reasoning": "In KCSE essays, always describe the bottleneck that directly impairs factory production or market competitiveness."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Industrial Policy Bottleneck Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Industrial Policy Bottleneck Challenge",
                            "prompt": "Kenya's textile mills are shutting down because cheap imported second-hand clothes (mitumba) flood local markets. Which geographical policy solution is most effective?",
                            "options": [
                                "Option A: Impose protective import tariffs on foreign second-hand clothes while offering tax rebates to local textile mills.",
                                "Option B: Close down all local cotton farms.",
                                "Option C: Import more finished clothes from Asia."
                            ],
                            "correct_option": "Option A: Impose protective import tariffs on foreign second-hand clothes while offering tax rebates to local textile mills.",
                            "explanation": "Protective tariffs raise import prices of foreign clothes, allowing local textile mills like Rivatex to sell competitively and create jobs."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Industrialisation Barriers & Solutions",
                        "content": {
                            "question": "How does expanding domestic geothermal energy at Olkaria directly solve a major problem facing Kenyan industrialisation?",
                            "options": [
                                "It provides cheap, reliable, domestic renewable power, reducing factory reliance on expensive imported crude oil.",
                                "It forces all factories to move to Lake Naivasha.",
                                "It eliminates the need for any industrial labor.",
                                "It stops foreign trade with COMESA countries."
                            ],
                            "correct_answer": 0,
                            "explanation": "Geothermal power offers cheap domestic base-load electricity, directly lowering factory energy bills and reducing reliance on volatile imported petroleum."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "summary",
                        "title": "Kenyan Industrialisation: Key Takeaways",
                        "content": {
                            "title": "Kenyan Industrialisation: Key Takeaways",
                            "summary_points": [
                                "Industrialisation earns foreign exchange, creates jobs, builds infrastructure, and balances national trade deficits.",
                                "Major bottlenecks include capital shortages, brain drain, Mitumba import competition, high energy costs, and raw material instability.",
                                "Geographical solutions include tax incentives, COMESA trade expansion, TVET technical training, protective tariffs, and geothermal power.",
                                "Industrial decentralisation spreads factories to rural counties via EPZ zones, curbing urban slum migration."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Case Study 1: Cottage Industry in India & Comparative Analysis
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Case Study 1: Cottage Industry in India & Comparative Analysis",
            "unit_description": "India's cottage industry model, spatial clusters, favorable factors, problems, and 6-point comparative matrix with Kenya.",
            "lesson_title": "Case Study 1: Cottage Industry in India & Comparative Analysis",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: India Cottage Case Study",
                        "content": {
                            "title": "Learning Objectives: India Cottage Case Study",
                            "goals": [
                                "Examine the geographical distribution and major clusters of cottage industries across India.",
                                "Analyze nine favorable factors driving India's rural cottage industry success.",
                                "Identify key problems facing Indian artisans, including middleman exploitation.",
                                "Execute a 6-point comparative analysis comparing India's cottage sector with Kenya's Jua Kali sector."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "India's Model Cottage Industry Network",
                        "content": {
                            "title": "India's Model Cottage Industry Network",
                            "text": "India possesses one of the world's most highly developed, ubiquitous cottage industry systems. Operating primarily out of rural village homes, millions of artisan families produce high-value hand-woven textiles, brassware, ivory carvings, and hand-knotted carpets."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Spatial Cluster Map of India's Cottage Industry Networks",
                        "content": {
                            "title": "Spatial Cluster Map of India's Cottage Industry Networks",
                            "caption": "Distribution of Major Cottage Industrial Clusters Across Coastal and Inland Provinces of India",
                            "description": "Map plotting Mumbai, Jabalpur, Nagpur, Bhopal, Madras, Calcutta, Bangalore, Lucknow, and Moradabad cottage craft centers."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographic Context & Key Industrial Centers",
                        "content": {
                            "title": "Geographic Context & Key Industrial Centers",
                            "text": "India's cottage industries are widespread across the subcontinent:\n\n• Key Centers: Mumbai, Jabalpur, Nagpur, Bhopal, Madras (Chennai), Calcutta (Kolkata), Bangalore, Lucknow, and Moradabad.\n• Dominant Products: Hand-loom cotton/silk weaving, brass/copper/silver metalware, ivory carvings, jewelry, hand-knotted carpets, and safety matches."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_image",
                        "title": "Traditional Handloom Weaving Workshop Setup in India",
                        "content": {
                            "title": "Traditional Handloom Weaving Workshop Setup in India",
                            "caption": "Rural Indian weavers operating wooden handlooms inside a village home workshop.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Handloom_weaving_setup.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Handloom_weaving_setup.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Favourable Factors for India's Cottage Industry",
                        "content": {
                            "title": "Favourable Factors for India's Cottage Industry",
                            "text": "1. Low Capital Requirement: Home workshops require very small financial investment.\n2. Ancient Family Heritage Skills: Specialized hand-weaving and metalwork skills passed down through generations.\n3. Massive Domestic Market: A population of over 1.4 billion creates huge local demand for household goods.\n4. Abundant Cheap Labour: Endless supply of affordable family labor.\n5. Widespread Rural Electricity: Well-distributed HEP grids connect rural village workshops."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Raw Materials, Simple Tools, and Income Motivation",
                        "content": {
                            "title": "Raw Materials, Simple Tools, and Income Motivation",
                            "text": "Plentiful local supplies of raw cotton, wool, silk, and copper combine with simple, easily maintained hand tools to make cottage manufacturing highly viable across rural Indian villages."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Cultural Heritage: Generation Specialization",
                        "content": {
                            "type": "tip",
                            "title": "Cultural Heritage: Generation Specialization",
                            "text": "Unlike Kenya where Jua Kali skills are learned informally in urban sheds, Indian cottage skills (such as Kashmir carpet knotting) are ancient family heritages taught from childhood."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Artisanal Silk Saree Handloom Weaving in India",
                        "content": {
                            "title": "Artisanal Silk Saree Handloom Weaving in India",
                            "caption": "An artisan weaving intricate silk sarees on a traditional wooden loom in an Indian cottage workshop.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Saree_Weaving_by_Handloom_2.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Saree_Weaving_by_Handloom_2.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Problems Facing India's Cottage Sector",
                        "content": {
                            "title": "Problems Facing India's Cottage Sector",
                            "text": "• High Raw Material Costs: Artisans struggle to buy quality yarn and metals.\n• Factory Competition: Cheap, mass-produced machine goods undermine hand-made items.\n• Middleman Exploitation: Traders supply expensive raw materials and buy finished items at very low prices, trapping weavers in debt. Solution: Establish artisan marketing cooperatives."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Middleman Exploitation vs Cooperative Marketing in Cottage Industries",
                        "content": {
                            "title": "Middleman Exploitation vs Cooperative Marketing in Cottage Industries",
                            "caption": "Disintermediation Model Contrasting Middleman Price Exploitation with Direct Artisan Cooperative Marketing",
                            "description": "Flowchart comparing traditional Middleman System (High Raw Material Price -> Low Buying Price -> Poor Artisan) with Cooperative System (Bulk Buying -> Direct Market Export -> High Artisan Profit)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Cooperative Disintermediation Solutions",
                        "content": {
                            "title": "Cooperative Disintermediation Solutions",
                            "text": "Forming artisan cooperatives eliminates predatory middlemen, allowing Indian weavers to buy raw cotton at wholesale prices and sell finished sarees directly to government handloom emporiums."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Six-Point Comparative Matrix: Indian Rural Cottage vs Kenyan Urban Jua Kali",
                        "content": {
                            "title": "Six-Point Comparative Matrix: Indian Rural Cottage vs Kenyan Urban Jua Kali",
                            "caption": "Structured Comparative Framework Contrasting Spatial Distribution, Skill Origins, Labor Units, Ownership, Ubiquity, and Raw Material Procurement",
                            "description": "Comparative matrix comparing India (strictly rural, ancient family skills, family unit, single family owned, ubiquitous in every home, middleman dependent) with Kenya (rural & urban, variable informal skills, individual/group unit, individual/cooperative owned, urban shed concentrated, direct scrap sourcing)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Structural Comparison: Cottage Industry in India vs Kenya",
                        "content": {
                            "headers": ["Comparison Criteria", "Cottage Industry in India", "Cottage / Jua Kali Industry in Kenya"],
                            "rows": [
                                ["Spatial Distribution", "Strictly rural-based; spread widely across all villages", "Located in both urban and rural areas (heavy urban concentration)"],
                                ["Skill Origins", "Ancient family heritage skills passed down generations", "Variable skills acquired informally through apprenticeships"],
                                ["Labour Unit", "Labour provided strictly by members of a single family", "Labour provided by individuals or group cooperatives"],
                                ["Ownership", "Workshops owned and managed by single families", "Workshops owned by individual artisans or cooperatives"],
                                ["Ubiquity (Presence)", "Highly ubiquitous; present in almost every village home", "Concentrated in urban open-air sheds (Nyayo sheds)"],
                                ["Raw Material Source", "Heavily dependent on trading middlemen for materials", "Artisans procure scrap metal directly from scrap yards"]
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rigorous Analysis of Similarities (India vs Kenya)",
                        "content": {
                            "title": "Rigorous Analysis of Similarities (India vs Kenya)",
                            "text": "• Low Capital Requirements: Both Indian cottage workshops and Kenyan Jua Kali sheds require minimal financial investment.\n• Local Raw Material Reliance: Both use local inputs (cotton/wool in India; scrap metal/clay in Kenya).\n• Manual Tools: Both rely heavily on hand labor and basic physical tools."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Rigorous Analysis of Differences (India vs Kenya)",
                        "content": {
                            "title": "Rigorous Analysis of Differences (India vs Kenya)",
                            "text": "• Spatial Distribution: India's cottage industry is strictly rural-based across villages, whereas Kenya's Jua Kali sector is heavily urban-concentrated in towns.\n• Specialization: Indian artisans possess ancient generation-long family skills, while Kenyan artisans learn informally."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive India vs Kenya Comparative Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive India vs Kenya Comparative Challenge",
                            "prompt": "How does raw material procurement differ between a traditional handloom weaver in India and a Jua Kali metal fabricator in Nairobi?",
                            "options": [
                                "Option A: Indian weavers rely heavily on middlemen traders, whereas Kenyan Jua Kali artisans buy scrap metal directly from scrap yards.",
                                "Option B: Indian weavers import scrap iron from Kenya.",
                                "Option C: Both sectors buy raw materials exclusively from foreign state monopolies."
                            ],
                            "correct_option": "Option A: Indian weavers rely heavily on middlemen traders, whereas Kenyan Jua Kali artisans buy scrap metal directly from scrap yards.",
                            "explanation": "Indian weavers rely on middlemen for cotton yarn, whereas Kenyan Jua Kali artisans source scrap iron directly from local collectors."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: India vs Kenya Cottage Comparison",
                        "content": {
                            "question": "Which spatial characteristic distinguishes India's cottage industry from Kenya's Jua Kali sector?",
                            "options": [
                                "India's cottage industry is strictly rural-based and ubiquitous across villages, whereas Kenya's Jua Kali is concentrated in urban towns.",
                                "Kenya's Jua Kali sector only operates in foreign ocean ships.",
                                "India's cottage industry only uses modern computer robotics.",
                                "Kenyan Jua Kali artisans only work inside family homes."
                            ],
                            "correct_answer": 0,
                            "explanation": "India's cottage sector is strictly rural and home-based, whereas Kenya's Jua Kali sector is heavily urban-concentrated in open-air town sheds."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Cottage Industry Comparative Analysis: Key Takeaways",
                        "content": {
                            "title": "Cottage Industry Comparative Analysis: Key Takeaways",
                            "summary_points": [
                                "India's cottage sector is driven by ancient family heritage skills, low capital, abundant rural labor, and widespread rural HEP.",
                                "Key Indian products include handloom textiles, brassware, ivory carvings, and hand-knotted carpets across Mumbai, Lucknow, and Moradabad.",
                                "Major Indian problems include middleman price exploitation, solved by forming artisan marketing cooperatives.",
                                "Comparing India and Kenya reveals similarities in low capital and local materials, but differences in rural ubiquity vs urban shed concentration."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Case Study 2 & 3: Germany's Ruhr Heavy Industry & Japan's High-Tech Sector
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Case Study 2 & 3: Germany's Ruhr Heavy Industry & Japan's High-Tech Sector",
            "unit_description": "Germany's Ruhr Valley heavy iron/steel industry, Japan's high-tech car & electronics sector, and global comparative synthesis.",
            "lesson_title": "Case Study 2 & 3: Germany's Ruhr Heavy Industry & Japan's High-Tech Sector",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Germany & Japan Industrial Models",
                        "content": {
                            "title": "Learning Objectives: Germany & Japan Industrial Models",
                            "goals": [
                                "Analyze the physical, mineral, and waterway factors favoring heavy steel industry in Germany's Ruhr Region.",
                                "Examine the geographic push factors forcing Japan to specialize in high-tech car and electronics manufacturing.",
                                "Evaluate major industrial belts in Germany (Essen, Duisburg) and Japan (Tokyo-Yokohama, Nagoya, Toyota City).",
                                "Construct a three-way comparative matrix synthesizing industrial structures in Kenya, Germany, and Japan."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Global Industrial Models: Heavy vs High-Tech",
                        "content": {
                            "title": "Global Industrial Models: Heavy vs High-Tech",
                            "text": "Germany's Ruhr Region represents the global gold standard for heavy iron and steel manufacturing powered by rich coal seams and river canals. Conversely, Japan represents a high-tech automated manufacturing model driven by computer robotics."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Navigable Waterway Network Supporting the German Ruhr Heavy Region",
                        "content": {
                            "title": "Navigable Waterway Network Supporting the German Ruhr Heavy Region",
                            "caption": "Hydrological Transport Infrastructure: Rivers Rhine, Ruhr, Lippe, and the Dortmund-Ems Canal Connecting Heavy Industrial Cities",
                            "description": "Map displaying River Rhine, River Ruhr, River Lippe, Dortmund-Ems Canal, and major steel cities Duisburg, Essen, and Dortmund."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Germany's Ruhr Region Heavy Industry",
                        "content": {
                            "title": "Germany's Ruhr Region Heavy Industry",
                            "text": "The Ruhr Region along River Ruhr (tributary of River Rhine) is Europe's premier heavy industrial zone:\n\n• Favourable Factors: 1. Massive coal, iron ore, and limestone deposits; 2. Dense navigable river/canal transport (R. Rhine, R. Ruhr, R. Lippe, Dortmund-Ems Canal); 3. Central European market; 4. Wealthy domestic capital investment."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Waterway Efficiency in Ruhr Transport",
                        "content": {
                            "title": "Waterway Efficiency in Ruhr Transport",
                            "text": "Heavy coal, iron ore, and finished steel plates are exceptionally bulky. Transporting them on barges along deep, navigable canals reduces freight costs by 70% compared to overland rail."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Duisburg Ruhr Blast Furnace Complex in Germany",
                        "content": {
                            "title": "Duisburg Ruhr Blast Furnace Complex in Germany",
                            "caption": "Historic heavy blast furnace steel infrastructure in Duisburg within Germany's Ruhr Industrial Region.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Duisburg%2C_Landschaftspark_Duisburg-Nord_--_2016_--_1238-44.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Duisburg,_Landschaftspark_Duisburg-Nord_--_2016_--_1238-44.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Economic Impact & Inertia in the Ruhr",
                        "content": {
                            "title": "Economic Impact & Inertia in the Ruhr",
                            "text": "Ruhr steel stimulated rapid urbanization (Essen, Dortmund, Duisburg) and infrastructure growth. Although domestic coal seams are now depleted, industrial inertia locks steel mills in Duisburg due to pre-existing canals and skilled labor."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Blast Furnace Iron & Steel Smelting Process Flow",
                        "content": {
                            "title": "Blast Furnace Iron & Steel Smelting Process Flow",
                            "caption": "Chemical & Mechanical Transformation: Iron Ore + Coal Coke + Limestone → Blast Furnace → Pig Iron → Steel Rolling Mill",
                            "description": "Flowchart showing raw material inputs (iron ore, coal coke, limestone), blast furnace hot air reaction, molten pig iron extraction, oxygen converter, and steel rolling mill."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Modern Ruhr Challenges & Environmental Pollution",
                        "content": {
                            "title": "Modern Ruhr Challenges & Environmental Pollution",
                            "text": "Heavy coal smelting caused severe sulfur smoke air pollution and river contamination. Depletion of shallow coal seams forces deep underground mining, raising domestic coal costs and requiring imported coal."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "callout",
                        "title": "Geographical Case Study: Duisburg Inland Port",
                        "content": {
                            "type": "tip",
                            "title": "Geographical Case Study: Duisburg Inland Port",
                            "text": "Duisburg is the world's largest inland river port, handling millions of tons of steel and coal barges connecting the Ruhr directly to Rotterdam sea port."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Geographic Push Factor: Japan's 80% Mountainous Archipelago",
                        "content": {
                            "title": "Geographic Push Factor: Japan's 80% Mountainous Archipelago",
                            "caption": "Spatial Relief Profile: Rugged Volcanic Mountains Forcing High-Tech Coastal Manufacturing Concentration",
                            "description": "Cross-section showing 80% rugged volcanic mountain interior restricting agriculture, pushing cities and automated car/electronics plants to narrow coastal plains."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Japan's High-Tech Car & Electronics Model",
                        "content": {
                            "title": "Japan's High-Tech Car & Electronics Model",
                            "text": "Japan is a mountainous volcanic archipelago (Hokkaido, Honshu, Kyushu, Shikoku). Because 80% of its land is steep mountains restricting farming, Japan was geographically forced to focus on high-tech manufacturing:\n\n• Key Factors: 1. Advanced computer robotics automation; 2. Fuel-efficient car design; 3. Highly educated, disciplined labor; 4. Deep-water coastal ports (Tokyo, Yokohama, Nagoya) for sea exports."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_image",
                        "title": "Automated Robotic Car Assembly Manufacturing Plant",
                        "content": {
                            "title": "Automated Robotic Car Assembly Manufacturing Plant",
                            "caption": "Advanced computer-controlled robotic arms assembling automobile chassis on an automated manufacturing line in Japan.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/6/67/BMW_Leipzig_MEDIA_050719_Download_Karosseriebau_max.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:BMW_Leipzig_MEDIA_050719_Download_Karosseriebau_max.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Robotic Automation & Fuel Efficiency",
                        "content": {
                            "title": "Robotic Automation & Fuel Efficiency",
                            "text": "Automated robotic assembly lines guarantee zero defect rates and low unit costs. Japanese automakers (Toyota, Honda, Nissan) dominate global markets by manufacturing highly fuel-efficient cars."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Spatial Industrial Belts of Japan: Tokyo-Yokohama, Osaka-Kobe, Nagoya",
                        "content": {
                            "title": "Spatial Industrial Belts of Japan: Tokyo-Yokohama, Osaka-Kobe, Nagoya",
                            "caption": "Thematic Map of Japan's Pacific Coastal Industrial Corridor Displaying Premier Car and Electronics Zones",
                            "description": "Map plotting Tokyo-Yokohama (Hitachi electronics), Osaka-Kobe, and Nagoya zone (Toyota Motor Corp HQ in Chiru City)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Japan's Premier Industrial Zones",
                        "content": {
                            "title": "Japan's Premier Industrial Zones",
                            "text": "1. Tokyo-Yokohama Belt: Leading motor vehicle and Hitachi electronics hub.\n2. Osaka-Kobe Belt: Major industrial zone on Honshu Island.\n3. Nagoya Belt: Toyota Motor Corporation headquarters located in Chiru City, 20 km east of Nagoya."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Global Case Study Decision Matrix",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Global Case Study Decision Matrix",
                            "prompt": "Why did Japan prioritize high-tech car and electronics manufacturing over large-scale commercial agriculture?",
                            "options": [
                                "Option A: 80% of Japan consists of rugged volcanic mountains, severely restricting arable farm land and pushing the nation into high-tech manufacturing.",
                                "Option B: Japan has no access to sea ports.",
                                "Option C: Japanese workers refused to use computers."
                            ],
                            "correct_option": "Option A: 80% of Japan consists of rugged volcanic mountains, severely restricting arable farm land and pushing the nation into high-tech manufacturing.",
                            "explanation": "Rugged volcanic terrain (80% mountainous) limited arable agriculture, forcing Japan to leverage high-tech robotic manufacturing for wealth."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Germany & Japan Industrial Models",
                        "content": {
                            "question": "Where is the global headquarters of Toyota Motor Corporation located within Japan's industrial geography?",
                            "options": [
                                "Chiru City, 20 km east of Nagoya",
                                "Sapporo, Hokkaido Island",
                                "Hiroshima City",
                                "Sendai Port"
                            ],
                            "correct_answer": 0,
                            "explanation": "Toyota Motor Corporation has its global manufacturing headquarters in Chiru City, situated 20 km east of Nagoya."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Global Case Studies: Key Takeaways",
                        "content": {
                            "title": "Global Case Studies: Key Takeaways",
                            "summary_points": [
                                "Germany's Ruhr Valley heavy iron/steel industry was built on rich coal seams, iron ore, and navigable river canals (Rhine, Ruhr, Lippe).",
                                "Industrial inertia keeps Ruhr steel mills in Duisburg and Essen despite domestic coal seam depletion.",
                                "Japan's 80% mountainous terrain restricted farming, pushing the nation into computer-robotic car (Toyota) and electronics (Hitachi) manufacturing.",
                                "Japan's main industrial belts line the Pacific coast (Tokyo-Yokohama, Osaka-Kobe, Nagoya)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Industrial Synthesis, Worked KCSE Essays, and Topic Assessment
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Industrial Synthesis, Worked KCSE Essays, and Topic Assessment",
            "unit_description": "Global three-way comparative synthesis (Kenya vs Germany vs Japan), worked KCSE essay models, and topic revision assessment.",
            "lesson_title": "Industrial Synthesis, Worked KCSE Essays, and Topic Assessment",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Industrial Synthesis & KCSE Exam Mastery",
                        "content": {
                            "title": "Learning Objectives: Industrial Synthesis & KCSE Exam Mastery",
                            "goals": [
                                "Synthesize structural differences between Kenya, Germany (Ruhr), and Japan industrial systems.",
                                "Master KCSE essay writing strategies for industrial location, inertia, and comparative questions.",
                                "Examine six strategic national policy interventions to accelerate Kenyan industrialisation.",
                                "Complete comprehensive end-of-topic revision exams."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Global Industrial Synthesis",
                        "content": {
                            "title": "Global Industrial Synthesis",
                            "text": "Comparing Kenya's agro-processing and Jua Kali sector with Germany's heavy Ruhr steel mills and Japan's automated car robotics highlights how natural resource endowments, physical terrain, and human capital shape national industrial profiles."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Three-Way Global Industrial Structure Comparison: Kenya vs Germany vs Japan",
                        "content": {
                            "title": "Three-Way Global Industrial Structure Comparison: Kenya vs Germany vs Japan",
                            "caption": "Comparative Tripartite Model Contrasting Dominant Industries, Energy Sources, Transport Modes, and Technological Levels",
                            "description": "Comparative matrix contrasting Kenya (Agro-processing & Jua Kali, Geothermal/HEP, Roads, Manual/semi-automated) with Germany (Heavy steel/coal, Coal/Gas, Canals/Rail, Heavy mechanical) and Japan (High-tech cars/electronics, Imported oil/HEP, Deep sea ports, Automated robotics)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Three-Way Comparative Matrix: Kenya vs Germany vs Japan",
                        "content": {
                            "headers": ["Feature", "Kenya's Manufacturing", "Germany's Ruhr Region", "Japan's High-Tech Sector"],
                            "rows": [
                                ["Dominant Industry", "Agricultural Processing & Jua Kali", "Heavy Iron, Coal, and Steel", "Automobiles & High-Tech Electronics"],
                                ["Primary Energy Source", "Geothermal & Hydroelectric (HEP)", "Coal, imported Gas, and HEP", "Hydroelectric & imported Oil"],
                                ["Terrain Factor", "Highland plains favor crop processing", "Navigable river valleys favor heavy barge transport", "80% mountainous terrain forced high-tech focus"],
                                ["Technological Level", "Low-to-moderate; highly manual in Jua Kali", "Moderate-to-high; heavy mechanical blast furnaces", "Super-advanced; automated robotics & computers"],
                                ["Primary Export Markets", "EAC & COMESA regional blocks", "European Union & global heavy steel markets", "Worldwide global exports (USA, Europe, Africa)"]
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Terrain, Energy, and Technology Synthesis",
                        "content": {
                            "title": "Terrain, Energy, and Technology Synthesis",
                            "text": "• Kenya leverages fertile highland soils for agricultural raw inputs.\n• Germany leverages flat, navigable river valleys (Rhine/Ruhr) to move heavy mineral ores.\n• Japan leverages deep-water ocean ports to import raw materials and export high-tech robotic cars."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Six-Point National Strategy for Sustainable Kenyan Industrialisation",
                        "content": {
                            "title": "Six-Point National Strategy for Sustainable Kenyan Industrialisation",
                            "caption": "Hexagonal Policy Framework: Geothermal Expansion, Solar Subsidies, TVET Training, EPZ Zones, EAC Trade, and Jiko Stoves",
                            "description": "Hexagonal framework illustrating 1. Geothermal steam expansion; 2. Zero-tax solar kits; 3. Wind power corridors; 4. River Tana catchment afforestation; 5. BRT transit buses; 6. Ceramic Jiko stove adoption."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Six-Point National Strategy for Kenyan Industrialisation",
                        "content": {
                            "title": "Six-Point National Strategy for Sustainable Kenyan Industrialisation",
                            "text": "To achieve Vision 2030 industrial goals, Kenya must execute six strategic actions: 1. Expand Olkaria geothermal power; 2. Subsidize off-grid solar; 3. Develop TVET technical skills; 4. Protect local textile mills with import tariffs; 5. Expand EPZ decentralisation zones; 6. Support Jua Kali cooperatives."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Comparative Essay Strategy: Step-by-Step Model Reasoning",
                        "content": {
                            "question": "Compare the factors that have influenced the development of the cottage industry in Kenya and India. (12 Marks)",
                            "strategy": "Structure your answer by clearly stating 3 similarities and 3 differences grounded strictly in source facts.",
                            "solution": [
                                "Similarities:\n1. Low Capital: Cottage workshops in both Kenya and India require very little capital to establish. (2 Marks)\n2. Local Materials: Both rely heavily on locally available raw inputs (sisal/scrap in Kenya; cotton/wood in India). (2 Marks)\n3. Manual Labour: Both rely on hand labor and simple tools. (2 Marks)\n\nDifferences:\n4. Spatial Distribution: India's cottage industry is strictly rural-based across villages, whereas Kenya's Jua Kali sector is concentrated in urban towns. (2 Marks)\n5. Skill Origins: Indian artisans possess ancient family heritage skills passed down generations, whereas Kenyan artisans acquire skills informally. (2 Marks)\n6. Raw Material Sourcing: Indian weavers rely on middlemen, whereas Kenyan Jua Kali artisans buy scrap directly from scrap yards. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 1: Industrial Location & Inertia",
                        "content": {
                            "question": "(a) Define industrial inertia. (2 Marks)\n(b) Explain three reasons why steel mills in Germany's Ruhr Region remain in Essen despite local coal depletion. (6 Marks)",
                            "strategy": "Define inertia precisely and cite sunk capital costs, specialized labor, and canal infrastructure.",
                            "solution": [
                                "(a) Industrial inertia is the tendency of an industry to remain established in a place even after the original locating factors no longer exist. (2 Marks)",
                                "(b) 1. High Sunk Costs: Moving massive blast furnaces and steel rolling mills is prohibitively expensive. (2 Marks)\n2. Specialized Labour: The region has a highly experienced, deeply specialized local steel workforce. (2 Marks)\n3. Pre-existing Infrastructure: Dense navigable canals (Rhine, Ruhr, Lippe) and railways provide cheap transport for imported coal. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 2: Kenya Jua Kali Sector Support",
                        "content": {
                            "question": "Describe three ways in which the government of Kenya supports the informal Jua Kali sector. (6 Marks)",
                            "strategy": "State exact government structures (KIE, Ministry department, Nyayo sheds, public land).",
                            "solution": [
                                "1. Financial Credit: Kenya Industrial Estates (KIE) provides affordable micro-credit loans to artisans to buy tools. (2 Marks)",
                                "2. Physical Infrastructure: KIE constructs permanent open-air Nyayo sheds at low rental rates for artisans. (2 Marks)",
                                "3. Land Allocation & Ministry Support: Municipalities allocate public land for workshops, and a dedicated department in the Ministry of Trade promotes informal artisans. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 3: Ruhr Heavy Steel Development Factors",
                        "content": {
                            "question": "Explain four physical and economic factors that favored heavy steel manufacturing in the Ruhr Region of Germany. (8 Marks)",
                            "strategy": "Detail raw minerals, navigable canals, central market, and domestic capital.",
                            "solution": [
                                "1. Abundant Minerals: Rich local deposits of coal, iron ore, and limestone provided raw smelting inputs. (2 Marks)",
                                "2. Navigable Waterways: Rivers Rhine, Ruhr, Lippe, and Dortmund-Ems Canal allowed cheap barge transport for heavy ores. (2 Marks)",
                                "3. Large Ready Market: Centrally located in dense, wealthy European consumer populations. (2 Marks)",
                                "4. Domestic Capital: Wealthy German industrial banks and coal profits supplied capital for massive blast furnaces. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 4: Kenya Industrial Bottlenecks & Solutions",
                        "content": {
                            "question": "Explain three major problems facing industrialisation in Kenya and suggest one geographical solution for each. (6 Marks)",
                            "strategy": "Pair each bottleneck directly with a valid policy solution.",
                            "solution": [
                                "1. High Energy Costs: Volatile imported crude inflates running costs → Develop cheap domestic geothermal power at Olkaria. (2 Marks)",
                                "2. Cheap Import Competition: Foreign second-hand clothes cripple textile mills → Impose protective import tariffs and curb customs smuggling. (2 Marks)",
                                "3. Shortage of Skilled Managers: Brain drain forces expensive expatriate hiring → Establish TVET technical institutes and improve salaries. (2 Marks)"
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps: Cause vs Effect & Classification Errors",
                        "content": {
                            "mistake": "Classifying a Posho Mill as Secondary Manufacturing or confusing Cause and Effect in essay answers.",
                            "correction": "Posho mills perform initial processing of raw maize (Primary Processing). Secondary manufacturing creates finished goods from pre-processed materials (Cement, Paper).",
                            "reasoning": "In KCSE exams, precise categorization of primary vs secondary industries is required for full marks."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Industrial Strategy Policy Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Industrial Strategy Policy Challenge",
                            "prompt": "As Cabinet Secretary for Industrialisation, how should you solve the problem of high factory production costs caused by expensive electricity?",
                            "options": [
                                "Option A: Expand domestic geothermal power generation at Olkaria to deliver cheap, reliable base-load electricity.",
                                "Option B: Import expensive diesel generators for every factory.",
                                "Option C: Shut down all manufacturing plants."
                            ],
                            "correct_option": "Option A: Expand domestic geothermal power generation at Olkaria to deliver cheap, reliable base-load electricity.",
                            "explanation": "Geothermal power offers cheap domestic base-load electricity, directly lowering factory running costs and boosting competitiveness."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 1: Global Comparative Synthesis",
                        "content": {
                            "question": "Which physical factor forced Japan to specialize in high-tech car and electronics manufacturing rather than commercial agriculture?",
                            "options": [
                                "80% of Japan consists of rugged volcanic mountains, severely restricting arable farm land.",
                                "Japan has no fresh water lakes.",
                                "Japan's climate is too hot for any human activity.",
                                "Japan has no sea access."
                            ],
                            "correct_answer": 0,
                            "explanation": "Japan's rugged volcanic mountain terrain (80% of land) restricted agriculture, forcing the country into high-tech manufacturing."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint 2: KCSE Essay Requirements",
                        "content": {
                            "question": "When answering a KCSE 'Compare' question on cottage industries in Kenya and India, what must your answer contain?",
                            "options": [
                                "Both explicit similarities and explicit differences between the two countries.",
                                "Only a map of Kenya.",
                                "Only complaints about high taxes.",
                                "Only definitions of heavy steel mills."
                            ],
                            "correct_answer": 0,
                            "explanation": "KCSE 'Compare' questions strictly require candidates to present both similarities and differences between the two regions."
                        }
                    }
                ],
                # Page 14
                [
                    {
                        "type": "summary",
                        "title": "Topic 5 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 5 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Industrial location is governed by raw materials, power, markets, labor, water, and government policies.",
                                "Industrial inertia anchors heavy steel mills in Germany's Ruhr Valley long after coal depletion due to sunk costs and canal networks.",
                                "Kenya's industrial sector combines formal agro-processing (tea, sugar, dairies) with informal Jua Kali metal reprocessing in KIE Nyayo sheds.",
                                "India's cottage sector is strictly rural and home-based with ancient family skills, while Kenya's Jua Kali sector is urban shed concentrated.",
                                "Japan's 80% mountainous terrain forced high-tech car (Toyota) and computer-robotic electronics manufacturing."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic5(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 5: Industry")
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

    topic_name = "Industry"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=5,
            description="Comprehensive syllabus on industrial location factors, industrial inertia, classification, Kenya formal & Jua Kali sectors, and comparative case studies (India, Germany Ruhr, Japan)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic5_curriculum()
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
    print("[SUCCESS] Form 4 Geography Topic 5 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_geography_topic5(replace=replace_flag)
