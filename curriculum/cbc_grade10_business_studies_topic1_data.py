"""
VLearn CBC Grade 10 Business Studies — Topic 1: Money
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic1_svgs import (
    SVG_CURRENCY_FEATURES,
    SVG_FUNCTIONS_OF_MONEY,
    SVG_DEMAND_CAPITAL_FORMATION,
    SVG_CBK_MONETARY_POLICY,
    SVG_ETHICS_COMPARISON,
    SVG_BUDGET_MATRIX
)

TOPIC_1_LESSONS = [
    # =========================================================================
    # LESSON 1: Kenyan Currency and Its Security Features
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Kenyan Currency and Its Security Features",
        "unit_description": "Official denominations, issuing authority, themes, and Feel-Look-Tilt security features of Kenyan banknotes and coins.",
        "lesson_title": "Kenyan Currency and Its Security Features",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Cash Circulation in a Kenyan Commercial Market",
                    "content": {
                        "title": "Everyday Cash Circulation in Kenyan Markets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "A bustling commercial market in Nairobi showing active cash transactions and the vital circulation of the Kenyan Shilling in everyday commerce.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Identify all circulating denominations of Kenyan banknotes and coins\n- State the issuing authority (CBK) and themes of Kenyan currency\n- Describe the key security features of Kenyan currency notes (Feel, Look, Tilt)\n- Distinguish between genuine and counterfeit currency in real-world transactions"
                    }
                }
            ],
            # Card 2: Core Concept & Legal Authority
            [
                {
                    "type": "definition_card",
                    "title": "Currency and Legal Tender",
                    "content": {
                        "term": "Currency",
                        "definition": "The official system of money in common circulation in a country, issued exclusively by the Central Bank of Kenya (CBK) as legal tender."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Kenyan Shilling (KES) and Issuing Authority",
                    "content": {
                        "text": "The **Central Bank of Kenya (CBK)** is the sole constitutional authority mandated to design, mint, print, and issue national currency.\n\nEvery Kenyan banknote carries the national landmark **Kenyatta International Convention Centre (KICC)** on the front, alongside distinct national economic and wildlife themes on the reverse."
                    }
                }
            ],
            # Card 3: Banknote Denominations & Themes Table
            [
                {
                    "type": "comparison_table",
                    "title": "Kenyan Banknote Denominations, Themes & Colors",
                    "content": {
                        "headers": ["Denomination", "Front Landmark", "Back Economic Theme", "Back Wildlife", "Dominant Color"],
                        "rows": [
                            ["KES 50", "KICC", "Green Energy (Wind, Solar, Geothermal)", "Buffalo (Nyati)", "Red / Pink"],
                            ["KES 100", "KICC", "Agriculture (Maize, Tea, Crops)", "Leopard (Chui)", "Violet / Purple"],
                            ["KES 200", "KICC", "Social Services (Education, Health, Athletics)", "Rhino (Kifaru)", "Blue"],
                            ["KES 500", "KICC", "Tourism (Maasai Mara National Reserve)", "Lion (Simba)", "Green"],
                            ["KES 1000", "KICC", "Governance (National Parliament)", "Elephant (Ndovu)", "Brown"]
                        ]
                    }
                }
            ],
            # Card 4: Vector Diagram — Security Features & Tactile Marks
            [
                {
                    "type": "suggested_diagram",
                    "title": "Banknote Security Architecture & Tactile Marks",
                    "content": {
                        "title": "Official CBK Feel-Look-Tilt Security Map",
                        "caption": "Detailed diagram illustrating the lion watermark, see-through dove, color-shifting thread, and the 1 to 5 tactile edge bars for visually impaired individuals.",
                        "svg_content": SVG_CURRENCY_FEATURES
                    }
                }
            ],
            # Card 5: Feel, Look, Tilt Verification Procedure
            [
                {
                    "type": "step_process",
                    "title": "The 3 Golden Rules: Feel, Look, Tilt",
                    "content": {
                        "intro": "Use the Central Bank of Kenya's official verification technique to verify genuine banknotes:",
                        "steps": [
                            {"title": "1. FEEL (Gusa)", "description": "Run fingers over the note. Feel the crisp cotton hybrid paper and raised tactile bars on the edges (50=1 bar, 100=2, 200=3, 500=4, 1000=5)."},
                            {"title": "2. LOOK (Tazama)", "description": "Hold the note against bright light. Confirm the three-dimensional lion watermark with 'CBK' text and the perfectly aligned see-through dove register."},
                            {"title": "3. TILT (Pindua)", "description": "Tilt the note under light. Observe the shiny vertical security thread shifting color from red to green and the golden iridescent band on the back."}
                        ]
                    }
                }
            ],
            # Card 6: Worked Example — Cash Verification Scenario
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Verifying Suspicious Cash at a Grocery Kiosk",
                    "content": {
                        "intro": "Wanjiku runs a fresh vegetable retail stall. A customer hands her a KES 500 note for goods. The note feels unusually smooth and flimsy like regular photocopy paper.",
                        "steps": [
                            "**Step 1 — Perform the 'Feel' Test:** Wanjiku runs her fingers over the surface and edges. The note lacks raised print and has no tactile edge bars.",
                            "**Step 2 — Perform the 'Look' Test:** She holds the note against the sunlight. The see-through dove shapes do not align, and there is no embedded lion watermark.",
                            "**Step 3 — Perform the 'Tilt' Test:** The vertical stripe is flat gray ink that fails to change from red to green when tilted.",
                            "**Step 4 — Evaluation & Action:** The note is confirmed counterfeit. Wanjiku politely refuses the note, explaining that it lacks standard security features, and asks for another payment method without entering a confrontation."
                        ]
                    }
                }
            ],
            # Card 7: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Protecting Micro-Retailers and Small Enterprises",
                        "text": "In Kenya, micro-entrepreneurs (such as mama mbogas, boda-boda operators, and kiosk traders) process rapid cash transactions in busy environments. Knowing how to verify security features in under 5 seconds prevents daily losses and protects enterprise working capital from counterfeit fraud."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Central Bank of Kenya: Banknote Security Features",
                    "content": {
                        "title": "How to Identify Genuine Kenyan Banknotes",
                        "youtube_id": "v83s92y5Tq4",
                        "url": "https://www.youtube.com/watch?v=v83s92y5Tq4",
                        "description": "Official educational demonstration showing the Feel-Look-Tilt method in action on all five denominations of Kenyan currency."
                    }
                }
            ],
            # Card 8: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: KES 200 Banknote Theme",
                    "content": {
                        "question": "Which of the following describes the correct theme and back-feature of a genuine KES 200 banknote?",
                        "options": [
                            "Agriculture, featuring maize, tea, and a leopard",
                            "Tourism, featuring the Maasai Mara and a lion",
                            "Green Energy, featuring wind power and a buffalo",
                            "Social Services, featuring athletics, education, and a rhino"
                        ],
                        "correct": "D",
                        "explanation": "The back of the KES 200 note represents Social Services, highlighting education, medical progress, and athletics, with a Rhino as the back animal."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Tactile Marks for Visually Impaired",
                    "content": {
                        "question": "A visually impaired person wants to confirm if they are holding a KES 1000 banknote. How many diagonal raised bars should they feel on the edges of the note?",
                        "options": [
                            "2 bars",
                            "3 bars",
                            "4 bars",
                            "5 bars"
                        ],
                        "correct": "D",
                        "explanation": "The diagonal tactile bars on the banknote edges increase with denomination: KES 50 has 1 bar, KES 100 has 2, KES 200 has 3, KES 500 has 4, and KES 1000 has 5 bars."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Sole Authority**: The Central Bank of Kenya (CBK) is the exclusive issuer of the Kenyan Shilling (KES).\n2. **Denominations**: 5 banknotes (50, 100, 200, 500, 1000) and 5 coins (1, 5, 10, 20, 40).\n3. **Feel-Look-Tilt**: Feel for crisp hybrid cotton paper & tactile bars; Look for the lion watermark & see-through dove; Tilt for the red-to-green shifting thread & golden band."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Functions of Money in Financial Transactions
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Functions of Money in Financial Transactions",
        "unit_description": "Overcoming the limitations of barter trade and mastering the 4 primary economic functions of money.",
        "lesson_title": "Functions of Money in Financial Transactions",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Open Air Market Trade in Kenya",
                    "content": {
                        "title": "Commerce and Monetary Exchange",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Traders exchanging fresh produce in a traditional Kenyan market, demonstrating how monetary exchange eliminates the friction of barter trade.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define barter trade and explain its major frictional limitations\n- Define money and explain its 4 primary economic functions\n- Relate each function of money to everyday commercial transactions in Kenya"
                    }
                }
            ],
            # Card 2: Barter Trade & Double Coincidence of Wants
            [
                {
                    "type": "definition_card",
                    "title": "Barter Trade and Double Coincidence of Wants",
                    "content": {
                        "term": "Barter Trade",
                        "definition": "The direct exchange of goods or services for other goods or services without using a standardized monetary medium."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Severe Limitations of Barter Trade",
                    "content": {
                        "text": "Barter trade is highly inefficient in a modern economy due to four major obstacles:\n\n- **Double Coincidence of Wants**: Both parties must simultaneously possess what the other desires.\n- **Lack of Common Measure of Value**: No standard formula to determine how many chickens equal one cow or a bag of maize.\n- **Indivisibility of Commodities**: Large items (e.g., live cows) cannot be split to buy small items like salt.\n- **Perishability**: Agricultural commodities (tomatoes, milk) rot quickly and cannot store wealth."
                    }
                }
            ],
            # Card 3: The 4 Core Functions of Money (Vector SVG)
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Core Functions of Money",
                    "content": {
                        "title": "Functions of Money Architecture",
                        "caption": "Vector diagram illustrating how money acts as a Medium of Exchange, Unit of Account, Store of Value, and Standard of Deferred Payment.",
                        "svg_content": SVG_FUNCTIONS_OF_MONEY
                    }
                }
            ],
            # Card 4: Breakdown of the 4 Functions
            [
                {
                    "type": "step_process",
                    "title": "Detailed Breakdown of the 4 Functions",
                    "content": {
                        "intro": "Money solves all barter limitations through four distinct economic mechanisms:",
                        "steps": [
                            {"title": "1. Medium of Exchange", "description": "Acts as an accepted intermediary token for buying and selling, eliminating the need for double coincidence of wants."},
                            {"title": "2. Unit of Account (Measure of Value)", "description": "Provides a common numeric currency denominator to quote prices, record costs, and calculate profit/loss."},
                            {"title": "3. Store of Value", "description": "Preserves purchasing power over time, allowing businesses and households to save wealth safely in bank accounts without decay."},
                            {"title": "4. Standard of Deferred Payment", "description": "Serves as a reliable measure to agree on debts, bank credit, trade invoices, and future installment settlements."}
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Tracing Farmer Juma's Day
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Analyzing Juma's Daily Transactions",
                    "content": {
                        "intro": "Farmer Juma carries out four distinct business actions during market day in Kitale. Identify the function of money demonstrated in each:",
                        "steps": [
                            "**Transaction A (Selling Produce):** Juma sells 2 bags of maize to a wholesaler for KES 4,000 cash. $\\rightarrow$ **Medium of Exchange** (facilitates immediate sale).",
                            "**Transaction B (Comparing Prices):** Juma reviews a price list showing a solar lantern costs KES 1,500 while a battery costs KES 500. $\\rightarrow$ **Unit of Account** (common scale of value).",
                            "**Transaction C (Saving for Next Term):** Juma buys the lantern for KES 1,500 and deposits the remaining KES 2,500 into his SACCO savings account. $\\rightarrow$ **Store of Value** (holding wealth for future use).",
                            "**Transaction D (Buying Inputs on Credit):** Juma takes 2 bags of fertilizer from the cooperative, signing to pay KES 3,000 in 60 days. $\\rightarrow$ **Standard of Deferred Payment** (credit contract)."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Digital Finance and E-Commerce Platforms",
                        "text": "Platforms like M-Pesa, Jumia, and mobile banking exist solely because money acts as a standardized unit of account and friction-free medium of exchange. Digital wallets allow instant settlement across millions of Kenyan users without physical commodity friction."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The History of Money: From Barter to Cash",
                    "content": {
                        "title": "Evolution and Functions of Money",
                        "youtube_id": "Y44w7A8P6Xk",
                        "url": "https://www.youtube.com/watch?v=Y44w7A8P6Xk",
                        "description": "Visual breakdown of why barter trade collapsed and how money transformed global and local trade efficiency."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Supermarket Price Display Function",
                    "content": {
                        "question": "Which function of money is demonstrated when a supermarket prints price tags on all shelf items in Kenyan Shillings?",
                        "options": [
                            "Medium of exchange",
                            "Unit of account (measure of value)",
                            "Store of value",
                            "Standard of deferred payment"
                        ],
                        "correct": "B",
                        "explanation": "The unit of account function provides a common numerical standard to quote prices and compare the economic value of diverse goods."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Double Coincidence of Wants",
                    "content": {
                        "question": "Barter trade is highly inefficient primarily because it requires a 'double coincidence of wants.' What does this mean?",
                        "options": [
                            "Both parties must possess identical amounts of cash",
                            "Two traders must meet at the exact same location and time",
                            "Each trader must possess the exact commodity that the other trader desires",
                            "The government must set the exchange rate before trading"
                        ],
                        "correct": "C",
                        "explanation": "Double coincidence of wants means Trader A has what Trader B wants, and Trader B has what Trader A wants simultaneously, which is rare and difficult to coordinate."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Barter Inefficiencies**: Double coincidence of wants, perishability, lack of standard valuation, and indivisibility.\n2. **4 Functions**: Medium of exchange (buying/selling), Unit of account (pricing/budgeting), Store of value (saving wealth), Standard of deferred payment (credit/loans).\n3. **Modern Foundation**: These 4 functions enable modern banking, credit, and digital e-commerce."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Demand for Money and Economic Development
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Demand for Money and Economic Development",
        "unit_description": "Liquidity preference, the 3 motives for holding cash, and how household savings drive national capital formation.",
        "lesson_title": "Demand for Money and Economic Development",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Banking and Financial Hub in Nairobi",
                    "content": {
                        "title": "Financial Intermediation and Capital Flow",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Nairobi%27s_Central_Business_District_Landmark_Skyscrapers..jpg",
                        "caption": "Nairobi Central Business District skyscrapers, representing the commercial capital and financial hub that mobilizes domestic savings into business credit.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define liquidity preference (demand for money)\n- Explain the 3 primary motives for holding cash (Transactions, Precautionary, Speculative)\n- Trace the flow from private savings to national capital formation and economic development"
                    }
                }
            ],
            # Card 2: Core Concept & 3 Motives
            [
                {
                    "type": "definition_card",
                    "title": "Demand for Money (Liquidity Preference)",
                    "content": {
                        "term": "Demand for Money",
                        "definition": "The desire of individuals, households, and businesses to hold wealth in physical cash or liquid bank deposits rather than tied up in illiquid physical assets."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Motives for Holding Cash",
                    "content": {
                        "text": "Economists categorize the desire to hold liquid cash into three core motives:\n\n- **1. Transaction Motive**: Holding cash to pay for planned, regular daily expenses (food, transport, supplier bills) because income arrives periodically while expenses occur daily.\n- **2. Precautionary Motive**: Holding a financial cushion for unexpected emergencies (illness, equipment breakdown, sudden travel).\n- **3. Speculative Motive**: Holding cash reserves to exploit sudden, profitable market opportunities (discounted wholesale stock, shares, land bargains)."
                    }
                }
            ],
            # Card 3: Vector SVG — Capital Formation Cycle
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Capital Formation & Economic Growth Cycle",
                    "content": {
                        "title": "How Savings Drive National Development",
                        "caption": "Flowchart showing how household cash savings pooled in banks and SACCOs create business credit, enabling capital investment and national infrastructure.",
                        "svg_content": SVG_DEMAND_CAPITAL_FORMATION
                    }
                }
            ],
            # Card 4: Step-by-Step Capital Formation Mechanism
            [
                {
                    "type": "step_process",
                    "title": "The 4 Stages of Capital Formation",
                    "content": {
                        "intro": "When individuals demand money for savings rather than immediate consumption, it powers the national economy:",
                        "steps": [
                            {"title": "1. Savings Mobilization", "description": "Households deposit surplus funds into commercial banks, SACCOs, and local investment chamas."},
                            {"title": "2. Financial Intermediation", "description": "Banks pool these dispersed deposits into substantial capital loan funds."},
                            {"title": "3. Productive Investment", "description": "Entrepreneurs borrow these funds to purchase heavy machinery, build factories, and adopt modern technology."},
                            {"title": "4. National Economic Expansion", "description": "Industrial production increases, creating new jobs, higher tax revenue, and higher national living standards."}
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Kamau's Electronics Repair Shop
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Analyzing Cash Motives in a Small Enterprise",
                    "content": {
                        "intro": "Kamau operates an electronics workshop in Eldoret. Classify the financial motive behind each portion of his KES 16,000 liquid cash reserves:",
                        "steps": [
                            "**Portion 1 (KES 8,000 in Cash Till):** Kept to pay monthly shop rent, buy soldering wire, and pay his assistant. $\\rightarrow$ **Transaction Motive** (planned operational expenses).",
                            "**Portion 2 (KES 3,000 in M-Pesa Wallet):** Reserved exclusively in case the power grid fails, to hire an emergency backup generator. $\\rightarrow$ **Precautionary Motive** (unplanned contingency).",
                            "**Portion 3 (KES 5,000 in Bank Account):** Kept ready to buy display screens in bulk if a distributor runs a sudden clearance sale. $\\rightarrow$ **Speculative Motive** (exploiting bargain opportunity)."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Kenyan Chamas and Community SACCOs",
                        "text": "In Kenya, over 10 million citizens belong to savings groups (*chamas*) and SACCOs. By pooling monthly liquid savings, chamas provide affordable business credit to members to purchase land, boda-bodas, or farm inputs, serving as a powerful domestic engine for capital formation."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How the Financial System Works: Savings & Investment",
                    "content": {
                        "title": "Capital Formation and Economic Growth",
                        "youtube_id": "2vU3FjYnF0Y",
                        "url": "https://www.youtube.com/watch?v=2vU3FjYnF0Y",
                        "description": "Explaining how private savings are transformed by financial institutions into commercial credit, driving infrastructure and enterprise growth."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Emergency Reserve Motive",
                    "content": {
                        "question": "A business owner keeps an emergency reserve of KES 5,000 cash to pay for a technician in case their main cold-room refrigerator breaks down. Under which motive is this money held?",
                        "options": [
                            "Speculative motive",
                            "Precautionary motive",
                            "Transaction motive",
                            "Investment motive"
                        ],
                        "correct": "B",
                        "explanation": "The precautionary motive involves holding liquid cash as a safety net against unexpected contingencies and operational emergencies."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Bank Savings and Capital Formation",
                    "content": {
                        "question": "How do individual household savings deposited in commercial banks contribute directly to national capital formation?",
                        "options": [
                            "By decreasing government tax collections",
                            "By providing a pool of loanable funds that banks lend to entrepreneurs for productive business investments",
                            "By forcing the country to rely on barter trade",
                            "By printing additional physical banknotes"
                        ],
                        "correct": "B",
                        "explanation": "Bank deposits pool household savings and channel them into commercial loans for machinery, technology, and factories, driving capital formation."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Demand for Money**: The preference to hold liquid cash rather than illiquid assets.\n2. **3 Motives**: Transaction (routine spending), Precautionary (unforeseen emergencies), Speculative (bargain asset opportunities).\n3. **Capital Formation**: Savings $\\rightarrow$ Financial Intermediation $\\rightarrow$ Productive Investment $\\rightarrow$ National Economic Growth."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Supply of Money in an Economy
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Supply of Money in an Economy",
        "unit_description": "Determinants of money supply, CBK monetary policy tools, and commercial bank credit creation.",
        "lesson_title": "Supply of Money in an Economy",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Central Bank of Kenya Headquarters in Nairobi",
                    "content": {
                        "title": "The Apex Monetary Authority of Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/CBK_Nairobi_1973.jpg",
                        "caption": "The Central Bank of Kenya (CBK) building on Haile Selassie Avenue in Nairobi, representing the monetary regulator controlling national currency supply and price stability.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define money supply in an economy\n- Explain the 3 primary monetary policy tools used by the Central Bank of Kenya (OMO, Reserve Requirement, CBR)\n- Describe how commercial banks create credit and expand money supply\n- Predict the directional impact of monetary policy changes on interest rates, borrowing, and inflation"
                    }
                }
            ],
            # Card 2: Core Concept & Money Supply Definition
            [
                {
                    "type": "definition_card",
                    "title": "Money Supply and Credit Creation",
                    "content": {
                        "term": "Money Supply",
                        "definition": "The total volume of monetary assets (currency in public circulation plus commercial bank deposits) available in an economy at a specific point in time."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Central Bank as the Monetary 'Tap'",
                    "content": {
                        "text": "Money supply cannot be expanded without limit. If money supply grows faster than real goods and services production, money loses purchasing power and **inflation** surges.\n\nThe **Central Bank of Kenya (CBK)** acts as the regulator, adjusting policy tools to maintain price stability and support sustainable economic growth."
                    }
                }
            ],
            # Card 3: Vector SVG — CBK Monetary Policy Tools
            [
                {
                    "type": "suggested_diagram",
                    "title": "Central Bank of Kenya Monetary Policy Tools",
                    "content": {
                        "title": "CBK Monetary Policy Architecture",
                        "caption": "Vector diagram detailing Open Market Operations (OMO), Reserve Requirements, and Central Bank Rate (CBR) policy transmission mechanisms.",
                        "svg_content": SVG_CBK_MONETARY_POLICY
                    }
                }
            ],
            # Card 4: Directional Policy Impact Table
            [
                {
                    "type": "comparison_table",
                    "title": "Central Bank Policy Actions & Directional Economic Effects",
                    "content": {
                        "headers": ["CBK Policy Action", "Impact on Commercial Banks", "Impact on Lending Rates", "Money Supply Effect"],
                        "rows": [
                            ["Raises Central Bank Rate (CBR)", "Borrowing from CBK becomes costly", "Commercial interest rates rise", "Decreases (↓) / Tightens"],
                            ["Lowers Central Bank Rate (CBR)", "Borrowing from CBK becomes cheaper", "Commercial interest rates fall", "Increases (↑) / Expands"],
                            ["Raises Reserve Ratio (CRR)", "More customer cash locked at CBK", "Loanable funds contract", "Decreases (↓) / Tightens"],
                            ["Lowers Reserve Ratio (CRR)", "Frees up excess cash reserves", "Loanable funds expand", "Increases (↑) / Expands"],
                            ["Sells Treasury Bonds (OMO)", "Withdraws cash from banking system", "Liquidity decreases", "Decreases (↓) / Tightens"],
                            ["Buys Treasury Bonds (OMO)", "Injects fresh cash into banks", "Liquidity increases", "Increases (↑) / Expands"]
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Analyzing Interest Rate Hikes
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Analyzing a Central Bank Rate Adjustment",
                    "content": {
                        "intro": "The Central Bank of Kenya announces that it has raised the Central Bank Rate (CBR) from 9.0% to 11.5% to curb rising consumer inflation. Trace the economic transmission mechanism:",
                        "steps": [
                            "**Step 1 — Identify the Policy Tool:** Central Bank Rate (CBR) benchmark interest rate.",
                            "**Step 2 — Determine Direction:** Tightening / contractionary policy (rate hike of +2.5%).",
                            "**Step 3 — Commercial Bank Reaction:** Commercial banks face higher borrowing costs from the CBK and raise loan interest rates to customers from 13% to 16%.",
                            "**Step 4 — Business and Consumer Response:** Entrepreneurs postpone taking loans for workshop expansions; consumer installment purchases slow down.",
                            "**Step 5 — Final Economic Outcome:** Credit creation contracts, circulating money supply growth slows, consumer demand cools, and inflation stabilizes."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "How Monetary Policy Impacts Small Business Expansion",
                        "text": "If an entrepreneur plans to borrow KES 500,000 to purchase a delivery van, a rise in the CBR increases monthly loan repayments significantly. Business managers closely track CBK Monetary Policy Committee (MPC) announcements to time major capital financing decisions."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Monetary Policy and Central Banks Explained",
                    "content": {
                        "title": "How Central Banks Control Money Supply",
                        "youtube_id": "1dq7mM8TXY8",
                        "url": "https://www.youtube.com/watch?v=1dq7mM8TXY8",
                        "description": "Educational breakdown of how interest rates, reserve ratios, and open market operations regulate the flow of money and maintain price stability."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Open Market Operations Impact",
                    "content": {
                        "question": "When the Central Bank of Kenya SELLS government treasury bills in the open market, what is the immediate effect on the money supply?",
                        "options": [
                            "The money supply increases",
                            "The money supply decreases",
                            "There is no change in the money supply",
                            "Commercial banks receive more cash to lend out"
                        ],
                        "correct": "B",
                        "explanation": "When the Central Bank sells securities, commercial banks and investors pay cash to the CBK, withdrawing currency from circulation and decreasing the money supply."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Reserve Requirement Mechanics",
                    "content": {
                        "question": "Why does raising the mandatory Cash Reserve Ratio (CRR) decrease the money supply in an economy?",
                        "options": [
                            "It forces the public to hold cash under their mattresses",
                            "It requires the Central Bank to print more coins",
                            "It reduces the fraction of customer deposits that commercial banks are legally allowed to lend out as credit",
                            "It increases international export prices"
                        ],
                        "correct": "C",
                        "explanation": "A higher reserve ratio forces commercial banks to hold more cash locked in CBK vaults, reducing loanable funds and credit creation."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Money Supply**: Total volume of currency in public hands and commercial bank deposits.\n2. **CBK Tools**: Open Market Operations (OMO), Cash Reserve Ratio (CRR), and Central Bank Rate (CBR).\n3. **Economic Balance**: Regulating money supply keeps consumer inflation low and stabilizes currency purchasing power."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Ethical and Unethical Use of Money
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Ethical and Unethical Use of Money",
        "unit_description": "Financial integrity, transparency, and analyzing the legal and societal damage of financial crimes.",
        "lesson_title": "Ethical and Unethical Use of Money",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Transparent Accounting and Financial Auditing",
                    "content": {
                        "title": "Financial Integrity and Auditing",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
                        "caption": "Accurate bookkeeping, transparent financial accounting, and auditing ledgers that uphold institutional trust and integrity in commercial transactions.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define financial ethics and financial integrity\n- Contrast ethical financial practices with unethical financial misconduct\n- Analyze real-world ethical dilemmas in business cash management\n- Explain the personal, legal, and economic consequences of financial crimes"
                    }
                }
            ],
            # Card 2: Core Concept & Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Financial Ethics and Integrity",
                    "content": {
                        "term": "Financial Ethics",
                        "definition": "The moral principles of honesty, transparency, fairness, and accountability that govern financial transactions and business conduct."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Why Financial Ethics is the Backbone of Commerce",
                    "content": {
                        "text": "The entire economic system is built on **trust**. If businesses, banks, and customers cannot trust financial statements, contracts, or cash validity, trade collapses.\n\nUpholding integrity protects personal professional reputations, preserves company solvency, and ensures government tax revenues fund essential public services."
                    }
                }
            ],
            # Card 3: Vector SVG — Ethics Comparison
            [
                {
                    "type": "suggested_diagram",
                    "title": "Ethical vs. Unethical Financial Practices",
                    "content": {
                        "title": "Financial Conduct Comparison Architecture",
                        "caption": "Vector diagram contrasting transparency, tax compliance, and fair lending against fraud, tax evasion, usury, and money laundering.",
                        "svg_content": SVG_ETHICS_COMPARISON
                    }
                }
            ],
            # Card 4: Comparison Table of Financial Practices
            [
                {
                    "type": "comparison_table",
                    "title": "Ethical vs. Unethical Financial Behaviors",
                    "content": {
                        "headers": ["Dimension", "Ethical Practice", "Unethical Practice", "Consequences of Misconduct"],
                        "rows": [
                            ["Accounting & Records", "Transparent, accurate cash books and invoices", "Financial Misrepresentation (falsifying books)", "Audit exposure, fraud prosecution, loss of license"],
                            ["Tax Obligations", "Tax Compliance (declaring true income to KRA)", "Tax Evasion (smuggling, underreporting revenue)", "Heavy financial penalties, asset seizure, imprisonment"],
                            ["Credit & Lending", "Fair lending with transparent, legal interest", "Usury (exploitative, predatory interest rates)", "Borrower bankruptcy, predatory confiscation of assets"],
                            ["Source of Funds", "Legitimate business and employment revenue", "Money Laundering (cleaning criminal proceeds)", "Asset freezing, anti-money laundering (AML) prosecution"],
                            ["Cash Handling", "Vigilant verification and reporting of fake notes", "Counterfeiting (creating or passing fake currency)", "Severe criminal conviction, erosion of national currency"]
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Branching Decision Scenario
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: The Transport Company Accounting Dilemma",
                    "content": {
                        "intro": "You are the head accountant at a regional bus company. The manager instructs you to delete KES 10,000 from daily cash sales so the business can underreport revenue and pay lower corporate income taxes.",
                        "steps": [
                            "**Option A (Complying with the Request):** You delete the record to please the boss. $\\rightarrow$ **Analysis:** This constitutes criminal tax evasion and financial misrepresentation. An external audit will trace the missing tickets, resulting in fines, criminal prosecution, and permanent loss of your professional license.",
                            "**Option B (Ethical Refusal & Advisory):** You politely refuse, explaining that professional accounting standards require complete records. You offer to review legitimate, legal tax allowances and operational expense deductions the company can claim. $\\rightarrow$ **Analysis:** This maintains financial integrity, protects your career, and shields the enterprise from devastating legal liabilities."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Societal Impact of Financial Integrity",
                        "text": "When corporate tax evasion and public fund embezzlement occur, national budgets for public hospitals, schools, and roads are depleted. Conversely, ethical business operations foster investor confidence, creating sustainable employment and national prosperity."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Financial Crimes, Ethics, and Money Laundering",
                    "content": {
                        "title": "The Impact of White-Collar Financial Crimes",
                        "youtube_id": "YwYn2kP9b-8",
                        "url": "https://www.youtube.com/watch?v=YwYn2kP9b-8",
                        "description": "Case study analyzing how fraud, bribery, and money laundering damage commercial enterprise stability and public welfare."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Financial Misrepresentation",
                    "content": {
                        "question": "What is the term used to describe the illegal practice of deliberately altering accounting records to hide the true financial position of a business?",
                        "options": [
                            "Money laundering",
                            "Tax compliance",
                            "Financial misrepresentation",
                            "Usury"
                        ],
                        "correct": "C",
                        "explanation": "Financial misrepresentation is the deceptive practice of manipulating financial statements or cash books to conceal losses, underreport taxes, or facilitate theft."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Usury and Predatory Lending",
                    "content": {
                        "question": "An unregistered lender offers emergency loans to desperate traders, demanding an exorbitant hidden interest rate of 100% per month and confiscating title deeds. This exploitative practice is termed:",
                        "options": [
                            "Direct foreign investment",
                            "Tax compliance",
                            "Embezzlement",
                            "Usury (exploitative predatory lending)"
                        ],
                        "correct": "D",
                        "explanation": "Usury is charging excessively high, predatory interest rates that exploit vulnerable borrowers unfairly."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Financial Integrity**: Demands honesty, transparency, tax compliance, and accurate bookkeeping.\n2. **Unethical Practices**: Fraud, embezzlement, tax evasion, usury, counterfeiting, and money laundering carry severe criminal penalties.\n3. **Trust Foundation**: Ethical monetary practices sustain commercial enterprise stability and public social welfare."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: The Role of Money in Day-to-Day Life
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "The Role of Money in Day-to-Day Life",
        "unit_description": "Distinguishing basic needs from wants, calculating opportunity costs, and preparing a balanced personal budget.",
        "lesson_title": "The Role of Money in Day-to-Day Life",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Student Budgeting and School Stationery Purchase",
                    "content": {
                        "title": "Daily Consumer Choices and Budgeting",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Kenyan_Samburu_children_in_a_classroom.jpg",
                        "caption": "Kenyan students in a classroom setting, representing daily consumer decisions, educational investments, and personal budgeting under income constraints.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Distinguish between basic physical needs and non-essential wants\n- Define and calculate opportunity cost in everyday consumer choices\n- Construct a balanced personal budget under a fixed income constraint\n- Develop lifelong habits of financial discipline and savings"
                    }
                }
            ],
            # Card 2: Needs vs. Wants and Opportunity Cost
            [
                {
                    "type": "definition_card",
                    "title": "Basic Needs, Wants, and Opportunity Cost",
                    "content": {
                        "term": "Opportunity Cost",
                        "definition": "The value of the next best alternative that is sacrificed or foregone when making a choice under a resource constraint."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Scarcity and Daily Financial Prioritization",
                    "content": {
                        "text": "Money is always scarce relative to human desires. Because resources are limited, you cannot purchase everything at once.\n\n- **Basic Needs**: Essential survival items (food, clean water, shelter, clothing, basic medicine, school books).\n- **Wants**: Desires that enhance comfort or luxury (designer accessories, entertainment, luxury snacks).\n\nEvery time you allocate limited money toward a want, you incur an **opportunity cost** in foregone needs or savings."
                    }
                }
            ],
            # Card 3: Vector SVG — Budget Matrix & Decision Model
            [
                {
                    "type": "suggested_diagram",
                    "title": "Personal Budgeting & Opportunity Cost Matrix",
                    "content": {
                        "title": "Akinyi's Weekly Spending Decision Model",
                        "caption": "Vector diagram illustrating how Akinyi balances KES 500 across transport, lunch, notebook, and savings while rejecting non-essential wants.",
                        "svg_content": SVG_BUDGET_MATRIX
                    }
                }
            ],
            # Card 4: Step-by-Step Budget Preparation Protocol
            [
                {
                    "type": "step_process",
                    "title": "6 Steps to Construct a Balanced Personal Budget",
                    "content": {
                        "intro": "Follow this structured protocol to manage pocket money, allowances, or business revenue:",
                        "steps": [
                            {"title": "1. Identify Total Inflow", "description": "Calculate exact total available income for the period (e.g., KES 500 allowance)."},
                            {"title": "2. Itemize Expected Expenses", "description": "List all items you plan to spend money on with their estimated costs."},
                            {"title": "3. Categorize Needs vs. Wants", "description": "Label each item as an 'Essential Need', 'Future Savings Goal', or 'Non-essential Want'."},
                            {"title": "4. Allocate to Needs First", "description": "Fund mandatory survival and educational expenses before considering discretionary items."},
                            {"title": "5. Determine Savings Portion", "description": "Set aside a minimum of 5–10% of income for emergency buffers and future capital goals."},
                            {"title": "6. Balance Inflows and Outflows", "description": "Adjust or eliminate wants until Total Expenses $\\le$ Total Income (Zero Debt)."}
                        ]
                    }
                }
            ],
            # Card 5: Worked Example — Akinyi's Weekly Budget
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Balancing Akinyi's KES 500 Allowance",
                    "content": {
                        "intro": "Akinyi receives a weekly school allowance of KES 500. Her competing expenditure desires total KES 620, creating a KES 120 deficit. Construct her balanced decision matrix:",
                        "steps": [
                            "**Step 1 — Mandatory Need (Transport):** KES 250 allocated for daily bus fare. $\\rightarrow$ **Approved** (vital for attendance).",
                            "**Step 2 — Mandatory Need (Lunch):** KES 150 allocated for daily school lunch. $\\rightarrow$ **Approved** (essential for health).",
                            "**Step 3 — Mandatory Need (Notebook):** KES 70 allocated for class assignments. $\\rightarrow$ **Approved** (essential class material).",
                            "**Step 4 — Discretionary Want (Fancy Hair Clip):** Cost KES 100. $\\rightarrow$ **Rejected** (represents the **Opportunity Cost** sacrificed to balance budget).",
                            "**Step 5 — Future Goal (Trip Savings):** Adjusted from KES 50 down to KES 30 to match available cash.",
                            "**Step 6 — Final Verification:** $\\text{Total Spending} = 250 + 150 + 70 + 30 = \\mathbf{\\text{KES } 500}$. Budget is 100% balanced with zero deficit!"
                        ]
                    }
                }
            ],
            # Card 6: Real-World Application & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Personal Budgeting as the Foundation of Enterprise Management",
                        "text": "Every large corporation, SACCO, and commercial bank operates on the identical principles of cash-flow budgeting. Mastering personal expenditure discipline in school directly builds the managerial competence required to control multimillion-shilling enterprise budgets."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Needs vs Wants and Teen Budgeting",
                    "content": {
                        "title": "Financial Discipline and Prioritization",
                        "youtube_id": "yvA1Xv0t-9k",
                        "url": "https://www.youtube.com/watch?v=yvA1Xv0t-9k",
                        "description": "Engaging youth financial literacy guide on overcoming impulse spending, distinguishing needs from wants, and building savings habits."
                    }
                }
            ],
            # Card 7: Formative Knowledge Checks & Key Takeaways
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Opportunity Cost",
                    "content": {
                        "question": "When Akinyi chooses to spend her last KES 70 on a required school notebook instead of buying a decorative hair accessory, the hair accessory represents her:",
                        "options": [
                            "Monetary supply",
                            "Precautionary motive",
                            "Opportunity cost",
                            "Capital deposit"
                        ],
                        "correct": "C",
                        "explanation": "Opportunity cost is the value of the foregone alternative (the hair accessory) sacrificed when making a choice under a resource constraint."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Basic Needs vs Wants",
                    "content": {
                        "question": "Which of the following is a basic physiological need required for human survival?",
                        "options": [
                            "A luxury smartphone",
                            "High-speed home video streaming",
                            "Designer wristwatch",
                            "Clean drinking water and nutritious food"
                        ],
                        "correct": "D",
                        "explanation": "Clean water, nutritious food, shelter, clothing, and basic healthcare are fundamental survival needs. Other options are lifestyle wants."
                    }
                },
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary Takeaways",
                    "content": {
                        "text": "1. **Scarcity & Prioritization**: Basic survival and educational needs must always be funded before discretionary wants.\n2. **Opportunity Cost**: Every spending decision involves a trade-off; smart budgeters minimize wasteful sacrifices.\n3. **Balanced Budgeting**: Total planned spending and savings must never exceed total income ($\text{Expenses} \\le \text{Income}$)."
                    }
                }
            ]
        ]
    }
]
