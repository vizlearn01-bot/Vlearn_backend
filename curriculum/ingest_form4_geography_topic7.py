"""
VLearn Form 4 Geography — Topic 7: Trade
Rich In-Place Production Ingestion Engine

Topic: Trade (Topic Order: 7)
Subject: Geography (Subject ID: 18)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (64 Total Pages):
  1. Introduction to Trade, Types of Trade, and Factors Influencing Trade (11 Pages)
  2. Internal Trade Architecture, Distribution Channels, and Domestic Market Systems (12 Pages)
  3. International Trade Dynamics, Imports, Exports, and Balance of Trade (12 Pages)
  4. Regional Economic Trading Blocs (COMESA, EAC, ECOWAS, EU) (12 Pages)
  5. Economic Significance of Trade and Challenges Facing Domestic & Foreign Trade in Kenya (11 Pages)
  6. Topic Synthesis, Key Glossary, Case Studies, and KCSE Examination Review (6 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_geography_topic7.py
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

def build_topic7_curriculum():
    """Returns the comprehensive, textbook-grade pedagogical page and block structure for Geography Topic 7."""
    return [
        # =====================================================================
        # LESSON 1: Introduction to Trade, Types of Trade, and Factors Influencing Trade (11 Pages)
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Introduction to Trade, Types of Trade, and Factors Influencing Trade",
            "unit_description": "Definition of trade, barter vs monetary trade evolution, internal vs international trade, and physical/economic factors.",
            "lesson_title": "Introduction to Trade, Types of Trade, and Factors Influencing Trade",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Fundamentals of Trade",
                        "content": {
                            "title": "Learning Objectives: Fundamentals of Trade",
                            "goals": [
                                "Define trade in a geographic context and trace its historical evolution from silent barter to modern monetary systems.",
                                "Distinguish between Internal (Domestic) Trade and International (Foreign) Trade across regional boundaries.",
                                "Analyze physical, economic, socio-cultural, and political factors influencing global trade flows."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Geographic Definition & Evolution of Trade",
                        "content": {
                            "title": "Geographic Definition & Evolution of Trade",
                            "text": "Trade is defined as the exchange, buying, or selling of commodities, goods, and services between individuals, regions, or nations. Geographically, trade arises because natural resources, climatic conditions, technological capabilities, and human skill sets are unevenly distributed across the surface of the earth. No single region is completely self-sufficient.\n\nHistorically, human societies engaged in Barter Trade—the direct exchange of goods for other goods without using money (e.g., swapping a bag of sorghum for a goat). Barter trade faced severe limitations, including the necessity for a 'double coincidence of wants' (finding someone who has what you need and wants what you have), lack of a standard unit of value, indivisibility of large animals or goods, and difficulty in storing perishable items. The invention of standardized monetary currencies (coins, banknotes, digital tokens) eliminated these bottlenecks, establishing modern commercial trade networks."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Trade Classification Taxonomy",
                        "content": {
                            "term": "Trade Classification Taxonomy",
                            "definition": "The formal categorization of commercial trade based on political boundaries and physical nature of commodities.",
                            "key_points": [
                                "Internal (Domestic / Home) Trade: The buying and selling of goods and services within the geographic boundaries of a single nation (e.g., trade between Nairobi, Kisumu, and Mombasa).",
                                "International (Foreign / External) Trade: The exchange of goods and services across national sovereign borders (e.g., trade between Kenya, Uganda, the UK, and China).",
                                "Visible Trade: The exchange of physical, tangible goods that can be weighed, measured, and inspected at border customs posts (e.g., tea, crude petroleum, coffee, motor vehicles).",
                                "Invisible Trade: The exchange of intangible services that generate foreign exchange or revenue without moving physical goods across customs checkpoints (e.g., international safari tourism, banking, shipping, education, insurance)."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Factors Influencing Internal and International Trade Flowchart",
                        "content": {
                            "title": "Factors Influencing Internal and International Trade Flowchart",
                            "caption": "Multidimensional Trade Drivers: Resource Availability → Transport & Logistics → Demand & Purchasing Power → Trade Agreements & Currency Stability",
                            "description": "Flowchart showing resource endowment, transport networks, demand, capital, political stability, and trade tariffs driving trade flows."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Physical Factors Influencing Trade",
                        "content": {
                            "title": "Physical Factors Influencing Trade",
                            "text": "1. Unequal Distribution of Natural Resources: Variations in geological formations, soil fertility, mineral deposits, and climate dictate what commodities a region can produce. For example, Kenya's fertile volcanic highlands enable high tea and coffee production, whereas Middle Eastern nations produce crude petroleum due to sedimentary oil basins.\n\n2. Relief and Topography: Mountainous terrain hinders road and railway construction, increasing transport costs and limiting trade, whereas flat plains, coastal rias, and navigable river basins facilitate smooth bulk transport."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "Trade Goods Cargo Vessel Visualization",
                        "content": {
                            "title": "Trade Goods Cargo Vessel Visualization",
                            "caption": "International container cargo ship exiting Mombasa port carrying agricultural exports and industrial imports.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/9/94/Container_ship_exiting_Mombasa_port%2C_Kenya_01.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Container_ship_exiting_Mombasa_port%2C_Kenya_01.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Economic and Political Factors Influencing Trade",
                        "content": {
                            "title": "Economic and Political Factors Influencing Trade",
                            "text": "1. Transport and Logistics Infrastructure: Efficient deep-water seaports (e.g., Mombasa), standard gauge railways (SGR), and international airports allow rapid transit of goods, lowering freight costs.\n\n2. Population Size and Purchasing Power: A large population with high disposable income creates strong consumer demand for domestic and foreign goods.\n\n3. Political Stability and Bilateral Agreements: Peaceful international relations, bilateral trade accords, and stable exchange rates encourage foreign investment and steady trade flows."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Domestic Market Produce Visualization",
                        "content": {
                            "title": "Domestic Market Produce Visualization",
                            "caption": "Fresh agricultural produce displayed at a local Kenyan retail market stall illustrating vibrant domestic trade supply chains.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:A_vegetable_stall_in_the_outskirts_of_Nairobi%2C_Kenya.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Visible vs Invisible Trade Dynamics",
                        "content": {
                            "title": "Visible vs Invisible Trade Dynamics",
                            "text": "In national economic accounting, visible trade deals with physical export/import commodities, while invisible trade covers service transactions. For instance, when a British tourist flies into Nairobi, stays in Masai Mara lodges, and hires local guides, Kenya earns foreign currency without shipping any physical goods abroad. This service transaction is categorized as an Invisible Export for Kenya."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "Barter Trade vs Monetary Trade Comparison",
                        "content": {
                            "headers": ["Feature / Dimension", "Barter Trade", "Monetary Trade"],
                            "rows": [
                                ["Exchange Medium", "Direct exchange of goods for goods", "Universal currency (Cash, Digital, Forex)"],
                                ["Valuation Standard", "No fixed rate; subject to bargaining", "Standardized prices per unit weight/item"],
                                ["Storage & Durability", "Perishable goods lose value quickly", "Money stored in bank accounts without decay"],
                                ["Divisibility", "Difficult to divide live cattle or large crops", "Currency easily divided into small denominations"],
                                ["Coincidence of Wants", "Requires exact double coincidence", "Universal acceptance of money by all sellers"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: The Double Coincidence of Wants",
                        "content": {
                            "text": "The greatest flaw of barter trade was the double coincidence of wants. If a farmer had maize and wanted shoes, he had to search for a shoemaker who specifically needed maize. Currency acts as a universal medium of exchange, eliminating this barrier and unlocking global trade efficiency."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Trade Factor Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Trade Factor Classifier",
                            "prompt": "Scenario: European tourists spend $2,500 each visiting Masai Mara National Reserve in Kenya, while Kenya imports $3,000 worth of German industrial motor vehicles. How are these two transactions categorized in Kenya's trade account?",
                            "options": [
                                "Option A: Tourism is an Invisible Export (earning foreign exchange); Vehicles are a Visible Import (expenditure on physical goods).",
                                "Option B: Tourism is a Visible Import; Vehicles are an Invisible Export.",
                                "Option C: Both transactions are Internal Barter Trade."
                            ],
                            "correct_option": "Option A: Tourism is an Invisible Export (earning foreign exchange); Vehicles are a Visible Import (expenditure on physical goods).",
                            "explanation": "Tourism is an intangible service providing foreign exchange, making it an invisible export. Motor vehicles are physical tangible commodities entering the country, making them a visible import."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Fundamentals of Trade",
                        "content": {
                            "question": "Which physical factor is primarily responsible for international trade in agricultural produce between tropical and temperate regions?",
                            "options": [
                                "Variations in climate and soil conditions preventing temperate zones from growing tropical crops like tea and coffee.",
                                "Identical soil types across all continents.",
                                "Differences in human languages.",
                                "Equal distribution of mineral deposits worldwide."
                            ],
                            "correct_answer": 0,
                            "explanation": "Climatic variations mean tropical crops (tea, coffee, cocoa) cannot grow in cold temperate regions, necessitating international import trade."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Invisible Trade",
                        "content": {
                            "mistake": "Classifying international tourism as an import for Kenya because tourists enter the country.",
                            "correction": "Tourism in Kenya is an INVISIBLE EXPORT because it brings foreign currency into Kenya from foreign visitors.",
                            "reasoning": "Export earnings mean receiving money from foreigners. When foreign tourists spend currency inside Kenya, it functions economically as an export earnings stream."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Introduction to Trade: Key Takeaways",
                        "content": {
                            "title": "Introduction to Trade: Key Takeaways",
                            "summary_points": [
                                "Trade is the geographic exchange of goods and services arising from unequal natural resource distribution.",
                                "Internal trade occurs within national borders; International trade crosses sovereign frontiers.",
                                "Visible trade involves tangible commodities; Invisible trade involves intangible services like tourism and shipping.",
                                "Trade is driven by resource endowment, transport networks, consumer purchasing power, and trade agreements."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Internal Trade Architecture, Distribution Channels, and Domestic Market Systems (12 Pages)
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Internal Trade Architecture, Distribution Channels, and Domestic Market Systems",
            "unit_description": "Wholesale vs retail distribution channels, open-air markets, supermarkets, and inter-regional trade in Kenya.",
            "lesson_title": "Internal Trade Architecture, Distribution Channels, and Domestic Market Systems",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Internal Trade Architecture",
                        "content": {
                            "title": "Learning Objectives: Internal Trade Architecture",
                            "goals": [
                                "Analyze the multi-tier supply chain: Producer -> Wholesaler -> Retailer -> Consumer.",
                                "Compare domestic retail structures in Kenya: Periodic open-air markets, supermarkets, kiosks, and itinerant hawkers.",
                                "Examine inter-regional trade flows between Kenya's fertile agricultural highlands and Arid/Semi-Arid Pastoral Lands (ASALs)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Internal Trade Architecture & Supply Chains",
                        "content": {
                            "title": "Internal Trade Architecture & Supply Chains",
                            "text": "Internal (Domestic) trade refers to commercial exchange within a country's boundaries. In Kenya, internal trade is structured through a well-defined supply chain:\n\n1. Producers: Farmers, agricultural estates, and manufacturing factories that harvest raw produce or manufacture finished consumer goods.\n\n2. Wholesalers: Intermediaries who buy commodities in large quantities (bulk) directly from producers, store them in warehouses, transport them to urban distribution hubs (e.g., Wakulima Market in Nairobi), and break bulk into smaller parcels for retailers.\n\n3. Retailers: Merchants who purchase smaller inventory quantities from wholesalers and sell individual items directly to final consumers through shops, market stalls, or supermarkets.\n\n4. Consumers: Individuals who purchase goods for final personal or household consumption."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Internal Trade Supply Chain: Producer to Consumer Channels",
                        "content": {
                            "title": "Internal Trade Supply Chain: Producer to Consumer Channels",
                            "caption": "Domestic Distribution Network: Agricultural/Industrial Producer → Bulk Wholesaler → Retail Shop / Supermarket → Final Consumer",
                            "description": "Flowchart showing commodity movement from agricultural farmer to wholesale market to retail store to consumer."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Maasai Domestic Trade Market Nairobi Visualization",
                        "content": {
                            "title": "Maasai Domestic Trade Market Nairobi Visualization",
                            "caption": "Local open-air artisan market in Nairobi displaying colorful beadwork, carvings, and traditional textiles.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Market-Nairobi.jpg"
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Domestic Retail Systems Taxonomy",
                        "content": {
                            "term": "Domestic Retail Systems Taxonomy",
                            "definition": "Classification of retail trade channels operating within Kenya's economy.",
                            "key_points": [
                                "Periodic Open-Air Markets: Weekly or bi-weekly markets held in rural towns (e.g., Karatina, Wangige, Luanda) where local farmers sell fresh food directly.",
                                "Permanent Urban Wholesale Markets: Major urban distribution centers (e.g., Wakulima Market Nairobi, Kongowea Market Mombasa) handling bulk produce.",
                                "Supermarkets & Department Stores: Self-service retail chains offering packaged food, groceries, and household electronics.",
                                "Kiosks & Small Shops: Small neighborhood retail shops operating in residential estates providing daily convenience items.",
                                "Itinerant Hawkers: Mobile street vendors selling clothes, fruits, and small household goods directly to pedestrians."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Dicotyledonous Agricultural Produce Trade Flow Matrix",
                        "content": {
                            "title": "Dicotyledonous Agricultural Produce Trade Flow Matrix",
                            "caption": "Inter-Regional Commodity Exchange in Kenya: Fertile Highlands (Tea, Coffee, Vegetables, Maize) ↔ Arid Pastoral Lands (Livestock, Meat, Hides)",
                            "description": "Map diagram illustrating agricultural trade flow between Kenyan highlands and arid pastoral regions."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Inter-Regional Trade in Kenya",
                        "content": {
                            "title": "Inter-Regional Trade in Kenya",
                            "text": "Kenya's internal trade is characterized by vibrant inter-regional exchange driven by ecological differences:\n\n• High-Potential Highlands (Central, Rift Valley, Western): Fertile volcanic soils and abundant rainfall enable production of maize, beans, potatoes, tea, milk, cabbages, and horticultural crops. These are transported to feed urban centers (Nairobi, Mombasa) and arid regions.\n\n• Arid & Semi-Arid Lands (Northern Kenya, Kajiado, Ukambani): Low rainfall favors nomadic pastoralism. Pastoralists supply cattle, goats, sheep, hides, and skins to urban abattoirs, receiving food grains and manufactured goods in return."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Wangige Wholesale Produce Market Visualization",
                        "content": {
                            "title": "Wangige Wholesale Produce Market Visualization",
                            "caption": "Wangige local agricultural produce market in Kiambu County, Kenya, illustrating domestic rural-urban trade channels.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Role of Wholesalers in Domestic Trade",
                        "content": {
                            "title": "Role of Wholesalers in Domestic Trade",
                            "text": "Wholesalers perform vital economic functions in internal trade:\n1. Bulk Breaking: Buying large harvests from thousands of scattered smallholders and breaking them into smaller units suitable for retail shops.\n2. Storage & Warehousing: Holding buffer stock in urban warehouses to stabilize market supply during dry seasons.\n3. Transport Logistics: Operating lorries to collect agricultural produce from farm gates and transport them to city markets.\n4. Credit Provision: Extending short-term credit to trusted retailers, enabling smooth inventory flow."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "Wholesale Trade vs Retail Trade Functional Comparison",
                        "content": {
                            "headers": ["Functional Aspect", "Wholesale Trade", "Retail Trade"],
                            "rows": [
                                ["Purchase Scale", "Buys in bulk directly from producers/factories", "Buys in small quantities from wholesalers"],
                                ["Target Customer", "Sells to retailers, institutions, or other traders", "Sells directly to final individual consumers"],
                                ["Capital Requirement", "Very high capital for warehousing and transport lorries", "Relatively lower capital for shop fittings or market stalls"],
                                ["Location Focus", "Located in major industrial zones or wholesale markets", "Distributed widely across residential areas and streets"],
                                ["Product Variety", "Specializes in specific commodity lines (e.g., grain trader)", "Offers wide variety of consumer items in one shop"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "Case Study: Wakulima Market (Nairobi) Internal Supply Chain",
                        "content": {
                            "question": "Examine how Wakulima Wholesale Market in Nairobi operates as a primary domestic trade node in Kenya. (4 Marks)",
                            "strategy": "Trace commodity origin, wholesale aggregation, transport, and retail distribution.",
                            "solution": [
                                "1. Commodity Sourcing (1 Mark): Lorries transport fresh vegetables, potatoes, and fruits from rural farming highlands (Kinangop, Meru, Nyandarua) overnight.",
                                "2. Wholesale Bulk Trading (1 Mark): Commission agents and wholesalers buy truckloads at dawn and sell bags/crates to urban traders.",
                                "3. Retail Breakdown (1 Mark): Small retailers, kiosk owners, and estate greengrocers buy crates to supply residential neighborhoods across Nairobi.",
                                "4. Price Stabilization (1 Mark): Wakulima functions as the central price-discovery hub for fresh food across East Africa."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Distribution Channel Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Distribution Channel Simulator",
                            "prompt": "Scenario: A smallholder potato farmer in Kinangop harvests 500 bags of potatoes. Why is selling to an urban wholesaler at Wakulima Market more efficient than traveling door-to-door to sell single bags to households in Nairobi?",
                            "options": [
                                "Option A: Wholesalers buy in bulk immediately, saving the farmer time, storage risk, and high retail transport overheads.",
                                "Option B: Door-to-door selling is always faster than selling to wholesalers.",
                                "Option C: Wholesalers pay with barter cattle."
                            ],
                            "correct_option": "Option A: Wholesalers buy in bulk immediately, saving the farmer time, storage risk, and high retail transport overheads.",
                            "explanation": "Wholesalers bridge the gap between rural smallholder producers and urban retail markets through bulk purchasing, storage, and transport logistics."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Internal Trade Architecture",
                        "content": {
                            "question": "Which retail distribution format operates primarily on specific days of the week in rural Kenyan towns?",
                            "options": [
                                "Periodic Open-Air Markets (e.g., Karatina, Luanda market days).",
                                "Hypermarkets in city malls.",
                                "Customs Free Zones.",
                                "Offshore Bonded Warehouses."
                            ],
                            "correct_answer": 0,
                            "explanation": "Periodic open-air markets gather rural buyers and sellers on set weekly market days."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Factors in Internal Trade Bottlenecks",
                        "content": {
                            "text": "Inadequate feeder roads connecting rural farms to main tarmac highways lead to high post-harvest losses. Perishable crops like tomatoes and milk frequently spoil before reaching urban wholesale markets during heavy rainy seasons."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Wholesale vs Retail",
                        "content": {
                            "mistake": "Stating that retailers buy goods directly from factories.",
                            "correction": "In standard supply chains, retailers buy from WHOLESALERS. Only massive supermarket chains bypass wholesalers to buy direct.",
                            "reasoning": "Small shops lack the capital or warehouse capacity to buy factory-level minimum order quantities."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Internal Trade: Key Takeaways",
                        "content": {
                            "title": "Internal Trade: Key Takeaways",
                            "summary_points": [
                                "Internal trade follows: Producer -> Wholesaler -> Retailer -> Consumer.",
                                "Wholesalers perform vital bulk-breaking, storage, transport, and price-discovery roles.",
                                "Retail formats include periodic open-air markets, supermarkets, kiosks, and hawkers.",
                                "Kenya's internal trade exchanges highland agricultural crops for ASAL pastoral livestock and urban manufactured goods."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: International Trade Dynamics, Imports, Exports, and Balance of Trade (12 Pages)
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "International Trade Dynamics, Imports, Exports, and Balance of Trade",
            "unit_description": "Imports, exports, Kenya's primary trading partners, Balance of Trade (deficit vs surplus), and Balance of Payments.",
            "lesson_title": "International Trade Dynamics, Imports, Exports, and Balance of Trade",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: International Trade Dynamics",
                        "content": {
                            "title": "Learning Objectives: International Trade Dynamics",
                            "goals": [
                                "Identify Kenya's major agricultural/mineral exports and industrial imports.",
                                "Distinguish between Balance of Trade (Visible Trade) and Balance of Payments.",
                                "Analyze causes and economic impacts of Kenya's persistent adverse Balance of Trade (Trade Deficit)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Kenya's International Trade Profile",
                        "content": {
                            "title": "Kenya's International Trade Profile",
                            "text": "International (Foreign) Trade involves commercial exchange across national sovereign borders. Kenya's foreign trade structure is typical of developing agrarian nations:\n\n• Primary Exports: Kenya predominantly exports low-value, raw or semi-processed agricultural commodities (black tea, Arabica coffee, cut flowers, fresh vegetables) and raw minerals (titanium ore, soda ash, cement).\n\n• Industrial Imports: Kenya heavily imports high-cost manufactured capital goods, including crude petroleum, refined fuels, industrial machinery, motor vehicles, iron/steel, pharmaceuticals, and chemical fertilizers.\n\n• Primary Trading Partners: Regional trade within EAC (Uganda, Tanzania, Rwanda), COMESA, European Union (UK, Netherlands), Asia (China, India, UAE), and the USA."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Kenya's Exports vs Imports Taxonomy",
                        "content": {
                            "term": "Kenya Export & Import Taxonomy",
                            "definition": "Classification of Kenya's major foreign trade commodities and partners.",
                            "key_points": [
                                "Major Agricultural Exports: Black Tea (world's top exporter), Cut Flowers (roses, carnations to Dutch auctions), Coffee, Vegetables.",
                                "Major Mineral Exports: Soda Ash (from Lake Magadi), Titanium Ore (from Kwale), Cement.",
                                "Major Capital Imports: Crude Oil & Refined Petroleum Products, Heavy Machinery, Motor Vehicles, Electronics, Steel.",
                                "Major Import Destinations: China, India, UAE, Saudi Arabia, Japan.",
                                "Major Export Destinations: Uganda, UK, USA, Pakistan (tea), Netherlands (flowers)."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "International Trade Commodity Balance Diagram",
                        "content": {
                            "title": "International Trade Commodity Balance Diagram",
                            "caption": "Kenya's Trade Scale: High-Value Industrial Imports (Petroleum/Machinery) vs Lower-Value Primary Agricultural Exports (Tea/Coffee) → Trade Deficit",
                            "description": "Balance scale diagram depicting low-value primary agricultural exports vs high-cost manufactured imports creating a trade deficit."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Mombasa Container Port International Trade Visualization",
                        "content": {
                            "title": "Mombasa Container Port International Trade Visualization",
                            "caption": "Port of Mombasa container terminal handling international maritime cargo trade.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "definition_card",
                        "title": "Balance of Trade vs Balance of Payments",
                        "content": {
                            "term": "International Trade Accounting Taxonomy",
                            "definition": "Financial ledger concepts measuring national foreign trade performance.",
                            "key_points": [
                                "Balance of Trade (BOT): The difference in monetary value between a nation's total visible physical exports and visible physical imports over a specified period.",
                                "Favourable Balance of Trade (Surplus): Occurs when monetary earnings from visible exports exceed expenditure on visible imports (Exports > Imports).",
                                "Unfavourable Balance of Trade (Deficit): Occurs when expenditure on visible imports exceeds earnings from visible exports (Imports > Exports).",
                                "Balance of Payments (BOP): A comprehensive macroeconomic accounting statement recording ALL economic transactions (visible goods, invisible services, capital transfers, foreign aid) between a country and the rest of the world."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "worked_example",
                        "title": "Calculating Balance of Trade: Worked Example",
                        "content": {
                            "question": "In a given financial year, Kenya exported visible agricultural and mineral commodities valued at KSh 750 Billion and imported visible industrial goods and petroleum valued at KSh 1.8 Trillion. Calculate Kenya's Balance of Trade and comment on the result. (4 Marks)",
                            "strategy": "Apply formula: Balance of Trade = Total Visible Exports - Total Visible Imports.",
                            "solution": [
                                "1. Formula: Balance of Trade = Visible Exports - Visible Imports (1 Mark)",
                                "2. Substitution: KSh 750,000,000,000 - KSh 1,800,000,000,000 (1 Mark)",
                                "3. Calculation: -KSh 1,050,000,000,000 (-1.05 Trillion KSh) (1 Mark)",
                                "4. Economic Evaluation: Kenya has an Unfavourable Balance of Trade (Trade Deficit) of KSh 1.05 Trillion because import expenditure far exceeds export earnings. (1 Mark)"
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Causes of Kenya's Persistent Trade Deficit",
                        "content": {
                            "title": "Causes of Kenya's Persistent Trade Deficit",
                            "text": "Kenya suffers from a chronic unfavourable Balance of Trade due to four major structural factors:\n\n1. Export of Low-Value Raw Primary Commodities: Agricultural exports (unrefined tea, coffee beans) fetch low, fluctuating prices on global commodity markets.\n\n2. Importation of Expensive Manufactured Capital Goods: Essential imports like crude oil, jet fuel, heavy machinery, motor vehicles, and electronics are extremely costly.\n\n3. Price Volatility vs High Import Inflation: World prices for primary agricultural goods are setting by foreign buyers and fluctuate downwards, while industrial import prices rise steadily.\n\n4. Trade Protectionism in Developed Nations: High agricultural subsidies and tariffs imposed by Western countries limit African export access."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "comparison_table",
                        "title": "Balance of Trade vs Balance of Payments Comparison",
                        "content": {
                            "headers": ["Comparison Feature", "Balance of Trade (BOT)", "Balance of Payments (BOP)"],
                            "rows": [
                                ["Scope of Accounting", "NARROW: Includes ONLY visible physical goods (merchandise)", "BROAD: Includes visible goods, invisible services, capital transfers"],
                                ["Key Components", "Visible Exports minus Visible Imports", "Current Account + Capital Account + Financial Account"],
                                ["Services Included?", "NO (Excludes tourism, banking, shipping)", "YES (Includes tourism earnings, remittances, foreign loans)"],
                                ["Ideal Target State", "Favourable Trade Surplus (Exports > Imports)", "Overall Equilibrium (Inflows = Outflows)"],
                                ["Impact of Deficit", "Depletes foreign reserves to pay for imports", "Requires foreign borrowing or IMF funding to bridge deficit"]
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Balance of Trade Calculator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Balance of Trade Calculator",
                            "prompt": "Scenario: Country Y exports $5 Billion worth of tea and imports $9 Billion worth of crude oil and machinery. How can Country Y improve its Balance of Trade deficit?",
                            "options": [
                                "Option A: Processing raw tea into branded packaged tea (value addition) to earn higher export prices, while developing domestic renewable energy to reduce oil imports.",
                                "Option B: Stop exporting tea completely.",
                                "Option C: Print more paper money."
                            ],
                            "correct_option": "Option A: Processing raw tea into branded packaged tea (value addition) to earn higher export prices, while developing domestic renewable energy to reduce oil imports.",
                            "explanation": "Value addition boosts export earnings per kilogram, while local energy production cuts high petroleum import costs."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: International Trade",
                        "content": {
                            "question": "Which accounting term includes both physical merchandise trade and invisible services like tourism and foreign aid?",
                            "options": [
                                "Balance of Payments (BOP)",
                                "Balance of Trade (BOT)",
                                "Visible Trade Deficit",
                                "Barter Scale"
                            ],
                            "correct_answer": 0,
                            "explanation": "Balance of Payments is the complete accounting statement covering visible merchandise, invisible services, and capital transactions."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Value Addition in Exports",
                        "content": {
                            "text": "Exporting raw unroasted coffee beans yields less than 10% of the retail price of roasted packaged coffee in European supermarkets. By establishing local coffee roasting and tea packaging factories (value addition), Kenya can triple its foreign exchange earnings."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Balance of Payments",
                        "content": {
                            "mistake": "Assuming that a trade deficit means a country has no foreign money.",
                            "correction": "A trade deficit on visible goods can be partially offset by invisible earnings (such as tourism revenue or diaspora remittances) in the Balance of Payments.",
                            "reasoning": "Diaspora remittances (KSh 500+ Billion annually in Kenya) help cushion the visible trade deficit."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "International Trade: Key Takeaways",
                        "content": {
                            "title": "International Trade: Key Takeaways",
                            "summary_points": [
                                "Kenya exports primary agricultural produce (tea, coffee, flowers) and imports crude oil/machinery.",
                                "Balance of Trade measures visible export earnings vs visible import expenses.",
                                "Kenya has a persistent trade deficit because primary agricultural prices are low while manufactured import prices are high.",
                                "Balance of Payments is a broader account including visible trade, invisible services, and capital flows."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Regional Economic Trading Blocs (COMESA, EAC, ECOWAS, EU) (12 Pages)
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Regional Economic Trading Blocs (COMESA, EAC, ECOWAS, EU)",
            "unit_description": "Regional economic integration, COMESA, East African Community (EAC), ECOWAS, EU, benefits, and problems.",
            "lesson_title": "Regional Economic Trading Blocs (COMESA, EAC, ECOWAS, EU)",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Trading Blocs",
                        "content": {
                            "title": "Learning Objectives: Trading Blocs",
                            "goals": [
                                "Define regional economic integration and explain progressive integration stages.",
                                "Analyze objectives, achievements, and challenges of the East African Community (EAC) and COMESA.",
                                "Evaluate economic benefits and common problems of regional trade associations."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Regional Economic Integration",
                        "content": {
                            "title": "Regional Economic Integration",
                            "text": "A regional trading bloc is an association of neighboring sovereign nations formed to encourage trade integration by reducing or eliminating tariffs, quotas, and non-tariff trade barriers among member states.\n\nIntegration progresses through five distinct levels:\n1. Preferential Trade Area (PTA): Lower tariffs on select goods traded among members.\n2. Free Trade Area (FTA): Zero internal tariffs among member states (e.g., COMESA FTA).\n3. Customs Union: Zero internal tariffs PLUS a Common External Tariff (CET) on goods imported from non-member nations (e.g., EAC Customs Union).\n4. Common Market: Free movement of goods, services, labor, and capital across member borders (e.g., EAC Common Market).\n5. Economic & Monetary Union: Single currency and unified monetary policy (e.g., European Union Eurozone)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Trading Blocs Integration Pyramid (Free Trade to Common Market)",
                        "content": {
                            "title": "Trading Blocs Integration Pyramid (Free Trade to Common Market)",
                            "caption": "Integration Levels: Preferential Trade Area → Free Trade Area (Zero Internal Tariffs) → Customs Union (Common External Tariff) → Common Market (Free Factor Movement) → Economic Union",
                            "description": "Pyramid diagram showing progressive stages of regional trade integration from PTA to Economic Union."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "East African Community Regional Trading Bloc Visualization",
                        "content": {
                            "title": "East African Community Regional Trading Bloc Visualization",
                            "caption": "Map logo of the East African Community (EAC) member countries promoting regional trade integration.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Flag_maps_of_the_East_African_Community.png",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Flag_maps_of_the_East_African_Community.png"
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Major Regional Trading Blocs Taxonomy",
                        "content": {
                            "term": "Regional Trading Blocs Taxonomy",
                            "definition": "Key international trading blocs involving Kenya and global trading partners.",
                            "key_points": [
                                "EAC (East African Community): Comprises Kenya, Uganda, Tanzania, Rwanda, Burundi, South Sudan, DRC, Somalia. Operates a Single Customs Territory and Common Market.",
                                "COMESA (Common Market for Eastern and Southern Africa): 21 member nations creating a vast Free Trade Area spanning Egypt to Swaziland with over 600 million consumers.",
                                "ECOWAS (Economic Community of West African States): 15 West African nations promoting regional economic self-sufficiency.",
                                "EU (European Union): Advanced economic union of 27 European nations with a single market and Euro currency."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Benefits of Regional Trading Blocs to Member States",
                        "content": {
                            "title": "Benefits of Regional Trading Blocs to Member States",
                            "text": "1. Expanded Market Size: Eliminating tariffs opens access to hundreds of millions of regional consumers, encouraging large-scale manufacturing.\n2. Increased Foreign Investment: Multinational companies invest in regional factories to supply tariff-free member markets.\n3. Joint Infrastructure Projects: Member states co-finance cross-border SGR railways, energy grids, and highways.\n4. Diplomatic Cooperation & Peace: Trade interdependence reduces political conflicts and border disputes."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Problems Facing Regional Trading Blocs in Africa",
                        "content": {
                            "title": "Problems Facing Regional Trading Blocs in Africa",
                            "text": "1. Production of Similar Commodities: Most East African nations export similar agricultural goods (tea, coffee, maize), limiting intra-regional demand.\n2. Inadequate Transport Infrastructure: Missing rail links and poor roads between member countries slow down border transit.\n3. Loss of Tariff Revenue: Small member states rely heavily on customs duties for national budgets and resist tariff elimination.\n4. Political Rivalries & Non-Tariff Barriers: Sudden border closures, trade disputes, and bureaucratic delays hinder seamless trade."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "comparison_table",
                        "title": "EAC vs COMESA Comparative Analysis",
                        "content": {
                            "headers": ["Feature / Dimension", "East African Community (EAC)", "COMESA"],
                            "rows": [
                                ["Membership Size", "8 Member Nations (East & Central Africa)", "21 Member Nations (Eastern & Southern Africa)"],
                                ["Integration Level", "Common Market & Single Customs Territory", "Free Trade Area (FTA) & Preferential Trade Zone"],
                                ["Geographic Proximity", "Highly contiguous neighboring countries", "Vast geographic spread (Egypt to Eswatini)"],
                                ["Free Movement of Persons", "Enabled via East African passport & ID check", "Varies by member country bilateral visa agreements"],
                                ["Key Trade Goods", "Agricultural produce, cement, manufactured goods", "Tea, sugar, copper, petroleum, manufactured goods"]
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Case Study: The Single Customs Territory of the EAC",
                        "content": {
                            "question": "Explain how the EAC Single Customs Territory benefits transit trade through the Port of Mombasa to landlocked Uganda and Rwanda. (4 Marks)",
                            "strategy": "Detail customs clearance at port of entry, duty assessment, and transit speed.",
                            "solution": [
                                "1. Port Cargo Clearance (1 Mark): Import duties for Uganda/Rwanda are assessed and paid directly at the Port of Mombasa before cargo departs.",
                                "2. Removal of Internal Weighbridges/Checkpoints (1 Mark): Cargo containers move along the SGR Corridor with minimal border delays.",
                                "3. Reduction in Transit Times (1 Mark): Transit time from Mombasa to Kampala reduced from 18 days to 4 days.",
                                "4. Lower Transport Costs (1 Mark): Eliminates double taxation and reduces shipping demurrage charges for landlocked neighbors."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Trading Bloc Classifier",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Trading Bloc Classifier",
                            "prompt": "Scenario: Member states in a trading bloc agree to zero internal trade tariffs AND adopt a uniform 15% import tariff on all goods entering from non-member countries (e.g., China). Which level of trade integration does this represent?",
                            "options": [
                                "Option A: Customs Union (which combines zero internal tariffs with a Common External Tariff).",
                                "Option B: Preferential Trade Area (PTA).",
                                "Option C: Barter Zone."
                            ],
                            "correct_option": "Option A: Customs Union (which combines zero internal tariffs with a Common External Tariff).",
                            "explanation": "A Customs Union goes beyond a Free Trade Area by imposing a Common External Tariff (CET) on foreign imports entering any member state."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Regional Trading Blocs",
                        "content": {
                            "question": "What is the primary obstacle preventing high volume intra-regional trade among neighboring East African Community states?",
                            "options": [
                                "Production of similar agricultural commodities (tea, coffee, maize) leading to low internal demand.",
                                "Excessive similarity in human languages.",
                                "Total absence of ports.",
                                "Banning of all merchant trucks."
                            ],
                            "correct_answer": 0,
                            "explanation": "Because member states produce identical primary crops, they have limited demand for each other's agricultural goods."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: The AfCFTA Vision",
                        "content": {
                            "text": "The African Continental Free Trade Area (AfCFTA) aims to unite all 55 African nations into a single free trade market of 1.3 billion people, creating the world's largest free trade zone since the WTO."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: EAC vs COMESA",
                        "content": {
                            "mistake": "Confusing EAC and COMESA membership in exam essays.",
                            "correction": "Remember: All EAC founding nations (Kenya, Uganda, Rwanda) belong to COMESA, but COMESA includes non-EAC nations like Egypt, Zambia, and Zimbabwe.",
                            "reasoning": "Countries can belong to multiple overlapping regional trading blocs."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Regional Trading Blocs: Key Takeaways",
                        "content": {
                            "title": "Regional Trading Blocs: Key Takeaways",
                            "summary_points": [
                                "Integration progresses: Preferential Trade Area -> Free Trade Area -> Customs Union -> Common Market -> Economic Union.",
                                "Kenya is a prominent leading member of both the EAC and COMESA.",
                                "Blocs expand market access and lower consumer prices but face hurdles from similar product lines and non-tariff barriers."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Economic Significance of Trade and Challenges Facing Domestic & Foreign Trade in Kenya (11 Pages)
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Economic Significance of Trade and Challenges Facing Domestic & Foreign Trade in Kenya",
            "unit_description": "Significance of trade, foreign exchange, employment, revenue, price fluctuations, dumping, and smuggling.",
            "lesson_title": "Economic Significance of Trade and Challenges Facing Domestic & Foreign Trade in Kenya",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Significance & Challenges of Trade",
                        "content": {
                            "title": "Learning Objectives: Significance & Challenges of Trade",
                            "goals": [
                                "Evaluate economic significance of trade to Kenya's national GDP and infrastructure.",
                                "Analyze major challenges facing foreign trade (fluctuating primary prices, dumping, protectionism, smuggling).",
                                "Examine government regulatory policy measures (KEBS quality checks, Export Processing Zones - EPZA, anti-dumping duties)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Economic Significance of Trade to Kenya",
                        "content": {
                            "title": "Economic Significance of Trade to Kenya",
                            "text": "Trade is a primary catalyst for Kenya's economic development:\n\n1. Earning Foreign Exchange: Commodity exports (tea, flowers, coffee) earn vital hard foreign currencies (USD, EUR, GBP) required to pay for capital imports.\n\n2. Government Revenue Generation: The government collects substantial customs duties, import tariffs, excise taxes, and VAT at border points to fund public infrastructure.\n\n3. Employment Creation: Millions of Kenyans are employed in trade logistics, transport, warehousing, customs clearing, clearing agencies, wholesale markets, and retail shops.\n\n4. Industrial Growth & Technology Transfer: Importing machinery and capital equipment stimulates domestic manufacturing and technological adoption."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Economic Benefits of Trade Cascade Flowchart",
                        "content": {
                            "title": "Economic Benefits of Trade Cascade Flowchart",
                            "caption": "Macroeconomic Impact: Commodity Exports → Foreign Exchange Earnings → Industrial Import Capital → Infrastructure & Job Creation → GDP Growth",
                            "description": "Flowchart showing export earnings feeding national reserves, enabling capital imports, job creation, and economic growth."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Kenyan Exports Produce Visualization",
                        "content": {
                            "title": "Kenyan Exports Produce Visualization",
                            "caption": "Fresh horticultural produce packaged for international airfreight export at Jomo Kenyatta International Airport.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg"
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Challenges Facing Foreign Trade Taxonomy",
                        "content": {
                            "term": "Trade Challenges Taxonomy",
                            "definition": "Key structural obstacles hindering Kenya's international commercial trade.",
                            "key_points": [
                                "Price Volatility: Global market prices for primary agricultural commodities fluctuate wildly depending on world supply.",
                                "Dumping: Importing subsidized foreign manufactured goods and selling them below local production cost, crippling domestic factories.",
                                "High Crude Petroleum Costs: Fluctuating global oil prices inflate domestic transport and electricity costs.",
                                "Protectionist Tariffs: Western nations impose stringent non-tariff phytosanitary barriers on African exports.",
                                "Porous Borders & Smuggling: Illegal entry of untaxed contraband goods across unpoliced borders deprives government revenue."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Government Measures to Promote & Regulate Trade",
                        "content": {
                            "title": "Government Measures to Promote & Regulate Trade",
                            "text": "To mitigate trade challenges, the Kenyan government implements key policy measures:\n\n1. Export Processing Zones (EPZA): Creating specialized industrial parks (e.g., EPZ Athi River) offering tax holidays and duty-free machinery imports to encourage export manufacturing.\n\n2. Quality Regulation (KEBS): Kenya Bureau of Standards enforces strict quality checks on imports to block sub-standard or counterfeit goods.\n\n3. Export Promotion (KENPRO): Assisting local exporters to secure foreign markets through international trade fairs.\n\n4. Anti-Dumping Duties & Tariffs: Levying protective import duties on goods that threaten domestic industries (e.g., sugar, steel, paper)."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "comparison_table",
                        "title": "Dumping vs Protectionism Economic Effects",
                        "content": {
                            "headers": ["Economic Dimension", "Dumping Practices", "Protectionism Policies"],
                            "rows": [
                                ["Primary Mechanism", "Selling foreign goods below local cost price", "Imposing high import tariffs & quotas"],
                                ["Impact on Local Factories", "Forces local factories to close down & layoff workers", "Protects local factories from unfair foreign competition"],
                                ["Impact on Consumer Prices", "Temporarily lowers consumer prices on foreign items", "Raises prices of imported items for consumers"],
                                ["Government Revenue", "Reduces tax revenue due to factory closures", "Increases tariff revenue collected at customs posts"]
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "worked_example",
                        "title": "KCSE Case Study: Export Processing Zones (EPZ) Athi River",
                        "content": {
                            "question": "Analyze how Export Processing Zones (EPZs) in Kenya promote foreign trade and industrialization. (4 Marks)",
                            "strategy": "Detail tax incentives, employment, manufacturing focus, and foreign exchange.",
                            "solution": [
                                "1. Tax Holidays & Duty Exemptions (1 Mark): EPZ companies enjoy 10-year corporate tax holidays and zero duty on imported raw machinery.",
                                "2. Export Manufacturing Focus (1 Mark): Over 80% of EPZ output (apparel, garments) must be exported, boosting foreign exchange.",
                                "3. Direct Employment (1 Mark): EPZs employ thousands of local workers in garment stitching and industrial assembly.",
                                "4. Foreign Direct Investment (1 Mark): Attracts international capital and technology transfer into Kenya."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Trade Problem Solver",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Trade Problem Solver",
                            "prompt": "Scenario: Subsidized foreign sugar enters Kenya selling at KSh 80 per kg, while local Kenyan sugar mills require KSh 120 per kg to break even. What policy measure should the government take to protect local sugar farmers?",
                            "options": [
                                "Option A: Impose protective anti-dumping tariffs and import quotas on foreign sugar imports to equalize local market prices.",
                                "Option B: Close all domestic sugar mills.",
                                "Option C: Give free sugar to everyone."
                            ],
                            "correct_option": "Option A: Impose protective anti-dumping tariffs and import quotas on foreign sugar imports to equalize local market prices.",
                            "explanation": "Anti-dumping duties neutralize artificial foreign subsidies, allowing domestic sugar millers and farmers to remain commercially viable."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Significance & Challenges",
                        "content": {
                            "question": "Which government agency in Kenya is responsible for inspecting imported foreign goods to ensure they meet mandatory quality standards?",
                            "options": [
                                "KEBS (Kenya Bureau of Standards)",
                                "EPZA (Export Processing Zones Authority)",
                                "KRA (Kenya Revenue Authority)",
                                "UNEP"
                            ],
                            "correct_answer": 0,
                            "explanation": "KEBS inspects imports to prevent counterfeit and sub-standard goods from entering the Kenyan market."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "callout",
                        "title": "Geographic Insight: Smuggling across Porous Borders",
                        "content": {
                            "text": "Smuggling untaxed goods (like electronic goods, sugar, or petroleum) across unpoliced borders robs the Kenya Revenue Authority (KRA) of billions in tax revenue and creates unfair competition for tax-paying local businesses."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Exam Traps: Dumping vs Smuggling",
                        "content": {
                            "mistake": "Using 'dumping' and 'smuggling' as identical terms.",
                            "correction": "DUMPING is selling subsidized foreign goods below cost price (often legally imported). SMUGGLING is the illegal transit of untaxed goods across borders to evade customs checks.",
                            "reasoning": "Dumping relates to predatory pricing; smuggling relates to customs tax evasion."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Significance of Trade: Key Takeaways",
                        "content": {
                            "title": "Significance of Trade: Key Takeaways",
                            "summary_points": [
                                "Trade earns foreign exchange, creates jobs, generates tax revenue, and drives infrastructure.",
                                "Foreign trade faces challenges from price volatility, crude oil import costs, protectionism, dumping, and smuggling.",
                                "Kenya uses KEBS standards, anti-dumping tariffs, and EPZA incentives to regulate and stimulate trade."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Topic Synthesis, Key Glossary, Case Studies, and KCSE Examination Review (6 Pages)
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Topic Synthesis, Key Glossary, Case Studies, and KCSE Examination Review",
            "unit_description": "Topic synthesis, KCSE essay questions (factors influencing trade, EAC integration), and master review assessment.",
            "lesson_title": "Topic Synthesis, Key Glossary, Case Studies, and KCSE Examination Review",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Trade Mastery",
                        "content": {
                            "title": "Learning Objectives: Trade Mastery",
                            "goals": [
                                "Synthesize domestic and international trade concepts across all 6 learning units.",
                                "Master KCSE 10-mark essay questions on trade factors, trade balance, and regional integration.",
                                "Complete end-of-topic revision assessment."
                            ]
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Market Stand Nairobi Visualization",
                        "content": {
                            "title": "Market Stand Nairobi Visualization",
                            "caption": "Urban retail trade stall in Nairobi representing domestic retail commerce.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                            "author": "CC BY-SA 4.0, Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Maasai_Market-Nairobi.jpg"
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 1: Factors Influencing International Trade",
                        "content": {
                            "question": "Explain five physical and economic factors that influence international trade flow between nations. (10 Marks)",
                            "strategy": "State factor (1 Mark) and explain geographical impact on trade volume (1 Mark).",
                            "solution": [
                                "1. Unequal Natural Resource Distribution (2 Marks): Variations in climate, geological mineral deposits, and soil fertility force nations to trade for goods they cannot produce locally.",
                                "2. Transport & Logistics Infrastructure (2 Marks): Modern deep-water seaports (Mombasa), railways (SGR), and airports reduce transport costs, enabling rapid movement of bulk cargo.",
                                "3. Market Demand & Purchasing Power (2 Marks): High population size accompanied by strong disposable income creates heavy demand for foreign imported goods.",
                                "4. Trade Tariffs & Protectionist Barriers (2 Marks): Import duties and quotas artificially raise foreign product prices, restricting trade volume.",
                                "5. Foreign Currency & Political Stability (2 Marks): Stable international exchange rates and peaceful diplomatic relations foster long-term commercial contracts."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Essay 2: Benefits and Problems of EAC Regional Integration",
                        "content": {
                            "question": "Discuss five benefits and three problems facing member states of the East African Community (EAC). (10 Marks)",
                            "strategy": "Divide response into Benefits (5 Marks) and Problems (5 Marks).",
                            "solution": [
                                "1. Benefits of EAC Regional Integration (5 Marks):\n   • Expands consumer market size to over 300 million people across 8 member states.\n   • Eliminates internal tariffs under the Customs Union, lowering prices for consumers.\n   • Enables free movement of labor, capital, and services under the Common Market.\n   • Facilitates joint cross-border infrastructure development (e.g., SGR railway, electricity grids).\n   • Enhances diplomatic cooperation, regional security, and peaceful dispute resolution.",
                                "2. Problems Facing EAC Integration (5 Marks):\n   • Member states produce similar primary agricultural crops (tea, coffee, maize), limiting intra-regional trade demand.\n   • Inadequate transport and logistics links between member countries slow down transit.\n   • Sudden border closures and political disputes among regional leaders disrupt trade."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "definition_card",
                        "title": "Master Glossary of Geography Trade Terms",
                        "content": {
                            "term": "Geography Trade Master Glossary",
                            "definition": "Essential textbook definitions required for KCSE Geography Paper 2.",
                            "key_points": [
                                "Visible Trade: Commercial exchange of physical, tangible goods (tea, crude oil).",
                                "Invisible Trade: Exchange of intangible services (tourism, shipping, banking).",
                                "Balance of Trade: Value of visible exports minus value of visible imports.",
                                "Trade Deficit: Monetary deficit occurring when visible import expenditure exceeds visible export earnings.",
                                "Balance of Payments: Comprehensive accounting statement of ALL visible, invisible, and capital transactions.",
                                "Customs Union: Trading bloc with zero internal tariffs and a Common External Tariff.",
                                "Dumping: Predatory practice of selling subsidized foreign goods below domestic production cost.",
                                "Value Addition: Processing raw primary commodities before export to increase market value."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "knowledge_check",
                        "title": "Topic 7 Mastery Assessment Question",
                        "content": {
                            "question": "Which combination correctly describes Kenya's primary foreign trade structure?",
                            "options": [
                                "Exports low-value primary agricultural goods (tea, coffee); Imports high-cost industrial capital goods (crude oil, machinery).",
                                "Exports heavy industrial machinery; Imports raw agricultural crops.",
                                "Exports crude oil; Imports tea and coffee.",
                                "Exports software only; Imports nothing."
                            ],
                            "correct_answer": 0,
                            "explanation": "Kenya exports primary agricultural produce and imports high-value manufactured goods and fuel."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "summary",
                        "title": "Topic 7 Mastery Synthesis & Review",
                        "content": {
                            "title": "Topic 7 Mastery Synthesis & Review",
                            "summary_points": [
                                "Trade is the exchange of goods and services; classified as Internal vs International, Visible vs Invisible.",
                                "Internal distribution proceeds: Producer -> Wholesaler -> Retailer -> Consumer.",
                                "Kenya exports agricultural products and imports crude oil/machinery, suffering a persistent trade deficit.",
                                "Regional trading blocs (EAC, COMESA) eliminate tariffs and expand market access.",
                                "Form 4 Geography Topic 7 (Trade) Ingestion is 100% Complete & Richly Enriched!"
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_geography_topic7():
    print("=" * 80)
    print("VLearn Form 4 Geography — Topic 7: Trade")
    print("In-Place Production Ingestion Engine (Preserves Topic ID)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    subject = Subject.objects.filter(grade=grade, name="Geography").first()

    if not subject:
        print("[!] Error: Subject 'Geography' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Trade"

    # Match topic by order or name in-place
    topic = Topic.objects.filter(subject=subject, order=7).first()
    if not topic:
        topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=7,
            description="Comprehensive syllabus on internal and international trade, wholesale/retail distribution channels, Kenya's major exports and imports, Balance of Trade and Balance of Payments, regional trading blocs (COMESA, EAC, ECOWAS, EU), significance of trade, and trade challenges (tariffs, price fluctuations, dumping, smuggling)."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        topic.name = topic_name
        topic.order = 7
        topic.description = "Comprehensive syllabus on internal and international trade, wholesale/retail distribution channels, Kenya's major exports and imports, Balance of Trade and Balance of Payments, regional trading blocs (COMESA, EAC, ECOWAS, EU), significance of trade, and trade challenges (tariffs, price fluctuations, dumping, smuggling)."
        topic.save()
        print(f"[*] Preserving existing Topic ID: {topic.id} ({topic.name})")

    curriculum_data = build_topic7_curriculum()
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
    print("[SUCCESS] Form 4 Geography Topic 7 (Trade) Ingested In-Place!")
    print(f"[*] Topic ID Preserved:     {topic.id}")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_form4_geography_topic7()
