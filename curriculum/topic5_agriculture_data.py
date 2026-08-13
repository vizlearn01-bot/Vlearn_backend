"""
Form 4 Agriculture — Topic 5 Data File
Topic: Agricultural Economics IV (Farm Accounts)
Curriculum: 844 (ID: 4) | Grade: Form 4 (ID: 4) | Subject: Agriculture (ID: 19) | Topic ID: 99 (Order: 5)

Contains 3 Learning Units:
1. Financial Documents and Source Records
2. Ledger, Cash Book, and Transaction Recording
3. Financial Statements (Balance Sheets and Profit & Loss Accounts)
"""

# =============================================================================
# CUSTOM DARK-MODE SVG DIAGRAMS FOR FARM ACCOUNTS
# =============================================================================

# 1. Sequence of Source Documents Flowchart
SVG_SOURCE_DOCUMENTS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Sequence of Source Documents in Credit Transactions</text>

  <!-- Step 1: LPO -->
  <rect x="60" y="90" width="140" height="100" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="10"/>
  <text x="130" y="125" font-family="Arial" font-size="14" fill="#38bdf8" font-weight="bold" text-anchor="middle">1. LPO</text>
  <text x="130" y="148" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Local Purchase</text>
  <text x="130" y="165" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Order</text>
  <text x="130" y="180" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">Buyer -> Seller</text>

  <!-- Arrow 1 -->
  <line x1="200" y1="140" x2="240" y2="140" stroke="#38bdf8" stroke-width="3"/>

  <!-- Step 2: Delivery Note -->
  <rect x="240" y="90" width="140" height="100" fill="#1e293b" stroke="#4ade80" stroke-width="2.5" rx="10"/>
  <text x="310" y="125" font-family="Arial" font-size="14" fill="#4ade80" font-weight="bold" text-anchor="middle">2. Delivery Note</text>
  <text x="310" y="148" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Accompanies Goods</text>
  <text x="310" y="165" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Signed on Arrival</text>
  <text x="310" y="180" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">Seller -> Buyer</text>

  <!-- Arrow 2 -->
  <line x1="380" y1="140" x2="420" y2="140" stroke="#4ade80" stroke-width="3"/>

  <!-- Step 3: Invoice -->
  <rect x="420" y="90" width="140" height="100" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5" rx="10"/>
  <text x="490" y="125" font-family="Arial" font-size="14" fill="#f59e0b" font-weight="bold" text-anchor="middle">3. Invoice</text>
  <text x="490" y="148" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Bill Requesting</text>
  <text x="490" y="165" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Credit Payment</text>
  <text x="490" y="180" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">Seller -> Buyer</text>

  <!-- Arrow 3 -->
  <line x1="560" y1="140" x2="600" y2="140" stroke="#f59e0b" stroke-width="3"/>

  <!-- Step 4: Receipt -->
  <rect x="600" y="90" width="140" height="100" fill="#1e293b" stroke="#f43f5e" stroke-width="2.5" rx="10"/>
  <text x="670" y="125" font-family="Arial" font-size="14" fill="#f43f5e" font-weight="bold" text-anchor="middle">4. Receipt</text>
  <text x="670" y="148" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Confirms Payment</text>
  <text x="670" y="165" font-family="Arial" font-size="11" fill="#f8fafc" text-anchor="middle">Settled (Cash/Cheque)</text>
  <text x="670" y="180" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">Seller -> Buyer</text>

  <!-- Document Functions Summary Box -->
  <rect x="60" y="230" width="680" height="210" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="12"/>
  <text x="400" y="262" font-family="Arial" font-size="15" fill="#f8fafc" font-weight="bold" text-anchor="middle">Summary of Farm Source Documents</text>

  <text x="90" y="295" font-family="Arial" font-size="13" fill="#38bdf8" font-weight="bold">LPO:</text>
  <text x="160" y="295" font-family="Arial" font-size="12" fill="#cbd5e1">Official order authorizing delivery of goods on credit.</text>

  <text x="90" y="330" font-family="Arial" font-size="13" fill="#4ade80" font-weight="bold">Delivery Note:</text>
  <text x="185" y="330" font-family="Arial" font-size="12" fill="#cbd5e1">Verifies quantity and physical condition of delivered items.</text>

  <text x="90" y="365" font-family="Arial" font-size="13" fill="#f59e0b" font-weight="bold">Invoice:</text>
  <text x="160" y="365" font-family="Arial" font-size="12" fill="#cbd5e1">Formal bill requesting payment for credit purchases.</text>

  <text x="90" y="400" font-family="Arial" font-size="13" fill="#f43f5e" font-weight="bold">Receipt:</text>
  <text x="160" y="400" font-family="Arial" font-size="12" fill="#cbd5e1">Permanent written proof of immediate cash/cheque settlement.</text>
</svg>"""


# 2. Cash Book Structure Diagram
SVG_CASH_BOOK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">Structure of a Double-Column Cash Book Ledger</text>

  <!-- Left Side: DEBIT (DR) -->
  <rect x="50" y="70" width="340" height="370" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="10"/>
  <rect x="50" y="70" width="340" height="40" fill="#0284c7" rx="10"/>
  <text x="220" y="96" font-family="Arial" font-size="16" fill="#ffffff" font-weight="bold" text-anchor="middle">DEBIT (DR) — RECEIPTS (MONEY IN)</text>

  <!-- DR Columns -->
  <text x="75" y="135" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold">Date</text>
  <text x="135" y="135" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold">Details</text>
  <text x="240" y="135" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold">Folio</text>
  <text x="290" y="135" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold">Cash</text>
  <text x="345" y="135" font-family="Arial" font-size="12" fill="#f59e0b" font-weight="bold">Bank</text>

  <line x1="50" y1="145" x2="390" y2="145" stroke="#475569" stroke-width="1.5"/>

  <!-- Right Side: CREDIT (CR) -->
  <rect x="410" y="70" width="340" height="370" fill="#1e293b" stroke="#f43f5e" stroke-width="2.5" rx="10"/>
  <rect x="410" y="70" width="340" height="40" fill="#be123c" rx="10"/>
  <text x="580" y="96" font-family="Arial" font-size="16" fill="#ffffff" font-weight="bold" text-anchor="middle">CREDIT (CR) — PAYMENTS (MONEY OUT)</text>

  <!-- CR Columns -->
  <text x="435" y="135" font-family="Arial" font-size="12" fill="#fca5a5" font-weight="bold">Date</text>
  <text x="495" y="135" font-family="Arial" font-size="12" fill="#fca5a5" font-weight="bold">Details</text>
  <text x="600" y="135" font-family="Arial" font-size="12" fill="#fca5a5" font-weight="bold">Folio</text>
  <text x="650" y="135" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold">Cash</text>
  <text x="705" y="135" font-family="Arial" font-size="12" fill="#f59e0b" font-weight="bold">Bank</text>

  <line x1="410" y1="145" x2="750" y2="145" stroke="#475569" stroke-width="1.5"/>

  <!-- Rules Note at Bottom -->
  <rect x="80" y="380" width="640" height="45" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
  <text x="400" y="407" font-family="Arial" font-size="12" fill="#38bdf8" text-anchor="middle" font-weight="bold">Contra Entries ("C"): Internal transfers (cash to bank) posted on BOTH sides simultaneously.</text>
</svg>"""


# 3. Accounting Cycle & Financial Statements Flowchart
SVG_ACCOUNTING_CYCLE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" width="100%" height="100%">
  <rect width="800" height="480" fill="#0f172a" rx="16"/>
  <text x="400" y="38" font-family="Arial" font-size="20" fill="#f8fafc" font-weight="bold" text-anchor="middle">The Complete Farm Accounting Cycle</text>

  <!-- 5 Circular Nodes -->
  <!-- Step 1 -->
  <rect x="50" y="120" width="120" height="80" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="10"/>
  <text x="110" y="150" font-family="Arial" font-size="12" fill="#38bdf8" font-weight="bold" text-anchor="middle">1. Source Doc</text>
  <text x="110" y="170" font-family="Arial" font-size="10" fill="#cbd5e1" text-anchor="middle">Invoice/Receipt</text>

  <line x1="170" y1="160" x2="200" y2="160" stroke="#94a3b8" stroke-width="2"/>

  <!-- Step 2 -->
  <rect x="200" y="120" width="120" height="80" fill="#1e293b" stroke="#4ade80" stroke-width="2" rx="10"/>
  <text x="260" y="150" font-family="Arial" font-size="12" fill="#4ade80" font-weight="bold" text-anchor="middle">2. Journal</text>
  <text x="260" y="170" font-family="Arial" font-size="10" fill="#cbd5e1" text-anchor="middle">First Entry</text>

  <line x1="320" y1="160" x2="350" y2="160" stroke="#94a3b8" stroke-width="2"/>

  <!-- Step 3 -->
  <rect x="350" y="120" width="120" height="80" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="10"/>
  <text x="410" y="150" font-family="Arial" font-size="12" fill="#f59e0b" font-weight="bold" text-anchor="middle">3. Ledger</text>
  <text x="410" y="170" font-family="Arial" font-size="10" fill="#cbd5e1" text-anchor="middle">Cash Book DR/CR</text>

  <line x1="470" y1="160" x2="500" y2="160" stroke="#94a3b8" stroke-width="2"/>

  <!-- Step 4 -->
  <rect x="500" y="120" width="120" height="80" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="10"/>
  <text x="560" y="150" font-family="Arial" font-size="12" fill="#f43f5e" font-weight="bold" text-anchor="middle">4. Valuation</text>
  <text x="560" y="170" font-family="Arial" font-size="10" fill="#cbd5e1" text-anchor="middle">Closing Inventory</text>

  <line x1="620" y1="160" x2="650" y2="160" stroke="#94a3b8" stroke-width="2"/>

  <!-- Step 5 -->
  <rect x="650" y="120" width="120" height="80" fill="#1e293b" stroke="#a855f7" stroke-width="2" rx="10"/>
  <text x="710" y="150" font-family="Arial" font-size="12" fill="#a855f7" font-weight="bold" text-anchor="middle">5. Statements</text>
  <text x="710" y="170" font-family="Arial" font-size="10" fill="#cbd5e1" text-anchor="middle">Balance &amp; P&amp;L</text>

  <!-- Final Statements Box Breakdown -->
  <rect x="150" y="240" width="500" height="200" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="12"/>
  <text x="400" y="270" font-family="Arial" font-size="16" fill="#38bdf8" font-weight="bold" text-anchor="middle">End-of-Year Financial Statements</text>

  <text x="180" y="305" font-family="Arial" font-size="14" fill="#4ade80" font-weight="bold">BALANCE SHEET:</text>
  <text x="180" y="330" font-family="Arial" font-size="12" fill="#cbd5e1">• Measures Solvency (Total Assets vs Total Liabilities).</text>
  <text x="180" y="350" font-family="Arial" font-size="12" fill="#cbd5e1">• Solvency Condition: Total Assets &gt; Total Liabilities (Net Capital).</text>

  <text x="180" y="385" font-family="Arial" font-size="14" fill="#f59e0b" font-weight="bold">PROFIT &amp; LOSS ACCOUNT:</text>
  <text x="180" y="410" font-family="Arial" font-size="12" fill="#cbd5e1">• Measures Annual Profit (Sales &amp; Receipts vs Purchases &amp; Expenses).</text>
  <text x="180" y="430" font-family="Arial" font-size="12" fill="#cbd5e1">• Includes Opening Valuation, Closing Valuation, and Debts.</text>
</svg>"""


# =============================================================================
# LESSON DATA DICTIONARIES
# =============================================================================

LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Financial Documents and Source Records",
    "lesson_title": "Financial Documents and Source Records",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Farm Accounting & Source Records",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 1 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Identify and explain the purpose of key source documents (Invoice, Receipt, Delivery Note, LPO, Journal, Inventory).\n"
                            "- Outline the sequential flow of source documents in credit purchases.\n"
                            "- Define valuation and execute a 5-step farm stocktaking and inventory valuation procedure."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Source Documents Defined",
                    "content": {
                        "text": (
                            "- **Source Document:** An original written record providing verifiable proof that a transaction took place.\n"
                            "- **Invoice:** A document issued by a seller to a buyer for goods taken on credit, requesting future payment.\n"
                            "- **Receipt:** A document issued by a seller immediately upon receiving cash or cheque payment.\n"
                            "- **Delivery Note:** A document accompanying delivered goods, signed by the buyer to confirm quantity and physical condition."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Source Document Flowchart Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Sequence of Credit Source Documents",
                    "content": {
                        "text": "Flowchart showing the chronological order of source documents from LPO, Delivery Note, and Invoice to final Receipt.",
                        "svg": SVG_SOURCE_DOCUMENTS
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Detailed Functions of LPO, Journal, and Inventory",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Source Document Functions",
                    "content": {
                        "headers": ["Document Name", "Issued By", "Primary Purpose", "Timing"],
                        "rows": [
                            ["Local Purchase Order (LPO)", "Buyer to Seller", "Formally authorizes supplier to deliver goods on credit", "Before delivery"],
                            ["Delivery Note", "Seller to Buyer", "Confirms goods delivered in correct quantity and condition", "During physical delivery"],
                            ["Invoice", "Seller to Buyer", "Requests payment for credit purchase", "After delivery"],
                            ["Receipt", "Seller to Buyer", "Confirms cash/cheque payment is fully settled", "Upon payment"],
                            ["Journal", "Farm Manager", "Chronological diary of first entry before ledger posting", "Daily"],
                            ["Inventory", "Farm Manager", "Complete itemized list of all assets and their financial value", "Fixed date (Year end)"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Step-by-Step Procedure: Farm Inventory & Valuation",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "5-Step Inventory and Valuation Procedure",
                    "content": {
                        "text": (
                            "**Step 1: Select the Valuation Date**\n"
                            "Choose a fixed closing date (e.g., December 31st) to capture a clean financial snapshot.\n\n"
                            "**Step 2: Conduct Physical Count (Stocktaking)**\n"
                            "Walk through the farm, itemizing every physical asset (land, buildings, machinery, livestock, feeds, cash).\n\n"
                            "**Step 3: Group Assets Systematically**\n"
                            "Divide items into Fixed Assets (durable property) and Current Assets (liquid/consumable property).\n\n"
                            "**Step 4: Apply Valuation Methods**\n"
                            "Value land/crops using current market prices. Value machinery/buildings by subtracting depreciation from cost.\n\n"
                            "**Step 5: Calculate Total Valuation**\n"
                            "Multiply quantities by unit values and sum up to obtain Total Farm Asset Valuation."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Practical Application: Credit Purchase Loop",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Case Study: Purchasing Feed on Credit",
                    "content": {
                        "text": (
                            "Kitheko Farm wants to buy 50 bags of layers' mash on credit:\n"
                            "1. Manager writes an **LPO** in duplicate, keeping the copy and sending the original to the agrovet.\n"
                            "2. Agrovet delivers feed accompanied by a **Delivery Note**. Storekeeper inspects bags and signs.\n"
                            "3. Agrovet mails an **Invoice** showing KShs 125,000 due in 30 days.\n"
                            "4. When the farm pays by cheque, the agrovet issues a serial-numbered **Receipt**."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Interactive Matching Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Matching Transactions to Source Documents",
                    "content": {
                        "text": "Match the transaction to its source document: (1) Paying cash for hand tools at hardware, (2) Receiving 20 crates of tomatoes with chef's signature, (3) Sending a bill for credit milk sales.",
                        "options": [
                            "A: (1) Receipt, (2) Delivery Note, (3) Invoice",
                            "B: (1) Invoice, (2) LPO, (3) Receipt",
                            "C: (1) Delivery Note, (2) Receipt, (3) Journal",
                            "D: (1) LPO, (2) Delivery Note, (3) Invoice"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "Receipts settle cash payments. Delivery Notes verify goods delivered. Invoices bill credit buyers."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Precautions in Stocktaking & Valuation",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Key Valuation Rules",
                    "content": {
                        "text": (
                            "- **Owned Assets Only:** Never include leased or rented equipment in the inventory.\n"
                            "- **Depreciation Accounting:** Always apply a depreciation factor to aging machinery and buildings.\n"
                            "- **Condition Inspection:** Inspect stored feeds, seeds, and drugs for spoilage before valuing."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Journal Page Structure",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Structure of the Journal",
                    "content": {
                        "text": (
                            "The Journal records daily transactions in chronological order before ledger posting.\n"
                            "**Columns:** Date | Transaction Details | Folio (LF Ref) | Debit (KShs) | Credit (KShs)"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Source documents provide verifiable proof for bookkeeping.\n"
                            "2. Credit purchases follow: LPO -> Delivery Note -> Invoice -> Receipt.\n"
                            "3. Stocktaking and valuation establish the total cash value of farm assets on a fixed date."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Inventory & Valuation (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Define a farm inventory and explain why conducting a valuation is critical for farm accounts. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Definition:** A farm inventory is an itemized list of all physical assets owned by the farm on a specific date.\n"
                            "2. **Estimation of Wealth:** Valuation assigns financial values based on market prices or costs to determine total asset worth.\n"
                            "3. **Depreciation Accounting:** Applies wear-and-tear reductions to machinery and buildings so asset values are not inflated.\n"
                            "4. **Balance Sheet Preparation:** Valuation provides total asset figures needed to calculate net capital and determine solvency."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Ledger, Cash Book, and Transaction Recording",
    "lesson_title": "Ledger, Cash Book, and Transaction Recording",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Double-Entry Bookkeeping",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 2 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- State the rules of the Double-Entry System (Debit vs Credit).\n"
                            "- Describe the layout and purpose of a Ledger.\n"
                            "- Post, balance, and close a Double-Column Cash Book.\n"
                            "- Identify and execute Contra Entries ('C' notation)."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Core Bookkeeping Terms",
                    "content": {
                        "text": (
                            "- **Ledger:** The principal book of accounts storing categorized individual accounts.\n"
                            "- **Debit (DR):** The left-hand side of an account page, recording money/value received.\n"
                            "- **Credit (CR):** The right-hand side of an account page, recording money/value paid out.\n"
                            "- **Double-Entry Rule:** Every transaction must be debited to one account and credited to another."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Cash Book Structure Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Double-Column Cash Book Layout",
                    "content": {
                        "text": "Anatomy diagram showing Debit (DR) side on left, Credit (CR) side on right, and Cash/Bank columns.",
                        "svg": SVG_CASH_BOOK
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Double-Entry Posting Rules",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Rules for DR and CR Entries",
                    "content": {
                        "text": (
                            "- **Debit Side (DR - Left):** Post all receipts (cash or cheques received).\n"
                            "- **Credit Side (CR - Right):** Post all payments (cash or cheques paid out).\n"
                            "- **Cash Column:** Record physical currency transactions.\n"
                            "- **Bank Column:** Record cheques, bank transfers, or direct deposits."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Contra Entries Explained",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Understanding Contra Entries ('C')",
                    "content": {
                        "text": (
                            "A **Contra Entry** is an internal cash transfer between the Cash box and Bank account.\n\n"
                            "**1. Cash Deposited into Bank:** Credit Cash column (money leaving cash box) AND Debit Bank column (money entering bank).\n"
                            "**2. Cash Withdrawn from Bank for Farm Use:** Credit Bank column AND Debit Cash column.\n"
                            "**Folio Mark:** Write 'C' in the Folio column on both sides."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Worked Example: Double-Column Cash Book Table",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Recording & Balancing July Cash Book",
                    "content": {
                        "text": (
                            "**Transactions:**\n"
                            "- Jul 1: Cheque received from Ndete KShs 2,000 -> Debit Bank (2,000)\n"
                            "- Jul 2: Paid DAP fertilizer by cheque KShs 5,000 -> Credit Bank (5,000)\n"
                            "- Jul 3: Cash received from Ngala KShs 5,000 -> Debit Cash (5,000)\n"
                            "- Jul 4: Paid water bill in cash KShs 400 -> Credit Cash (400)\n"
                            "- Jul 11: Deposited cash into bank KShs 2,000 -> Contra: Credit Cash (2,000) & Debit Bank (2,000)\n\n"
                            "**Balancing at Month End:**\n"
                            "- Total Cash DR = 5,000 | Total Cash CR = 2,400 -> Cash Balance c/d = **KShs 2,600**\n"
                            "- Total Bank DR = 4,000 | Total Bank CR = 8,500 -> Bank Overdraft = **-KShs 4,500**"
                        )
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Step-by-Step Procedure: Balancing Cash Book",
            "blocks": [
                {
                    "block_type": "step_by_step_procedure",
                    "component_type": "step_by_step_procedure",
                    "title": "5 Steps to Balance a Cash Book",
                    "content": {
                        "text": (
                            "**Step 1: Set up Double-Column Layout**\n"
                            "Divide page into DR (left) and CR (right) with Date, Details, Folio, Cash, Bank columns.\n\n"
                            "**Step 2: Post Receipts to DR Side**\n"
                            "Enter all incoming cash in Cash column and cheques in Bank column.\n\n"
                            "**Step 3: Post Payments to CR Side**\n"
                            "Enter all outgoing cash in Cash column and cheques in Bank column.\n\n"
                            "**Step 4: Record Contra Entries ('C')**\n"
                            "Post internal cash-to-bank transfers on both sides simultaneously with 'C' in Folio.\n\n"
                            "**Step 5: Calculate Balance Carried Down (c/d)**\n"
                            "Sum DR and CR columns. Write difference as Balance c/d on smaller side and draw double underline under totals."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Interactive Spot-The-Error Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Identifying Bookkeeping Errors",
                    "content": {
                        "text": "A storekeeper receives KShs 3,000 cash for egg sales and posts it on the Credit (CR) side. What error occurred?",
                        "options": [
                            "A: No error. Receipts belong on Credit side.",
                            "B: Wrong side. Cash sales are receipts and must be posted on Debit (DR) side.",
                            "C: Wrong column. Cash sales belong in Bank column.",
                            "D: Cash sales must be posted to Journal only."
                        ],
                        "correct_answer_index": 1,
                        "explanation": "Cash receipts represent incoming money and must be debited on the DR side. Posting on CR incorrectly implies a payment."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Types of Ledgers",
            "blocks": [
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Ledger Categorization",
                    "content": {
                        "text": (
                            "- **Sales Ledger (Debtors Ledger):** Contains individual accounts of customers who owe money for credit purchases.\n"
                            "- **Purchases Ledger (Creditors Ledger):** Contains accounts of suppliers to whom the farm owes money.\n"
                            "- **General Ledger:** Contains nominal accounts (expenses, sales, assets, capital)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Double-entry rules require equal Debit and Credit postings.\n"
                            "2. Cash books combine Cash and Bank columns to track liquid balances.\n"
                            "3. Contra entries ('C') transfer funds between Cash and Bank columns internally."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Double-Entry Rules & Contra Entries (8 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Explain the double-entry bookkeeping rules for a cash book and define a contra entry with an agricultural example. (8 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Debit Rule:** All cash and cheque receipts are posted on the left-hand Debit (DR) side.\n"
                            "2. **Credit Rule:** All cash and cheque payments are posted on the right-hand Credit (CR) side.\n"
                            "3. **Column Separation:** Physical cash is recorded in the Cash column; cheques/transfers in the Bank column.\n"
                            "4. **Contra Entry:** An internal transfer of funds between Cash and Bank columns recorded on both sides simultaneously with 'C' in Folio (e.g. depositing farm cash into bank)."
                        )
                    }
                }
            ]
        }
    ]
}

LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Financial Statements (Balance Sheets and Profit & Loss Accounts)",
    "lesson_title": "Financial Statements (Balance Sheets and Profit & Loss Accounts)",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Final Financial Statements",
            "blocks": [
                {
                    "block_type": "learning_goal",
                    "component_type": "learning_goal",
                    "title": "Module 3 Objectives",
                    "content": {
                        "text": (
                            "By the end of this lesson, you will be able to:\n\n"
                            "- Classify assets (Fixed vs Current) and liabilities (Current vs Long-Term).\n"
                            "- Construct a Farm Balance Sheet and calculate Net Capital.\n"
                            "- Evaluate farm solvency ($Total Assets > Total Liabilities$).\n"
                            "- Construct a Profit and Loss Account using opening valuation, closing valuation, expenditures, and receipts."
                        )
                    }
                },
                {
                    "block_type": "definition_card",
                    "component_type": "definition_card",
                    "title": "Financial Statement Definitions",
                    "content": {
                        "text": (
                            "- **Balance Sheet:** A financial statement showing total assets, liabilities, and net worth on a specific date.\n"
                            "- **Fixed Asset:** Permanent property not easily converted to cash (land, buildings).\n"
                            "- **Current Asset:** Liquid property easily converted to cash within 1 year (livestock, cash, debts receivable).\n"
                            "- **Long-Term Liability:** Debts payable over many years (>15 years).\n"
                            "- **Current Liability:** Short-term debts payable within 1 year."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Accounting Cycle Flowchart Diagram",
            "blocks": [
                {
                    "block_type": "suggested_diagram",
                    "component_type": "suggested_diagram",
                    "title": "Complete Farm Accounting Cycle",
                    "content": {
                        "text": "Flowchart showing the 5 stages of the farm accounting cycle from Source Documents to final Balance Sheet and Profit & Loss Accounts.",
                        "svg": SVG_ACCOUNTING_CYCLE
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Balance Sheet Equations & Solvency",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Balance Sheet Formulas & Solvency Rules",
                    "content": {
                        "text": (
                            "**Balance Sheet Equation:**\n"
                            "**Total Assets = Total Liabilities + Net Capital**\n\n"
                            "**Net Capital Formula:**\n"
                            "**Net Capital = Total Assets - Total Liabilities**\n\n"
                            "**Solvency Conditions:**\n"
                            "- **Solvent Farm:** Total Assets > Total Liabilities (Net Capital is positive).\n"
                            "- **Insolvent Farm:** Total Liabilities > Total Assets (Bankrupt state)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Worked Example: Katilo School Farm Balance Sheet",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Balance Sheet & Solvency Calculation",
                    "content": {
                        "text": (
                            "**Assets:** Land (800,000), Buildings (350,000), Fences (100,000), Livestock (180,000), Debts Receivable (45,000), Cash in Bank (60,000), Cash in Hand (15,000).\n"
                            "**Total Assets = KShs 1,550,000**\n\n"
                            "**Liabilities:** Land Loan (300,000), 15-Yr Bank Loan (150,000), Debts Payable (80,000), Friend Credit (20,000), Overdraft (40,000).\n"
                            "**Total Liabilities = KShs 590,000**\n\n"
                            "**Net Capital = 1,550,000 - 590,000 = KShs 960,000**\n"
                            "**Solvency Status:** Solvent (Total Assets exceed Total Liabilities by KShs 960,000)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Official Balance Sheet Table Format",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "comparison_table",
                    "title": "Katilo School Farm Balance Sheet (Dec 31, 2026)",
                    "content": {
                        "headers": ["Assets (KShs)", "Amount", "Liabilities & Net Capital (KShs)", "Amount"],
                        "rows": [
                            ["Fixed Assets: Land", "800,000", "Long-Term Liabilities: Land Loan", "300,000"],
                            ["Fixed Assets: Buildings", "350,000", "Long-Term Liabilities: 15-Yr Loan", "150,000"],
                            ["Fixed Assets: Fences", "100,000", "Current Liabilities: Debts Payable", "80,000"],
                            ["Current Assets: Livestock", "180,000", "Current Liabilities: Friend Credit", "20,000"],
                            ["Current Assets: Debts Receivable", "45,000", "Current Liabilities: Overdraft", "40,000"],
                            ["Current Assets: Cash in Bank", "60,000", "Net Capital (Balancing Factor)", "960,000"],
                            ["Current Assets: Cash in Hand", "15,000", "N/A", "N/A"],
                            ["TOTAL ASSETS", "1,550,000", "TOTAL LIABILITIES & NET CAPITAL", "1,550,000"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Profit and Loss Account Structure",
            "blocks": [
                {
                    "block_type": "concept_explanation",
                    "component_type": "concept_explanation",
                    "title": "Syllabus P&L Layout Rules",
                    "content": {
                        "text": (
                            "The official 8-4-4 Agriculture syllabus presents Profit & Loss Accounts in a unique format:\n"
                            "- **Left Column (Sales & Receipts):** Income during year + Debts receivable + Closing Valuation.\n"
                            "- **Right Column (Purchases & Expenses):** Opening Valuation + Expenditure during year + Debts payable.\n"
                            "- **Net Profit:** Total Sales & Receipts - Total Purchases & Expenses (entered on right side as balancing factor)."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Worked Example: Kitheko Farm Profit & Loss Account",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "worked_example",
                    "title": "Constructing P&L Statement",
                    "content": {
                        "text": (
                            "**Sales & Receipts (Left):**\n"
                            "Income (380,000) + Debts Receivable (50,000) + Closing Valuation (250,000) = **KShs 680,000**\n\n"
                            "**Purchases & Expenses (Right before profit):**\n"
                            "Opening Valuation (200,000) + Expenditures (150,000) + Debts Payable (30,000) = **KShs 380,000**\n\n"
                            "**Net Profit = 680,000 - 380,000 = KShs 300,000**\n"
                            "Entered on right side as 'Balance (being net profit)' to balance total at KShs 680,000."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Interactive Classification Exercise",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "knowledge_check",
                    "title": "Classifying Balance Sheet Items",
                    "content": {
                        "text": "Classify: (1) A 10-year orchard loan, (2) Dairy cattle, (3) Unpaid feed bill.",
                        "options": [
                            "A: (1) Long-Term Liability, (2) Current Asset, (3) Current Liability",
                            "B: (1) Current Liability, (2) Fixed Asset, (3) Long-Term Liability",
                            "C: (1) Long-Term Liability, (2) Fixed Asset, (3) Current Asset",
                            "D: (1) Fixed Asset, (2) Current Asset, (3) Current Liability"
                        ],
                        "correct_answer_index": 0,
                        "explanation": "A 10-year loan is a Long-Term Liability. Dairy cattle are Current Assets. Unpaid bills are Current Liabilities."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Module Summary",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "Core Module Summary",
                    "content": {
                        "text": (
                            "1. Balance sheets prove farm solvency by balancing Total Assets against Total Liabilities + Net Capital.\n"
                            "2. Profit & Loss accounts calculate net annual profit using Opening/Closing valuations, sales, and expenditures."
                        )
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "KCSE Examination Challenge",
            "blocks": [
                {
                    "block_type": "summary",
                    "component_type": "summary",
                    "title": "KCSE Model Essay: Profit & Loss Statement (12 Marks)",
                    "content": {
                        "text": (
                            "**Question:** Given Opening Valuation KShs 120,000, Closing Valuation KShs 150,000, Feeds/Chemicals KShs 80,000, Wages KShs 40,000, Egg sales KShs 210,000, Unpaid vet bill KShs 10,000, Debts receivable KShs 30,000, calculate net profit and construct the P&L Account. (12 Marks)\n\n"
                            "**Model Answer:**\n"
                            "1. **Sales & Receipts (Left):** 210,000 + 30,000 + 150,000 = **KShs 390,000**.\n"
                            "2. **Purchases & Expenses (Right):** 120,000 + (80,000 + 40,000) + 10,000 = **KShs 250,000**.\n"
                            "3. **Net Profit:** 390,000 - 250,000 = **KShs 140,000**.\n"
                            "4. **Statement Table:** Present Sales & Receipts on left (390,000) and Purchases & Expenses + Net Profit (140,000) on right balancing both totals at KShs 390,000."
                        )
                    }
                }
            ]
        }
    ]
}

TOPIC_5_LESSONS = [
    LESSON_1_DATA,
    LESSON_2_DATA,
    LESSON_3_DATA
]
