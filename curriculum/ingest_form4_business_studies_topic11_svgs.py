"""
VLearn Form 4 Business Studies — Topic 11: Ledger
Educational Dark-Mode SVG Vector Graphics
"""

SVG_T_ACCOUNT_STANDARD_LAYOUT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" fill="#0f172a" rx="16"/>
  
  <!-- Account Title Header -->
  <rect x="250" y="20" width="400" height="45" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="450" y="48" fill="#f8fafc" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">TITLE OF ACCOUNT (e.g. Cash Account)</text>

  <!-- Side Markers: Dr vs Cr -->
  <text x="40" y="48" fill="#38bdf8" font-family="sans-serif" font-size="18" font-weight="bold">Dr. (Debit Side)</text>
  <text x="800" y="48" fill="#f87171" font-family="sans-serif" font-size="18" font-weight="bold">Cr. (Credit Side)</text>

  <!-- Large T-Account Dividers -->
  <g transform="translate(40, 75)">
    <rect x="0" y="0" width="820" height="370" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <line x1="410" y1="0" x2="410" y2="370" stroke="#38bdf8" stroke-width="3"/>

    <!-- Left Header: Debit Columns -->
    <rect x="0" y="0" width="410" height="35" rx="12" fill="#0284c7"/>
    <text x="30" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Date</text>
    <text x="140" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Particulars</text>
    <text x="270" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Folio</text>
    <text x="350" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Shs.</text>

    <!-- Debit Column Guidelines -->
    <line x1="80" y1="35" x2="80" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="250" y1="35" x2="250" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="310" y1="35" x2="310" y2="370" stroke="#334155" stroke-width="1"/>

    <!-- Sample Debit Entry -->
    <text x="15" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">20-3 Feb 1</text>
    <text x="90" y="70" fill="#34d399" font-family="sans-serif" font-size="11">Capital (Start)</text>
    <text x="270" y="70" fill="#94a3b8" font-family="sans-serif" font-size="11">C1</text>
    <text x="330" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">70,000</text>

    <!-- Right Header: Credit Columns -->
    <rect x="410" y="0" width="410" height="35" rx="12" fill="#be123c"/>
    <text x="440" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Date</text>
    <text x="550" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Particulars</text>
    <text x="680" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Folio</text>
    <text x="760" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Shs.</text>

    <!-- Credit Column Guidelines -->
    <line x1="490" y1="35" x2="490" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="660" y1="35" x2="660" y2="370" stroke="#334155" stroke-width="1"/>
    <line x1="720" y1="35" x2="720" y2="370" stroke="#334155" stroke-width="1"/>

    <!-- Sample Credit Entry -->
    <text x="425" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">20-3 Feb 4</text>
    <text x="500" y="70" fill="#f87171" font-family="sans-serif" font-size="11">Equipment</text>
    <text x="680" y="70" fill="#94a3b8" font-family="sans-serif" font-size="11">E1</text>
    <text x="740" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">20,000</text>

    <text x="425" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">20-3 Feb 14</text>
    <text x="500" y="100" fill="#f87171" font-family="sans-serif" font-size="11">Bank Deposit</text>
    <text x="680" y="100" fill="#94a3b8" font-family="sans-serif" font-size="11">B1</text>
    <text x="740" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">40,000</text>
  </g>
</svg>"""

SVG_FIVE_POSTING_RULES_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">FIVE CORE BOOKKEEPING POSTING RULES</text>

  <g transform="translate(40, 65)">
    <!-- Header -->
    <rect x="0" y="0" width="820" height="40" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="120" y="25" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Account Type</text>
    <text x="320" y="25" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Nature of Account</text>
    <text x="540" y="25" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">To Increase (+)</text>
    <text x="720" y="25" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">To Decrease (-)</text>

    <!-- Row 1: Asset -->
    <rect x="0" y="50" width="820" height="55" rx="8" fill="#1e293b"/>
    <text x="120" y="83" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ASSET</text>
    <text x="320" y="83" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Property owned by business</text>
    <text x="540" y="83" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DEBIT (Dr)</text>
    <text x="720" y="83" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CREDIT (Cr)</text>

    <!-- Row 2: Liability -->
    <rect x="0" y="115" width="820" height="55" rx="8" fill="#1e293b"/>
    <text x="120" y="148" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">LIABILITY</text>
    <text x="320" y="148" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Debts owed to outsiders</text>
    <text x="540" y="148" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CREDIT (Cr)</text>
    <text x="720" y="148" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DEBIT (Dr)</text>

    <!-- Row 3: Capital -->
    <rect x="0" y="180" width="820" height="55" rx="8" fill="#1e293b"/>
    <text x="120" y="213" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CAPITAL</text>
    <text x="320" y="213" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Owner's equity / stake</text>
    <text x="540" y="213" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CREDIT (Cr)</text>
    <text x="720" y="213" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DEBIT (Dr)</text>

    <!-- Row 4: Expense -->
    <rect x="0" y="245" width="820" height="55" rx="8" fill="#1e293b"/>
    <text x="120" y="278" fill="#a78bfa" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">EXPENSE</text>
    <text x="320" y="278" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Operational running costs</text>
    <text x="540" y="278" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DEBIT (Dr)</text>
    <text x="720" y="278" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CREDIT (Cr)</text>

    <!-- Row 5: Revenue -->
    <rect x="0" y="310" width="820" height="55" rx="8" fill="#1e293b"/>
    <text x="120" y="343" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">REVENUE</text>
    <text x="320" y="343" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Trading gains / incomes</text>
    <text x="540" y="343" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CREDIT (Cr)</text>
    <text x="720" y="343" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">DEBIT (Dr)</text>
  </g>
</svg>"""

SVG_SPECIALIZED_STOCK_ACCOUNTS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">FOUR SPECIALIZED TRADING STOCK ACCOUNTS</text>

  <!-- Central Node: Stock Movements -->
  <circle cx="450" cy="220" r="70" fill="#0284c7" stroke="#38bdf8" stroke-width="3"/>
  <text x="450" y="215" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">STOCK</text>
  <text x="450" y="235" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">MOVEMENTS</text>

  <!-- 4 Corner Specialized Accounts -->
  <!-- 1. Purchases Account (Top-Left) -->
  <g transform="translate(40, 60)">
    <rect x="0" y="0" width="340" height="120" rx="12" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="35" rx="12" fill="#059669"/>
    <text x="170" y="23" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. PURCHASES ACCOUNT (Dr)</text>
    <text x="15" y="60" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold">• Action: Debited when goods are bought for resale.</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="sans-serif" font-size="11">Note: Fixed assets (computers/furniture) are NOT posted here!</text>
  </g>

  <!-- 2. Sales Account (Top-Right) -->
  <g transform="translate(520, 60)">
    <rect x="0" y="0" width="340" height="120" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="35" rx="12" fill="#0284c7"/>
    <text x="170" y="23" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. SALES ACCOUNT (Cr)</text>
    <text x="15" y="60" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">• Action: Credited when goods are sold to customers.</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="sans-serif" font-size="11">Represents main trading revenue earned by the firm.</text>
  </g>

  <!-- 3. Returns Inwards Account (Bottom-Left) -->
  <g transform="translate(40, 280)">
    <rect x="0" y="0" width="340" height="120" rx="12" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="35" rx="12" fill="#6d28d9"/>
    <text x="170" y="23" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">3. RETURNS INWARDS ACCOUNT (Dr)</text>
    <text x="15" y="60" fill="#a78bfa" font-family="sans-serif" font-size="12" font-weight="bold">• Action: Debited when customers return goods.</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="sans-serif" font-size="11">Reduces total sales and increases stock in shop.</text>
  </g>

  <!-- 4. Returns Outwards Account (Bottom-Right) -->
  <g transform="translate(520, 280)">
    <rect x="0" y="0" width="340" height="120" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect x="0" y="0" width="340" height="35" rx="12" fill="#d97706"/>
    <text x="170" y="23" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">4. RETURNS OUTWARDS ACCOUNT (Cr)</text>
    <text x="15" y="60" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">• Action: Credited when faulty goods returned to suppliers.</text>
    <text x="15" y="85" fill="#cbd5e1" font-family="sans-serif" font-size="11">Reduces total purchases and reduces supplier debt.</text>
  </g>
</svg>"""

SVG_FIVE_BALANCING_STEPS_FLOWCHART = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">FIVE PROCEDURAL STEPS FOR BALANCING OFF A T-ACCOUNT</text>

  <!-- Step 1 -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="740" height="60" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="20" fill="#0284c7"/>
    <text x="35" y="36" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1</text>
    <text x="75" y="25" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">Step 1: Total Both Sides Separately</text>
    <text x="75" y="45" fill="#cbd5e1" font-family="sans-serif" font-size="11">Add up all debit figures and all credit figures on scratch paper.</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(40, 145)">
    <rect x="0" y="0" width="740" height="60" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="20" fill="#059669"/>
    <text x="35" y="36" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2</text>
    <text x="75" y="25" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Step 2: Find the Mathematical Difference</text>
    <text x="75" y="45" fill="#cbd5e1" font-family="sans-serif" font-size="11">Subtract the smaller side total from the larger side total (Account Balance).</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(40, 220)">
    <rect x="0" y="0" width="740" height="60" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="20" fill="#d97706"/>
    <text x="35" y="36" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">3</text>
    <text x="75" y="25" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold">Step 3: Insert "Balance c/d" (Carried Down)</text>
    <text x="75" y="45" fill="#cbd5e1" font-family="sans-serif" font-size="11">Write calculated difference on smaller side as "Balance c/d" to force equality.</text>
  </g>

  <!-- Step 4 -->
  <g transform="translate(40, 295)">
    <rect x="0" y="0" width="740" height="60" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="20" fill="#6d28d9"/>
    <text x="35" y="36" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">4</text>
    <text x="75" y="25" fill="#a78bfa" font-family="sans-serif" font-size="13" font-weight="bold">Step 4: Draw Double Underscores Across Totals</text>
    <text x="75" y="45" fill="#cbd5e1" font-family="sans-serif" font-size="11">Write equal totals on both sides on same line and double-underline to close period.</text>
  </g>

  <!-- Step 5 -->
  <g transform="translate(40, 370)">
    <rect x="0" y="0" width="740" height="60" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <circle cx="35" cy="30" r="20" fill="#be123c"/>
    <text x="35" y="36" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">5</text>
    <text x="75" y="25" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">Step 5: Bring Balance Down as "Balance b/d" (Brought Down)</text>
    <text x="75" y="45" fill="#cbd5e1" font-family="sans-serif" font-size="11">Record balance on OPPOSITE side below totals as opening balance for next period.</text>
  </g>
</svg>"""

SVG_SIX_LEDGER_CLASSIFICATIONS_TREE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">SIX CLASSIFICATIONS OF ACCOUNTING LEDGER BOOKS</text>

  <!-- Central Root Node -->
  <rect x="330" y="60" width="240" height="45" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="450" y="88" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">THE LEDGER BOOK SYSTEM</text>

  <!-- 6 Specialized Branch Cards -->
  <!-- 1. Sales Ledger -->
  <g transform="translate(40, 130)">
    <rect x="0" y="0" width="240" height="90" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="120" y="25" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">1. Sales Ledger (Debtors)</text>
    <text x="120" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">Personal accounts of credit customers</text>
    <text x="120" y="68" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">e.g. Wanjiku A/C, Otieno A/C</text>
  </g>

  <!-- 2. Purchase Ledger -->
  <g transform="translate(330, 130)">
    <rect x="0" y="0" width="240" height="90" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="120" y="25" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">2. Purchase Ledger (Creditors)</text>
    <text x="120" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">Personal accounts of credit suppliers</text>
    <text x="120" y="68" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">e.g. Chama Motors, Nyamwea A/C</text>
  </g>

  <!-- 3. Cash Book -->
  <g transform="translate(620, 130)">
    <rect x="0" y="0" width="240" height="90" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="120" y="25" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">3. Cash Book</text>
    <text x="120" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">High-volume cash &amp; bank accounts</text>
    <text x="120" y="68" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">e.g. Cash Account, Bank Account</text>
  </g>

  <!-- 4. Nominal Ledger -->
  <g transform="translate(40, 250)">
    <rect x="0" y="0" width="240" height="90" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="120" y="25" fill="#a78bfa" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">4. Nominal Ledger</text>
    <text x="120" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">Operational expenses &amp; revenues</text>
    <text x="120" y="68" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">e.g. Wages, Rent, Commission A/C</text>
  </g>

  <!-- 5. Private Ledger -->
  <g transform="translate(330, 250)">
    <rect x="0" y="0" width="240" height="90" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="120" y="25" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">5. Private Ledger</text>
    <text x="120" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">Confidential owner equity accounts</text>
    <text x="120" y="68" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">e.g. Capital A/C, Drawings A/C</text>
  </g>

  <!-- 6. General Ledger -->
  <g transform="translate(620, 250)">
    <rect x="0" y="0" width="240" height="90" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="120" y="25" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">6. General Ledger</text>
    <text x="120" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="10" text-anchor="middle">Catch-all for real &amp; asset accounts</text>
    <text x="120" y="68" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">e.g. Buildings, Vehicles, Stock A/C</text>
  </g>

  <rect x="40" y="370" width="820" height="45" rx="8" fill="#0284c7" fill-opacity="0.25"/>
  <text x="450" y="398" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Purpose: Keeps the accounting filing system organized, scalable, and audit-ready!</text>
</svg>"""
