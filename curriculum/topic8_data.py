"""
VLearn Form 4 Business Studies — Topic 8: Economic Integration
Authoritative Pedagogical Data Structures for 3 Lessons (30 Pages).
"""

from curriculum.ingest_form4_business_studies_topic8_svgs import (
    SVG_INTEGRATION_STAGES_LADDER,
    SVG_STAGE_COMPARISON_MATRIX,
    SVG_TRADE_CREATION_VS_DIVERSION,
    SVG_INTEGRATION_BENEFITS_TREE,
    SVG_INTEGRATION_LIMITATIONS_MATRIX
)

# Verified Wikimedia photographic assets
IMG_EAC_TRANSPORT_CORRIDOR = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
    "text": "Standard Gauge Railway cross-border freight corridor, facilitating regional integration, transit trade, and infrastructure connectivity across East Africa.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
}

IMG_MOMBASA_PORT_TRANSIT = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Kilindini Harbour at the Port of Mombasa, illustrating the East African Customs Union (EACU) Common External Tariff (CET) enforcement and regional transit operations.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_LABOR_MOBILITY_FABRICATION = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "Technical fabrication workshop in Kenya, demonstrating cross-border factor mobility (labor and skilled entrepreneurs) within a regional Common Market.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

IMG_REGIONAL_COMMODITY_MARKET = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Agricultural commodity market in Kenya illustrating intra-regional food trade, market expansion, and regional consumer choices.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

# ==============================================================================
# LESSON 1: MEANING, FORMS AND STAGES OF ECONOMIC INTEGRATION (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Meaning, Forms and Stages of Economic Integration",
    "lesson_title": "Hierarchical Integration Ladders, Common External Tariffs, and Factor Mobility",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Economic Integration",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define economic integration, identify and distinguish between the four main stages of economic integration, explain their features, and cite real-world trade bloc examples."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Countries Integrate Regionally",
                    "content": {
                        "text": "As an individual nation, Kenya has a domestic market of about 50 million people. By integrating with neighboring countries in the East African Community (EAC), Kenyan businesses gain direct access to a market of over 300 million people, enabling firms to pool resources, specialize, and compete globally."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition of Economic Integration",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Economic Integration",
                    "content": {
                        "term": "Economic Integration",
                        "definition": "A process where two or more countries in the same geographical region join up and cooperate with each other to abolish trade barriers and coordinate economic policies for mutual financial benefit."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Stage 1: Free Trade Area (FTA)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Characteristics of a Free Trade Area",
                    "content": {
                        "text": "• Definition: Member countries agree to abolish or relax tariffs, quotas, and trade barriers among themselves.\n• Key Feature: Each individual country remains completely free to impose its own independent trade tariffs on non-member countries.\n• Examples: PTA (Preferential Trade Area), LAFTA (Latin American Free Trade Area)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Stage 2: Customs Union",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Characteristics of a Customs Union",
                    "content": {
                        "text": "• Definition: Has all features of a Free Trade Area, but member countries impose a Common External Tariff (CET) on trade with non-member nations.\n• Key Feature: Internal trade is free, and any cargo entering the bloc from the outside world faces the exact same tax rate regardless of port of entry.\n• Examples: EACU (East African Customs Union), BENELUX."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Customs Union & CET Enforcement",
                    "content": IMG_MOMBASA_PORT_TRANSIT
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Stage 3: Common Market",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Characteristics of a Common Market",
                    "content": {
                        "text": "• Definition: Has all features of a Customs Union, plus free movement of factors of production (labor, capital, land, entrepreneurship) among member states.\n• Key Feature: Citizens can work, live, invest, and set up businesses anywhere in the bloc without work permits or capital controls.\n• Examples: EEC (European Economic Community), CACM."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Cross-Border Factor & Labor Mobility",
                    "content": IMG_LABOR_MOBILITY_FABRICATION
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Stage 4: Economic Union",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Characteristics of an Economic Union",
                    "content": {
                        "text": "• Definition: The highest stage of economic integration.\n• Key Feature: Combines all features of a Common Market with joint economic institutions, a common monetary system (single shared currency), and common public services (railways, harbors, central bank).\n• Example: European Union (EU)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Four Stages of Economic Integration Ladder",
                    "svg_content": SVG_INTEGRATION_STAGES_LADDER,
                    "content": {
                        "text": "Concentric circle / ladder diagram illustrating the 4 progressive stages of integration."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Comparative Analysis Across All 4 Stages",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Integration Stages Feature Comparison",
                    "content": {
                        "headers": ["Stage", "Internal Tariffs", "Common External Tariff (CET)", "Factor Mobility (Labor/Capital)", "Unified Currency & Institutions"],
                        "rows": [
                            ["Free Trade Area (FTA)", "Abolished / Relaxed", "Independent (Each sets own)", "Restricted", "None"],
                            ["Customs Union", "Abolished / Relaxed", "Common External Tariff (CET)", "Restricted", "None"],
                            ["Common Market", "Abolished / Relaxed", "Common External Tariff (CET)", "Fully Free Movement", "None"],
                            ["Economic Union", "Abolished / Relaxed", "Common External Tariff (CET)", "Fully Free Movement", "Unified Single Currency & Central Bank"]
                        ]
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Integration Stage Comparison Matrix",
                    "svg_content": SVG_STAGE_COMPARISON_MATRIX,
                    "content": {
                        "text": "Comparison matrix mapping internal tariffs, CET, factor mobility, and currency across all 4 stages."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Case Study: Kenya-Tanzania Labor Permit Realities",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Customs Union vs Common Market Case Study",
                    "content": {
                        "text": "Suppose Kenya and Tanzania operate strictly as a Customs Union. If a Kenyan firm wants to hire Tanzanian truck drivers to work permanently in Mombasa, those drivers still require complex work permits because a Customs Union does NOT guarantee factor mobility. Only when they transition to a Common Market can labor move freely across borders."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: FTA vs. Customs Union CET",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Common External Tariff Distinction",
                    "content": {
                        "text": "Do not confuse FTAs and Customs Unions! Both abolish internal tariffs. But in an FTA, member countries set INDEPENDENT tariffs against non-members. In a Customs Union, all members present a unified Common External Tariff (CET) front to the world."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "What key feature distinguishes a Common Market from a Customs Union?",
                        "options": [
                            "Abolition of internal trade tariffs",
                            "Free movement of factors of production (labor and capital) across borders",
                            "A common monetary currency issued by a single central bank",
                            "Setting independent external tariffs against non-member nations"
                        ],
                        "correct_answer": "Free movement of factors of production (labor and capital) across borders",
                        "explanation": "A Common Market includes all features of a Customs Union while introducing free factor mobility (unrestricted movement of labor and capital)."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: BENEFITS AND LIMITATIONS OF ECONOMIC INTEGRATION (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Benefits and Limitations of Economic Integration",
    "lesson_title": "Market Expansion, Collective Bargaining Power, and Monopolistic Protection Risks",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Integration Benefits and Demerits",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain six compelling economic benefits of integration, evaluate six structural limitations and risks, and analyze policy trade-offs."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Regional Integration is a Double-Edged Sword",
                    "content": {
                        "text": "When the EAC expanded, some Kenyan manufacturers expanded rapidly into regional markets, while others faced stiff competition. Economic integration trades national trade sovereignty for collective regional power, requiring careful policy balance."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Six Compelling Benefits of Integration",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Economic Benefits of Trade Blocs",
                    "content": {
                        "text": "1. Wider Market Size: Combining populations increases market size, enabling manufacturers to enjoy economies of scale.\n2. Encourages Specialization: Member nations focus on producing commodities where they are most efficient.\n3. Cheap & High-Quality Goods: Intense regional competition drives down prices and boosts product quality.\n4. Promotes Regional Peace: Mutual economic interdependence reduces border conflicts.\n5. Common Bargaining Front: Negotiating as a unified bloc secures superior terms of trade with global giants (EU, China).\n6. Employment Creation: Free factor mobility allows citizens to seek jobs anywhere in the bloc."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Six Economic Benefits of Integration Tree",
                    "svg_content": SVG_INTEGRATION_BENEFITS_TREE,
                    "content": {
                        "text": "Mind map diagram illustrating wider market, specialization, cheap quality goods, peace, bargaining power, and job creation."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Infrastructure Connectivity in Regional Blocs",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Cross-Border Infrastructure & Transit Freight",
                    "content": IMG_EAC_TRANSPORT_CORRIDOR
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Six Demerits & Risks of Integration",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Structural Limitations of Trade Blocs",
                    "content": {
                        "text": "1. Retaliation by Non-Members: Setting high external tariffs causes excluded nations to retaliate against bloc exports.\n2. Production of Low-Quality Goods: Over-protected regional firms become lazy and produce substandard items.\n3. High Consumer Prices: Inefficient regional infant industries pass high costs to local consumers.\n4. Less Consumer Choice: Tariffs on superior non-member imports restrict consumer options.\n5. Emergence of Regional Monopolies: Large corporations in dominant member states destroy small local businesses.\n6. Perpetual Infant Protection: Weak regional industries demand endless taxpayer subsidies."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Structural Limitations of Trade Blocs Matrix",
                    "svg_content": SVG_INTEGRATION_LIMITATIONS_MATRIX,
                    "content": {
                        "text": "Matrix mapping retaliation, substandard goods, high prices, restricted choice, monopolies, and perpetual protection."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Pros vs. Demerits Comparison",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Integration Benefits vs. Limitations",
                    "content": {
                        "headers": ["Economic Dimension", "Integration Benefits", "Integration Limitations & Risks"],
                        "rows": [
                            ["Market Scope", "Access to wider regional consumer market (300M+)", "Risk of retaliation by excluded non-member nations"],
                            ["Product Quality", "Competition drives quality improvement & lower costs", "Over-protection can shelter substandard regional products"],
                            ["Domestic Firms", "Specialization & economies of scale growth", "Dominant member corporations create regional monopolies"],
                            ["Diplomacy", "Regional peace & unified global bargaining front", "Unequal development levels cause member state trade friction"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Regional Trade Policy Simulator Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Sugar Protectionism Trade-Off Scenario",
                    "content": {
                        "text": "Kenya's Trade Minister faces a choice: Option 1: Protect struggling local sugar farmers by blocking cheap sugar imports from an EAC partner. Option 2: Allow cheap sugar imports freely.\nOutcome 1: Option 1 triggers retaliation: partner states ban Kenyan manufactured cosmetics. Outcome 2: Option 2 causes short-term sugar job losses, but lowers sugar prices nationwide and increases manufactured export growth."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Economic integration expands markets, encourages specialized efficiency, and builds unified bargaining strength. However, it risks non-member retaliation, shelters inefficient infant industries, and can create regional monopolies."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Regional Dominance Friction",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Asymmetric Development",
                    "content": {
                        "text": "If one member state has a more advanced manufacturing sector, it can run persistent trade surpluses against partner states. This asymmetric dominance leads to non-tariff barriers and regional trade friction unless wealth-sharing mechanisms are built into the bloc."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Check Your Understanding 1",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Common Bargaining Front Power",
                    "content": {
                        "text": "Why a common bargaining front works: Negotiating as a 300-million-person regional bloc gives member states massive leverage when bargaining trade deals with large economic superpowers (US, EU, China), securing far better terms than a small isolated nation could achieve."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding 2",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Which of the following is a potential risk experienced by member states in a regional trade bloc?",
                        "options": [
                            "Expanded economies of scale for local producers",
                            "Emergence of regional monopolies from dominant member states outcompeting local firms",
                            "Automatic elimination of all global trade retaliation",
                            "Free movement of labor across national borders"
                        ],
                        "correct_answer": "Emergence of regional monopolies from dominant member states outcompeting local firms",
                        "explanation": "Large, powerful corporations in advanced member states can destroy small businesses in weaker partner states, creating exploitative regional monopolies."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: TRADE CREATION VS DIVERSION AND REGIONAL APPLICATIONS (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Trade Creation vs Diversion and Regional Applications",
    "lesson_title": "Welfare Shifts, EAC Trade Integration, and KCSE Examination Mastery",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Trade Creation vs Diversion",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define trade creation and trade diversion, analyze their welfare effects, discuss real-world EAC integration challenges, and master KCSE examination practice."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Integration Does Not Always Increase Efficiency",
                    "content": {
                        "text": "Students often assume regional integration always increases economic welfare. However, if a Customs Union forces member states to stop buying cheap goods from efficient non-members (like Japan) and buy expensive goods from regional partners due to high external tariffs, trade diversion occurs, lowering consumer welfare!"
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Trade Creation (Positive Welfare Effect)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Trade Creation",
                    "content": {
                        "term": "Trade Creation",
                        "definition": "The shift in domestic consumption from an inefficient, high-cost local producer to a low-cost, efficient regional partner following the elimination of internal trade tariffs, expanding total trade and consumer welfare."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Trade Diversion (Negative Welfare Effect)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Trade Diversion",
                    "content": {
                        "term": "Trade Diversion",
                        "definition": "The shift in import sourcing away from a low-cost, efficient non-member producer (e.g. Japan) to an inefficient, high-cost regional partner due to the imposition of a high Common External Tariff (CET) on non-members."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Trade Creation vs Trade Diversion Flowchart",
                    "svg_content": SVG_TRADE_CREATION_VS_DIVERSION,
                    "content": {
                        "text": "Flowchart contrasting positive trade creation welfare gains with negative trade diversion welfare losses."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Worked Numerical Scenario: Trade Diversion Math",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Japan Electronics Trade Diversion Scenario",
                    "content": {
                        "text": "Scenario: Prior to integration, Country A imported electronics from Japan (non-member) at Sh. 10,000 + 5% tariff = Sh. 10,500. Country B (regional partner) produced electronics at Sh. 13,000.\nAfter forming a Customs Union, Country A and B set a 40% CET on Japan. Japanese electronics now cost Sh. 14,000 (10,000 + 40%). Country B electronics cross borders tax-free at Sh. 13,000.\nOutcome: Country A switches from Japan (Sh. 10,500) to Country B (Sh. 13,000). Trade Diversion has occurred! Consumers pay Sh. 2,500 more for lower quality electronics."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "EAC Regional Application & Non-Tariff Barriers",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Regional Commodity Market Distribution",
                    "content": IMG_REGIONAL_COMMODITY_MARKET
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Trade Creation expands trade and improves welfare by shifting consumption to efficient regional partners. Trade Diversion reduces welfare by forcing members to buy expensive regional goods over cheap non-member goods due to high CETs."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Watch Out: KCSE Exam Trap on Stages",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Integration Ladder Order",
                    "content": {
                        "text": "Integration is a strict ladder: Free Trade Area ---> Customs Union ---> Common Market ---> Economic Union. You cannot jump straight to an Economic Union without establishing a CET and factor mobility!"
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "KCSE Integrated Practice: Paper 1",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Paper 1 Short-Answer Mastery",
                    "content": {
                        "text": "1. Main Difference: FTA has independent external tariffs; Customs Union has Common External Tariff (CET).\n2. Four Features of Economic Union: Zero internal tariffs, CET, free factor mobility, single currency & joint central bank.\n3. Regional Examples: EACU = Customs Union; EEC = Common Market; PTA = Free Trade Area.\n4. Trade Creation vs Diversion: Creation shifts to cheaper regional partner; Diversion shifts away from cheaper non-member due to CET."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "When a Customs Union's high Common External Tariff forces member nations to stop importing cheap goods from efficient non-members and buy expensive goods from regional partners, what economic phenomenon has occurred?",
                        "options": [
                            "Trade Creation",
                            "Trade Diversion",
                            "Currency Devaluation",
                            "Export Processing Zone Creation"
                        ],
                        "correct_answer": "Trade Diversion",
                        "explanation": "Trade Diversion occurs when high Common External Tariffs divert imports away from cheap non-member producers to more expensive regional partners."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Integrated Practice: Paper 2 (Benefits Essay)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Essay Model Answer: Benefits of Integration for Kenya",
                    "content": {
                        "text": "Question: Discuss five benefits Kenya derives from participating in regional economic integration (10 Marks).\n\nModel Answer:\n1. Expanded Market Size: Access to over 300 million EAC consumers allows local firms to expand production and enjoy economies of scale.\n2. Enhanced Efficiency & Quality: Competition from regional firms forces Kenyan producers to adopt modern technology and lower costs.\n3. Free Labor Mobility: Skilled Kenyan professionals (teachers, engineers, doctors) can secure jobs across member states without work permits.\n4. Unified Bargaining Position: Negotiating as a regional bloc secures superior terms of trade with global superpowers (US, EU, China).\n5. Fostering Peace & Security: Close economic ties and shared infrastructure (SGR) reduce border conflicts with neighboring nations."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Integrated Practice: Paper 2 (Limitations Essay)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Essay Model Answer: Limitations of Regional Trade Blocs",
                    "content": {
                        "text": "Question: Explain five limitations countries encounter in regional trade agreements (10 Marks).\n\nModel Answer:\n1. Risk of Retaliation: Violating trade pacts causes partner nations to place embargoes or heavy tariffs on exports.\n2. Sustaining Inefficient Domestic Firms: Sheltering regional firms from global competition leads to substandard products.\n3. Higher Prices for Consumers: Protected regional infant industries with high costs pass expenses to local consumers.\n4. Restricted Consumer Choice: CET tariffs on foreign goods limit consumer options.\n5. Monopolistic Exploitation: Dominant corporations in strong member states destroy small businesses in weaker nations, creating regional monopolies."
                    }
                }
            ]
        }
    ]
}

TOPIC8_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA
]
