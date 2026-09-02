"""
VLearn CBC Grade 10 Business Studies — Topic 3: Budgeting in Business
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic3_svgs import (
    SVG_BUDGET_FOUNDATIONS,
    SVG_MASTER_BUDGET_STRUCTURE,
    SVG_CASH_BUDGET_MECHANICS,
    SVG_MONTHLY_CASH_BUDGET,
    SVG_VARIANCE_ANALYSIS_FRAMEWORK,
    SVG_BUDGETARY_CONTROL_CYCLE
)

TOPIC_3_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Importance of Budgeting in Business
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Importance of Budgeting in Business",
        "unit_description": "Concept of budgets, financial roadmaps, cash inflows and outflows, surplus, deficit, and the managerial importance of budgeting.",
        "lesson_title": "Meaning and Importance of Budgeting in Business",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Trading in an Open-Air Kenyan Market",
                    "content": {
                        "title": "Cash Inflows and Daily Expenses in Retail Enterprise",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Traders at Wangige Market in Kiambu County managing daily cash collections from sales against inventory restocking payments and transport costs.",
                        "author": "Kristinabudiati",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a budget, budgeting, cash receipts, cash payments, surplus, and deficit\n- Explain the analogy of a financial roadmap in enterprise management\n- Distinguish between expected cash inflows (receipts) and planned cash outflows (payments)\n- Explain the primary management functions of budgeting (roadmap, control, resource allocation, and accountability)"
                    }
                }
            ],
            # Card 2: Core Concept & Formal Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Budget and Budgeting Defined",
                    "content": {
                        "term": "Business Budget",
                        "definition": "A formal financial plan, expressed in monetary terms, outlining an enterprise's expected cash inflows (receipts) and planned cash outflows (payments) over a specified future period."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Matatu Fuel Map Analogy",
                    "content": {
                        "text": "Imagine driving a passenger matatu from Nairobi to Nakuru with a fixed amount of fuel. If you drive without checking your fuel gauge or estimating consumption for the steep Great Rift Valley hills, you will run out of fuel mid-journey and strand your passengers.\n\nA **business budget** functions like a financial roadmap: it projects how much money you have at the start, how much you will burn on operating expenses, and where you will collect cash from sales to reach your profitability targets safely."
                    }
                }
            ],
            # Card 3: Vector SVG — Budget Architecture & Pillars
            [
                {
                    "type": "suggested_diagram",
                    "title": "Architecture and Core Pillars of a Business Budget",
                    "content": {
                        "title": "Cash Inflows, Outflows, and Strategic Budgetary Functions",
                        "caption": "Vector diagram illustrating how cash receipts and payments interact to create surpluses or deficits, supported by the four managerial functions of budgeting.",
                        "svg_content": SVG_BUDGET_FOUNDATIONS
                    }
                }
            ],
            # Card 4: Comparative Matrix — Inflows vs Outflows in Kenyan Enterprises
            [
                {
                    "type": "comparison_table",
                    "title": "Classification of Cash Inflows (Receipts) vs. Outflows (Payments)",
                    "content": {
                        "headers": ["Type of Enterprise", "Expected Cash Inflows (Receipts)", "Planned Cash Outflows (Payments)", "Net Cash Result Target"],
                        "rows": [
                            ["Retail Grocery Kiosk (Mama Mboga)", "Daily cash sales of vegetables, customer mobile money payments, trader Chama payouts", "Wholesale vegetable purchases at Marikiti, market stall rent, daily matatu transport fees", "Maintain positive daily cash surplus for stock restocking"],
                            ["Boda Boda Transport Group", "Passenger daily fares, parcel delivery fees, member monthly subscription shares", "Fuel and petrol purchases, routine engine oil servicing, county parking permits, loan repayments", "Accumulate cash surplus to service bike asset financing"],
                            ["Small-Scale Dairy Farm", "Daily raw milk sales to local collection centers, sale of organic manure to horticulture farmers", "Cattle feed (dairy meal/hay), veterinary medicines, farm hand wages, water pumping bills", "Ensure seasonal drought reserves and consistent working capital"],
                            ["Hairdressing Salon", "Client fees for braiding, hair washing, styling, and sale of beauty hair care products", "Shop rental, purchase of hair creams/weaves, electricity bills, stylist commissions", "Generate sufficient monthly cash to cover fixed rent and utilities"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation — Mama Jane's Kasarani Grocery
            [
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Calculation: Mama Jane's Monthly Budget Projection",
                    "content": {
                        "intro": "Mama Jane runs a retail grocery kiosk in Kasarani, Nairobi. She wants to plan her finances for January 2026 to ensure she has sufficient cash to pay her rent and avoid shop closure.",
                        "steps": [
                            "**Step 1: Identify the Given Financial Data:**\n- Opening Cash Balance ($A$) = $\\text{KES } 6,000$\n- Expected Cash Sales from vegetables = $\\text{KES } 95,000$\n- Youth Enterprise Cash Grant received = $\\text{KES } 10,000$\n- Wholesale stock purchases (vegetables/fruits) = $\\text{KES } 65,000$\n- Monthly kiosk stall rent = $\\text{KES } 10,000$\n- Daily matatu transport for produce = $\\text{KES } 8,000$\n- Electricity and county council market fees = $\\text{KES } 3,000$",
                            "**Step 2: State the Governing Formulas:**\n$$\\text{Total Cash Receipts } (B) = \\sum \\text{Cash Inflows}$$\n$$\\text{Total Cash Payments } (C) = \\sum \\text{Cash Outflows}$$\n$$\\text{Net Cash Flow } (D) = B - C$$\n$$\\text{Closing Cash Balance } (E) = A + D$$",
                            "**Step 3: Substitute the Given Values:**\n$$\\text{Total Cash Receipts } (B) = 95,000 + 10,000 = \\text{KES } 105,000$$\n$$\\text{Total Cash Payments } (C) = 65,000 + 10,000 + 8,000 + 3,000 = \\text{KES } 86,000$$",
                            "**Step 4: Compute the Monthly Net Cash Flow and Closing Balance:**\n$$\\text{Net Cash Flow } (D) = 105,000 - 86,000 = +\\text{KES } 19,000 \\text{ (Cash Surplus)}$$\n$$\\text{Closing Cash Balance } (E) = 6,000 + 19,000 = \\text{KES } 25,000$$",
                            "**Step 5: State the Final Answer:**\nMama Jane will generate a Net Cash Surplus of $\\text{KES } 19,000$ and conclude January with a healthy Closing Cash Balance of $\\text{KES } 25,000$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:**\n- **Strategic Value:** Because Mama Jane planned her cash flow in advance, she confirms that she can pay her $\\text{KES } 10,000$ rent comfortably without risking business eviction.\n- **Common Pitfall:** Confusing stock inventory on shelves with liquid cash. A business owner might have $\\text{KES } 50,000$ worth of vegetables on display, but if cash receipts are not budgeted, they will face a liquidity crisis when cash rent falls due."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Cash Flow Management in Kasarani Retail Trading",
                        "text": "In Kenyan micro-retail clusters such as Kasarani, Gikomba, and Kongowea, entrepreneurs who maintain written daily cash budgets are 70% less likely to suffer sudden insolvency compared to those who operate on informal guesswork. Disciplined budgeting allows small traders to negotiate bulk purchase discounts with wholesalers and secure emergency credit from commercial banks."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Budgeting Basics for Small Businesses & Entrepreneurs",
                    "content": {
                        "title": "Understanding Business Cash Flow and Budgeting",
                        "youtube_id": "qJ7v37s9yHk",
                        "url": "https://www.youtube.com/watch?v=qJ7v37s9yHk",
                        "description": "Educational guide explaining the essentials of budgeting, distinguishing cash inflows from outflows, and avoiding small business liquidity traps."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Definition of a Cash Surplus",
                    "content": {
                        "question": "Which of the following mathematical conditions defines a cash surplus in a monthly business budget?",
                        "options": [
                            "Planned Cash Payments exceed Expected Cash Receipts",
                            "Expected Cash Receipts exceed Planned Cash Payments",
                            "Opening Cash Balance is exactly equal to zero",
                            "Total assets are equal to total liabilities"
                        ],
                        "correct": "B",
                        "explanation": "A cash surplus occurs when expected cash inflows (receipts) are greater than planned cash outflows (payments), resulting in a positive Net Cash Flow ($Receipts > Payments$)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Core Purpose of Business Budgeting",
                    "content": {
                        "question": "Why is a business budget referred to as a 'financial roadmap' for an entrepreneur?",
                        "options": [
                            "It legally exempts the enterprise from paying county licensing fees",
                            "It guarantees that sales prices will never change during inflation",
                            "It outlines projected cash revenues and planned expenditures to guide spending and prevent liquidity crises",
                            "It automatically calculates corporate income tax without keeping accounting books"
                        ],
                        "correct": "C",
                        "explanation": "Like a physical roadmap, a budget guides management by forecasting future revenues and spending limits, ensuring the business stays solvent and achieves its targets."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 3: Identifying Cash Receipts",
                    "content": {
                        "question": "Which of the following items represents an Expected Cash Inflow (Receipt) for a commercial bakery?",
                        "options": [
                            "Purchasing 50 bags of baking flour on cash payment",
                            "Paying monthly electricity bills for baking ovens",
                            "Collecting cash from a local supermarket for bread delivered on 14-day credit",
                            "Paying monthly wages to assistant bakers"
                        ],
                        "correct": "C",
                        "explanation": "Collecting cash from debtors (credit customers) brings liquid cash into the business bank account, representing a cash receipt (inflow). The other options represent cash payments (outflows)."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary_card",
                    "title": "Lesson 1 Summary & Key Takeaways",
                    "content": {
                        "bullet_points": [
                            "A **business budget** is a quantitative financial forecast outlining expected income (receipts) and planned expenditures (payments) over a defined future period.",
                            "**Net Cash Flow** equals Total Cash Receipts minus Total Cash Payments ($Net = Receipts - Payments$).",
                            "A **Surplus** ($Receipts > Payments$) increases cash reserves; a **Deficit** ($Payments > Receipts$) drains reserves and requires short-term financing.",
                            "Budgeting serves four essential managerial functions: acting as a financial roadmap, enabling spending control, directing resource allocation, and establishing organizational accountability."
                        ]
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Types of Business Budgets
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Types of Business Budgets",
        "unit_description": "Classification of business budgets into operating budgets, financial budgets, flexibility classifications (fixed vs flexible), and the master budget.",
        "lesson_title": "Types of Business Budgets",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Industrial Production and Manufacturing Operations",
                    "content": {
                        "title": "Operational Planning in Commercial Production",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
                        "caption": "Manufactured cookware in an enterprise workshop, illustrating the need for production budgets, direct materials budgets, and labor planning to meet customer sales demand.",
                        "author": "Leonard Kisuu",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify business budgets into Operating Budgets, Financial Budgets, and Flexibility Budgets\n- Explain why the Sales Budget is the starting foundation stone for all operational plans\n- Describe the role and components of the Master Budget\n- Distinguish between Fixed (Static) Budgets and Flexible Budgets"
                    }
                }
            ],
            # Card 2: Core Concept & Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Operating, Financial, and Master Budgets Defined",
                    "content": {
                        "term": "Master Budget",
                        "definition": "The comprehensive, consolidated financial planning package that integrates all individual departmental operating budgets and financial budgets into a single unified blueprint."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Carpenter's Specialized Toolset Analogy",
                    "content": {
                        "text": "A master carpenter does not use a single hammer for every task; they carry measuring tapes, saws, chisels, and drills, each designed for a specific job.\n\nSimilarly, a business uses specialized budgets for each function: the sales team uses a **Sales Budget**, the factory uses a **Production Budget**, procurement uses a **Direct Materials Budget**, and finance uses a **Cash Budget**. The **Master Budget** brings all these tools together into one coordinated system."
                    }
                }
            ],
            # Card 3: Vector SVG — Master Budget Component Taxonomy
            [
                {
                    "type": "suggested_diagram",
                    "title": "Master Budget Taxonomy and Hierarchical Structure",
                    "content": {
                        "title": "Operating Budgets vs. Financial Budgets",
                        "caption": "Vector diagram illustrating the hierarchy of operating budgets (Sales, Production, Materials, Labor, Overhead) and financial budgets (Cash, CapEx, Budgeted Financial Statements).",
                        "svg_content": SVG_MASTER_BUDGET_STRUCTURE
                    }
                }
            ],
            # Card 4: Comparative Matrix — Comprehensive Budget Classifications
            [
                {
                    "type": "comparison_table",
                    "title": "Comparison of Business Budget Classifications",
                    "content": {
                        "headers": ["Budget Classification", "Core Focus", "Key Sub-Budgets Included", "Primary Department Responsible", "Key Decision Driven"],
                        "rows": [
                            ["Operating Budgets", "Day-to-day revenue-generating operations and direct manufacturing expenses", "Sales Budget, Production Budget, Direct Materials, Direct Labor, Overhead, Selling & Admin", "Sales, Production, Purchasing, and Marketing Departments", "Determines physical units to manufacture and input costs required"],
                            ["Financial Budgets", "Cash liquidity, long-term capital assets, and overall balance sheet health", "Cash Budget, Capital Expenditure Budget (CapEx), Budgeted Income Statement, Budgeted Balance Sheet", "Finance and Treasury Department", "Ensures business maintains liquid cash to pay maturing debts"],
                            ["Fixed (Static) Budgets", "Single activity level planning without variation", "Baseline annual departmental cost allocations", "Executive Management and Accounting", "Sets benchmark spending limits when production volume is predictable"],
                            ["Flexible Budgets", "Dynamic planning across multiple capacity levels (e.g. 60%, 80%, 100%)", "Variable cost flex schedules and stepped fixed cost plans", "Cost Accounting and Operations Management", "Adapts expense targets when customer demand fluctuates widely"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Production Budget Calculation — Kipekee Bakers
            [
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Calculation: Production Budget for Kipekee Bakers",
                    "content": {
                        "intro": "Kipekee Bakers in Nakuru is preparing its production budget for the month of April. The management wants to calculate exactly how many cakes must be baked to satisfy sales demand while maintaining safe buffer stock.",
                        "steps": [
                            "**Step 1: Identify the Given Financial and Production Data:**\n- Forecasted Sales Demand for April = $4,500\\text{ cakes}$\n- Desired Ending Finished Goods Inventory on April 30th = $600\\text{ cakes}$\n- Opening Finished Goods Inventory on April 1st = $350\\text{ cakes}$",
                            "**Step 2: State the Governing Production Formula:**\n$$\\text{Required Production Units} = \\text{Budgeted Sales Units} + \\text{Desired Ending Inventory} - \\text{Beginning Inventory}$$",
                            "**Step 3: Substitute the Given Values:**\n$$\\text{Required Production Units} = 4,500 + 600 - 350$$",
                            "**Step 4: Execute the Mathematical Steps:**\n$$\\text{Total Cakes Needed} = 4,500 + 600 = 5,100\\text{ cakes}$$\n$$\\text{Units to Manufacture} = 5,100 - 350 = 4,750\\text{ cakes}$$",
                            "**Step 5: State the Final Answer:**\nKipekee Bakers must bake exactly $4,750\\text{ cakes}$ during April.",
                            "**Step 6: Economic Interpretation & Common Pitfall:**\n- **Strategic Value:** Planning production prevents stockouts during peak retail hours while avoiding overbaking, which causes costly food spoilage.\n- **Common Pitfall:** Forgetting to subtract the beginning inventory ($350\\text{ cakes}$). If ignored, the bakery would produce $5,100\\text{ cakes}$, tying up working capital in excess perishable stock."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Commercial Bakery Operations in Nakuru",
                        "text": "Large-scale commercial bakeries in Nakuru County utilize integrated master budgets to coordinate their flour procurement, baker shift scheduling, and fleet distribution. By basing flour orders on weekly sales forecasts, these bakeries eliminate ingredient wastage and optimize bulk purchasing terms from grain millers in Eldoret."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Types of Business Budgets - Master, Operating & Financial",
                    "content": {
                        "title": "Navigating Operating and Financial Budgets",
                        "youtube_id": "X1Lp4mU4SjY",
                        "url": "https://www.youtube.com/watch?v=X1Lp4mU4SjY",
                        "description": "Comprehensive explanation of business budget types, showing how the sales budget feeds into production, materials, labor, and the master financial plan."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Starting Point of the Budgeting Cycle",
                    "content": {
                        "question": "Why is the Sales Budget considered the primary starting foundation stone of the entire master budgeting process?",
                        "options": [
                            "It calculates corporate tax liabilities due to the revenue authority",
                            "All production, raw materials, and labor requirements depend directly on expected sales volume",
                            "It measures the depreciation of long-term factory machinery",
                            "It must be officially audited by external accountants before any goods are made"
                        ],
                        "correct": "B",
                        "explanation": "A business cannot determine how many units to manufacture, how much raw material to purchase, or how many workers to hire until it establishes its forecasted sales volume."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Classification of Cash Budget",
                    "content": {
                        "question": "Under which main family of budgets is the Cash Budget classified?",
                        "options": [
                            "Operating Budgets",
                            "Manufacturing Overhead Budgets",
                            "Financial Budgets",
                            "Static Production Budgets"
                        ],
                        "correct": "C",
                        "explanation": "The Cash Budget is classified under Financial Budgets because it focuses on cash liquidity, working capital solvency, and cash flow timing rather than physical manufacturing operations."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 3: Flexible vs Fixed Budgets",
                    "content": {
                        "question": "What is the key distinguishing characteristic of a Flexible Budget compared to a Fixed (Static) Budget?",
                        "options": [
                            "A flexible budget applies only to non-profit charitable organizations",
                            "A flexible budget adjusts cost allowances dynamically across multiple levels of output activity",
                            "A flexible budget ignores all variable production expenses",
                            "A flexible budget is prepared only once every ten years"
                        ],
                        "correct": "B",
                        "explanation": "Unlike a fixed budget which is set for only one activity level, a flexible budget provides dynamic cost targets tailored to different capacity volumes (such as 60%, 80%, or 100% output)."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary_card",
                    "title": "Lesson 2 Summary & Key Takeaways",
                    "content": {
                        "bullet_points": [
                            "**Operating Budgets** plan day-to-day operations and include Sales, Production, Direct Materials, Direct Labor, Overhead, and Administrative expenses.",
                            "The **Sales Budget** is the foundation stone of all business planning because operational and purchasing budgets depend on projected customer demand.",
                            "**Financial Budgets** encompass the Cash Budget, Capital Expenditure Budget (CapEx), Budgeted Income Statement, and Budgeted Balance Sheet.",
                            "The **Master Budget** integrates all operational and financial sub-budgets into an overarching corporate blueprint.",
                            "**Fixed Budgets** plan for a single volume level, whereas **Flexible Budgets** dynamically adjust targets across varying output levels."
                        ]
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Cash Budget Structure and Assumptions
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Cash Budget Structure and Assumptions",
        "unit_description": "Components of a cash budget, timing of cash movements, accrual vs cash basis, excluding non-cash items, and carrying forward balances.",
        "lesson_title": "Cash Budget Structure and Assumptions",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Systematic Financial Record Keeping and Analysis",
                    "content": {
                        "title": "Tracking Physical Cash Inflows and Outflows",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg",
                        "caption": "An organized accounting workstation, demonstrating systematic tracking of liquid cash movements, bank balances, and supplier payments.",
                        "author": "Kristin Dos Santos",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the structure of a standard monthly Cash Budget\n- Apply the Water Tank model to understand cash accumulation and drainage\n- Differentiate cash accounting from accrual accounting in cash budget preparation\n- Identify and exclude non-cash accounting adjustments (such as depreciation)\n- Explain how closing balances are carried forward as opening balances for subsequent months"
                    }
                }
            ],
            # Card 2: Core Concept & Definitions
            [
                {
                    "type": "definition_card",
                    "title": "Cash Budget and Strict Cash Basis Defined",
                    "content": {
                        "term": "Cash Budget",
                        "definition": "A detailed schedule forecasting expected physical cash receipts and disbursements over specified future time intervals, determining expected cash surplus or deficit."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Liquidity Water Tank Analogy",
                    "content": {
                        "text": "Think of your business bank account as a water storage tank:\n\n- **Opening Cash Balance:** The water level already in the tank on the 1st of the month.\n- **Cash Inflows (Receipts):** Water pumped into the tank from sales, loan disbursements, and debtor collections.\n- **Cash Outflows (Payments):** Water drained out through bottom taps for rent, stock purchases, wages, and utilities.\n- **Closing Cash Balance:** The water remaining at the end of the month, which immediately becomes the **Opening Balance** for the following month."
                    }
                }
            ],
            # Card 3: Vector SVG — Cash Budget Mechanics & Rules
            [
                {
                    "type": "suggested_diagram",
                    "title": "Cash Budget Mechanics and the Liquidity Water Tank",
                    "content": {
                        "title": "The Mathematical Flow of Business Liquidity",
                        "caption": "Vector diagram illustrating the water tank model, Net Cash Flow formulas, strict cash accounting rules, and the non-cash exclusion principle.",
                        "svg_content": SVG_CASH_BUDGET_MECHANICS
                    }
                }
            ],
            # Card 4: Comparative Matrix — Cash Budget vs Budgeted Income Statement
            [
                {
                    "type": "comparison_table",
                    "title": "Cash Budget vs. Budgeted Income Statement (Profit & Loss)",
                    "content": {
                        "headers": ["Comparison Feature", "Cash Budget", "Budgeted Income Statement (P&L)", "Why the Distinction Matters"],
                        "rows": [
                            ["Accounting Basis", "Strict Cash Basis (records physical cash movements only)", "Accrual Basis (records revenue when earned and expenses when incurred)", "A profitable business on paper can go bankrupt if cash is tied up in uncollected debts"],
                            ["Credit Sales Treatment", "Recorded ONLY when cash is physically collected from debtors", "Recorded in full at the time the sales invoice is issued", "Prevents overestimating available spending cash before customers actually pay"],
                            ["Non-Cash Items (Depreciation)", "STRICTLY EXCLUDED (no physical cash leaves the business)", "INCLUDED as an operating expense to reduce taxable accounting profit", "Deducting depreciation from cash budget causes false cash deficit alarms"],
                            ["Capital Expenditures (Asset Purchases)", "Included in FULL in the month the asset is paid for in cash", "Excluded from P&L (only monthly depreciation is charged)", "Reflects large cash outflows required to purchase delivery vans or machinery"],
                            ["Primary Financial Objective", "Liquidity Management & Solvency (Can we pay bills this month?)", "Profitability Assessment (Did operations generate overall net income?)", "Both statements are complementary but serve distinct managerial purposes"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation — Kivali School Tuck Shop
            [
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Calculation: Kivali School Tuck Shop Term 1 Cash Budget",
                    "content": {
                        "intro": "The student enterprise committee of Kivali School Tuck Shop in Machakos is preparing their January cash budget. They need to calculate their expected closing cash balance.",
                        "steps": [
                            "**Step 1: Identify the Given Financial Data:**\n- Opening Cash Balance on January 1st ($A$) = $\\text{KES } 15,000$\n- Cash sales of snacks and stationery = $\\text{KES } 48,000$\n- Cash collected from teachers' credit accounts = $\\text{KES } 12,000$\n- Payments for wholesale snack inventory restock = $\\text{KES } 38,000$\n- Monthly stall rent paid to school administration = $\\text{KES } 6,000$\n- Display counter depreciation (Book expense) = $\\text{KES } 4,000$\n- Credit sales made to students payable in February = $\\text{KES } 7,000$",
                            "**Step 2: Apply Cash Accounting Rules and Exclusions:**\n- **Exclude Depreciation ($\\text{KES } 4,000$):** Depreciation is a non-cash accounting entry. Zero liquid cash moves.\n- **Exclude February Credit Sales ($\\text{KES } 7,000$):** Uncollected credit is not cash in hand; it will be recorded in February when paid.",
                            "**Step 3: State the Formulas and Substitute Values:**\n$$\\text{Total Cash Receipts } (B) = 48,000 + 12,000 = \\text{KES } 60,000$$\n$$\\text{Total Cash Payments } (C) = 38,000 + 6,000 = \\text{KES } 44,000$$\n$$\\text{Net Cash Flow } (D) = B - C = 60,000 - 44,000 = +\\text{KES } 16,000$$",
                            "**Step 4: Calculate the January Closing Cash Balance:**\n$$\\text{Closing Cash Balance } (E) = A + D = 15,000 + 16,000 = \\text{KES } 31,000$$",
                            "**Step 5: State the Final Answer:**\nKivali School Tuck Shop generates a Net Cash Surplus of $\\text{KES } 16,000$, resulting in a January Closing Cash Balance of $\\text{KES } 31,000$ (which carries forward as February's Opening Balance).",
                            "**Step 6: Economic Interpretation & Common Pitfall:**\n- **Strategic Value:** The tuck shop has $\\text{KES } 31,000$ liquid cash available to fund inventory expansions in February.\n- **Common Pitfall:** Subtracting depreciation ($\\text{KES } 4,000$) would mistakenly report closing cash as $\\text{KES } 27,000$, misrepresenting actual bank liquidity."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Managing High School Tuck Shops and Canteens",
                        "text": "School-based student enterprises in Machakos County use weekly cash budgets to manage seasonal demand peaks during sports days and visiting days. By separating uncollected credit sales from cash receipts, student treasurers ensure they never default on supplier payments for milk and fresh bakery deliveries."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "How Cash Budgets Work - Cash Inflows vs Cash Outflows",
                    "content": {
                        "title": "Mastering the Mechanics of Cash Budgets",
                        "youtube_id": "sVKQn2v8KYQ",
                        "url": "https://www.youtube.com/watch?v=sVKQn2v8KYQ",
                        "description": "Visual breakdown of cash inflows, outflows, timing differences, and the strict exclusion of non-cash expenses in financial planning."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Treatment of Depreciation in Cash Budgets",
                    "content": {
                        "question": "Why is depreciation expense strictly excluded from a business's Cash Budget?",
                        "options": [
                            "Because depreciation is only calculated by government tax inspectors",
                            "Because depreciation is a non-cash book adjustment that involves no physical outflow of liquid money",
                            "Because depreciation is classified as a cash inflow rather than an outflow",
                            "Because depreciation only applies to businesses operating in the transport sector"
                        ],
                        "correct": "B",
                        "explanation": "A Cash Budget exclusively tracks physical movements of money. Depreciation represents the wear-and-tear book valuation of assets and involves no cash transaction; hence it is excluded."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Carry-Forward Principle",
                    "content": {
                        "question": "What is the standard procedure for handling the Closing Cash Balance of January when preparing a multi-month cash budget?",
                        "options": [
                            "It is reset to zero at the start of February",
                            "It is transferred to the government as revenue tax",
                            "It automatically becomes the Opening Cash Balance for the month of February",
                            "It is added to total sales revenue as an extra income item in February"
                        ],
                        "correct": "C",
                        "explanation": "Cash remaining in the bank or till at the close of one month (January 31st) is the exact cash available at the dawn of the next month (February 1st), serving as February's Opening Balance."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 3: Credit Sales Timing",
                    "content": {
                        "question": "A retail shop sells goods worth KES 25,000 on credit in March, with the customer agreeing to pay in April. How should this transaction be recorded in the Cash Budget?",
                        "options": [
                            "Recorded as a Cash Receipt in March",
                            "Recorded as a Cash Receipt in April when the physical cash is collected",
                            "Recorded as a Cash Payment in March",
                            "Excluded completely from all financial records"
                        ],
                        "correct": "B",
                        "explanation": "Cash budgets follow strict cash timing rules. Credit sales are recorded only in the specific month when physical cash is received from the debtor (April)."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary_card",
                    "title": "Lesson 3 Summary & Key Takeaways",
                    "content": {
                        "bullet_points": [
                            "A **Cash Budget** tracks the flow of physical money in and out of an enterprise over successive periods.",
                            "The **Water Tank Principle** demonstrates that Closing Balance = Opening Balance + Receipts − Payments.",
                            "**Strict Cash Accounting:** Credit transactions are recognized only when physical cash changes hands.",
                            "**Non-Cash Exclusion:** Depreciation, bad debt write-offs, and asset revaluations are strictly excluded from cash budgets.",
                            "The **Carry-Forward Rule:** The closing cash balance of Month $t$ is always the opening cash balance of Month $t+1$."
                        ]
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Preparing a Simple Monthly Cash Budget
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Preparing a Simple Monthly Cash Budget",
        "unit_description": "Comprehensive practical preparation of multi-month cash budgets, numerical reconciliation, capital expenditure evaluation, and solvency analysis.",
        "lesson_title": "Preparing a Simple Monthly Cash Budget",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Artisan Electronics Repair and Small Enterprise Operations",
                    "content": {
                        "title": "Managing Capital Outlays and Cash Reserves in Micro-Enterprises",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
                        "caption": "A skilled artisan enterprise in Nairobi's informal sector, illustrating the necessity of multi-month cash planning before purchasing expensive specialized equipment.",
                        "author": "Harold Odhiambo Otieno",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Construct a complete multi-column monthly Cash Budget from raw financial transactions\n- Categorize monthly cash inflows and outflows into structured lines\n- Accurately compute Net Cash Flow and carry forward closing balances across multiple months\n- Evaluate whether an enterprise has sufficient liquidity to execute capital equipment purchases"
                    }
                }
            ],
            # Card 2: Core Concept & Methodical Preparation Steps
            [
                {
                    "type": "definition_card",
                    "title": "Multi-Period Cash Budgeting Defined",
                    "content": {
                        "term": "Multi-Month Cash Budget",
                        "definition": "A comparative financial schedule displaying sequential monthly cash receipts, disbursements, net cash flows, and cumulative balances to project medium-term liquidity trends."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 6-Step Methodical Construction Protocol",
                    "content": {
                        "text": "To prepare an error-free cash budget for any enterprise:\n\n1. **Establish Opening Cash:** Record verified liquid cash in bank and till on Day 1.\n2. **Schedule Cash Receipts:** Tabulate monthly cash sales, debtor collections, and non-operating cash incomes.\n3. **Schedule Cash Payments:** Itemize inventory purchases, operating rent, utilities, wages, and capital outlays.\n4. **Compute Net Cash Flow:** Calculate $D = \\text{Total Receipts } (B) - \\text{Total Payments } (C)$.\n5. **Determine Closing Cash:** Compute $E = \\text{Opening Cash } (A) + \\text{Net Cash Flow } (D)$.\n6. **Carry Forward:** Transfer Closing Cash of Month 1 to Opening Cash of Month 2."
                    }
                }
            ],
            # Card 3: Vector SVG — Multi-Month Numerical Table
            [
                {
                    "type": "suggested_diagram",
                    "title": "Multi-Month Cash Budget: Baraka Mobile Repair Shop",
                    "content": {
                        "title": "Two-Month Cash Budget Numerical Model",
                        "caption": "Vector diagram illustrating the line-by-line financial model for January and February 2026, highlighting receipts, payments, surplus, and the carry-forward link.",
                        "svg_content": SVG_MONTHLY_CASH_BUDGET
                    }
                }
            ],
            # Card 4: Comparative Matrix — Complete Spreadsheet Layout
            [
                {
                    "type": "comparison_table",
                    "title": "Baraka Mobile Repair Shop — Comprehensive Cash Budget Schedule",
                    "content": {
                        "headers": ["Budget Financial Line Item", "January 2026 (KES)", "February 2026 (KES)", "Financial Category & Operational Note"],
                        "rows": [
                            ["Opening Cash Balance (A)", "20,000", "21,000", "Base liquidity starting position (Feb carries forward Jan Closing)"],
                            ["Cash Sales (Repair Services)", "30,000", "45,000", "Direct cash payments from walk-in repair customers"],
                            ["Debtor Collections (Credit Schools)", "—", "10,000", "Collection of January phone repairs done on 30-day credit for local schools"],
                            ["Total Cash Receipts (B)", "30,000", "55,000", "Total liquid inflows entering enterprise bank account"],
                            ["Spare Parts Purchases (Screens/Batteries)", "15,000", "20,000", "Cash payments to electronics wholesale importers in Kisumu"],
                            ["Rent Expense (Workshop Stall)", "8,000", "8,000", "Fixed monthly premises rent paid to commercial landlord"],
                            ["Assistant Technician Wages", "6,000", "6,000", "Monthly remuneration for skilled repair technician assistant"],
                            ["Micro-Soldering Tool (CapEx)", "—", "12,000", "One-time capital equipment acquisition to enable motherboard repairs"],
                            ["Total Cash Payments (C)", "29,000", "46,000", "Total liquid outflows disbursed during the month"],
                            ["Net Cash Flow (D = B − C)", "+1,000", "+9,000", "Operating monthly cash surplus generated by business operations"],
                            ["Closing Cash Balance (E = A + D)", "21,000", "30,000", "Cumulative liquidity reserve at month-end available for next cycle"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation — Baraka Mobile Repair Shop
            [
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Calculation: Otieno's Two-Month Cash Reconciliation",
                    "content": {
                        "intro": "Otieno operates Baraka Mobile Repair Shop in Kisumu. He wants to know if his business can afford to buy a specialized KES 12,000 micro-soldering station in February 2026 without running into a cash deficit.",
                        "steps": [
                            "**Step 1: Reconcile January Cash Flow:**\n- Opening Balance ($A_1$) = $\\text{KES } 20,000$\n- Total Receipts ($B_1$) = Cash Sales = $\\text{KES } 30,000$\n- Total Payments ($C_1$) = Parts ($15,000$) + Rent ($8,000$) + Wages ($6,000$) = $\\text{KES } 29,000$\n- Net Cash Flow ($D_1$) = $30,000 - 29,000 = +\\text{KES } 1,000 \\text{ (Surplus)}$\n- Closing Cash Balance ($E_1$) = $20,000 + 1,000 = \\text{KES } 21,000$",
                            "**Step 2: Carry Forward to February:**\n- February Opening Balance ($A_2$) = January Closing Balance ($E_1$) = $\\text{KES } 21,000$",
                            "**Step 3: Reconcile February Cash Flow:**\n- Total Receipts ($B_2$) = Cash Sales ($45,000$) + Debtor Collections ($10,000$) = $\\text{KES } 55,000$\n- Total Payments ($C_2$) = Parts ($20,000$) + Rent ($8,000$) + Wages ($6,000$) + Tool ($12,000$) = $\\text{KES } 46,000$\n- Net Cash Flow ($D_2$) = $55,000 - 46,000 = +\\text{KES } 9,000 \\text{ (Surplus)}$\n- Closing Cash Balance ($E_2$) = $21,000 + 9,000 = \\text{KES } 30,000$",
                            "**Step 4: Evaluate Capital Investment Feasibility:**\n- Tool Cost = $\\text{KES } 12,000$\n- Net Cash Flow in Feb remains positive ($+\\text{KES } 9,000$)\n- Ending Cash Balance remains robust at $\\text{KES } 30,000$",
                            "**Step 5: Final Managerial Decision:**\nYes! Otieno can safely buy the micro-soldering station in February. His business maintains a strong liquidity cushion of $\\text{KES } 30,000$, ensuring zero risk of insolvency.",
                            "**Step 6: Economic Interpretation & Common Pitfall:**\n- **Strategic Value:** Budgeting allows small enterprises to invest in growth assets (machinery) using accumulated operating cash surpluses rather than taking high-interest loans.\n- **Common Pitfall:** Failing to carry forward January's closing balance ($\text{KES } 21,000$) to February, which would wrongly show February's closing balance as only $\text{KES } 9,000$ instead of the true $\text{KES } 30,000$."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Electronics Repair Enterprises in Kisumu",
                        "text": "Electronics and mobile phone repair technicians in Kisumu's Jua Kali sector rely on cash budgeting to plan for high-cost diagnostic tools, screen laminators, and microscope equipment. Staggering capital equipment purchases during high-revenue seasonal months protects working capital and preserves credit ratings with spare parts distributors."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Preparing a Monthly Cash Budget Example",
                    "content": {
                        "title": "Step-by-Step Construction of a Monthly Cash Budget",
                        "youtube_id": "8i_rK19CgHw",
                        "url": "https://www.youtube.com/watch?v=8i_rK19CgHw",
                        "description": "Practical walkthrough demonstrating the step-by-step construction of a multi-month cash budget, calculating Net Cash Flow, and carrying forward closing balances."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Impact of Expense Reduction on Closing Cash",
                    "content": {
                        "question": "If Otieno negotiates a KES 1,000 rent discount in February (reducing rent from KES 8,000 to KES 7,000), how will this affect his calculated February Closing Cash Balance?",
                        "options": [
                            "It will decrease the February closing cash balance by KES 1,000",
                            "It will increase the February closing cash balance by KES 1,000 (from KES 30,000 to KES 31,000)",
                            "It will have zero effect because rent is a fixed contract",
                            "It will turn the January surplus into a deficit"
                        ],
                        "correct": "B",
                        "explanation": "A reduction in cash payments decreases Total Outflows ($C$), which increases Net Cash Flow ($D$) and increases the Closing Cash Balance ($E$) by that exact amount (KES 1,000)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Evaluating Capital Equipment Outlays",
                    "content": {
                        "question": "Under what condition is it safe for a small enterprise to purchase a high-cost capital asset using cash reserves?",
                        "options": [
                            "When the projected closing cash balance remains positive and leaves an adequate operational liquidity buffer",
                            "Only when the business has zero outstanding debtors",
                            "When total payments exceed total receipts for three consecutive years",
                            "Only when the government offers a 100% tax grant"
                        ],
                        "correct": "A",
                        "explanation": "A business can safely purchase capital assets in cash when its budgeted cash flow confirms that the closing balance remains comfortably positive to fund routine operating bills."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 3: Net Cash Flow Calculation",
                    "content": {
                        "question": "A kiosk trader has Total Cash Receipts of KES 75,000 and Total Cash Payments of KES 82,000 in June. What is the Net Cash Flow for June?",
                        "options": [
                            "+KES 7,000 surplus",
                            "-KES 7,000 deficit",
                            "+KES 157,000",
                            "Zero"
                        ],
                        "correct": "B",
                        "explanation": "Net Cash Flow = Receipts (75,000) − Payments (82,000) = -KES 7,000 (a Net Cash Deficit of KES 7,000)."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary_card",
                    "title": "Lesson 4 Summary & Key Takeaways",
                    "content": {
                        "bullet_points": [
                            "A **Multi-Month Cash Budget** connects sequential trading periods via the carry-forward link ($Closing_t = Opening_{t+1}$).",
                            "**Net Cash Flow** ($D = B - C$) reflects monthly cash generation, independent of the opening balance.",
                            "**Closing Cash Balance** ($E = A + D$) represents the total liquidity reserve at the end of each period.",
                            "Preparing monthly cash budgets enables entrepreneurs to safely schedule capital equipment purchases (CapEx) without triggering cash crises."
                        ]
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Using a Budget to Control Spending (Variance Analysis)
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Using a Budget to Control Spending (Variance Analysis)",
        "unit_description": "Concept of variance, calculating variances, directional classification (Favourable vs Unfavourable), and implementing corrective managerial actions.",
        "lesson_title": "Using a Budget to Control Spending (Variance Analysis)",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Financial Analysis and Performance Review",
                    "content": {
                        "title": "Auditing Actual Results Against Budgeted Targets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
                        "caption": "An analyst comparing budgeted spending figures against actual ledger records on a financial spreadsheet, identifying cost overruns and revenue gains.",
                        "author": "Dave Dugdale",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a variance and explain the purpose of variance analysis in business control\n- Calculate numerical variances using the formula: $Variance = Actual - Budget$\n- Classify variances as Favourable (F) or Unfavourable (U) for both income and expense items\n- Interpret variance reports and prescribe corrective managerial actions to restore financial discipline"
                    }
                }
            ],
            # Card 2: Core Concept & Directional Rules
            [
                {
                    "type": "definition_card",
                    "title": "Variance and Variance Analysis Defined",
                    "content": {
                        "term": "Variance Analysis",
                        "definition": "The quantitative management process of calculating differences between actual financial results and budgeted targets, investigating root causes, and applying corrective actions."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Directional Rules of Financial Variances",
                    "content": {
                        "text": "A variance is not merely a positive or negative number; its business meaning depends on whether the line item represents **Income** or **Expenditure**:\n\n- **Income Items (Sales, Collections):**\n  - $\\text{Actual} > \\text{Budget} \\implies$ **Favourable (F)** (More cash earned).\n  - $\\text{Actual} < \\text{Budget} \\implies$ **Unfavourable (U)** (Less cash earned).\n- **Expense Items (Purchases, Rent, Utilities, Wages):**\n  - $\\text{Actual} > \\text{Budget} \\implies$ **Unfavourable (U)** (Cost overrun drains cash).\n  - $\\text{Actual} < \\text{Budget} \\implies$ **Favourable (F)** (Cost savings preserve cash)."
                    }
                }
            ],
            # Card 3: Vector SVG — Variance Analysis Decision Matrix
            [
                {
                    "type": "suggested_diagram",
                    "title": "Variance Analysis Decision Framework and Directional Rules",
                    "content": {
                        "title": "Classifying Financial Variances and Corrective Feedback Loops",
                        "caption": "Vector diagram illustrating the directional classification of income vs. expense variances and the management corrective action protocol.",
                        "svg_content": SVG_VARIANCE_ANALYSIS_FRAMEWORK
                    }
                }
            ],
            # Card 4: Comparative Matrix — Income vs Expense Variance Rules
            [
                {
                    "type": "comparison_table",
                    "title": "Income Variances vs. Expenditure Variances Matrix",
                    "content": {
                        "headers": ["Financial Category", "Condition ($Actual \\text{ vs. } Budget$)", "Variance Direction", "Effect on Business Cash", "Typical Enterprise Example"],
                        "rows": [
                            ["Revenue / Cash Inflows", "Actual Sales > Budgeted Sales", "Favourable (F)", "Increases cash reserves above planned levels", "Budgeted KES 30,000 sales; Actual KES 34,000 (+KES 4,000 F)"],
                            ["Revenue / Cash Inflows", "Actual Debtors < Budgeted Debtors", "Unfavourable (U)", "Decreases cash collected; shrinks liquidity", "Budgeted KES 50,000 collections; Actual KES 45,000 (-KES 5,000 U)"],
                            ["Expenditure / Cash Outflows", "Actual Costs > Budgeted Costs", "Unfavourable (U)", "Drains cash reserves; erodes profitability", "Budgeted KES 15,000 spare parts; Actual KES 18,000 (KES 3,000 U overspend)"],
                            ["Expenditure / Cash Outflows", "Actual Costs < Budgeted Costs", "Favourable (F)", "Preserves liquid cash through cost efficiencies", "Budgeted KES 2,000 electricity; Actual KES 1,500 (KES 500 F cost saving)"],
                            ["All Line Items", "Actual Result = Budgeted Figure", "Nil (Zero Variance)", "Exact alignment with management plan", "Budgeted rent KES 8,000; Actual rent KES 8,000 (Zero variance)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation — Baraka Shop January Variance Report
            [
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Calculation: January Variance Audit for Baraka Shop",
                    "content": {
                        "intro": "At the end of January, Otieno compares his actual financial ledger against his planned budget figures. Calculate the variance for each line item and assign the correct direction (F or U).",
                        "steps": [
                            "**Step 1: Identify Budgeted vs. Actual Data:**\n- **Cash Sales:** Budget = $\\text{KES } 30,000$; Actual = $\\text{KES } 34,000$\n- **Spare Parts Purchases:** Budget = $\\text{KES } 15,000$; Actual = $\\text{KES } 18,000$\n- **Workshop Electricity Bill:** Budget = $\\text{KES } 2,000$; Actual = $\\text{KES } 1,500$\n- **Debtor Collections:** Budget = $\\text{KES } 10,000$; Actual = $\\text{KES } 8,000$",
                            "**Step 2: State the Universal Variance Formula:**\n$$\\text{Variance} = \\text{Actual Result} - \\text{Budgeted Figure}$$",
                            "**Step 3: Calculate Line-by-Line:**\n- **1. Cash Sales (Income):**\n  $$\\text{Variance} = 34,000 - 30,000 = +\\text{KES } 4,000 \\implies \\mathbf{KES\\ 4,000\\ (F)}$$\n- **2. Spare Parts (Expense):**\n  $$\\text{Variance} = 18,000 - 15,000 = +\\text{KES } 3,000 \\implies \\mathbf{KES\\ 3,000\\ (U)}$$\n- **3. Electricity Bill (Expense):**\n  $$\\text{Variance} = 1,500 - 2,000 = -\\text{KES } 500 \\implies \\mathbf{KES\\ 500\\ (F)}$$\n- **4. Debtor Collections (Income):**\n  $$\\text{Variance} = 8,000 - 10,000 = -\\text{KES } 2,000 \\implies \\mathbf{KES\\ 2,000\\ (U)}$$",
                            "**Step 4: Compile the Formal Variance Table:**\n- Cash Sales: $\\text{KES } 4,000\\text{ (F)}$\n- Spare Parts: $\\text{KES } 3,000\\text{ (U)}$\n- Electricity: $\\text{KES } 500\\text{ (F)}$\n- Debtor Collections: $\\text{KES } 2,000\\text{ (U)}$",
                            "**Step 5: Prescribe Corrective Managerial Actions:**\n- **Spare Parts (KES 3,000 U):** Investigate why parts costs rose. Check if the supplier permanently raised prices or if technicians damaged screens during installation. Renegotiate wholesale pricing or adjust repair price list.\n- **Debtors (KES 2,000 U):** Tighten credit control terms for client schools and send formal payment reminders.\n- **Sales (KES 4,000 F):** Identify top-performing marketing tactics (e.g. social media ads) and replicate them in February.",
                            "**Step 6: Economic Interpretation & Common Pitfall:**\n- **Strategic Value:** Variance analysis directs management attention exclusively to areas where performance deviated from plan (Management by Exception).\n- **Common Pitfall:** Treating mathematical plus ($+$) as always good and minus ($-$) as bad. In expenses, $+3,000$ indicates an overspend (Unfavourable), while $-500$ indicates a cost saving (Favourable)."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Cost Control in Eldoret Agri-Processing SMEs",
                        "text": "Agri-processing enterprises in Eldoret review monthly variance reports to monitor raw maize and diesel drying fuel costs. When fuel expenses show an unfavourable variance exceeding 10%, factory managers immediately service boiler engines and renegotiate bulk supply contracts with petroleum distributors to restore target profit margins."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Variance Analysis - Favourable vs Unfavourable Variances Explained",
                    "content": {
                        "title": "Understanding Financial Variance Analysis",
                        "youtube_id": "p6r7S9qH1kU",
                        "url": "https://www.youtube.com/watch?v=p6r7S9qH1kU",
                        "description": "Clear educational explanation of variance analysis, calculating actual vs budgeted differences, and assigning favourable and unfavourable directions."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Expense Variance Classification",
                    "content": {
                        "question": "A boutique owner budgeted KES 12,000 for transport, but the actual transport bill came to KES 9,500. What is the variance and its directional classification?",
                        "options": [
                            "KES 2,500 Unfavourable (U)",
                            "KES 2,500 Favourable (F)",
                            "KES 21,500 Favourable (F)",
                            "Nil"
                        ],
                        "correct": "B",
                        "explanation": "For expense items, spending LESS than budgeted ($9,500 < 12,000$) saves liquid cash for the enterprise, resulting in a KES 2,500 Favourable (F) variance."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Revenue Variance Classification",
                    "content": {
                        "question": "A hardware store budgeted to collect KES 200,000 from cash sales in May, but actual cash sales reached only KES 175,000. How is this variance classified?",
                        "options": [
                            "KES 25,000 Favourable (F)",
                            "KES 25,000 Unfavourable (U)",
                            "KES 375,000 Unfavourable (U)",
                            "Zero variance"
                        ],
                        "correct": "B",
                        "explanation": "For income items, generating LESS cash revenue than planned ($175,000 < 200,000$) reduces cash inflow, resulting in a KES 25,000 Unfavourable (U) variance."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 3: Purpose of Variance Analysis",
                    "content": {
                        "question": "What is the primary management objective of performing variance analysis at the end of every month?",
                        "options": [
                            "To legally punish suppliers for market price changes",
                            "To discover where actual performance differed from the budget, understand why, and take corrective action",
                            "To eliminate the need for future cash budgeting",
                            "To convert fixed costs into non-taxable assets"
                        ],
                        "correct": "B",
                        "explanation": "Variance analysis enables management by exception: identifying significant discrepancies between planned and actual results so managers can eliminate waste and exploit profitable trends."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "summary_card",
                    "title": "Lesson 5 Summary & Key Takeaways",
                    "content": {
                        "bullet_points": [
                            "**Variance** is the quantitative difference between actual performance and the budgeted target ($Variance = Actual - Budget$).",
                            "**Income Variances:** Actual > Budget is **Favourable (F)**; Actual < Budget is **Unfavourable (U)**.",
                            "**Expense Variances:** Actual > Budget is **Unfavourable (U)**; Actual < Budget is **Favourable (F)**.",
                            "**Management by Exception:** Variance analysis allows leaders to focus attention on significant problem areas without wasting time on operations that went exactly to plan.",
                            "Variance findings feed directly into corrective actions: auditing suppliers, curbing wasteful expenditure, and updating subsequent forecasts."
                        ]
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Review, Accountability, and Appreciation of Budgeting
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Review, Accountability, and Appreciation of Budgeting",
        "unit_description": "The continuous budgetary control cycle, promoting financial discipline and awareness, accountability and transparency in public and private enterprises, and topic synthesis.",
        "lesson_title": "Review, Accountability, and Appreciation of Budgeting",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Artisans and Cooperative Enterprise Trading",
                    "content": {
                        "title": "Ethical Accountability and Financial Governance in Enterprise",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                        "caption": "Traders at the Maasai Market in Nairobi, demonstrating how transparent financial records, joint budgeting, and cooperative accountability build stakeholder trust.",
                        "author": "khym54",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the 4 stages of the continuous Budgetary Control Cycle\n- Analyze how budgeting fosters financial discipline and cost consciousness across staff\n- Explain the role of budgeting in promoting accountability and transparency in SACCOs, schools, and enterprises\n- Synthesize all core principles of Topic 3 (Budgeting in Business)"
                    }
                }
            ],
            # Card 2: Core Concept & Ethical Governance Principles
            [
                {
                    "type": "definition_card",
                    "title": "Budgetary Control and Financial Governance Defined",
                    "content": {
                        "term": "Budgetary Control",
                        "definition": "The comprehensive system of establishing departmental budgets, continually comparing actual achievements against planned limits, and taking corrective actions to secure business objectives."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Three Pillars of Ethical Budgetary Management",
                    "content": {
                        "text": "Budgeting transcends mathematical arithmetic; it is the cornerstone of ethical business stewardship:\n\n1. **Promoting Financial Discipline:** Clear spending caps prevent impulsive or wasteful expenditures by managers and employees.\n2. **Enhancing Financial Awareness:** Involving staff in budget preparation fosters a culture of cost-consciousness, ensuring everyone protects resources.\n3. **Ensuring Accountability & Transparency:** Clear budgets ensure that funds entrusted by SACCO members, school boards, or business partners are spent strictly as authorized, deterring fraud and mismanagement."
                    }
                }
            ],
            # Card 3: Vector SVG — The Continuous Budgetary Control Cycle
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Continuous Budgetary Control and Accountability Cycle",
                    "content": {
                        "title": "The Four-Stage Closed-Loop Governance Cycle",
                        "caption": "Vector diagram illustrating the 4 continuous stages of budgetary control: Plan & Forecast, Execute & Monitor, Compare & Analyze, and Correct & Revise.",
                        "svg_content": SVG_BUDGETARY_CONTROL_CYCLE
                    }
                }
            ],
            # Card 4: Comparative Matrix — The 4 Stages of Budgetary Control
            [
                {
                    "type": "comparison_table",
                    "title": "Four Stages of the Continuous Budgetary Control Cycle",
                    "content": {
                        "headers": ["Stage in Cycle", "Key Management Activities", "Primary Personnel Responsible", "Key Output / Document Generated", "Risk If Stage Is Omitted"],
                        "rows": [
                            ["Stage 1: Plan & Forecast", "Gather historical sales data, market trends, and departmental cost estimates to set realistic targets", "Department Heads, Budget Committee, Executive Directors", "Approved Master Budget & Departmental Budgets", "Enterprise operates blindly without financial goals"],
                            ["Stage 2: Execute & Monitor", "Implement daily operations; record all cash receipts and payments with receipts and invoices", "Accountants, Cashiers, Procurement Officers, Sales Team", "Cash Books, Payment Vouchers, Bank Statements", "Funds leak through unrecorded or unauthorized purchases"],
                            ["Stage 3: Compare & Analyze", "Compute mathematical variances ($Actual - Budget$) and classify as Favourable or Unfavourable", "Cost Accountants and Management Audit Team", "Comprehensive Monthly Variance Report", "Management remains ignorant of cost overruns and losses"],
                            ["Stage 4: Correct & Revise", "Investigate root causes of variances, eliminate inefficiencies, adjust operations, and update future budgets", "Executive Management, Department Supervisors", "Corrective Action Directives & Updated Forecasts", "Repeated mistakes drain working capital, causing insolvency"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation — Comprehensive Topic Synthesis
            [
                {
                    "type": "worked_example",
                    "title": "Step-by-Step Comprehensive Calculation: SACCO Micro-Enterprise Budget Audit",
                    "content": {
                        "intro": "The youth management committee of 'Ushindi Youth Boda SACCO' in Machakos audits their Q1 cash budget performance. Reconcile their financial accounts and evaluate budgetary compliance.",
                        "steps": [
                            "**Step 1: Given Q1 Cash Budget vs. Actual Data:**\n- Opening Cash on January 1st ($A$) = $\\text{KES } 50,000$\n- **Budgeted Receipts:** Member transport levies = $\\text{KES } 180,000$; Asset finance interest = $\\text{KES } 40,000$\n- **Actual Receipts:** Member levies collected = $\\text{KES } 195,000$; Interest collected = $\\text{KES } 38,000$\n- **Budgeted Payments:** Bike maintenance = $\\text{KES } 80,000$; Office rent = $\\text{KES } 30,000$; County permits = $\\text{KES } 20,000$\n- **Actual Payments:** Bike maintenance = $\\text{KES } 92,000$; Office rent = $\\text{KES } 30,000$; County permits = $\\text{KES } 18,000$",
                            "**Step 2: Calculate Total Actual Receipts and Payments:**\n$$\\text{Total Actual Receipts } (B) = 195,000 + 38,000 = \\text{KES } 233,000$$\n$$\\text{Total Actual Payments } (C) = 92,000 + 30,000 + 18,000 = \\text{KES } 140,000$$",
                            "**Step 3: Calculate Net Cash Flow and Closing Cash Balance:**\n$$\\text{Net Cash Flow } (D) = 233,000 - 140,000 = +\\text{KES } 93,000 \\text{ (Surplus)}$$\n$$\\text{Closing Cash Balance } (E) = 50,000 + 93,000 = \\text{KES } 143,000$$",
                            "**Step 4: Compute Key Line Variances ($Actual - Budget$):**\n- **Member Levies (Income):** $195,000 - 180,000 = +\\text{KES } 15,000\\text{ (F)}$\n- **Interest Income (Income):** $38,000 - 40,000 = -\\text{KES } 2,000\\text{ (U)}$\n- **Bike Maintenance (Expense):** $92,000 - 80,000 = +\\text{KES } 12,000\\text{ (U overspend)}$\n- **County Permits (Expense):** $18,000 - 20,000 = -\\text{KES } 2,000\\text{ (F savings)}$\n- **Office Rent (Expense):** $30,000 - 30,000 = \\text{Nil}$",
                            "**Step 5: Formulate Committee Governance Decisions:**\n- **Maintenance Overspend (KES 12,000 U):** The committee audits garage repair invoices and discovers substandard spare parts caused recurring breakdowns. They switch to an authorized dealer with warranty protection.\n- **Levy Collections (KES 15,000 F):** Higher compliance due to mobile money automation; committee approves keeping the digital payment gateway.",
                            "**Step 6: Economic Interpretation & Summary:**\n- **Strategic Outcome:** The SACCO expanded its cash reserves from $\\text{KES } 50,000$ to $\\text{KES } 143,000$, enabling the purchase of an additional motorcycle in Q2.\n- **Governance Value:** Transparent variance reporting builds member trust and prevents the embezzlement of communal funds."
                        ]
                    }
                }
            ],
            # Card 6: Real-World Case Study & Educational Video
            [
                {
                    "type": "real_world_example",
                    "title": "Real-World Commercial Application",
                    "content": {
                        "title": "Accountability and Governance in Kenyan SACCOs",
                        "text": "Over 14,000 registered SACCOs in Kenya manage billions of shillings in member savings. Under regulations enforced by the Sacco Societies Regulatory Authority (SASRA), every SACCO must prepare comprehensive annual operating and cash budgets, submit quarterly variance audits to supervisory committees, and present audited financial statements at Annual General Meetings (AGMs) to safeguard member deposits."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Budgetary Control and Financial Management in Business",
                    "content": {
                        "title": "The Role of Budgetary Control in Business Sustainability",
                        "youtube_id": "m1R5T6yP2kE",
                        "url": "https://www.youtube.com/watch?v=m1R5T6yP2kE",
                        "description": "Executive overview of budgetary control systems, highlighting corporate governance, continuous monitoring, and ethical accountability in financial management."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs (Topic 3 Final Assessment)
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Budgetary Control Cycle Sequence",
                    "content": {
                        "question": "Which of the following correctly outlines the sequential stages of the Budgetary Control Cycle?",
                        "options": [
                            "Execute $\\rightarrow$ Revise $\\rightarrow$ Plan $\\rightarrow$ Compare",
                            "Plan & Forecast $\\rightarrow$ Execute & Monitor $\\rightarrow$ Compare & Analyze $\\rightarrow$ Correct & Revise",
                            "Compare $\\rightarrow$ Plan $\\rightarrow$ Execute $\\rightarrow$ Liquidate",
                            "Record $\\rightarrow$ Tax Audit $\\rightarrow$ Close Account $\\rightarrow$ Plan"
                        ],
                        "correct": "B",
                        "explanation": "The continuous budgetary control cycle begins with planning and setting targets, executing operations, comparing actuals against budget (variance analysis), and implementing corrective revisions."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Ethical Role of Budgeting in Cooperatives",
                    "content": {
                        "question": "Why is strict budgeting essential for maintaining transparency in cooperative societies and school enterprises?",
                        "options": [
                            "It allows officials to spend funds on personal projects without receipts",
                            "It ensures that member or institutional funds are disbursed only for authorized, pre-approved purposes, preventing fraud and misappropriation",
                            "It automatically doubles member savings every three months",
                            "It replaces the need for keeping financial vouchers and receipts"
                        ],
                        "correct": "B",
                        "explanation": "Budgeting enforces ethical financial governance by ensuring expenditures remain strictly within authorized limits, protecting communal funds and maintaining stakeholder trust."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 3: Comprehensive Topic Synthesis",
                    "content": {
                        "question": "Which of the following statements correctly summarizes the golden rules of business budgeting?",
                        "options": [
                            "Cash budgets must include non-cash depreciation, ignore sales forecasts, and delete closing balances",
                            "Operating budgets start with sales forecasts, cash budgets track physical cash only, and variance analysis drives corrective control",
                            "Budgets are static legal documents that must never be updated once written",
                            "A cash deficit means the business has made an accounting profit"
                        ],
                        "correct": "B",
                        "explanation": "Effective business budgeting begins with the sales forecast, tracks actual physical liquidity in cash budgets (excluding non-cash items), and uses variance analysis to steer business performance."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Topic 3 Mastery Summary
            [
                {
                    "type": "summary_card",
                    "title": "Topic 3 Synthesis: The 5 Golden Rules of Business Budgeting",
                    "content": {
                        "bullet_points": [
                            "**Rule 1 — The Engine:** The **Sales Budget** is the foundation stone for all operating, production, and purchasing plans.",
                            "**Rule 2 — The Cash Rule:** A **Cash Budget** tracks only physical cash movements; non-cash items like depreciation are strictly excluded.",
                            "**Rule 3 — The Carry-Forward Link:** The Closing Cash Balance of one month is always the Opening Cash Balance of the subsequent month ($Closing_t = Opening_{t+1}$).",
                            "**Rule 4 — Variance Control:** Variances ($Actual - Budget$) are Favourable when they increase cash and Unfavourable when they reduce cash, guiding management action.",
                            "**Rule 5 — Continuous Governance:** The 4-stage **Budgetary Control Cycle** (Plan $\\rightarrow$ Execute $\\rightarrow$ Compare $\\rightarrow$ Revise) ensures financial discipline, solvency, and ethical transparency."
                        ]
                    }
                }
            ]
        ]
    }
]
