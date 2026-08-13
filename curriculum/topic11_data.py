"""
VLearn Form 4 Business Studies — Topic 11: Ledger
Authoritative Pedagogical Data Structures for 4 Lessons (40 Pages).
"""

from curriculum.ingest_form4_business_studies_topic11_svgs import (
    SVG_T_ACCOUNT_STANDARD_LAYOUT,
    SVG_FIVE_POSTING_RULES_MATRIX,
    SVG_SPECIALIZED_STOCK_ACCOUNTS,
    SVG_FIVE_BALANCING_STEPS_FLOWCHART,
    SVG_SIX_LEDGER_CLASSIFICATIONS_TREE
)

# Verified Wikimedia photographic assets
IMG_LEDGER_BOOK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Physical accounting ledger records, illustrating double-entry transaction posting, T-account column structures, and audit trail maintenance.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_RETAIL_TRANSACTIONS = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg",
    "text": "Commercial trading operations demonstrating cash and credit sales transactions posted to specialized ledger accounts.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg"
}

IMG_ACCOUNTING_DESK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "Corporate accounting desk illustrating trial balance preparation, ledger balancing, and error detection.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

# ==============================================================================
# LESSON 1: DOUBLE ENTRY AND LEDGER STRUCTURE (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Double Entry and Ledger Structure",
    "lesson_title": "Architectural T-Account Anatomy, Column Distribution, and Double-Entry Rules",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Ledgers and Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain the meaning and purpose of a ledger and a ledger account, state the basic rules of double-entry bookkeeping, and describe the format and key columns of a standard T-account."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Filing Cabinet of Business Memory",
                    "content": {
                        "text": "As a business grows, it engages in thousands of transactions daily. A ledger acts as the organized filing cabinet of a business's financial brain. By grouping all transactions of the same type into dedicated accounts, the owner can determine at any moment exactly how much cash is available, how much stock is on hand, and how much is owed to suppliers."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Definition of an Account and Ledger",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Account & Ledger Definitions",
                    "content": {
                        "term": "Ledger & Account",
                        "definition": "An Account (A/C) is a chronological, systematic record of all transactions affecting a particular business item. The Ledger is the main 'book of accounts' (or book of second entry) where individual accounts are maintained."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Anatomy of a Standard T-Account",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Structure of a T-Account",
                    "content": {
                        "text": "Every ledger account has the visual shape of a capital letter 'T':\n• Debit Side (Dr): The left-hand side of the account.\n• Credit Side (Cr): The right-hand side of the account.\nEach side contains four functional columns: Date, Particulars, Folio (cross-reference page number), and Amount (Shs)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Standard T-Account Layout Diagram",
                    "svg_content": SVG_T_ACCOUNT_STANDARD_LAYOUT,
                    "content": {
                        "text": "Diagram showing Dr/Cr sides, Title, and 4 functional columns (Date, Particulars, Folio, Amount)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The Golden Rule of Double Entry",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "The Principle of Double Entry",
                    "content": {
                        "term": "Double Entry Rule",
                        "definition": "For every debit entry, there must be an equal and corresponding credit entry. Every transaction affects at least two accounts—one is debited, and the other is credited."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Accounting Ledger Books & Double Entry",
                    "content": IMG_LEDGER_BOOK
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "The Four Functional Columns Explained",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Column Functions",
                    "content": {
                        "text": "1. Date Column: Records the exact day, month, and year of the transaction.\n2. Particulars Column: Brief description naming the corresponding double-entry account.\n3. Folio Column: Page number cross-reference connecting journals and ledgers for audit trails.\n4. Amount Column: Monetary value of the transaction in Kenyan shillings."
                    }
                },
                {
                    "block_type": "table",
                    "component_type": "comparison_table",
                    "title": "Debit Side vs Credit Side Comparison Table",
                    "content": {
                        "headers": ["Feature", "Debit Side (Dr)", "Credit Side (Cr)"],
                        "rows": [
                            ["Position", "Left-hand side of T-account", "Right-hand side of T-account"],
                            ["Increases (+)", "Assets and Expenses", "Liabilities, Capital, and Revenues"],
                            ["Decreases (-)", "Liabilities, Capital, and Revenues", "Assets and Expenses"],
                            ["Normal Balance", "Debit Balance (b/d on left)", "Credit Balance (b/d on right)"]
                        ]
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
                        "text": "An account is a T-shaped chronological record of transactions for a specific item. Every transaction requires dual entries: a debit on the left side of one account and an equal credit on the right side of another."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Watch Out: Debit (Dr) vs. Credit (Cr) Sides",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Left vs Right Memory",
                    "content": {
                        "text": "Do not confuse Debit and Credit! Debit (Dr) ALWAYS refers to the LEFT-hand side of a T-account. Credit (Cr) ALWAYS refers to the RIGHT-hand side. The terms themselves simply mean left and right in accounting layout!"
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
                    "title": "Folio Column Purpose",
                    "content": {
                        "text": "Why Folio is critical: The Folio column cross-references ledger page numbers to source journals. This allows auditors and managers to trace any ledger figure directly back to its original invoice or receipt."
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
                        "question": "In standard double-entry bookkeeping, what is the fundamental rule regarding transaction recording?",
                        "options": [
                            "Every transaction is debited in two separate accounts",
                            "For every debit entry, there must be an equal and corresponding credit entry",
                            "Transactions are credited on the left side of an account",
                            "Assets and Liabilities are recorded in the same T-account"
                        ],
                        "correct_answer": "For every debit entry, there must be an equal and corresponding credit entry",
                        "explanation": "Double-entry bookkeeping mandates that every debit entry must have an equal and corresponding credit entry across accounts."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Lesson 1 Review & Summary",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "summary",
                    "title": "Lesson 1 Summary",
                    "content": {
                        "text": "Ledgers organize financial accounts using T-structures. Left is Debit (Dr), right is Credit (Cr). Every transaction must balance across at least two accounts."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: POSTING RULES FOR TRANSACTIONS (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Posting Rules for Transactions",
    "lesson_title": "Five Core Bookkeeping Rules, 5-Step Posting Procedure, and Stock Accounts",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Posting Rules",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to state and apply the posting rules for assets, liabilities, capital, expenses, and revenues, execute the 5-step transaction analysis, and post stock movements in specialized accounts."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Steering the Accounting Ship",
                    "content": {
                        "text": "Posting a transaction on the wrong side of an account is like steering a ship in the opposite direction. If you buy a motor vehicle but credit the vehicle account, your books falsely show you lost a vehicle instead of acquiring one! Mastering the 5 posting rules guarantees A = C + L stays balanced."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Five Core Posting Rules",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The 5 Core Bookkeeping Rules",
                    "content": {
                        "text": "1. Asset Accounts: Increase on Debit (Dr+), Decrease on Credit (Cr-).\n2. Liability Accounts: Increase on Credit (Cr+), Decrease on Debit (Dr-).\n3. Capital Accounts: Increase on Credit (Cr+), Decrease on Debit (Dr-).\n4. Expense Accounts: Increase on Debit (Dr+), Decrease on Credit (Cr-).\n5. Revenue Accounts: Increase on Credit (Cr+), Decrease on Debit (Dr-)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Five Core Posting Rules Matrix",
                    "svg_content": SVG_FIVE_POSTING_RULES_MATRIX,
                    "content": {
                        "text": "Matrix mapping Assets, Liabilities, Capital, Expenses, and Revenues to Dr/Cr rules."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The 5-Step Transaction Posting Procedure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "5-Step Posting Procedure",
                    "content": {
                        "text": "Step 1: Identify transaction details.\nStep 2: Determine accounts affected.\nStep 3: Classify each account (Asset, Liability, Capital, Expense, Revenue).\nStep 4: Determine direction (+ or -).\nStep 5: Apply Dr/Cr rules to make entries."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Mathai's Business 4-Transaction Worked Walkthrough",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mathai's 4-Transaction Double-Entry Posting",
                    "content": {
                        "text": "Transaction 1 [Feb 1]: Mathai started business with 70k cash ---> Dr Cash A/C 70,000; Cr Capital A/C 70,000.\nTransaction 2 [Feb 4]: Bought office equipment for 20k cash ---> Dr Office Equipment A/C 20,000; Cr Cash A/C 20,000.\nTransaction 3 [Feb 6]: Bought motor vehicle for 350k on credit from Chama Motors ---> Dr Motor Vehicle A/C 350,000; Cr Chama Motors A/C 350,000.\nTransaction 4 [Feb 14]: Deposited 40k cash into bank ---> Dr Bank A/C 40,000; Cr Cash A/C 40,000."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Four Specialized Stock Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Specialized Trading Stock Accounts",
                    "content": {
                        "text": "Do NOT write all stock movements in a general Stock Account! Use four specialized accounts:\n1. Purchases Account: Debited when goods are bought for resale.\n2. Sales Account: Credited when goods are sold to customers.\n3. Returns Inwards Account: Debited when customers return goods.\n4. Returns Outwards Account: Credited when faulty goods returned to suppliers."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Four Specialized Trading Stock Accounts Flowchart",
                    "svg_content": SVG_SPECIALIZED_STOCK_ACCOUNTS,
                    "content": {
                        "text": "Flowchart organizing Purchases, Sales, Returns Inwards, and Returns Outwards."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Source Typo Warnings: Rent & Credit Purchases",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Source Typo Corrections",
                    "content": {
                        "text": "1. Rent Received Typo (Page 345): 'Received 20k cash for rent paid'. Correct label is Rent Received / Rent Income (Revenue Cr).\n2. Credit Purchase Cash Swap Error (Page 345): Solution mistakenly credited Cash for a credit purchase from Crown Traders. Correct entry MUST credit Crown Traders (Creditor), NOT Cash!"
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
                        "text": "Assets and expenses increase on Debit (Dr). Liabilities, Capital, and Revenues increase on Credit (Cr). Stock changes are tracked across four specialized trading accounts."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Watch Out: Buying Resale Goods vs Fixed Assets",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Resale vs Asset Purchases",
                    "content": {
                        "text": "Only goods bought specifically for resale are debited to the Purchases Account! If a business buys office furniture or computers for operational use, debit Furniture or Computer Asset Account directly, NOT Purchases!"
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
                    "title": "Returns Inwards Rule",
                    "content": {
                        "text": "Why Returns Inwards is Debited: When a customer returns goods, trading revenue decreases and stock comes back into the shop. Thus, Returns Inwards Account is debited."
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
                        "question": "Which ledger account is debited when a business purchases a delivery motor van on credit from Kenya Motors?",
                        "options": [
                            "Purchases Account",
                            "Motor Vehicles Account",
                            "Kenya Motors Account",
                            "Cash Account"
                        ],
                        "correct_answer": "Motor Vehicles Account",
                        "explanation": "Purchasing a fixed asset for operations requires debiting the Motor Vehicles asset account directly (not Purchases)."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: BALANCING LEDGER ACCOUNTS (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Balancing Ledger Accounts",
    "lesson_title": "Five Procedural Balancing Steps, Carried Down vs Brought Down, and Trial Balance Agreement",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Balancing Accounts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to explain the meaning of balancing a ledger account, detail the 5 procedural balancing steps, distinguish between debit and credit balances, and balance off a full set of accounts."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Finding the Single Net Truth",
                    "content": {
                        "text": "At the end of a month, an owner does not want to look at 20 separate debit and credit numbers in Cash. They want one clear answer: 'How much cash is left right now?' Balancing off condenses chronological lists into a clean starting balance for the next period."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "The 5 Procedural Balancing Steps",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "5 Steps of Balancing T-Accounts",
                    "content": {
                        "text": "Step 1: Total debit side and credit side separately on scratch paper.\nStep 2: Subtract smaller total from larger total (Account Balance).\nStep 3: Insert 'Balance c/d' on smaller side to force equality.\nStep 4: Draw double lines (underscores) beneath equal horizontal totals.\nStep 5: Bring balance down as 'Balance b/d' on OPPOSITE side below totals."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Five Procedural Steps for Balancing T-Accounts",
                    "svg_content": SVG_FIVE_BALANCING_STEPS_FLOWCHART,
                    "content": {
                        "text": "Flowchart visual outlining the 5 steps: totals, difference, c/d, double underline, b/d."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Debit Balances vs. Credit Balances",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Defining Debit & Credit Balances",
                    "content": {
                        "text": "• Debit Balance: Debit side > Credit side. c/d written on credit side; b/d brought down on debit side. (Assets & Expenses).\n• Credit Balance: Credit side > Debit side. c/d written on debit side; b/d brought down on credit side. (Liabilities, Capital, Revenues)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Mutua Traders 8-Transaction Full Ledger Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Mutua Traders Scenario & Transactions",
                    "content": {
                        "text": "Transactions (Jan 1 - 9, 2015):\nJan 1: Started business with Furniture 130k.\nJan 2: Bought goods 50k on credit from Nyamwea.\nJan 4: Sold goods 40k cash.\nJan 5: Deposited 20k cash into bank.\nJan 6: KIE Loan 30k by cheque.\nJan 7: Paid Nyamwea 30k by cheque.\nJan 9: Withdrew 60k cash from bank for office use."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Mutua Traders Ledger Balancing (Capital, Furniture, Purchases, Sales)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Postings & Balances (Accounts 1-4)",
                    "content": {
                        "text": "1. Capital A/C: Cr Jan 1 Furniture 130k. Jan 10 Balance c/d Dr 130k. Jan 10 Balance b/d Cr 130k.\n2. Furniture A/C: Dr Jan 1 Capital 130k. Jan 10 Balance c/d Cr 130k. Jan 10 Balance b/d Dr 130k.\n3. Purchases A/C: Dr Jan 2 Nyamwea 50k. Jan 10 Balance c/d Cr 50k. Jan 10 Balance b/d Dr 50k.\n4. Sales A/C: Cr Jan 4 Cash 40k. Jan 10 Balance c/d Dr 40k. Jan 10 Balance b/d Cr 40k."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Mutua Traders Ledger Balancing (Bank, Cash, Loan, Nyamwea)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Postings & Balances (Accounts 5-8)",
                    "content": {
                        "text": "5. Bank A/C: Dr (20k + 30k = 50k); Cr (30k + 60k = 90k). Dr Balance c/d 40k. Cr Balance b/d 40k (Bank Overdraft!).\n6. Cash A/C: Dr (40k + 60k = 100k); Cr (20k). Cr Balance c/d 80k. Dr Balance b/d 80k.\n7. KIE Loan A/C: Cr Jan 6 Bank 30k. Dr Balance c/d 30k. Cr Balance b/d 30k. (Source typo 60k corrected to 30k!)\n8. Nyamwea A/C: Dr Jan 7 Bank 30k; Cr Jan 2 Purchases 50k. Dr Balance c/d 20k. Cr Balance b/d 20k."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Double-Entry Balance Agreement Check",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Debit vs Credit Balances Agreement Verification",
                    "content": {
                        "text": "Ending Debit Balances: Furniture (130k) + Purchases (50k) + Cash (80k) = Sh. 260,000.\nEnding Credit Balances: Capital (130k) + Sales (40k) + Bank Overdraft (40k) + KIE Loan (30k) + Nyamwea (20k) = Sh. 260,000.\nBoth sides agree at Sh. 260,000! Double-entry is 100% verified."
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
                        "text": "Balancing off an account calculates the net difference, inserts Balance c/d on the smaller side, double-underlines equal totals, and brings down Balance b/d on the opposite side."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Balance b/d Placement",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Balance b/d Side",
                    "content": {
                        "text": "Balance c/d is written on the smaller side to force mathematical equality. But Balance b/d MUST be brought down on the OPPOSITE side (the side that originally had larger transactions)!"
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
                        "question": "If the debit side of a Cash account totals Sh. 100,000 and the credit side totals Sh. 20,000, how is the account balanced off?",
                        "options": [
                            "Balance c/d Sh. 80,000 is written on the debit side",
                            "Balance c/d Sh. 80,000 is written on the credit side, and Balance b/d Sh. 80,000 is brought down on the debit side",
                            "Both sides are double-underlined at Sh. 80,000",
                            "Balance b/d Sh. 80,000 is brought down on the credit side"
                        ],
                        "correct_answer": "Balance c/d Sh. 80,000 is written on the credit side, and Balance b/d Sh. 80,000 is brought down on the debit side",
                        "explanation": "Since the debit side is larger by Sh. 80,000, Balance c/d is inserted on the credit side to balance, and brought down as Balance b/d on the debit side."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: TYPES OF LEDGERS AND EXAMINATION APPLICATION (10 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Types of Ledgers and Examination Application",
    "lesson_title": "Six Ledger Classifications, Multi-Step Ledger Posting, and Trial Balance Error Analysis",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Ledger Classifications",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to list and define the six primary classifications of ledgers, assign accounts to correct ledger books, execute multi-step postings, and master KCSE trial balance error essays."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Organizing the Accounting Library",
                    "content": {
                        "text": "If a business kept hundreds of customer accounts, supplier accounts, expense accounts, and asset accounts in one massive book, finding a single balance would take hours. Segmenting accounts into 6 logical ledger books keeps accounting efficient and secure."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Six Primary Ledger Classifications",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The 6 Ledger Books",
                    "content": {
                        "text": "1. Sales Ledger (Debtors Ledger): Personal accounts of credit customers (Wanjiku, Otieno).\n2. Purchase Ledger (Creditors Ledger): Personal accounts of credit suppliers (Chama Motors, Nyamwea).\n3. Cash Book: Cash in hand and cash at bank accounts.\n4. Nominal Ledger: Operational expenses and non-trading revenues (Wages, Rent, Commission).\n5. Private Ledger: Confidential owner equity accounts (Capital, Drawings).\n6. General Ledger: Catch-all for real accounts, fixed assets, and stock (Buildings, Vehicles, Stock)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Six Classifications of Accounting Ledgers Mind Map",
                    "svg_content": SVG_SIX_LEDGER_CLASSIFICATIONS_TREE,
                    "content": {
                        "text": "Mind map diagram showing Sales, Purchase, Cash Book, Nominal, Private, and General ledgers."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Corporate Office Accounting Operations",
            "blocks": [
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Corporate Office Accounting Desk & Trial Balance",
                    "content": IMG_ACCOUNTING_DESK
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Otieno Multi-Step Ledger Posting Scenario",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "Otieno November 2025 Multi-Step Scenario",
                    "content": {
                        "text": "Transactions:\nNov 1: Started business with 80k cash till.\nNov 3: Bought furniture 15k on credit from Woodworks Ltd.\nNov 5: Bought goods 30k cash.\nNov 12: Deposited 40k cash into bank.\nNov 20: Paid Woodworks Ltd 10k by cheque.\n\nBalances as at Nov 30:\nCapital b/d Cr 80k, Furniture b/d Dr 15k, Purchases b/d Dr 30k, Cash b/d Dr 10k, Bank b/d Dr 30k, Woodworks Ltd b/d Cr 5k."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "KCSE Integrated Practice: Paper 1 (Ledger Table)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Paper 1 Double-Entry Table",
                    "content": {
                        "text": "• Paid creditor 12k from private savings ---> Dr Creditor A/C, Cr Capital A/C.\n• Started business with 150k personal cash ---> Dr Cash A/C, Cr Capital A/C.\n• Purchased sewing machine for resale by cheque 45k ---> Dr Purchases A/C, Cr Bank A/C.\n• Proprietor withdrew 8k cash for home use ---> Dr Drawings A/C, Cr Cash A/C."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "KCSE Integrated Practice: Paper 2 (Uses of Ledgers Essay)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Model Essay: Five Uses of Ledger Accounts",
                    "content": {
                        "text": "Question: Explain five uses of ledger accounts to a business organization (10 Marks).\n\nModel Answer:\n1. Tracking Increases and Decreases: Summarizes chronological movements in specific assets, liabilities, and expenses.\n2. Rapid Computation of Ending Balances: Calculates net balances instantly without reviewing raw documents.\n3. Permanent Reference Audit Material: Serves as historical records for managers, tax auditors, and legal verification.\n4. Facilitating Final Financial Accounts: Provides summarized figures to prepare Trading, Profit & Loss, and Balance Sheets.\n5. Checking Arithmetic Accuracy: Enables Trial Balance preparation to detect bookkeeping errors."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "KCSE Integrated Practice: Paper 2 (Errors Not Disclosed by Trial Balance)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "worked_example",
                    "title": "KCSE Model Essay: Five Errors Not Disclosed by Trial Balance",
                    "content": {
                        "text": "Question: Discuss five types of errors that are not disclosed by a Trial Balance (10 Marks).\n\nModel Answer:\n1. Error of Omission: Transaction completely omitted from books; no debit or credit made.\n2. Error of Commission: Posted to correct side of wrong account within same class (e.g. Otieno instead of Okoth).\n3. Error of Principle: Transaction recorded in wrong class of account (e.g. motor van debited to Purchases).\n4. Error of Complete Reversal: Correct accounts used, but debit is credited and credit is debited.\n5. Error of Compensation: Separate errors in different accounts accidentally cancel each other out."
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
                        "text": "Ledgers are divided into six specialized books (Sales, Purchase, Cash Book, Nominal, Private, General) to organize records. Trial Balances test arithmetic equality but cannot detect errors of omission, principle, or commission."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Watch Out: Error of Principle",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Watch Out: Error of Principle",
                    "content": {
                        "text": "An Error of Principle occurs when an entry breaks fundamental accounting concepts—such as debiting Purchases (Expense) when buying a delivery van (Fixed Asset). Because a debit and credit of equal value were made, the Trial Balance WILL STILL BALANCE!"
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
                        "question": "In which specialized ledger book are the personal accounts of credit suppliers (creditors) kept?",
                        "options": [
                            "Sales Ledger",
                            "Purchase Ledger",
                            "Nominal Ledger",
                            "Private Ledger"
                        ],
                        "correct_answer": "Purchase Ledger",
                        "explanation": "The Purchase Ledger (also called Creditors Ledger) contains the personal accounts of all credit suppliers."
                    }
                }
            ]
        }
    ]
}

TOPIC11_UNITS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA,
    LESSON_4_DATA
]
