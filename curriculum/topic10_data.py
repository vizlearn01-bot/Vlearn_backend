"""
VLearn Form 4 Business Studies — Topic 10: Business Transactions
Authoritative Pedagogical Data Structures for 3 Lessons (30 Pages).
"""

from curriculum.ingest_form4_business_studies_topic10_svgs import (
    SVG_CASH_VS_CREDIT_TRANSACTIONS,
    SVG_BALANCE_SHEET_ADJUSTMENT_RULES,
    SVG_BIGFOOT_CASE_TRANSACTION_FLOW,
    SVG_CAPITAL_FLOW_PIPELINE,
    SVG_TRANSACTION_EFFECTS_BALANCE_SCALE
)

# Verified Wikimedia photographic assets
IMG_WANGIGE_MARKET = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Wangige local market in Kiambu County — a typical Kenyan retail market where cash and credit transactions take place daily.",
    "author": "Kristinabudiati",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_ANALYZING_FINANCIAL_DATA = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "text": "A person analysing financial data and tracking the effects of business transactions on the balance sheet equations.",
    "author": "Dave Dugdale",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg"
}

IMG_JUA_KALI_POTS = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
    "text": "Jua Kali-made aluminium cooking pots ready for sale — representing business inventory and owner's capital investment.",
    "author": "Leonard Kisuu",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_cooking_pots.jpg"
}

# ==============================================================================
# LESSON 1: MEANING AND CLASSIFICATION OF BUSINESS TRANSACTIONS (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Meaning and Classification of Business Transactions",
    "lesson_title": "Immediate Settlement, Deferred Credit, and Payment Medium Taxonomy",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Business Transactions",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Cash Transactions at the Market",
                    "content": IMG_WANGIGE_MARKET
                },
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "goals": [
                            "Define what a business transaction is",
                            "Distinguish clearly between cash and credit transactions",
                            "Identify accepted payment mediums",
                            "Spot textbook typographical duplication"
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Lifeblood of Commercial Enterprises",
                    "content": {
                        "text": "Every single day, businesses engage in thousands of activities—buying stock, selling products, paying bills, and collecting money from customers. To ensure a business knows whether it is making profit or running out of cash, every single dealing must be systematically recorded. Classifying these transactions is the first step in accounting!"
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition of a Business Transaction",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of a Business Transaction",
                    "content": {
                        "term": "Business Transaction",
                        "definition": "Any dealing between two or more individuals or parties that can be assigned a monetary value. Non-monetary events (such as hiring a skilled manager or employee politeness) are NOT business transactions and cannot be recorded in accounts."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Cash Transactions and Mediums of Exchange",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Characteristics of Cash Transactions",
                    "content": {
                        "text": "- Definition: An exchange where both parts of the deal are executed and settled immediately.\n- Accepted Mediums: Payment does not have to be in physical notes/coins! It can be made using physical cash, cheques drawn on bank accounts, money orders, postal orders, mobile money transfers (M-Pesa), or bank drafts."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Immediate Retail Cash Transactions",
                    "content": IMG_WANGIGE_MARKET
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Credit Transactions (Deferred Payment)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Characteristics of Credit Transactions",
                    "content": {
                        "text": "- Definition: An exchange where goods or services are bought or sold now, but payment is deferred to an agreed future date.\n- Alternative Term: Also referred to as deferred payment transactions.\n- Impact: Creates Debtors (for credit sales) or Creditors (for credit purchases)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Cash vs Credit Transactions Comparison Matrix",
                    "svg_content": SVG_CASH_VS_CREDIT_TRANSACTIONS,
                    "content": {
                        "text": "Matrix comparing cash and credit transactions across timing, payment mediums, and ledger impacts."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Cash vs. Credit Feature Comparison Table",
            "blocks": [
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Cash vs. Credit Transactions Comparison",
                    "content": {
                        "headers": ["Dimension", "Cash Transaction", "Credit Transaction"],
                        "rows": [
                            ["Payment Timing", "Executed immediately at point of deal", "Deferred to an agreed future date"],
                            ["Ledger Impact", "No debtor or creditor created", "Creates Debtors (sales) or Creditors (purchases)"],
                            ["Mediums Accepted", "Physical cash, cheque, M-Pesa, bank draft", "Credit invoice, debit/credit notes, promise to pay"],
                            ["Example", "Buying stock for cash Sh. 80,000", "Buying stock on 30-day credit Sh. 90,000"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Local Kiosk Transaction Scenarios",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Local Market Scenarios",
                    "content": {
                        "text": "- Scenario A: Mama Mboga buys a crate of tomatoes for Sh. 2,000 and pays cash immediately ---> Cash Transaction.\n- Scenario B: A customer takes sugar worth Sh. 300 and promises to pay at month end ---> Credit Transaction (deferred payment).\n- Scenario C: Mama Mboga pays her supplier Sh. 10,000 by cheque immediately on delivery ---> Cash Transaction (settlement is immediate via bank)."
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
                        "text": "A business transaction must have a monetary value. Cash transactions are settled immediately (via cash, cheque, or mobile transfer). Credit transactions involve deferred payment settled in the future."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Cheque Misconception & Source Typo",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "common_mistake",
                    "title": "Watch Out: Cheque Misconception",
                    "content": {
                        "text": "1. Cheque Misconception: Paying by cheque is NOT a credit transaction! In accounting, bank balances are liquid cash resources. A cheque settles the deal immediately, making it a Cash Transaction.\n2. Source Typo Alert: Printed curriculum notes sometimes duplicate credit transaction text under 'Cash transactions'. Always recognize deferred payment as Credit!"
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
                    "title": "Monetary Value Test",
                    "content": {
                        "text": "Why hiring a top manager is NOT a transaction: Although hiring a skilled manager benefits the firm, no direct monetary exchange occurred at the contract signing moment. It cannot be recorded in books of accounts."
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
                        "question": "A business buys stock of goods worth Sh. 50,000 and pays the supplier immediately by cheque. How is this transaction classified?",
                        "options": [
                            "Credit Transaction",
                            "Cash Transaction",
                            "Capital Investment",
                            "Deferred Payment"
                        ],
                        "correct_answer": "Cash Transaction",
                        "explanation": "Payment by cheque settles the obligation immediately from the business bank account, making it a Cash Transaction."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: EFFECTS OF TRANSACTIONS ON THE BALANCE SHEET (THE BIGFOOT CASE) (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Effects of Transactions on the Balance Sheet",
    "lesson_title": "Balance Sheet Equilibrium, Asset Swaps, and Dual Expansion Mechanics",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Balance Sheet Adjustments",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Tracking Balance Sheet Adjustments",
                    "content": IMG_ANALYZING_FINANCIAL_DATA
                },
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "goals": [
                            "Explain how transactions alter balance sheet items",
                            "Describe the 3 rules governing balance sheet adjustments",
                            "Trace transactions step-by-step to construct a final balanced Balance Sheet"
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Balance Sheet Scale",
                    "content": {
                        "text": "The balance sheet is like a scale. When a transaction occurs, it alters assets, liabilities, or capital. To preserve A = C + L, either something on the same side must offset it (Asset Swap), or an equal change must happen on the opposite side (Dual Expansion/Contraction)."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Three Rules of Balance Sheet Adjustments",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Rules Governing Transaction Adjustments",
                    "content": {
                        "text": "1. Asset Swap: Increase in one asset = decrease in another asset (Totals unchanged).\n2. Liability/Capital Swap: Increase in one liability = decrease in another liability (Totals unchanged).\n3. Dual Expansion / Contraction: Asset side and Liability/Capital side change in the SAME direction (Totals expand or contract equally)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Three Rules of Balance Sheet Adjustments Flowchart",
                    "svg_content": SVG_BALANCE_SHEET_ADJUSTMENT_RULES,
                    "content": {
                        "text": "Flowchart diagram illustrating asset swaps, liability swaps, and dual expansion/contraction."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Bigfoot Communications Case Study Baseline",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Bigfoot Communications Baseline Position (31st Dec 2005)",
                    "content": {
                        "text": "Baseline Position as at 31st Dec 2005:\nFixed Assets: Buildings 1M, Motor Vans 1.5M, Furniture 200k = Total Fixed Assets 2.7M.\nCurrent Assets: Stock 300k, Debtors 100k, Cash in Bank 700k, Cash in Hand 500k = Total Current Assets 1.6M.\nTotal Assets = Sh. 4,300,000.\nCapital & Liabilities: Capital 3.35M, Bank Loan 800k, Creditors 150k = Total Cap & Liab = Sh. 4,300,000."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Tracing Transactions (a) through (d)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Transactions (a) to (d) Breakdown",
                    "content": {
                        "text": "- Trans (a) [2 Jan]: Bought stock for cash 80k ---> Asset Swap (Stock +80k, Cash -80k to 420k). Totals = 4.3M.\n- Trans (b) [3 Jan]: Cash to Bank transfer 100k ---> Asset Swap (Bank +100k to 800k, Cash -100k to 320k). Totals = 4.3M.\n- Trans (c) [5 Jan]: Paid creditors 50k by cheque ---> Dual Contraction (Bank -50k to 750k, Creditors -50k to 100k). Totals = 4.25M.\n- Trans (d) [8 Jan]: Bought stock on credit 90k ---> Dual Expansion (Stock +90k to 470k, Creditors +90k to 190k). Totals = 4.34M."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Tracing Transactions (e) through (g)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Transactions (e) to (g) Breakdown",
                    "content": {
                        "text": "- Trans (e) [12 Jan]: Sold stock on credit at cost 150k ---> Asset Swap (Stock -150k to 320k, Debtors +150k to 250k). Totals = 4.34M.\n- Trans (f) [16 Jan]: KIE Loan 500k to repay bank loan ---> Liability Swap (KIE Loan +500k, Bank Loan -500k to 300k). Totals = 4.34M.\n- Trans (g) [20 Jan]: Received cash from debtor 100k ---> Asset Swap (Cash +100k to 420k, Debtors -100k to 150k). Totals = 4.34M."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Bigfoot Communications 7-Step Transaction Flow",
                    "svg_content": SVG_BIGFOOT_CASE_TRANSACTION_FLOW,
                    "content": {
                        "text": "Flowchart tracing all 7 Bigfoot transactions and their balance sheet impact."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Bigfoot Final Balance Sheet Construction",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Bigfoot Final Balance Sheet as at 20th January 2006",
                    "content": {
                        "text": "Left Side (Assets):\nFixed Assets: Buildings (1M) + Vans (1.5M) + Furniture (200k) = 2.7M.\nCurrent Assets: Stock (320k) + Debtors (150k) + Bank (750k) + Cash (420k) = 1.64M.\nTotal Assets = Sh. 4,340,000.\n\nRight Side (Capital & Liabilities):\nCapital = 3.35M.\nLong-Term Liabilities: Bank Loan (300k) + KIE Loan (500k) = 800k.\nCurrent Liabilities: Creditors = 190k.\nTotal Capital & Liabilities = 3.35M + 800k + 190k = Sh. 4,340,000 [BALANCED!]"
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
                        "text": "Every transaction alters balance sheet items while preserving accounting equilibrium. Asset swaps and liability swaps keep totals unchanged; dual expansions and contractions expand or shrink totals equally."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Dual Expansion Equilibrium",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "common_mistake",
                    "title": "Watch Out: Dual Expansion",
                    "content": {
                        "text": "Buying stock on credit increases Stock (Asset) and increases Creditors (Liability). Do not confuse this with an asset swap! Both sides expand equally, keeping A = C + L perfectly level."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Dual Expansion vs Dual Contraction Scale",
                    "svg_content": SVG_TRANSACTION_EFFECTS_BALANCE_SCALE,
                    "content": {
                        "text": "Scale diagram illustrating dual expansion and dual contraction balance shifts."
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
                    "title": "Makara Traders Scenario",
                    "content": {
                        "text": "Makara Traders deposits Sh. 120,000 personal money into a new bank account ---> Dual Expansion! Capital increases by 120,000 and Bank (Asset) increases by 120,000."
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
                        "question": "Which of the following transactions represents a Dual Contraction on the balance sheet?",
                        "options": [
                            "Buying office furniture for cash Sh. 20,000",
                            "Paying trade creditors Sh. 50,000 by cheque",
                            "Buying stock on 30-day credit Sh. 90,000",
                            "Transferring cash from hand to bank"
                        ],
                        "correct_answer": "Paying trade creditors Sh. 50,000 by cheque",
                        "explanation": "Paying creditors by cheque reduces Bank (Asset) and reduces Creditors (Liability) simultaneously, representing a Dual Contraction."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: CHANGES IN CAPITAL AND DETERMINING CAPITAL EQUATIONS (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Changes in Capital and Determining Capital Equations",
    "lesson_title": "Owner's Equity Dynamics, Capital Pipeline Tracking, and Algebraic Solvers",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Capital Changes",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Capital and Inventory",
                    "content": IMG_JUA_KALI_POTS
                },
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "goals": [
                            "Explain the four causes of capital changes",
                            "State and manipulate the capital tracking equation",
                            "Calculate initial capital, final capital, drawings, investments, or profits",
                            "Master KCSE essay answers"
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Tracking Owner's Net Worth Over Time",
                    "content": {
                        "text": "When an entrepreneur invests money into a business, capital does not remain static. It expands when the business earns net profits or when the owner introduces personal assets, and contracts when the owner takes out drawings or when trading losses occur."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Four Causes of Capital Changes",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Four Economic Causes of Capital Alteration",
                    "content": {
                        "text": "1. Drawings (D): Cash or goods taken by the owner for private/personal use ---> Reduces Capital.\n2. Additional Investment (I): Personal assets introduced into the business by the owner ---> Increases Capital.\n3. Net Profit (P): Revenue exceeds costs in a trading period ---> Increases Capital.\n4. Net Loss (L): Costs exceed revenue in a trading period ---> Reduces Capital."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Owner Equity & Investment Expansion",
                    "content": IMG_JUA_KALI_POTS
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Capital Tracking Equation & Transpositions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Capital Tracking Formula & Transpositions",
                    "content": {
                        "text": "- Core Formula: Final Capital (CC) = Initial Capital (OC) + Net Profit (P) + Additional Investment (I) - Drawings (D)\n- Solve for Profit (P): P = CC - OC - I + D\n- Solve for Drawings (D): D = OC + P + I - CC\n- Solve for Initial Capital (OC): OC = CC - P - I + D\n- Solve for Additional Investment (I): I = CC - OC - P + D"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Capital Expansion & Contraction Pipeline",
                    "svg_content": SVG_CAPITAL_FLOW_PIPELINE,
                    "content": {
                        "text": "Pipeline diagram showing how initial capital expands via profits/investments and contracts via drawings."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Worked Math: Mali Traders Final Capital",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mali Traders Final Capital Calculation",
                    "content": {
                        "text": "Problem: Initial Capital (OC) = 250,000; Investment (I) = 68,000; Drawings (D) = 92,000; Net Profit (P) = 180,000. Calculate Final Capital (CC).\n\nSolution:\nCC = OC + I + P - D\nCC = 250,000 + 68,000 + 180,000 - 92,000\nCC = 498,000 - 92,000 = Sh. 406,000."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Math: Finding Initial Capital",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Trader Initial Capital Solution",
                    "content": {
                        "text": "Problem: Final Capital (CC) = 580,000; Drawings (D) = 75,000; Personal PC Investment (I) = 45,000; Net Profit (P) = 120,000. Calculate Initial Capital (OC).\n\nSolution:\nOC = CC - P - I + D\nOC = 580,000 - 120,000 - 45,000 + 75,000\nOC = 415,000 + 75,000 = Sh. 490,000."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Math: Detecting Profit vs. Loss",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Profit vs Loss Detection Scenario",
                    "content": {
                        "text": "Problem: OC = 300,000; CC = 240,000; D = 80,000; I = 10,000. Determine if profit or loss occurred and find value.\n\nSolution:\nP = CC - OC - I + D\nP = 240,000 - 300,000 - 10,000 + 80,000\nP = -70,000 + 80,000 = +10,000.\nSince result is positive, the firm earned a Net Profit of Sh. 10,000!"
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
                        "text": "Profits and additional investments expand owner's capital. Drawings and losses contract owner's capital. All five variables are linked by CC = OC + P + I - D."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Personal Computer Investment",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "common_mistake",
                    "title": "Watch Out: Non-Cash Investments",
                    "content": {
                        "text": "Additional investments do not have to be cash! Bringing a personal car, computer, or building into the business is an Additional Investment (I) that increases capital at fair market value."
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
                    "title": "KCSE Paper 1 Ledger Effects Table",
                    "content": {
                        "text": "1. Furniture by cheque: Furniture A/C Debit (Asset +), Bank A/C Credit (Asset -) ---> Asset Swap.\n2. Wages in cash: Wages Expense Debit (Capital -), Cash Credit (Asset -) ---> Contraction.\n3. Stock on credit: Purchases Debit (Asset +), Creditors Credit (Liability +) ---> Dual Expansion.\n4. Private drawings: Drawings Debit (Capital -), Cash Credit (Asset -) ---> Dual Contraction."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Integrated Practice: Paper 2 (Balance Sheet Effects Essay)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Essay Model Answer: Effects of Transactions on Balance Sheet Totals",
                    "content": {
                        "text": "Question: Discuss the effects of various business transactions on balance sheet totals, explaining conditions under which totals expand, contract, or remain unchanged (10 Marks).\n\nModel Answer:\n1. No Change in Totals (Swaps): Occurs when a transaction alters items within one side of the balance sheet. Asset Swap (buying furniture for cash) or Liability Swap (refinancing a bank loan with a KIE loan).\n2. Expansion of Totals (Dual Expansion): Occurs when an asset and a liability/capital increase simultaneously. E.g., buying stock on credit or owner introducing a personal car as capital.\n3. Contraction of Totals (Dual Contraction): Occurs when an asset and a liability/capital decrease simultaneously. E.g., paying creditors by cheque or owner withdrawing cash for personal use."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "An entrepreneur has Initial Capital of Sh. 450,000, makes Drawings of Sh. 60,000, introduces a personal computer worth Sh. 35,000, and reports a Net Profit of Sh. 115,000. What is the Final Capital?",
                        "options": [
                            "Sh. 600,000",
                            "Sh. 540,000",
                            "Sh. 450,000",
                            "Sh. 510,000"
                        ],
                        "correct_answer": "Sh. 540,000",
                        "explanation": "Final Capital = Initial Capital (450k) + Investment (35k) + Profit (115k) - Drawings (60k) = 600k - 60k = Sh. 540,000."
                    }
                }
            ]
        }
    ]
}

TOPIC10_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA
]
