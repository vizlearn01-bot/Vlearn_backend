"""
VLearn CBC Grade 10 Business Studies — Topic 14: Effects of Business Transactions
Full Structured Lesson Card Definitions (Lessons 1 to 5)
Decomposed into 8 atomic pedagogical cards per lesson with zero bracket citations,
complete responsive SVGs, verified Wikimedia visual hooks, and KaTeX math formulas.
"""

from curriculum.cbc_grade10_business_studies_topic14_svgs import (
    SVG_ACCOUNTING_EQUATION_BALANCE_SCALE,
    SVG_BALANCE_SHEET_ARCHITECTURE,
    SVG_TRANSACTION_EFFECTS_MATRIX,
    SVG_SIMULATION_PROGRESSION_TIMELINE,
    SVG_CAPITAL_ADJUSTMENT_RESERVOIR
)

TOPIC_14_LESSONS = [
    # =========================================================================
    # LESSON 1: The Accounting Equation
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "The Accounting Equation",
        "unit_description": "Foundational mathematics of double-entry accounting, core concepts of Assets, Liabilities, and Owner's Capital, mathematical rearrangements, the seesaw balance mechanism, and missing value calculations.",
        "lesson_title": "The Accounting Equation",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "City Market Commercial Setup in Nairobi",
                    "content": {
                        "title": "Retail Commerce and Capital Investment in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "An active Kenyan market stall with display counters, stock, and equipment, demonstrating how enterprise assets are financed through owner equity and borrowed capital.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define the Accounting Equation and identify its three structural pillars: Assets, Capital, and Liabilities\n- Explain the Seesaw / Balance Scale analogy governing enterprise financing\n- Express the accounting equation in its three equivalent mathematical forms ($A = C + L$, $C = A - L$, and $L = A - C$)\n- Calculate missing accounting values using step-by-step KaTeX mathematical substitution"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "The Fundamental Accounting Equation",
                    "content": {
                        "term": "Accounting Equation",
                        "definition": "The mathematical expression showing that the total economic resources (Assets) of a business entity are perpetually equal to the sum of claims against those resources by the owner (Capital) and external creditors (Liabilities): Assets = Capital + Liabilities."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Structural Pillars of Accounting",
                    "content": {
                        "text": "Every business enterprise relies on three core financial elements:\n\n- **Asset (A):** Any valuable economic resource owned or controlled by a business as a result of past transactions, expected to generate future economic benefits (e.g., cash, inventory, equipment, buildings, trade debtors).\n- **Liability (L):** A present legal obligation or financial debt owed by the business to external third parties, arising from past transactions, settled through future resource outflows (e.g., bank loans, trade creditors, unpaid utility bills).\n- **Capital / Owner's Equity (C):** The owner's personal financial investment and residual claim on the business assets after settling all external liabilities ($Capital = Assets - Liabilities$).\n- **The Dual-Claim Rule:** A business entity owns nothing in isolation without a corresponding source of funding. Total assets are always financed by internal capital or external borrowing."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Accounting Equation Balance Scale Mechanism",
                    "content": {
                        "title": "The Seesaw Balance Model of Assets and Claims",
                        "caption": "Precision vector diagram illustrating how total economic resources (Assets) on the left pan are held in perfect mathematical equilibrium against owner's equity and external liabilities on the right pan.",
                        "svg_content": SVG_ACCOUNTING_EQUATION_BALANCE_SCALE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Matrix: Assets vs. Liabilities vs. Capital",
                    "content": {
                        "headers": ["Financial Element", "Nature & Definition", "Source of Funding", "Legal Claim Priority", "Typical Kenyan SME Examples"],
                        "rows": [
                            ["Assets (A)", "Economic resources owned and utilized to generate business revenue", "Funded by owner equity or creditor borrowing", "N/A (Represents the pool of resources being claimed)", "Cash in bank, vegetable stock, delivery motorcycle, shop blenders"],
                            ["Liabilities (L)", "Present financial obligations owed to external parties", "External creditors, commercial banks, suppliers", "First Priority (Must be settled first in legal liquidation)", "Equity Bank loan, trade creditors (unpaid suppliers), accrued rent"],
                            ["Capital (C)", "Owner's personal financial stake and residual interest", "Owner's personal savings, retained earnings, equity injections", "Residual Priority (Claim settled only after all debts are paid)", "Owner's startup cash, personal motor vehicle transferred to business"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Solving for Missing Accounting Equation Values",
                    "content": {
                        "intro": "Mwangi starts 'Nyeri Fruit Juice Bar' with commercial blending machines worth $\\text{KES } 30,000$, shop display fittings of $\\text{KES } 15,000$, fresh fruit stock of $\\text{KES } 8,000$, and business cash at bank of $\\text{KES } 12,000$. To finance these assets, he took a microfinance loan of $\\text{KES } 12,000$ and owes local fruit farmers $\\text{KES } 7,000$ on 30-day credit. Calculate Mwangi's Total Assets, Total Liabilities, and Owner's Capital (Net Worth).",
                        "steps": [
                            "**Step 1: Given Information:**\n- Blenders & Machinery = $\\text{KES } 30,000$\n- Furniture & Fittings = $\\text{KES } 15,000$\n- Inventory / Fruit Stock = $\\text{KES } 8,000$\n- Cash at Bank = $\\text{KES } 12,000$\n- Microfinance Loan = $\\text{KES } 12,000$\n- Trade Creditors = $\\text{KES } 7,000$",
                            "**Step 2: Formula & Economic Rules:**\n$$\\text{Total Assets } (A) = \\text{Machinery} + \\text{Furniture} + \\text{Inventory} + \\text{Cash}$$\n$$\\text{Total Liabilities } (L) = \\text{Microfinance Loan} + \\text{Trade Creditors}$$\n$$\\text{Owner's Capital } (C) = \\text{Total Assets } (A) - \\text{Total Liabilities } (L)$$",
                            "**Step 3: Substitution:**\n$$A = 30,000 + 15,000 + 8,000 + 12,000$$\n$$L = 12,000 + 7,000$$\n$$C = A - L$$",
                            "**Step 4: Calculation:**\n$$A = \\text{KES } 65,000$$\n$$L = \\text{KES } 19,000$$\n$$C = 65,000 - 19,000 = \\text{KES } 46,000$$",
                            "**Step 5: Final Answer & Unit:**\n- Total Assets = $\\text{KES } 65,000$\n- Total Liabilities = $\\text{KES } 19,000$\n- Owner's Capital = $\\text{KES } 46,000$\n- Verification: $Assets \\,(65,000) = Capital \\,(46,000) + Liabilities \\,(19,000)$",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Mwangi's business commands $\\text{KES } 65,000$ in productive wealth, of which $70.77\\%$ is owned outright by Mwangi (equity) and $29.23\\%$ is financed by creditors. *Common Pitfall:* Forgetting that debts to suppliers (trade creditors) are liabilities rather than operating expenses when balancing initial capitalization."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Mwangi's Fruit Juice Bar, Nyeri Town",
                    "content": {
                        "title": "Capital Structure and Asset Acquisition in Nyeri County",
                        "text": "In Nyeri Town, Mwangi launched 'Nyeri Fruit Juice Bar' by pooling KES 35,000 from his personal savings and securing a KES 15,000 soft loan from his sister. With the combined KES 50,000 capital and liability funds, Mwangi purchased a heavy-duty commercial blender (KES 28,000), secured shop shelving (KES 12,000), and bought a batch of passion fruits and mangoes from local farmers (KES 10,000). By maintaining strict records, Mwangi ensured that every shilling of equipment and fruit stock on the asset side matched his equity and debt obligations."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "The Fundamental Accounting Equation Explained",
                    "content": {
                        "title": "Mastering Assets, Liabilities, and Owner's Equity",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Comprehensive visual guide to the accounting equation, dual claims, and mathematical formulations in commercial bookkeeping."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Calculating Business Liabilities",
                    "content": {
                        "question": "A hardware store in Eldoret has Total Assets valued at KES 480,000 and the owner's Capital stands at KES 310,000. What is the total monetary value of the enterprise's Liabilities?",
                        "options": [
                            "KES 790,000",
                            "KES 170,000",
                            "KES 310,000",
                            "KES 140,000"
                        ],
                        "correct": "B",
                        "explanation": "Applying the rearranged liability formulation $Liabilities = Assets - Capital$, we calculate $Liabilities = 480,000 - 310,000 = \\text{KES } 170,000$."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: The Core Principle of the Accounting Equation",
                    "content": {
                        "question": "Why must the Accounting Equation ($Assets = Capital + Liabilities$) balance after every single commercial transaction?",
                        "options": [
                            "Because government commercial law requires all profits to be deposited in bank reserves",
                            "Because every asset acquired by an enterprise is completely financed by either the owner's equity or third-party debt claims",
                            "Because liabilities must always exceed capital to maintain commercial solvency",
                            "Because cash transactions do not require bookkeeping entries"
                        ],
                        "correct": "B",
                        "explanation": "The accounting equation reflects the dual-aspect rule: every economic resource owned by a business must have an originating source of funding, represented by internal owner's capital or external creditors' liabilities."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Universal Accounting Equation:** $Assets = Capital + Liabilities$ forms the mathematical cornerstone of all modern accounting systems.\n2. **Three Formulations:** The equation can be rearranged into $Capital = Assets - Liabilities$ (Net Worth) and $Liabilities = Assets - Capital$ (Debt Claim).\n3. **Dual Claims:** Assets represent what the business owns, while Capital and Liabilities represent internal and external claims on those assets.\n4. **Perpetual Equilibrium:** Every commercial exchange alters at least two accounts, preserving the exact seesaw balance."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: The Statement of Financial Position (Balance Sheet)
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "The Statement of Financial Position (Balance Sheet)",
        "unit_description": "Financial snapshot of enterprise health, classification of Non-Current and Current Assets, Non-Current and Current Liabilities, standard vertical structure, working capital, and balance sheet preparation.",
        "lesson_title": "The Statement of Financial Position (Balance Sheet)",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Financial Audit and Statement Preparation in Kenya",
                    "content": {
                        "title": "Accounting and Financial Statement Analysis",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
                        "caption": "An accountant preparing financial statements using analytical ledger reports and calculators, illustrating the preparation of the Statement of Financial Position.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define the Statement of Financial Position (Balance Sheet) as a financial snapshot as at a specific date\n- Distinguish between Non-Current Assets and Current Assets based on lifespan and liquidity\n- Distinguish between Non-Current Liabilities and Current Liabilities based on maturity period\n- Construct a standard vertical Statement of Financial Position and compute Working Capital"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "The Statement of Financial Position",
                    "content": {
                        "term": "Statement of Financial Position",
                        "definition": "A formal accounting statement that lists and classifies an enterprise's assets, liabilities, and owner's capital as at a specific calendar date, providing a comprehensive snapshot of its financial health and net worth."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Classification of Assets and Liabilities",
                    "content": {
                        "text": "To provide meaningful information to bankers, tax authorities, and managers, financial items are categorized into standardized classes:\n\n- **Non-Current Assets (Fixed Assets):** Long-term resources acquired for operational use over more than one financial year to generate income, not intended for immediate resale (e.g., land, commercial buildings, delivery vehicles, machinery, furniture).\n- **Current Assets:** Short-term resources held as cash or expected to be converted into cash, sold, or consumed within one financial year (e.g., stock/inventory, trade debtors/receivables, bank deposits, cash in hand).\n- **Non-Current Liabilities (Long-Term Debts):** Obligations due for settlement after more than twelve months (e.g., 5-year bank development loans, commercial mortgages).\n- **Current Liabilities:** Short-term debts payable within twelve months (e.g., trade creditors/payables, bank overdrafts, accrued expenses).\n- **Working Capital:** The liquid operating cushion computed as $\\text{Working Capital} = \\text{Current Assets} - \\text{Current Liabilities}$."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Architecture of the Statement of Financial Position",
                    "content": {
                        "title": "Standard Vertical Structure & Asset-Liability Hierarchy",
                        "caption": "High-precision vector SVG diagram depicting the standard vertical layout of the Statement of Financial Position, subtotal classifications, and the final equilibrium between Total Assets and Total Capital & Liabilities.",
                        "svg_content": SVG_BALANCE_SHEET_ARCHITECTURE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Matrix: Asset & Liability Classifications",
                    "content": {
                        "headers": ["Classification", "Lifespan / Time Horizon", "Primary Function", "Liquidity / Settlement Speed", "Kenyan Enterprise Examples"],
                        "rows": [
                            ["Non-Current Assets (NCA)", "Long-term (Greater than 1 year)", "Production infrastructure and operational capacity", "Low liquidity (Cannot be quickly converted to cash without loss)", "Tea processing factory machinery, delivery trucks, posho mill motors"],
                            ["Current Assets (CA)", "Short-term (Converted within 1 year)", "Daily trading, sales replenishment, liquid buffer", "High liquidity (Cash or near-cash instruments)", "Packaged maize flour stock, customer debtors, M-Pesa business balance"],
                            ["Non-Current Liabilities (NCL)", "Long-term (Matures after 1 year)", "Financing major capital equipment and infrastructure", "Long-term repayment schedule with structured interest", "5-year commercial expansion loan from KCB Bank, equipment asset financing"],
                            ["Current Liabilities (CL)", "Short-term (Matures within 1 year)", "Financing short-term working capital and supplies", "Immediate settlement required (0 to 90 days)", "Trade credit owed to millers, 30-day bank overdraft, unpaid electricity bill"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Preparing a Statement of Financial Position",
                    "content": {
                        "intro": "The following financial balances were extracted from the ledger records of 'Olerai Dairies' in Naivasha as at 31st December 2026: Delivery Pickup Truck $\\text{KES } 250,000$; Milk Pasteurization Machine $\\text{KES } 90,000$; Inventory of Packaged Milk $\\text{KES } 45,000$; Trade Debtors (Supermarkets) $\\text{KES } 30,000$; Cash at Bank $\\text{KES } 35,000$; 3-Year Commercial Bank Loan $\\text{KES } 120,000$; Trade Creditors (Dairy Farmers) $\\text{KES } 40,000$; Accrued Electricity Bill $\\text{KES } 10,000$; and Owner's Capital $\\text{KES } 280,000$. Prepare the Statement of Financial Position and calculate Working Capital.",
                        "steps": [
                            "**Step 1: Given Information & Grouping:**\n- Non-Current Assets (NCA): Delivery Truck (KES 250,000), Pasteurizer (KES 90,000)\n- Current Assets (CA): Inventory (KES 45,000), Debtors (KES 30,000), Bank (KES 35,000)\n- Non-Current Liabilities (NCL): 3-Year Bank Loan (KES 120,000)\n- Current Liabilities (CL): Trade Creditors (KES 40,000), Accrued Electricity (KES 10,000)\n- Owner's Capital (C): KES 280,000",
                            "**Step 2: Formula & Economic Rules:**\n$$\\text{Total NCA} = 250,000 + 90,000$$\n$$\\text{Total CA} = 45,000 + 30,000 + 35,000$$\n$$\\text{Total Assets } (TA) = \\text{Total NCA} + \\text{Total CA}$$\n$$\\text{Total CL} = 40,000 + 10,000$$\n$$\\text{Total Capital \\& Liabilities} = C + \\text{Total NCL} + \\text{Total CL}$$\n$$\\text{Working Capital} = \\text{Total CA} - \\text{Total CL}$$",
                            "**Step 3: Substitution:**\n$$\\text{Total NCA} = \\text{KES } 340,000$$\n$$\\text{Total CA} = \\text{KES } 110,000$$\n$$TA = 340,000 + 110,000 = \\text{KES } 450,000$$\n$$\\text{Total NCL} = \\text{KES } 120,000$$\n$$\\text{Total CL} = \\text{KES } 50,000$$\n$$\\text{Total Claims} = 280,000 + 120,000 + 50,000 = \\text{KES } 450,000$$",
                            "**Step 4: Working Capital Calculation:**\n$$\\text{Working Capital} = 110,000 - 50,000 = \\text{KES } 60,000$$",
                            "**Step 5: Final Statement Layout & Balance:**\n- Total Non-Current Assets = $\\text{KES } 340,000$\n- Total Current Assets = $\\text{KES } 110,000$\n- **TOTAL ASSETS = $\\text{KES } 450,000$**\n- Owner's Capital = $\\text{KES } 280,000$\n- Non-Current Liabilities = $\\text{KES } 120,000$\n- Current Liabilities = $\\text{KES } 50,000$\n- **TOTAL CAPITAL & LIABILITIES = $\\text{KES } 450,000$**\n- Working Capital = $\\text{KES } 60,000$",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Olerai Dairies is in a robust financial position: its Total Assets ($\\,\\text{KES } 450,000$) match Total Claims perfectly. A positive working capital of $\\text{KES } 60,000$ guarantees the business can comfortably pay its short-term debts to dairy farmers without selling long-term equipment. *Common Pitfall:* Misclassifying short-term unpaid electricity bills as non-current liabilities."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Olerai Dairies in Naivasha",
                    "content": {
                        "title": "Balance Sheet Management for Agribusiness Solvency",
                        "text": "Olerai Dairies collects raw milk from over 80 smallholder farmers across Nakuru County. When seeking an expansion credit line from a commercial bank, the loan officer required a certified Statement of Financial Position as at the end of the trading year. By clearly demonstrating KES 340,000 in heavy pasteurizing assets and KES 60,000 in net working capital, Olerai proved it possessed sufficient liquidity to service daily operational costs while maintaining substantial asset backing to secure long-term loan facilities."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding the Statement of Financial Position",
                    "content": {
                        "title": "Structure and Interpretation of the Balance Sheet",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Step-by-step walkthrough of Balance Sheet construction, asset/liability classifications, and working capital evaluation."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Asset Classification Criteria",
                    "content": {
                        "question": "A bakery enterprise in Nakuru purchases a delivery van for KES 650,000 to transport bread to retailers and buys baking flour worth KES 80,000. How are the van and the flour correctly classified on the Balance Sheet?",
                        "options": [
                            "The van is a Current Asset and the flour is a Non-Current Asset",
                            "Both the van and the flour are classified as Current Liabilities",
                            "The van is a Non-Current Asset and the flour is a Current Asset (Inventory)",
                            "The van is Capital and the flour is a Non-Current Liability"
                        ],
                        "correct": "C",
                        "explanation": "The delivery van has an expected operational lifespan exceeding one year and is used for transport infrastructure (Non-Current Asset), whereas flour is inventory intended to be baked and sold within days (Current Asset)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Working Capital Computation",
                    "content": {
                        "question": "If a retail boutique has Current Assets of KES 180,000 and Current Liabilities of KES 75,000, what is its Net Working Capital?",
                        "options": [
                            "KES 255,000",
                            "KES 105,000",
                            "KES 75,000",
                            "KES 180,000"
                        ],
                        "correct": "B",
                        "explanation": "Working Capital is calculated as Current Assets minus Current Liabilities: $\\text{Working Capital} = 180,000 - 75,000 = \\text{KES } 105,000$."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Financial Snapshot:** The Statement of Financial Position reveals the financial standing of an enterprise at a single specific calendar date.\n2. **Standard Groupings:** Assets are split into Non-Current (fixed infrastructure) and Current (liquid stock/cash), while Liabilities are divided into Non-Current (>1 year debt) and Current (<1 year debt).\n3. **Working Capital Health:** Net Working Capital ($CA - CL$) measures short-term liquidity and buffer against cash shortages.\n4. **Absolute Equality:** Total Assets must always equal the sum of Owner's Capital, Non-Current Liabilities, and Current Liabilities."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Transaction Effects on the Accounting Equation
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Transaction Effects on the Accounting Equation",
        "unit_description": "The double-entry dual effect rule, four primary transaction patterns, simultaneous account shifts, asset substitutions, debt settlements, and perpetual equilibrium verification.",
        "lesson_title": "Transaction Effects on the Accounting Equation",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Wangige Agricultural & Retail Marketplace in Kiambu",
                    "content": {
                        "title": "Commercial Transactions in a Busy Kenyan Market",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Vendors conducting cash and credit purchases of fresh produce in Wangige Market, illustrating daily commercial transaction flows.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the Double-Entry Dual Effect principle governing every commercial transaction\n- Identify the 4 primary transaction patterns affecting Assets, Liabilities, and Capital\n- Analyze how cash purchases, credit acquisitions, and debt settlements alter specific accounts\n- Demonstrate mathematically that the accounting equation remains balanced after every transaction"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "The Double-Entry Dual Aspect Rule",
                    "content": {
                        "term": "Dual Aspect Principle",
                        "definition": "The foundational accounting rule establishing that every commercial transaction has a two-fold (dual) impact on the financial structure of a business, affecting at least two ledger accounts and ensuring the equation Assets = Capital + Liabilities never breaches equilibrium."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Primary Transaction Patterns",
                    "content": {
                        "text": "All commercial business activities fall into four fundamental transaction patterns:\n\n- **Pattern 1: Increase in Asset and Increase in Capital (Asset ↑, Capital ↑):** When the owner injects cash, personal vehicles, or equipment into the business, or when the enterprise earns trading profit.\n- **Pattern 2: Increase in Asset and Increase in Liability (Asset ↑, Liability ↑):** When the business buys inventory or equipment on credit, or takes a bank loan.\n- **Pattern 3: Asset Exchange / Substitution (Asset A ↑, Asset B ↓):** When one asset is converted into another without changing total assets (e.g., buying stock with bank cash, collecting cash from a debtor).\n- **Pattern 4: Decrease in Asset and Decrease in Liability or Capital (Asset ↓, Liability/Capital ↓):** When the business settles supplier debts, repays a loan, or when the owner withdraws cash for personal use (Drawings)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The 4 Transaction Effect Pathways Matrix",
                    "content": {
                        "title": "Visual Decision Flow of Transaction Effects on Assets, Capital, and Debts",
                        "caption": "Comprehensive dark-mode vector SVG diagram depicting the four core transaction impact pathways, showing mathematical shifts and equation balance invariance.",
                        "svg_content": SVG_TRANSACTION_EFFECTS_MATRIX
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Master Transaction Effect Classification Matrix",
                    "content": {
                        "headers": ["Transaction Description", "Asset Effect (A)", "Capital Effect (C)", "Liability Effect (L)", "Equation Balance Verification"],
                        "rows": [
                            ["1. Owner deposits KES 100K savings in bank", "+100,000 (Bank Cash)", "+100,000 (Owner Equity)", "0 (No change)", "Assets (100K) = Capital (100K) + Liab (0) ✓"],
                            ["2. Buy shop display counter on credit KES 40K", "+40,000 (Furniture)", "0 (No change)", "+40,000 (Trade Creditors)", "Assets (140K) = Capital (100K) + Liab (40K) ✓"],
                            ["3. Buy inventory for cash KES 15K", "+15K (Stock) / -15K (Cash)", "0 (No change)", "0 (No change)", "Assets (140K) = Capital (100K) + Liab (40K) ✓"],
                            ["4. Pay trade creditor KES 10K cash", "-10,000 (Bank Cash)", "0 (No change)", "-10,000 (Creditors)", "Assets (130K) = Capital (100K) + Liab (30K) ✓"],
                            ["5. Collect KES 8K cash from credit debtor", "+8K (Cash) / -8K (Debtors)", "0 (No change)", "0 (No change)", "Assets (130K) = Capital (100K) + Liab (30K) ✓"],
                            ["6. Owner withdraws KES 5K cash for home use", "-5,000 (Bank Cash)", "-5,000 (Drawings)", "0 (No change)", "Assets (125K) = Capital (95K) + Liab (30K) ✓"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Step-by-Step Transaction Impact Tracking",
                    "content": {
                        "intro": "Wanjala starts 'Kitale Green Grocers' from a zero baseline ($0 = 0 + 0$). Trace the exact financial state after each of the following 4 successive transactions: (T1) Deposits $\\text{KES } 100,000$ cash into the business bank account; (T2) Purchases display shelves worth $\\text{KES } 40,000$ on credit from 'Nakuru Woodworks'; (T3) Buys fresh vegetable stock for $\\text{KES } 15,000$ cash; (T4) Pays $\\text{KES } 10,000$ cash to 'Nakuru Woodworks' to settle part of the debt.",
                        "steps": [
                            "**Step 1: Starting Baseline State (Day 0):**\n$$\\text{Assets (0)} = \\text{Capital (0)} + \\text{Liabilities (0)}$$",
                            "**Step 2: Transaction 1 (Capital Deposit):**\n- Bank Asset increases by $\\text{KES } 100,000$; Capital increases by $\\text{KES } 100,000$.\n$$\\text{Assets (Bank: 100,000)} = \\text{Capital (100,000)} + \\text{Liabilities (0)}$$\n$$\\text{Balance: } 100,000 = 100,000$$",
                            "**Step 3: Transaction 2 (Credit Purchase):**\n- Shelves Asset increases by $\\text{KES } 40,000$; Creditors Liability increases by $\\text{KES } 40,000$.\n$$\\text{Assets (Bank 100,000 + Shelves 40,000)} = \\text{Capital (100,000)} + \\text{Creditors (40,000)}$$\n$$\\text{Balance: } 140,000 = 140,000$$",
                            "**Step 4: Transaction 3 (Asset Exchange - Stock for Cash):**\n- Stock Asset increases by $\\text{KES } 15,000$; Bank Asset decreases by $\\text{KES } 15,000$ (New Bank = $\\text{KES } 85,000$).\n$$\\text{Total Assets} = \\text{Bank (85,000)} + \\text{Shelves (40,000)} + \\text{Stock (15,000)} = \\text{KES } 140,000$$\n$$\\text{Balance: } 140,000 = 140,000$$",
                            "**Step 5: Transaction 4 (Debt Settlement):**\n- Bank Asset decreases by $\\text{KES } 10,000$ (New Bank = $\\text{KES } 75,000$); Creditors Liability decreases by $\\text{KES } 10,000$ (New Creditors = $\\text{KES } 30,000$).\n$$\\text{Total Assets} = 75,000 + 40,000 + 15,000 = \\text{KES } 130,000$$\n$$\\text{Total Claims} = \\text{Capital (100,000)} + \\text{Creditors (30,000)} = \\text{KES } 130,000$$\n$$\\text{Final Balance: } 130,000 = 130,000$$",
                            "**Step 6: Economic Interpretation & Common Pitfall:** After four transactions, Wanjala owns $\\text{KES } 130,000$ in total assets financed by $\\text{KES } 100,000$ of his own equity and $\\text{KES } 30,000$ in remaining supplier debt. *Common Pitfall:* Believing that buying stock for cash reduces total business wealth—it merely substitutes liquid cash for physical inventory."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Kitale Green Grocers",
                    "content": {
                        "title": "Inventory Replenishment and Supplier Credit Tracking in Trans-Nzoia",
                        "text": "In Kitale, Wanjala operates 'Kitale Green Grocers'. On Monday, Wanjala purchases 50 bags of potatoes on 14-day supplier credit from local farmers (increasing potato inventory and increasing trade creditors by KES 40,000). On Wednesday, he sells 20 bags for cash at cost (increasing cash and reducing potato stock by KES 16,000). On Friday, he pays the farmers KES 20,000 via mobile money. By tracking the dual effect of every transaction, Wanjala prevents cash shortfalls and maintains flawless credit reputation with farm suppliers."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How Transactions Change the Accounting Equation",
                    "content": {
                        "title": "Visualizing Dual Effects and Double Entry Accounting",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "Educational guide on transaction analysis, dual-entry principles, asset substitutions, and liability settlements."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Impact of Debt Repayment",
                    "content": {
                        "question": "A business owner pays KES 25,000 cash from the business bank account to settle an outstanding supplier invoice. What is the exact impact on the Accounting Equation?",
                        "options": [
                            "Bank Cash (Asset) decreases by KES 25,000 and Trade Creditors (Liability) decreases by KES 25,000",
                            "Bank Cash (Asset) decreases by KES 25,000 and Capital increases by KES 25,000",
                            "Trade Creditors (Liability) increases by KES 25,000 and Inventory (Asset) decreases by KES 25,000",
                            "There is no change because cash and debts cancel each other out"
                        ],
                        "correct": "A",
                        "explanation": "Settling a debt causes a cash outflow (reducing the Bank Asset by KES 25,000) and simultaneously extinguishes the creditor obligation (reducing the Liability by KES 25,000), keeping both sides of the equation in balance."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Asset Exchange Mechanics",
                    "content": {
                        "question": "When an entrepreneur uses KES 50,000 from the business cash till to purchase a new laptop for office bookkeeping, how are Total Assets and Owner's Capital affected?",
                        "options": [
                            "Total Assets increase by KES 50,000 and Capital increases by KES 50,000",
                            "Total Assets remain completely unchanged, and Owner's Capital remains unchanged",
                            "Total Assets decrease by KES 50,000 and Liabilities increase by KES 50,000",
                            "Total Assets increase by KES 50,000 and Liabilities decrease by KES 50,000"
                        ],
                        "correct": "B",
                        "explanation": "This is an Asset Exchange (Pattern 3): Office Equipment increases by KES 50,000 while Cash decreases by KES 50,000. Total asset value is unchanged and owner's capital is unaffected."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Dual Aspect Invariance:** Every transaction produces at least two offsetting ledger movements, preserving $Assets = Capital + Liabilities$.\n2. **Asset Exchanges:** Buying assets for cash or collecting debtor accounts alters asset composition without changing total asset value.\n3. **Parallel Expansion:** Injections of capital or credit acquisitions expand both sides of the accounting equation equally.\n4. **Parallel Contraction:** Paying creditors or owner drawings reduces total assets and total claims equally."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Comprehensive Accounting Equation Simulation
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Comprehensive Accounting Equation Simulation",
        "unit_description": "Multi-period cumulative transaction simulations, dynamic account balance progression, interim ledger tracking, and drafting post-transaction Statements of Financial Position.",
        "lesson_title": "Comprehensive Accounting Equation Simulation",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "M-Pesa and Banking Agent Services in Kenya",
                    "content": {
                        "title": "Commercial Financial Services and Logistics in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/M-PESA_mobile_money_and_Equity_agent%2C_Nairobi%2C_Kenya.jpg",
                        "caption": "A mobile money and commercial banking agent handling deposits and business transactions, reflecting daily working capital flows.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Trace sequential multi-day business transactions across a new enterprise startup\n- Calculate dynamic running balances for individual asset, liability, and capital accounts\n- Construct an updated Statement of Financial Position after sequential commercial events\n- Evaluate the liquidity and solvency of a growing enterprise through balance sheet simulation"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Cumulative Accounting Simulation",
                    "content": {
                        "term": "Transaction Simulation",
                        "definition": "The chronological recording and dynamic updating of financial transactions over an operating trading period to model how individual ledger accounts and total balance sheet values evolve over time."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Dynamic State Tracking and Interim Balance Sheets",
                    "content": {
                        "text": "Managing a live enterprise requires continuous accounting updates:\n\n- **Running Account Balances:** After every commercial transaction, the balance of specific accounts (e.g., Bank, Inventory, Creditors) must be recalculated immediately.\n- **Interim Balance Sheet:** A temporary Statement of Financial Position drafted at intermediate intervals (e.g., weekly or monthly) to assess liquidity and debt exposure before committing to major expenditures.\n- **Solvency Monitoring:** Ensuring that liquid current assets remain sufficient to settle maturing liabilities, avoiding bankruptcy risk during rapid business expansion."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Multi-Day Transaction Simulation Progression",
                    "content": {
                        "title": "Chronological Stepper & Balance Tracking (Baraka Deliveries)",
                        "caption": "High-precision vector SVG diagram depicting the multi-day progression of Baraka Tuk-Tuk Deliveries from Monday startup to Friday closing position, showing dynamic running totals.",
                        "svg_content": SVG_SIMULATION_PROGRESSION_TIMELINE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Multi-Day Transaction Log Matrix (Baraka Deliveries)",
                    "content": {
                        "headers": ["Day & Event", "Specific Account Shifts", "Total Assets (A)", "Total Liabilities (L)", "Owner's Capital (C)", "Equation Status"],
                        "rows": [
                            ["Day 0: Initial State", "No accounts active", "KES 0", "KES 0", "KES 0", "0 = 0 + 0 ✓"],
                            ["Mon: Capital Deposit", "Bank +150,000; Capital +150,000", "KES 150,000", "KES 0", "KES 150,000", "150K = 150K + 0 ✓"],
                            ["Tue: Buy Tuk-Tuk Cash", "Tuk-Tuk +120,000; Bank -120,000", "KES 150,000", "KES 0", "KES 150,000", "150K = 150K + 0 ✓"],
                            ["Wed: Spares on Credit", "Inventory +18,000; Creditors +18,000", "KES 168,000", "KES 18,000", "KES 150,000", "168K = 150K + 18K ✓"],
                            ["Thu: Bank Loan Inflow", "Bank +50,000; Loan +50,000", "KES 218,000", "KES 68,000", "KES 150,000", "218K = 150K + 68K ✓"],
                            ["Fri: Partial Debt Pay", "Bank -8,000; Creditors -8,000", "KES 210,000", "KES 60,000", "KES 150,000", "210K = 150K + 60K ✓"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: End-of-Week Statement of Financial Position Construction",
                    "content": {
                        "intro": "Halima runs 'Baraka Tuk-Tuk Deliveries' in Mombasa. Over her first week, she completes the following transactions: (1) Injects $\\text{KES } 150,000$ cash into bank as startup capital; (2) Buys a transport Tuk-Tuk for $\\text{KES } 120,000$ cash; (3) Buys spare tyres and fuel on credit for $\\text{KES } 18,000$ from Mombasa Auto Spares; (4) Obtains a $\\text{KES } 50,000$ microfinance loan deposited into bank; (5) Pays $\\text{KES } 8,000$ cash to Mombasa Auto Spares. Calculate final account balances and prepare Halima's Friday Statement of Financial Position.",
                        "steps": [
                            "**Step 1: Compute Running Balance for Each Account:**\n- **Motor Vehicle (Tuk-Tuk):** $0 + 120,000 = \\text{KES } 120,000$\n- **Inventory (Spares & Fuel):** $0 + 18,000 = \\text{KES } 18,000$\n- **Bank Cash:** $0 + 150,000 - 120,000 + 50,000 - 8,000 = \\text{KES } 72,000$\n- **Trade Creditors (Mombasa Auto):** $0 + 18,000 - 8,000 = \\text{KES } 10,000$\n- **Microfinance Loan:** $0 + 50,000 = \\text{KES } 50,000$\n- **Owner's Capital:** $0 + 150,000 = \\text{KES } 150,000$",
                            "**Step 2: Classify and Aggregate Assets:**\n$$\\text{Non-Current Assets} = \\text{Motor Vehicle} = \\text{KES } 120,000$$\n$$\\text{Current Assets} = \\text{Inventory } (18,000) + \\text{Bank Cash } (72,000) = \\text{KES } 90,000$$\n$$\\text{TOTAL ASSETS} = 120,000 + 90,000 = \\text{KES } 210,000$$",
                            "**Step 3: Classify and Aggregate Capital & Liabilities:**\n$$\\text{Owner's Capital} = \\text{KES } 150,000$$\n$$\\text{Non-Current Liabilities} = \\text{Microfinance Loan} = \\text{KES } 50,000$$\n$$\\text{Current Liabilities} = \\text{Trade Creditors} = \\text{KES } 10,000$$\n$$\\text{TOTAL CAPITAL \\& LIABILITIES} = 150,000 + 50,000 + 10,000 = \\text{KES } 210,000$$",
                            "**Step 4: Compute Working Capital:**\n$$\\text{Working Capital} = \\text{Current Assets } (90,000) - \\text{Current Liabilities } (10,000) = \\text{KES } 80,000$$",
                            "**Step 5: Final Statement Layout & Balance:**\n- Total Non-Current Assets = $\\text{KES } 120,000$\n- Total Current Assets = $\\text{KES } 90,000$\n- **TOTAL ASSETS = $\\text{KES } 210,000$**\n- Owner's Capital = $\\text{KES } 150,000$\n- Non-Current Liabilities = $\\text{KES } 50,000$\n- Current Liabilities = $\\text{KES } 10,000$\n- **TOTAL CAPITAL & LIABILITIES = $\\text{KES } 210,000$**",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Halima's enterprise is highly liquid and solvent: she holds $\\text{KES } 72,000$ in cash against only $\\text{KES } 10,000$ in short-term debts. *Common Pitfall:* Deducting the partial debt payment (KES 8,000) from Capital rather than reducing the Trade Creditors liability."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Baraka Tuk-Tuk Deliveries, Mombasa",
                    "content": {
                        "title": "Transport Fleet Expansion and Working Capital Management",
                        "text": "Operating from Mombasa's Old Town, Halima expanded 'Baraka Tuk-Tuk Deliveries' from a single vehicle to a small courier fleet servicing tourist hotels and coastal merchants. By maintaining strict multi-step accounting equation simulations, Halima tracked the impact of fuel credit lines, vehicle maintenance outlays, and microfinance loan servicing. This precise tracking prevented over-borrowing and enabled Baraka Deliveries to secure commercial insurance coverage on favorable terms."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Comprehensive Accounting Simulation and Balance Sheet Flow",
                    "content": {
                        "title": "Tracking Multi-Step Business Transactions",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "Step-by-step masterclass tracing multi-period business transactions, ledger updates, and balance sheet formulation."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Post-Transaction Balance Sheet Impact",
                    "content": {
                        "question": "In Halima's simulation, what was the net effect of paying KES 8,000 cash to Mombasa Auto Spares on Friday?",
                        "options": [
                            "Total Assets and Total Liabilities both decreased by KES 8,000, reducing the balance sheet total to KES 210,000",
                            "Total Assets increased by KES 8,000 while Capital decreased by KES 8,000",
                            "Total Liabilities decreased by KES 8,000 while Capital increased by KES 8,000",
                            "No change occurred on the balance sheet because it was an internal transfer"
                        ],
                        "correct": "A",
                        "explanation": "Paying cash to settle supplier debt reduces Bank Cash (Asset) by KES 8,000 and reduces Trade Creditors (Liability) by KES 8,000, bringing both balance sheet totals down from KES 218,000 to KES 210,000."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Impact of Commercial Loan Inflow",
                    "content": {
                        "question": "When a business borrows KES 50,000 from a microfinance bank and deposits it into its commercial bank account, what happens to Owner's Capital?",
                        "options": [
                            "Owner's Capital increases by KES 50,000",
                            "Owner's Capital decreases by KES 50,000",
                            "Owner's Capital remains unchanged because the loan is an external liability claim",
                            "Owner's Capital doubles automatically"
                        ],
                        "correct": "C",
                        "explanation": "Borrowing funds increases the Bank Cash Asset and increases Liabilities (Bank Loan). The owner's equity (Capital) is completely unaffected because the funds originate from external creditors."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Dynamic Progression:** A business's financial position evolves with every transaction, but the accounting equation remains in perpetual balance.\n2. **Account-by-Account Tracking:** Maintaining running balances for Cash, Inventory, Equipment, and Debts prevents double-entry bookkeeping discrepancies.\n3. **External Funding vs. Equity:** Commercial loans increase assets and liabilities simultaneously without altering the owner's initial capital stake.\n4. **Periodic Financial Snapshots:** Constructing regular Statements of Financial Position enables entrepreneurs to monitor working capital and solvency."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Net Worth and Capital Adjustments
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Net Worth and Capital Adjustments",
        "unit_description": "Dynamics of owner's equity, impact of Net Profit, Net Loss, Drawings, and Additional Capital injections, the Capital Adjustment Formula, and missing figure calculations.",
        "lesson_title": "Net Worth and Capital Adjustments",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Small Enterprise Proprietor in Kenya",
                    "content": {
                        "title": "Sole Proprietorship Commerce and Net Worth Growth in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Banana_Street_Vendor_Kenya.jpg",
                        "caption": "An active Kenyan micro-entrepreneur managing daily inventory and sales proceeds, demonstrating how operating profits build business net worth.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define Owner's Equity (Net Worth) and understand its dynamic determinants\n- Analyze the impact of Net Profit, Net Loss, Drawings, and Additional Capital on capital\n- Apply the Capital Adjustment Formula: $\\text{Closing Capital} = \\text{Opening Capital} + \\text{Net Profit} - \\text{Drawings} + \\text{Additional Capital}$\n- Solve for missing financial figures (Net Profit, Drawings, or Opening Capital) from incomplete accounting records"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Capital Adjustments and Net Worth",
                    "content": {
                        "term": "Capital Adjustment",
                        "definition": "The periodic accounting process of updating the owner's opening equity balance by adding net operating profits and additional capital injections, and subtracting net losses and personal drawings to determine the closing net worth of the enterprise."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Four Determinants of Capital Adjustments",
                    "content": {
                        "text": "An owner's equity in a business fluctuates based on four fundamental financial forces:\n\n- **1. Net Profit (NP):** The surplus earned when operating revenues exceed operating expenses ($\\text{Revenue} - \\text{Expenses} > 0$). Net profit belongs to the owner and directly increases Capital.\n- **2. Net Loss (NL):** The deficit incurred when operating expenses exceed revenues ($\\text{Expenses} - \\text{Revenue} > 0$). Net loss erodes business assets and reduces Capital.\n- **3. Drawings (D):** Any cash, inventory, or equipment withdrawn from the business by the owner for personal or family use. Drawings reduce Capital.\n- **4. Additional Capital (AC):** Fresh personal funds or private assets introduced into the business by the owner during the trading period, increasing Capital.\n- **The Capital Adjustment Formula:**\n$$\\text{Closing Capital } (C_e) = \\text{Opening Capital } (C_0) + \\text{Net Profit } (NP) - \\text{Drawings } (D) + \\text{Additional Capital } (AC)$$"
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Owner's Equity Reservoir & Capital Adjustment Flow",
                    "content": {
                        "title": "The Reservoir Model of Net Worth and Capital Inflows/Outflows",
                        "caption": "Precision vector SVG diagram illustrating the owner's capital tank, showing inflow pipes of Net Profit and Additional Capital, outflow pipes of Drawings and Losses, and the final Closing Capital gauge.",
                        "svg_content": SVG_CAPITAL_ADJUSTMENT_RESERVOIR
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Capital Adjustment Factors Matrix",
                    "content": {
                        "headers": ["Adjustment Factor", "Mathematical Sign", "Impact on Owner Equity", "Commercial Origin / Cause", "Kenyan SME Example"],
                        "rows": [
                            ["Opening Capital (C₀)", "Baseline (+)", "Starting net worth benchmark", "Cumulative past investments and retained profits", "KES 200,000 initial capital on 1st January"],
                            ["Net Trading Profit (+NP)", "Positive (+)", "Increases owner net worth", "Revenues exceed operating expenses", "KES 45,000 net profit from boutique dress sales"],
                            ["Additional Capital (+AC)", "Positive (+)", "Increases owner net worth", "Owner injects personal cash or private vehicle", "KES 15,000 personal savings added for festive stock"],
                            ["Owner Drawings (−D)", "Negative (−)", "Reduces owner net worth", "Owner withdraws cash or stock for household use", "KES 12,000 withdrawn to pay child's school fees"],
                            ["Net Trading Loss (−NL)", "Negative (−)", "Reduces owner net worth", "Operating expenses exceed sales revenue", "Deficit incurred during prolonged shop renovation"],
                            ["Closing Capital (C_end)", "Resultant (=)", "Final net worth at year-end", "Net mathematical sum of all equity movements", "KES 248,000 closing capital on 31st December"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Multi-Variable Capital Adjustment Calculations",
                    "content": {
                        "intro": "Solve the following two real-world capital adjustment problems for Kenyan retail enterprises:\n\n**Scenario A:** On 1st January 2026, Amina started 'Amina's Modern Boutique' in Kisumu with an Opening Capital of $\\text{KES } 200,000$. During the year, she earned a Net Profit of $\\text{KES } 45,000$, introduced Additional Capital of $\\text{KES } 15,000$, and withdrew $\\text{KES } 12,000$ for family school fees. Calculate Amina's Closing Capital as at 31st December 2026.\n\n**Scenario B:** Juma's electronics shop had an Opening Capital of $\\text{KES } 150,000$ and a Closing Capital of $\\text{KES } 175,000$. During the year, Juma made Drawings of $\\text{KES } 10,000$ and introduced no additional capital. Calculate Juma's Net Profit for the year.",
                        "steps": [
                            "**Step 1: Given Information:**\n- Scenario A: $C_0 = \\text{KES } 200,000$, $NP = \\text{KES } 45,000$, $AC = \\text{KES } 15,000$, $D = \\text{KES } 12,000$\n- Scenario B: $C_0 = \\text{KES } 150,000$, $C_e = \\text{KES } 175,000$, $D = \\text{KES } 10,000$, $AC = \\text{KES } 0$",
                            "**Step 2: Formula & Mathematical Rules:**\n$$\\text{Closing Capital } (C_e) = C_0 + NP - D + AC$$\n$$\\text{Rearranged for Net Profit: } NP = C_e - C_0 + D - AC$$",
                            "**Step 3: Substitution (Scenario A):**\n$$C_e = 200,000 + 45,000 - 12,000 + 15,000$$",
                            "**Step 4: Calculation (Scenario A):**\n$$C_e = 245,000 - 12,000 + 15,000 = 233,000 + 15,000 = \\text{KES } 248,000$$",
                            "**Step 5: Substitution & Calculation (Scenario B):**\n$$NP = 175,000 - 150,000 + 10,000 - 0$$\n$$NP = 25,000 + 10,000 = \\text{KES } 35,000$$",
                            "**Step 6: Economic Interpretation & Common Pitfall:** In Scenario A, Amina grew her personal wealth within the business by $\\text{KES } 48,000$ ($248,000 - 200,000$). In Scenario B, Juma's true operating profit was $\\text{KES } 35,000$, even though net worth only grew by $\\text{KES } 25,000$, because $\\text{KES } 10,000$ was siphoned out in personal drawings. *Common Pitfall:* Forgetting to add back drawings when rearranging the formula to solve for Net Profit."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Amina's Modern Boutique, Kisumu City",
                    "content": {
                        "title": "Balancing Reinvestment and Household Drawings in Kisumu",
                        "text": "Located along Oginga Odinga Street in Kisumu, Amina operates a thriving women's clothing boutique. To expand her product range, Amina reinvested 75% of her annual trading profits back into purchasing designer fabrics while limiting personal drawings strictly to essential household expenses. When reviewing her year-end financial position, Amina verified that her business net worth had expanded from KES 200,000 to KES 248,000, establishing a solid equity foundation that enabled her to open a second branch in Kakamega."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Understanding Owner's Equity and Capital Adjustments",
                    "content": {
                        "title": "Calculating Closing Capital, Profits, and Drawings",
                        "youtube_id": "0h6bXgW8VqM",
                        "url": "https://www.youtube.com/watch?v=0h6bXgW8VqM",
                        "description": "Comprehensive accounting tutorial covering capital adjustments, drawings effects, net profit allocation, and owner's equity equations."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Calculating Net Profit from Incomplete Records",
                    "content": {
                        "question": "A retail shop in Thika started the trading year with an Opening Capital of KES 120,000. During the year, the owner withdrew KES 15,000 for personal domestic use and made no additional capital contributions. If the Closing Capital at year-end was KES 145,000, what was the Net Profit earned during the year?",
                        "options": [
                            "KES 25,000",
                            "KES 40,000",
                            "KES 10,000",
                            "KES 145,000"
                        ],
                        "correct": "B",
                        "explanation": "Rearranging the capital adjustment formula: $\\text{Net Profit} = \\text{Closing Capital} - \\text{Opening Capital} + \\text{Drawings} = 145,000 - 120,000 + 15,000 = 25,000 + 15,000 = \\text{KES } 40,000$."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Impact of Drawings on Enterprise Capital",
                    "content": {
                        "question": "Why does an owner's withdrawal of cash for personal family use (Drawings) reduce the business Capital?",
                        "options": [
                            "Because drawings are classified as statutory government taxes",
                            "Because drawings represent an outflow of business assets without generating any commercial revenue, reducing the owner's residual equity stake",
                            "Because drawings automatically increase external trade liabilities",
                            "Because drawings are illegal under the Kenya Companies Act"
                        ],
                        "correct": "B",
                        "explanation": "Drawings reduce business assets (cash/inventory) for private non-commercial utility, directly shrinking the owner's residual financial interest (Capital) in the business."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Dynamic Equity:** Owner's Capital is not static; it increases through profits and capital additions and decreases through losses and drawings.\n2. **Capital Adjustment Formula:** $\\text{Closing Capital} = \\text{Opening Capital} + \\text{Net Profit} - \\text{Drawings} + \\text{Additional Capital}$.\n3. **Drawings Impact:** Withdrawing assets for private use directly drains business liquidity and erodes owner net worth.\n4. **Reinvestment Power:** Retaining trading profits within the enterprise builds long-term capital reserves and accelerates sustainable commercial expansion."
                    }
                }
            ]
        ]
    }
]
