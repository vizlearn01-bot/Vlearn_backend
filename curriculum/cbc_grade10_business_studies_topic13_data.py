"""
VLearn CBC Grade 10 Business Studies — Topic 13: Business Transactions
Full Structured Lesson Card Definitions (Lessons 1 to 5)
"""

from curriculum.cbc_grade10_business_studies_topic13_svgs import (
    SVG_TRANSACTION_ANATOMY_AND_TAXONOMY,
    SVG_CASH_TRANSACTION_DYNAMICS,
    SVG_CREDIT_LIFECYCLE_AND_RISK_FRAMEWORK,
    SVG_PAYMENT_METHODS_TAXONOMY_AND_TRADE_OFFS,
    SVG_ENTERPRISE_PAYMENT_POLICY_ARCHITECTURE
)

TOPIC_13_LESSONS = [
    # =========================================================================
    # LESSON 1: Meaning and Nature of Business Transactions
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Meaning and Nature of Business Transactions",
        "unit_description": "Conceptual definition of business transactions, criteria for commercial validity, distinction between external and internal transactions, financial impact, source document verification, and economic valuation.",
        "lesson_title": "Meaning and Nature of Business Transactions",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Vibrant Retail and Commercial Trading in Nairobi",
                    "content": {
                        "title": "Commercial Transactions in Kenyan Retail Markets",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "A lively commercial market scene in Nairobi, where hundreds of cash, mobile, and credit transactions take place daily to drive commerce.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a business transaction and distinguish transactions from non-transactional operational events\n- Differentiate between external and internal business transactions with concrete Kenyan commercial examples\n- Analyze the four mandatory characteristics of a valid business transaction (two parties, exchange of value, monetary measurement, source document support)\n- Calculate net changes in business net worth resulting from commercial transactions"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Business Transactions and Commercial Parties",
                    "content": {
                        "term": "Business Transaction",
                        "definition": "Any financial event or exchange of value between two or more parties that can be measured objectively in monetary terms (e.g. Kenya Shillings) and directly alters the assets, liabilities, or owner's equity of an enterprise."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Football Passing Analogy & Core Pillars",
                    "content": {
                        "text": "Understanding what constitutes a valid business transaction is like analyzing a football pass during a match:\n\n- **Two Distinct Players:** For a pass to occur, there must be a passer (seller) and a receiver (buyer). One player cannot complete a pass alone.\n- **Object of Value Passed:** The ball represents physical goods, services, or cash being exchanged.\n- **Observable Definite Action:** The kick changes the physical position of the ball. In business, a financial settlement changes the financial position of the enterprise.\n- **Non-Transaction Operational Events:** If a football player simply ties his shoelaces or polishes his boots on the pitch, no pass occurred. Similarly, when a shopkeeper dusts display shelves, interviews a job applicant, or discusses a prospective order over a cup of tea, no value has been transferred, no source document is generated, and zero accounting entries are made in the financial ledger."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Anatomy & Taxonomy of Business Transactions",
                    "content": {
                        "title": "The Four Pillars of Validity and Dual Transaction Classification",
                        "caption": "High-precision architectural diagram illustrating the four mandatory pillars of a valid transaction, external vs. internal exchanges, and the fundamental accounting equation filter.",
                        "svg_content": SVG_TRANSACTION_ANATOMY_AND_TAXONOMY
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "External vs. Internal Transactions",
                    "content": {
                        "text": "Every valid business transaction is categorized into one of two structural classes:\n\n1. **External Transactions:** Financial exchanges occurring between the enterprise and outside third-party entities. Examples include selling electronics to walk-in customers, buying stock from factory distributors, paying rent to a landlord, or settling electricity bills with Kenya Power via Paybill.\n2. **Internal Transactions:** Financial events that occur entirely within the boundaries of the firm without direct interaction with outside entities, yet still alter the book value of business assets or liabilities. Examples include writing down the annual depreciation of a delivery motorbike, transferring finished inventory from the central warehouse to the retail shop floor, or writing off damaged stock."
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Classification Matrix: External, Internal, and Non-Transaction Events",
                    "content": {
                        "headers": ["Classification", "Parties Involved", "Exchange / Event Nature", "Source Document Generated", "Accounting / Financial Statement Impact", "Kenyan Enterprise Example"],
                        "rows": [
                            ["External Cash / Credit Sale", "Business & External Customer", "Transfer of goods/services for instant cash or credit promise", "Cash Sale Receipt / Commercial Sales Invoice", "Increases Cash / Debtors; Increases Sales Revenue", "Selling 5 solar panels for KES 60,000 at Juma's Eldoret shop"],
                            ["External Expense Settlement", "Business & Service / Utility Provider", "Payment for utility services or operational inputs consumed", "Payment Voucher / ETR Receipt / Bank Slip", "Decreases Cash; Increases Operating Expenses", "Paying KES 4,500 monthly electricity bill to Kenya Power via Paybill"],
                            ["Internal Asset Adjustment", "Business Internal Entity Only", "Wear-and-tear adjustment or reallocation of asset values", "Depreciation Schedule / Journal Voucher", "Decreases Fixed Asset book value; Increases Depreciation Expense", "Writing down Eldoret shop delivery motorbike value by KES 15,000 annual wear"],
                            ["Non-Transaction Event", "Business & Prospective Client / Applicant", "Preliminary discussions or maintenance without value transfer", "None (Internal Minutes or Meeting Memo only)", "Zero financial impact; strictly omitted from accounting books", "Interviewing two sales assistant candidates for the electronics shop"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Accounting Equation Impact & Net Worth Calculation",
                    "content": {
                        "intro": "Juma establishes 'Eldoret SmartHub' with an initial cash capital investment of $C_0 = \\text{KES } 250,000$. During his first week of commercial operations, he engages in the following four events:\n1. Purchases 10 smartphones for $\\text{KES } 120,000$ cash to hold as trading inventory.\n2. Pays shop rent of $\\text{KES } 20,000$ in cash for the month.\n3. Sells 4 smartphones (which cost $\\text{KES } 12,000$ each, total cost $\\text{KES } 48,000$) to customers for a total cash price of $\\text{KES } 72,000$.\n4. Spends 2 hours interviewing two candidates for a shop assistant position.\n\nCalculate Juma's closing cash balance, closing inventory value, total business assets, net profit earned, and closing owner's equity, verifying that the fundamental Accounting Equation holds.",
                        "steps": [
                            "**Step 1: Given Information:** Initial cash $C_0 = \\text{KES } 250,000$. Inventory purchase $P_1 = \\text{KES } 120,000$ ($10\\text{ units @ KES } 12,000$). Rent expense $E_1 = \\text{KES } 20,000$. Sales revenue $R_1 = \\text{KES } 72,000$ ($4\\text{ units sold}$). Cost of goods sold $\\text{COGS} = 4 \\times \\text{KES } 12,000 = \\text{KES } 48,000$. Job interview event = Non-transaction ($\\text{KES } 0$).",
                            "**Step 2: Formula & Accounting Rules:**\n$$\\text{Closing Cash} = C_0 - P_1 - E_1 + R_1$$\n$$\\text{Closing Inventory} = \\text{Initial Stock Purchased} - \\text{COGS}$$\n$$\\text{Total Assets} = \\text{Closing Cash} + \\text{Closing Inventory}$$\n$$\\text{Net Profit} = R_1 - \\text{COGS} - E_1$$\n$$\\text{Closing Owner's Equity} = C_0 + \\text{Net Profit}$$\n$$\\text{Accounting Equation Test:} \\quad \\text{Assets} = \\text{Liabilities} + \\text{Owner's Equity}$$",
                            "**Step 3: Substitution:**\n$$\\text{Closing Cash} = 250,000 - 120,000 - 20,000 + 72,000$$\n$$\\text{Closing Inventory} = 120,000 - 48,000$$\n$$\\text{Net Profit} = 72,000 - 48,000 - 20,000$$\n$$\\text{Closing Equity} = 250,000 + \\text{Net Profit}$$",
                            "**Step 4: Calculation:**\n$$\\text{Closing Cash} = \\text{KES } 182,000$$\n$$\\text{Closing Inventory} = \\text{KES } 72,000 \\quad (6 \\text{ smartphones remaining @ KES } 12,000)$$\n$$\\text{Total Assets} = 182,000 + 72,000 = \\text{KES } 254,000$$\n$$\\text{Net Profit} = 24,000 - 20,000 = \\text{KES } 4,000$$\n$$\\text{Closing Owner's Equity} = 250,000 + 4,000 = \\text{KES } 254,000$$",
                            "**Step 5: Final Answer & Unit Verification:** Closing Cash is $\\text{KES } 182,000$. Closing Inventory is $\\text{KES } 72,000$. Total Assets equal $\\text{KES } 254,000$. Net Profit earned is $\\text{KES } 4,000$. Liabilities are $\\text{KES } 0$. Therefore, $\\text{Assets } (\\text{KES } 254,000) = \\text{Liabilities } (\\text{KES } 0) + \\text{Owner's Equity } (\\text{KES } 254,000)$, perfectly balancing the equation.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Valid commercial transactions actively expand owner equity through generated profit margins. The job interview event is omitted entirely because no exchange of value occurred ($\\text{KES } 0$ financial impact). *Common Pitfall:* Counting the full selling price ($\\text{KES } 72,000$) as profit without deducting the $\\text{KES } 48,000$ cost of inventory sold and $\\text{KES } 20,000$ operating rent expenses."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Juma Electronics in Eldoret CBD",
                    "content": {
                        "title": "Transitioning from Informal Handshakes to Digitized Transaction Records",
                        "text": "In Eldoret town along Uganda Road, Juma operated 'Juma Electronics and Mobile Care' for three years as an informal kiosk. He frequently mixed personal cash with shop proceeds, neglected to issue receipts for smartphone repairs, and failed to record stock taken by relatives. Consequently, his business suffered unexplained cash shortfalls and stock shrinkage exceeding KES 180,000 annually. After attending a Kenya National Chamber of Commerce and Industry (KNCCI) enterprise workshop, Juma installed a digitized Point-of-Sale (POS) electronic cash register linked to a KRA Electronic Tax Register (ETR). Every single smartphone sale, screen repair fee, and spare part purchase was backed by a numbered source receipt. Within six months, stock losses dropped by 92%, and his audited transaction records enabled him to secure a KES 500,000 commercial expansion loan from a local bank."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Introduction to Business Transactions and Accounting Foundations",
                    "content": {
                        "title": "Understanding Business Transactions, Source Documents, and the Accounting Equation",
                        "youtube_id": "v83s92y5Tq4",
                        "url": "https://www.youtube.com/watch?v=v83s92y5Tq4",
                        "description": "Educational breakdown of business transactions, distinguishing financial exchanges from operational activities, and tracing impacts on the fundamental accounting equation."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying Valid Business Transactions",
                    "content": {
                        "question": "Wanjiku operates a bakery in Nakuru. On Monday morning, she signs a one-year contract with a new delivery driver agreeing that he will start work next Monday at a monthly wage of KES 18,000. On Monday afternoon, she pays KES 2,500 cash to a local mechanic who repaired the bakery delivery van. How should Wanjiku treat these two events in her accounting books?",
                        "options": [
                            "Record both events as valid business transactions immediately in the cash book",
                            "Record the KES 2,500 repair as a valid transaction, but do not record the signed employment contract until work is performed and wages are paid",
                            "Record the employment contract as an asset and ignore the repair expense",
                            "Omit both events because neither involved the direct sale of bread to customers"
                        ],
                        "correct": "B",
                        "explanation": "Paying KES 2,500 for van repairs involves an immediate exchange of cash for repair services supported by a receipt, making it a valid external transaction. The signed employment contract is an agreement for future services; no work has been done and no money has changed hands, so it cannot be entered into financial accounts until wages are earned or paid."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Classification of Business Transactions",
                    "content": {
                        "question": "Which of the following scenarios represents an internal business transaction rather than an external business transaction?",
                        "options": [
                            "Settling a monthly KES 6,000 water bill with the county water company via mobile money",
                            "Purchasing 50 bags of wheat flour from a grain miller on 30-day credit terms",
                            "Writing down the book value of office computers by KES 25,000 to reflect annual depreciation wear",
                            "Receiving a KES 100,000 bank loan deposit into the business current account"
                        ],
                        "correct": "C",
                        "explanation": "Calculating and recording depreciation is an internal transaction because it takes place entirely within the business enterprise without an external third party, yet it directly adjusts asset book values and net profit in the financial statements."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Definition of Transaction:** A business transaction is any exchange of value between two or more parties that is measurable in money and alters the firm's financial position.\n2. **The 4 Pillars of Validity:** Every valid transaction requires two distinct parties, an exchange of economic value, objective monetary valuation (KES), and verifiable source document proof.\n3. **External vs. Internal Exchanges:** External transactions occur with outside entities (sales, purchases, utility bills); internal transactions adjust internal asset values (depreciation, stock write-downs).\n4. **Accounting Equation Filter:** Operational activities (interviews, price inquiries, cleaning) that involve no value exchange are strictly excluded from financial accounting records."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Cash Transactions
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Cash Transactions",
        "unit_description": "Nature of immediate commercial settlement, physical and digital cash instruments, cash discounts, cash receipts, liquidity benefits, security challenges, and working capital acceleration.",
        "lesson_title": "Cash Transactions",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Wangige Local Produce Market in Kiambu County",
                    "content": {
                        "title": "Instant Cash Settlement at Wangige Market",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
                        "caption": "Traders exchanging farm produce for immediate cash and mobile money payments at Wangige market, demonstrating instant cash settlement.",
                        "author": "Kristinabudiati",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define cash transactions and explain why modern 'cash' encompasses physical currency, mobile wallets, and instant bank transfers\n- Analyze the 4 primary advantages and 3 major operational disadvantages of cash transactions\n- Distinguish between Trade Discount and Cash Discount in commercial settlement\n- Calculate cash discounts, net cash received, and prompt settlement savings"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Cash Transactions and Liquid Equivalents",
                    "content": {
                        "term": "Cash Transaction",
                        "definition": "A commercial transaction where monetary payment is made or received immediately at the exact time goods or services are exchanged, leaving zero outstanding debt between buyer and seller."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Modern Cash & The Instant Coffee Analogy",
                    "content": {
                        "text": "In contemporary Kenyan business, 'cash' is not limited to paper banknotes and coins. It includes any financial instrument that gives the seller instant, spendable purchasing power:\n\n- **The Instant Coffee Analogy:** When you prepare instant coffee, adding hot water to granules produces ready coffee on the spot—there is no roasting, grinding, or drip delay. A cash transaction produces immediate liquidity on the spot, concluding the commercial contract without debtor tracking.\n- **Modern Cash Equivalents:** Physical currency notes/coins, Mobile Money (M-Pesa Buy Goods Till, Airtel Money), Point-of-Sale (POS) debit card swipes, and real-time bank transfers (PesaLink).\n- **Cash Receipt:** The primary source document issued by the seller to the buyer as legal proof that immediate payment has been received.\n- **Cash Discount:** A percentage price reduction granted by the seller to induce the buyer to settle promptly in cash rather than taking credit."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Cash Transaction Settlement Mechanism & Liquidity Flow",
                    "content": {
                        "title": "Immediate Value Exchange and Working Capital Acceleration",
                        "caption": "High-precision vector diagram illustrating the immediate settlement architecture, modern Kenyan cash instruments, and the working capital liquidity flywheel.",
                        "svg_content": SVG_CASH_TRANSACTION_DYNAMICS
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Trade Discount vs. Cash Discount Dynamics",
                    "content": {
                        "text": "A crucial commercial distinction in transactions is between trade discounts and cash discounts:\n\n- **Trade Discount:** A deduction from the catalogue list price given to encourage bulk purchasing or trade intermediaries. It is deducted on the invoice before calculating net amounts and is never recorded in formal ledger discount accounts.\n- **Cash Discount:** A financial incentive offered on the net invoice price to motivate immediate cash payment or settlement within a specified discount period (e.g. 5% cash discount for spot payment). It is formally recorded as 'Discount Allowed' (an expense for the seller) and 'Discount Received' (revenue for the buyer)."
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comparative Analysis: Cash Transactions vs. Credit Transactions",
                    "content": {
                        "headers": ["Operational Dimension", "Cash Transaction", "Credit Transaction", "Seller Advantage / Risk", "Buyer Advantage / Risk"],
                        "rows": [
                            ["Settlement Timing", "Immediate at point of exchange", "Deferred by 30 to 90 days", "Seller gains instant spendable cash; zero waiting", "Buyer must possess ready funds immediately"],
                            ["Default & Bad Debt Risk", "0.00% (Zero default possibility)", "Moderate to High default risk", "Seller completely eliminates bad debt write-offs", "Buyer avoids interest or late repayment penalties"],
                            ["Price Concessions", "Cash Discounts (2% to 5%)", "Trade discounts for volume only", "Seller sacrifices small margin to accelerate cash velocity", "Buyer secures lower unit purchase cost"],
                            ["Source Document", "Cash Sale Receipt / ETR Slip", "Commercial Sales Invoice", "Immediate cash book entry with zero debtor ledger upkeep", "Buyer records accounts payable liability in purchases ledger"],
                            ["Sales Turnover Impact", "Capped by buyer's instant pocket money", "Dramatically expands purchasing volume", "Seller risks losing high-ticket sales if credit is refused", "Buyer can acquire productive equipment and stock on credit"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Trade Discount, Cash Discount, and Net Cash Settlement",
                    "content": {
                        "intro": "Atieno operates a wholesale grain store in Kibuye Market, Kisumu. She sells $Q = 50\\text{ bags}$ of dry maize to 'Lakeside Bakers' at a catalogue list price of $P = \\text{KES } 3,200\\text{ per bag}$. She offers a $TD = 10\\%$ Trade Discount for bulk purchases exceeding 30 bags, and an additional $CD = 5\\%$ Cash Discount if the buyer settles immediately via mobile money. Lakeside Bakers pays on the spot via Lipa Na M-Pesa. Calculate the Gross Catalogue Value, Trade Discount Amount, Net Invoice Price, Cash Discount Amount, and Final Cash Amount received by Atieno.",
                        "steps": [
                            "**Step 1: Given Information:** Quantity $Q = 50\\text{ bags}$. Unit catalogue list price $P = \\text{KES } 3,200$. Bulk trade discount rate $TD = 10\\% = 0.10$. Prompt cash discount rate $CD = 5\\% = 0.05$.",
                            "**Step 2: Formula & Economic Accounting Rules:**\n$$\\text{Gross Catalogue Value} = Q \\times P$$\n$$\\text{Trade Discount Amount} = \\text{Gross Catalogue Value} \\times TD$$\n$$\\text{Net Invoice Price} = \\text{Gross Catalogue Value} - \\text{Trade Discount Amount}$$\n$$\\text{Cash Discount Amount} = \\text{Net Invoice Price} \\times CD$$\n$$\\text{Final Cash Settled} = \\text{Net Invoice Price} - \\text{Cash Discount Amount}$$",
                            "**Step 3: Substitution:**\n$$\\text{Gross Catalogue Value} = 50 \\times 3,200$$\n$$\\text{Trade Discount Amount} = 160,000 \\times 0.10$$\n$$\\text{Net Invoice Price} = 160,000 - 16,000$$\n$$\\text{Cash Discount Amount} = 144,000 \\times 0.05$$\n$$\\text{Final Cash Settled} = 144,000 - 7,200$$",
                            "**Step 4: Calculation:**\n$$\\text{Gross Catalogue Value} = \\text{KES } 160,000$$\n$$\\text{Trade Discount Amount} = \\text{KES } 16,000$$\n$$\\text{Net Invoice Price} = \\text{KES } 144,000$$\n$$\\text{Cash Discount Amount} = \\text{KES } 7,200$$\n$$\\text{Final Cash Settled} = \\text{KES } 136,800$$",
                            "**Step 5: Final Answer & Unit Verification:** The Gross Catalogue Value is $\\text{KES } 160,000$. The Trade Discount is $\\text{KES } 16,000$. The Net Invoice Price is $\\text{KES } 144,000$. The Cash Discount allowed is $\\text{KES } 7,200$. The total cash received by Atieno into her mobile till is $\\text{KES } 136,800$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Trade discount is deducted first from the list price to determine the agreed commercial transaction price (Net Invoice Price of $\\text{KES } 144,000$). The cash discount is then computed strictly on this net invoice amount. *Common Pitfall:* Adding the two discount percentages together ($10\\% + 5\\% = 15\\%$) and deducting $15\\%$ from the gross value ($160,000 \\times 0.15 = \\text{KES } 24,000$). Deducting sequentially yields a combined discount of $\\text{KES } 23,200$, avoiding a costly $\\text{KES } 800$ error."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Atieno Grain Wholesalers in Kisumu",
                    "content": {
                        "title": "Eliminating Cash Shrinkage and Capturing Supplier Discounts via Digital Cash",
                        "text": "At Kibuye Market in Kisumu, Atieno Wholesalers traded strictly in physical paper notes. In 2023, Atieno suffered two major setbacks: employee cash drawer theft of KES 65,000 and the inadvertent acceptance of three counterfeit KES 1,000 notes. Furthermore, carrying bags of cash to bank branches at 4:00 PM exposed her to street muggings. Atieno adopted a Safaricom Lipa Na M-Pesa Buy Goods Till. Over 90% of her retail and wholesale buyers switched to mobile till payments. With instant, verified digital cash flowing directly into her business wallet, Atieno was able to instantly settle raw grain purchases with farmers in rural Siaya using B2C mobile transfers, capturing a 4% prompt cash discount. Her annual working capital turnover accelerated from 6 cycles to 14 cycles."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Cash Transactions, Receipts, and Liquidity Management",
                    "content": {
                        "title": "Mechanics of Cash Transactions, Working Capital Velocity, and Cash Discounts",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "Comprehensive visual guide to cash transactions, liquidity management, trade vs cash discounts, and digital cash settlement channels."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Calculating Net Cash from Sequential Discounts",
                    "content": {
                        "question": "A hardware dealer in Machakos lists 100 bags of cement at KES 800 per bag. He grants a 5% Trade Discount for bulk purchases and an additional 4% Cash Discount for instant settlement via mobile money. If a builder buys all 100 bags and pays immediately, what is the exact cash amount the builder settles?",
                        "options": [
                            "KES 72,800",
                            "KES 72,960",
                            "KES 76,000",
                            "KES 73,600"
                        ],
                        "correct": "B",
                        "explanation": "Gross value = 100 × 800 = KES 80,000. Trade discount = 5% of 80,000 = KES 4,000. Net invoice price = 80,000 - 4,000 = KES 76,000. Cash discount = 4% of 76,000 = KES 3,040. Final cash settled = 76,000 - 3,040 = KES 72,960."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Liquidity Advantages of Cash Transactions",
                    "content": {
                        "question": "Why does a retail supermarket in Eldoret actively encourage customers to pay cash or mobile money rather than offering 30-day store credit accounts?",
                        "options": [
                            "Cash transactions legally exempt the supermarket from paying corporate income taxes to KRA",
                            "Cash transactions provide immediate liquidity to restock fast-moving goods and eliminate bad debt default losses",
                            "Commercial banks charge a 20% penalty fee on all credit sales invoices",
                            "Credit transactions require physical gold deposits at the Central Bank of Kenya"
                        ],
                        "correct": "B",
                        "explanation": "Cash transactions provide instant liquidity, enabling the enterprise to restock inventory immediately without delay, while totally eliminating the risk of customer defaults (bad debts) and debtor administrative costs."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Definition of Cash Transaction:** Immediate monetary settlement at the point of exchange, leaving zero outstanding liability between parties.\n2. **Modern Cash Scope:** Encompasses physical currency, mobile money (M-Pesa till), debit card POS swipes, and real-time bank transfers (PesaLink).\n3. **Trade vs. Cash Discounts:** Trade discount is deducted from list price for volume; cash discount is deducted from net invoice price to reward prompt payment.\n4. **Liquidity vs. Sales Cap Trade-Off:** Cash transactions ensure zero bad debts and immediate reinvestment, but offering credit may be necessary to win high-ticket sales."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Credit Transactions
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Credit Transactions",
        "unit_description": "Mechanics of deferred settlement, debtors as current assets, creditors as current liabilities, credit terms, credit appraisal (the 5 Cs), invoice generation, bad debts, and debt recovery.",
        "lesson_title": "Credit Transactions",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Commercial Wholesale and Trade Goods in Nairobi",
                    "content": {
                        "title": "Wholesale Trade and Credit Supply in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Maasai_Market-Nairobi.jpg",
                        "caption": "Artisans and wholesale merchants negotiating trade terms and credit supply agreements in Nairobi.",
                        "author": "khym54",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define credit transactions and explain the economic rationale behind deferred commercial settlement\n- Distinguish between debtors (accounts receivable / assets) and creditors (accounts payable / liabilities)\n- Interpret standard credit terms (e.g. '2/10, net 30') and calculate cash discount savings versus annual cost of trade credit\n- Evaluate credit management tools (the 5 Cs of Credit) and bad debt provisioning"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Credit Transactions, Debtors, and Creditors",
                    "content": {
                        "term": "Credit Transaction",
                        "definition": "A commercial agreement where goods or services are delivered immediately to the buyer, but financial settlement is legally deferred (postponed) to a specified future maturity date."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Postpaid Electricity Analogy & Balance Sheet Roles",
                    "content": {
                        "text": "Understanding credit transactions is intuitive when compared to postpaid utility services:\n\n- **Postpaid Electricity Analogy:** Kenya Power supplies electricity to your business 24/7. You use it to power machinery and lights without paying on the spot. At month-end, you receive an itemized bill (invoice) with a 30-day payment deadline. You consume value today and settle later.\n- **Debtor (Account Receivable):** A customer who has received goods on credit and owes money to the enterprise. In accounting, debtors are classified as **Current Assets** because they represent future cash inflows.\n- **Creditor (Account Payable):** A supplier from whom the enterprise purchased goods on credit and to whom money is owed. Creditors are classified as **Current Liabilities** because they represent future cash outflows.\n- **Sales Invoice:** The primary source document issued by a credit seller detailing goods supplied, prices, total debt, delivery dates, and credit terms (e.g. 'net 30').\n- **Bad Debt:** An uncollectible debtor balance written off as an operating expense when the customer goes bankrupt, becomes untraceable, or defaults."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Credit Transaction Lifecycle & The 5 Cs Appraisal Model",
                    "content": {
                        "title": "Stages of Commercial Credit and Debtor Risk Management",
                        "caption": "Architectural vector diagram illustrating the 5-stage credit lifecycle, the 5 Cs of credit appraisal, credit terms (2/10, net 30), and the balance sheet dichotomy between Debtors and Creditors.",
                        "svg_content": SVG_CREDIT_LIFECYCLE_AND_RISK_FRAMEWORK
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 5 Cs of Credit Appraisal",
                    "content": {
                        "text": "Before granting credit to a buyer, professional enterprises evaluate the **5 Cs of Credit** to protect against default:\n\n1. **Character:** The buyer's integrity, reputation, and willingness to pay (verified through Credit Reference Bureau / CRB scores and past supplier references).\n2. **Capacity:** The cash flow generating ability of the customer's business to service debt obligations from operating turnover.\n3. **Capital:** The financial strength and net equity invested by the owners in the business.\n4. **Collateral:** Tangible assets (e.g. logbooks, title deeds, inventory charges) pledged by the borrower to secure repayment in case of default.\n5. **Conditions:** Macroeconomic factors, industry growth trends, interest rates, and inflation affecting the borrower's operational environment."
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "The 5 Cs of Credit Appraisal for Kenyan Enterprises",
                    "content": {
                        "headers": ["The 5 Cs Pillar", "Definition / Core Question", "Verification Method in Kenya", "Risk Indicator to Watch", "Enterprise Mitigation Strategy"],
                        "rows": [
                            ["Character", "Does the debtor demonstrate moral integrity to honor debt?", "CRB credit report, Metropol score, trade references", "History of bounced cheques, loan defaults, court disputes", "Demand 50% upfront cash deposit; require personal guarantor"],
                            ["Capacity", "Does the debtor generate enough cash flow to repay on time?", "6-month audited bank statements, M-Pesa till turnover", "Declining monthly sales turnover, irregular cash flows", "Set conservative credit limit tied to 20% of monthly sales"],
                            ["Capital", "What is the net financial worth and equity of the business?", "Audited balance sheet, asset ownership records", "Highly leveraged business with debt exceeding equity 3:1", "Require co-signature of company directors on credit agreement"],
                            ["Collateral", "What tangible security covers default risk?", "Vehicle logbooks, title deeds, debentures over stock", "Encumbered assets already charged to commercial banks", "Register official legal charge on collateral via Business Registration Service"],
                            ["Conditions", "How do economic and seasonal factors impact repayment?", "Industry sector reports, inflation rate, drought reports", "Severe economic downturn, seasonal crop failure risks", "Shorten credit terms from 60 days to 14 days during volatile periods"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Credit Terms Evaluation and Implied Cost of Forgoing Cash Discounts",
                    "content": {
                        "intro": "Kamau operates a hardware store in Nakuru. He sells construction supplies worth $I = \\text{KES } 200,000$ to contractor Mary on credit terms $\\text{'2/10, net 30'}$. Mary evaluates two payment options:\n- **Option A:** Settle the bill on Day 10 to take advantage of the $2\\%$ cash discount.\n- **Option B:** Settle the full invoice on Day 30 (forgoing the discount to retain cash for 20 extra days).\n\nCalculate the cash savings if Mary chooses Option A, and calculate the Annual Percentage Rate (APR) cost of trade credit if Mary chooses Option B and forgoes the prompt discount.",
                        "steps": [
                            "**Step 1: Given Information:** Invoice amount $I = \\text{KES } 200,000$. Cash discount rate $d = 2\\% = 0.02$. Discount window $= 10\\text{ days}$. Net credit maturity $= 30\\text{ days}$. Days of extended credit $= 30 - 10 = 20\\text{ days}$.",
                            "**Step 2: Formula & Financial Equations:**\n$$\\text{Cash Discount Savings} = I \\times d$$\n$$\\text{Net Settlement Amount (Day 10)} = I - \\text{Cash Discount Savings}$$\n$$\\text{Annual Percentage Rate (APR)} = \\left(\\frac{d}{1 - d}\\right) \\times \\left(\\frac{365}{\\text{Net Days} - \\text{Discount Days}}\\right) \\times 100$$",
                            "**Step 3: Substitution:**\n$$\\text{Cash Discount Savings} = 200,000 \\times 0.02$$\n$$\\text{Net Settlement Amount (Day 10)} = 200,000 - 4,000$$\n$$\\text{APR} = \\left(\\frac{0.02}{1 - 0.02}\\right) \\times \\left(\\frac{365}{30 - 10}\\right) \\times 100$$",
                            "**Step 4: Calculation:**\n$$\\text{Cash Discount Savings} = \\text{KES } 4,000$$\n$$\\text{Net Settlement Amount (Day 10)} = \\text{KES } 196,000$$\n$$\\text{APR} = \\left(\\frac{0.02}{0.98}\\right) \\times \\left(\\frac{365}{20}\\right) \\times 100 = 0.020408 \\times 18.25 \\times 100 = 37.24\\%$$",
                            "**Step 5: Final Answer & Unit Verification:** Under Option A, Mary saves $\\text{KES } 4,000$, paying only $\\text{KES } 196,000$. If Mary chooses Option B, the implied annual financing cost of holding the money for 20 extra days is $37.24\\%\\text{ per annum}$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Forgoing a $2\\%$ discount to delay payment by $20\\text{ days}$ is economically equivalent to borrowing money at an exorbitant $37.24\\%$ annual interest rate. A rational business should borrow from a commercial bank at $14\\%$ interest to pay suppliers on Day 10, pocketing the net savings. *Common Pitfall:* Assuming a $2\\%$ discount is negligible, ignoring the compounding effect across multiple $20\\text{-day}$ cycles in a financial year."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Kamau Construction Supplies in Nakuru",
                    "content": {
                        "title": "Overcoming the Debtor Trap through Credit Limits and CRB Verification",
                        "text": "Kamau operated 'Kamau Construction Supplies' in Nakuru, supplying cement, timber, and iron sheets to local contractors. Eager to expand market share, Kamau offered credit to anyone who requested it on informal verbal promises. Within eighteen months, outstanding debtors accumulated to KES 3.8 million, of which KES 1.2 million became uncollectible bad debts when two rogue contractors dissolved their unregistered firms. Kamau faced a severe liquidity crunch and could no longer restock cement. He restructured his credit management policy: (1) Instituting mandatory CRB background checks, (2) Requiring signed formal credit contracts with collateral charges for invoices over KES 100,000, (3) Offering '2/10, net 30' discount terms to incentivize early payment, and (4) Enforcing a strict 30-day accounts receivable aging review. Within one year, overdue debt dropped by 82% and bad debts fell below 1.5% of turnover."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Credit Transactions, Debtors, and the 5 Cs of Credit",
                    "content": {
                        "title": "Managing Commercial Credit, Invoices, Debtors, and Cash Discount Terms",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Comprehensive tutorial on credit transactions, trade credit appraisal using the 5 Cs, invoice terms (2/10, net 30), and accounts receivable management."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Balance Sheet Classification of Debtors and Creditors",
                    "content": {
                        "question": "An agrochemical dealer in Kitale sells fertilizer worth KES 150,000 on credit to a local maize cooperative and purchases pesticide worth KES 90,000 on credit from a chemical manufacturer. How are the cooperative and the chemical manufacturer classified on the dealer's balance sheet?",
                        "options": [
                            "Cooperative is a Creditor (Liability); Manufacturer is a Debtor (Asset)",
                            "Cooperative is a Debtor (Current Asset); Manufacturer is a Creditor (Current Liability)",
                            "Both are classified as Non-Current Fixed Assets",
                            "Both are classified as Owner's Equity additions"
                        ],
                        "correct": "B",
                        "explanation": "The cooperative owes money to the business for goods received, making them a Debtor (Current Asset / Accounts Receivable). The manufacturer is owed money by the business for goods supplied, making them a Creditor (Current Liability / Accounts Payable)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Decision Making on Supplier Credit Terms",
                    "content": {
                        "question": "A wholesale distributor in Nyeri offers a retailer credit terms of '3/10, net 45' on an invoice of KES 500,000. If the retailer has access to a bank overdraft facility charging 14% annual interest, what is the most profitable financial decision for the retailer?",
                        "options": [
                            "Pay on Day 45 to hold onto cash as long as possible regardless of the discount",
                            "Borrow on the 14% bank overdraft to pay on Day 10, because the implied cost of forgoing the 3% discount (32.18% APR) is far higher than the bank borrowing rate",
                            "Refuse the goods and cancel the order",
                            "Pay on Day 60 and incur late penalty interest charges"
                        ],
                        "correct": "B",
                        "explanation": "The implied annual cost of forgoing the 3% discount for 35 extra days (45 - 10) is: (0.03 / 0.97) × (365 / 35) × 100 = 32.25% APR. Since borrowing from the bank costs only 14% APR, borrowing to pay on Day 10 saves 18.25% in net financing costs."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Definition of Credit Transaction:** Immediate physical exchange of goods/services with financial settlement deferred to a specified future maturity date.\n2. **Assets vs. Liabilities:** Debtors (customers who owe the firm) are Current Assets; Creditors (suppliers owed by the firm) are Current Liabilities.\n3. **The 5 Cs of Credit Appraisal:** Character, Capacity, Capital, Collateral, and Conditions must be evaluated before granting trade credit to mitigate default risk.\n4. **Credit Terms Mathematics:** Terms like '2/10, net 30' carry an implied APR cost of 37.24% if discounts are forgone; smart businesses settle early to capture cash discounts."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Payment Methods in Transactions
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Payment Methods in Transactions",
        "unit_description": "Comprehensive taxonomy of commercial settlement channels in Kenya: physical currency, cheques, mobile money (M-Pesa/Airtel), EFT, RTGS, PesaLink, and debit/credit cards, analyzing speed, cost, security, and transaction ceilings.",
        "lesson_title": "Payment Methods in Transactions",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Kenyan Currency Banknotes and Coins",
                    "content": {
                        "title": "Legal Tender and Settlement Instruments in Kenya",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Kenyan_currency.jpg",
                        "caption": "Kenyan shilling banknotes and coins alongside modern electronic payment channels regulating national commercial exchange.",
                        "author": "Ephymbaya",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify the 6 major payment instruments used in Kenyan commerce (Cash, Cheques, Mobile Money, EFT, RTGS, Cards)\n- Compare payment channels on velocity, settlement risk, transaction costs, and legal enforceability\n- Explain the operational distinction between batch processing (EFT) and instant settlement (RTGS / PesaLink)\n- Calculate transaction fee structures and total cost of payment settlement across different channels"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Commercial Payment Instruments and Settlement Systems",
                    "content": {
                        "term": "Payment Method",
                        "definition": "A legally recognized mechanism, instrument, or channel through which monetary value is transferred from a payer to a payee to discharge a financial obligation arising from a business transaction."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Vehicle Analogy & Key Payment Rails",
                    "content": {
                        "text": "Choosing a payment method is like choosing a vehicle for transportation:\n\n- **Walking (Physical Cash):** Ideal for tiny distances (micro-purchases under KES 1,000 like matatu fare or buying vegetables), but exhausting and dangerous for carrying millions of shillings.\n- **Motorbike / Personal Car (Mobile Money & Debit Cards):** Fast, flexible, and convenient for daily medium-value transactions (KES 1,000 to KES 250,000) with instant confirmation.\n- **Commercial Cargo Airplane / Train (EFT & RTGS Bank Transfers):** Essential for moving heavy, high-value freight across long distances. Bank rails provide secure, legally binding, multi-million shilling settlements backed by the Central Bank of Kenya (CBK).\n\nKey Commercial Payment Rails in Kenya:\n- **Cheques:** Written, signed orders directing a bank (drawee) to pay a stated sum from the account holder's balance (drawer) to a named entity (payee). Requires 2–3 clearing days.\n- **EFT (Electronic Funds Transfer):** Automated inter-bank batch clearing processed within 24 to 48 hours (cost-effective for bulk employee salaries).\n- **RTGS (Real Time Gross Settlement):** High-value, real-time gross settlement system operated by CBK; mandatory for individual payments of KES 1,000,000 and above."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Payment Methods Taxonomy & Strategic Selection Matrix",
                    "content": {
                        "title": "Comprehensive Payment Rail Architecture and Evaluation Criteria",
                        "caption": "High-precision vector diagram illustrating the 6 major Kenyan payment channels, speed vs. risk matrices, fee structures, and Central Bank of Kenya settlement thresholds.",
                        "svg_content": SVG_PAYMENT_METHODS_TAXONOMY_AND_TRADE_OFFS
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Central Bank of Kenya (CBK) Regulatory Guidelines",
                    "content": {
                        "text": "The Central Bank of Kenya regulates commercial payment rails to safeguard national financial stability:\n\n1. **The KES 1,000,000 RTGS Rule:** Commercial banks are legally prohibited from processing single paper cheques or electronic EFTs exceeding KES 1,000,000 through the automated clearinghouse. All transactions of KES 1,000,000 and above must be settled via the Kenya National Payments System (KNPS) RTGS rail to eliminate inter-bank credit risk.\n2. **Mobile Money Caps:** The CBK caps individual mobile wallet transactions at KES 250,000 per transaction and KES 500,000 daily aggregate to combat money laundering and terrorist financing."
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Comprehensive Comparison Matrix of Commercial Payment Channels in Kenya",
                    "content": {
                        "headers": ["Payment Instrument", "Clearing Speed", "Default / Fraud Risk", "Fee Structure", "Transaction Limit / Scope", "Optimal Commercial Application"],
                        "rows": [
                            ["Physical Currency", "Instantaneous (Spot)", "High (Armed robbery, theft, counterfeits)", "Nil direct transaction fee (cash handling costs apply)", "Micro-amounts (< KES 2,000)", "Street vending, matatu fares, kiosk snacks"],
                            ["Mobile Money (Till / Paybill)", "Instantaneous (Real-time 24/7)", "Medium (SIM swap fraud, wrong recipient)", "Tiered tariff (0.5% to 1.5% merchant discount)", "Up to KES 250,000 per tx (KES 500k/day)", "Retail store checkouts, restaurant dining, MSME supplies"],
                            ["Commercial Cheque", "Slow (2 to 3 clearing business days)", "Medium-High (Bounced cheques, signature forgery)", "Low (Cheque leaf fee KES 20 to 50)", "Customarily < KES 1,000,000", "School fees, commercial rent, factory supplies"],
                            ["EFT (Electronic Transfer)", "Moderate (24 to 48 hours batch)", "Very Low (Bank automated files)", "Low flat batch fee (KES 50 to 150)", "Standard batch < KES 1,000,000", "Monthly staff salaries, routine vendor settlements"],
                            ["RTGS (Kenya Payments)", "Real-Time (Gross instant settlement)", "Nil (CBK-backed, irreversible finality)", "Flat premium fee (KES 500 to 1,000)", "Mandatory for >= KES 1,000,000", "Commercial real estate, heavy machinery import, tenders"],
                            ["Debit / Credit Cards (POS)", "Instantaneous authorization", "Low-Medium (Card skimming, chargebacks)", "1.5% to 3.0% Merchant Discount Rate (MDR)", "Capped by cardholder bank limit", "Supermarkets, luxury hotels, online e-commerce"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Strategic Payment Method Optimization and Cost Analysis",
                    "content": {
                        "intro": "Wekesa operates a commercial poultry enterprise in Bungoma. At the end of the month, he must execute three commercial disbursements:\n1. **Disbursement 1 (Payroll):** Pay monthly wages to 15 farmhands totaling $\\text{KES } 180,000$ (average KES 12,000 each). Options: (a) Individual B2C M-Pesa transfers at $\\text{KES } 55\\text{ fee per transfer}$, or (b) A single automated bank batch EFT at a flat fee of $\\text{KES } 150$.\n2. **Disbursement 2 (Feed Supplier):** Settle a routine feed supplier invoice of $\\text{KES } 250,000$. Options: (a) Crossed bank Cheque costing $\\text{KES } 30\\text{ leaf fee}$, or (b) Mobile Paybill at a $0.5\\%$ merchant tariff.\n3. **Disbursement 3 (Machinery Import):** Pay an industrial incubator manufacturer in Mombasa $\\text{KES } 2,400,000$. Options: (a) RTGS bank transfer at flat $\\text{KES } 750$, or (b) 10 multiple split M-Pesa transactions at $\\text{KES } 108\\text{ fee each}$.\n\nCalculate the most cost-effective and legally compliant payment method for each disbursement, determine the total settlement fees incurred, and calculate total enterprise savings compared to suboptimal choices.",
                        "steps": [
                            "**Step 1: Given Information:** Disbursement 1: $15\\text{ staff}$, total $\\text{KES } 180,000$. Option 1a fee $= 15 \\times 55$; Option 1b fee $= \\text{KES } 150$. Disbursement 2: $\\text{KES } 250,000$. Option 2a fee $= \\text{KES } 30$; Option 2b fee $= 250,000 \\times 0.005$. Disbursement 3: $\\text{KES } 2,400,000$ (Exceeds $\\text{KES } 1,000,000$ threshold). Option 3a (RTGS) fee $= \\text{KES } 750$; Option 3b (10 M-Pesa splits) fee $= 10 \\times 108 = \\text{KES } 1,080$ (and legally restricted).",
                            "**Step 2: Formula & Decision Rules:**\n$$\\text{Cost}_{1a} = N_{\\text{staff}} \\times \\text{Fee}_{\\text{M-Pesa}} \\quad \\text{vs.} \\quad \\text{Cost}_{1b} = \\text{Flat EFT Fee}$$\n$$\\text{Cost}_{2a} = \\text{Cheque Leaf Fee} \\quad \\text{vs.} \\quad \\text{Cost}_{2b} = \\text{Invoice Value} \\times 0.5\\%$$\n$$\\text{Cost}_{3a} = \\text{RTGS Fee} \\quad \\text{vs.} \\quad \\text{Cost}_{3b} = N_{\\text{splits}} \\times \\text{Fee}_{\\text{M-Pesa}}$$\n$$\\text{Total Optimized Cost} = \\min(\\text{Cost}_1) + \\min(\\text{Cost}_2) + \\text{Cost}_{3a}$$\n$$\\text{Enterprise Savings} = \\text{Suboptimal Total} - \\text{Optimized Total}$$",
                            "**Step 3: Substitution:**\n$$\\text{Cost}_{1a} = 15 \\times 55 = \\text{KES } 825 \\quad \\text{vs.} \\quad \\text{Cost}_{1b} = \\text{KES } 150$$\n$$\\text{Cost}_{2a} = \\text{KES } 30 \\quad \\text{vs.} \\quad \\text{Cost}_{2b} = 250,000 \\times 0.005 = \\text{KES } 1,250$$\n$$\\text{Cost}_{3a} = \\text{KES } 750 \\quad \\text{vs.} \\quad \\text{Cost}_{3b} = 10 \\times 108 = \\text{KES } 1,080$$",
                            "**Step 4: Calculation:**\n- Disbursement 1: Select Bank EFT (Cost: $\\text{KES } 150$, saving $\\text{KES } 675$).\n- Disbursement 2: Select Crossed Cheque (Cost: $\\text{KES } 30$, saving $\\text{KES } 1,220$).\n- Disbursement 3: Select RTGS Transfer (Cost: $\\text{KES } 750$, saving $\\text{KES } 330$ + $100\\%$ legally compliant with CBK rules).\n$$\\text{Optimized Total Fees} = 150 + 30 + 750 = \\text{KES } 930$$\n$$\\text{Suboptimal Total Fees} = 825 + 1,250 + 1,080 = \\text{KES } 3,155$$\n$$\\text{Total Enterprise Savings} = 3,155 - 930 = \\text{KES } 2,225$$",
                            "**Step 5: Final Answer & Unit Verification:** The optimized payment channels are: Disbursement 1 via Bank EFT ($\\text{KES } 150$), Disbursement 2 via Crossed Cheque ($\\text{KES } 30$), and Disbursement 3 via RTGS Transfer ($\\text{KES } 750$). Total optimized fees equal $\\text{KES } 930$, generating $\\text{KES } 2,225$ in monthly transaction fee savings.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Matching the payment instrument to the transaction size and recipient profile yields substantial recurring operational cost savings ($\\text{KES } 2,225\\text{ monthly}$). For payments exceeding $\\text{KES } 1,000,000$, RTGS is not merely cheaper—it is legally mandatory under Central Bank of Kenya prudential regulations. *Common Pitfall:* Defaulting to mobile money for high-value business procurement or payroll, incurring high tiered fees and hitting daily transfer ceilings."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Wekesa Poultry Farm in Bungoma",
                    "content": {
                        "title": "Optimizing Multi-Channel Commercial Payment Rails",
                        "text": "Wekesa Poultry Farm in Bungoma grew from a small backyard coop of 200 chickens into a commercial supplier processing 5,000 broilers weekly. Initially, Wekesa paid staff wages in physical cash, settled feed suppliers via multiple mobile money transfers, and accepted paper cheques from unvetted retail buyers. This haphazard approach resulted in a bounced cheque loss of KES 140,000, KES 52,000 in unnecessary mobile money transaction fees, and 4 hours lost every Friday counting wage envelopes. Wekesa streamlined his payment architecture: (1) Integrating Lipa Na M-Pesa Buy Goods Till for retail chicken sales, (2) Routing monthly staff payroll through a consolidated bank batch EFT file, (3) Requiring direct bank RTGS transfers for wholesale hotel orders exceeding KES 1,000,000, and (4) Settling routine supplier invoices with crossed order cheques. This structured policy reduced monthly payment processing costs by 70% and eliminated settlement default losses."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Payment Methods: Cash, Cheques, Mobile Money, EFT, RTGS",
                    "content": {
                        "title": "Understanding Modern Payment Methods, Clearing Systems, and CBK Regulations",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Comprehensive visual breakdown of commercial payment methods in Kenya, analyzing transaction speed, costs, fraud security, and clearing mechanisms."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Mandatory Clearing Rails for High-Value Transactions",
                    "content": {
                        "question": "A coffee milling enterprise in Nyeri is purchasing a piece of commercial real estate worth KES 4,500,000. Under Central Bank of Kenya (CBK) clearing rules, which payment method must be used to ensure immediate, gross, and irreversible settlement?",
                        "options": [
                            "Writing 5 separate paper cheques of KES 900,000 each",
                            "Real Time Gross Settlement (RTGS)",
                            "Splitting the payment into 18 mobile money transfers",
                            "Delivering 45 bundles of physical KES 1,000 banknotes in a briefcase"
                        ],
                        "correct": "B",
                        "explanation": "Under Central Bank of Kenya regulations, single transactions of KES 1,000,000 and above must be processed via Real Time Gross Settlement (RTGS) to guarantee instantaneous, gross, and legally irreversible settlement without clearing delays."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Efficiency in Enterprise Payroll Disbursement",
                    "content": {
                        "question": "A tea packaging factory in Kericho employs 120 permanent workers. Which payment method provides the highest security, lowest per-person transaction cost, and most verifiable electronic audit trail for monthly salary disbursement?",
                        "options": [
                            "Withdrawing KES 1.8 million in physical cash and distributing paper envelopes",
                            "Processing an automated bank batch Electronic Funds Transfer (EFT) directly to employee bank accounts",
                            "Writing 120 individual uncrossed bearer cheques",
                            "Sending individual mobile money transfers with daily split limits"
                        ],
                        "correct": "B",
                        "explanation": "Bank batch EFT enables the enterprise to upload a single encrypted payroll schedule to its commercial bank, disbursing salaries to 120 workers simultaneously for a single low flat fee, eliminating armed robbery risks and generating an automated audit trail."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Payment Methods Spectrum:** Modern commerce utilizes physical cash, mobile money, cheques, EFT batch files, RTGS transfers, and card POS terminals.\n2. **Selection Criteria:** The optimal payment method depends on transaction value, settlement velocity, fraud risk, fee structure, and legal ceilings.\n3. **CBK Regulatory Thresholds:** Single payments of KES 1,000,000 and above require mandatory RTGS clearance; mobile wallets are capped at KES 250,000 per transaction.\n4. **Cost Optimization:** Enterprises save substantial operational capital by deploying batch EFT for payroll and crossed cheques for suppliers rather than incurring high tiered mobile fees on large balances."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Practical Project: Managing Business Payments
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Practical Project: Managing Business Payments",
        "unit_description": "Practical design and implementation of enterprise payment policies, cash flow segmentation (inflows vs outflows), internal cash controls, petty cash management, and bank reconciliation.",
        "lesson_title": "Practical Project: Managing Business Payments",
        "pages": [
            # Card 1: Photographic Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Enterprise Bookkeeping and Financial Data Analysis",
                    "content": {
                        "title": "Practical Payment Management and Financial Controls",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
                        "caption": "A financial administrator preparing payment reconciliations, expense vouchers, and bank statements for a growing enterprise.",
                        "author": "Dave Dugdale",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Formulate a 3-step Enterprise Payment Policy balancing customer convenience, transaction fees, and cash security\n- Segment enterprise cash flows into Inflows (revenue collection) and Outflows (procurement, expenses, wages)\n- Implement the Imprest Petty Cash System with standard voucher controls for micro-expenses\n- Prepare a cash flow reconciliation verifying physical cash against digital till and bank statements"
                    }
                }
            ],
            # Card 2: Formal Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Enterprise Payment Policy and Internal Controls",
                    "content": {
                        "term": "Business Payment Policy",
                        "definition": "A formalized set of operational rules and controls established by enterprise management detailing approved payment instruments for customer revenue collection, supplier disbursements, debt settlement, and cash handling procedures."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "Highway Tollgate Analogy & Imprest Petty Cash",
                    "content": {
                        "text": "Managing enterprise payments without a formal policy is like operating an open highway without toll booths—cash leaks in every direction:\n\n- **Highway Tollgate Analogy:** A well-designed payment policy sets up designated lanes: high-speed cashless electronic lanes for regular traffic (Mobile Till/M-Pesa), monitored gates for heavy commercial trucks (EFT/Cheques), and an emergency booth with exact coin logs (Imprest Petty Cash).\n- **Inflows vs. Outflows:** Inflows represent revenue entering the firm (sales, debtor collections); Outflows represent disbursements leaving the firm (procurement, wages, rent).\n- **Petty Cash Imprest System:** A small fixed cash fund (the 'float', e.g. KES 5,000) maintained in a locked box to pay minor incidental expenses (baking soda, tea milk, delivery rider). Every expense requires a signed **Petty Cash Voucher** with an attached receipt.\n- **Golden Imprest Rule:** The reimbursement amount drawn to restore the fund is *always exactly equal* to the total sum of valid expense vouchers submitted."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Enterprise Payment Policy & Petty Cash Imprest Architecture",
                    "content": {
                        "title": "3-Tier Payment Policy Design and Imprest Reconciliation Cycle",
                        "caption": "High-precision vector diagram illustrating the Baraka Bakery 3-tier payment framework, inflow/outflow separation, and the 4-step Imprest Petty Cash reconciliation loop.",
                        "svg_content": SVG_ENTERPRISE_PAYMENT_POLICY_ARCHITECTURE
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The 3 Steps to Formulating an Enterprise Payment Policy",
                    "content": {
                        "text": "Every enterprise should execute three structured steps to establish a resilient payment policy:\n\n1. **Step 1: Cash Flow Segmentation:** Map all incoming customer revenue streams (Inflows) and outgoing vendor/operational expenditures (Outflows).\n2. **Step 2: Payment Rail Matching:** Assign the safest, most cost-effective payment channel to each transaction tier based on transaction value and speed requirements.\n3. **Step 3: Internal Control Rules & Segregation of Duties:** Institute mandatory authorization rules—for example, requiring dual signatures on cheques above KES 5,000, enforcing daily mobile till reconciliations, and segregating cash handling from accounting ledger entry."
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Baraka Bakery Enterprise Payment Policy Framework",
                    "content": {
                        "headers": ["Transaction Category", "Payment Rail / Channel", "Approved Limit / Threshold", "Mandatory Source Document", "Internal Control & Authorization Rule"],
                        "rows": [
                            ["Student Scone Sales (Inflow)", "Lipa Na M-Pesa Buy Goods Till", "KES 20 to KES 500 per sale", "Automated SMS Till Receipt / POS Slip", "Daily closing till balance reconciled against physical scone count"],
                            ["Over-the-Counter Coin Sales", "Physical Cash Locked Box", "Micro-purchases < KES 100 only", "Manual Cash Counter Receipt", "Cashier daily sign-off; cash deposited into till wallet at 4:00 PM"],
                            ["Bulk Flour & Sugar Wholesale", "Bank Electronic Funds Transfer (EFT)", "Invoices >= KES 5,000", "Supplier Invoice & Delivery Note", "Dual authorization required (Project Manager + Treasurer signatures)"],
                            ["Casual Labour & Cleaning", "Mobile Money B2C / Paybill", "KES 200 to KES 1,000 per shift", "Signed Casual Wage Voucher", "Authorized by Bakery Supervisor upon shift completion verification"],
                            ["Incidental Repairs & Baking Yeast", "Imprest Petty Cash Fund", "Micro-expenses <= KES 500", "Numbered Petty Cash Voucher + Receipt", "Disbursed by Petty Cashier; reimbursed weekly to fixed KES 5,000 float"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Imprest Petty Cash Fund Audit and Replenishment Calculation",
                    "content": {
                        "intro": "Baraka Bakery establishes an Imprest Petty Cash Fund with a fixed float of $F = \\text{KES } 5,000$ on 1st August. During the first two weeks of commercial operations, the petty cashier disburses the following authorized voucher expenses:\n- Aug 3 (Voucher 01): Baking powder and vanilla essence $=\\text{KES } 650$\n- Aug 6 (Voucher 02): Boda-boda delivery of packaging cartons $=\\text{KES } 400$\n- Aug 9 (Voucher 03): Kitchen cleaning detergent and sponges $=\\text{KES } 750$\n- Aug 12 (Voucher 04): Emergency replacement of electric oven fuse $=\\text{KES } 900$\n- Aug 14 (Voucher 05): Drinking water for bakery kitchen staff $=\\text{KES } 300$\n\nOn 15th August, the project supervisor conducts a petty cash audit. The physical cash remaining in the lockbox is $C_{\\text{actual}} = \\text{KES } 2,000$.\nCalculate the total voucher expenditure, verify whether any cash discrepancy (shortage or overage) exists, and determine the exact reimbursement cheque amount required to restore the fund to its fixed float.",
                        "steps": [
                            "**Step 1: Given Information:** Fixed float $F = \\text{KES } 5,000$. Disbursed vouchers: $v_1 = \\text{KES } 650$, $v_2 = \\text{KES } 400$, $v_3 = \\text{KES } 750$, $v_4 = \\text{KES } 900$, $v_5 = \\text{KES } 300$. Actual physical cash counted in box $C_{\\text{actual}} = \\text{KES } 2,000$.",
                            "**Step 2: Formula & Accounting Rules:**\n$$\\text{Total Vouchers Disbursed } (V) = \\sum_{i=1}^{n} v_i$$\n$$\\text{Expected Cash Remaining } (C_{\\text{expected}}) = F - V$$\n$$\\text{Cash Discrepancy} = C_{\\text{actual}} - C_{\\text{expected}}$$\n$$\\text{Reimbursement Cheque Amount} = V = F - C_{\\text{actual}}$$",
                            "**Step 3: Substitution:**\n$$V = 650 + 400 + 750 + 900 + 300$$\n$$C_{\\text{expected}} = 5,000 - V$$\n$$\\text{Cash Discrepancy} = 2,000 - C_{\\text{expected}}$$\n$$\\text{Reimbursement Cheque Amount} = V$$",
                            "**Step 4: Calculation:**\n$$V = \\text{KES } 3,000$$\n$$C_{\\text{expected}} = 5,000 - 3,000 = \\text{KES } 2,000$$\n$$\\text{Cash Discrepancy} = 2,000 - 2,000 = \\text{KES } 0 \\quad (\\text{Perfect Reconciliation / Zero Shortage})$$\n$$\\text{Reimbursement Cheque Amount} = \\text{KES } 3,000$$",
                            "**Step 5: Final Answer & Unit Verification:** Total vouchers disbursed equal $\\text{KES } 3,000$. The expected cash matches the physical cash count exactly at $\\text{KES } 2,000$ (zero shortage). The reimbursement cheque drawn on the main bank account is $\\text{KES } 3,000$, restoring the petty cash box to its fixed float of $\\text{KES } 5,000$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Under the Imprest System, the reimbursement cheque is ALWAYS exactly equal to the sum of valid vouchers spent ($\\text{KES } 3,000$). This mechanism guarantees that the total of (Physical Cash + Signed Vouchers) constantly equals the fixed float ($\\text{KES } 2,000 + \\text{KES } 3,000 = \\text{KES } 5,000$), providing an airtight internal control against cash leakage. *Common Pitfall:* Requesting an arbitrary reimbursement sum (e.g. $\\text{KES } 5,000$) rather than the exact voucher total of $\\text{KES } 3,000$, which would distort cash balances."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Baraka Youth Bakery Project in Kiambu",
                    "content": {
                        "title": "Implementing Internal Cash Controls in a Student-Led Micro-Enterprise",
                        "text": "At Amani High School in Kiambu, the Grade 10 Business Studies class launched 'Baraka Bakery' to bake and sell fresh scones to 800 students during morning break. During the first two weeks, sales revenue was collected in a plastic biscuit tin. By day 10, the project treasurer discovered a KES 4,200 deficit between expected sales and physical coins, while two receipts for emergency yeast purchases were lost. The class convened to draft a formal Enterprise Payment Policy: (1) Adopting a Safaricom Lipa Na M-Pesa Buy Goods Till for student scone purchases, (2) Limiting coin sales to a locked cash box managed by an elected daily cashier, (3) Instituting a KES 5,000 Imprest Petty Cash Fund with numbered vouchers for baking additives, and (4) Routing bulk flour procurement through bank EFT requiring dual signatures from the class President and Treasurer. Over the subsequent term, cash discrepancies dropped to zero, and the bakery generated KES 45,000 in net profit."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Internal Cash Controls, Petty Cash Imprest System, and Payment Policies",
                    "content": {
                        "title": "Designing Business Payment Policies, Imprest Petty Cash, and Internal Controls",
                        "youtube_id": "qJ7v37s9yHk",
                        "url": "https://www.youtube.com/watch?v=qJ7v37s9yHk",
                        "description": "Practical educational video on designing enterprise payment policies, implementing the petty cash imprest system, and enforcing segregation of duties."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: The Imprest Petty Cash Replenishment Mechanism",
                    "content": {
                        "question": "A poultry enterprise maintains an Imprest Petty Cash Fund with a fixed float of KES 8,000. At the end of the month, the petty cashier has KES 2,500 in physical cash remaining and KES 5,500 in authorized expense vouchers. How much should the main cashier disburse to reimburse the fund?",
                        "options": [
                            "KES 8,000",
                            "KES 2,500",
                            "KES 5,500",
                            "KES 10,500"
                        ],
                        "correct": "C",
                        "explanation": "Under the Imprest System, the reimbursement is always exactly equal to the total sum of authorized vouchers spent (KES 5,500). Adding KES 5,500 to the remaining KES 2,500 restores the fund precisely to its fixed float of KES 8,000."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Segregation of Duties in Cash Management",
                    "content": {
                        "question": "To prevent fraud and employee misappropriation in a retail supermarket in Machakos, which internal control procedure is most critical regarding cash management?",
                        "options": [
                            "Allowing the head cashier to record entries in the general accounting ledger and perform the monthly bank reconciliation alone",
                            "Enforcing strict segregation of duties so that the person handling physical cash at the till is separate from the person maintaining financial ledger records",
                            "Eliminating all source receipts and relying exclusively on verbal trust",
                            "Storing all daily cash proceeds in an unlocked drawer accessible to all sales staff"
                        ],
                        "correct": "B",
                        "explanation": "Segregation of duties ensures that no single employee has end-to-end control over cash handling and financial recordkeeping. Separating physical cash custody from accounting entries prevents unauthorized misappropriation and falsification of records."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **Payment Policy Purpose:** Establishes operational rules matching transaction values to secure payment channels, preventing theft and minimizing fees.\n2. **Inflow vs. Outflow Separation:** Channels customer revenue through digital till wallets and routes supplier procurement through bank transfers or cheques.\n3. **Imprest Petty Cash System:** Operates on a fixed float where periodic reimbursement exactly equals the sum of authorized vouchers spent, maintaining an airtight audit trail.\n4. **Internal Control Imperative:** Segregation of duties between cash handlers and accounting recordkeepers is vital for preventing fraud and ensuring enterprise sustainability."
                    }
                }
            ]
        ]
    }
]
