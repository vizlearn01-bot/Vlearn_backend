"""
VLearn Form 4 Business Studies — Topic 7: International Trade
Authoritative Pedagogical Data Structures for 5 Lessons (50 Pages).
"""

from curriculum.ingest_form4_business_studies_topic7_svgs import (
    SVG_HOME_VS_INTERNATIONAL_TRADE,
    SVG_BALANCE_OF_PAYMENTS_T_ACCOUNT,
    SVG_TERMS_OF_SALE_PIPELINE,
    SVG_INTERNATIONAL_FINANCIAL_INSTITUTIONS_TRIO,
    SVG_TRADE_PROTECTIONISM_EFFECTS
)

# Verified Wikimedia photographic assets
IMG_PORT_OF_MOMBASA = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Kilindini Harbour at the Port of Mombasa, illustrating international maritime trade logistics, container shipping lines, customs clearance, and export-import cargo handling.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_JKIA_AIR_CARGO = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
    "text": "Freight logistics transport network connecting Mombasa Port to Nairobi inland container depots, demonstrating international terms of sale and multi-modal freight movement.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
}

IMG_CENTRAL_BANK_FOREX = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Retail commodity market in Kenya illustrating local currency pricing versus foreign exchange requirements for imported food and fuel supplies.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_ATHI_RIVER_EPZ = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "Export processing manufacturing workshop in Kenya, demonstrating export-oriented industrialization, duty-free privileges, and foreign direct investment.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

# ==============================================================================
# LESSON 1: MEANING, BASIS AND IMPORTANCE OF INTERNATIONAL TRADE (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Meaning, Basis and Importance of International Trade",
    "lesson_title": "Foreign Trade Categories, Comparative Advantage, and Global Market Dynamics",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to International Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define international trade, distinguish between bilateral and multilateral trade, explain five differences between home trade and international trade, and evaluate the advantages and disadvantages of global trade."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Nations Trade Globally",
                    "content": {
                        "text": "Kenya produces world-class tea and coffee, but does not manufacture commercial aircraft or refine crude oil. Through international trade, Kenya exports its agricultural surplus to purchase machinery, vehicles, and fuel from foreign countries, raising national living standards."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition & Categories of International Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of International Trade",
                    "content": {
                        "term": "International Trade",
                        "definition": "The exchange of goods and services across national boundaries between two or more countries, comprising exports (sales abroad) and imports (purchases from abroad)."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Bilateral vs. Multilateral Trade",
                    "content": {
                        "text": "• Bilateral Trade: Trade carried out between exactly two countries under a bilateral agreement (e.g. Kenya and China).\n• Multilateral Trade: Trade carried out among three or more countries (e.g. Kenya trading concurrently with EAC, EU, and India)."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Home Trade vs. International Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Home Trade vs. International Trade",
                    "content": {
                        "headers": ["Feature", "Home Trade (Domestic)", "International Trade (Foreign)"],
                        "rows": [
                            ["Boundaries", "Occurs within national borders", "Crosses international frontiers"],
                            ["Currency", "Uses single domestic currency (KShs)", "Requires foreign exchange (USD, Euro, Sterling)"],
                            ["Trade Barriers", "Free of internal tariffs/quotas", "Subject to customs duties, tariffs, and quotas"],
                            ["Legal Framework", "Governed by single national law", "Governed by diverse national & international commercial laws"],
                            ["Transport Risk", "Shorter distances, lower freight risk", "Long distances (sea/air), marine risks, currency fluctuation"]
                        ]
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Home vs International Trade Boundaries",
                    "svg_content": SVG_HOME_VS_INTERNATIONAL_TRADE,
                    "content": {
                        "text": "Comparison diagram illustrating domestic commerce versus cross-border international trade boundaries."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Eight Advantages of International Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Benefits of Global Trade Participation",
                    "content": {
                        "text": "1. Obtaining Non-Produced Goods: Acquire essential goods not produced locally (crude oil, jetliners).\n2. Cheaper Goods: Import items produced more cheaply abroad.\n3. Encouraging Specialization: Focus resources on goods with a comparative advantage (tea, coffee).\n4. Promoting Competition: Foreign competition improves domestic product quality.\n5. Transfer of Technology: Adoption of modern foreign technology and managerial skills.\n6. Resource Exploitation: Global demand enables full utilization of domestic natural resources.\n7. Factor Mobility: Movement of capital and skilled labor across frontiers.\n8. Promoting Peace: Diplomatic relations and mutual dependence build international harmony."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "International Trade Cargo Operations",
                    "content": IMG_PORT_OF_MOMBASA
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Six Disadvantages of International Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Economic Risks of International Trade",
                    "content": {
                        "text": "1. Collapse of Infant Local Industries: Cheap imports drive young domestic producers out of business.\n2. Importation of Harmful Goods: Risk of toxic, expired, or illicit goods entering the country.\n3. Overdependency: Relying on foreign nations for strategic items (food, defense) threatens national sovereignty.\n4. Supply Vulnerability: War or political disputes among trading partners cut off vital supplies.\n5. Imported Inflation: High prices in exporting countries are directly transmitted to importing consumers.\n6. Cultural Erosion: Foreign exposure can erode domestic cultural values."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Case Study: Kenya's Specialization Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Tea Export vs Crude Oil Import Case Study",
                    "content": {
                        "text": "Kenya possesses abundant fertile land ideal for tea farming, but lacks oil reserves. By specializing in tea production, Kenya exports surplus tea to the Middle East, using earned foreign exchange to import refined fuel and heavy machinery. Without international trade, Kenya would have unutilized land and no fuel to power its transport grid."
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
                        "text": "International trade allows nations to overcome resource limitations through specialization. However, open global trade exposes local infant industries to severe foreign competition, imported inflation, and dependency risks."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Bilateral vs Multilateral",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Trade Agreement Types",
                    "content": {
                        "text": "Bilateral trade is strictly between TWO nations. Multilateral trade involves THREE or more nations. If Kenya trades with Uganda under a regional agreement that includes Tanzania, Rwanda, and Burundi, it is multilateral trade!"
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
                    "title": "Comparative Advantage in Specialization",
                    "content": {
                        "text": "Why specialization increases global output: When each country allocates resources to producing goods where its production costs are lowest (comparative advantage), global resource efficiency increases, producing higher quality goods at lower prices for all trading partners."
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
                        "question": "Which of the following is a structural difference between Home Trade and International Trade?",
                        "options": [
                            "Home trade involves goods while international trade involves services only",
                            "International trade requires foreign exchange currency conversion and customs clearance",
                            "Home trade requires a Bill of Lading while international trade does not",
                            "International trade takes place strictly within local county boundaries"
                        ],
                        "correct_answer": "International trade requires foreign exchange currency conversion and customs clearance",
                        "explanation": "International trade crosses national borders, requiring foreign exchange conversion, compliance with customs regulations, and international commercial law."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: TERMS OF TRADE AND BALANCE OF PAYMENTS (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Terms of Trade and Balance of Payments",
    "lesson_title": "Export Price Ratios, Current Account Structure, and BOP Deficit Mitigation",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to TOT and BOP",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to calculate and interpret the Terms of Trade (TOT), outline the structure of Balance of Payments (BOP) accounts, analyze causes of BOP disequilibrium, and demonstrate policies to correct a trade deficit."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why TOT and BOP Act as Economic Report Cards",
                    "content": {
                        "text": "A nation can export huge physical volumes of goods but earn very little if export prices are low relative to import prices. Terms of Trade (TOT) and Balance of Payments (BOP) accounts act as a country's macroeconomic report card, tracking its global financial strength."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Terms of Trade (TOT) Formula & Interpretation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "TOT Mathematical Formula",
                    "content": {
                        "text": "Terms of Trade (TOT) = (Export Price Index / Import Price Index) * 100\n\n• Favorable Terms of Trade (TOT > 100%): Export prices rise faster than import prices. The country buys more imports per unit of exports.\n• Unfavorable Terms of Trade (TOT < 100%): Import prices rise faster than export prices. The country must export more physical goods to buy the same imports."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Structure of Balance of Payments (BOP) Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Components of BOP Accounts",
                    "content": {
                        "text": "1. Current Account: Records Visible Trade (physical goods exports/imports -> Visible Balance) and Invisible Trade (services like tourism, shipping -> Invisible Balance). Current Account Balance = Visible Balance + Invisible Balance.\n2. Capital Account: Records capital inflows (+ FDI, external loans) and capital outflows (- debt repayments, capital flight).\n3. Official Settlement Account: Records Central Bank balancing actions using foreign exchange reserves or IMF drawing rights."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Balance of Payments T-Account Structure",
                    "svg_content": SVG_BALANCE_OF_PAYMENTS_T_ACCOUNT,
                    "content": {
                        "text": "Accounting structure diagram mapping Current, Capital, and Official Settlement accounts."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Causes of Balance of Payments Deficit",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Six Drivers of BOP Disequilibrium",
                    "content": {
                        "text": "1. Fall in Export Volumes: Drought or poor output reduces export quantities.\n2. Deteriorating Terms of Trade: Fall in export prices relative to import prices.\n3. Increased Import Demand: High spending on imported luxury goods or fuel.\n4. Foreign Trade Barriers: External tariffs/quotas restricting local exports.\n5. Capital Flight: Outflow of investment capital exceeding inflows.\n6. Overvalued Local Currency: Makes exports expensive to foreigners and imports cheap to citizens."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Four Policy Strategies to Correct BOP Deficit",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "BOP Deficit Correction Toolkit",
                    "content": {
                        "text": "1. Control Imports: High tariffs, quotas/embargoes, foreign exchange controls, administrative bottlenecks.\n2. Promote Exports: Export compensation schemes, customs duty drawbacks, commercial attachés at foreign embassies.\n3. Monetary Action (Currency Devaluation): Deliberately lowering currency value to make exports cheap and imports expensive.\n4. Capital Attraction: Offering tax incentives to attract Foreign Direct Investment (FDI)."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Foreign Reserve & Exchange Monitoring",
                    "content": IMG_CENTRAL_BANK_FOREX
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Calculation 1: 5-Step Current Account & TOT Math",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "5-Step BOP Current Account & TOT Math",
                    "content": {
                        "text": "Problem: Country transactions for 2025:\nVisible Exports = Sh. 180,000M | Visible Imports = Sh. 220,000M\nInvisible Exports = Sh. 90,000M | Invisible Imports = Sh. 70,000M\nExport Price Index = 125 | Import Price Index = 80\nCalculate: a) Visible Balance b) Invisible Balance c) Current Account Balance d) Terms of Trade\n\nSolution:\nStep 1: Visible Balance = 180,000 - 220,000 = Sh. -40,000M (Deficit)\nStep 2: Invisible Balance = 90,000 - 70,000 = Sh. +20,000M (Surplus)\nStep 3: Current Account Balance = -40,000 + 20,000 = Sh. -20,000M (Deficit)\nStep 4: Terms of Trade = (125 / 80) * 100 = 156.25%\nStep 5: Interpretation = TOT is 156.25% (>100%), indicating favorable terms of trade. However, the Current Account remains in deficit by Sh. 20,000M due to heavy visible merchandise imports."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Worked Calculation 2: Price Index Deterioration",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "TOT Deterioration Calculation",
                    "content": {
                        "text": "Problem: Export price index is 110, while import price index is 125. Calculate TOT and state whether favorable.\n\nSolution:\nTOT = (110 / 125) * 100 = 88%.\nSince 88% is below 100%, the Terms of Trade is unfavorable. Export prices have fallen relative to import prices, forcing the country to export more physical volume to buy the same imports."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "TOT measures export price relative to import price. Balance of Payments summarizes all foreign financial transactions. Governments correct BOP deficits by combining tariffs, export compensation schemes, currency devaluation, and FDI promotion."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Visible vs Invisible Trade",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Trade Components",
                    "content": {
                        "text": "Visible trade refers exclusively to physical tangible goods (tea, cars, oil). Invisible trade refers to intangible services (tourism, shipping, banking, dividends). Current Account Balance MUST combine both visible and invisible balances!"
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
                        "question": "How does currency devaluation help correct a persistent Balance of Payments deficit?",
                        "options": [
                            "It makes domestic exports cheaper to foreign buyers and imported goods expensive to local citizens",
                            "It increases foreign debt interest rates",
                            "It outlaws all agricultural exports",
                            "It forces the Central Bank to double local cash printing"
                        ],
                        "correct_answer": "It makes domestic exports cheaper to foreign buyers and imported goods expensive to local citizens",
                        "explanation": "Devaluation lowers the relative price of domestic goods abroad (boosting export demand) while making imports expensive at home (reducing import spending)."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: TERMS OF SALE AND TRADE DOCUMENTS (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Terms of Sale and Trade Documents",
    "lesson_title": "Logistics Liability Boundaries, Payment Guarantees, and Customs Documentation",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Terms of Sale and Documents",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain ten terms of sale used in international trade, identify who pays freight and insurance under each quotation, and analyze key trade documents."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Defining Liability Boundaries Matters",
                    "content": {
                        "text": "When importing machinery from Tokyo, you must know where your financial responsibility starts. If quoted 'LOCO', you pay all transport and insurance from the seller's factory. If quoted 'C.I.F. Mombasa', the seller pays freight and insurance up to Mombasa port!"
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Ten International Terms of Sale",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Price Quotations Taxonomy",
                    "content": {
                        "text": "1. LOCO (Ex-works): Base price at exporter factory gate. Importer pays ALL transport & insurance.\n2. F.O.R (Free on Rail): Seller pays transport to nearest rail station.\n3. D.D (Delivered Docks): Seller pays transport to exporting port docks.\n4. F.A.S (Free Alongside Ship): Seller pays to docks + dock handling. Excludes ship loading.\n5. F.O.B (Free on Board): Seller pays up to loading onto ship. Importer pays sea freight & insurance.\n6. C & F (Cost and Freight): Seller pays goods cost + sea freight. Importer buys marine insurance.\n7. C.I.F (Cost, Insurance, Freight): Seller pays goods cost + sea freight + marine insurance to importer port.\n8. In Bond: Seller pays to bonded warehouse. Importer pays storage & customs duty.\n9. Franco (Free Deliver): Seller pays ALL costs, duty, & transport directly to importer door.\n10. O.N.O (Or Nearest Offer): Exporter accepts stated price or close offer."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Terms of Sale Expense & Risk Pipeline",
                    "svg_content": SVG_TERMS_OF_SALE_PIPELINE,
                    "content": {
                        "text": "Horizontal pipeline diagram showing risk and cost transfer checkpoints from LOCO to Franco."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Twelve Key International Trade Documents",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Essential International Trade Documentation",
                    "content": {
                        "text": "1. Letter of Credit (L/C): Issued by importer's bank guaranteeing payment to exporter upon shipping document submission.\n2. Bill of Lading: Contract of carriage, receipt for loaded cargo, and document of title (ownership) for sea freight.\n3. Import License: Government permit granting permission to import specific goods.\n4. Indent: Purchasing order sent to foreign buying agent.\n5. Certificate of Origin: Certifies country of manufacture for preferential tariff determination.\n6. Consular Invoice: Invoice certified by importing country consul to prevent under-invoicing.\n7. Proforma Invoice: Advance price quotation used for customs clearance or pre-payment.\n8. Airway Bill: Air transport consignment note (NOT a document of title).\n9. Letter of Hypothecation: Authorizes bank to sell cargo if importer defaults on payment.\n10. Freight Note: Statement of shipping charges.\n11. Weight Note: Official dock measurement certificate.\n12. Shipping Note: Ship owner cargo details."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Freight Logistics & Cargo Handling",
                    "content": IMG_JKIA_AIR_CARGO
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Letter of Credit vs. Bill of Lading",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Letter of Credit vs. Bill of Lading",
                    "content": {
                        "headers": ["Feature", "Letter of Credit (L/C)", "Bill of Lading"],
                        "rows": [
                            ["Issuing Party", "Importer's Commercial Bank", "Shipping Line / Sea Carrier"],
                            ["Primary Function", "Payment guarantee to exporter", "Contract of carriage, cargo receipt, & document of title"],
                            ["Document of Title", "No (Financial guarantee)", "Yes (Transfers ownership of goods)"],
                            ["Transport Mode", "Used across all transport modes", "Used specifically for sea freight transport"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Cost Comparison: Quote A vs Quote B",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "LOCO vs C.I.F. Cost Comparison Math",
                    "content": {
                        "text": "Problem: Importer buying machinery from Hamburg:\nQuote A: Sh. 8,000,000 LOCO Hamburg.\nQuote B: Sh. 9,100,000 C.I.F. Mombasa.\nAdditional Logistics Expenses:\nFactory to station: Sh. 100,000 | Rail to docks: Sh. 250,000 | Dock loading: Sh. 150,000 | Sea freight: Sh. 450,000 | Marine insurance: Sh. 100,000.\nDetermine which quote is cheaper up to Mombasa port.\n\nSolution:\nPath 1 (Quote A LOCO): Base Sh. 8M + 100k + 250k + 150k + 450k + 100k = Sh. 9,050,000.\nPath 2 (Quote B C.I.F.): Quoted price includes cost + freight + insurance = Sh. 9,100,000.\nConclusion: Quote A (LOCO Hamburg) is cheaper by Sh. 50,000!"
                    }
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
                        "text": "Terms of sale define where financial responsibility shifts from exporter to importer. The Letter of Credit guarantees payment, while the Bill of Lading transfers cargo ownership."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Watch Out: C.I.F. vs C & F",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Insurance Inclusion",
                    "content": {
                        "text": "C.I.F. includes Insurance! C & F includes only Cost and Freight. If quoted C & F, the importer must independently purchase marine insurance to protect cargo against sea hazards."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Check Your Understanding 1",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Document of Title Distinction",
                    "content": {
                        "text": "Why the Bill of Lading is a Document of Title: The holder of the original Bill of Lading has legal ownership of the cargo described. The carrier will ONLY release cargo at the destination port upon presentation of the endorsed Bill of Lading."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Check Your Understanding 2",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Under a F.O.B (Free on Board) Yokohama quotation, who is responsible for paying ocean sea freight and marine insurance?",
                        "options": [
                            "The Japanese Exporter",
                            "The Importer",
                            "The Shipping Company",
                            "The Central Bank"
                        ],
                        "correct_answer": "The Importer",
                        "explanation": "Under F.O.B., the exporter's financial liability ends once goods are loaded onto the ship. The importer must pay sea freight and marine insurance."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Check Your Understanding 3",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Which international trade document provides a financial guarantee from the buyer's bank that payment will be made upon presentation of shipping documents?",
                        "options": [
                            "Bill of Lading",
                            "Letter of Credit",
                            "Airway Bill",
                            "Certificate of Origin"
                        ],
                        "correct_answer": "Letter of Credit",
                        "explanation": "A Letter of Credit is issued by the importer's bank to guarantee payment to the exporter once shipping documents are submitted."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: INTERNATIONAL FINANCIAL INSTITUTIONS (10 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "International Financial Institutions",
    "lesson_title": "Global Monetary Surveillance, Infrastructure Credit, and Development Assistance",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Global Financial Institutions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to identify three key international financial institutions (IMF, World Bank, ADB) and analyze their core objectives, functions, and roles in global trade."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why International Financial Institutions Exist",
                    "content": {
                        "text": "When a nation faces a severe Balance of Payments deficit and runs out of foreign exchange, it cannot print foreign currency. It must turn to international financial institutions for short-term balance of payments support or long-term development loans."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The International Monetary Fund (IMF)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "IMF Objectives & Functions",
                    "content": {
                        "text": "Created at Bretton Woods in 1944, the IMF acts as a global financial referee:\n1. Exchange Rate Stability: Collaborates with members to prevent competitive currency devaluations.\n2. International Cooperation: Provides consultation and monetary coordination.\n3. Liquidity Provision: Holds a pool of member currencies to grant short-term loans to countries facing Balance of Payments deficits."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The African Development Bank (ADB) Group",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "ADB Group Objectives & Structure",
                    "content": {
                        "text": "Established in 1964, the ADB promotes economic and social development across Africa. Comprises three arms: African Development Bank (ADB), African Development Fund (ADF), and Nigeria Trust Fund (NTF). Focuses on long-term infrastructure loans (highways, dams, power grids, agricultural systems)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The World Bank (IBRD)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "World Bank Objectives & Functions",
                    "content": {
                        "text": "Created at Bretton Woods in 1944 (originally for post-WWII European reconstruction). Today focuses on reducing poverty in developing nations through long-term development loans, policy advice, and structural adjustment programs."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "International Financial Institutions Comparison",
                    "svg_content": SVG_INTERNATIONAL_FINANCIAL_INSTITUTIONS_TRIO,
                    "content": {
                        "text": "Structural comparison diagram contrasting IMF, World Bank, and ADB."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "IMF vs. World Bank vs. ADB Comparison",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "Global Financial Institutions Division of Labor",
                    "content": {
                        "headers": ["Institution", "Primary Focus", "Loan Horizon & Target"],
                        "rows": [
                            ["International Monetary Fund (IMF)", "Exchange rate stability & monetary surveillance", "Short-term balance of payments deficit rescue"],
                            ["World Bank (IBRD)", "Global poverty reduction & structural growth", "Long-term development projects & policy loans"],
                            ["African Development Bank (ADB)", "African regional economic development", "Long-term regional infrastructure (highways, dams, grids)"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Global Institution Matcher Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Financial Institution Selection Scenario",
                    "content": {
                        "text": "• Scenario A: Kenya's foreign exchange reserves are depleted by drought, threatening crude oil import payments ---> Turn to the IMF for short-term balance of payments liquidity support.\n• Scenario B: Kenya plans to construct a multi-billion shilling regional power grid linking to Ethiopia ---> Turn to the African Development Bank (ADB) or World Bank for long-term infrastructure credit."
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
                        "text": "The IMF maintains short-term monetary stability and rescues BOP accounts. The World Bank and ADB provide long-term development loans for physical infrastructure and poverty reduction."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: IMF vs World Bank Roles",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Short-Term vs Long-Term",
                    "content": {
                        "text": "Do not confuse the IMF and World Bank! The IMF is for short-term monetary emergencies and exchange rate stability. The World Bank is for long-term physical project financing and poverty reduction."
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
                    "title": "IMF Conditionality",
                    "content": {
                        "text": "IMF loan conditionality: When granting balance of payments emergency loans, the IMF requires borrowing nations to implement macroeconomic reforms (fiscal restraint, currency devaluation, public spending controls) to restore financial equilibrium."
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
                        "question": "Which international financial institution is specifically structured to finance long-term regional infrastructure projects such as highways, dams, and electrical grids across African nations?",
                        "options": [
                            "International Monetary Fund (IMF)",
                            "African Development Bank (ADB) Group",
                            "World Trade Organization (WTO)",
                            "Central Bank of Kenya"
                        ],
                        "correct_answer": "African Development Bank (ADB) Group",
                        "explanation": "The ADB Group focuses specifically on funding long-term regional infrastructure projects to promote social and economic development in Africa."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 5: TRADE RESTRICTIONS, EXCHANGE RATES AND EPZ TRENDS (10 Pages)
# ==============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Trade Restrictions, Exchange Rates and EPZ Trends",
    "lesson_title": "Protectionist Barriers, Foreign Exchange Regimes, and Export Incentive Zones",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Protectionism and EPZs",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define trade protectionism, state six reasons and four methods for trade restriction, evaluate protectionism, explain exchange rate systems, and analyze Export Processing Zones (EPZs)."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Governments Restrict Trade",
                    "content": {
                        "text": "To protect local farmers from cheap imported food or defend local manufacturers from foreign dumping, governments use protectionist tools like tariffs and quotas, while creating EPZ industrial zones to promote export manufacturing."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Six Reasons for Trade Protectionism",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Reasons for Restricting Trade",
                    "content": {
                        "text": "1. Protecting Infant Industries: Young local firms lack economies of scale and cannot survive open foreign competition.\n2. Protecting Strategic Industries: Ensures self-reliance in food, defense, and medicine.\n3. Creating & Protecting Jobs: Encourages local manufacturing growth to employ citizens.\n4. Preventing Dumping: Blocks foreign countries from selling surplus/substandard goods at unnaturally low prices.\n5. Conserving Foreign Exchange: Controls import spending to protect trade balances.\n6. Cultural & Social Protection: Restricts harmful or undesirable foreign goods."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Four Methods of Trade Restriction",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Protectionist Tools",
                    "content": {
                        "text": "1. Tariffs (Customs Duties): Import taxes that raise retail prices of foreign goods, encouraging local purchases.\n2. Quotas & Embargoes: Physical limits on import quantities. Total ban is an embargo.\n3. Foreign Exchange Control: Rationing foreign currency allocations to non-essential importers.\n4. Moral Suasion: Appealing to citizens to voluntarily buy local products."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Economic Impact of Import Tariffs",
                    "svg_content": SVG_TRADE_PROTECTIONISM_EFFECTS,
                    "content": {
                        "text": "Market diagram illustrating the impact of tariffs on import volume, domestic production, and prices."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Foreign Exchange Rate Systems",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Exchange Rate Regimes",
                    "content": {
                        "text": "1. Floating / Fluctuating System: Exchange rate determined purely by market demand and supply of foreign currency.\n2. Fixed System: Currency value fixed by Central Bank against gold or a anchor currency.\n3. Managed / Adjustable Peg System: Currency is pegged but adjusted if structural imbalances occur."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Export Processing Zones (EPZs)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "What is an EPZ?",
                    "content": {
                        "text": "An Export Processing Zone (EPZ) is a designated industrial area set aside by government where firms receive tax holidays and duty-free import privileges to process raw materials into finished exports."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Export Processing Manufacturing",
                    "content": IMG_ATHI_RIVER_EPZ
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Advantages vs Disadvantages of EPZs",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "comparison_table",
                    "title": "EPZ Policy Trade-Offs",
                    "content": {
                        "headers": ["Category", "Advantages of EPZs", "Disadvantages of EPZs"],
                        "rows": [
                            ["Investment & Tax", "Attracts Foreign Direct Investment (FDI)", "Zero short-term tax revenue during tax holidays"],
                            ["Employment", "Creates manufacturing jobs for local labor", "Foreign management dominance in top positions"],
                            ["Industrial Growth", "Transfers modern technology & techniques", "Regional imbalance (concentrated in a few towns)"],
                            ["Trade Balance", "Boosts exports to correct BOP deficits", "Rapid urbanization pressure around zones"]
                        ]
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
                        "text": "Protectionism uses tariffs and quotas to shield local industries. Modern trends balance protection with Export Processing Zones (EPZs) to attract FDI and boost export manufacturing."
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
                        "text": "1. Home vs Foreign Trade: Currency, boundaries, tariffs, laws.\n2. Terms of Sale Definitions: LOCO (factory gate), F.O.B (loaded on ship), C.I.F (cost + freight + marine insurance).\n3. Protectionism Reasons: Infant industry, job protection, anti-dumping, strategic defense.\n4. BOP Correction Tools: Tariffs, quotas, export compensation, devaluation."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Integrated Practice: Paper 2 (BOP Mitigation Essay)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Essay Model Answer: Correcting BOP Deficits",
                    "content": {
                        "text": "Question: Explain five measures Kenya can implement to correct a persistent Balance of Payments deficit (10 Marks).\n\nModel Answer:\n1. Import Tariffs: Levy customs duties on luxury imports to raise retail prices and switch demand to local goods.\n2. Import Quotas: Set statutory volume limits on non-essential imports to cap forex spending.\n3. Foreign Exchange Controls: Ration Central Bank foreign currency allocations to essential importers only.\n4. Export Compensation Schemes: Pay local exporters a percentage of export value to lower global prices and boost sales.\n5. Currency Devaluation: Deliberately lower local currency value to make exports cheap abroad and imports expensive at home."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Integrated Practice: Paper 2 (Protectionism Essay)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Essay Model Answer: Protectionism Benefits & Limitations",
                    "content": {
                        "text": "Question: Discuss five benefits and five limitations of trade protectionism (10 Marks).\n\nModel Answer:\nBenefits:\n1. Shields Infant Industries: Protects young firms from multinational competition.\n2. Job Creation: Boosts domestic production and employment.\n3. Defense Self-Reliance: Ensures strategic food/military independence.\n4. Anti-Dumping: Prevents foreign surplus dumping.\n5. Forex Conservation: Protects trade balances.\n\nLimitations:\n1. Retaliation: Foreign trading partners restrict domestic exports in response.\n2. Lower Quality: Lack of competition leads to poor local products.\n3. High Consumer Prices: Small domestic firms pass high unit costs to consumers.\n4. Reduced Choice: Limits foreign product availability.\n5. Inefficient Monopolies: Protected local firms exploit monopoly power."
                    }
                }
            ]
        }
    ]
}

TOPIC7_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA
]
