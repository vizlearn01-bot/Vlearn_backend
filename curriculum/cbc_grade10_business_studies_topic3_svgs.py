"""
VLearn CBC Grade 10 Business Studies — Topic 3: Budgeting in Business
High Precision Vector SVGs
"""

# =============================================================================
# SVG 1: Meaning, Foundations & Purpose of a Business Budget (Lesson 1)
# =============================================================================
SVG_BUDGET_FOUNDATIONS = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <!-- Background Container -->
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <!-- Header -->
  <text x="480" y="48" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Architecture &amp; Strategic Value of a Business Budget</text>
  <text x="480" y="72" font-size="12" fill="#94a3b8" text-anchor="middle">Financial Planning, Liquidity Management, and Operational Steering</text>

  <!-- Left: Cash Inflows (Receipts) -->
  <g transform="translate(50, 95)">
    <rect width="260" height="230" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="260" height="36" rx="10" fill="#059669"/>
    <text x="130" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CASH INFLOWS (Receipts)</text>
    
    <g transform="translate(18, 55)">
      <circle cx="8" cy="8" r="4" fill="#34d399"/>
      <text x="20" y="12" font-size="11" font-weight="bold" fill="#34d399">Cash Sales Revenue</text>
      <text x="20" y="28" font-size="9.5" fill="#cbd5e1">Daily sales to customers</text>
      
      <circle cx="8" cy="48" r="4" fill="#34d399"/>
      <text x="20" y="52" font-size="11" font-weight="bold" fill="#34d399">Debtor Collections</text>
      <text x="20" y="68" font-size="9.5" fill="#cbd5e1">Cash collected from credit buyers</text>

      <circle cx="8" cy="88" r="4" fill="#34d399"/>
      <text x="20" y="92" font-size="11" font-weight="bold" fill="#34d399">Capital / Grants / Loans</text>
      <text x="20" y="108" font-size="9.5" fill="#cbd5e1">Bank loans, owner equity, grants</text>

      <circle cx="8" cy="128" r="4" fill="#34d399"/>
      <text x="20" y="132" font-size="11" font-weight="bold" fill="#34d399">Other Cash Incomes</text>
      <text x="20" y="148" font-size="9.5" fill="#cbd5e1">Rent received, interest earned</text>
    </g>
  </g>

  <!-- Center: Financial Engine & Comparison -->
  <g transform="translate(340, 95)">
    <rect width="280" height="230" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="280" height="36" rx="10" fill="#0284c7"/>
    <text x="140" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">BUDGET BALANCE ENGINE</text>

    <!-- Formula Box -->
    <rect x="20" y="50" width="240" height="50" rx="8" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="130" y="70" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Net Cash Flow = Receipts - Payments</text>
    <text x="130" y="88" font-size="10" fill="#cbd5e1" text-anchor="middle">Closing Cash = Opening + Net Cash Flow</text>

    <!-- Surplus Badge -->
    <rect x="20" y="112" width="240" height="48" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="30" y="130" font-size="11" font-weight="bold" fill="#34d399">SURPLUS (Receipts &gt; Payments)</text>
    <text x="30" y="146" font-size="9.5" fill="#94a3b8">Provides liquidity buffer &amp; investment funds</text>

    <!-- Deficit Badge -->
    <rect x="20" y="168" width="240" height="48" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="30" y="186" font-size="11" font-weight="bold" fill="#fb7185">DEFICIT (Payments &gt; Receipts)</text>
    <text x="30" y="202" font-size="9.5" fill="#94a3b8">Signals cash crisis; requires loan/overdraft</text>
  </g>

  <!-- Right: Cash Outflows (Payments) -->
  <g transform="translate(650, 95)">
    <rect width="260" height="230" rx="12" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <rect width="260" height="36" rx="10" fill="#e11d48"/>
    <text x="130" y="24" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">CASH OUTFLOWS (Payments)</text>

    <g transform="translate(18, 55)">
      <circle cx="8" cy="8" r="4" fill="#fb7185"/>
      <text x="20" y="12" font-size="11" font-weight="bold" fill="#fb7185">Stock &amp; Raw Materials</text>
      <text x="20" y="28" font-size="9.5" fill="#cbd5e1">Purchases of goods for resale</text>

      <circle cx="8" cy="48" r="4" fill="#fb7185"/>
      <text x="20" y="52" font-size="11" font-weight="bold" fill="#fb7185">Operating Expenses</text>
      <text x="20" y="68" font-size="9.5" fill="#cbd5e1">Rent, electricity, water, transport</text>

      <circle cx="8" cy="88" r="4" fill="#fb7185"/>
      <text x="20" y="92" font-size="11" font-weight="bold" fill="#fb7185">Salaries &amp; Wages</text>
      <text x="20" y="108" font-size="9.5" fill="#cbd5e1">Employee labor remuneration</text>

      <circle cx="8" cy="128" r="4" fill="#fb7185"/>
      <text x="20" y="132" font-size="11" font-weight="bold" fill="#fb7185">Capital Expenditures</text>
      <text x="20" y="148" font-size="9.5" fill="#cbd5e1">Buying equipment, vans, machinery</text>
    </g>
  </g>

  <!-- Connecting Arrows -->
  <path d="M 310 210 L 340 210" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)" fill="none"/>
  <path d="M 650 210 L 620 210" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-red)" fill="none"/>

  <!-- Bottom: 4 Strategic Functions of a Budget -->
  <g transform="translate(50, 345)">
    <rect width="860" height="135" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="430" y="25" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">Four Core Managerial Functions of a Business Budget</text>

    <!-- 1. Roadmap -->
    <rect x="20" y="40" width="190" height="78" rx="8" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="115" y="60" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Financial Roadmap</text>
    <text x="115" y="80" font-size="9" fill="#cbd5e1" text-anchor="middle">Navigates future revenue</text>
    <text x="115" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">&amp; planned expenditures</text>

    <!-- 2. Cost Control -->
    <rect x="230" y="40" width="190" height="78" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="325" y="60" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">2. Spending Control</text>
    <text x="325" y="80" font-size="9" fill="#cbd5e1" text-anchor="middle">Detects overspending</text>
    <text x="325" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">early via limits</text>

    <!-- 3. Resource Allocation -->
    <rect x="440" y="40" width="190" height="78" rx="8" fill="#1e293b" stroke="#f59e0b"/>
    <text x="535" y="60" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">3. Resource Allocation</text>
    <text x="535" y="80" font-size="9" fill="#cbd5e1" text-anchor="middle">Channels scarce capital</text>
    <text x="535" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">to productive priority areas</text>

    <!-- 4. Accountability -->
    <rect x="650" y="40" width="190" height="78" rx="8" fill="#1e293b" stroke="#a855f7"/>
    <text x="745" y="60" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">4. Accountability</text>
    <text x="745" y="80" font-size="9" fill="#cbd5e1" text-anchor="middle">Holds managers and staff</text>
    <text x="745" y="96" font-size="9" fill="#94a3b8" text-anchor="middle">responsible for targets</text>
  </g>
</svg>
""".strip()


# =============================================================================
# SVG 2: Types of Business Budgets & Master Budget Hierarchy (Lesson 2)
# =============================================================================
SVG_MASTER_BUDGET_STRUCTURE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Master Budget Architecture &amp; Component Taxonomy</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Hierarchical Interdependence of Operating, Financial, and Flexibility Budgets</text>

  <!-- Top Apex: Master Budget -->
  <g transform="translate(320, 85)">
    <rect width="320" height="52" rx="10" fill="#0f172a" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="160" y="24" font-size="14" font-weight="bold" fill="#fbbf24" text-anchor="middle">MASTER BUDGET (The Comprehensive Plan)</text>
    <text x="160" y="42" font-size="10" fill="#cbd5e1" text-anchor="middle">Consolidates all operating and financial sub-budgets</text>
  </g>

  <!-- Branches Downward -->
  <path d="M 400 137 L 400 165 L 240 165 L 240 185" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <path d="M 560 137 L 560 165 L 720 165 L 720 185" stroke="#10b981" stroke-width="2" fill="none"/>

  <!-- Left Branch: Operating Budgets -->
  <g transform="translate(50, 185)">
    <rect width="380" height="235" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <rect width="380" height="32" rx="8" fill="#0284c7"/>
    <text x="190" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. OPERATING BUDGETS (Day-to-Day Activities)</text>

    <!-- Sales Budget Box (The Foundation) -->
    <rect x="15" y="42" width="350" height="38" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="25" y="60" font-size="11" font-weight="bold" fill="#fbbf24">★ Sales Budget (The Starting Point):</text>
    <text x="25" y="74" font-size="9.5" fill="#cbd5e1">Forecasts expected revenue; drives all operational activity</text>

    <!-- Downward arrow to production -->
    <text x="190" y="93" font-size="11" fill="#38bdf8" text-anchor="middle">↓</text>

    <!-- Production Budget Box -->
    <rect x="15" y="98" width="350" height="34" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="25" y="114" font-size="10.5" font-weight="bold" fill="#38bdf8">Production Budget:</text>
    <text x="25" y="126" font-size="9" fill="#cbd5e1">Calculates units to manufacture = Sales + Desired Ending - Opening</text>

    <!-- Manufacturing Sub-Budgets Grid -->
    <g transform="translate(15, 140)">
      <rect x="0" y="0" width="110" height="40" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="55" y="16" font-size="9.5" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Direct Materials</text>
      <text x="55" y="30" font-size="8.5" fill="#94a3b8" text-anchor="middle">Raw inputs</text>

      <rect x="120" y="0" width="110" height="40" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="175" y="16" font-size="9.5" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Direct Labor</text>
      <text x="175" y="30" font-size="8.5" fill="#94a3b8" text-anchor="middle">Wages &amp; hours</text>

      <rect x="240" y="0" width="110" height="40" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="295" y="16" font-size="9.5" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Mfg. Overhead</text>
      <text x="295" y="30" font-size="8.5" fill="#94a3b8" text-anchor="middle">Factory power/rent</text>
    </g>

    <!-- Selling & Admin Expenses -->
    <rect x="15" y="188" width="350" height="34" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="25" y="204" font-size="10" font-weight="bold" fill="#cbd5e1">Selling &amp; Admin Expense Budget:</text>
    <text x="25" y="216" font-size="8.5" fill="#94a3b8">Marketing, sales reps, office utilities, and admin costs</text>
  </g>

  <!-- Right Branch: Financial Budgets -->
  <g transform="translate(530, 185)">
    <rect width="380" height="235" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="380" height="32" rx="8" fill="#059669"/>
    <text x="190" y="21" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. FINANCIAL BUDGETS (Cash &amp; Balance Sheet)</text>

    <!-- Cash Budget Box (Crucial) -->
    <rect x="15" y="42" width="350" height="38" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="25" y="60" font-size="11" font-weight="bold" fill="#34d399">★ Cash Budget (Liquidity Steering):</text>
    <text x="25" y="74" font-size="9.5" fill="#cbd5e1">Forecasts cash receipts, cash payments &amp; closing cash balances</text>

    <!-- Capital Expenditure Budget -->
    <rect x="15" y="88" width="350" height="38" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="25" y="104" font-size="10.5" font-weight="bold" fill="#38bdf8">Capital Expenditure Budget (CapEx):</text>
    <text x="25" y="118" font-size="9" fill="#94a3b8">Plans long-term asset investments (vans, machinery, premises)</text>

    <!-- Budgeted Financial Statements -->
    <g transform="translate(15, 134)">
      <rect x="0" y="0" width="170" height="46" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="85" y="18" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Budgeted Income Stmt</text>
      <text x="85" y="34" font-size="8.5" fill="#94a3b8" text-anchor="middle">Projected Profit / Loss</text>

      <rect x="180" y="0" width="170" height="46" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="265" y="18" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Budgeted Balance Sheet</text>
      <text x="265" y="34" font-size="8.5" fill="#94a3b8" text-anchor="middle">Projected Assets &amp; Equity</text>
    </g>

    <!-- Key Distinction Note -->
    <rect x="15" y="188" width="350" height="34" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="25" y="203" font-size="9.5" font-weight="bold" fill="#fbbf24">Cash Budget vs. Budgeted Income Statement:</text>
    <text x="25" y="215" font-size="8.5" fill="#cbd5e1">Cash budget tracks liquid cash; Income stmt tracks accrual profit.</text>
  </g>

  <!-- Bottom: Flexibility Classification Badge -->
  <g transform="translate(50, 435)">
    <rect width="860" height="50" rx="8" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="30" y="22" font-size="11" font-weight="bold" fill="#c084fc">Flexibility Classifications:</text>
    <text x="30" y="38" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#38bdf8">Fixed (Static) Budget:</tspan> Prepared for single activity level.  |  <tspan font-weight="bold" fill="#34d399">Flexible Budget:</tspan> Adjusts dynamically across multiple output volumes (e.g. 60%, 80%, 100%).</text>
  </g>
</svg>
""".strip()


# =============================================================================
# SVG 3: Cash Budget Structure & The "Water Tank" Principle (Lesson 3)
# =============================================================================
SVG_CASH_BUDGET_MECHANICS = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Cash Budget Mechanics &amp; The Liquidity Water Tank Model</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Tracking Physical Cash Movements and Monthly Balances</text>

  <!-- Left: The Water Tank Analogy -->
  <g transform="translate(50, 90)">
    <rect width="360" height="390" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="180" y="28" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE WATER TANK LIQUIDITY ANALOGY</text>

    <!-- Inflow Pipe (Top) -->
    <rect x="140" y="45" width="80" height="30" fill="#059669" rx="4"/>
    <text x="180" y="64" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">INFLOW PIPE</text>
    <path d="M 180 75 L 180 95" stroke="#34d399" stroke-width="3" stroke-dasharray="4" marker-end="url(#arrow-green)"/>
    <text x="180" y="90" font-size="9" fill="#34d399" text-anchor="middle">Cash Sales + Debtors</text>

    <!-- Main Tank -->
    <rect x="70" y="105" width="220" height="180" rx="8" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
    
    <!-- Water Level Inside Tank -->
    <rect x="72" y="175" width="216" height="108" rx="6" fill="#0284c7" opacity="0.6"/>
    <line x1="72" y1="175" x2="288" y2="175" stroke="#38bdf8" stroke-width="2"/>
    
    <text x="180" y="145" font-size="11" font-weight="bold" fill="#93c5fd" text-anchor="middle">OPENING CASH BALANCE</text>
    <text x="180" y="160" font-size="9.5" fill="#cbd5e1" text-anchor="middle">(Cash in Hand + Bank at start of month)</text>
    
    <text x="180" y="225" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">CLOSING CASH BALANCE</text>
    <text x="180" y="242" font-size="9.5" fill="#e0f2fe" text-anchor="middle">= Opening + Inflows - Outflows</text>
    <text x="180" y="260" font-size="8.5" fill="#fcd34d" text-anchor="middle">➜ Carried Forward to Next Month</text>

    <!-- Outflow Pipe (Bottom Drain) -->
    <path d="M 180 285 L 180 310" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4"/>
    <rect x="140" y="310" width="80" height="30" fill="#e11d48" rx="4"/>
    <text x="180" y="329" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">DRAIN VALVE</text>
    <text x="180" y="358" font-size="9.5" fill="#fb7185" text-anchor="middle">Rent, Stock, Wages, Bills</text>
    <text x="180" y="373" font-size="9" fill="#94a3b8" text-anchor="middle">(Cash Outflows)</text>
  </g>

  <!-- Right: Mathematical Rules and Exclusions -->
  <g transform="translate(440, 90)">
    <!-- Core Mathematical Formulas -->
    <rect width="470" height="155" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="235" y="28" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">Core Cash Budget Formulas</text>

    <g transform="translate(20, 45)">
      <rect width="430" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="15" y="26" font-size="11" font-weight="bold" fill="#38bdf8">1. Net Cash Flow =</text>
      <text x="150" y="26" font-size="11" fill="#ffffff">Total Cash Receipts − Total Cash Payments</text>

      <rect y="50" width="430" height="42" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="15" y="76" font-size="11" font-weight="bold" fill="#38bdf8">2. Closing Balance =</text>
      <text x="150" y="76" font-size="11" fill="#ffffff">Opening Cash Balance + Net Cash Flow</text>
    </g>

    <!-- Golden Rules & Exclusions -->
    <g transform="translate(0, 170)">
      <rect width="470" height="220" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="235" y="28" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">CRITICAL CASH BUDGET RULES &amp; EXCLUSIONS</text>

      <!-- Rule 1: Physical Cash Only -->
      <g transform="translate(20, 45)">
        <rect width="430" height="48" rx="6" fill="#1e293b" stroke="#334155"/>
        <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#34d399">✓ Rule 1: Strict Cash Accounting Basis</text>
        <text x="12" y="36" font-size="9.5" fill="#cbd5e1">Record only physical cash receipts and disbursements when cash actually moves.</text>
      </g>

      <!-- Rule 2: Exclude Non-Cash Items -->
      <g transform="translate(20, 100)">
        <rect width="430" height="48" rx="6" fill="#1e293b" stroke="#f43f5e"/>
        <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#fb7185">✗ Rule 2: NEVER Include Depreciation or Non-Cash Items</text>
        <text x="12" y="36" font-size="9.5" fill="#cbd5e1">Depreciation is a book write-down; zero liquid cash leaves the business.</text>
      </g>

      <!-- Rule 3: Credit Timing -->
      <g transform="translate(20, 155)">
        <rect width="430" height="48" rx="6" fill="#1e293b" stroke="#38bdf8"/>
        <text x="12" y="20" font-size="10.5" font-weight="bold" fill="#38bdf8">⏳ Rule 3: Credit Sales Recorded Only Upon Collection</text>
        <text x="12" y="36" font-size="9.5" fill="#cbd5e1">Goods sold on 30-day credit in Jan appear as Cash Receipts in February.</text>
      </g>
    </g>
  </g>
</svg>
""".strip()


# =============================================================================
# SVG 4: Step-by-Step Multi-Month Cash Budget Workflow (Lesson 4)
# =============================================================================
SVG_MONTHLY_CASH_BUDGET = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Multi-Month Cash Budget: Baraka Mobile Repair Shop</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Step-by-Step Numerical Flow (January – February 2026)</text>

  <!-- Table Container -->
  <g transform="translate(50, 85)">
    <!-- Header Row -->
    <rect width="860" height="34" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="25" y="22" font-size="11.5" font-weight="bold" fill="#38bdf8">Cash Budget Line Item</text>
    <text x="560" y="22" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">January (KES)</text>
    <text x="740" y="22" font-size="11.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">February (KES)</text>

    <!-- Row 1: Opening Balance -->
    <rect y="38" width="860" height="32" fill="#1e293b" stroke="#334155"/>
    <text x="25" y="59" font-size="11" font-weight="bold" fill="#fbbf24">Opening Cash Balance (A)</text>
    <text x="560" y="59" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">20,000</text>
    <text x="740" y="59" font-size="11" font-weight="bold" fill="#fcd34d" text-anchor="middle">21,000 ⤶</text>

    <!-- Section Header: Inflows -->
    <rect y="74" width="860" height="24" fill="#065f46"/>
    <text x="25" y="90" font-size="10.5" font-weight="bold" fill="#34d399">CASH INFLOWS (Receipts)</text>

    <!-- Inflow items -->
    <rect y="100" width="860" height="24" fill="#1e293b"/>
    <text x="35" y="116" font-size="10" fill="#cbd5e1">• Cash Sales</text>
    <text x="560" y="116" font-size="10" fill="#ffffff" text-anchor="middle">30,000</text>
    <text x="740" y="116" font-size="10" fill="#ffffff" text-anchor="middle">45,000</text>

    <rect y="126" width="860" height="24" fill="#0f172a"/>
    <text x="35" y="142" font-size="10" fill="#cbd5e1">• Credit Collections (Debtors)</text>
    <text x="560" y="142" font-size="10" fill="#94a3b8" text-anchor="middle">—</text>
    <text x="740" y="142" font-size="10" fill="#ffffff" text-anchor="middle">10,000</text>

    <!-- Total Inflows -->
    <rect y="152" width="860" height="28" fill="#1e293b" stroke="#10b981"/>
    <text x="25" y="171" font-size="11" font-weight="bold" fill="#34d399">Total Cash Receipts (B)</text>
    <text x="560" y="171" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">30,000</text>
    <text x="740" y="171" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">55,000</text>

    <!-- Section Header: Outflows -->
    <rect y="184" width="860" height="24" fill="#881337"/>
    <text x="25" y="200" font-size="10.5" font-weight="bold" fill="#fb7185">CASH OUTFLOWS (Payments)</text>

    <!-- Outflow items -->
    <rect y="210" width="860" height="22" fill="#1e293b"/>
    <text x="35" y="226" font-size="9.5" fill="#cbd5e1">• Spare Parts Purchases</text>
    <text x="560" y="226" font-size="9.5" fill="#ffffff" text-anchor="middle">15,000</text>
    <text x="740" y="226" font-size="9.5" fill="#ffffff" text-anchor="middle">20,000</text>

    <rect y="234" width="860" height="22" fill="#0f172a"/>
    <text x="35" y="250" font-size="9.5" fill="#cbd5e1">• Rent Expense</text>
    <text x="560" y="250" font-size="9.5" fill="#ffffff" text-anchor="middle">8,000</text>
    <text x="740" y="250" font-size="9.5" fill="#ffffff" text-anchor="middle">8,000</text>

    <rect y="258" width="860" height="22" fill="#1e293b"/>
    <text x="35" y="274" font-size="9.5" fill="#cbd5e1">• Wages for Assistant</text>
    <text x="560" y="274" font-size="9.5" fill="#ffffff" text-anchor="middle">6,000</text>
    <text x="740" y="274" font-size="9.5" fill="#ffffff" text-anchor="middle">6,000</text>

    <rect y="282" width="860" height="22" fill="#0f172a"/>
    <text x="35" y="298" font-size="9.5" fill="#fbbf24">• Micro-Soldering Tool (CapEx)</text>
    <text x="560" y="298" font-size="9.5" fill="#94a3b8" text-anchor="middle">—</text>
    <text x="740" y="298" font-size="9.5" fill="#fcd34d" text-anchor="middle">12,000</text>

    <!-- Total Outflows -->
    <rect y="306" width="860" height="28" fill="#1e293b" stroke="#f43f5e"/>
    <text x="25" y="325" font-size="11" font-weight="bold" fill="#fb7185">Total Cash Payments (C)</text>
    <text x="560" y="325" font-size="11" font-weight="bold" fill="#fb7185" text-anchor="middle">29,000</text>
    <text x="740" y="325" font-size="11" font-weight="bold" fill="#fb7185" text-anchor="middle">46,000</text>

    <!-- Net Cash Flow -->
    <rect y="338" width="860" height="28" fill="#0f172a" stroke="#38bdf8"/>
    <text x="25" y="357" font-size="11" font-weight="bold" fill="#38bdf8">Net Cash Flow (D = B − C)</text>
    <text x="560" y="357" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">+1,000 (Surplus)</text>
    <text x="740" y="357" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">+9,000 (Surplus)</text>

    <!-- Closing Balance -->
    <rect y="370" width="860" height="32" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="25" y="391" font-size="12" font-weight="bold" fill="#ffffff">Closing Cash Balance (E = A + D)</text>
    <text x="560" y="391" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">21,000</text>
    <text x="740" y="391" font-size="13" font-weight="bold" fill="#fcd34d" text-anchor="middle">30,000</text>
  </g>

  <!-- Carry-forward Visual Arrow -->
  <path d="M 610 475 C 670 475, 680 145, 740 145" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3" fill="none" opacity="0.7"/>
</svg>
""".strip()


# =============================================================================
# SVG 5: Variance Analysis Framework & Directional Rules (Lesson 5)
# =============================================================================
SVG_VARIANCE_ANALYSIS_FRAMEWORK = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Financial Variance Analysis: Directional Rules &amp; Cost Control</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Comparing Actual Performance Against Budget to Steer Business Decisions</text>

  <!-- Formula Header -->
  <g transform="translate(260, 85)">
    <rect width="440" height="42" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="220" y="26" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">Variance = Actual Result − Budgeted Figure</text>
  </g>

  <!-- Left Column: Revenue / Inflows -->
  <g transform="translate(50, 145)">
    <rect width="410" height="230" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="410" height="34" rx="10" fill="#059669"/>
    <text x="205" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">REVENUE &amp; CASH INFLOW ITEMS</text>

    <!-- Favourable Condition -->
    <rect x="15" y="48" width="380" height="78" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="25" y="70" font-size="11.5" font-weight="bold" fill="#34d399">✓ Actual &gt; Budget ➜ FAVOURABLE (F)</text>
    <text x="25" y="90" font-size="10" fill="#cbd5e1">• Effect: More cash received than expected.</text>
    <text x="25" y="108" font-size="9.5" fill="#94a3b8">Example: Budgeted Sales KES 30k, Actual KES 34k ➜ +KES 4,000 (F)</text>

    <!-- Unfavourable Condition -->
    <rect x="15" y="136" width="380" height="78" rx="8" fill="#1e293b" stroke="#f43f5e"/>
    <text x="25" y="158" font-size="11.5" font-weight="bold" fill="#fb7185">✗ Actual &lt; Budget ➜ UNFAVOURABLE (U)</text>
    <text x="25" y="178" font-size="10" fill="#cbd5e1">• Effect: Less cash generated; liquidity shrinks.</text>
    <text x="25" y="196" font-size="9.5" fill="#94a3b8">Example: Budgeted Debtors KES 50k, Actual KES 45k ➜ -KES 5,000 (U)</text>
  </g>

  <!-- Right Column: Costs & Expenses -->
  <g transform="translate(500, 145)">
    <rect width="410" height="230" rx="12" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <rect width="410" height="34" rx="10" fill="#e11d48"/>
    <text x="205" y="22" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">EXPENDITURE &amp; CASH OUTFLOW ITEMS</text>

    <!-- Unfavourable Condition -->
    <rect x="15" y="48" width="380" height="78" rx="8" fill="#1e293b" stroke="#f43f5e"/>
    <text x="25" y="70" font-size="11.5" font-weight="bold" fill="#fb7185">✗ Actual &gt; Budget ➜ UNFAVOURABLE (U)</text>
    <text x="25" y="90" font-size="10" fill="#cbd5e1">• Effect: Overspending drains business cash reserves.</text>
    <text x="25" y="108" font-size="9.5" fill="#94a3b8">Example: Budgeted Parts KES 15k, Actual KES 18k ➜ -KES 3,000 (U)</text>

    <!-- Favourable Condition -->
    <rect x="15" y="136" width="380" height="78" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="25" y="158" font-size="11.5" font-weight="bold" fill="#34d399">✓ Actual &lt; Budget ➜ FAVOURABLE (F)</text>
    <text x="25" y="178" font-size="10" fill="#cbd5e1">• Effect: Cost savings preserve liquidity.</text>
    <text x="25" y="196" font-size="9.5" fill="#94a3b8">Example: Budgeted Electricity KES 2k, Actual KES 1.5k ➜ +KES 500 (F)</text>
  </g>

  <!-- Bottom: Corrective Action Decision Loop -->
  <g transform="translate(50, 395)">
    <rect width="860" height="85" rx="10" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="430" y="24" font-size="12" font-weight="bold" fill="#c084fc" text-anchor="middle">Management Action Protocol Following Variance Analysis</text>
    
    <g transform="translate(20, 38)">
      <rect width="395" height="34" rx="6" fill="#1e293b" stroke="#f43f5e"/>
      <text x="15" y="21" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#fb7185">For Unfavourable Variances:</tspan> Audit suppliers, eliminate waste, renegotiate rent/contracts.</text>
      
      <rect x="425" width="395" height="34" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="440" y="21" font-size="10" fill="#cbd5e1"><tspan font-weight="bold" fill="#34d399">For Favourable Variances:</tspan> Identify winning drivers (e.g. promo channels) and scale them.</text>
    </g>
  </g>
</svg>
""".strip()


# =============================================================================
# SVG 6: Budgetary Control & Accountability Cycle (Lesson 6)
# =============================================================================
SVG_BUDGETARY_CONTROL_CYCLE = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  
  <text x="480" y="46" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Continuous Budgetary Control &amp; Accountability Cycle</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Fostering Financial Discipline, Transparency, and Sustainable Enterprise Growth</text>

  <!-- Central Hub -->
  <circle cx="480" cy="265" r="75" fill="#0f172a" stroke="#fbbf24" stroke-width="2.5"/>
  <text x="480" y="245" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">BUDGETARY</text>
  <text x="480" y="265" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">GOVERNANCE</text>
  <text x="480" y="285" font-size="9" fill="#cbd5e1" text-anchor="middle">Discipline &amp; Integrity</text>
  <text x="480" y="298" font-size="8.5" fill="#38bdf8" text-anchor="middle">Zero Waste Culture</text>

  <!-- 4 Cycle Quadrants -->
  <!-- 1. Top-Left: Stage 1 - Plan & Forecast -->
  <g transform="translate(70, 95)">
    <rect width="280" height="120" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <rect width="280" height="28" rx="8" fill="#0284c7"/>
    <text x="140" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 1: PLAN &amp; FORECAST</text>
    <text x="15" y="48" font-size="10.5" font-weight="bold" fill="#38bdf8">• Establish Sales &amp; Cost Limits</text>
    <text x="15" y="64" font-size="9.5" fill="#cbd5e1">Gather market intelligence and historical data</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">to set realistic, achievable monetary targets.</text>
    <text x="15" y="102" font-size="9" fill="#94a3b8">Outcome: Approved Master &amp; Cash Budgets</text>
  </g>

  <!-- 2. Top-Right: Stage 2 - Execute & Record -->
  <g transform="translate(610, 95)">
    <rect width="280" height="120" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
    <rect width="280" height="28" rx="8" fill="#059669"/>
    <text x="140" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 2: EXECUTE &amp; MONITOR</text>
    <text x="15" y="48" font-size="10.5" font-weight="bold" fill="#34d399">• Daily Financial Implementation</text>
    <text x="15" y="64" font-size="9.5" fill="#cbd5e1">Record all actual cash receipts and payments</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">with strict receipts, invoices, and vouchers.</text>
    <text x="15" y="102" font-size="9" fill="#94a3b8">Outcome: Accurate Ledger &amp; Cash Records</text>
  </g>

  <!-- 3. Bottom-Right: Stage 3 - Compare & Analyze -->
  <g transform="translate(610, 310)">
    <rect width="280" height="120" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <rect width="280" height="28" rx="8" fill="#d97706"/>
    <text x="140" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 3: COMPARE &amp; ANALYZE</text>
    <text x="15" y="48" font-size="10.5" font-weight="bold" fill="#fbbf24">• Compute Financial Variances</text>
    <text x="15" y="64" font-size="9.5" fill="#cbd5e1">Compare Actual vs. Budget to calculate</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">Favourable (F) and Unfavourable (U) results.</text>
    <text x="15" y="102" font-size="9" fill="#94a3b8">Outcome: Comprehensive Variance Report</text>
  </g>

  <!-- 4. Bottom-Left: Stage 4 - Corrective Action & Revision -->
  <g transform="translate(70, 310)">
    <rect width="280" height="120" rx="10" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
    <rect width="280" height="28" rx="8" fill="#7c3aed"/>
    <text x="140" y="19" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">STAGE 4: CORRECT &amp; REVISE</text>
    <text x="15" y="48" font-size="10.5" font-weight="bold" fill="#c084fc">• Corrective Operational Action</text>
    <text x="15" y="64" font-size="9.5" fill="#cbd5e1">Hold department heads accountable, fix waste,</text>
    <text x="15" y="80" font-size="9.5" fill="#cbd5e1">and refine next quarter's budget estimates.</text>
    <text x="15" y="102" font-size="9" fill="#94a3b8">Outcome: Upgraded Continuous Plan</text>
  </g>

  <!-- Cycle Arrows connecting stages -->
  <!-- 1 -> 2 (Top) -->
  <path d="M 350 155 L 610 155" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrow-blue)"/>
  <text x="480" y="145" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Execute Plan</text>

  <!-- 2 -> 3 (Right) -->
  <path d="M 750 215 L 750 310" stroke="#10b981" stroke-width="2" stroke-dasharray="4"/>
  <text x="795" y="265" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Monthly Close</text>

  <!-- 3 -> 4 (Bottom) -->
  <path d="M 610 370 L 350 370" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <text x="480" y="390" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Variance Feedback</text>

  <!-- 4 -> 1 (Left) -->
  <path d="M 210 310 L 210 215" stroke="#a855f7" stroke-width="2" stroke-dasharray="4"/>
  <text x="160" y="265" font-size="9.5" font-weight="bold" fill="#c084fc" text-anchor="middle">Revise Budget</text>

  <!-- Bottom Core Takeaways Bar -->
  <g transform="translate(70, 445)">
    <rect width="820" height="42" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="410" y="26" font-size="10.5" fill="#cbd5e1" text-anchor="middle"><tspan font-weight="bold" fill="#fbbf24">Key Governance Principle:</tspan> Budgeting enforces transparent custodianship of enterprise &amp; cooperative funds.</text>
  </g>
</svg>
""".strip()
