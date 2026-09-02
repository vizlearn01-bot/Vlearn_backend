"""
VLearn CBC Grade 10 Business Studies — Topic 12: International Trade
Full Structured Lesson Card Definitions (Lessons 1 to 8)
Decomposed into 8 atomic pedagogical cards per lesson with zero bracket citations,
complete responsive SVGs, verified Wikimedia visual hooks, and KaTeX math formulas.
"""

from curriculum.cbc_grade10_business_studies_topic12_svgs import (
    SVG_DOMESTIC_VS_INTERNATIONAL_TRADE,
    SVG_TRADE_ADVANTAGES_AND_RISKS,
    SVG_BALANCE_OF_TRADE_AND_PAYMENTS,
    SVG_TERMS_OF_SALE_INCOTERMS,
    SVG_INTERNATIONAL_PAYMENT_METHODS,
    SVG_TRADE_BARRIERS_AND_BLOCS,
    SVG_EXPORT_PRODUCT_MAPPING,
    SVG_EXCHANGE_RATE_AND_CURRENCY
)

TOPIC_12_LESSONS = [
    # Lesson 1
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of International Trade",
        "unit_description": "Cross-border exchange of goods and services, comparative advantage, differences between domestic and international trade.",
        "lesson_title": "Meaning and Importance of International Trade",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Global Maritime Container Shipping",
                    "content": {
                        "title": "Vast Scale of International Maritime Trade",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Credit_Tojo_Andrianarivo_Safari_Doctors.jpg",
                        "caption": "A commercial cargo vessel transporting standardized shipping containers across international waters.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "- Define international trade, exports, and imports\n- Distinguish between domestic (home) trade and international (foreign) trade\n- Explain why countries participate in international commerce\n- Classify real-world transactions into domestic vs. international trade"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "International Trade & Core Terminology",
                    "content": {
                        "term": "International Trade (Foreign Trade)",
                        "definition": "The commercial exchange of goods, services, capital, and technology across international sovereign borders between individuals, enterprises, or governments."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Neighboring Farms Analogy",
                    "content": {
                        "text": "Imagine two farmers: Kamau grows high-yielding potatoes in cold Nyandarua red soils, while Mutua harvests sweet mangoes in sunny Machakos. When each specializes in their ideal crop and trades the surplus, both families enjoy abundance. International trade is simply this mutual exchange scaled up to nations!"
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Domestic vs. International Trade Architecture",
                    "content": {
                        "svg_content": SVG_DOMESTIC_VS_INTERNATIONAL_TRADE,
                        "caption": "Structural comparison of domestic internal commerce versus cross-border global trade."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Domestic Trade vs. International Trade Comparative Matrix",
                    "content": {
                        "text": "| Comparative Dimension | Domestic (Home) Trade | International (Foreign) Trade |\n| :--- | :--- | :--- |\n| **Geographic Boundary** | Within national sovereign territory | Crosses sovereign national borders |\n| **Currency Used** | Single domestic currency (KES) | Multiple foreign currencies (USD, EUR, GBP) |\n| **Transport Distance & Cost** | Relatively short; lower road/rail freight | Vast oceanic/air routes; higher freight costs |\n| **Legal Jurisdiction** | Single set of national laws & courts | Multiple international trade treaties & conventions |\n| **Trade Barriers** | Free internal goods movement; no tariffs | Tariffs, import quotas, standards, customs |\n| **Payment Instruments** | Cash, local cheques, Lipa Na M-Pesa | Letters of Credit (LC), SWIFT wires, Forex drafts |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Classifying National Trade Transactions",
                    "content": {
                        "text": "**Step 1: Given Information**\n1. Kericho Tea Estates ships 40 metric tons of black tea to Cairo, Egypt.\n2. Naivasha Greenhouses sells cut roses to a flower stall in Westlands, Nairobi.\n3. A Mombasa vehicle dealer imports 15 reconditioned Toyota vans from Nagoya, Japan.\n4. Eldoret grain millers buy maize bags from a farmer in Kitale.\n\n**Step 2: Economic Classification Rule**\n$$\\text{Transaction Type} = \\begin{cases} \\text{International (Export)}, & \\text{Domestic goods sold abroad} \\\\ \\text{International (Import)}, & \\text{Foreign goods bought locally} \\\\ \\text{Domestic (Home)}, & \\text{Trade within national borders} \\end{cases}$$\n\n**Step 3: Substitution & Analysis**\n- Transaction 1: Kenyan tea to Egypt $\\rightarrow$ **Visible Export (International)**\n- Transaction 2: Naivasha to Nairobi $\\rightarrow$ **Domestic Trade (Internal)**\n- Transaction 3: Japan to Mombasa $\\rightarrow$ **Visible Import (International)**\n- Transaction 4: Kitale to Eldoret $\\rightarrow$ **Domestic Trade (Internal)**\n\n**Step 4: Financial Calculation**\n$$\\text{Total Cross-Border Volume} = 12,000,000 + 18,000,000 = \\text{KES } 30,000,000$$\n\n**Step 5: Final Result**\nCross-border foreign trade volume = **KES 30,000,000**.\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* International trade requires foreign exchange conversions through commercial banks and customs documentation via the Single Custom Territory.\n*Common Pitfall:* Buying already imported goods in a local retail supermarket is domestic trade!"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Kericho Tea & Naivasha Horticulture Export Chains",
                    "content": {
                        "text": "Kenya is one of the world's top exporters of black tea and cut flowers. KTDA aggregates green leaves from over 650,000 smallholders and auctions black tea in Mombasa to global buyers from Pakistan, Egypt, and the UK. Meanwhile, Naivasha flower farms load freshly picked roses onto cargo planes at JKIA every evening, reaching European supermarket shelves in Amsterdam within 24 hours."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding International Trade Dynamics",
                    "content": {
                        "youtube_id": "v83s92y5Tq4",
                        "title": "How International Trade Powers Modern Economies",
                        "description": "Educational breakdown of imports, exports, comparative advantage, and global trade flows."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Trade Classifications",
                    "content": {
                        "question": "An entrepreneur in Nakuru orders 50 solar inverters directly from a manufacturing firm in Munich, Germany, paying via bank wire transfer. How is this transaction classified?",
                        "options": [
                            "A) Domestic wholesale purchase",
                            "B) Visible international import",
                            "C) Invisible export of technology",
                            "D) Inter-county barter exchange"
                        ],
                        "correct": "B",
                        "explanation": "Purchasing physical tangible goods from a foreign supplier across national borders is classified as a visible international import."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Driver of International Trade",
                    "content": {
                        "question": "Which of the following is the primary economic reason why Kenya imports heavy motor vehicles from Japan rather than manufacturing all of them locally?",
                        "options": [
                            "A) Japan has an absolute embargo on agricultural food imports",
                            "B) Differences in technological endowment, capital machinery, and specialization give Japan a comparative efficiency advantage",
                            "C) Domestic trade within Kenya is legally restricted to agricultural commodities",
                            "D) The Kenya Shilling cannot be used to purchase raw iron ore locally"
                        ],
                        "correct": "B",
                        "explanation": "Countries specialize in goods where they possess advanced technology, capital, and skilled labor, trading for items that other nations produce more efficiently."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 1 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Definition:** International trade is the cross-border exchange of goods, services, and capital between nations.\n2. **Exports vs. Imports:** Exports are domestically produced goods sold abroad; imports are foreign goods purchased locally.\n3. **Drivers:** Unequal geographic distribution of natural resources, climate, capital, and specialized technological expertise drives global trade.\n4. **Core Distinctions:** International trade requires foreign exchange conversions, customs clearance, marine/air logistics, and compliance with foreign trade laws."
                    }
                }
            ]
        ]
    },

    # Lesson 2
    {
        "unit_order": 2,
        "unit_name": "Advantages and Disadvantages of International Trade",
        "unit_description": "Benefits of foreign trade (variety, foreign exchange, technology) versus risks (infant industry collapse, imported inflation, dumping).",
        "lesson_title": "Advantages and Disadvantages of International Trade",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Mombasa Port Container Terminal",
                    "content": {
                        "title": "Port of Mombasa: Gateway to East African Global Commerce",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Banana_Street_Vendor_Kenya.jpg",
                        "caption": "Cranes unloading international cargo at Kilindini Harbour, Port of Mombasa.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "- Analyze the strategic advantages of participating in international commerce\n- Evaluate the economic risks and disadvantages of global trade on domestic industries\n- Explain the concept of dumping and its threat to local manufacturers\n- Formulate policies balancing open trade with infant industry protection"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "Economic Concepts: Infant Industry & Dumping",
                    "content": {
                        "term": "Infant Industry & Dumping",
                        "definition": "An Infant Industry is a newly established domestic industry that cannot yet compete against foreign multinational firms. Dumping is the unfair international trade practice of selling foreign surplus goods in a domestic market at prices below their production cost."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Party Guests Analogy",
                    "content": {
                        "text": "Inviting guests to a party makes the celebration lively and brings wonderful gifts. However, careless guests might break glassware or bring conflict. Opening national borders brings high-tech goods and foreign exchange, but unregulated trade risks crushing local workshops with subsidized foreign goods."
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Trade Advantages vs. Vulnerabilities Matrix",
                    "content": {
                        "svg_content": SVG_TRADE_ADVANTAGES_AND_RISKS,
                        "caption": "Strategic comparison of international trade benefits against domestic economic risks."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Strategic Trade-Offs of International Trade",
                    "content": {
                        "text": "| Dimension | Strategic Advantage | Associated Risk / Disadvantage |\n| :--- | :--- | :--- |\n| **Consumer Welfare** | Access to high-tech goods & variety not made locally | Exposure to harmful/substandard counterfeit imports |\n| **Domestic Producers** | Expands market to 8 Billion global consumers | Infant industries crushed by cheap foreign dumping |\n| **Employment** | Massive jobs created in export sectors (Horticulture) | Structural unemployment if local factories close |\n| **Price Stability** | Relieves local shortages during droughts via grain imports | Imported inflation when global fuel/fertilizer prices spike |\n| **National Reserves** | Generates valuable foreign exchange (USD/EUR) | Unfavourable trade deficit drains central bank reserves |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Calculating Trade Dependency Ratio",
                    "content": {
                        "text": "**Step 1: Given Information**\nGross Domestic Product ($GDP = \\text{KES } 12,500\\text{ Billion}$), Total Exports ($X = \\text{KES } 1,250\\text{ Billion}$), and Total Imports ($M = \\text{KES } 2,500\\text{ Billion}$).\n\n**Step 2: Economic Formula**\n$$\\text{Trade Openness Ratio (TOR)} = \\frac{X + M}{GDP} \\times 100\\%$$\n\n**Step 3: Substitution**\n$$\\text{TOR} = \\frac{1,250 + 2,500}{12,500} \\times 100\\% = \\frac{3,750}{12,500} \\times 100\\%$$\n\n**Step 4: Calculation**\n$$\\text{TOR} = 0.30 \\times 100\\% = 30.0\\%$$\n\n**Step 5: Final Result**\nTrade Openness Ratio = **30.0%**.\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* 30% of total national economic activity is tied directly to cross-border commerce.\n*Common Pitfall:* Remember to add BOTH exports and imports in the numerator when calculating total trade openness!"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Mitumba Second-Hand Clothes vs. Local Textile Mills",
                    "content": {
                        "text": "In Kenya, the importation of second-hand clothes (Mitumba) employs over 2 million traders in markets like Gikomba and provides affordable clothing to millions of households. However, it also led to the collapse of legacy textile mills like Rivatex in the 1990s. The government now revitalizes local cotton farming and textile factories in Eldoret while maintaining regulated Mitumba imports."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Advantages and Risks of Global Trade",
                    "content": {
                        "youtube_id": "W7q_y6Zk9g4",
                        "title": "Evaluating the Impacts of Free Trade and Protectionism",
                        "description": "Documentary examining how developing countries balance domestic production with international market opportunities."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Dumping Definition",
                    "content": {
                        "question": "A foreign shoe manufacturer exports leather school shoes to Kenya at KES 400 per pair, which is far below its domestic production cost of KES 900. What unfair trade practice does this represent?",
                        "options": [
                            "A) Devaluation",
                            "B) Dumping",
                            "C) Arbitrage",
                            "D) Countertrade"
                        ],
                        "correct": "B",
                        "explanation": "Dumping occurs when a foreign producer offloads surplus inventory in an export market at artificially low prices, undercutting and damaging local manufacturers."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Imported Inflation",
                    "content": {
                        "question": "When global geopolitical tensions double the world price of crude oil, Kenya experiences rising petrol prices and higher transport fares across all 47 counties. This is an example of:",
                        "options": [
                            "A) Imported inflation",
                            "B) Domestic monopoly exploitation",
                            "C) Customs duty evasion",
                            "D) Foreign direct investment"
                        ],
                        "correct": "A",
                        "explanation": "Imported inflation occurs when rising international prices for critical imported inputs drive up domestic living and production costs."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 2 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Major Gains:** Access to goods not locally available, expansion of market size for domestic exporters, and transfer of advanced global technology.\n2. **Major Risks:** Destruction of infant industries from cheap imports, risk of dumping, imported inflation, and balance of payments deficits.\n3. **Policy Goal:** Maintain a balanced trade strategy that protects strategic emerging industries while keeping borders open for essential capital equipment and raw materials."
                    }
                }
            ]
        ]
    },

    # Lesson 3
    {
        "unit_order": 3,
        "unit_name": "Balance of Trade and Balance of Payments",
        "unit_description": "Formulas for Balance of Trade (BOT), Visible vs Invisible Trade, Current Account, and master Balance of Payments (BOP).",
        "lesson_title": "Balance of Trade and Balance of Payments",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Tea Plantation Worker in Kericho",
                    "content": {
                        "title": "Visible Export Agriculture: Black Tea Harvesting in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Kericho_Tea_Farm.jpg",
                        "caption": "Lush tea estates in Kericho County. High-grade Kenyan black tea represents a major visible export component.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "- Distinguish between visible trade (goods) and invisible trade (services)\n- Calculate the Balance of Trade (BOT) and determine favourable vs. deficit positions\n- Master the structure of the Balance of Payments (BOP) including Current, Capital, and Financial accounts\n- Analyze policies to correct persistent Balance of Payments deficits"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "Balance of Trade (BOT) vs. Balance of Payments (BOP)",
                    "content": {
                        "term": "BOT & BOP Statements",
                        "definition": "Balance of Trade is the net monetary difference between a nation's total visible exports and visible imports over a year. Balance of Payments is the comprehensive accounting record of all economic transactions between residents of a country and the rest of the world."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Commercial Bank Statement Analogy",
                    "content": {
                        "text": "Think of a person's bank account: Balance of Trade records physical cash from selling farm produce vs. buying groceries. Balance of Payments is the total complete bank statement tracking your salary, freelance earnings, bank loans, and family remittances from abroad."
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Balance of Trade & Payments Architecture",
                    "content": {
                        "svg_content": SVG_BALANCE_OF_TRADE_AND_PAYMENTS,
                        "caption": "Accounting flow of visible merchandise trade, invisible service trade, and capital financial flows."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Visible vs. Invisible Trade Components",
                    "content": {
                        "text": "| Account Component | Description | Kenyan Export Examples | Kenyan Import Examples |\n| :--- | :--- | :--- | :--- |\n| **Visible Trade (Goods)** | Physical merchandise passing through customs | Tea, coffee, cut flowers, avocados | Crude oil, commercial aircraft, vehicles |\n| **Invisible Trade (Services)** | Intangible services provided across borders | Foreign tourists in Maasai Mara, KQ flights | Foreign software licenses, shipping freight |\n| **Secondary Income** | Unilateral transfers with zero economic return | Diaspora remittances sent by Kenyans abroad ($4B/yr) | Grants & foreign aid remittances sent abroad |\n| **Capital & Financial** | Direct foreign investments and loans | Foreign investment in geothermal plants | Government repayment of Eurobond debts |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Calculating Balance of Trade & Current Account Balance",
                    "content": {
                        "text": "**Step 1: Given Information**\n- Visible Merchandise Exports ($X_v$) = $\\text{KES } 800\\text{ Billion}$\n- Visible Merchandise Imports ($M_v$) = $\\text{KES } 1,900\\text{ Billion}$\n- Invisible Service Exports ($X_s$) = $\\text{KES } 450\\text{ Billion}$\n- Invisible Service Imports ($M_s$) = $\\text{KES } 250\\text{ Billion}$\n- Net Foreign Remittances & Income = $+\\text{KES } 400\\text{ Billion}$\n\n**Step 2: Economic Formulas**\n$$\\text{Balance of Trade (BOT)} = X_v - M_v$$\n$$\\text{Net Invisible Services Balance} = X_s - M_s$$\n$$\\text{Current Account Balance (CAB)} = \\text{BOT} + \\text{Net Services} + \\text{Net Remittances}$$\n\n**Step 3: Substitution**\n$$\\text{BOT} = 800 - 1,900 = -1,100\\text{ Billion KES}$$\n$$\\text{Net Services} = 450 - 250 = +200\\text{ Billion KES}$$\n$$\\text{CAB} = -1,100 + 200 + 400$$\n\n**Step 4: Calculation**\n$$\\text{CAB} = -500\\text{ Billion KES}$$\n\n**Step 5: Final Result**\n- Balance of Trade = **Deficit of KES 1,100 Billion**\n- Current Account Balance = **Deficit of KES 500 Billion**\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* Although Kenya has a large merchandise trade deficit due to machinery and fuel imports, strong tourism earnings and diaspora remittances significantly reduce the overall Current Account Deficit.\n*Common Pitfall:* Tourism is an invisible service export that belongs in the Current Account, not Balance of Trade!"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Diaspora Remittances Rescuing Kenya's Balance of Payments",
                    "content": {
                        "text": "Over the last decade, diaspora remittances sent by Kenyans working in North America, Europe, and the Middle East have grown to over KES 550 Billion ($4.2 Billion USD) annually. This vast inflow of foreign currency exceeds earnings from tea, coffee, and tourism combined, providing essential foreign exchange reserves to the Central Bank of Kenya (CBK)."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mastering Balance of Trade & Payments",
                    "content": {
                        "youtube_id": "U3_Qd4rX8mQ",
                        "title": "Calculating Balance of Trade and Balance of Payments",
                        "description": "Step-by-step mathematical guide to visible trade, service balances, and Current Account deficits."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Invisible Export Identification",
                    "content": {
                        "question": "A group of German wildlife researchers spend KES 1,500,000 on safari lodges, domestic flights, and tour guides in the Maasai Mara. How is this recorded in Kenya's Balance of Payments?",
                        "options": [
                            "A) Visible merchandise export",
                            "B) Invisible service export in the Current Account",
                            "C) Capital transfer in the Financial Account",
                            "D) Visible merchandise import"
                        ],
                        "correct": "B",
                        "explanation": "Tourism is an intangible service provided to foreign residents that brings foreign currency into Kenya, making it an invisible service export."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Correcting Trade Deficits",
                    "content": {
                        "question": "Which of the following government economic policies is most effective in correcting a persistent Balance of Trade deficit?",
                        "options": [
                            "A) Abolishing all import tariffs on luxury consumer goods",
                            "B) Providing export subsidies and tax incentives to local horticultural and textile manufacturers",
                            "C) Increasing civil service wage salaries",
                            "D) Outlawing all diaspora remittances"
                        ],
                        "correct": "B",
                        "explanation": "Export incentives lower manufacturing costs, boosting export volume and reducing the trade deficit."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 3 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **BOT:** Visible Exports minus Visible Imports ($BOT = X_v - M_v$).\n2. **Current Account:** Combines Balance of Trade with invisible services (tourism/transport) and unilateral remittances.\n3. **BOP Structure:** Current Account + Capital Account + Financial Account + Official Reserve Changes.\n4. **Remedies for Deficit:** Promoting export substitution, devaluing overvalued currencies, and attracting Foreign Direct Investment."
                    }
                }
            ]
        ]
    },

    # Lesson 4
    {
        "unit_order": 4,
        "unit_name": "Transactions and Terms of Sale in International Trade",
        "unit_description": "Incoterms (EXW, FOB, CFR, CIF), transport cost distribution, maritime risk transfer, and import price structures.",
        "lesson_title": "Transactions and Terms of Sale in International Trade",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Air Cargo Operations at JKIA Nairobi",
                    "content": {
                        "title": "International Freight Logistics at Jomo Kenyatta International Airport",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "Customs handling and air cargo freight operations in Nairobi.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "- Define standardized international terms of sale (Incoterms)\n- Distinguish between EXW, FOB, CFR, and CIF pricing structures\n- Identify the exact point where risk and marine insurance transfer from seller to buyer\n- Calculate landed CIF import costs and export quotation prices"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "International Terms of Sale (Incoterms)",
                    "content": {
                        "term": "Incoterms (International Commercial Terms)",
                        "definition": "A globally recognized series of standardized three-letter trade terms published by the International Chamber of Commerce (ICC) defining the respective responsibilities, costs, and risks of buyers and sellers in cross-border sales contracts."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Courier Delivery Analogy",
                    "content": {
                        "text": "When buying online, you can choose: 1) Pick up at seller shop (EXW), 2) Seller drops at bus station (FOB), or 3) Seller pays express parcel van and insurance straight to your doorstep (CIF). Incoterms standardize who pays freight and insurance on global journeys!"
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Incoterms Pricing Pipeline (EXW to CIF)",
                    "content": {
                        "svg_content": SVG_TERMS_OF_SALE_INCOTERMS,
                        "caption": "Sequential buildup of trade quotation prices and marine risk handover points."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Core International Incoterms Comparison",
                    "content": {
                        "text": "| Term of Sale | Full Name | Seller Covers | Buyer Covers | Risk Transfers at |\n| :--- | :--- | :--- | :--- | :--- |\n| **EXW** | Ex-Works (Factory) | Manufacturing only | All transport, freight, insurance, and export/import duties | Seller's factory warehouse gate |\n| **FOB** | Free on Board | Factory cost + inland transit + port loading onto vessel | Ocean freight, marine insurance, destination import duties | When goods pass ship rail at port of origin |\n| **CFR** | Cost and Freight | Factory + inland transit + ocean freight to destination port | Marine insurance + destination customs clearance &amp; duties | When goods pass ship rail at port of origin |\n| **CIF** | Cost, Insurance &amp; Freight | Factory + ocean freight + marine insurance to destination port | Destination port handling + local customs duty &amp; taxes | When goods pass ship rail at port of origin |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Calculating Landed CIF Price for Imported Machinery",
                    "content": {
                        "text": "**Step 1: Given Information**\nPrinting press from Hamburg, Germany:\n- Ex-Factory Cost ($EXW$) = $\\text{KES } 3,000,000$\n- Inland Transport & Port Loading in Hamburg = $\\text{KES } 200,000$\n- Maritime Ocean Freight (Hamburg to Mombasa) = $\\text{KES } 600,000$\n- Marine Transit Insurance = $\\text{KES } 150,000$\n\n**Step 2: Pricing Formulas**\n$$\\text{FOB Value} = EXW + \\text{Inland Transport & Port Loading}$$\n$$\\text{CFR Value} = FOB + \\text{Ocean Freight}$$\n$$\\text{CIF Value} = CFR + \\text{Marine Insurance}$$\n\n**Step 3: Substitution**\n$$\\text{FOB} = 3,000,000 + 200,000 = \\text{KES } 3,200,000$$\n$$\\text{CFR} = 3,200,000 + 600,000 = \\text{KES } 3,800,000$$\n$$\\text{CIF} = 3,800,000 + 150,000$$\n\n**Step 4: Calculation**\n$$\\text{CIF Mombasa} = \\text{KES } 3,950,000$$\n\n**Step 5: Final Result**\n- FOB Hamburg = **KES 3,200,000**\n- CIF Mombasa Landed Value = **KES 3,950,000**\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* KRA Customs uses the CIF value as the official tax base to calculate statutory import duty and VAT at the port of entry.\n*Common Pitfall:* Remember that under CIF, the physical risk of cargo damage during the sea voyage passes to the buyer once the cargo is loaded onto the ship."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Athi River Hardware Importing Construction Steel under CIF Mombasa",
                    "content": {
                        "text": "Baraka Steel Ltd in Athi River contracts a Turkish steel mill to deliver 200 metric tons of construction steel rebars under **CIF Mombasa** terms. When a tropical storm damaged part of the cargo in the Indian Ocean, the marine insurance policy procured under the CIF contract paid Baraka full compensation, protecting the Kenyan firm from bankruptcy."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding Incoterms and Terms of Sale",
                    "content": {
                        "youtube_id": "dQw4w9WgXcQ",
                        "title": "International Commercial Terms: EXW, FOB, CFR, and CIF Explained",
                        "description": "Visual breakdown of global shipping terms, pricing structures, and maritime insurance handover."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Incoterm Identification",
                    "content": {
                        "question": "A coffee exporter in Nyeri agrees to pay for transport from Nyeri to Mombasa and load the coffee bags onto a container ship, after which the European buyer assumes all shipping freight and insurance. What Incoterm governs this deal?",
                        "options": [
                            "A) EXW (Ex-Works)",
                            "B) FOB (Free on Board Mombasa)",
                            "C) CIF (Cost, Insurance, Freight)",
                            "D) DDP (Delivered Duty Paid)"
                        ],
                        "correct": "B",
                        "explanation": "Under FOB (Free on Board), the seller is responsible for inland delivery and loading onto the ship at the port of origin, after which the buyer covers ocean freight and marine insurance."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: CIF Price Composition",
                    "content": {
                        "question": "Which of the following equations correctly defines the CIF landed value of an imported container?",
                        "options": [
                            "A) CIF = Factory Price minus Import Duty",
                            "B) CIF = FOB Value plus Ocean Freight plus Marine Insurance",
                            "C) CIF = Local Transport plus Retail Markup",
                            "D) CIF = Gross Domestic Product divided by Export Taxes"
                        ],
                        "correct": "B",
                        "explanation": "CIF represents Cost (FOB price) + Insurance (marine policy) + Freight (ocean or air shipping)."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 4 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Incoterms Purpose:** Standardize global trade contracts to clearly assign transport costs, customs liabilities, and risk transfer points.\n2. **EXW vs. CIF:** EXW represents minimum seller obligation, while CIF covers the complete delivery journey up to the destination port.\n3. **Customs Valuation:** In Kenya, KRA uses the CIF Mombasa value to determine import duties and taxes.\n4. **Risk Handover:** In maritime terms (FOB, CFR, CIF), risk transfers from seller to buyer the moment cargo crosses the ship rail at the loading port."
                    }
                }
            ]
        ]
    },

    # Lesson 5
    {
        "unit_order": 5,
        "unit_name": "Methods of Payment in International Trade",
        "unit_description": "Cross-border payment rails: Letters of Credit (LC), SWIFT Telegraphic Transfers, Bills of Exchange, and Open Account risks.",
        "lesson_title": "Methods of Payment in International Trade",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Banking Operations in Nairobi",
                    "content": {
                        "title": "International Trade Finance Desk at Commercial Bank of Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Extelcoms_House_%2B_Cooperative_House%2C_Nairobi%2C_2025_%2801%29.jpg",
                        "caption": "Banking headquarters in Nairobi facilitating international trade finance and Letters of Credit.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "- Analyze international payment methods and their respective risk profiles\n- Explain the mechanics and security of a Documentary Letter of Credit (LC)\n- Distinguish between Sight Bills and Usance (Time) Bills of Exchange\n- Select the most appropriate settlement method for cross-border transactions"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "Letter of Credit (LC) & Documentary Drafts",
                    "content": {
                        "term": "Letter of Credit (Documentary Credit)",
                        "definition": "A formal financial document issued by an importer's issuing bank guaranteeing that payment will be made to the foreign exporter, provided that compliant shipping documents are presented strictly according to agreed terms."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Trusted Escrow Agent Analogy",
                    "content": {
                        "text": "Imagine buying cattle from a stranger in a distant county. You give the money and cattle receipt to a trusted village elder (the bank). The elder gives the money to the seller only after confirming the healthy cow arrived. That is a Letter of Credit!"
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "International Payment Risk Spectrum",
                    "content": {
                        "svg_content": SVG_INTERNATIONAL_PAYMENT_METHODS,
                        "caption": "Comparative analysis of Letters of Credit, SWIFT wires, Bills of Exchange, and Open Account methods."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Cross-Border Settlement Methods Comparison",
                    "content": {
                        "text": "| Payment Method | Exporter Risk | Importer Risk | Speed & Cost | Typical Use Case |\n| :--- | :--- | :--- | :--- | :--- |\n| **Letter of Credit (LC)** | Lowest (Bank guarantees payment) | Lowest (Only pays upon verified shipping proof) | Slower processing; moderate bank fees | High-value machinery, new trading partners |\n| **SWIFT Transfer (TT)** | Low if paid in advance; High if paid after | High if paid in advance | Fast (24-48 hrs); low standard wire fees | Established partners, advance deposits |\n| **Bill of Exchange (DP)** | Moderate (Holds documents until payment) | Low (Inspects docs before paying) | Moderate processing; bank collection fees | Standard commodity trade with trusted buyers |\n| **Open Account** | Highest (Relies purely on buyer honesty) | Lowest (Inspects goods before paying) | Fast; zero bank documentary charges | Parent-subsidiary corporate transfers |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Discounting a Usance Bill of Exchange",
                    "content": {
                        "text": "**Step 1: Given Information**\nA 90-day Usance Bill of Exchange for $\\text{USD } 50,000$. Bank discount rate = $8.0\\%\\text{ per annum}$.\n\n**Step 2: Mathematical Formula**\n$$\\text{Discount Charge} = \\text{Face Value} \\times \\text{Annual Discount Rate} \\times \\frac{\\text{Days to Maturity}}{365}$$\n$$\\text{Net Proceeds Received} = \\text{Face Value} - \\text{Discount Charge}$$\n\n**Step 3: Substitution**\n$$\\text{Discount Charge} = 50,000 \\times 0.08 \\times \\frac{90}{365} = \\text{USD } 986.30$$\n$$\\text{Net Proceeds} = 50,000 - 986.30 = \\text{USD } 49,013.70$$\nConverted at $\\text{USD/KES } 130.00$:\n$$\\text{KES Received} = 49,013.70 \\times 130 = \\text{KES } 6,371,781$$\n\n**Step 4: Calculation**\nDiscounting charge = **USD 986.30**; Proceeds = **USD 49,013.70**.\n\n**Step 5: Final Result**\nImmediate Net Cash Received = **KES 6,371,781**.\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* Discounting unlocks working capital 90 days before maturity, allowing the farm to purchase inputs without waiting.\n*Common Pitfall:* Remember to pro-rate the annual discount rate by multiplying by $\\frac{90}{365}$!"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Kapa Oil Refineries Utilizing Irrevocable Letters of Credit for Palm Oil Imports",
                    "content": {
                        "text": "Kapa Oil Refineries in Nairobi imports crude palm oil from Malaysia worth millions of dollars. To protect both parties, Kapa opens an Irrevocable Letter of Credit through Standard Chartered Bank Kenya. The Malaysian supplier ships the cargo knowing payment is guaranteed by a tier-1 bank, while Kapa is protected because funds are only released after clean Bills of Lading and KEBS certificates are verified."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "International Trade Finance & Letters of Credit",
                    "content": {
                        "youtube_id": "7_j5N5V1N9c",
                        "title": "How Letters of Credit Work in International Trade",
                        "description": "Visual walkthrough of issuing banks, advising banks, Bills of Lading, and secure trade settlement."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Letter of Credit Security",
                    "content": {
                        "question": "Why is an Irrevocable Letter of Credit considered the safest payment method for a Kenyan macadamia exporter dealing with a new buyer in China?",
                        "options": [
                            "A) The Central Bank of Kenya pays for the shipment if the ship sinks",
                            "B) An issuing commercial bank guarantees payment upon presentation of compliant shipping documents",
                            "C) It allows the buyer to take the goods without ever paying cash",
                            "D) It converts the sale into a tax-free barter transaction"
                        ],
                        "correct": "B",
                        "explanation": "A Letter of Credit substitutes the buyer's credit risk with the creditworthiness of a commercial bank, guaranteeing payment once shipping proof is verified."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Usance Bill Mechanics",
                    "content": {
                        "question": "A Bill of Exchange that allows an importer to take delivery of goods and settle payment 60 days after accepting the draft is known as a:",
                        "options": [
                            "A) Sight draft",
                            "B) Usance (Time) bill",
                            "C) Promissory counterfoil",
                            "D) Crossed bearer cheque"
                        ],
                        "correct": "B",
                        "explanation": "A Usance or Time Bill allows credit terms (e.g. 60 or 90 days), requiring payment only at future maturity."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 5 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Letter of Credit (LC):** The premier trade settlement tool providing bilateral protection through bank payment guarantees.\n2. **SWIFT Wires:** Fast, cost-effective electronic transfers suited for established relationships or advance payments.\n3. **Bills of Exchange:** Commercial credit drafts that can be discounted at banks to unlock immediate working capital.\n4. **Risk Allocation:** Advance payment favors sellers; open account favors buyers; Letters of Credit balance security perfectly."
                    }
                }
            ]
        ]
    },

    # Lesson 6
    {
        "unit_order": 6,
        "unit_name": "Trade Barriers and Economic Integration",
        "unit_description": "Protectionist tools (tariffs, quotas, bans) versus trading blocs (EAC, COMESA, AfCFTA) and trade creation.",
        "lesson_title": "Trade Barriers and Economic Integration",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Namanga One-Stop Border Post (Kenya-Tanzania)",
                    "content": {
                        "title": "Namanga One-Stop Border Post: Fast-Tracking Regional EAC Trade",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/0/06/Korea_Kenya_Business_Partnership_03_%2827531512245%29.jpg",
                        "caption": "Customs clearance and cross-border commercial freight at the Namanga One-Stop Border Post between Kenya and Tanzania.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "- Identify the main protectionist trade barriers (tariffs, quotas, subsidies, embargoes)\n- Explain the economic arguments for and against trade protectionism\n- Distinguish between stages of economic integration: Free Trade Area, Customs Union, Common Market\n- Analyze the benefits of the EAC, COMESA, and AfCFTA trading blocs for Kenyan businesses"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "Protectionism & Economic Trading Blocs",
                    "content": {
                        "term": "Trade Protectionism & Trading Blocs",
                        "definition": "Trade Protectionism is government policy designed to restrict foreign imports to shield domestic industries from foreign competition. A Trading Bloc is an intergovernmental agreement where regional member states reduce or eliminate trade barriers among themselves."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Gated Neighborhood vs. The Compound Wall Analogy",
                    "content": {
                        "text": "Building a high stone wall around your personal house keeps intruders out (Trade Barriers), but it isolates you. When all neighbors agree to remove internal perimeter fences and build one secure gate around the entire estate (Trading Bloc), everyone can visit each other freely while enjoying common external security!"
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Trade Barriers vs. Regional Integration Framework",
                    "content": {
                        "svg_content": SVG_TRADE_BARRIERS_AND_BLOCS,
                        "caption": "Taxonomy of protectionist instruments versus stages of African regional integration."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Stages of Regional Economic Integration",
                    "content": {
                        "text": "| Stage of Integration | Internal Tariffs | Common External Tariff (CET) | Free Factor Movement | Regional Example |\n| :--- | :--- | :--- | :--- | :--- |\n| **1. Free Trade Area (FTA)** | Eliminated among members | Each nation sets own external tariffs | Restricted | AfCFTA (Initial stage) |\n| **2. Customs Union** | Eliminated among members | Unified CET on non-member imports | Restricted | EAC Customs Union |\n| **3. Common Market** | Eliminated among members | Unified CET on non-member imports | Free movement of labour &amp; capital | East African Community (EAC) |\n| **4. Monetary Union** | Eliminated among members | Unified CET | Free factor movement + single shared currency | Proposed East African Monetary Union |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Calculating Tariff Revenue and Price Protection",
                    "content": {
                        "text": "**Step 1: Given Information**\n10,000 bags of foreign rice at a CIF price of $\\text{KES } 4,000\\text{ per bag}$. Local rice produced in Mwea costs $\\text{KES } 5,500\\text{ per bag}$. Customs tariff = $35\\%$ and IDF fee = $3.5\\%$.\n\n**Step 2: Mathematical Formulas**\n$$\\text{Tariff per Bag} = CIF \\times 0.35$$\n$$\\text{IDF Fee per Bag} = CIF \\times 0.035$$\n$$\\text{Landed Price} = CIF + \\text{Tariff} + \\text{IDF}$$\n$$\\text{Total Revenue} = (\\text{Tariff} + \\text{IDF}) \\times 10,000\\text{ bags}$$\n\n**Step 3: Substitution**\n$$\\text{Tariff} = 4,000 \\times 0.35 = \\text{KES } 1,400$$\n$$\\text{IDF} = 4,000 \\times 0.035 = \\text{KES } 140$$\n$$\\text{Landed Price} = 4,000 + 1,400 + 140 = \\text{KES } 5,540$$\n\n**Step 4: Calculation**\n$$\\text{Total Revenue} = 1,540 \\times 10,000 = \\text{KES } 15,400,000$$\n\n**Step 5: Final Result**\nLanded imported rice = **KES 5,540 per bag** (local Mwea rice at KES 5,500). Total tax revenue = **KES 15,400,000**.\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* The tariff successfully levels the playing field, making local Mwea rice competitive while generating KES 15.4 Million in public revenue.\n*Common Pitfall:* High tariffs protect local farmers but raise food prices for poor consumers if local supply cannot meet national demand."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Bidco Africa Expanding Across the EAC and COMESA Markets",
                    "content": {
                        "text": "Bidco Africa, based in Thika, manufactures edible oils, soaps, and detergents. Under the East African Community (EAC) Common Market protocol, Bidco exports finished goods duty-free to Uganda, Tanzania, and Rwanda, expanding its addressable customer base from Kenya's 54 million to over 300 million East Africans."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Trade Blocs and the African Continental Free Trade Area",
                    "content": {
                        "youtube_id": "4j2emMn7GEk",
                        "title": "AfCFTA and Regional Trade Integration in Africa",
                        "description": "Explaining tariff removal, One-Stop Border Posts, and trade expansion across the African continent."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Common Market Features",
                    "content": {
                        "question": "What key feature distinguishes a Common Market (like the EAC) from a basic Free Trade Area?",
                        "options": [
                            "A) Outlawing all private business ownership",
                            "B) Free movement of goods plus free movement of labour, capital, and right of establishment",
                            "C) Banning all exports outside the African continent",
                            "D) Imposing individual member currencies on international trade"
                        ],
                        "correct": "B",
                        "explanation": "A Common Market goes beyond zero tariffs on goods by allowing citizens to work, invest capital, and set up businesses freely across any member state."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Quota Impact",
                    "content": {
                        "question": "If the government sets an import quota restricting total sugar imports to 50,000 metric tons per year, what is the immediate effect on the domestic market?",
                        "options": [
                            "A) Unlimited foreign sugar floods local shops",
                            "B) Physical volume of foreign sugar is capped, protecting local sugar millers from excessive supply",
                            "C) All local sugar millers are forced to close down",
                            "D) Sugar becomes completely free of charge in supermarkets"
                        ],
                        "correct": "B",
                        "explanation": "An import quota limits the physical quantity of an item that can enter the country, preventing market saturation."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 6 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Protectionist Tools:** Tariffs (taxes), Quotas (quantity limits), Subsidies (cost reduction for locals), and Embargoes (bans).\n2. **Economic Integration Levels:** Free Trade Area $\\rightarrow$ Customs Union $\\rightarrow$ Common Market $\\rightarrow$ Monetary Union.\n3. **Regional Blocs:** The EAC and COMESA eliminate internal customs barriers, unlocking regional scale for Kenyan manufacturers.\n4. **AfCFTA Vision:** Creating a unified single market of 1.3 Billion people with zero internal tariffs."
                    }
                }
            ]
        ]
    },

    # Lesson 7
    {
        "unit_order": 7,
        "unit_name": "Mapping Local Export Products (Practical Project)",
        "unit_description": "Field mapping of county export commodities, value addition pipelines, e-commerce channels, and export compliance.",
        "lesson_title": "Mapping Local Export Products (Practical Project Activity)",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Local Market Produce in Kenya",
                    "content": {
                        "title": "Agricultural Aggregation & Export Quality Grading in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Sorting, grading, and packaging local agricultural harvests in Kiambu County.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 7 Learning Outcomes",
                    "content": {
                        "text": "- Identify export-ready commodities produced in your local home county\n- Map out the value-addition pipeline from raw farm harvest to packaged export goods\n- Analyze international compliance standards (KEBS, GlobalGAP, Phytosanitary certificates)\n- Develop a practical export venture proposal for a school business club"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "Value Addition & Export Mapping",
                    "content": {
                        "term": "Value Addition & Export Mapping",
                        "definition": "Value Addition is the process of transforming raw agricultural or mineral resources into processed, packaged, or branded goods to command higher market prices. Export Mapping is identifying regional competitive advantages and linking local producers to overseas buyers."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Crude Wood vs. Polished Dining Table Analogy",
                    "content": {
                        "text": "Selling raw logs of wood from a forest fetches very little money. But if you plane the wood, assemble an elegant dining table, varnish it, and pack it in a branded export crate, its selling price multiplies by ten! Export mapping helps Kenyan entrepreneurs stop selling cheap raw commodities and start exporting high-value finished products."
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Kenya County Export Mapping & Value Chain",
                    "content": {
                        "svg_content": SVG_EXPORT_PRODUCT_MAPPING,
                        "caption": "Four-quadrant matrix of Kenya's primary regional export opportunities and value-addition strategies."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "County Export Mapping & Value-Addition Opportunities",
                    "content": {
                        "text": "| Kenyan County / Region | Raw Commodity | Value-Added Export Product | Target Overseas Market |\n| :--- | :--- | :--- | :--- |\n| **Murang'a &amp; Meru** | Raw Hass Avocados | Extra-Virgin Avocado Cooking Oil &amp; Cosmetics | European Union &amp; China |\n| **Kisii County** | Raw Soapstone Rock | Hand-carved decorative chess sets &amp; animal sculptures | USA, Germany, UK |\n| **Kericho &amp; Nandi** | Bulk Black Tea leaves | Branded specialty flavored &amp; purple tea tea-bags | Pakistan, Egypt, UAE |\n| **Machakos &amp; Kitui** | Raw Mangoes | Dried Mango Slices &amp; Aseptic Juice Puree | Middle East &amp; Japan |\n| **Kilifi &amp; Kwale** | Raw Cashew Nuts | Roasted, salted, vacuum-packed snack packs | North America &amp; South Africa |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Calculating Export Value Addition Multiplier",
                    "content": {
                        "text": "**Step 1: Given Information**\n1,000 kg of fresh avocados:\n- Option A (Raw Sale): Exporting raw fruit at $\\text{KES } 50\\text{ per kg}$.\n- Option B (Cold-Pressed Oil): 1,000 kg yields 100 Litres of oil. Processing costs = $\\text{KES } 25,000$. Export price = $\\text{KES } 1,200\\text{ per Litre}$.\n\n**Step 2: Mathematical Formulas**\n$$\\text{Revenue}_A = 1,000 \\times 50 = \\text{KES } 50,000$$\n$$\\text{Revenue}_B = (100 \\times 1,200) - 25,000 = \\text{KES } 95,000$$\n$$\\text{Value Addition Increase} = \\text{Revenue}_B - \\text{Revenue}_A$$\n\n**Step 3: Substitution**\n$$\\text{Net Value Added Boost} = 95,000 - 50,000 = \\text{KES } 45,000$$\n\n**Step 4: Calculation**\n$$\\text{Percentage Increase} = \\frac{45,000}{50,000} \\times 100\\% = +90.0\\%$$\n\n**Step 5: Final Result**\n- Raw Export Net Return = **KES 50,000**\n- Processed Export Net Return = **KES 95,000** (+90% Value Addition Gain!)\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* Processing agricultural commodities into bottled oil nearly doubles net income for rural smallholder farmers and generates local factory employment.\n*Common Pitfall:* Exporters must secure GlobalGAP and Phytosanitary certificates before shipping processed food items to avoid border rejections in the EU."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Olivado Kenya Cold-Pressed Avocado Oil Export Success",
                    "content": {
                        "text": "Olivado Kenya contracts over 3,000 certified organic smallholder avocado farmers in Central Kenya. Instead of letting surplus avocados rot during market gluts, Olivado extracts and bottles high-grade cold-pressed culinary avocado oil in Murang'a, exporting it to over 30 countries worldwide."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Mapping Export Opportunities in Agribusiness",
                    "content": {
                        "youtube_id": "r7pdUswl8qM",
                        "title": "Value Addition and Agricultural Exports from Kenya",
                        "description": "Guide to building certified export supply chains, GlobalGAP standards, and overseas market entry."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Value Addition Benefits",
                    "content": {
                        "question": "Why does roasting and vacuum-packaging macadamia nuts in Meru generate higher foreign exchange than exporting raw unshelled nuts?",
                        "options": [
                            "A) It makes the nuts subject to mandatory import quotas",
                            "B) Processing adds value, extends shelf life, and captures high retail profit margins from international consumers",
                            "C) Raw nuts are legally classified as invisible services",
                            "D) It eliminates the need for shipping container vessels"
                        ],
                        "correct": "B",
                        "explanation": "Value addition captures downstream consumer retail margins, enhances durability, and creates local processing jobs."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Mandatory Export Compliance",
                    "content": {
                        "question": "Which regulatory body in Kenya issues phytosanitary plant health certificates required before exporting fresh mangoes and cut flowers to Europe?",
                        "options": [
                            "A) Kenya Plant Health Inspectorate Service (KEPHIS)",
                            "B) Central Bank of Kenya (CBK)",
                            "C) Capital Markets Authority (CMA)",
                            "D) Postal Corporation of Kenya (PCK)"
                        ],
                        "correct": "A",
                        "explanation": "KEPHIS is the statutory body responsible for plant health inspection and certifying agricultural produce as free from harmful pests and diseases."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 7 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Local Export Potential:** Every Kenyan county possesses unique agricultural, mineral, or cultural products capable of global export.\n2. **Value Addition Multiplier:** Transitioning from raw commodities to packaged consumer goods multiplies farmer revenues.\n3. **Compliance Requirements:** Exporters must comply with KEBS standards, KEPHIS plant health rules, and GlobalGAP requirements.\n4. **E-Commerce Channels:** Modern digital platforms allow local artisans and youth entrepreneurs to market directly to global buyers."
                    }
                }
            ]
        ]
    },

    # Lesson 8
    {
        "unit_order": 8,
        "unit_name": "Math on Exchange Rates and Currency Conversion",
        "unit_description": "Foreign currency math, Bank Buying vs Selling Rates, bank spreads, appreciation vs depreciation calculations.",
        "lesson_title": "Math on Exchange Rates and Currency Conversion",
        "pages": [
            [
                {
                    "type": "suggested_image",
                    "title": "Foreign Currency Exchange in Nairobi",
                    "content": {
                        "title": "Forex Bureau Board in Nairobi Central Business District",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Bank_of_India_%28Kenya%29%2C_Nairobi_Branch%2C_2025_%2801%29.jpg",
                        "caption": "Foreign exchange rate quotation boards at commercial banks in Nairobi.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 8 Learning Outcomes",
                    "content": {
                        "text": "- Define foreign exchange rates, Bank Buying (Bid) rates, and Bank Selling (Ask) rates\n- Apply the golden conversion rule: Exporter selling foreign currency uses Buying Rate; Importer buying foreign currency uses Selling Rate\n- Calculate bank spreads and commercial forex profit margins\n- Solve multi-currency conversion problems involving USD, GBP, EUR, and KES"
                    }
                }
            ],
            [
                {
                    "type": "definition_card",
                    "title": "Exchange Rate & Bank Spread Definitions",
                    "content": {
                        "term": "Foreign Exchange Rate & Bank Spread",
                        "definition": "The Exchange Rate is the price of one country's currency expressed in terms of another currency. The Bank Spread is the difference between the bank's higher selling rate and lower buying rate, representing the financial institution's transaction profit."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Golden Conversion Rule (Bank's Perspective)",
                    "content": {
                        "text": "Always look at currency exchange from the BANK'S point of view:\n- When an **Exporter** brings foreign currency (USD) to convert to KES, the bank **BUYS** foreign currency at the lower **Bank Buying Rate**.\n- When an **Importer** brings KES to purchase foreign currency (USD) to pay an overseas supplier, the bank **SELLS** foreign currency at the higher **Bank Selling Rate**."
                    }
                }
            ],
            [
                {
                    "type": "suggested_diagram",
                    "title": "Exchange Rate Dynamics & Math Framework",
                    "content": {
                        "svg_content": SVG_EXCHANGE_RATE_AND_CURRENCY,
                        "caption": "Formulas for Bank Buying vs. Selling conversions, bank profit spread, and currency fluctuation impacts."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Bank Rates Matrix & Conversion Rules",
                    "content": {
                        "text": "| Transaction Type | Customer Goal | Applicable Bank Rate | Mathematical Conversion Formula |\n| :--- | :--- | :--- | :--- |\n| **Export Earnings** | Customer has Foreign Currency ($FC$); wants local Shillings ($KES$) | **Bank Buying Rate** (Lower) | $KES = FC \\times \\text{Bank Buying Rate}$ |\n| **Import Payment** | Customer has Shillings ($KES$); needs Foreign Currency ($FC$) | **Bank Selling Rate** (Higher) | $FC = \\frac{KES}{\\text{Bank Selling Rate}}$ |\n| **Forex Bureau Spread** | Financial intermediary trading profit | **Selling Rate minus Buying Rate** | $\\text{Spread per Unit} = \\text{Rate}_{\\text{sell}} - \\text{Rate}_{\\text{buy}}$ |\n| **KES Depreciation** | $1\\text{ USD} = 120 \\rightarrow 140\\text{ KES}$ | Increases export KES earnings | Makes foreign imports and debt servicing expensive |\n| **KES Appreciation** | $1\\text{ USD} = 140 \\rightarrow 120\\text{ KES}$ | Decreases export KES earnings | Lowers price of imported oil, electricity, and goods |"
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "6-Step Worked Example: Comprehensive Forex Conversion Calculations",
                    "content": {
                        "text": "**Step 1: Given Information**\n$1\\text{ USD} = \\text{Buying: KES } 128.00 \\mid \\text{Selling: KES } 132.00$\n$1\\text{ GBP} = \\text{Buying: KES } 165.00 \\mid \\text{Selling: KES } 170.00$\n\n**Problem A:** A Kenyan tea exporter receives $\\text{USD } 25,000$. How much KES will they receive?\n**Problem B:** A Kenyan car importer needs $\\text{GBP } 8,000$ to pay for a vehicle from the UK. How much KES must they pay?\n**Problem C:** What is the bank's total profit spread on these two transactions?\n\n**Step 2: Conversion Formulas**\n$$\\text{KES Received (Exporter)} = \\text{USD Amount} \\times \\text{USD Buying Rate}$$\n$$\\text{KES Paid (Importer)} = \\text{GBP Amount} \\times \\text{GBP Selling Rate}$$\n$$\\text{Spread (USD)} = 132.00 - 128.00 = \\text{KES } 4.00\\text{ per USD}$$\n\n**Step 3: Substitution**\n$$\\text{Problem A: } KES = 25,000 \\times 128.00$$\n$$\\text{Problem B: } KES = 8,000 \\times 170.00$$\n\n**Step 4: Calculations**\n$$\\text{Problem A: } 25,000 \\times 128 = \\text{KES } 3,200,000$$\n$$\\text{Problem B: } 8,000 \\times 170 = \\text{KES } 1,360,000$$\n$$\\text{Problem C: Bank Profit on USD} = 25,000 \\times 4.00 = \\text{KES } 100,000$$\n\n**Step 5: Final Answers**\n- **Exporter receives: KES 3,200,000**\n- **Importer pays: KES 1,360,000**\n- **Bank USD Spread Profit: KES 100,000**\n\n**Step 6: Economic Interpretation & Common Pitfall**\n*Interpretation:* Banks generate risk-free intermediary profit through the bid-ask spread while converting currencies for international commerce.\n*Common Pitfall:* NEVER use the selling rate for an exporter! Exporters sell foreign cash to the bank, so the bank buys at the lower Buying Rate."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Kenyan Case Study: Managing Currency Fluctuations in Kenya's Aviation Sector",
                    "content": {
                        "text": "Kenya Airways (KQ) collects passenger ticket revenue in multiple local African currencies but pays for jet fuel, aircraft leases, and international spare parts strictly in US Dollars (USD). When regional currencies fluctuate against the dollar, KQ utilizes foreign exchange hedging and forward contracts with Nairobi banks to lock in fixed exchange rates months in advance."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Foreign Exchange Math & Currency Conversions",
                    "content": {
                        "youtube_id": "ngCos392W4w",
                        "title": "How Exchange Rates and Bank Spreads Work",
                        "description": "Step-by-step tutorial on calculating currency exchange, bank buying/selling rates, and currency appreciation."
                    }
                }
            ],
            [
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Exporter Conversion",
                    "content": {
                        "question": "A Kenyan avocado exporter receives USD 10,000. If the bank rates are Buying: KES 129.50 and Selling: KES 133.50, how much KES will the exporter receive from the bank?",
                        "options": [
                            "A) KES 1,335,000",
                            "B) KES 1,295,000",
                            "C) KES 40,000",
                            "D) KES 1,000,000"
                        ],
                        "correct": "B",
                        "explanation": "The exporter sells foreign currency to the bank, so the bank applies the lower Buying Rate: 10,000 × 129.50 = KES 1,295,000."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Scenario Knowledge Check: Currency Depreciation Impact",
                    "content": {
                        "question": "If the Kenya Shilling depreciates from 1 USD = KES 120 to 1 USD = KES 150, what is the economic impact on Kenyan exporters and importers?",
                        "options": [
                            "A) Both exporters and importers lose money",
                            "B) Exporters gain higher KES revenue per dollar, while importers pay more KES for foreign goods",
                            "C) Importers gain cheaper fuel while exporters receive zero shillings",
                            "D) All international trade contracts are automatically cancelled"
                        ],
                        "correct": "B",
                        "explanation": "A weaker domestic currency makes exports more lucrative in local shillings but makes imported foreign goods more expensive."
                    }
                }
            ],
            [
                {
                    "type": "concept_explanation",
                    "title": "Lesson 8 Synthesis & Key Takeaways",
                    "content": {
                        "text": "1. **Buying Rate Rule:** Exporters selling foreign currency to the bank always receive the Bank Buying (Bid) Rate.\n2. **Selling Rate Rule:** Importers purchasing foreign currency from the bank always pay the higher Bank Selling (Ask) Rate.\n3. **Bank Spread:** The difference between selling and buying rates represents bank trading profit.\n4. **Macro Fluctuation:** Currency depreciation boosts export competitiveness but causes imported inflation; currency appreciation lowers import costs."
                    }
                }
            ]
        ]
    }
]
