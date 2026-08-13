"""
VLearn Form 4 Business Studies — Topic 13: Cash Book
Educational Dark-Mode SVG Vector Graphics
"""

SVG_SINGLE_COLUMN_CASH_BOOK_LAYOUT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" fill="#0f172a" rx="16"/>
  
  <!-- Header Title -->
  <rect x="250" y="20" width="400" height="45" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="450" y="48" fill="#f8fafc" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">SINGLE-COLUMN CASH BOOK (CASH ACCOUNT)</text>

  <!-- Side Markers -->
  <text x="40" y="48" fill="#38bdf8" font-family="sans-serif" font-size="18" font-weight="bold">Dr. (Receipts / Inflows)</text>
  <text x="800" y="48" fill="#f87171" font-family="sans-serif" font-size="18" font-weight="bold">Cr. (Payments / Outflows)</text>

  <!-- Main Table Container -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="820" height="370" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <line x1="410" y1="0" x2="410" y2="370" stroke="#38bdf8" stroke-width="3"/>

    <!-- Left Header: Debit Columns -->
    <rect x="0" y="0" width="410" height="35" rx="12" fill="#0284c7"/>
    <text x="25" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Date</text>
    <text x="130" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Details (Particulars)</text>
    <text x="270" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">L.F.</text>
    <text x="340" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Amount (Sh)</text>

    <!-- Debit Column Lines -->
    <line x1="75" y1="35" x2="75" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="255" y1="35" x2="255" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="315" y1="35" x2="315" y2="370" stroke="#334155" stroke-width="1"/>

    <!-- Debit Entries -->
    <text x="10" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">Feb 1</text>
    <text x="85" y="70" fill="#34d399" font-family="sans-serif" font-size="11">Capital</text>
    <text x="270" y="70" fill="#94a3b8" font-family="sans-serif" font-size="11">G.L.</text>
    <text x="330" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">100,000</text>

    <text x="10" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">Feb 5</text>
    <text x="85" y="100" fill="#34d399" font-family="sans-serif" font-size="11">Sales</text>
    <text x="270" y="100" fill="#94a3b8" font-family="sans-serif" font-size="11">G.L.</text>
    <text x="330" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">40,000</text>

    <!-- Right Header: Credit Columns -->
    <rect x="410" y="0" width="410" height="35" rx="12" fill="#be123c"/>
    <text x="435" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Date</text>
    <text x="540" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Details (Particulars)</text>
    <text x="680" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">L.F.</text>
    <text x="750" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Amount (Sh)</text>

    <!-- Credit Column Lines -->
    <line x1="485" y1="35" x2="485" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="665" y1="35" x2="665" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="725" y1="35" x2="725" y2="370" stroke="#334155" stroke-width="1"/>

    <!-- Credit Entries -->
    <text x="420" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">Feb 3</text>
    <text x="495" y="70" fill="#f87171" font-family="sans-serif" font-size="11">Rent</text>
    <text x="680" y="70" fill="#94a3b8" font-family="sans-serif" font-size="11">G.L.</text>
    <text x="740" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">20,000</text>
  </g>
</svg>"""

SVG_TWO_COLUMN_CASH_BOOK_LAYOUT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">TWO-COLUMN CASH BOOK (CASH &amp; BANK SIDE-BY-SIDE)</text>

  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="820" height="380" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <line x1="410" y1="0" x2="410" y2="380" stroke="#38bdf8" stroke-width="3"/>

    <!-- Header Left -->
    <rect x="0" y="0" width="410" height="40" rx="12" fill="#0284c7"/>
    <text x="15" y="25" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Date</text>
    <text x="110" y="25" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Details</text>
    <text x="220" y="25" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">L.F.</text>
    <text x="270" y="25" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">Cash (Sh)</text>
    <text x="350" y="25" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">Bank (Sh)</text>

    <!-- Header Right -->
    <rect x="410" y="0" width="410" height="40" rx="12" fill="#be123c"/>
    <text x="425" y="25" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Date</text>
    <text x="520" y="25" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Details</text>
    <text x="630" y="25" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">L.F.</text>
    <text x="680" y="25" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold">Cash (Sh)</text>
    <text x="760" y="25" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">Bank (Sh)</text>

    <!-- Column Dividers -->
    <line x1="250" y1="40" x2="250" y2="380" stroke="#334155" stroke-width="1"/>
    <line x1="330" y1="40" x2="330" y2="380" stroke="#334155" stroke-width="1"/>
    <line x1="660" y1="40" x2="660" y2="380" stroke="#334155" stroke-width="1"/>
    <line x1="740" y1="40" x2="740" y2="380" stroke="#334155" stroke-width="1"/>

    <!-- Row Entries -->
    <text x="10" y="80" fill="#cbd5e1" font-family="sans-serif" font-size="11">Mar 1</text>
    <text x="75" y="80" fill="#34d399" font-family="sans-serif" font-size="11">Bal b/d</text>
    <text x="260" y="80" fill="#cbd5e1" font-family="sans-serif" font-size="11">13,200</text>
    <text x="340" y="80" fill="#cbd5e1" font-family="sans-serif" font-size="11">56,000</text>

    <text x="420" y="80" fill="#cbd5e1" font-family="sans-serif" font-size="11">Mar 12</text>
    <text x="480" y="80" fill="#f87171" font-family="sans-serif" font-size="11">Creditor</text>
    <text x="750" y="80" fill="#cbd5e1" font-family="sans-serif" font-size="11">8,200</text>

    <text x="10" y="110" fill="#cbd5e1" font-family="sans-serif" font-size="11">Mar 2</text>
    <text x="75" y="110" fill="#34d399" font-family="sans-serif" font-size="11">Sales</text>
    <text x="260" y="110" fill="#cbd5e1" font-family="sans-serif" font-size="11">12,000</text>

    <text x="420" y="110" fill="#cbd5e1" font-family="sans-serif" font-size="11">Mar 31</text>
    <text x="480" y="110" fill="#f87171" font-family="sans-serif" font-size="11">Rent</text>
    <text x="670" y="110" fill="#cbd5e1" font-family="sans-serif" font-size="11">7,500</text>

    <!-- Balancing Double Lines -->
    <line x1="250" y1="310" x2="400" y2="310" stroke="#cbd5e1" stroke-width="1"/>
    <line x1="660" y1="310" x2="810" y2="310" stroke="#cbd5e1" stroke-width="1"/>
    <text x="260" y="330" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">25,200</text>
    <text x="340" y="330" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">80,500</text>
    <text x="670" y="330" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">25,200</text>
    <text x="750" y="330" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">80,500</text>
    <line x1="250" y1="340" x2="400" y2="340" stroke="#38bdf8" stroke-width="2"/>
    <line x1="660" y1="340" x2="810" y2="340" stroke="#38bdf8" stroke-width="2"/>
  </g>
</svg>"""

SVG_THREE_COLUMN_CASH_BOOK_DISCOUNT_RULES = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">THREE-COLUMN CASH BOOK &amp; THE DISCOUNT GOLDEN RULE</text>

  <!-- Left Box: Discount Allowed vs Received -->
  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="390" height="380" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="40" rx="12" fill="#0284c7"/>
    <text x="195" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DEBIT SIDE: DISCOUNT ALLOWED (Dr)</text>
    <text x="20" y="70" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold">• Nature: Expense to the business</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Granted to credit customers (debtors) for prompt payment</text>

    <!-- Rule Badge -->
    <rect x="20" y="130" width="350" height="100" rx="8" fill="#0284c7" fill-opacity="0.2"/>
    <text x="195" y="160" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">GOLDEN DISCOUNT RULE</text>
    <text x="195" y="185" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">Discount columns are NEVER balanced against each other!</text>
    <text x="195" y="205" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">No 'Balance c/d' is EVER written for discounts!</text>

    <text x="20" y="260" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">• Month-End Action: Simply total the column (e.g. Sh 7,720)</text>
    <text x="20" y="285" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Post total directly to General Ledger Discount Allowed A/C</text>
  </g>

  <!-- Right Box: Discount Received -->
  <g transform="translate(470, 65)">
    <rect x="0" y="0" width="390" height="380" rx="12" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="40" rx="12" fill="#be123c"/>
    <text x="195" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CREDIT SIDE: DISCOUNT RECEIVED (Cr)</text>
    <text x="20" y="70" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">• Nature: Revenue / income to the business</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Received from suppliers (creditors) for prompt settlement</text>

    <!-- Contrast Box -->
    <rect x="20" y="130" width="350" height="100" rx="8" fill="#be123c" fill-opacity="0.2"/>
    <text x="195" y="160" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CASH &amp; BANK COLUMNS ARE BALANCED</text>
    <text x="195" y="185" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">Cash and Bank columns ARE balanced using Balance c/d!</text>
    <text x="195" y="205" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">Cash/Bank opening balances brought down as Balance b/d</text>

    <text x="20" y="260" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold">• Month-End Action: Simply total the column (e.g. Sh 1,600)</text>
    <text x="20" y="285" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Post total directly to General Ledger Discount Received A/C</text>
  </g>
</svg>"""

SVG_CONTRA_ENTRIES_FLOWCHART = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">CONTRA ENTRIES: INTERNAL TRANSFERS MARKED WITH 'C'</text>

  <!-- Left Node: Cash Till -->
  <g transform="translate(60, 100)">
    <rect x="0" y="0" width="260" height="240" rx="14" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="260" height="40" rx="14" fill="#059669"/>
    <text x="130" y="25" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">OFFICE CASH TILL</text>
    <text x="130" y="100" fill="#34d399" font-family="sans-serif" font-size="40" font-weight="bold" text-anchor="middle">KSh</text>
    <text x="130" y="150" fill="#cbd5e1" font-family="sans-serif" font-size="13" text-anchor="middle">Physical Cash in Hand</text>
    <text x="130" y="180" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Folio Symbol: "C" in L.F.</text>
  </g>

  <!-- Right Node: Bank Vault -->
  <g transform="translate(580, 100)">
    <rect x="0" y="0" width="260" height="240" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="260" height="40" rx="14" fill="#0284c7"/>
    <text x="130" y="25" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">BANK ACCOUNT</text>
    <text x="130" y="100" fill="#38bdf8" font-family="sans-serif" font-size="36" font-weight="bold" text-anchor="middle">BANK</text>
    <text x="130" y="150" fill="#cbd5e1" font-family="sans-serif" font-size="13" text-anchor="middle">Commercial Bank Account</text>
    <text x="130" y="180" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Folio Symbol: "C" in L.F.</text>
  </g>

  <!-- Transfer Arrows -->
  <!-- Top Arrow: Cash Deposited into Bank -->
  <path d="M 330 160 L 560 160" stroke="#34d399" stroke-width="4" stroke-dasharray="6,6"/>
  <polygon points="570,160 555,150 555,170" fill="#34d399"/>
  <rect x="370" y="125" width="160" height="30" rx="6" fill="#059669"/>
  <text x="450" y="145" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">1. Cash Banked (Cr Cash, Dr Bank)</text>

  <!-- Bottom Arrow: Cash Withdrawn from Bank -->
  <path d="M 570 280 L 340 280" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6,6"/>
  <polygon points="330,280 345,270 345,290" fill="#38bdf8"/>
  <rect x="370" y="295" width="160" height="30" rx="6" fill="#0284c7"/>
  <text x="450" y="315" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">2. Cash Withdrawn (Dr Cash, Cr Bank)</text>

  <rect x="150" y="380" width="600" height="45" rx="8" fill="#0284c7" fill-opacity="0.25"/>
  <text x="450" y="408" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Definition: Both debit and credit double entries are completed within the Cash Book itself!</text>
</svg>"""

SVG_DISHONOURED_CHEQUE_REVERSAL_FLOW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">ACCOUNTING REVERSAL OF A DISHONOURED (BOUNCED) CHEQUE</text>

  <!-- Step 1: Cheque Receipt -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="240" height="120" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="120" y="25" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">1. Cheque Received from Debtor</text>
    <text x="120" y="55" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">Debtor (Mueni) pays Sh 2,050</text>
    <text x="120" y="85" fill="#34d399" font-family="sans-serif" font-size="11" text-anchor="middle">Entry: DEBIT Bank Column</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <path d="M 290 130 L 320 130" stroke="#64748b" stroke-width="3"/>

  <!-- Step 2: Bank Presentation & Dishonour -->
  <g transform="translate(330, 70)">
    <rect x="0" y="0" width="240" height="120" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="120" y="25" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">2. Bank Refuses Payment</text>
    <text x="120" y="55" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DISHONOURED / BOUNCED</text>
    <text x="120" y="85" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">(Insufficient funds / signature mismatch)</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <path d="M 580 130 L 610 130" stroke="#64748b" stroke-width="3"/>

  <!-- Step 3: Reversal Entry -->
  <g transform="translate(620, 70)">
    <rect x="0" y="0" width="240" height="120" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="120" y="25" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">3. Reversal Entry in Cash Book</text>
    <text x="120" y="55" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">Write Debtor Name in details</text>
    <text x="120" y="85" fill="#f87171" font-family="sans-serif" font-size="11" text-anchor="middle">Entry: CREDIT Bank Column</text>
  </g>

  <!-- Consequence Summary Box -->
  <g transform="translate(40, 230)">
    <rect x="0" y="0" width="820" height="180" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="410" y="30" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">DUAL DUAL-ENTRY IMPACT OF DISHONOURED CHEQUES</text>
    
    <text x="30" y="70" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">1. Impact on Cash Book (Bank Column):</text>
    <text x="50" y="95" fill="#cbd5e1" font-family="sans-serif" font-size="12">Credited in Bank column to reduce bank balance by bounced amount (prevents false liquidity).</text>

    <text x="30" y="130" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">2. Impact on Sales Ledger (Debtor's Personal Account):</text>
    <text x="50" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="12">Debited in debtor's account (e.g. Mueni A/C) to revive their liability so they still owe the money!</text>
  </g>
</svg>"""
