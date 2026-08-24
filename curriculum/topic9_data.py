"""
VLearn Form 4 Business Studies — Topic 9: Determining the Net Worth of a Business
Authoritative Pedagogical Data Structures for 3 Lessons (30 Pages).
"""

from curriculum.ingest_form4_business_studies_topic9_svgs import (
    SVG_ASSETS_VS_LIABILITIES_CLASSIFICATION,
    SVG_BOOKKEEPING_EQUATION_BALANCE_SCALE,
    SVG_BALANCE_SHEET_HORIZONTAL_T_LAYOUT,
    SVG_SOLVENCY_VS_INSOLVENCY_COMPARISON,
    SVG_STAKEHOLDERS_BALANCE_SHEET_USES
)

# Verified Wikimedia photographic assets
IMG_JUA_KALI_FABRICATOR = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "A Jua Kali artisan fabricating metalwork in Nairobi's informal manufacturing sector, illustrating owner capital investment and machinery fixed assets.",
    "author": "Harold Odhiambo Otieno",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

IMG_ANALYZING_FINANCIAL_DATA = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "text": "A person analysing financial data and spreadsheets, working through balance sheet calculations and balance equations.",
    "author": "Dave Dugdale",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg"
}

IMG_ACCOUNTANT_DESK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg",
    "text": "An accounting office with organised workstations, showing the formal environment for balance sheet preparation and solvency assessment.",
    "author": "Kristin Dos Santos",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:The_Accountants_desks_(3817577217).jpg"
}

# ==============================================================================
# LESSON 1: BUSINESS RECORDS AND ACCOUNTING TERMS (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Business Records and Accounting Terms",
    "lesson_title": "Asset Taxonomy, Liability Obligations, and Owner's Equity Foundations",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Bookkeeping and Accounting",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Jua Kali Business Assets",
                    "content": IMG_JUA_KALI_FABRICATOR
                },
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "goals": [
                            "Explain the meaning of bookkeeping and transactions",
                            "Define and classify debtors, creditors, and goods",
                            "Classify assets into fixed and current",
                            "Classify liabilities into long-term and current",
                            "Define capital"
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Financial Records Matter",
                    "content": {
                        "text": "If you open a retail shop in your local market town, you cannot rely on memory to track who owes you money, who you owe money to, or how much stock is worth. Bookkeeping provides a systematic, chronological record of monetary transactions so you can make informed decisions, prove your business value to banks, and plan growth."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Core Accounting Definitions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Core Accounting Definitions",
                    "content": {
                        "term": "Bookkeeping & Transactions",
                        "definition": "Bookkeeping is the systematic, chronological recording of business transactions in a set of books. Business Transactions are dealings between two or more parties involving monetary value."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Goods, Debtors, and Creditors",
                    "content": {
                        "text": "-Goods: Items bought specifically for resale to earn profit (e.g. supermarket bread).\n-Debtor: A person/firm who received value on credit and owes money to the business (classified as Current Asset).\n-Creditor: A person/firm to whom the business owes money for goods/services bought on credit (classified as Current Liability)."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Classification of Assets",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition & Characteristics of Assets",
                    "content": {
                        "term": "Assets",
                        "definition": "Property of all kinds owned and controlled by an individual or business, to which a reliable monetary value can be attached."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Fixed vs. Current Assets",
                    "content": {
                        "text": "-Fixed Assets: Durable resources expected to last more than one year, not intended for resale (Premises, Motor Vehicles, Furniture & Fittings, Machinery & Plant).\n-Current Assets: Temporary resources expected to be converted into cash or used up within one year (Cash in Hand, Cash at Bank, Stock of Goods, Debtors, Prepaid Expenses)."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Retail Business Operating Assets",
                    "content": IMG_JUA_KALI_FABRICATOR
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Classification of Liabilities",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition & Characteristics of Liabilities",
                    "content": {
                        "term": "Liabilities",
                        "definition": "Borrowed money and items bought on credit representing debts or legal obligations owed by the business to outsiders."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Long-Term vs. Current Liabilities",
                    "content": {
                        "text": "-Long-Term Liabilities: Debts not expected to be settled within one year (5-Year Bank Loans, Mortgages).\n-Current Liabilities: Debts payable within one year (Creditors, Bank Overdraft, Accrued Expenses / Unpaid Bills)."
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Assets vs. Liabilities Comparison Table",
                    "content": {
                        "headers": ["Accounting Category", "Definition", "Time Duration / Lifespan", "Balance Sheet Side", "Examples"],
                        "rows": [
                            ["Fixed Assets", "Durable resources owned for operations", "Long-term (More than 1 year)", "Left Side (Assets)", "Premises, Motor Vehicles, Machinery"],
                            ["Current Assets", "Liquid resources converted to cash", "Short-term (Less than 1 year)", "Left Side (Assets)", "Cash, Bank, Stock, Debtors"],
                            ["Long-Term Liabilities", "External debts owed to outsiders", "Long-term (More than 1 year)", "Right Side (Liabilities)", "5-Year Bank Loan, Mortgages"],
                            ["Current Liabilities", "Short-term debts payable to outsiders", "Short-term (Less than 1 year)", "Right Side (Liabilities)", "Trade Creditors, Bank Overdraft"]
                        ]
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Assets vs Liabilities Classification Matrix",
                    "svg_content": SVG_ASSETS_VS_LIABILITIES_CLASSIFICATION,
                    "content": {
                        "text": "Classification diagram organizing fixed/current assets and long-term/current liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Capital (Owner's Equity)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Capital",
                    "content": {
                        "term": "Capital",
                        "definition": "The money, goods, or assets provided by the owner to start and run the business, representing the owner's financial claim on assets after subtracting external liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Mama Mboga Small Business Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Local Vendor Asset-Liability Scenario",
                    "content": {
                        "text": "A local mama mboga has Sh. 3,000 cash (Current Asset), Sh. 2,000 kale/tomato stock (Current Asset), a Sh. 1,500 wooden stand (Fixed Asset), and owes a wholesale supplier Sh. 1,000 for credit tomatoes (Current Liability). Her total assets are Sh. 6,500, liabilities are Sh. 1,000, and her net Capital stake is Sh. 5,500."
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
                        "text": "Assets are what the business owns. Liabilities are what the business owes to outsiders. Capital is what the business owes back to the owner."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Debtors vs Creditors Memory Trick",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "memory_tip",
                    "title": "Watch Out: Debtors vs Creditors",
                    "content": {
                        "text": "-Debtors start with D ---> think Debit / Collect (Asset). They owe us money.\n-Creditors start with C ---> think Credit / Pay (Liability). We owe them money.\n-Prepaid Expenses: Paying next year's insurance in advance is a Current Asset because the insurer owes us a service!"
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
                    "title": "Asset Characteristics Check",
                    "content": {
                        "text": "Four essential characteristics of an Asset: 1. Owned/controlled by the business 2. Acquired from a past event 3. Reliable monetary value 4. Classified as fixed or current."
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
                        "question": "Which of the following items is correctly classified as a Current Asset?",
                        "options": [
                            "Premises and Buildings",
                            "Stock of Goods for Resale",
                            "5-Year Development Bank Loan",
                            "Trade Creditors"
                        ],
                        "correct_answer": "Stock of Goods for Resale",
                        "explanation": "Stock of goods is expected to be converted into cash within a short period (less than one year), making it a Current Asset."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: THE BOOKKEEPING EQUATION AND QUANTITATIVE CALCULATIONS (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "The Bookkeeping Equation and Quantitative Calculations",
    "lesson_title": "Algebraic Balance Equations, Variable Transpositions, and Multi-Asset Math",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Bookkeeping Equation",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Analyzing Balance Equations",
                    "content": IMG_ANALYZING_FINANCIAL_DATA
                },
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "goals": [
                            "State and derive the Bookkeeping Equation (Accounting Equation)",
                            "Manipulate it algebraically to solve for Assets (A), Capital (C), or Liabilities (L)",
                            "Address source typographical inconsistencies"
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Balanced Law of Accounting",
                    "content": {
                        "text": "Bookkeeping operates on a balanced law of nature: everything the business owns (Assets) was financed either by the owner's investment (Capital) or by borrowing from outsiders (Liabilities). Thus, the two sides of the accounting equation must always balance!"
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The Accounting Equation & Transpositions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Accounting Equation Formulations",
                    "content": {
                        "text": "-Core Equation: Assets = Capital + Liabilities  (A = C + L)\n-Capital Formula: Capital = Assets - Liabilities  (C = A - L)\n-Liabilities Formula: Liabilities = Assets - Capital  (L = A - C)"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Bookkeeping Equation Balance Scale",
                    "svg_content": SVG_BOOKKEEPING_EQUATION_BALANCE_SCALE,
                    "content": {
                        "text": "Physical balance scale diagram visualizing Assets = Capital + Liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Source Typo Corrections & Syllabus Fidelity",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "common_mistake",
                    "title": "Source Typo Warnings",
                    "content": {
                        "text": "1. Formula Typo Warning: On printed source page 325, text incorrectly prints 'Assets = Capital - liabilities'. This is an algebraic typo! The correct starting formula is Assets = Capital + Liabilities (Capital = Assets - Liabilities).\n2. Arithmetic Typo Warning: For Business A where Assets = 620,000 and Liabilities = 230,000, source text prints '390,900'. The true mathematical value is Sh. 390,000!"
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Worked Math: Solving Businesses A, B, and C",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "3-Business Missing Variable Calculation",
                    "content": {
                        "intro": "Problem: Find missing variables W, X, and Y:\nBusiness A: Assets = 620,000; Liabilities = 230,000. Find Capital (W).\nBusiness B: Capital = 400,000; Liabilities = 120,000. Find Assets (X).\nBusiness C: Assets = 800,000; Capital = 500,000. Find Liabilities (Y).",
                        "steps": [
                            "Step 1 (Business A): W = A - L = 620,000 - 230,000 = Sh. 390,000.",
                            "Step 2 (Business B): X = C + L = 400,000 + 120,000 = Sh. 520,000.",
                            "Step 3 (Business C): Y = A - C = 800,000 - 500,000 = Sh. 300,000.",
                            "Step 4: Check balance: Business A: 390k + 230k = 620k [OK]; Business B: 520k - 120k = 400k [OK]; Business C: 500k + 300k = 800k [OK]."
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Math: Gichuru Traders Capital",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Gichuru Traders Capital Calculation",
                    "content": {
                        "intro": "Problem: Gichuru Traders has Fixed Assets of Sh. 450,000, Current Assets of Sh. 120,000, and owes Creditors Sh. 80,000. Calculate Capital.",
                        "steps": [
                            "Step 1: Total Assets = Fixed Assets + Current Assets = 450,000 + 120,000 = Sh. 570,000.",
                            "Step 2: Capital = Total Assets - Liabilities = 570,000 - 80,000 = Sh. 490,000."
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Math: Multi-Item Retail Shop Breakdown",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "9-Item Retail Shop Capital & Net Worth Calculation",
                    "content": {
                        "intro": "Problem: Extracted items: Premises 1.2M, Vehicles 800k, Stock 150k, Debtors 90k, Bank 210k, Cash 40k, 5-Yr Loan 600k, Creditors 120k, Accrued Electricity 10k.\nCalculate: a) Fixed Assets b) Current Assets c) Long-Term Liabilities d) Short-Term Liabilities e) Capital",
                        "steps": [
                            "a) Fixed Assets = 1.2M + 800k = Sh. 2,000,000",
                            "b) Current Assets = 150k + 90k + 210k + 40k = Sh. 490,000\n   Total Assets = 2M + 490k = Sh. 2,490,000",
                            "c) Long-Term Liabilities = 5-Yr Loan = Sh. 600,000",
                            "d) Short-Term Liabilities = 120k + 10k = Sh. 130,000\n   Total Liabilities = 600k + 130k = Sh. 730,000",
                            "e) Capital = Total Assets - Total Liabilities = 2,490,000 - 730,000 = Sh. 1,760,000."
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
                        "text": "Every shilling of business assets has a source: either the owner (Capital) or a lender (Liabilities). Thus, A = C + L is always in perfect mathematical balance."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Single Change Rebalancing",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "common_mistake",
                    "title": "Watch Out: Dual Transaction Impact",
                    "content": {
                        "text": "Any single transaction impacts at least two accounts! If an owner invests cash into the business, Cash (Asset) increases and Capital increases. If the business buys stock for cash, Stock (Asset) increases while Cash (Asset) decreases, leaving total assets unchanged."
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
                    "title": "Zero Liability Business Capital",
                    "content": {
                        "text": "If a business has zero external liabilities, its Capital is exactly equal to its Total Assets (C = A - 0 = A). All resources are 100% owned by the entrepreneur."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "If a business purchases motor vehicles worth Sh. 500,000 using cash from its bank account, what is the effect on its Total Assets?",
                        "options": [
                            "Total Assets increase by Sh. 500,000",
                            "Total Assets remain unchanged (Motor Vehicles increase while Bank decreases by Sh. 500,000)",
                            "Total Assets decrease by Sh. 500,000",
                            "Capital increases by Sh. 500,000"
                        ],
                        "correct_answer": "Total Assets remain unchanged (Motor Vehicles increase while Bank decreases by Sh. 500,000)",
                        "explanation": "Exchanging one asset (cash at bank) for another asset (motor vehicles) leaves the total value of assets completely unchanged."
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
                        "question": "A business has Total Assets worth Sh. 950,000 and Total Liabilities of Sh. 340,000. What is its Capital (Net Worth)?",
                        "options": [
                            "Sh. 1,290,000",
                            "Sh. 610,000",
                            "Sh. 340,000",
                            "Sh. 950,000"
                        ],
                        "correct_answer": "Sh. 610,000",
                        "explanation": "Capital = Total Assets - Total Liabilities = 950,000 - 340,000 = Sh. 610,000."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: THE BALANCE SHEET, SOLVENCY AND NET WORTH (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "The Balance Sheet, Solvency and Net Worth",
    "lesson_title": "Financial Snapshot Statements, Solvency Analysis, and Net Worth Determination",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Balance Sheet",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Formal Balance Sheet Preparation",
                    "content": IMG_ACCOUNTANT_DESK
                },
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "goals": [
                            "Define a Balance Sheet and its heading rules",
                            "Prepare a structured Balance Sheet",
                            "Distinguish between solvency and insolvency",
                            "Define Net Worth",
                            "List uses for five stakeholders"
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Financial X-Ray of a Business",
                    "content": {
                        "text": "A doctor uses an X-ray to see inside a patient's body. Similarly, bank managers, tax authorities, and investors use a Balance Sheet as a financial X-ray to determine if a business is healthy, buried under debt, or facing insolvency."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Structure and Rules of a Balance Sheet",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Balance Sheet Structural Rules",
                    "content": {
                        "text": "1. Three-Part Heading: Name of business, statement name ('Balance Sheet'), and date ('As at [Date]'). We write 'As at' because it is a snapshot of one specific calendar day.\n2. Classification Order: Assets listed as Fixed then Current (in order of liquidity: Stock -> Debtors -> Bank -> Cash). Capital & Liabilities listed as Capital, Long-Term Liabilities, then Current Liabilities.\n3. Perfect Balance: Total Assets MUST equal Total Capital & Liabilities."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Horizontal T-Account Balance Sheet Layout",
                    "svg_content": SVG_BALANCE_SHEET_HORIZONTAL_T_LAYOUT,
                    "content": {
                        "text": "Layout diagram showing 3-part heading, Assets on left, Capital & Liabilities on right, and equal totals."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Solvency vs. Insolvency Analysis",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Solvency & Insolvency Definitions",
                    "content": {
                        "text": "-Solvency: A business is solvent when Total Assets > External Liabilities (positive Net Worth / Capital).\n-Insolvency: A business is insolvent when External Liabilities > Total Assets (resulting in negative Capital / Capital Deficiency). Selling all assets is insufficient to pay off debts."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Solvency vs Insolvency Comparative Analysis",
                    "svg_content": SVG_SOLVENCY_VS_INSOLVENCY_COMPARISON,
                    "content": {
                        "text": "Comparative diagram contrasting solvent positive net worth with insolvent capital deficiency."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Five Stakeholder Uses of a Balance Sheet",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Uses of Financial Statements",
                    "content": {
                        "text": "1. Lenders / Banks: Assess collateral security and debt repayment ability.\n2. Owners / Shareholders: Verify Net Worth growth and return on equity.\n3. Tax Authorities (KRA): Verify profit tax compliance and asset valuations.\n4. Potential Investors: Evaluate financial risk before purchasing shares.\n5. Management: Diagnostic tool to compare performance trends across periods."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Five Stakeholder Uses of a Balance Sheet",
                    "svg_content": SVG_STAKEHOLDERS_BALANCE_SHEET_USES,
                    "content": {
                        "text": "Mind map diagram illustrating balance sheet uses for lenders, owners, investors, tax authorities, and managers."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Balance Sheet 1: Wasco Traders",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Wasco Traders Balance Sheet as at 30th Oct 1995",
                    "content": {
                        "intro": "Problem: Extract: Cash 20,520; Bank 160,230; Premises 800,000; Debtors 40,000; Creditors 62,500; 2-Yr Loan 40,000; Stock 2,500.",
                        "steps": [
                            "Left Side (Assets):\nFixed: Premises = 800,000\nCurrent: Stock (2,500) + Debtors (40,000) + Bank (160,230) + Cash (20,520) = 223,250\nTotal Assets = Sh. 1,023,250",
                            "Right Side (Capital & Liabilities):\nTotal Liabilities = 40,000 + 62,500 = 102,500\nCapital (Net Worth) = 1,023,250 - 102,500 = Sh. 920,750\nTotal Capital & Liabilities = 920,750 + 40,000 + 62,500 = Sh. 1,023,250 [BALANCED!]"
                        ]
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Commercial Banking Credit Assessment",
                    "content": IMG_ACCOUNTANT_DESK
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Balance Sheet 2: Mile Traders (Net Profit Addition)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mile Traders Balance Sheet (Net Profit Included)",
                    "content": {
                        "intro": "Problem: Stock 100k, Capital 800k, Debtors 50k, Creditors 80k, Cash 10k, Net Profit 10k, Overdraft 70k, Machines 600k, Furniture 200k.",
                        "steps": [
                            "Left Side (Assets): Machines (600k) + Furniture (200k) + Stock (100k) + Debtors (50k) + Cash (10k) = Sh. 960,000.",
                            "Right Side (Capital & Liabilities): Adjusted Capital = Capital (800k) + Net Profit (10k) = 810k. Liabilities = Creditors (80k) + Overdraft (70k) = 150k. Total = 810k + 150k = Sh. 960,000 [BALANCED!]"
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
                        "text": "A Balance Sheet is a financial snapshot showing what a firm owns (Assets) minus what it owes outsiders (Liabilities) to reveal its Net Worth (Capital)."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: 'As at' Heading Rule",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "common_mistake",
                    "title": "Watch Out: Heading Terminology",
                    "content": {
                        "text": "Never write 'Balance Sheet for the year ended...'! A Balance Sheet changes with every single transaction. It is true ONLY on a specific calendar day, so the heading MUST read 'Balance Sheet as at [Date]'."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Integrated Practice: Paper 1",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "key_takeaway",
                    "title": "KCSE Paper 1 Short-Answer Mastery",
                    "content": {
                        "text": "1. Accounting Equation: Assets = Capital + Liabilities (A = C + L).\n2. Net Worth Formula: Net Worth = Total Assets - External Liabilities.\n3. Solvency Condition: Total Assets > Total External Liabilities.\n4. Three Heading Rules: Business name, statement title ('Balance Sheet'), and date ('As at [Date]')."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Integrated Practice: Paper 2 (Uses & Differences Essays)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Essay Model Answer: Five Uses of a Balance Sheet",
                    "content": {
                        "text": "Question: Discuss five uses of a Balance Sheet to various financial users (10 Marks).\n\nModel Answer:\n1. Lenders & Banks: Assess collateral security and verify debt repayment capability.\n2. Owners & Shareholders: Track Net Worth growth and evaluate return on capital.\n3. Potential Investors: Analyze financial risk before purchasing company shares.\n4. Management: Diagnostic tool to compare asset/debt ratios across accounting periods.\n5. Tax Authorities (KRA): Verify profit tax filings and asset valuation compliance."
                    }
                }
            ]
        }
    ]
}

TOPIC9_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA
]
