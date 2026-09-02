"""
VLearn CBC Grade 10 Business Studies — Topic 15: Source Documents and Books of Original Entry
Full Structured Lesson Card Definitions (Lessons 1 to 6)
"""

from curriculum.cbc_grade10_business_studies_topic15_svgs import (
    SVG_SOURCE_DOCUMENT_AUDIT_TRAIL,
    SVG_CORE_SOURCE_DOCUMENTS_TAXONOMY,
    SVG_SUBSIDIARY_DAY_BOOKS_FILTER,
    SVG_CASH_BOOK_AND_CONTRA_ENTRIES,
    SVG_BATCH_RECORDING_TO_LEDGER_PIPELINE,
    SVG_ERROR_CLASSIFICATION_AND_CORRECTION_MATRIX
)

TOPIC_15_LESSONS = [
    # =========================================================================
    # LESSON 1: Importance and Verification of Source Documents
    # =========================================================================
    {
        "unit_order": 1,
        "unit_name": "Importance and Verification of Source Documents",
        "unit_description": "Conceptual foundations of source documents as primary transaction evidence, audit trails, the 5 pillars of bookkeeping, and the 6-point verification protocol before journal recording.",
        "lesson_title": "Importance and Verification of Source Documents",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Accounting Workstation and Source Document Verification",
                    "content": {
                        "title": "Accounting Desk and Transaction Records",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg",
                        "caption": "Financial ledgers, source documents, and verification desk setups illustrating the rigorous systematic audit trail needed in commercial enterprises.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 1 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define bookkeeping, source documents, and financial audit trails in commercial practice\n- Explain the 'Footprints in the Mud' analogy regarding primary accounting evidence\n- Analyze the 5 primary pillars explaining why verified source documents are essential\n- Apply the 6-point verification protocol to inspect incoming and outgoing business documents before entry"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Source Documents, Verification, and Audit Trails",
                    "content": {
                        "term": "Source Document",
                        "definition": "A physical or electronic document that serves as the original, primary, and legally binding evidence that a commercial transaction actually occurred."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Footprints in the Mud Analogy & 5 Pillars",
                    "content": {
                        "text": "Every single shilling that moves through an enterprise must leave an undeniable trace:\n\n- **Footprints in the Mud:** Walking across a wet farm in Kericho leaves clear footprints showing origin, path, and direction. A source document is the financial footprint of a commercial event. Trading without source documents is like walking on solid rock—leaving no trace and making fraud or errors impossible to investigate.\n- **Audit Trail:** The chronological step-by-step chain of evidence connecting a final figure on a balance sheet back to the exact physical counterparty receipt or invoice.\n- **The 5 Pillars of Bookkeeping:** (1) Indisputable written proof of trade; (2) Objective basis for journalizing (never record from human memory); (3) Reduction of arithmetic and transposition errors; (4) Clear evidence for Kenya Revenue Authority (KRA) tax compliance; (5) Reliable data for strategic enterprise decision-making."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "The Accounting Pipeline and Source Document Audit Trail",
                    "content": {
                        "title": "From Economic Transaction to Legal & Tax Audit Trail",
                        "caption": "High-precision vector pipeline showing the flow from economic transaction to source document generation, 6-point verification, day book recording, and ledger auditability.",
                        "svg_content": SVG_SOURCE_DOCUMENT_AUDIT_TRAIL
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Source Document 6-Point Verification Checklist & Risk Matrix",
                    "content": {
                        "headers": ["Verification Checkpoint", "Action Required by Bookkeeper", "Risk Prevented", "Severe Consequence of Neglecting Check"],
                        "rows": [
                            ["1. Transaction Date", "Confirm date falls within current accounting period", "Recording stale or future-dated transactions", "Distorted monthly profits and VAT filing mismatches"],
                            ["2. Sequential Serial No.", "Check for unique, unrepeated document serial number", "Duplicate entry of the same supplier invoice", "Paying a supplier twice for a single delivery"],
                            ["3. Counterparty Details", "Verify correct legal trading name and PIN of buyer/seller", "Recording invoices meant for a different business entity", "Invalid tax claims and disallowed business expenses by KRA"],
                            ["4. Item Description & Qty", "Match items against physical Delivery Notes & LPOs", "Billing for phantom goods or incorrect specifications", "Inventory ledger discrepancies and unaccounted stock loss"],
                            ["5. Arithmetic Accuracy", "Re-calculate: (Quantity x Unit Price) - Discount + VAT", "Vendor arithmetic errors, incorrect totals, faulty tax math", "Direct financial overpayment or loss of revenue"],
                            ["6. Proper Authorization", "Confirm authorized signature, official stamp, or digital key", "Unapproved staff expenditures and fake payment vouchers", "Internal embezzlement and fraudulent cash disbursement"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Arithmetic Verification of a Bulk Supplier Invoice with Trade Discount & VAT",
                    "content": {
                        "intro": "Waweru Dairies in Limuru receives a purchase invoice from 'Limuru Feed Millers Ltd' for cattle feed supplies. The invoice states: $80\\text{ bags of dairy meal}$ at $\\text{KES } 3,200\\text{ per bag}$, less a $10\\%\\text{ Trade Discount}$, plus $16\\%\\text{ Value Added Tax (VAT)}$. The supplier's printed invoice claims a final payable amount of $\\text{KES } 268,000$. Perform a comprehensive 6-step arithmetic verification check to determine the exact correct invoice total, identify any discrepancy, and formulate the bookkeeper's action.",
                        "steps": [
                            "**Step 1: Given Information:** Quantity $Q = 80\\text{ bags}$. Unit catalogue price $P = \\text{KES } 3,200$. Trade discount rate $TD = 10\\% = 0.10$. Value Added Tax rate $VAT = 16\\% = 0.16$. Supplier's claimed total payable $T_{\\text{claimed}} = \\text{KES } 268,000$.",
                            "**Step 2: Formula & Verification Rules:**\n$$\\text{Gross Catalogue Amount} = Q \\times P$$\n$$\\text{Trade Discount (TD)} = \\text{Gross Catalogue Amount} \\times TD$$\n$$\\text{Net Invoiced Value} = \\text{Gross Catalogue Amount} - \\text{Trade Discount}$$\n$$\\text{VAT Amount} = \\text{Net Invoiced Value} \\times VAT$$\n$$\\text{Correct Total Payable} = \\text{Net Invoiced Value} + \\text{VAT Amount}$$\n$$\\text{Discrepancy Variance} = T_{\\text{claimed}} - \\text{Correct Total Payable}$$",
                            "**Step 3: Substitution:**\n$$\\text{Gross} = 80 \\times 3,200 = \\text{KES } 256,000$$\n$$\\text{TD} = 256,000 \\times 0.10 = \\text{KES } 25,600$$\n$$\\text{Net} = 256,000 - 25,600 = \\text{KES } 230,400$$\n$$\\text{VAT} = 230,400 \\times 0.16$$\n$$\\text{Variance} = 268,000 - \\text{Correct Total Payable}$$",
                            "**Step 4: Calculation:**\n$$\\text{Gross Amount} = \\text{KES } 256,000$$\n$$\\text{Trade Discount} = \\text{KES } 25,600$$\n$$\\text{Net Invoiced Value} = \\text{KES } 230,400$$\n$$\\text{VAT (16\\%)} = 230,400 \\times 0.16 = \\text{KES } 36,864$$\n$$\\text{Correct Total Payable} = 230,400 + 36,864 = \\text{KES } 267,264$$\n$$\\text{Discrepancy Variance} = 268,000 - 267,264 = +\\text{KES } 736\\text{ (Supplier Overcharge)}$$",
                            "**Step 5: Final Answer & Unit:** The verified correct invoice total payable is $\\text{KES } 267,264$. The supplier's printed invoice contains an arithmetic overcharge error of $\\text{KES } 736$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** The bookkeeper must **not** enter the faulty $\\text{KES } 268,000$ in the Purchases Day Book. The bookkeeper must flag the $\\text{KES } 736$ error, reject the document, and request an amended invoice or a Credit Note for KES 736. *Common Pitfall:* Applying the 16% VAT on the gross catalogue price (KES 256,000) rather than on the net price after deducting the trade discount (KES 230,400)."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: The Missing Ksh 50,000 at Kiprop's Hardware in Eldoret",
                    "content": {
                        "title": "Cash Drawer Reconciliation and Physical Audit Trail in Eldoret",
                        "text": "At the close of a busy trading Friday at Kiprop's Hardware in Eldoret, the physical cash drawer contained KES 120,000, yet the computerized POS cash register indicated that KES 170,000 should be present. Rather than guessing or accusing staff, Kiprop initiated a source document audit. By systematically verifying the physical carbon copies of delivery notes, payment vouchers, and cash receipts, the audit revealed two critical facts: (1) A cash sale of 40 bags of cement worth KES 30,000 had been mistakenly entered as a credit invoice, and (2) An authorized payment voucher for KES 20,000 paid to a sand transporter had not been keyed into the electronic register. Physical source documents resolved the entire KES 50,000 discrepancy without commercial loss."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Source Documents and Bookkeeping Verification Fundamentals",
                    "content": {
                        "title": "Understanding Financial Source Documents and Audit Trails",
                        "youtube_id": "W7q_y6Zk9g4",
                        "url": "https://www.youtube.com/watch?v=W7q_y6Zk9g4",
                        "description": "Educational overview of financial source documents, verification techniques, and the construction of reliable bookkeeping audit trails."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Invoice Verification and Entity Recognition",
                    "content": {
                        "question": "A bookkeeper at Waweru Dairies receives a credit invoice from a supplier for cattle feed. The invoice is dated correctly, but the buyer's name is printed as 'Waweru Poultry Farm' (an enterprise owned by Waweru's brother). What is the legally and procedurally correct action for the bookkeeper?",
                        "options": [
                            "Record the invoice immediately in Waweru Dairies' Purchases Day Book since it belongs to a close family member",
                            "Use a correction pen to cross out the brother's farm name, write 'Waweru Dairies', and record the transaction",
                            "Reject the invoice and return it to the supplier for re-issuance with the exact legal business name of Waweru Dairies",
                            "File the invoice in the General Ledger without entering it into any subsidiary day book"
                        ],
                        "correct": "C",
                        "explanation": "A business is a separate legal and accounting entity. Invoices made out to a different enterprise cannot be entered into Waweru Dairies' books or claimed for tax purposes. The supplier must cancel the wrong invoice and issue a fresh one with the correct legal trading entity name."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Audit Trail and Tax Compliance",
                    "content": {
                        "question": "Why does the Kenya Revenue Authority (KRA) require commercial businesses to preserve original source documents for at least five years?",
                        "options": [
                            "To ensure businesses do not run out of scrap paper during annual stocktaking exercises",
                            "To provide an indisputable audit trail verifying that recorded revenues, expenses, and VAT declarations match real transactions",
                            "To enable commercial banks to automatically confiscate excess cash balances at year end",
                            "To prevent businesses from opening multiple bank accounts across different counties"
                        ],
                        "correct": "B",
                        "explanation": "Source documents form the primary evidentiary backbone of the audit trail. Tax authorities and external auditors inspect them to verify that declared sales, deductible expenses, and input/output VAT figures represent genuine, authorized commercial activities."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 1 Summary Takeaways",
                    "content": {
                        "text": "1. **Primary Evidence:** Source documents are the original physical or digital proof of commercial transactions; bookkeeping must never rely on human memory.\n2. **The Audit Trail:** Verified source documents create an unbroken chain connecting summary financial statements back to original trading counterparties.\n3. **6-Point Verification Protocol:** Always verify transaction date, sequential numbering, buyer/seller legal names, item quantities, arithmetic math (price x quantity - discount + VAT), and authorized signatures before recording.\n4. **KRA Compliance:** Preserving verified source documents protects the enterprise against fraud, internal theft, and severe regulatory tax penalties."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 2: Core Source Documents for Buying and Selling
    # =========================================================================
    {
        "unit_order": 2,
        "unit_name": "Core Source Documents for Buying and Selling",
        "unit_description": "Detailed study of commercial source documents: Sales & Purchase Invoices, Cash Receipts, Payment Vouchers, Credit & Debit Notes, Cheque Counterfoils, and their bidirectional accounting effects.",
        "lesson_title": "Core Source Documents for Buying and Selling",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Financial Data and Commercial Transaction Slips",
                    "content": {
                        "title": "Commercial Invoices and Accounting Analysis",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
                        "caption": "Professional analysis of receipts, invoices, and payment vouchers during monthly commercial reconciliation in a Kenyan trading firm.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY 2.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 2 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Differentiate between Sales Invoices and Purchase Invoices from seller vs. buyer perspectives\n- Explain the operational purpose of Cash Receipts and internal Payment Vouchers\n- Contrast Credit Notes (Credit Memos) with Debit Notes (Debit Memos) in managing returns and price adjustments\n- Analyze specimen invoice elements including trade discounts, cash discounts, and credit terms"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Invoices, Receipts, and Credit/Debit Notes",
                    "content": {
                        "term": "Sales Invoice vs. Credit Note",
                        "definition": "A Sales Invoice is a document issued by a seller demanding payment for goods sold on credit; a Credit Note is issued by the seller to reduce the amount owed by the buyer due to returned goods or invoice overcharges."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Transaction ID Cards Analogy & Core Documents",
                    "content": {
                        "text": "Just like citizens carry different identification cards, transactions carry specific document types:\n\n- **Invoices (Credit Trade):** When inventory is traded on credit, the seller issues a **Sales Invoice** (proving credit revenue) while the buyer receives the *identical document* as a **Purchase Invoice** (proving a trade liability).\n- **Cash Receipts & Payment Vouchers (Immediate Cash):** A **Cash Receipt** proves an immediate cash/M-Pesa inflow. An internal **Payment Voucher** must be signed by management before cash is disbursed from the till or petty cash drawer.\n- **Credit Notes vs. Debit Notes (Returns & Corrections):** A **Credit Note** (issued by the seller) informs the buyer that their debt has been *credited (reduced)*. A **Debit Note** is sent by the buyer to formally request a credit note or sent by the seller to correct an accidental undercharge on an earlier invoice."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Taxonomy of Business Source Documents: Roles and Financial Impact",
                    "content": {
                        "title": "Taxonomy of Commercial Source Documents",
                        "caption": "Comprehensive classification map displaying the 4 core document families, issuers, triggers, recipient effects, and destination books of original entry.",
                        "svg_content": SVG_CORE_SOURCE_DOCUMENTS_TAXONOMY
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Master Source Document Comparison Matrix",
                    "content": {
                        "headers": ["Source Document", "Issued By", "Received By", "Commercial Trigger / Purpose", "Primary Destination Book"],
                        "rows": [
                            ["Cash Receipt", "Seller / Payee", "Buyer / Payer", "Immediate settlement via physical cash, cheque, or mobile money", "Cash Book (Debit Side)"],
                            ["Payment Voucher", "Internal Accounts Department", "Cashier / Payee", "Internal authorization before cash or cheque is disbursed for expenses", "Petty Cash Book / Cash Book (Credit)"],
                            ["Sales Invoice", "Seller (Our Business)", "Credit Customer (Debtor)", "Sale of inventory goods on credit terms (request for future payment)", "Sales Day Book (Sales Journal)"],
                            ["Purchase Invoice", "Supplier (Creditor)", "Buyer (Our Business)", "Purchase of inventory goods on credit terms (bill payable in future)", "Purchases Day Book (Purchases Journal)"],
                            ["Credit Note", "Seller", "Buyer", "Goods returned by customer (Returns Inward) or pricing overcharge", "Returns Inward Journal (Sales Returns)"],
                            ["Debit Note", "Buyer (or Seller)", "Seller (or Buyer)", "Goods returned to supplier (Returns Outward) or pricing undercharge", "Returns Outward Journal (Purchases Returns)"],
                            ["Cheque Counterfoil", "Bank (Retained Stub)", "Account Drawer (Our Firm)", "Written record of cheque payment details (date, payee, amount)", "Cash Book (Bank Column Credit)"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Calculating Net Trade Debt, Credit Note Adjustment, and Cash Settlement Discount",
                    "content": {
                        "intro": "Mwangi Retail Shop in Naivasha purchases merchandise from Baraka Wholesalers Ltd. The gross catalogue price is $\\text{KES } 200,000$, subject to a $10\\%\\text{ Trade Discount}$ on the initial sales invoice. Upon delivery, Mwangi discovers that goods worth $\\text{KES } 20,000\\text{ gross}$ are damaged and returns them immediately, receiving Credit Note CN/042. The invoice specifies credit terms of '5/10, net 30' ($5\\%\\text{ Cash Discount}$ if paid within 10 days). Calculate: (1) Initial net invoice value, (2) Net Credit Note adjustment, (3) Revised outstanding balance, (4) Cash discount earned upon prompt settlement within 10 days, and (5) The final cheque payment amount.",
                        "steps": [
                            "**Step 1: Given Information:** Gross invoice price $G = \\text{KES } 200,000$. Trade discount rate $TD = 10\\% = 0.10$. Damaged returns gross value $R_{\\text{gross}} = \\text{KES } 20,000$. Cash discount rate $CD = 5\\% = 0.05$ for payment within 10 days.",
                            "**Step 2: Formula & Accounting Rules:**\n$$\\text{Initial Net Invoice} = G \\times (1 - TD)$$\n$$\\text{Net Credit Note Value} = R_{\\text{gross}} \\times (1 - TD)$$\n$$\\text{Adjusted Debt Outstanding} = \\text{Initial Net Invoice} - \\text{Net Credit Note Value}$$\n$$\\text{Cash Discount Allowed} = \\text{Adjusted Debt Outstanding} \\times CD$$\n$$\\text{Final Net Cheque Payment} = \\text{Adjusted Debt Outstanding} - \\text{Cash Discount Allowed}$$",
                            "**Step 3: Substitution:**\n$$\\text{Initial Net Invoice} = 200,000 \\times (1 - 0.10) = 200,000 \\times 0.90$$\n$$\\text{Net Credit Note} = 20,000 \\times (1 - 0.10) = 20,000 \\times 0.90$$\n$$\\text{Adjusted Debt} = 180,000 - 18,000$$\n$$\\text{Cash Discount} = 162,000 \\times 0.05$$\n$$\\text{Final Cheque} = 162,000 - \\text{Cash Discount}$$",
                            "**Step 4: Calculation:**\n$$\\text{Initial Net Invoice} = \\text{KES } 180,000$$\n$$\\text{Net Credit Note (CN/042)} = \\text{KES } 18,000$$\n$$\\text{Adjusted Debt Outstanding} = \\text{KES } 162,000$$\n$$\\text{Cash Discount Earned} = 162,000 \\times 0.05 = \\text{KES } 8,100$$\n$$\\text{Final Net Cheque Payment} = 162,000 - 8,100 = \\text{KES } 153,900$$",
                            "**Step 5: Final Answer & Unit:** Mwangi Retail Shop pays $\\text{KES } 153,900$ via cheque. The trade discount deducted at source was $\\text{KES } 20,000$, the net credit note was $\\text{KES } 18,000$, and the cash discount received for prompt payment was $\\text{KES } 8,100$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Trade discount is deducted on the invoice before recording and never appears in ledger accounts. In contrast, Cash Discount (KES 8,100) is an incentive for early payment and is formally recorded in the Three-Column Cash Book (Discount Received column). *Common Pitfall:* Calculating the 5% cash discount on the gross initial debt (KES 180,000) rather than on the net adjusted balance after deducting the Credit Note (KES 162,000)."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: A Day of Trade at Neema Supermarket in Nakuru",
                    "content": {
                        "title": "Multi-Channel Transaction Flow at Neema Supermarket Nakuru",
                        "text": "At Neema Supermarket in Nakuru, hundreds of transactions are processed across different commercial channels each day: (1) Walk-in retail shoppers paying cash or via M-Pesa till receive printed thermal Cash Receipts; (2) A local boarding school ordering 50 bags of rice on credit receives a Sales Invoice detailing 30-day payment terms; (3) When the school returns 3 damaged bags of rice, Neema's accounts desk issues a Credit Note reducing the school's ledger balance; (4) When paying the weekly store cleaner, the cashier prepares and signs an internal Payment Voucher. Standardizing these source documents prevents fraud and maintains absolute inventory accountability."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Invoices, Credit Notes, and Business Documents Explained",
                    "content": {
                        "title": "How Invoices, Receipts, and Credit/Debit Notes Function",
                        "youtube_id": "Zk2y_mX-6-k",
                        "url": "https://www.youtube.com/watch?v=Zk2y_mX-6-k",
                        "description": "Visual exploration of trade documents, discounts, and return adjustments in commercial accounting practice."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Handling Defective Goods Returns",
                    "content": {
                        "question": "A retail trader in Eldoret returns 5 bags of spoiled wheat flour to a wholesaler from whom they were purchased on credit. Which source document will the wholesaler issue to the retailer to confirm that the retailer's outstanding debt has been reduced?",
                        "options": [
                            "Payment Voucher",
                            "Debit Note",
                            "Credit Note",
                            "Cash Receipt"
                        ],
                        "correct": "C",
                        "explanation": "A Credit Note is issued by a seller to a buyer when goods are returned (Returns Inward) or when an overcharge occurred. It formally notifies the customer that their debtor account has been credited (reduced)."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Perspective of Commercial Invoices",
                    "content": {
                        "question": "When Nairobi Textiles Ltd sells school uniform fabric on 30-day credit to St. Mark's High School, how is the physical invoice document classified by the two trading parties?",
                        "options": [
                            "As a Sales Invoice by Nairobi Textiles Ltd and as a Purchase Invoice by St. Mark's High School",
                            "As a Credit Note by Nairobi Textiles Ltd and as a Debit Note by St. Mark's High School",
                            "As a Purchase Invoice by Nairobi Textiles Ltd and as a Sales Invoice by St. Mark's High School",
                            "As a Payment Voucher by both Nairobi Textiles Ltd and St. Mark's High School"
                        ],
                        "correct": "A",
                        "explanation": "The exact same transaction document represents a Sales Invoice to the selling vendor (recording credit sales revenue) and a Purchase Invoice to the buying school (recording a trade purchase liability)."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 2 Summary Takeaways",
                    "content": {
                        "text": "1. **Invoice Perspectives:** The same paper document is a Sales Invoice to the seller (credit revenue) and a Purchase Invoice to the buyer (credit liability).\n2. **Cash Settlement Proofs:** Cash Receipts confirm immediate money received; internal Payment Vouchers authorize cash disbursements.\n3. **Returns Handling:** Credit Notes issued by sellers reduce customer debts (Returns Inward); Debit Notes request adjustments or correct invoice undercharges.\n4. **Discount Distinctions:** Trade discounts are deducted on the invoice before journal entry; Cash discounts are recorded in the Cash Book to reward early debt payment."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 3: Books of Original Entry: Specialized Day Books
    # =========================================================================
    {
        "unit_order": 3,
        "unit_name": "Books of Original Entry: Specialized Day Books",
        "unit_description": "Function, classification, and standard columnar formats of specialized day books (Sales Day Book, Purchases Day Book, Returns Inward Journal, Returns Outward Journal, General Journal) and the Golden Filter Rules.",
        "lesson_title": "Books of Original Entry: Specialized Day Books",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Accounting Office and Journal Ledger Entry",
                    "content": {
                        "title": "Administrative Office and Bookkeeping Journals",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Kenya_Office_Work.jpg",
                        "caption": "Administrative bookkeepers organizing daily commercial vouchers into specialized subsidiary day books in a modern Kenyan enterprise.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 3 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Define a Book of Original Entry (Subsidiary Book / Day Book / Journal)\n- Explain the 'Post Office Mail Sorting' analogy of transaction journalizing\n- Apply the Two Golden Filter Rules governing subsidiary day books\n- Construct standard columnar layouts for Sales, Purchases, Returns Inward, Returns Outward, and General Journals"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Books of Original Entry and Specialized Journals",
                    "content": {
                        "term": "Book of Original Entry (Subsidiary Book / Day Book)",
                        "definition": "An accounting journal where commercial transactions are systematically and chronologically recorded from verified source documents before being posted into the ledger accounts."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Post Office Mail Sorting Analogy & Golden Rules",
                    "content": {
                        "text": "In a busy business handling hundreds of transactions daily, posting every single receipt directly into the main ledger would create chaotic, unreadable books:\n\n- **The Mail Sorting Analogy:** In a central post office, letters are not delivered individually across the country as they arrive. They are sorted into regional sacks (Nairobi, Nakuru, Mombasa). Specialized Day Books act as these sorting sacks, grouping similar transactions chronologically before posting summary totals to the ledger.\n- **Golden Rule 1 (Cash Filter):** Immediate cash, bank, or M-Pesa transactions are **never** entered in Day Books—they go straight to the **Cash Book**.\n- **Golden Rule 2 (Inventory Filter):** Specialized Day Books (Sales and Purchases Journals) record **strictly inventory goods meant for resale**. Buying an office vehicle or computer on credit is non-inventory and must be entered in the **General Journal (Journal Proper)**."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Specialized Books of Original Entry (Subsidiary Books Architecture)",
                    "content": {
                        "title": "The Transaction Filtering Architecture",
                        "caption": "The transaction filtering engine routing source documents to dedicated day books based on payment settlement type and asset classification.",
                        "svg_content": SVG_SUBSIDIARY_DAY_BOOKS_FILTER
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Specialized Day Books vs. General Journal Classification Matrix",
                    "content": {
                        "headers": ["Journal / Day Book", "Source Document", "Transactions Included", "Strictly Excluded Items", "Periodic Summary Double Entry"],
                        "rows": [
                            ["Sales Day Book (Sales Journal)", "Outgoing Sales Invoices", "Credit sales of inventory (resale goods)", "Cash sales; credit sales of fixed capital assets", "Credit Sales Account (GL), Debit Debtors Control"],
                            ["Purchases Day Book (Purchases Journal)", "Incoming Supplier Invoices", "Credit purchases of inventory (resale goods)", "Cash purchases; credit purchases of fixed capital assets", "Debit Purchases Account (GL), Credit Creditors Control"],
                            ["Returns Inward Journal (Sales Returns)", "Outgoing Credit Notes", "Damaged/wrong goods returned by credit customers", "Cash refunds to retail customers", "Debit Returns Inward Account (GL), Credit Debtors Control"],
                            ["Returns Outward Journal (Purchases Returns)", "Incoming Credit Notes / Debit Notes", "Goods returned by our business to credit suppliers", "Cash rebates on immediate purchases", "Credit Returns Outward Account (GL), Debit Creditors Control"],
                            ["General Journal (Journal Proper)", "Internal JVs / Special Contracts", "Credit purchase/sale of fixed assets, opening/closing entries, errors", "Routine credit sales/purchases of inventory; all cash items", "Direct bespoke Debits and Credits with narration"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Sales Day Book Journalizing and Trade Discount Deductions",
                    "content": {
                        "intro": "Kipekee Distributors in Kisumu processes four credit sales of merchandise during August 2026: (1) Aug 4 to Achieng Stores (Inv 101): $50\\text{ bags of sugar @ KES } 1,800\\text{ less } 5\\%\\text{ trade discount}$; (2) Aug 11 to Barasa Traders (Inv 102): $40\\text{ cartons of soap @ KES } 2,500\\text{ net}$; (3) Aug 19 to Chebet Wholesalers (Inv 103): $100\\text{ packets of tea @ KES } 600\\text{ less } 10\\%\\text{ trade discount}$; (4) Aug 26 to Douglas Retailers (Inv 104): $25\\text{ bales of flour @ KES } 2,400\\text{ less } 8\\%\\text{ trade discount}$. In addition, on Aug 20, Kipekee sold an old office photocopier on credit to J. Omondi for $\\text{KES } 35,000$. Calculate the net entry for each transaction, compute the monthly Sales Day Book total posted to the General Ledger, and identify the correct recording for the photocopier.",
                        "steps": [
                            "**Step 1: Given Information:** Inv 101: Gross $= 50 \\times 1,800 = \\text{KES } 90,000$, $TD = 5\\%$. Inv 102: Net $= 40 \\times 2,500 = \\text{KES } 100,000$. Inv 103: Gross $= 100 \\times 600 = \\text{KES } 60,000$, $TD = 10\\%$. Inv 104: Gross $= 25 \\times 2,400 = \\text{KES } 60,000$, $TD = 8\\%$. Photocopier: $\\text{KES } 35,000$ (Fixed Asset).",
                            "**Step 2: Formula & Filtering Rules:**\n$$\\text{Net Invoiced Sales Amount} = \\text{Gross Amount} \\times (1 - TD)$$\n$$\\text{Monthly Sales Day Book Total (}\\Sigma\\text{)} = \\sum \\text{Net Invoices (Inventory Only)}$$\n*Rule:* Credit sales of fixed assets (photocopier) do not enter the Sales Day Book; they enter the General Journal.",
                            "**Step 3: Substitution:**\n$$\\text{Inv 101 (Achieng)} = 90,000 \\times (1 - 0.05) = 90,000 \\times 0.95$$\n$$\\text{Inv 102 (Barasa)} = \\text{KES } 100,000$$\n$$\\text{Inv 103 (Chebet)} = 60,000 \\times (1 - 0.10) = 60,000 \\times 0.90$$\n$$\\text{Inv 104 (Douglas)} = 60,000 \\times (1 - 0.08) = 60,000 \\times 0.92$$",
                            "**Step 4: Calculation:**\n$$\\text{Inv 101} = \\text{KES } 85,500$$\n$$\\text{Inv 102} = \\text{KES } 100,000$$\n$$\\text{Inv 103} = \\text{KES } 54,000$$\n$$\\text{Inv 104} = \\text{KES } 55,200$$\n$$\\text{Total Sales Day Book} = 85,500 + 100,000 + 54,000 + 55,200 = \\text{KES } 294,700$$",
                            "**Step 5: Final Answer & Unit:** Total credit sales recorded in the Sales Day Book for August is $\\text{KES } 294,700$. On August 31, this total is credited to the Sales Account in the General Ledger (GL). The credit sale of the photocopier (KES 35,000) is recorded in the General Journal (Dr J. Omondi, Cr Office Equipment Account).",
                            "**Step 6: Economic Interpretation & Common Pitfall:** The Sales Day Book records only inventory sales. Including the photocopier would falsely inflate trading revenue and distort gross profit. *Common Pitfall:* Recording gross sales before trade discount, or confusing the Sales Day Book with the Sales Ledger."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Overcoming Ledger Chaos at Kipekee Distributors in Kisumu",
                    "content": {
                        "title": "Implementing Subsidiary Day Books in Kisumu Wholesale Trade",
                        "text": "Kipekee Distributors in Kisumu supplies over 400 retail kiosks with dry groceries. In its early days, the bookkeeper attempted to post every single daily credit sale directly into the main General Ledger. Within two months, the ledger became completely congested with over 3,000 unorganized entries, resulting in billing delays and lost invoices. The company restructured its accounting by introducing specialized subsidiary day books: Sales Day Book, Purchases Day Book, and Returns Journals. Daily individual entries were diverted to customer personal ledgers, while single monthly batch totals were posted to the General Ledger, cutting bookkeeping hours by 70%."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Specialized Journals and Day Books Explained",
                    "content": {
                        "title": "How Subsidiary Books and Day Books Work",
                        "youtube_id": "U3_Qd4rX8mQ",
                        "url": "https://www.youtube.com/watch?v=U3_Qd4rX8mQ",
                        "description": "In-depth guide on recording credit sales, purchases, and returns in subsidiary day books."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Buying Capital Equipment on Credit",
                    "content": {
                        "question": "Baraka Furniture Workshop manufactures and sells wooden tables and chairs. On August 12, they purchased a computerized office printing machine on credit from Naivasha Tech Ltd for KES 45,000. In which book of original entry should this transaction be recorded?",
                        "options": [
                            "Purchases Day Book",
                            "Cash Book",
                            "General Journal (Journal Proper)",
                            "Sales Day Book"
                        ],
                        "correct": "C",
                        "explanation": "The Purchases Day Book is reserved exclusively for the credit purchase of inventory (goods intended for resale, which for Baraka is timber or furniture). An office printer is a long-term capital asset. Non-routine credit purchases of non-current assets must be recorded in the General Journal."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: The Subsidiary Books Filtering Rule",
                    "content": {
                        "question": "Which of the following transactions is strictly PROHIBITED from being recorded in the Sales Day Book?",
                        "options": [
                            "Selling 20 bags of maize on credit to a local secondary school",
                            "Selling 50 loaves of bread for immediate cash settlement at the retail counter",
                            "Selling 10 cartons of soap on 30-day credit terms to a grocery kiosk",
                            "Selling 15 bags of fertilizer on credit to an agricultural cooperative"
                        ],
                        "correct": "B",
                        "explanation": "The Sales Day Book records only credit sales of inventory. Any transaction settled with immediate cash, cheque, or mobile money must bypass the day books and be entered directly into the Cash Book."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 3 Summary Takeaways",
                    "content": {
                        "text": "1. **Subsidiary Book Function:** Day books act as chronological sorting filters for similar transactions before posting summaries to the general ledger.\n2. **Strict Inventory Scope:** Sales and Purchases Day Books record ONLY credit transactions involving inventory (goods meant for resale).\n3. **Cash Prohibition:** Immediate cash and bank payments NEVER enter day books; they belong exclusively in the Cash Book.\n4. **General Journal Role:** Non-routine transactions, such as credit purchases/sales of fixed assets, opening balances, and error corrections, are journalized in the General Journal with narrations."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 4: Cash Books and the General Journal
    # =========================================================================
    {
        "unit_order": 4,
        "unit_name": "Cash Books and the General Journal",
        "unit_description": "The dual identity of the Cash Book, single/double/three-column formats, cash vs trade discounts, and the mechanics of Contra entries.",
        "lesson_title": "Cash Books and the General Journal",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Mobile Money, Banking, and Retail Cash Flow in Kenya",
                    "content": {
                        "title": "M-Pesa and Commercial Banking Desk",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/M-PESA_mobile_money_and_Equity_agent%2C_Nairobi%2C_Kenya.jpg",
                        "caption": "A multi-channel financial agent handling physical cash, bank deposits, and M-Pesa settlements, demonstrating daily cash book inflows and outflows.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 4 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Explain the unique 'Dual Identity' of the Cash Book (Journal + Ledger Accounts)\n- Differentiate between Single-Column, Double-Column, and Three-Column Cash Books\n- Record Contra Entries accurately using the bold folio indicator 'C'\n- Distinguish between Discount Allowed (Expense) and Discount Received (Income)"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Cash Book, Contra Entries, and Cash Discounts",
                    "content": {
                        "term": "Cash Book & Contra Entry",
                        "definition": "The Cash Book is a specialized book of prime entry that also serves as the ledger accounts for cash and bank. A Contra Entry is a transaction transferring money internally between the cash box and bank account of the same firm."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Superhero Dual Identity & Cash Book Formats",
                    "content": {
                        "text": "The Cash Book is unique among all accounting books because it has a dual personality:\n\n- **The Dual Identity:** It serves as a **Book of Original Entry** (recording cash/bank receipts and payments chronologically) and simultaneously acts as the **Ledger Accounts** (Cash Account and Bank Account). No separate cash account is needed in the General Ledger!\n- **Single-Column Cash Book:** Contains one money column per side; used by micro-enterprises handling only physical cash.\n- **Double-Column Cash Book:** Features two money columns per side (**Cash** and **Bank**) to track physical cash and bank transactions simultaneously.\n- **Three-Column Cash Book:** Adds a third column on each side for **Discounts**:\n  - **Discount Allowed (Debit Side):** Cash discount granted to credit customers for early payment (treated as an Expense).\n  - **Discount Received (Credit Side):** Cash discount granted by suppliers for early settlement of invoices (treated as Income/Gain)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Double-Column Cash Book Architecture & Contra Entry Mechanics",
                    "content": {
                        "title": "Double-Column Cash Book Layout & Contra Entries",
                        "caption": "T-format specimen showing receipts on the debit side, payments on the credit side, and contra transfers between cash and bank columns.",
                        "svg_content": SVG_CASH_BOOK_AND_CONTRA_ENTRIES
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Trade Discount vs. Cash Discount Comparative Matrix",
                    "content": {
                        "headers": ["Feature / Dimension", "Trade Discount", "Cash Discount Allowed", "Cash Discount Received"],
                        "rows": [
                            ["Primary Purpose", "Encourage bulk purchasing by buyers", "Encourage credit customers to pay promptly", "Reward from suppliers for prompt debt settlement"],
                            ["Timing of Deduction", "Deducted at the point of sale on the invoice", "Deducted at the time of cash/cheque settlement", "Deducted at the time of paying supplier invoice"],
                            ["Shown on Invoice?", "Yes (explicitly subtracted from gross price)", "No (stated only as conditional terms, e.g. '5/10')", "No (stated only as payment terms)"],
                            ["Bookkeeping Entry", "NOT recorded in any ledger account", "Entered in Debit Discount column of Cash Book", "Entered in Credit Discount column of Cash Book"],
                            ["Accounting Impact", "Reduces initial recorded revenue / purchases", "Recorded as an Expense in General Ledger", "Recorded as Income / Revenue in General Ledger"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Constructing and Balancing a Three-Column Cash Book with Contra Entries",
                    "content": {
                        "intro": "Mama Halima's Wholesale Store in Garissa commences August 2026 with Cash in hand of $\\text{KES } 30,000$ and Cash at bank of $\\text{KES } 180,000$. During August, the following transactions occur: (1) Aug 5: Paid shop rent $\\text{KES } 25,000$ via bank cheque; (2) Aug 10: Cash sales $\\text{KES } 45,000$; (3) Aug 14: Deposited $\\text{KES } 35,000$ cash from till into bank account (Contra); (4) Aug 18: Received a cheque from debtor Ali for $\\text{KES } 38,000$ in full settlement of a $\\text{KES } 40,000$ debt (allowed $\\text{KES } 2,000$ discount); (5) Aug 22: Withdrew $\\text{KES } 10,000$ from bank for office cash box (Contra); (6) Aug 28: Paid supplier Kiptoo $\\text{KES } 57,000$ via cheque having received $\\text{KES } 3,000$ cash discount. Calculate: (a) Total Discount Allowed, (b) Total Discount Received, (c) Closing Cash balance (c/d), and (d) Closing Bank balance (c/d).",
                        "steps": [
                            "**Step 1: Given Information:** Opening Balances: Cash b/d $= \\text{KES } 30,000$, Bank b/d $= \\text{KES } 180,000$. Receipts: Cash Sales KES 45,000 (Cash Dr); Banking cash KES 35,000 (Bank Dr, Cash Cr - Contra); Debtor Ali KES 38,000 (Bank Dr) + KES 2,000 Discount Allowed; Cash withdrawal KES 10,000 (Cash Dr, Bank Cr - Contra). Payments: Rent KES 25,000 (Bank Cr); Supplier Kiptoo KES 57,000 (Bank Cr) + KES 3,000 Discount Received.",
                            "**Step 2: Formula & Balancing Rules:**\n$$\\text{Total Debit Cash} = \\text{Opening Cash} + \\text{Cash Sales} + \\text{Bank Withdrawal}$$\n$$\\text{Total Credit Cash} = \\text{Cash Banked} + \\text{Closing Cash (c/d)}$$\n$$\\text{Total Debit Bank} = \\text{Opening Bank} + \\text{Cash Banked} + \\text{Debtor Cheque}$$\n$$\\text{Total Credit Bank} = \\text{Rent} + \\text{Cash Withdrawn} + \\text{Supplier Payment} + \\text{Closing Bank (c/d)}$$\n*Rule:* Discount columns are totaled periodically and posted to General Ledger; they are NEVER balanced!",
                            "**Step 3: Substitution:**\n$$\\text{Debit Cash Total} = 30,000 + 45,000 + 10,000 = \\text{KES } 85,000$$\n$$\\text{Cash Payments} = \\text{KES } 35,000\\text{ (Banked)}$$\n$$\\text{Debit Bank Total} = 180,000 + 35,000 + 38,000 = \\text{KES } 253,000$$\n$$\\text{Bank Payments} = 25,000 + 10,000 + 57,000 = \\text{KES } 92,000$$",
                            "**Step 4: Calculation:**\n$$\\text{Closing Cash Balance (c/d)} = 85,000 - 35,000 = \\text{KES } 50,000$$\n$$\\text{Closing Bank Balance (c/d)} = 253,000 - 92,000 = \\text{KES } 161,000$$\n$$\\text{Total Discount Allowed (Debit)} = \\text{KES } 2,000$$\n$$\\text{Total Discount Received (Credit)} = \\text{KES } 3,000$$",
                            "**Step 5: Final Answer & Unit:** As at August 31, Mama Halima's Cash Book shows: Closing Cash Balance (c/d) of $\\text{KES } 50,000$, Closing Bank Balance (c/d) of $\\text{KES } 161,000$, Total Discount Allowed of $\\text{KES } 2,000$, and Total Discount Received of $\\text{KES } 3,000$.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** Contra entries (banking cash and withdrawing cash for business) affect both sides of the same cash book and require the folio letter **'C'**. They require zero external ledger posting because double entry is completed internally. *Common Pitfall:* Attempting to balance the discount columns against each other. Discount Allowed is an expense and Discount Received is income; each column total is posted independently to its respective General Ledger account."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Daily Cash Flow Control at Mama Halima's Wholesale in Garissa",
                    "content": {
                        "title": "Managing Cash, Bank, and Mobile Money in Garissa Town",
                        "text": "Mama Halima's Wholesale Store in Garissa operates in an intense cash-and-banking environment. Every day, retail kiosk owners pay via cash and M-Pesa till numbers, while transport contractors and fuel suppliers demand bank transfers. To prevent theft and keep accurate track of funds, Mama Halima maintains a Three-Column Cash Book. Physical cash from high sales days is banked every afternoon, marked with a bold 'C' in the folio column. By strictly balancing cash and bank balances at 5:00 PM daily, Mama Halima maintains zero unexplained cash leaks."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Two-Column and Three-Column Cash Books Tutorial",
                    "content": {
                        "title": "Cash Book Balancing and Contra Entries",
                        "youtube_id": "fTTGALaRZoc",
                        "url": "https://www.youtube.com/watch?v=fTTGALaRZoc",
                        "description": "Practical demonstration of cash book entries, discount columns, and contra transactions in senior secondary accounting."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Recording Internal Contra Transfers",
                    "content": {
                        "question": "On August 25, Mama Halima took KES 20,000 cash from her shop till and deposited it into the business bank account at Equity Bank. How should this transaction be recorded in the Double-Column Cash Book?",
                        "options": [
                            "Debit the Bank column and Credit the Cash column, marking both with 'C' in the Folio column",
                            "Debit the Cash column and Credit the Bank column, marking both with 'C' in the Folio column",
                            "Debit the Bank column only and post a credit entry to the Capital Account in the General Ledger",
                            "Credit the Bank column only and post a debit entry to the Drawings Account in the General Ledger"
                        ],
                        "correct": "A",
                        "explanation": "Depositing cash into the bank increases the bank balance (Debit Bank column) and decreases physical cash in hand (Credit Cash column). Because both sides of the double entry are completed within the cash book, it is marked with 'C' (Contra) in the folio column."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Discount Allowed Accounting Treatment",
                    "content": {
                        "question": "What is the correct accounting classification and month-end ledger destination for the total of the 'Discount Allowed' column in the Three-Column Cash Book?",
                        "options": [
                            "It is an Income and its total is credited to the Discount Received Account",
                            "It is an Expense and its total is debited to the Discount Allowed Account in the General Ledger",
                            "It is a Current Asset and is added directly to Closing Stock in the balance sheet",
                            "It is a Liability and is credited to the Bank Overdraft Account"
                        ],
                        "correct": "B",
                        "explanation": "Discount Allowed is a cash discount granted to credit customers to encourage prompt payment. It represents a cost of doing business (an Expense). At the end of the month, the column total is debited to the Discount Allowed Account in the General Ledger."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 4 Summary Takeaways",
                    "content": {
                        "text": "1. **Dual Identity:** The Cash Book serves simultaneously as a book of original entry and as the ledger accounts for cash and bank.\n2. **Contra Entries (Folio 'C'):** Internal money transfers between the cash drawer and bank account are completed entirely within the cash book without external ledger postings.\n3. **Three-Column Format:** Incorporates Discount Allowed (Debit side - Expense) and Discount Received (Credit side - Income).\n4. **No Discount Balancing:** Cash and bank columns are balanced periodically (c/d and b/d), but discount columns are simply totaled and posted to their respective General Ledger accounts."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 5: Step-by-Step Recording, Batches, and Totals
    # =========================================================================
    {
        "unit_order": 5,
        "unit_name": "Step-by-Step Recording, Batches, and Totals",
        "unit_description": "The complete posting workflow from source document verification, daily subsidiary ledger posting, period-end columnar summation, to general ledger double-entry batch consolidation.",
        "lesson_title": "Step-by-Step Recording, Batches, and Totals",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Historical and Modern General Accounting Ledgers",
                    "content": {
                        "title": "General Ledger Bookkeeping and Batch Summaries",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Camp_Chesterfield_general_account_ledger%2C_1910-1916_-_DPLA_-_206e8c73ecb9419118717c75562a2497_%28page_1%29.jpg",
                        "caption": "An authentic accounting ledger showing systematic cross-referencing folios, batch summations, and period-end balance double underlines.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC0 1.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 5 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Trace the 5-step posting pipeline from source document verification to general ledger integration\n- Distinguish between daily individual postings to personal ledgers and month-end batch postings to control accounts\n- Master cross-referencing using Folio codes (L/F, SL, PL, GL)\n- Apply double-entry rules to month-end day book totals"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Folio Cross-Referencing, Subsidiary Ledgers, and Batch Posting",
                    "content": {
                        "term": "Batch Posting & Folio Tracking",
                        "definition": "Batch posting is the process of transferring the cumulative periodic total of a subsidiary day book into the General Ledger as a single double-entry figure, with folio codes referencing the source pages."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The River and Lake Analogy & The 5-Step Pipeline",
                    "content": {
                        "text": "Understanding how transactions travel from receipts to final balance sheets requires visualizing the River and Lake model:\n\n- **The River and Lake:** Individual daily sales are like small rainwater streams flowing into a tributary river (the **Sales Day Book**). At month end, the entire accumulated river volume pours as a single massive batch into the lake (the **General Ledger Sales Account**).\n- **The 5-Step Posting Pipeline:**\n  1. *Step 1 (Verification):* Inspect physical invoices for valid dates, authorized signatures, and arithmetic math.\n  2. *Step 2 (Day Book Entry):* Enter invoice details chronologically in the specialized Day Book.\n  3. *Step 3 (Daily Personal Posting):* Post each transaction daily to the personal account of the debtor (Sales Ledger) or creditor (Purchases Ledger) to maintain real-time individual balances.\n  4. *Step 4 (Periodic Totaling):* Sum the day book money columns at the end of the month.\n  5. *Step 5 (Double Entry Batch Posting):* Post the cumulative total to the General Ledger (e.g., Credit Sales Account, Debit Total Debtors Control Account)."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "End-to-End Posting Pipeline: From Source Document to General Ledger",
                    "content": {
                        "title": "The 5-Step Batch Posting Pipeline",
                        "caption": "Visual schematic of daily individual debit entries in customer accounts and monthly cumulative credit entry to the Sales Revenue Account.",
                        "svg_content": SVG_BATCH_RECORDING_TO_LEDGER_PIPELINE
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Individual Daily Posting vs. Periodic Batch Posting Matrix",
                    "content": {
                        "headers": ["Feature / Dimension", "Individual Daily Posting", "Periodic Batch Total Posting"],
                        "rows": [
                            ["Timing / Frequency", "Conducted daily as each invoice or receipt is processed", "Conducted periodically (end of week or end of month)"],
                            ["Destination Ledger", "Subsidiary Ledgers (Sales Ledger / Purchases Ledger)", "General Ledger (Main Double-Entry Ledger)"],
                            ["Account Type", "Personal Accounts (e.g., Joy Primary School A/c, Kiptoo Millers A/c)", "Impersonal Accounts (e.g., Sales Revenue A/c, Purchases A/c)"],
                            ["Double Entry Status", "Memorandum entry only (does NOT complete double entry)", "COMPLETES formal double-entry system (Equal Dr and Cr)"],
                            ["Primary Purpose", "Track exact outstanding balance owed by or to each specific counterparty", "Record total enterprise revenues, expenses, assets, and liabilities"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Reconciling Purchases Day Book Batch Totals with Trade Creditors Control",
                    "content": {
                        "intro": "Baraka Stationery Supplies in Kisumu begins the trading period on August 1 with Trade Creditors (Payables) opening balance of $\\text{KES } 220,000$. During August, the Purchases Day Book records verified credit purchases totaling $\\text{KES } 540,000$. The Returns Outward Journal shows goods returned to suppliers totaling $\\text{KES } 45,000$. Payments made via bank cheque to trade creditors during the month total $\\text{KES } 410,000$, and suppliers granted cash discounts received totaling $\\text{KES } 20,000$. Calculate the closing balance of Trade Creditors as at August 31 and demonstrate the double-entry reconciliation.",
                        "steps": [
                            "**Step 1: Given Information:** Opening Trade Creditors balance $B_0 = \\text{KES } 220,000\\text{ (Cr)}$. Total Credit Purchases from Purchases Day Book $P = \\text{KES } 540,000$. Returns Outward $R_{\\text{out}} = \\text{KES } 45,000$. Cheque payments to creditors $C_{\\text{paid}} = \\text{KES } 410,000$. Cash Discounts Received $D_{\\text{rec}} = \\text{KES } 20,000$.",
                            "**Step 2: Formula & Control Account Rules:**\n$$\\text{Total Creditors Liability (Credit Side)} = B_0 + P$$\n$$\\text{Total Debt Reductions (Debit Side)} = R_{\\text{out}} + C_{\\text{paid}} + D_{\\text{rec}}$$\n$$\\text{Closing Trade Creditors Balance (c/d)} = \\text{Total Creditors Liability} - \\text{Total Debt Reductions}$$",
                            "**Step 3: Substitution:**\n$$\\text{Total Credit Liability} = 220,000 + 540,000 = \\text{KES } 760,000$$\n$$\\text{Total Debt Reductions} = 45,000 + 410,000 + 20,000 = \\text{KES } 475,000$$\n$$\\text{Closing Balance (c/d)} = 760,000 - 475,000$$",
                            "**Step 4: Calculation:**\n$$\\text{Total Credit Side} = \\text{KES } 760,000$$\n$$\\text{Total Debit Reductions} = \\text{KES } 475,000$$\n$$\\text{Closing Balance (c/d)} = 760,000 - 475,000 = \\text{KES } 285,000$$",
                            "**Step 5: Final Answer & Unit:** The closing balance of Trade Creditors (Payables) as at August 31 is $\\text{KES } 285,000\\text{ (Cr balance b/d for September 1)}$. The monthly total of $\\text{KES } 540,000$ from the Purchases Day Book is debited to the Purchases Account in the General Ledger.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** The $\\text{KES } 540,000$ batch total increases total supplier liability, while returns, bank payments, and discounts received reduce the liability. *Common Pitfall:* Forgetting that Returns Outward and Discounts Received reduce the creditors' balance on the debit side before computing the final closing liability."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: Month-End Financial Consolidation at Baraka Stationery in Kisumu",
                    "content": {
                        "title": "Batch Posting and Debtor Ledger Cross-Referencing in Kisumu",
                        "text": "At Baraka Stationery in Kisumu, bookkeeper Atieno manages over 80 credit customer accounts representing local schools. Throughout the month, every sales invoice is posted daily into each school's personal account in the Sales Ledger, ensuring that when headteachers call to inquire about their outstanding debt, exact balances are instantly accessible. On the final afternoon of the month, Atieno sums the Sales Day Book column (KES 450,000), writes the folio cross-reference 'GL/15', and makes a single batch entry crediting the Sales Revenue Account in the General Ledger. This streamlined division of labor guarantees accuracy and complete double-entry balance."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Posting from Books of Prime Entry to Ledgers",
                    "content": {
                        "title": "Step-by-Step Posting from Day Books to General Ledger",
                        "youtube_id": "WqlX5z6k4eQ",
                        "url": "https://www.youtube.com/watch?v=WqlX5z6k4eQ",
                        "description": "Step-by-step tutorial on folio cross-referencing and periodic batch consolidation in double-entry bookkeeping."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Chronological Sequence of Accounting Tasks",
                    "content": {
                        "question": "Which of the following represents the correct chronological sequence of bookkeeping tasks required to process a credit purchase of inventory?",
                        "options": [
                            "Post monthly total to General Ledger -> Record in Purchases Day Book -> Verify supplier invoice -> Post to supplier personal ledger",
                            "Verify supplier invoice -> Record in Purchases Day Book -> Post daily to supplier personal ledger -> Post monthly total to General Ledger",
                            "Record in General Journal -> Post to Cash Book -> Verify delivery note -> Total the Trial Balance",
                            "Post to supplier personal ledger -> Verify receipt -> Total the Cash Book -> Issue Credit Note"
                        ],
                        "correct": "B",
                        "explanation": "The proper sequence begins with source document verification, followed by chronological recording in the Purchases Day Book, daily posting to the supplier's personal account in the Purchases Ledger, and finally month-end batch total posting to the Purchases Account in the General Ledger."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Month-End Purchases Day Book Posting",
                    "content": {
                        "question": "At the end of the month, what is the correct double-entry destination for the cumulative total of the Purchases Day Book?",
                        "options": [
                            "Credited to the Purchases Account in the General Ledger",
                            "Debited to the Purchases Account in the General Ledger and Credited to Creditors Control Account",
                            "Debited to the Cash Account and Credited to the Sales Account",
                            "Recorded only in the personal ledger accounts of individual suppliers"
                        ],
                        "correct": "B",
                        "explanation": "Purchases represent an increase in goods acquired for resale (an expense/asset flow), so the monthly total is debited to the Purchases Account in the General Ledger. To complete the double entry, the aggregate liability is credited to the Creditors Control Account."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 5 Summary Takeaways",
                    "content": {
                        "text": "1. **5-Step Pipeline:** Source Document Verification -> Day Book Recording -> Daily Personal Posting -> Periodic Totaling -> General Ledger Batch Posting.\n2. **Daily vs Batch:** Personal accounts are updated daily to maintain real-time counterparty balances; general ledger accounts are updated with monthly totals to complete double entry.\n3. **Folio Cross-Referencing:** Folio codes (SL, PL, GL) create a transparent audit trail linking journal entries to ledger pages.\n4. **Control Account Integration:** Month-end day book totals update General Ledger control accounts (Debtors and Creditors) to ensure the Trial Balance balances perfectly."
                    }
                }
            ]
        ]
    },

    # =========================================================================
    # LESSON 6: Error Detection, Business Ethics, and Controls
    # =========================================================================
    {
        "unit_order": 6,
        "unit_name": "Error Detection, Business Ethics, and Controls",
        "unit_description": "Taxonomy of bookkeeping errors, Trial Balance diagnostics, the Suspense Account mechanism, correcting journal entries, and ethical internal control systems.",
        "lesson_title": "Error Detection, Business Ethics, and Controls",
        "pages": [
            # Card 1: Visual Hook & Learning Goals
            [
                {
                    "type": "suggested_image",
                    "title": "Trade Transparency and Enterprise Auditing in Kenya",
                    "content": {
                        "title": "Commercial Auditing and Error Inspection",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/City_Market_in_Nairobi.jpg",
                        "caption": "Active trading environment highlighting the critical role of error detection, accurate record-keeping, and legal tax compliance in sustaining enterprise trust.",
                        "author": "Wikimedia Commons",
                        "licensing": "CC BY-SA 4.0"
                    }
                },
                {
                    "type": "learning_goal",
                    "title": "Lesson 6 Learning Outcomes",
                    "content": {
                        "text": "By the end of this lesson, you will be able to:\n\n- Classify bookkeeping errors into those that affect vs. do not affect Trial Balance agreement\n- Identify the 5 errors not revealed by a Trial Balance (Omission, Commission, Principle, Original Entry, Compensating)\n- Apply the Suspense Account mechanism and General Journal correcting entries\n- Appraise the ethical, legal (KRA), and fiduciary responsibilities of professional bookkeepers"
                    }
                }
            ],
            # Card 2: Definitions & Core Concepts
            [
                {
                    "type": "definition_card",
                    "title": "Accounting Errors, Suspense Accounts, and Ethics",
                    "content": {
                        "term": "Error of Principle vs. Suspense Account",
                        "definition": "An Error of Principle is a mistake where a transaction violates fundamental accounting rules by confusing capital and revenue items; a Suspense Account is a temporary account opened to balance the Trial Balance until errors are located and corrected."
                    }
                },
                {
                    "type": "concept_explanation",
                    "title": "The Pipe Leak Analogy & Error Classification",
                    "content": {
                        "text": "Finding mistakes in bookkeeping is like inspecting a water pipe system for leaks:\n\n- **The Pipe Leak Analogy:** If 1,000 liters of water enter a building but only 900 liters emerge, the discrepancy reveals an obvious leak (an arithmetic error disturbing the Trial Balance). But if water flows to the wrong room without leaking outside, the water meters still balance—just like deceptive errors that do not affect Trial Balance equality!\n- **Category A (Errors NOT Affecting Trial Balance):** (1) *Error of Omission* (transaction completely forgotten); (2) *Error of Commission* (correct side, wrong personal account); (3) *Error of Principle* (treating capital assets as expenses); (4) *Error of Original Entry* (wrong figure entered in day book first); (5) *Compensating Errors* (two independent errors accidentally cancelling each other out).\n- **Category B (Errors that DO Disrupt Trial Balance):** Transposition errors (digits reversed), single entry errors, and arithmetic summation errors. The discrepancy is placed temporarily in a **Suspense Account** until cleared via General Journal correcting entries."
                    }
                }
            ],
            # Card 3: Deep Dive Breakdown & High-Precision Dark-Mode Vector SVG
            [
                {
                    "type": "suggested_diagram",
                    "title": "Bookkeeping Error Classification & Trial Balance Diagnostics",
                    "content": {
                        "title": "Taxonomy of Errors and Internal Controls",
                        "caption": "Comprehensive matrix contrasting errors that do not affect the trial balance against arithmetic errors requiring a suspense account.",
                        "svg_content": SVG_ERROR_CLASSIFICATION_AND_CORRECTION_MATRIX
                    }
                }
            ],
            # Card 4: Comparative Matrix
            [
                {
                    "type": "comparison_table",
                    "title": "Classification of Accounting Errors: Causes, Examples, and Detection Methods",
                    "content": {
                        "headers": ["Error Classification", "Nature of Mistake", "Trial Balance Agreement?", "Diagnostic / Detection Method", "Correction Method"],
                        "rows": [
                            ["Error of Omission", "Transaction completely omitted from all books", "Yes (Totals agree perfectly)", "Bank reconciliation or supplier statement check", "Enter original transaction in General Journal"],
                            ["Error of Commission", "Posted to wrong person's account in same ledger class", "Yes (Totals agree perfectly)", "Customer complaints or debtor statement query", "Dr correct debtor, Cr wrong debtor via Journal"],
                            ["Error of Principle", "Violates fundamental rules (Capital vs Revenue)", "Yes (Totals agree perfectly)", "Audit review of asset vs expense accounts", "Dr Asset A/c, Cr Expense A/c via Journal"],
                            ["Error of Original Entry", "Wrong amount written in Day Book initially", "Yes (Totals agree perfectly)", "Re-checking physical invoice arithmetic", "Journalize difference to adjust both accounts"],
                            ["Compensating Error", "Two unrelated errors cancel out arithmetically", "Yes (Totals agree perfectly)", "Detailed audit vouching of all accounts", "Correct each independent error via Journal"],
                            ["Transposition Error", "Digits reversed (e.g., KES 4,500 entered as 5,400)", "NO (Debits ≠ Credits)", "Difference is divisible by 9!", "Open Suspense Account, journalize difference"],
                            ["Single Entry Error", "Debit entered but credit forgotten (or vice versa)", "NO (Debits ≠ Credits)", "Trial Balance difference equals omitted entry", "Credit missing account, debit Suspense Account"]
                        ]
                    }
                }
            ],
            # Card 5: Step-by-Step Worked Calculation
            [
                {
                    "type": "worked_example",
                    "title": "Worked Example: Correcting Trial Balance Errors via Suspense Account and General Journal Entries",
                    "content": {
                        "intro": "The preliminary Trial Balance of Baraka SACCO in Nyeri as at December 31, 2026, fails to agree: Total Debits $= \\text{KES } 1,452,000$ and Total Credits $= \\text{KES } 1,460,800$ (Credit excess difference of $\\text{KES } 8,800$). The difference is entered in a Suspense Account (Debit $\\text{KES } 8,800$). Subsequent audit discovers two errors: (1) A cash payment for motor vehicle repairs of $\\text{KES } 7,200$ was correctly credited in the Cash Book, but was incorrectly debited to the Motor Vehicle (Asset) Account as $\\text{KES } 2,700$ (a combined error of principle and transposition error); (2) Commission received of $\\text{KES } 4,300$ in cash was correctly debited in the Cash Book, but was completely omitted from the Commission Income Account (a single entry error). Formulate correcting journal entries, clear the Suspense Account, and determine the final agreed Trial Balance total.",
                        "steps": [
                            "**Step 1: Given Information:** Initial Trial Balance: Debits $= \\text{KES } 1,452,000$, Credits $= \\text{KES } 1,460,800$. Initial Suspense Account balance $= \\text{KES } 8,800\\text{ (Debit)}$. Error 1: Paid repairs KES 7,200 (Credit Cash 7,200 correct, Debit Motor Vehicle 2,700 wrong). Error 2: Commission received KES 4,300 (Debit Cash 4,300 correct, Credit Commission Income omitted).",
                            "**Step 2: Formula & Correcting Journal Rules:**\n*Error 1 Correction:*\n- Debit Motor Vehicle Repairs Expense Account with correct KES 7,200.\n- Credit Motor Vehicle Asset Account with wrong KES 2,700 to cancel it.\n- Credit Suspense Account with difference: $7,200 - 2,700 = \\text{KES } 4,500$.\n*Error 2 Correction:*\n- Credit Commission Income Account with KES 4,300.\n- Debit Suspense Account with KES 4,300.",
                            "**Step 3: Substitution & Suspense Account Ledger:**\n$$\\text{Suspense A/c Opening Balance (Dr)} = \\text{KES } 8,800$$\n$$\\text{Credit Suspense from Error 1} = \\text{KES } 4,500$$\n$$\\text{Credit Suspense from Error 2} = \\text{KES } 4,300$$\n$$\\text{Total Credits to Suspense} = 4,500 + 4,300 = \\text{KES } 8,800$$\n$$\\text{Net Suspense Account Balance} = 8,800 - 8,800 = \\text{KES } 0\\text{ (Fully Cleared!)}$$",
                            "**Step 4: Calculation of Corrected Trial Balance Totals:**\n$$\\text{Corrected Debits} = \\text{Initial Debits} - \\text{Wrong Asset (2,700)} + \\text{Repairs Expense (7,200)} = 1,452,000 - 2,700 + 7,200 = \\text{KES } 1,456,500$$\n$$\\text{Add Suspense Cleared} = 1,456,500 + \\text{Omitted Credits Adjusted}$$\n$$\\text{Corrected Credits} = \\text{Initial Credits (1,460,800)} + \\text{Commission Income (4,300)} - \\text{Suspense Removed (8,800)} = \\text{KES } 1,456,300$$\n$$\\text{Reconciled Agreed Trial Balance Total} = \\text{KES } 1,465,100$$",
                            "**Step 5: Final Answer & Unit:** The Suspense Account is fully cleared with a zero balance ($0$). The corrected, verified Trial Balance agrees perfectly at $\\text{KES } 1,465,100$ on both Debit and Credit sides.",
                            "**Step 6: Economic Interpretation & Common Pitfall:** The discrepancy of KES 8,800 was caused by a KES 4,500 debit shortage from the transposition error ($7,200 - 2,700 = 4,500$) plus the KES 4,300 single entry omission ($4,500 + 4,300 = 8,800$). *Common Pitfall:* Assuming a Trial Balance that balances is error-free; Errors of Principle (classifying repairs as vehicles) distort balance sheet assets and net profit without disturbing trial balance agreement."
                        ]
                    }
                }
            ],
            # Card 6: Kenyan Case Study & Video
            [
                {
                    "type": "real_world_example",
                    "title": "Kenyan Enterprise Case Study: The Discrepancy Mystery and Audit at Baraka SACCO in Nyeri",
                    "content": {
                        "title": "Internal Audit and Error Rectification at Baraka SACCO Nyeri",
                        "text": "During an annual internal audit at Baraka SACCO in Nyeri, the audit committee discovered that the treasurer had recorded the purchase of office stationery worth KES 15,000 as 'Office Equipment' (an Error of Principle) and had inverted an electricity bill payment of KES 8,100 as KES 1,800 in the ledger (a Transposition Error). Because the SACCO manages community savings, maintaining uncompromised financial records was vital. The committee prepared General Journal correction entries with clear narrations, cleared the Suspense Account, and instituted double-signature internal authorization for all future disbursements, restoring member confidence."
                    }
                },
                {
                    "type": "suggested_video",
                    "title": "Correction of Errors and Suspense Accounts",
                    "content": {
                        "title": "How to Correct Accounting Errors and Clear Suspense Accounts",
                        "youtube_id": "7_j5N5V1N9c",
                        "url": "https://www.youtube.com/watch?v=7_j5N5V1N9c",
                        "description": "Practical demonstration of identifying accounting errors, journalizing corrections, and clearing suspense accounts in senior secondary business studies."
                    }
                }
            ],
            # Card 7: Formative Scenario-Based MCQs
            [
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 1: Identifying an Error of Principle",
                    "content": {
                        "question": "A bookkeeper records the cash purchase of an office delivery van for KES 850,000 by debiting the 'Motor Vehicle Running Expenses Account' and crediting the Cash Book. What type of bookkeeping error has been committed?",
                        "options": [
                            "Error of Omission",
                            "Error of Principle",
                            "Error of Commission",
                            "Transposition Error"
                        ],
                        "correct": "B",
                        "explanation": "An Error of Principle occurs when fundamental accounting rules are violated, specifically confusing capital expenditure (acquiring a long-term asset like a van) with revenue expenditure (routine operational expenses like fuel or repairs). The Trial Balance will still balance, but the financial statements will be fundamentally misstated."
                    }
                },
                {
                    "type": "knowledge_check",
                    "title": "Knowledge Check 2: Mathematical Signature of Transposition Errors",
                    "content": {
                        "question": "An auditor notices that a Trial Balance debit total exceeds the credit total by KES 3,600. What diagnostic mathematical property suggests this discrepancy was caused by a Transposition Error?",
                        "options": [
                            "The difference of KES 3,600 is exactly divisible by 9 ($3,600 \\div 9 = 400$)",
                            "The difference is an even number ending in zero",
                            "The difference represents exactly 16% Value Added Tax",
                            "The difference matches the opening cash balance"
                        ],
                        "correct": "A",
                        "explanation": "A classic mathematical property of Transposition Errors (reversing the sequence of digits, such as writing 84 instead of 48) is that the resulting arithmetic difference is always evenly divisible by 9."
                    }
                }
            ],
            # Card 8: Lesson Synthesis & Key Takeaways
            [
                {
                    "type": "key_takeaway",
                    "title": "Lesson 6 Summary Takeaways",
                    "content": {
                        "text": "1. **Error Classification:** Errors that do NOT affect the Trial Balance (Omission, Commission, Principle, Original Entry, Compensating) vs. Errors that DO disrupt agreement (Transposition, Single Entry, Addition).\n2. **Error of Principle Danger:** Violates fundamental accounting concepts (e.g., treating capital assets as expenses), distorting balance sheet assets and net profit while leaving the Trial Balance in balance.\n3. **Suspense Account:** A temporary holding account used to record the trial balance discrepancy until investigated and cleared via General Journal correcting entries.\n4. **Ethical Stewardship:** Honest, verified, and transparent bookkeeping is a legal and moral obligation that protects enterprise sustainability, member funds, and KRA compliance."
                    }
                }
            ]
        ]
    }
]
