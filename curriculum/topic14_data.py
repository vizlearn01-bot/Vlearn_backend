"""
VLearn Form 4 Business Studies — Topic 14: Financial Statements
Authoritative Pedagogical Data Structures for 5 Lessons (50 Pages).
"""

from curriculum.ingest_form4_business_studies_topic14_svgs import (
    SVG_FINANCIAL_STATEMENTS_INFORMATION_FLOW,
    SVG_TRADING_ACCOUNT_FORMULA_TREE,
    SVG_PROFIT_AND_LOSS_STRUCTURE,
    SVG_CLASSIFIED_BALANCE_SHEET_TRIANGLE,
    SVG_YEAR_END_ADJUSTMENTS_MATRIX
)

# Verified Wikimedia photographic assets
IMG_FINANCIAL_AUDIT = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "text": "Financial statement analysis and corporate audit desk, illustrating financial report verification, balance sheet analysis, and spreadsheet calculations.",
    "author": "Dave Dugdale",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg"
}

IMG_RETAIL_TRADING_OPERATIONS = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Commercial trading enterprise logistics and retail operations, illustrating stock inventory valuation, gross profit determination, and working capital management.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

# ==============================================================================
# LESSON 1: PURPOSE AND COMPONENTS OF FINANCIAL STATEMENTS (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Purpose and Components of Financial Statements",
    "lesson_title": "Year-End Accounting Cycles, Statement Roles, and Stakeholder Analysis",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Financial Statements",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define final financial statements, explain their general purpose, identify their three primary components, explain the 12-month trading period concept, and detail why different stakeholders analyze financial statements."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Ultimate Financial Scorecard",
                    "content": {
                        "text": "If you run a business, cash in hand is not the same as profit! You could have cash from a recent loan but be losing money on every sale. To find out the true financial health of a business, we prepare structured year-end reports—our financial statements, the ultimate scorecard for any enterprise."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Three Primary Components of Financial Statements",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Financial Statements & 3 Components",
                    "content": {
                        "term": "Financial Statements",
                        "definition": "Structured reports prepared at the end of an accounting period to summarize a business's trading activities and financial standing. The 3 primary components are:\n1. Trading Account: Determines Gross Profit or Gross Loss from direct buying and selling.\n2. Profit and Loss (P&L) Account: Determines Net Profit or Net Loss after factoring in all operating expenses and non-trading incomes.\n3. Balance Sheet: Shows the financial position (assets, liabilities, capital) as at a specific date."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Accounting Information Flow Sequence",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Year-End Accounting Cycle",
                    "content": {
                        "text": "Financial statement figures flow in a strict sequence:\nTrial Balance ---> Trading Account (Gross Profit) ---> Profit & Loss Account (Net Profit) ---> Balance Sheet (Capital Section)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Accounting Information Flow Diagram",
                    "svg_content": SVG_FINANCIAL_STATEMENTS_INFORMATION_FLOW,
                    "content": {
                        "text": "Flowchart illustrating Trial Balance to Trading A/C to P&L A/C to Balance Sheet."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The Concept of the Trading Period",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The 12-Month Accounting Cycle",
                    "content": {
                        "text": "Financial statements are constructed at the end of a trading period (typically a 12-month duration like a calendar year or fiscal year). This 12-month cycle allows a business to capture seasonal fluctuations and compare its performance year-on-year."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Stakeholders and Their Decision Needs",
            "blocks": [
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Stakeholders & Financial Decision Needs",
                    "content": {
                        "headers": ["Stakeholder Group", "Primary Focus Area", "Specific Decision Requirement"],
                        "rows": [
                            ["Management", "Trading & P&L Statements", "Measure operational performance against plans and previous years"],
                            ["Financiers / Lenders", "Balance Sheet & Solvency", "Evaluate solvency, collateral security, and loan repayment ability"],
                            ["Shareholders / Owners", "P&L Net Profit & Capital", "Verify return on capital invested and dividend payout capacity"],
                            ["Government (KRA)", "Net Profit Calculation", "Assess official business income taxes levielable"],
                            ["Potential Investors", "P&L & Balance Sheet Ratios", "Determine whether shares represent a viable and profitable investment"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Corporate Audit Operations",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Corporate Financial Statement Audit Operations",
                    "content": IMG_FINANCIAL_AUDIT
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
                        "text": "The Trading Account shows direct buying/selling profit (Gross Profit). P&L shows true business profit after running costs (Net Profit). The Balance Sheet is a snapshot of assets, capital, and liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Cash vs. Profit Distinction",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Cash is NOT Profit",
                    "content": {
                        "text": "Cash in hand measures immediate liquidity. Profit measures wealth creation. A firm can be rich in cash from loan borrowings while suffering severe net trading losses!"
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
                    "title": "KRA Assessment Role",
                    "content": {
                        "text": "Why KRA requires P&L statements: Net Profit calculated in the Profit and Loss statement serves as the legal tax base for Corporate Income Tax assessment."
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
                        "question": "Which financial statement is prepared specifically to determine the gross profit or gross loss of a business?",
                        "options": [
                            "Profit and Loss Account",
                            "Trading Account",
                            "Balance Sheet",
                            "Cash Book"
                        ],
                        "correct_answer": "Trading Account",
                        "explanation": "The Trading Account calculates Gross Profit or Gross Loss by deducting Cost of Goods Sold from Net Sales."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: TRADING ACCOUNT AND GROSS PROFIT/LOSS (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Trading Account and Gross Profit/Loss",
    "lesson_title": "Direct Trading Calculations, Cost of Goods Sold, and Gross Profit Extraction",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Trading Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define sales, net sales, purchases, net purchases, and COGS, distinguish between carriage inwards and outwards, and construct a standard horizontal Trading Account."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Direct Trading Margins",
                    "content": {
                        "text": "If you buy mobile phones for 10,000 Shs and sell them for 12,000 Shs, your markup is 2,000 Shs. But if you paid 500 Shs transport to bring them to your shop, and customers returned 2 faulty units, your direct profit changes. The Trading Account organizes these items logically."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Core Components of the Trading Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Trading Account Component Definitions",
                    "content": {
                        "text": "• Gross Sales & Returns Inwards: Net Sales = Gross Sales - Returns Inwards.\n• Gross Purchases & Returns Outwards: Net Purchases = Gross Purchases - Returns Outwards.\n• Carriage Inwards: Transport on purchases $\\rightarrow$ ADDED to purchases (direct cost).\n• Carriage Outwards: Transport on sales $\\rightarrow$ DO NOT INCLUDE in Trading Account! (It is a P&L expense).\n• Opening Stock & Closing Stock: Stock at start and unsold stock at end."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Core Trading Account Formulas",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Core Trading Formulas",
                    "content": {
                        "text": "1. Net Sales = Gross Sales - Returns Inwards\n2. Net Purchases = Gross Purchases - Returns Outwards + Carriage Inwards\n3. Cost of Goods Available for Sale (COGAS) = Opening Stock + Net Purchases\n4. Cost of Goods Sold (COGS) = COGAS - Closing Stock\n5. Gross Profit = Net Sales - Cost of Goods Sold"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Trading Account Formula Tree Diagram",
                    "svg_content": SVG_TRADING_ACCOUNT_FORMULA_TREE,
                    "content": {
                        "text": "Formula tree illustrating Net Sales, Net Purchases, COGS, and Gross Profit."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Mrs Moyo Simplified Trading Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mrs Moyo Simplified Trading Trace",
                    "content": {
                        "text": "Opening Stock = 500 Shs; Purchases = 2,000 Shs; Sales = 2,800 Shs; Closing Stock = 0 Shs.\n• COGAS = 500 + 2,000 = Sh. 2,500.\n• COGS = 2,500 - 0 = Sh. 2,500.\n• Gross Profit = Net Sales (2,800) - COGS (2,500) = Sh. 300."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Karanja Traders Worked Trading Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Karanja Traders Full Trading Account Walkthrough",
                    "content": {
                        "text": "Information: Opening Stock 20k, Purchases 270k, Sales 300k, Returns Inwards 15k, Closing Stock 50k, Carriage Inwards 10k.\n\nSteps:\n1. Net Sales = 300,000 - 15,000 = Sh. 285,000.\n2. Net Purchases = 270,000 + 10,000 = Sh. 280,000.\n3. COGAS = 20,000 + 280,000 = Sh. 300,000.\n4. COGS = 300,000 - 50,000 = Sh. 250,000.\n5. Gross Profit = 285,000 - 250,000 = Sh. 35,000."
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Karanja Traders Trading Account (Year Ended 31st December 2003)",
                    "content": {
                        "headers": ["Debit Side (Costs / Stock)", "Shs.", "Credit Side (Sales / Revenue)", "Shs."],
                        "rows": [
                            ["Opening Stock", "20,000", "Gross Sales Revenue", "300,000"],
                            ["Add: Purchases (270,000)", "270,000", "Less: Returns Inwards (Sales Returns)", "(15,000)"],
                            ["Add: Carriage Inwards", "10,000", "Net Sales Revenue", "285,000"],
                            ["Cost of Goods Available for Sale", "300,000", "-", "-"],
                            ["Less: Closing Stock (Inventory)", "(50,000)", "-", "-"],
                            ["Cost of Goods Sold (COGS)", "250,000", "-", "-"],
                            ["GROSS PROFIT c/d", "35,000", "-", "-"],
                            ["TOTALS", "285,000 Shs", "TOTALS", "285,000 Shs"]
                        ]
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Commercial Trading Operations & Stock Management",
                    "content": IMG_RETAIL_TRADING_OPERATIONS
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Worked Example: Missing Closing Stock Calculation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Worked Example: Determining Missing Closing Stock",
                    "content": {
                        "text": "Problem: Opening Stock 10k, Purchases 50k, Sales 58k, Gross Profit 10k. Find Closing Stock.\n\nSolution:\n1. COGS = Sales (58k) - Gross Profit (10k) = Sh. 48,000.\n2. COGS = Opening Stock (10k) + Purchases (50k) - Closing Stock.\n3. 48,000 = 60,000 - Closing Stock ---> Closing Stock = 60,000 - 48,000 = Sh. 12,000."
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
                        "text": "Carriage Inwards is added to Purchases in the Trading Account. Carriage Outwards is an operating expense placed in the Profit and Loss Account."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Returns Subtraction Sides",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Returns Subtraction Rules",
                    "content": {
                        "text": "Returns Inwards (sales returns) are subtracted from Sales on the credit side. Returns Outwards (purchase returns) are subtracted from Purchases on the debit side."
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
                    "title": "COGAS vs COGS Distinction",
                    "content": {
                        "text": "COGAS is total stock available for sale (Opening + Net Purchases). COGS is stock actually sold (COGAS minus unsold Closing Stock)."
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
                        "question": "How is Carriage Inwards treated when constructing a Trading Account?",
                        "options": [
                            "Debited to the Profit and Loss Account as an operating expense",
                            "Added to Purchases in the Trading Account",
                            "Subtracted from Gross Sales on the Credit side",
                            "Deducted from Closing Stock"
                        ],
                        "correct_answer": "Added to Purchases in the Trading Account",
                        "explanation": "Carriage Inwards is a direct transport cost incurred to bring purchased goods into the business, so it is added to Purchases in the Trading Account."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: PROFIT AND LOSS ACCOUNT AND NET PROFIT/LOSS (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Profit and Loss Account and Net Profit/Loss",
    "lesson_title": "Indirect Operating Expenses, Non-Trading Incomes, and Net Earnings",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Profit and Loss Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to distinguish between gross profit and net profit, classify indirect expenses and non-trading revenues, and construct a standard Profit and Loss Account."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Exposing Operational Realities",
                    "content": {
                        "text": "Gross profit only tells you if you make money on physical stock. But if shop rent is huge, electricity is soaring, and advertising cost is massive, a business with Sh. 50,000 Gross Profit can die of a Sh. 10,000 Net Loss! P&L exposes these operational realities."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Net Profit Equation and Item Classification",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "P&L Equation & Classification",
                    "content": {
                        "text": "Net Profit = (Gross Profit + Other Incomes) - Total Operating Expenses\n• Credit Side (Revenues): Gross Profit b/d, Discounts Received, Commission Received, Rent Received.\n• Debit Side (Expenses): Administrative (postage, telephone, insurance, rent), Selling (advertising, carriage outwards), Financial (discounts allowed, bank charges)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Profit and Loss Account Structure Diagram",
                    "svg_content": SVG_PROFIT_AND_LOSS_STRUCTURE,
                    "content": {
                        "text": "Component diagram contrasting Credit Incomes with Debit Operating Expenses."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Karanja Traders Continuation (Net Profit Tracing)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Karanja Traders Net Profit Tracing",
                    "content": {
                        "text": "Gross Profit b/d = 35k. Advertising 5k, Telephone 2k, Insurance 3k, Discount Allowed 1k, Commission Received 4k.\n• Total Revenue = Gross Profit (35k) + Commission Received (4k) = Sh. 39,000.\n• Total Expenses = 5k + 2k + 3k + 1k = Sh. 11,000.\n• Net Profit = 39,000 - 11,000 = Sh. 28,000."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Gathioro's Mobile Phones Worked P&L Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Gathioro's Mobile Phones P&L Walkthrough",
                    "content": {
                        "text": "Gross Profit 209k. Telephone 6.4k, Insurance 8.2k, Postage 3.85k, Rent 19.6k, Advertising 12.9k, Discount Allowed 7.3k, Discount Received 4k.\n\nSteps:\n1. Total Revenues = 209,000 + 4,000 = Sh. 213,000.\n2. Total Operating Expenses = 6,400 + 8,200 + 3,850 + 19,600 + 12,900 + 7,300 = Sh. 58,250.\n3. Net Profit = 213,000 - 58,250 = Sh. 154,750 (transferred to Capital)."
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Gathioro's Mobile Phones Profit & Loss Account (Year Ended 31st October 2013)",
                    "content": {
                        "headers": ["Debit Side (Operating Expenses)", "Shs.", "Credit Side (Revenues & Incomes)", "Shs."],
                        "rows": [
                            ["Telephone Expense", "6,400", "Gross Profit b/d (from Trading A/C)", "209,000"],
                            ["Insurance Expense", "8,200", "Discount Received (from creditors)", "4,000"],
                            ["Postage Expense", "3,850", "-", "-"],
                            ["Rent Expense", "19,600", "-", "-"],
                            ["Advertising Expense", "12,900", "-", "-"],
                            ["Discount Allowed Expense", "7,300", "-", "-"],
                            ["NET PROFIT (Transferred to Capital)", "154,750", "-", "-"],
                            ["TOTALS", "213,000 Shs", "TOTALS", "213,000 Shs"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Gross Profit considers direct inventory cost. Net Profit considers all operating running costs of the enterprise."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Watch Out: Discount Allowed vs. Discount Received Placement",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Discount Placements in P&L",
                    "content": {
                        "text": "Discount Allowed is an expense (Debit side). Discount Received is a non-trading income (Credit side)."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Check Your Understanding 1",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Carriage Outwards P&L Placement",
                    "content": {
                        "text": "Carriage Outwards is a selling and distribution expense, placed on the Debit side of the Profit and Loss Account."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Check Your Understanding 2",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "knowledge_check",
                    "title": "Formative Assessment",
                    "content": {
                        "question": "Which of the following items is credited to the Profit and Loss Account as an operating revenue?",
                        "options": [
                            "Carriage Outwards",
                            "Discounts Allowed to Debtors",
                            "Commission Received",
                            "Insurance Premiums Paid"
                        ],
                        "correct_answer": "Commission Received",
                        "explanation": "Commission Received is a non-trading income credited to the Profit and Loss Account."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Lesson 3 Review",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Lesson 3 Summary",
                    "content": {
                        "text": "P&L Account adds non-trading revenues to Gross Profit and subtracts all operating expenses to arrive at Net Profit."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Summary Checklist",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Checklist",
                    "content": {
                        "text": "Verified P&L equation, expense classifications, and Net Profit transfer to Balance Sheet Capital."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: BALANCE SHEET FROM FINAL ACCOUNTS (10 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Balance Sheet from Final Accounts",
    "lesson_title": "Classified Asset-Liability Layouts, Capital Equations, and Liquidity Ratios",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Classified Balance Sheet",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to classify balance sheet items into fixed assets, current assets, capital, long-term liabilities, and current liabilities, construct a classified Balance Sheet, and calculate Working Capital and Capital Employed."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Financial Position Snapshot",
                    "content": {
                        "text": "Trading and P&L accounts tell you if you made money over the past year. The Balance Sheet shows where that money went—whether locked in machinery or cash at bank—and details your debts to evaluate financial safety."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Asset, Capital, and Liability Classifications",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Classified Balance Sheet Categories",
                    "content": {
                        "text": "• Fixed Assets: Long-term operational properties (Premises, Motor Vehicles, Furniture).\n• Current Assets: Short-term liquid assets (Closing Stock, Debtors, Bank, Cash, Prepayments).\n• Capital Equation: Closing Capital = Initial Capital + Net Profit - Drawings.\n• Long-Term Liabilities: External debts > 1 year (Bank Loans).\n• Current Liabilities: Debts due < 1 year (Trade Creditors, Overdrafts, Accrued Expenses)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Classified Balance Sheet Pyramid Diagram",
                    "svg_content": SVG_CLASSIFIED_BALANCE_SHEET_TRIANGLE,
                    "content": {
                        "text": "Structural diagram categorizing Fixed Assets, Current Assets, Working Capital, Capital Employed, and Liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Core Financial Ratios: Working Capital & Capital Employed",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Core Financial Metrics",
                    "content": {
                        "text": "1. Working Capital = Current Assets - Current Liabilities (Short-term liquidity measure).\n2. Capital Employed = Fixed Assets + Working Capital (OR Closing Capital + Long-Term Liabilities).\n3. Borrowed Capital = Long-Term Liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Solvency vs. Insolvency Defined",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Solvency & Insolvency",
                    "content": {
                        "term": "Solvency",
                        "definition": "Solvent: A business is solvent when Total Assets exceed Liabilities (Assets > Liabilities). Insolvent: A business is insolvent when Liabilities exceed Total Assets, resulting in negative capital (deficiency) and bankruptcy risk."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Jumbo Traders Ratio Worked Analysis",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Jumbo Traders Financial Metric Tracing",
                    "content": {
                        "text": "Data: FA (Land 50k + Plant 20k + Vehicles 30k = 100k); CA (Stock 10k + Debtors 6k + Bank 10k + Cash 2k = 28k); CL (Creditors 7k + Rent owing 1k = 8k); LTL (Loans 30k); Closing Capital 90k.\n• Working Capital = 28,000 - 8,000 = Sh. 20,000.\n• Capital Employed = 100,000 + 20,000 = Sh. 120,000 (Check: 90,000 + 30,000 = Sh. 120,000).\n• Borrowed Capital = Sh. 30,000."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Gathioro's Mobile Phones Classified Balance Sheet",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Gathioro's Mobile Phones Balance Sheet Walkthrough",
                    "content": {
                        "text": "Assets: Fixed Assets (Vehicles 480k + Furniture 190k = 670k); Current Assets (Stock 60k + Debtors 63k + Cash 65k = 188k) ---> Total Assets = Sh. 858,000.\nCapital & Liabilities: Opening Capital 626,250 + Net Profit 154,750 - Drawings 88,000 = Closing Capital Sh. 693,000. Current Liabilities (Creditors 165k) ---> Total Cap & Liab = Sh. 858,000 [BALANCED!]"
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Gathioro's Mobile Phones Balance Sheet (As at 31st October 2013)",
                    "content": {
                        "headers": ["Classification / Item Details", "Sub-Amount (Shs.)", "Total Amount (Shs.)"],
                        "rows": [
                            ["Fixed Assets: Motor Vehicles", "480,000", "-"],
                            ["Fixed Assets: Furniture", "190,000", "-"],
                            ["Total Fixed Assets", "-", "670,000"],
                            ["Current Assets: Closing Stock (Inventory)", "60,000", "-"],
                            ["Current Assets: Debtors", "63,000", "-"],
                            ["Current Assets: Cash in Hand", "65,000", "-"],
                            ["Total Current Assets", "-", "188,000"],
                            ["TOTAL ASSETS", "-", "858,000 Shs"],
                            ["Capital: Opening Capital", "626,250", "-"],
                            ["Add: Net Profit (from P&L A/C)", "154,750", "-"],
                            ["Less: Owner Drawings", "(88,000)", "-"],
                            ["Net Closing Capital", "-", "693,000"],
                            ["Current Liabilities: Trade Creditors", "-", "165,000"],
                            ["TOTAL CAPITAL & LIABILITIES", "-", "858,000 Shs"]
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
                        "text": "Working Capital (Current Assets - Current Liabilities) is the short-term operational lifeblood of a business."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Drawings Subtraction",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Drawings Treatment",
                    "content": {
                        "text": "Drawings are always subtracted from capital in the equity section; they are NEVER classified as a liability."
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
                    "title": "Working Capital Purpose",
                    "content": {
                        "text": "Why Working Capital is critical: Without positive working capital, even a highly profitable business can fail because it cannot meet immediate short-term supplier debts."
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
                        "question": "How is Working Capital calculated on a classified Balance Sheet?",
                        "options": [
                            "Fixed Assets minus Current Assets",
                            "Current Assets minus Current Liabilities",
                            "Closing Capital plus Long-Term Liabilities",
                            "Total Assets minus Drawings"
                        ],
                        "correct_answer": "Current Assets minus Current Liabilities",
                        "explanation": "Working Capital represents short-term liquidity, calculated as Current Assets minus Current Liabilities."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 5: ADJUSTMENTS AND EXAMINATION APPLICATION (10 Pages)
# ==============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Adjustments and Examination Application",
    "lesson_title": "Year-End Accruals, Prepayments, Nyaituya Walkthrough, and KCSE Essays",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Year-End Accounting Adjustments",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain accruals and prepayments, apply adjustments to Trading and P&L accounts, present adjusted items in the Balance Sheet, and construct complete year-end final accounts under KCSE conditions."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Matching Principle",
                    "content": {
                        "text": "If you pay rent for 15 months in advance, should you record the full 15-month cost as this year's expense? No! The matching concept mandates that we only record expenses and incomes that relate to the current 12-month period."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Accruals vs. Prepayments Decision Matrix",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Accruals & Prepayments Dual Effects",
                    "content": {
                        "text": "• Accrued Expense (Owing): P&L ADD (+); Balance Sheet Current Liability.\n• Accrued Income (Due): P&L ADD (+); Balance Sheet Current Asset.\n• Prepaid Expense (Advance): P&L DEDUCT (-); Balance Sheet Current Asset.\n• Prepaid Income (Advance): P&L DEDUCT (-); Balance Sheet Current Liability."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Year-End Adjustments Decision Matrix",
                    "svg_content": SVG_YEAR_END_ADJUSTMENTS_MATRIX,
                    "content": {
                        "text": "Matrix mapping Accrued Expenses (+, CL), Accrued Incomes (+, CA), Prepaid Expenses (-, CA), and Prepaid Incomes (-, CL)."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Nyaituya Comprehensive 5-Adjustment Walkthrough (Trading A/C)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Nyaituya Trading Account Extraction",
                    "content": {
                        "text": "Trading Data: Sales 720k, Returns Inwards 20k $\\rightarrow$ Net Sales Sh. 700,000. Purchases 340k, Returns Outwards 18k $\\rightarrow$ Net Purchases Sh. 322,000. Opening Stock 60k, Closing Stock 52k.\n• COGS = 60,000 + 322,000 - 52,000 = Sh. 330,000.\n• Gross Profit = 700,000 - 330,000 = Sh. 370,000."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Nyaituya Comprehensive Walkthrough (P&L A/C)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Nyaituya P&L Account Adjustments & Net Profit",
                    "content": {
                        "text": "Adjusted Expenses & Incomes:\n• Rent = 16,000 + 6,000 (accrued) = Sh. 22,000.\n• Commission Received = 9,000 + 5,000 (due) = Sh. 14,000.\n• Insurance = 30,000 - 4,000 (prepaid) = Sh. 26,000.\n• Salaries owing = Sh. 21,000 | Advertising = Sh. 24,000.\n• Total Revenues = 370,000 + 14,000 = Sh. 384,000.\n• Total Expenses = 22k + 24k + 26k + 21k = Sh. 93,000.\n• Net Profit = 384,000 - 93,000 = Sh. 291,000."
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Nyaituya Trading, Profit & Loss Account (Year Ended 31st December 2005)",
                    "content": {
                        "headers": ["Debit Side (Expenses & Costs)", "Shs.", "Credit Side (Revenues & Incomes)", "Shs."],
                        "rows": [
                            ["Opening Stock", "60,000", "Gross Sales Revenue", "720,000"],
                            ["Add: Purchases (340,000 - 18,000)", "322,000", "Less: Returns Inwards", "(20,000)"],
                            ["Cost of Goods Available for Sale", "382,000", "Net Sales Revenue", "700,000"],
                            ["Less: Closing Stock (Inventory)", "(52,000)", "-", "-"],
                            ["Cost of Goods Sold (COGS)", "330,000", "-", "-"],
                            ["GROSS PROFIT c/d", "370,000", "-", "-"],
                            ["Trading Subtotals", "700,000 Shs", "Trading Subtotals", "700,000 Shs"],
                            ["Rent Expense (16,000 + 6,000 accrued)", "22,000", "Gross Profit b/d", "370,000"],
                            ["Advertising Expense", "24,000", "Commission (9,000 + 5,000 due)", "14,000"],
                            ["Insurance (30,000 - 4,000 prepaid)", "26,000", "-", "-"],
                            ["Salaries Owing (accrued expense)", "21,000", "-", "-"],
                            ["NET PROFIT (Transferred to Capital)", "291,000", "-", "-"],
                            ["P&L TOTALS", "384,000 Shs", "P&L TOTALS", "384,000 Shs"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Nyaituya Comprehensive Walkthrough (Balance Sheet)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Nyaituya Classified Balance Sheet & Ratio Analysis",
                    "content": {
                        "text": "Balance Sheet:\n• Fixed Assets: Furniture (100k) + Premises (400k) = Sh. 500,000.\n• Current Assets: Stock (52k) + Debtors (54k) + Cash (15k) + Prepaid Insurance (4k) + Commission due (5k) = Sh. 130,000 ---> Total Assets = Sh. 630,000.\n• Net Closing Capital: Opening Cap (288k) + Net Profit (291k) - Drawings (40k) = Sh. 539,000.\n• Current Liabilities: Creditors (64k) + Rent accrued (6k) + Salaries owing (21k) = Sh. 91,000 ---> Total Cap & Liab = Sh. 630,000 [BALANCED!]\n• Working Capital = 130,000 - 91,000 = Sh. 39,000."
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Nyaituya Classified Balance Sheet (As at 31st December 2005)",
                    "content": {
                        "headers": ["Classification / Account Details", "Sub-Amount (Shs.)", "Total Amount (Shs.)"],
                        "rows": [
                            ["Fixed Assets: Furniture & Fittings", "100,000", "-"],
                            ["Fixed Assets: Premises", "400,000", "-"],
                            ["Total Fixed Assets", "-", "500,000"],
                            ["Current Assets: Closing Stock", "52,000", "-"],
                            ["Current Assets: Debtors", "54,000", "-"],
                            ["Current Assets: Cash in Hand", "15,000", "-"],
                            ["Current Assets: Prepaid Insurance", "4,000", "-"],
                            ["Current Assets: Commission Due (Accrued Income)", "5,000", "-"],
                            ["Total Current Assets", "-", "130,000"],
                            ["TOTAL ASSETS", "-", "630,000 Shs"],
                            ["Capital: Opening Capital", "288,000", "-"],
                            ["Add: Net Profit (from P&L A/C)", "291,000", "-"],
                            ["Less: Owner Drawings", "(40,000)", "-"],
                            ["Net Closing Capital", "-", "539,000"],
                            ["Current Liabilities: Trade Creditors", "64,000", "-"],
                            ["Current Liabilities: Rent Accrued", "6,000", "-"],
                            ["Current Liabilities: Salaries Owing", "21,000", "-"],
                            ["Total Current Liabilities", "-", "91,000"],
                            ["TOTAL CAPITAL & LIABILITIES", "-", "630,000 Shs"]
                        ]
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Corporate Audit & Balance Sheet Verification",
                    "content": IMG_FINANCIAL_AUDIT
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Multi-Step Mutua Traders Ratio Practice",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mutua Traders Financial Ratio Calculations",
                    "content": {
                        "text": "Data: FA 450k, Closing Stock 35k, Debtors 25k, Cash 15k, Creditors 20k, Rent owing 5k, 3-yr Loan 100k, Capital 400k.\n• Current Assets = 35k + 25k + 15k = Sh. 75,000.\n• Current Liabilities = 20k + 5k = Sh. 25,000.\n• Working Capital = 75,000 - 25,000 = Sh. 50,000.\n• Capital Employed = FA (450k) + WC (50k) = Sh. 500,000."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "KCSE Integrated Practice: Paper 2 Model Essays (Financier Balance Sheet)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Model Essay: Financier Balance Sheet Requirements",
                    "content": {
                        "text": "Question: Explain five reasons why a potential financier requires a Balance Sheet before granting a long-term loan (10 Marks).\n\nModel Answer:\n1. Assess Solvency Position: Verifies if total assets exceed external liabilities (low default risk).\n2. Evaluate Working Capital / Liquidity: Checks if liquid assets cover immediate operating costs and interest.\n3. Examine Fixed Asset Collateral: Identifies machinery/premises available as security for the loan.\n4. Determine Capital Gearing: Compares owner's equity with long-term bank loans to detect debt over-reliance.\n5. Identify Existing Creditor Claims: Assesses competing creditor claims on business assets."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "KCSE Integrated Practice: Paper 2 (Trading vs. P&L Account)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Model Essay: Trading A/C vs. P&L A/C Differences",
                    "content": {
                        "text": "Question: Differentiate between a Trading Account and a Profit and Loss Account under four distinct headings (8 Marks).\n\nModel Answer:\n• Purpose: Trading A/C calculates Gross Profit/Loss from direct trading; P&L A/C calculates Net Profit/Loss of entire business.\n• Inputs: Trading A/C includes stock, purchases, carriage inwards, sales; P&L A/C includes operating expenses and non-trading incomes.\n• Sequence: Trading A/C prepared first; P&L A/C prepared second starting with Gross Profit b/d.\n• Running Costs: Trading A/C excludes general running costs; P&L A/C includes administrative, selling, and financial costs."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Key Idea & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Key Idea",
                    "content": {
                        "text": "Accrued expenses/incomes are added in P&L. Prepaid expenses/incomes are deducted. Accrued expenses and prepaid incomes are Current Liabilities; prepaid expenses and accrued incomes are Current Assets."
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
                        "question": "How is an expense paid in advance (prepaid expense) treated in the Profit & Loss Account and Balance Sheet?",
                        "options": [
                            "Added to P&L expense and classified as Current Liability",
                            "Deducted from P&L expense and classified as Current Asset",
                            "Added to P&L expense and classified as Fixed Asset",
                            "Deducted from P&L expense and classified as Current Liability"
                        ],
                        "correct_answer": "Deducted from P&L expense and classified as Current Asset",
                        "explanation": "Prepaid expenses are deducted from P&L because they belong to next period, and listed as Current Assets in the Balance Sheet."
                    }
                }
            ]
        }
    ]
}

TOPIC14_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA,
    LESSON_5_DATA
]
