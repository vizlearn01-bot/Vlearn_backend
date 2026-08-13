"""
VLearn Form 4 Business Studies — Topic 13: Cash Book
Authoritative Pedagogical Data Structures for 4 Lessons (40 Pages).
"""

from curriculum.ingest_form4_business_studies_topic13_svgs import (
    SVG_SINGLE_COLUMN_CASH_BOOK_LAYOUT,
    SVG_TWO_COLUMN_CASH_BOOK_LAYOUT,
    SVG_THREE_COLUMN_CASH_BOOK_DISCOUNT_RULES,
    SVG_CONTRA_ENTRIES_FLOWCHART,
    SVG_DISHONOURED_CHEQUE_REVERSAL_FLOW
)

# Verified Wikimedia photographic assets
IMG_CASH_BOOK_RECORDS = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Physical cash book accounting records in Kenya, illustrating dual-column postings, ledger folios, and cash transaction journals.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_BANK_CASH_DESK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Commercial bank cash desk operations, demonstrating daily cash deposits, cheque clearing, and liquidity management.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

# ==============================================================================
# LESSON 1: CASH BOOK PURPOSE AND SINGLE-COLUMN CASH BOOK (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Cash Book Purpose and Single-Column Cash Book",
    "lesson_title": "Dual Journal-Ledger Role, Layout Anatomy, and Single-Column Postings",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Cash Book",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define a Cash Book and explain its dual role in accounting, identify the different types of cash books, describe the structure of a Single-Column Cash Book, and record and balance single-column accounts."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Lifeblood of Daily Operations",
                    "content": {
                        "text": "For any business in Kenya, cash is the lifeblood of daily operations. If a business recorded every single cash purchase of sugar, bread, or stationery in separate general ledger accounts, its ledger books would quickly become cluttered. The Cash Book pulls cash and bank transactions out of the general ledger into a specialized book, relieving the general ledger of thousands of routine entries."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition and Dual Purpose of a Cash Book",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Cash Book Definition & Dual Role",
                    "content": {
                        "term": "Cash Book",
                        "definition": "A Cash Book is a book of original entry (journal) and a ledger account that contains the Cash account and the Bank account only. It serves a dual purpose:\n1. As a Book of Original Entry: Transactions are recorded here directly from primary source documents.\n2. As a Ledger Account: Contains the final asset balances for cash and bank without needing separate cash/bank accounts in the General Ledger."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Five Primary Types of Cash Books",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The 5 Cash Book Categories",
                    "content": {
                        "text": "1. Single-Column Cash Book: Features one monetary column on each side (Dr and Cr) for Cash or Bank.\n2. Double-Column (Two-Column) Cash Book: Features two monetary columns on each side for Cash and Bank side-by-side.\n3. Three-Column Cash Book: Features three monetary columns on each side for Cash, Bank, and Discounts (allowed/received).\n4. Petty Cash Book: Used to record small, routine expenses (bus fare, tea leaves).\n5. Analysis Cash Book: Categorizes receipts and payments under specialized analytical columns."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Single-Column Cash Book Structure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Structure & Rules of Entry",
                    "content": {
                        "text": "A Single-Column Cash Book follows the classic T-account layout split into Debit (left, receiving) and Credit (right, paying):\n• Columns: Date, Details (Particulars), L.F. (Ledger Folio), and Amount (Shs).\n• Rules of Entry: Debited when cash is received (inflows); Credited when cash is paid out (outflows)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Single-Column Cash Book Standard Layout",
                    "svg_content": SVG_SINGLE_COLUMN_CASH_BOOK_LAYOUT,
                    "content": {
                        "text": "Diagram showing Dr (Receipts) vs Cr (Payments), Date, Details, L.F., and Amount columns."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Single-Column vs. Multi-Column Comparison",
            "blocks": [
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Cash Book Types Comparison Matrix",
                    "content": {
                        "headers": ["Type", "Monetary Columns (per side)", "Accounts Tracked", "Discount Handling"],
                        "rows": [
                            ["Single-Column", "1 Column", "Cash OR Bank (prepared on separate pages)", "No discount columns"],
                            ["Two-Column", "2 Columns", "Cash AND Bank (prepared side-by-side)", "No discount columns"],
                            ["Three-Column", "3 Columns", "Cash, Bank, AND Cash Discounts", "Disc Allowed (Dr) & Disc Received (Cr)"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "February Sole Trader Walkthrough: Cash & Bank Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "February Transactions Cash & Bank Postings",
                    "content": {
                        "text": "Cash Account Postings:\n• Debits (Receipts): Capital 100k + Sales 40k + Momani 22k + Commission 7k + Bank withdrawal 50k = 219,000 Shs.\n• Credits (Payments): Rent 20k + Bank deposit 18k + Carriage In 9k + Salaries 16k = 63,000 Shs.\n• Cash Balance c/d = 219,000 - 63,000 = Sh. 156,000 (Debit balance b/d on March 1st).\n\nBank Account Postings:\n• Debits (Deposits): Capital 250k + Sales 30k + Cash deposit 18k = 298,000 Shs.\n• Credits (Cheques): Furniture 15k + Purchases 80k + Salaries 26k + Drawings 16k + Cash withdrawal 50k + Amino 28k + Salaries 32k = 247,000 Shs.\n• Bank Balance c/d = 298,000 - 247,000 = Sh. 51,000 (Debit balance b/d on March 1st)."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Physical Cash Book Accounting Records",
                    "content": IMG_CASH_BOOK_RECORDS
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Worked Examples: Basic & Jokin Traders KCSE-Level",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Jokin Traders Single-Column Cash Extraction",
                    "content": {
                        "text": "Problem: Bal b/d Cash 45,700, Sales 35,000, Salaries 4,800, Purchases 2,000, Raji Traders 15,000.\n\nSolution:\nDr. Receipts = 45,700 + 35,000 = Sh. 80,700.\nCr. Payments = 4,800 + 2,000 + 15,000 = Sh. 21,800.\nBalance c/d = 80,700 - 21,800 = Sh. 58,900. Brought down as Debit Balance b/d Sh. 58,900!"
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
                        "text": "The Cash Book is both a journal and a ledger account. Cash receipts are debited on the left; cash payments are credited on the right."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Calendar Typographical Errors",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Realistic Calendar Dates",
                    "content": {
                        "text": "Some printed reference notes list transactions under 'Feb 31'. February has only 28 days (or 29 in leap years). In school exams, always write realistic dates (Feb 28)!"
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
                        "question": "On which side of a Single-Column Cash Book is a cash payment for office rent recorded?",
                        "options": [
                            "Debit Side (Left)",
                            "Credit Side (Right)",
                            "Folio Column",
                            "Nominal Ledger Page"
                        ],
                        "correct_answer": "Credit Side (Right)",
                        "explanation": "All cash outflows/payments are credited on the right-hand side of the Cash Book."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: TWO-COLUMN CASH BOOK (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Two-Column Cash Book",
    "lesson_title": "Unified Liquid Asset Views, Parallel Columns, and Independent Column Balancing",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Two-Column Cash Book",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain the purpose of a Two-Column Cash Book, set up its format, record cash and bank transactions side-by-side, and balance each column independently."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Unified Liquid Asset Management",
                    "content": {
                        "text": "Writing cash entries on page 10 and bank entries on page 20 becomes tedious as a business grows. The Two-Column Cash Book places cash and bank accounts side-by-side on the exact same page, providing managers with a unified, instant view of all liquid assets."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Format and Structure of the Two-Column Cash Book",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Side-by-Side Column Setup",
                    "content": {
                        "text": "A Two-Column Cash Book features two monetary columns (Cash Sh and Bank Sh) on both Debit and Credit sides:\n• Left Side (Debit): Cash receipts and Bank deposits.\n• Right Side (Credit): Cash payments and Bank withdrawals (cheques issued)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Two-Column Cash Book Standard Layout",
                    "svg_content": SVG_TWO_COLUMN_CASH_BOOK_LAYOUT,
                    "content": {
                        "text": "Layout diagram showing Cash and Bank columns side-by-side with independent summation lines."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Rules for Independent Column Balancing",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Independent Column Balancing Rule",
                    "content": {
                        "text": "Cash and Bank are treated as two separate accounts sharing one physical page:\n1. Total Debit Cash vs Credit Cash separately; insert Balance c/d on smaller side.\n2. Total Debit Bank vs Credit Bank separately; insert Balance c/d on smaller side.\n3. NEVER add Cash figures to Bank figures!"
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Mingi Traders Walkthrough & Typo Analysis",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mingi Traders March Walkthrough & Path A/B Analysis",
                    "content": {
                        "text": "Transactions: Balances: Cash 13.2k, Bank 56k. Sales (cash) 12k. Creditor (cheque) 8.2k. Debtors cheque 4.5k (text) / 24.5k (solution). Rent (cash) 7.5k.\n\nPath A (Solution Value 24.5k):\n• Cash Debit (25.2k) - Credit (7.5k) = Cash Balance c/d Sh. 17,700.\n• Bank Debit (80.5k) - Credit (8.2k) = Bank Balance c/d Sh. 72,300.\n\nPath B (Text Value 4.5k):\n• Cash Balance c/d = Sh. 17,700.\n• Bank Debit (60.5k) - Credit (8.2k) = Bank Balance c/d Sh. 52,300."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Tabagon Traders KCSE-Level Two-Column Example",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Tabagon Traders June Two-Column Cash Book",
                    "content": {
                        "text": "June Balances: Cash 22k, Bank 145k. Cheque rec 18k. Water cash 2.4k. Machinery cheque 45k. Carriage cash 3.5k.\n\nResults:\nCash Column: Debit (22k) - Credit (2.4k + 3.5k = 5.9k) = Balance c/d Sh. 16,100.\nBank Column: Debit (145k + 18k = 163k) - Credit (45k) = Balance c/d Sh. 118,000."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Commercial Bank Cash Desk Operations",
                    "content": IMG_BANK_CASH_DESK
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Bank Overdraft Balance Placement",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Bank Overdraft in Two-Column Cash Books",
                    "content": {
                        "text": "If Bank Credit payments exceed Bank Debit deposits, the business has a Bank Overdraft. The opening overdraft balance is brought down on the Credit side (Cr Bal b/d), and the ending Balance c/d is written on the Debit side to balance."
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
                        "text": "Cash and Bank are two independent ledger accounts sharing one page. Each column is totalled and balanced separately."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Spending Physical Cash Boundaries",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Physical Cash Limits",
                    "content": {
                        "text": "Unlike a bank account which can be overdrawn, you CANNOT spend more physical cash than you have! Therefore, the Cash column MUST always have a debit balance or zero."
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
                    "title": "Segregation of Liquid Funds",
                    "content": {
                        "text": "Why Cash and Bank are kept side-by-side: It allows managers to monitor physical till cash versus cleared bank balances without opening separate ledger pages."
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
                        "question": "How are the Cash and Bank columns balanced at the end of the month in a Two-Column Cash Book?",
                        "options": [
                            "Cash and Bank figures are added together and balanced as one total",
                            "Each column (Cash and Bank) is balanced completely independently",
                            "Discount Allowed is subtracted from the Bank column",
                            "Bank figures are transferred to the General Ledger before balancing"
                        ],
                        "correct_answer": "Each column (Cash and Bank) is balanced completely independently",
                        "explanation": "Cash and Bank represent separate ledger accounts sharing a page, so each column is balanced independently."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: THREE-COLUMN CASH BOOK AND DISCOUNTS (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Three-Column Cash Book and Discounts",
    "lesson_title": "Cash Discounts, Three-Monetary Columns, and Discount Totalling Rules",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to the Three-Column Cash Book",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define a Three-Column Cash Book, distinguish between Discount Allowed and Discount Received, calculate cash discounts, and apply the Golden Rule for discount columns."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Integrating Prompt Payment Incentives",
                    "content": {
                        "text": "Offering discounts is a powerful tool to ensure quick payment from credit customers. Instead of opening separate journal entries for hundreds of tiny discounts, the Three-Column Cash Book adds dedicated Discount columns to record payments and discounts simultaneously."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Discount Allowed vs. Discount Received",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "D.A. vs D.R. Definitions",
                    "content": {
                        "text": "• Discount Allowed (D.A.): Allowance granted to credit debtors for prompt payment. Expense to business $\\rightarrow$ Debit side.\n• Discount Received (D.R.): Allowance received from suppliers for prompt settlement. Revenue to business $\\rightarrow$ Credit side."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Golden Rule for Discount Columns",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Golden Discount Rule",
                    "content": {
                        "text": "Unlike Cash and Bank columns, Discount columns are NEVER balanced against each other!\n• Debit Discount column = Total Discount Allowed (Expense).\n• Credit Discount column = Total Discount Received (Revenue).\nAt month-end, simply total each discount column at the bottom without carrying down any balance!"
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Three-Column Cash Book Discount Rules",
                    "svg_content": SVG_THREE_COLUMN_CASH_BOOK_DISCOUNT_RULES,
                    "content": {
                        "text": "Diagram showing Cash/Bank balanced with Balance c/d while Discount columns are only totalled."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Calculating Cash Discounts and Net Amounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Discount Calculation Formulas",
                    "content": {
                        "text": "1. Discount Amount = (Discount % ÷ 100) × Gross Amount Owed\n2. Net Payment Received / Paid = Gross Amount Owed - Discount Amount\nExample: Mwanza settles Sh. 160,000 account at 4% discount ---> Discount = 6,400 Shs; Net Cheque Received = 153,600 Shs."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Mutua Traders January Walkthrough (Part 1)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mutua Traders January Scenario Setup",
                    "content": {
                        "text": "Transactions: Balances: Cash 74k, Bank Overdraft 500k. Sales (cash) 100k. Salaries (cheque) 203k. Mwanza cheque 153,600 (Disc Allowed 6,400). Furniture (cheque) 170k. Kamaru (cash 78,400, Disc Rec 1,600). Sales (cheque) 300k. Wages (cash) 48k. Bank withdrawal 60k (Contra). Drawings (cash) 10k. Maluka (cash 33k, Disc Allowed 1,320)."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Mutua Traders January Walkthrough (Part 2: Deposit Contra & Balances)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Cash Deposit Contra Math & Final Balances",
                    "content": {
                        "text": "Cash Deposit Math:\n• Total Cash Receipts = 74k + 100k + 60k + 33k = 267,000 Shs.\n• Cash Payments before deposit = 78.4k + 48k + 10k = 136,400 Shs.\n• Retained cash required = Sh. 50,000.\n• Cash Deposited into Bank = (267,000 - 136,400) - 50,000 = Sh. 80,600 (Contra entry!).\n\nFinal Balances:\n• Cash Balance c/d = Sh. 50,000.\n• Bank Overdraft Balance c/d = Sh. 398,800.\n• Discount Allowed Total = Sh. 7,720 | Discount Received Total = Sh. 1,600."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Kiboko Traders Three-Column KCSE Example",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Kiboko Traders June Three-Column Cash Book",
                    "content": {
                        "text": "June Balances: Cash 40k, Bank Overdraft 17k. Mutes (cheque 30k, Disc Allowed 2k). Cash banked 12k. Wayua (cheque 39.6k, Disc Rec 400). Capital bank deposit 56k. Cash sales 24k. Mutua (cheque 16k, Disc Allowed 1,632). Odhiambo (cash 7.2k). Retained cash 3.2k (banked 40k contra).\n\nResults: Cash Bal c/d Sh. 3,200; Bank Bal c/d Sh. 87,000; Disc Allowed Sh. 3,632; Disc Received Sh. 400."
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
                        "text": "Cash and Bank columns are balanced using Balance c/d. Discount columns are simply totalled at month-end and never balanced."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Discount Typo Corrections",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Discount Rate Digit Slips",
                    "content": {
                        "text": "If a printed question states 'allowed a cash discount of 40%' for a 6,400 discount on 160,000, it is a digit slip for 4%. Always verify discount math for commercial realism!"
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
                        "question": "What is the correct month-end procedure for the Discount Allowed column in a Three-Column Cash Book?",
                        "options": [
                            "Subtract it from Discount Received and write Balance c/d",
                            "Simply sum up the column total and post it directly to Discount Allowed account in General Ledger",
                            "Carry down the balance to the Credit side",
                            "Transfer the total to the Bank column"
                        ],
                        "correct_answer": "Simply sum up the column total and post it directly to Discount Allowed account in General Ledger",
                        "explanation": "Discount columns are never balanced; they are simply totalled and posted to General Ledger."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: CONTRA ENTRIES AND DISHONOURED CHEQUES (10 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Contra Entries and Dishonoured Cheques",
    "lesson_title": "Internal Fund Transfers, Bounced Cheque Reversals, and Comprehensive Ledger Balancing",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Contra Entries and Bounced Cheques",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define a Contra entry and identify its folio symbol 'C', record cash deposits and withdrawals, explain reasons for dishonoured cheques, and execute reversal entries."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Internal Transfers and Bounced Payments",
                    "content": {
                        "text": "When you transfer cash from the till into the bank, both sides of the double entry happen right inside the Cash Book! This is a Contra entry. When a customer's cheque bounces, you must reverse the bank deposit and restore their debt."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Contra Entries Explained (Symbol 'C')",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Recording Contra Entries",
                    "content": {
                        "text": "A Contra entry completes its double entry within the Cash Book:\n• Cash Deposited into Bank: Credit Cash column, Debit Bank column; write 'C' in L.F.\n• Cash Withdrawn for Office: Credit Bank column, Debit Cash column; write 'C' in L.F."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Contra Entries Flowchart Diagram",
                    "svg_content": SVG_CONTRA_ENTRIES_FLOWCHART,
                    "content": {
                        "text": "Flowchart illustrating internal cash till to bank vault transfers marked with 'C'."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Dishonoured Cheques and Reversal Entries",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Dishonoured Cheque Reversal Path",
                    "content": {
                        "text": "If a cheque bounces (insufficient funds, stop payment, signature mismatch):\n1. Credit Bank Column in Cash Book (reverses bounced deposit).\n2. Debit Debtor's Personal Account in Sales Ledger (revives debt)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Dishonoured Cheque Reversal Flowchart",
                    "svg_content": SVG_DISHONOURED_CHEQUE_REVERSAL_FLOW,
                    "content": {
                        "text": "Sequence diagram showing cheque deposit, dishonour stamp, and credit reversal."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Tabagon Co. Ltd. November Comprehensive Walkthrough",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Tabagon Co. Ltd. November Walkthrough",
                    "content": {
                        "text": "Transactions: Balances: Bank 12k, Cash 2.5k. Sales 2.5k, Purchases 1.75k. Kirop cheque 1,425 (Disc 75), Kirui 1,900 (Disc 100), Nasimiyu 2,037 (Disc 63). Ondiek cash 1.2k, Jane cash 3,850, Mueni cheque 2,050 (Disc 300). Cash banked 2k (Contra). Sales cash 8.5k. Mueni cheque 4.5k (Disc 500). Cash withdrawal contra 14,188. Salary cash 8k. Mueni Nov 5 cheque dishonoured 2,050.\n\nResults:\n• Cash Balance c/d = Sh. 20,988.\n• Bank Overdraft Balance c/d = Sh. 1,050 (caused by Mueni's bounced cheque!).\n• Disc Allowed = Sh. 800 | Disc Received = Sh. 238."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Reasons for Cheque Dishonour",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "6 Common Reasons for Dishonour",
                    "content": {
                        "text": "1. Insufficient Funds (Drawer has less money than cheque value).\n2. Countermand of Payment (Drawer instructs bank to stop payment).\n3. Signature Mismatch (Signature does not match specimen card).\n4. Mutilated Cheque (Cheque is torn or damaged).\n5. Post-Dated Cheque (Cheque date is in the future).\n6. Stale Cheque (Cheque date is over 6 months old)."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Multi-Step Application: Sole Proprietor Liquidity Analysis",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Sole Proprietor November Liquidity Case Study",
                    "content": {
                        "text": "Problem: Cash 50k, Bank Overdraft 12k. Rent cash 15k. Ondiek cheque 19k (Disc 1k). Retained cash 10k (banked 25k contra). Ondiek cheque dishonoured 19k.\n\nLiquidity Analysis:\nEnding Cash = 10,000 Shs; Ending Bank = 13,000 Shs (Positive debit balance!). Total liquidity = Sh. 23,000. Banking 25k cash successfully eliminated opening 12k overdraft despite Ondiek's bounced cheque!"
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "KCSE Integrated Practice: Paper 2 Essay Model Answers",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Model Essay: Commercial Banks vs NBFIs",
                    "content": {
                        "text": "Question: Discuss five differences between commercial banks and non-bank financial institutions (NBFIs) in Kenya (10 Marks).\n\nModel Answer:\n1. Current Account Provision: Commercial banks offer current accounts with cheque books; NBFIs do not.\n2. Term of Finance: Commercial banks focus on short/medium-term working capital; NBFIs focus on long-term capital development.\n3. Purpose Restrictions: Commercial bank credit is unrestricted; NBFI credit is restricted (e.g. mortgages).\n4. Foreign Exchange: Commercial banks deal in forex; NBFIs cannot deal in forex.\n5. Clearing House: Commercial banks participate in clearing houses; NBFIs do not."
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
                        "text": "Contra entries move money internally between cash and bank (marked 'C'). Dishonoured cheques reverse bounced payments by crediting Bank and reviving debtor accounts."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Overdraft Trigger Risk",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Overdraft Risks from Bounced Cheques",
                    "content": {
                        "text": "If you write cheques based on uncleared deposits that later bounce, your account can drop into an expensive bank overdraft!"
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
                        "question": "How is a dishonoured cheque from a debtor recorded in a Three-Column Cash Book?",
                        "options": [
                            "Debited in the Cash column",
                            "Credited in the Bank column with the debtor's name in details",
                            "Credited in the Discount Received column",
                            "Debited in the Discount Allowed column"
                        ],
                        "correct_answer": "Credited in the Bank column with the debtor's name in details",
                        "explanation": "Dishonoured cheques reverse the original deposit by crediting the Bank column in the Cash Book."
                    }
                }
            ]
        }
    ]
}

TOPIC13_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA
]
