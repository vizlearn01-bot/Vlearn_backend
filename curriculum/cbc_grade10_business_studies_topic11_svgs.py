"""
VLearn CBC Grade 10 Business Studies — Topic 11: Public Finance
Vector SVG Diagram Definitions (Responsive Dark-Mode Optimized, viewBox='0 0 960 520')
"""

# =============================================================================
# SVG 1: Public Finance Architecture & Budget Sequence (Lesson 1)
# =============================================================================
SVG_PUBLIC_FINANCE_ARCHITECTURE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>
    <linearGradient id="revGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0EA5E9" />
      <stop offset="100%" stop-color="#0284C7" />
    </linearGradient>
    <linearGradient id="expGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <linearGradient id="govGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <filter id="cardShadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="520" fill="url(#bgGrad1)" rx="16" />

  <!-- Header -->
  <text x="480" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#F8FAFC" text-anchor="middle" letter-spacing="0.5">PUBLIC FINANCE SYSTEM &amp; BUDGET FLOW IN KENYA</text>
  <text x="480" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94A3B8" text-anchor="middle">Government Resource Mobilization, Resource Allocation &amp; Budget Sequence</text>

  <!-- Central Government Treasury Core -->
  <g transform="translate(340, 95)" filter="url(#cardShadow1)">
    <rect width="280" height="85" rx="12" fill="url(#govGrad)" stroke="#34D399" stroke-width="2" />
    <text x="140" y="32" font-family="system-ui, sans-serif" font-size="16" font-weight="700" fill="#FFFFFF" text-anchor="middle">NATIONAL TREASURY</text>
    <text x="140" y="52" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#D1FAE5" text-anchor="middle">Sovereign Financial Planning &amp; Allocation</text>
    <text x="140" y="70" font-family="system-ui, sans-serif" font-size="10" fill="#ECFDF5" text-anchor="middle">Sequence: Needs Assessment → Revenue Mobilization</text>
  </g>

  <!-- Left Column: Revenue Inflows -->
  <g transform="translate(40, 205)" filter="url(#cardShadow1)">
    <rect width="400" height="280" rx="12" fill="#1E293B" stroke="#38BDF8" stroke-width="2" />
    <rect x="0" y="0" width="400" height="42" rx="12" fill="url(#revGrad)" />
    <text x="200" y="27" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">GOVERNMENT REVENUE INFLOWS (T)</text>
    
    <!-- Item 1: Direct Taxes -->
    <rect x="20" y="58" width="360" height="46" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1" />
    <circle cx="42" cy="81" r="12" fill="#0284C7" />
    <text x="42" y="86" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="65" y="76" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#E2E8F0">Direct Taxes (Unshiftable Burden)</text>
    <text x="65" y="93" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">PAYE (Salaries), Corporate Tax (30%), Capital Gains Tax (15%)</text>

    <!-- Item 2: Indirect Taxes -->
    <rect x="20" y="112" width="360" height="46" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1" />
    <circle cx="42" cy="135" r="12" fill="#0284C7" />
    <text x="42" y="140" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
    <text x="65" y="130" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#E2E8F0">Indirect Taxes (Shiftable to Consumers)</text>
    <text x="65" y="147" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">VAT (16%), Excise Duty (Sin Taxes), Customs &amp; Import Duties</text>

    <!-- Item 3: Non-Tax Revenues -->
    <rect x="20" y="166" width="360" height="46" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1" />
    <circle cx="42" cy="189" r="12" fill="#0284C7" />
    <text x="42" y="194" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
    <text x="65" y="184" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#E2E8F0">Non-Tax &amp; Commercial Revenues</text>
    <text x="65" y="201" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Court Fines, Trade Licenses, Park Fees, Parastatal Dividends</text>

    <!-- Item 4: Public Debt -->
    <rect x="20" y="220" width="360" height="46" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1" />
    <circle cx="42" cy="243" r="12" fill="#0284C7" />
    <text x="42" y="248" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
    <text x="65" y="238" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#E2E8F0">Public Debt &amp; External Grants</text>
    <text x="65" y="255" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Treasury Bills/Bonds (Domestic) + World Bank/IMF/Eurobond</text>
  </g>

  <!-- Right Column: Expenditure Outflows -->
  <g transform="translate(520, 205)" filter="url(#cardShadow1)">
    <rect width="400" height="280" rx="12" fill="#1E293B" stroke="#F59E0B" stroke-width="2" />
    <rect x="0" y="0" width="400" height="42" rx="12" fill="url(#expGrad)" />
    <text x="200" y="27" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">GOVERNMENT EXPENDITURE OUTFLOWS (G)</text>

    <!-- Recurrent Expenditure Section -->
    <rect x="20" y="58" width="360" height="98" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1" />
    <rect x="20" y="58" width="6" height="98" rx="3" fill="#F59E0B" />
    <text x="35" y="78" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FDE68A">Recurrent Expenditure (Operational)</text>
    <text x="35" y="96" font-family="system-ui, sans-serif" font-size="11" fill="#CBD5E1">• Civil Service Salaries (Teachers, Police, Doctors)</text>
    <text x="35" y="114" font-family="system-ui, sans-serif" font-size="11" fill="#CBD5E1">• Hospital Consumables, Fuel &amp; Office Electricity</text>
    <text x="35" y="132" font-family="system-ui, sans-serif" font-size="11" fill="#CBD5E1">• Public Debt Interest Service (Consolidated Fund)</text>
    <text x="35" y="148" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Characteristic: Short-term; does not create permanent physical assets.</text>

    <!-- Development Expenditure Section -->
    <rect x="20" y="168" width="360" height="98" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1" />
    <rect x="20" y="168" width="6" height="98" rx="3" fill="#10B981" />
    <text x="35" y="188" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#A7F3D0">Development Expenditure (Capital Assets)</text>
    <text x="35" y="206" font-family="system-ui, sans-serif" font-size="11" fill="#CBD5E1">• Infrastructure: Thika Superhighway, SGR, Lamu Port</text>
    <text x="35" y="224" font-family="system-ui, sans-serif" font-size="11" fill="#CBD5E1">• Energy &amp; Water: Olkaria Geothermal, Thwake Multi-purpose Dam</text>
    <text x="35" y="242" font-family="system-ui, sans-serif" font-size="11" fill="#CBD5E1">• Modern Market Hubs &amp; CBC School Laboratories</text>
    <text x="35" y="258" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Characteristic: Long-term; builds productive national capital capacity.</text>
  </g>

  <!-- Flow Connectors -->
  <path d="M 240 205 L 240 137 L 340 137" fill="none" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6,4" />
  <polygon points="338,132 348,137 338,142" fill="#38BDF8" />
  <text x="280" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8">Revenue Flow</text>

  <path d="M 620 137 L 720 137 L 720 205" fill="none" stroke="#F59E0B" stroke-width="3" stroke-dasharray="6,4" />
  <polygon points="715,203 720,213 725,203" fill="#F59E0B" />
  <text x="640" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#F59E0B">Spending Flow</text>
</svg>"""

# =============================================================================
# SVG 2: Adam Smith's Canons of Taxation Matrix (Lesson 2)
# =============================================================================
SVG_CANONS_OF_TAXATION_FRAMEWORK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16" />
      <stop offset="100%" stop-color="#172033" />
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.3" />
    </filter>
  </defs>

  <rect width="960" height="520" fill="url(#bgGrad2)" rx="16" />

  <!-- Header -->
  <text x="480" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#F8FAFC" text-anchor="middle">ADAM SMITH'S 4 CANONS (PRINCIPLES) OF TAXATION</text>
  <text x="480" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#94A3B8" text-anchor="middle">Essential Pillars of an Efficient, Equitable and Modern Sovereign Tax System</text>

  <!-- 2x2 Grid of Principles -->

  <!-- 1. Equity (Top-Left) -->
  <g transform="translate(40, 95)" filter="url(#shadow2)">
    <rect width="420" height="185" rx="12" fill="#1E293B" stroke="#6366F1" stroke-width="2" />
    <rect x="0" y="0" width="420" height="38" rx="12" fill="#4F46E5" />
    <text x="210" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. PRINCIPLE OF EQUITY (FAIRNESS)</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#A5B4FC">Core Rule: Ability-to-Pay Principle</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Tax burden is distributed proportionally to wealth &amp; earnings.</text>
    <text x="20" y="105" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Vertical Equity: High earners pay higher percentage rates.</text>
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Horizontal Equity: Persons with equal income pay equal taxes.</text>
    <rect x="15" y="140" width="390" height="32" rx="6" fill="#0F172A" stroke="#312E81" />
    <text x="210" y="160" font-family="system-ui, sans-serif" font-size="10.5" fill="#C7D2FE" text-anchor="middle">Kenyan Application: Progressive PAYE Tax Bands (10% to 35%)</text>
  </g>

  <!-- 2. Certainty (Top-Right) -->
  <g transform="translate(500, 95)" filter="url(#shadow2)">
    <rect width="420" height="185" rx="12" fill="#1E293B" stroke="#0EA5E9" stroke-width="2" />
    <rect x="0" y="0" width="420" height="38" rx="12" fill="#0284C7" />
    <text x="210" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. PRINCIPLE OF CERTAINTY</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#7DD3FC">Core Rule: No Arbitrary or Secret Tax Levies</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Amount, payment deadline, and assessment rules are explicit.</text>
    <text x="20" y="105" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Taxpayers and businesses can forecast tax costs accurately.</text>
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Prevents corruption, extortion, and sudden tax surprises.</text>
    <rect x="15" y="140" width="390" height="32" rx="6" fill="#0F172A" stroke="#075985" />
    <text x="210" y="160" font-family="system-ui, sans-serif" font-size="10.5" fill="#BAE6FD" text-anchor="middle">Kenyan Application: Annual Finance Acts &amp; Published KRA Tariffs</text>
  </g>

  <!-- 3. Convenience (Bottom-Left) -->
  <g transform="translate(40, 305)" filter="url(#shadow2)">
    <rect width="420" height="185" rx="12" fill="#1E293B" stroke="#10B981" stroke-width="2" />
    <rect x="0" y="0" width="420" height="38" rx="12" fill="#059669" />
    <text x="210" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. PRINCIPLE OF CONVENIENCE</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#6EE7B7">Core Rule: Seamless Timing &amp; Method of Remittance</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Taxes are collected at the moment taxpayer has funds.</text>
    <text x="20" y="105" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Simple channels minimize friction, long queues, and stress.</text>
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Frictionless payments dramatically increase voluntary compliance.</text>
    <rect x="15" y="140" width="390" height="32" rx="6" fill="#0F172A" stroke="#065F46" />
    <text x="210" y="160" font-family="system-ui, sans-serif" font-size="10.5" fill="#A7F3D0" text-anchor="middle">Kenyan Application: Supermarket Point-of-Sale VAT &amp; M-Pesa KRA Paybill</text>
  </g>

  <!-- 4. Economy (Bottom-Right) -->
  <g transform="translate(500, 305)" filter="url(#shadow2)">
    <rect width="420" height="185" rx="12" fill="#1E293B" stroke="#F59E0B" stroke-width="2" />
    <rect x="0" y="0" width="420" height="38" rx="12" fill="#D97706" />
    <text x="210" y="25" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. PRINCIPLE OF ECONOMY (EFFICIENCY)</text>
    <text x="20" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FDE68A">Core Rule: Low Collection Cost Ratio</text>
    <text x="20" y="85" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Administrative cost to collect tax &lt;&lt; Revenue harvested.</text>
    <text x="20" y="105" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Spending KES 90 to collect KES 100 violates this canon.</text>
    <text x="20" y="125" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Automated online portals drastically cut administrative waste.</text>
    <rect x="15" y="140" width="390" height="32" rx="6" fill="#0F172A" stroke="#78350F" />
    <text x="210" y="160" font-family="system-ui, sans-serif" font-size="10.5" fill="#FEF08A" text-anchor="middle">Kenyan Application: KRA iTax Digital Returns &amp; Electronic TIMS/eTIMS</text>
  </g>
</svg>"""

# =============================================================================
# SVG 3: Direct vs. Indirect Taxes & Rate Progression Spectrum (Lesson 3)
# =============================================================================
SVG_TAX_STRUCTURE_AND_PROGRESSION = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" />
      <stop offset="100%" stop-color="#1C2541" />
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.35" />
    </filter>
  </defs>

  <rect width="960" height="520" fill="url(#bgGrad3)" rx="16" />

  <!-- Header -->
  <text x="480" y="38" font-family="system-ui, sans-serif" font-size="20" font-weight="800" fill="#F8FAFC" text-anchor="middle">TAX CLASSIFICATION: DIRECT VS. INDIRECT &amp; RATE STRUCTURES</text>
  <text x="480" y="60" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">Tax Incidence Dynamics, Shifting Mechanisms and Economic Impact on Household Budgets</text>

  <!-- Top Left: Direct Taxes -->
  <g transform="translate(35, 80)" filter="url(#shadow3)">
    <rect width="425" height="205" rx="10" fill="#1E293B" stroke="#3B82F6" stroke-width="1.5" />
    <rect x="0" y="0" width="425" height="34" rx="10" fill="#2563EB" />
    <text x="212" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">DIRECT TAXES (The Arrow: Burden Unshiftable)</text>
    
    <text x="15" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#93C5FD">Target: Personal Income, Business Profit &amp; Capital Assets</text>
    <text x="15" y="73" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Impact = Incidence: The legal entity assessed pays out-of-pocket.</text>
    
    <!-- Flow Mini Diagram -->
    <rect x="15" y="85" width="395" height="60" rx="6" fill="#0F172A" stroke="#334155" />
    <text x="60" y="112" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Taxpayer (Worker)</text>
    <text x="60" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Earns KES 100,000</text>
    
    <path d="M 120 115 L 280 115" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrow)" />
    <text x="200" y="107" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" fill="#38BDF8" text-anchor="middle">Direct Deduction (PAYE)</text>
    
    <text x="340" y="112" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399" text-anchor="middle">KRA Treasury</text>
    <text x="340" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#A7F3D0">Receives KES 25,000</text>

    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">• Examples: PAYE, Corporate Tax (30%), Withholding Tax (5-15%), CGT (15%)</text>
    <text x="15" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#6EE7B7">✓ Progressive by nature; acts as automatic economic stabilizer.</text>
  </g>

  <!-- Top Right: Indirect Taxes -->
  <g transform="translate(500, 80)" filter="url(#shadow3)">
    <rect width="425" height="205" rx="10" fill="#1E293B" stroke="#F97316" stroke-width="1.5" />
    <rect x="0" y="0" width="425" height="34" rx="10" fill="#EA580C" />
    <text x="212" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">INDIRECT TAXES (The Net: Burden Shiftable)</text>
    
    <text x="15" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FDBA74">Target: Goods, Services, Imports &amp; Commercial Spending</text>
    <text x="15" y="73" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Impact ≠ Incidence: Merchant collects tax; Consumer bears burden.</text>
    
    <!-- Flow Mini Diagram -->
    <rect x="15" y="85" width="395" height="60" rx="6" fill="#0F172A" stroke="#334155" />
    <text x="50" y="112" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#F8FAFC" text-anchor="middle">Consumer</text>
    <text x="50" y="128" font-family="system-ui, sans-serif" font-size="8.5" fill="#94A3B8">Pays KES 116</text>

    <path d="M 90 115 L 180 115" stroke="#FB923C" stroke-width="2" />
    <text x="135" y="107" font-family="system-ui, sans-serif" font-size="8.5" fill="#FB923C" text-anchor="middle">+16% VAT</text>

    <text x="225" y="112" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#FBBF24" text-anchor="middle">Supermarket</text>
    <text x="225" y="128" font-family="system-ui, sans-serif" font-size="8.5" fill="#94A3B8">Collects KES 16</text>

    <path d="M 270 115 L 340 115" stroke="#34D399" stroke-width="2" />
    <text x="305" y="107" font-family="system-ui, sans-serif" font-size="8.5" fill="#34D399" text-anchor="middle">Remits</text>

    <text x="375" y="112" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#34D399" text-anchor="middle">KRA</text>
    <text x="375" y="128" font-family="system-ui, sans-serif" font-size="8.5" fill="#A7F3D0">KES 16 Tax</text>

    <text x="15" y="165" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">• Examples: VAT (16%), Excise Duty (Airtime, Soda), Customs Tariffs</text>
    <text x="15" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#F87171">⚠ Regressive impact: Consumes a higher % of low-income household earnings.</text>
  </g>

  <!-- Bottom Panel: 3 Tax Rate Progression Models -->
  <g transform="translate(35, 305)" filter="url(#shadow3)">
    <rect width="890" height="195" rx="10" fill="#1E293B" stroke="#64748B" stroke-width="1.5" />
    <rect x="0" y="0" width="890" height="32" rx="10" fill="#334155" />
    <text x="445" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#F8FAFC" text-anchor="middle">TAX RATE DYNAMICS &amp; INCOME BURDEN SPECTRUM</text>

    <!-- Model 1: Progressive -->
    <rect x="15" y="45" width="275" height="135" rx="8" fill="#0F172A" stroke="#22C55E" stroke-width="1" />
    <text x="152" y="68" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#4ADE80" text-anchor="middle">Progressive Tax System</text>
    <text x="25" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Rate increases as Income rises.</text>
    <text x="25" y="108" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• High earners pay higher rate (%).</text>
    <text x="25" y="126" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">• Reduces national wealth inequality.</text>
    <text x="25" y="148" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#86EFAC">Example: Kenya PAYE (10% → 35%)</text>
    <path d="M 230 160 L 270 120" stroke="#4ADE80" stroke-width="3" />
    <polygon points="265,118 275,118 272,128" fill="#4ADE80" />

    <!-- Model 2: Proportional -->
    <rect x="307" y="45" width="275" height="135" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="1" />
    <text x="444" y="68" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8" text-anchor="middle">Proportional (Flat) Tax</text>
    <text x="317" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Constant flat % for all income levels.</text>
    <text x="317" y="108" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Everyone pays equal proportion.</text>
    <text x="317" y="126" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">• Simple to calculate and administer.</text>
    <text x="317" y="148" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#7DD3FC">Example: Flat 30% Corporate Profit Tax</text>
    <line x1="520" y1="140" x2="565" y2="140" stroke="#38BDF8" stroke-width="3" />

    <!-- Model 3: Regressive -->
    <rect x="600" y="45" width="275" height="135" rx="8" fill="#0F172A" stroke="#EF4444" stroke-width="1" />
    <text x="737" y="68" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F87171" text-anchor="middle">Regressive Tax System</text>
    <text x="610" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Effective tax % falls as income rises.</text>
    <text x="610" y="108" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Heavier relative burden on poor.</text>
    <text x="610" y="126" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">• Flat consumption levies create this.</text>
    <text x="610" y="148" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FCA5A5">Example: VAT on Sugar / Kerosene</text>
    <path d="M 820 120 L 860 160" stroke="#EF4444" stroke-width="3" />
    <polygon points="855,162 865,162 862,152" fill="#EF4444" />
  </g>
</svg>"""

# =============================================================================
# SVG 4: Customs Duty Tariff Barrier & Infant Industry Protection (Lesson 4)
# =============================================================================
SVG_CUSTOMS_DUTY_AND_PROTECTIONISM = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D1117" />
      <stop offset="100%" stop-color="#161B22" />
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <rect width="960" height="520" fill="url(#bgGrad4)" rx="16" />

  <!-- Header -->
  <text x="480" y="40" font-family="system-ui, sans-serif" font-size="21" font-weight="800" fill="#F8FAFC" text-anchor="middle">CUSTOMS DUTIES &amp; INFANT INDUSTRY PROTECTION MECHANISM</text>
  <text x="480" y="64" font-family="system-ui, sans-serif" font-size="12.5" fill="#94A3B8" text-anchor="middle">How Strategic Import Tariffs Equalize Playing Fields, Shield Domestic Jobs &amp; Raise Revenue</text>

  <!-- Left: Foreign Subsidized Exporter -->
  <g transform="translate(35, 95)" filter="url(#shadow4)">
    <rect width="260" height="380" rx="12" fill="#1E293B" stroke="#64748B" stroke-width="1.5" />
    <rect x="0" y="0" width="260" height="40" rx="12" fill="#334155" />
    <text x="130" y="25" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">FOREIGN PRODUCER</text>
    
    <circle cx="130" cy="85" r="30" fill="#0F172A" stroke="#38BDF8" stroke-width="2" />
    <text x="130" y="90" font-family="system-ui, sans-serif" font-size="20" text-anchor="middle">🚢</text>

    <text x="130" y="135" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8" text-anchor="middle">Mass Automation &amp; Scale</text>
    <text x="20" y="160" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• High subsidies in origin country</text>
    <text x="20" y="180" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Massive production volume</text>
    <text x="20" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Export price below local cost</text>
    <text x="20" y="220" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Risk: Market dumping in Kenya</text>

    <rect x="15" y="250" width="230" height="110" rx="8" fill="#0F172A" stroke="#475569" />
    <text x="130" y="275" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#F87171" text-anchor="middle">Port of Mombasa Arrival Price</text>
    <text x="130" y="305" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#EF4444" text-anchor="middle">KES 500 / Bag</text>
    <text x="130" y="335" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">Without tariff, crushes local mills!</text>
  </g>

  <!-- Center: The Tariff Barrier (Customs Border) -->
  <g transform="translate(320, 95)" filter="url(#shadow4)">
    <rect width="320" height="380" rx="12" fill="#1E293B" stroke="#F59E0B" stroke-width="2" />
    <rect x="0" y="0" width="320" height="40" rx="12" fill="#D97706" />
    <text x="160" y="25" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">KRA CUSTOMS TARIFF WALL</text>

    <!-- Tariff Calculation Box -->
    <rect x="15" y="55" width="290" height="130" rx="8" fill="#0F172A" stroke="#B45309" />
    <text x="160" y="78" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24" text-anchor="middle">Strategic Tariff Assessment</text>
    <text x="30" y="102" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">Import CIF Base: <tspan font-weight="bold" fill="#FFFFFF">KES 500</tspan></text>
    <text x="30" y="122" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">+ Customs Duty (60%): <tspan font-weight="bold" fill="#FBBF24">KES 300</tspan></text>
    <text x="30" y="142" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">+ Import Declaration Fee (IDF): <tspan font-weight="bold" fill="#93C5FD">KES 25</tspan></text>
    <line x1="30" y1="150" x2="290" y2="150" stroke="#475569" stroke-width="1" />
    <text x="160" y="172" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FDE68A" text-anchor="middle">New Clearance Price = KES 825</text>

    <!-- Strategic National Benefits -->
    <rect x="15" y="200" width="290" height="160" rx="8" fill="#0F172A" stroke="#334155" />
    <text x="160" y="222" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8" text-anchor="middle">4 Protectionist Objectives</text>
    <text x="25" y="245" font-family="system-ui, sans-serif" font-size="10" fill="#CBD5E1">1. Shields Infant Domestic Industries</text>
    <text x="25" y="265" font-family="system-ui, sans-serif" font-size="10" fill="#CBD5E1">2. Preserves Local Factory Employment</text>
    <text x="25" y="285" font-family="system-ui, sans-serif" font-size="10" fill="#CBD5E1">3. Mobilizes Billions in Treasury Revenue</text>
    <text x="25" y="305" font-family="system-ui, sans-serif" font-size="10" fill="#CBD5E1">4. Protects FX Reserves &amp; Curbs Dumping</text>
    <text x="160" y="335" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399" text-anchor="middle">Result: Fair Competition Achieved</text>
  </g>

  <!-- Right: Kenyan Infant Domestic Producer -->
  <g transform="translate(665, 95)" filter="url(#shadow4)">
    <rect width="260" height="380" rx="12" fill="#1E293B" stroke="#10B981" stroke-width="1.5" />
    <rect x="0" y="0" width="260" height="40" rx="12" fill="#059669" />
    <text x="130" y="25" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">LOCAL KENYAN FACTORY</text>

    <circle cx="130" cy="85" r="30" fill="#0F172A" stroke="#10B981" stroke-width="2" />
    <text x="130" y="90" font-family="system-ui, sans-serif" font-size="20" text-anchor="middle">🏭</text>

    <text x="130" y="135" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#6EE7B7" text-anchor="middle">Athi River Cement Mill</text>
    <text x="20" y="160" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Employs 2,500 Kenyan workers</text>
    <text x="20" y="180" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• High local power &amp; freight costs</text>
    <text x="20" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Developing scale &amp; technology</text>
    <text x="20" y="220" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Pays PAYE &amp; Local County Rates</text>

    <rect x="15" y="250" width="230" height="110" rx="8" fill="#0F172A" stroke="#047857" />
    <text x="130" y="275" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399" text-anchor="middle">Local Retail Price in Kenya</text>
    <text x="130" y="305" font-family="system-ui, sans-serif" font-size="18" font-weight="800" fill="#10B981" text-anchor="middle">KES 750 / Bag</text>
    <text x="130" y="335" font-family="system-ui, sans-serif" font-size="10" fill="#A7F3D0" text-anchor="middle">Competitive vs. KES 825 Import!</text>
  </g>
</svg>"""

# =============================================================================
# SVG 5: Tax Compliance vs. Tax Evasion & The Leaky Bucket of Public Ethics (Lesson 5)
# =============================================================================
SVG_TAX_ETHICS_AND_ACCOUNTABILITY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#1E1B4B" />
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.3" />
    </filter>
  </defs>

  <rect width="960" height="520" fill="url(#bgGrad5)" rx="16" />

  <!-- Header -->
  <text x="480" y="38" font-family="system-ui, sans-serif" font-size="20" font-weight="800" fill="#F8FAFC" text-anchor="middle">TAX ETHICS, COMPLIANCE &amp; PUBLIC ACCOUNTABILITY CONTRACT</text>
  <text x="480" y="60" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">The Reciprocal Social Contract: Civic Duty of Taxpayers vs. Government Stewardship of Public Funds</text>

  <!-- Left: Citizen Legal & Ethical Spectrum -->
  <g transform="translate(40, 80)" filter="url(#shadow5)">
    <rect width="420" height="400" rx="12" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5" />
    <rect x="0" y="0" width="420" height="36" rx="12" fill="#0284C7" />
    <text x="210" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">TAXPAYER BEHAVIOR SPECTRUM</text>

    <!-- Zone 1: Compliance -->
    <rect x="15" y="50" width="390" height="98" rx="8" fill="#0F172A" stroke="#10B981" stroke-width="1.5" />
    <text x="30" y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34D399">1. Tax Compliance (Lawful &amp; Ethical)</text>
    <text x="30" y="90" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Timely registration with KRA PIN.</text>
    <text x="30" y="108" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Accurate annual return declarations via iTax by June 30th.</text>
    <text x="30" y="126" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#6EE7B7">Outcome: Fuels national development &amp; public welfare.</text>

    <!-- Zone 2: Avoidance -->
    <rect x="15" y="160" width="390" height="98" rx="8" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5" />
    <text x="30" y="182" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FBBF24">2. Tax Avoidance (Lawful Tax Minimization)</text>
    <text x="30" y="200" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Utilizing statutory reliefs, allowances &amp; capital deductions.</text>
    <text x="30" y="218" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Investing in tax-free infrastructure bonds or mortgage relief.</text>
    <text x="30" y="236" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FDE68A">Outcome: Legal financial optimization within the letter of the law.</text>

    <!-- Zone 3: Evasion -->
    <rect x="15" y="270" width="390" height="115" rx="8" fill="#0F172A" stroke="#EF4444" stroke-width="1.5" />
    <text x="30" y="292" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#F87171">3. Tax Evasion (Illegal &amp; Criminal Offense)</text>
    <text x="30" y="310" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Deliberately concealing cash income, falsifying expense books.</text>
    <text x="30" y="328" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Smuggling contraband goods to bypass customs duties.</text>
    <text x="30" y="348" font-family="system-ui, sans-serif" font-size="10" fill="#FCA5A5">Penalties: Heavy fines (up to 200%), asset freezing &amp; jail terms.</text>
    <text x="30" y="366" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#EF4444">Outcome: Starves public schools, clinics &amp; roads of funds.</text>
  </g>

  <!-- Right: Government Public Stewardship & Accountability -->
  <g transform="translate(500, 80)" filter="url(#shadow5)">
    <rect width="420" height="400" rx="12" fill="#1E293B" stroke="#8B5CF6" stroke-width="1.5" />
    <rect x="0" y="0" width="420" height="36" rx="12" fill="#6D28D9" />
    <text x="210" y="24" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">GOVERNMENT ETHICAL STEWARDSHIP</text>

    <rect x="15" y="50" width="390" height="155" rx="8" fill="#0F172A" stroke="#A78BFA" stroke-width="1" />
    <text x="30" y="74" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#C4B5FD">Pillars of Public Financial Accountability</text>
    <text x="30" y="96" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• <tspan font-weight="bold" fill="#FFFFFF">Office of the Auditor-General (OAG):</tspan> Independent annual scrutiny</text>
    <text x="30" y="114" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• <tspan font-weight="bold" fill="#FFFFFF">Controller of Budget (OCOB):</tspan> Authorizes withdrawals from funds</text>
    <text x="30" y="132" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• <tspan font-weight="bold" fill="#FFFFFF">Public Procurement &amp; Asset Disposal Act:</tspan> Transparent bidding</text>
    <text x="30" y="150" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• <tspan font-weight="bold" fill="#FFFFFF">Equalization Fund:</tspan> Affirmative action for marginalized areas</text>
    <text x="30" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399">Goal: Zero corruption, 100% value for every tax shilling.</text>

    <!-- The Social Contract Equilibrium -->
    <rect x="15" y="220" width="390" height="165" rx="8" fill="#0F172A" stroke="#6366F1" stroke-width="1" />
    <text x="210" y="245" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#818CF8" text-anchor="middle">THE SOCIAL CONTRACT EQUILIBRIUM</text>
    
    <rect x="30" y="260" width="165" height="50" rx="6" fill="#1E293B" stroke="#38BDF8" />
    <text x="112" y="280" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="middle">Citizen Action</text>
    <text x="112" y="296" font-family="system-ui, sans-serif" font-size="9" fill="#CBD5E1" text-anchor="middle">Faithful Tax Payment</text>

    <text x="210" y="290" font-family="system-ui, sans-serif" font-size="16" fill="#FBBF24" text-anchor="middle">⇄</text>

    <rect x="225" y="260" width="165" height="50" rx="6" fill="#1E293B" stroke="#34D399" />
    <text x="307" y="280" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399" text-anchor="middle">State Delivery</text>
    <text x="307" y="296" font-family="system-ui, sans-serif" font-size="9" fill="#CBD5E1" text-anchor="middle">Roads, Security, Health</text>

    <text x="210" y="340" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">When both sides fulfill their duties, national prosperity is sustained.</text>
    <text x="210" y="360" font-family="system-ui, sans-serif" font-size="9.5" fill="#94A3B8" text-anchor="middle">Mismanagement breeds tax resistance; compliance enables infrastructure.</text>
  </g>
</svg>"""

# =============================================================================
# SVG 6: Government Budget Balancing & Deficit Financing Anatomy (Lesson 6)
# =============================================================================
SVG_BUDGET_BALANCE_AND_DEFICIT_FINANCING = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D16" />
      <stop offset="100%" stop-color="#172033" />
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.35" />
    </filter>
  </defs>

  <rect width="960" height="520" fill="url(#bgGrad6)" rx="16" />

  <!-- Header -->
  <text x="480" y="38" font-family="system-ui, sans-serif" font-size="20" font-weight="800" fill="#F8FAFC" text-anchor="middle">NATIONAL BUDGET BALANCE &amp; DEFICIT FINANCING ANATOMY</text>
  <text x="480" y="60" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">Mathematical Mechanics of Budget Surpluses, Deficits and Fiscal Debt Sustainability</text>

  <!-- 3 Budget States Comparison (Top Row) -->
  <g transform="translate(35, 80)" filter="url(#shadow6)">
    <!-- 1. Surplus -->
    <rect x="0" y="0" width="280" height="150" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5" />
    <rect x="0" y="0" width="280" height="28" rx="10" fill="#059669" />
    <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. BUDGET SURPLUS (R &gt; G)</text>
    <text x="140" y="55" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#34D399" text-anchor="middle">Total Revenue &gt; Total Spending</text>
    <text x="20" y="80" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Excess funds generated</text>
    <text x="20" y="98" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Used to retire public debt or save</text>
    <text x="20" y="116" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Creates sovereign wealth reserves</text>
    <text x="20" y="136" font-family="system-ui, sans-serif" font-size="9.5" fill="#6EE7B7">Rare in growing developing nations.</text>

    <!-- 2. Balanced -->
    <rect x="305" y="0" width="280" height="150" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5" />
    <rect x="0" y="0" width="280" height="28" rx="10" fill="#0284C7" transform="translate(305, 0)" />
    <text x="445" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. BALANCED BUDGET (R = G)</text>
    <text x="445" y="55" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#38BDF8" text-anchor="middle">Total Revenue == Total Spending</text>
    <text x="325" y="80" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Expenditure fully covered by taxes</text>
    <text x="325" y="98" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Zero new debt accumulation</text>
    <text x="325" y="116" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Fiscal stability is preserved</text>
    <text x="325" y="136" font-family="system-ui, sans-serif" font-size="9.5" fill="#7DD3FC">Ideal benchmark for fiscal prudence.</text>

    <!-- 3. Deficit -->
    <rect x="610" y="0" width="280" height="150" rx="10" fill="#1E293B" stroke="#EF4444" stroke-width="1.5" />
    <rect x="0" y="0" width="280" height="28" rx="10" fill="#DC2626" transform="translate(610, 0)" />
    <text x="750" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. BUDGET DEFICIT (R &lt; G)</text>
    <text x="750" y="55" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" fill="#F87171" text-anchor="middle">Total Revenue &lt; Total Spending</text>
    <text x="630" y="80" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Expenditure exceeds tax revenues</text>
    <text x="630" y="98" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Common when building mega infrastructure</text>
    <text x="630" y="116" font-family="system-ui, sans-serif" font-size="10.5" fill="#CBD5E1">• Financing Gap must be bridged!</text>
    <text x="630" y="136" font-family="system-ui, sans-serif" font-size="9.5" fill="#FCA5A5">Requires borrowing or asset sales.</text>
  </g>

  <!-- Bottom Panel: Bridging the Deficit & Debt Channels -->
  <g transform="translate(35, 255)" filter="url(#shadow6)">
    <rect width="890" height="235" rx="12" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5" />
    <rect x="0" y="0" width="890" height="34" rx="12" fill="#D97706" />
    <text x="445" y="23" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">HOW GOVERNMENTS BRIDGE FISCAL DEFICITS (DEFICIT FINANCING CHANNELS)</text>

    <!-- Channel 1: Domestic Debt -->
    <rect x="20" y="50" width="270" height="165" rx="8" fill="#0F172A" stroke="#334155" />
    <circle cx="45" cy="75" r="14" fill="#0284C7" />
    <text x="45" y="80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">A</text>
    <text x="70" y="75" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#38BDF8">Domestic Borrowing</text>
    <text x="70" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Treasury Bills &amp; Bonds</text>
    <text x="25" y="115" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Borrowing from local banks, SACCOs, pension funds, and citizens.</text>
    <text x="25" y="145" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Advantage: Paid back in KES; no direct foreign exchange currency risk.</text>
    <text x="25" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#F87171">⚠ Risk: May crowd out private credit.</text>

    <!-- Channel 2: External Sovereign Debt -->
    <rect x="310" y="50" width="270" height="165" rx="8" fill="#0F172A" stroke="#334155" />
    <circle cx="335" cy="75" r="14" fill="#F59E0B" />
    <text x="335" y="80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">B</text>
    <text x="360" y="75" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FBBF24">External Borrowing</text>
    <text x="360" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Concessional &amp; Commercial</text>
    <text x="315" y="115" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Multilateral: World Bank, IMF, AfDB (Low interest rates, long grace period).</text>
    <text x="315" y="145" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Bilateral/Eurobonds: Commercial international bond investors.</text>
    <text x="315" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#F87171">⚠ Risk: Currency depreciation hikes debt.</text>

    <!-- Channel 3: Fiscal Reform & Discipline -->
    <rect x="600" y="50" width="270" height="165" rx="8" fill="#0F172A" stroke="#334155" />
    <circle cx="625" cy="75" r="14" fill="#10B981" />
    <text x="625" y="80" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">C</text>
    <text x="650" y="75" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#34D399">Fiscal Adjustments</text>
    <text x="650" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8">Revenue &amp; Spending Reforms</text>
    <text x="605" y="115" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Expanding tax base via eTIMS &amp; curbing tax avoidance/evasion.</text>
    <text x="605" y="145" font-family="system-ui, sans-serif" font-size="10.5" fill="#E2E8F0">• Austerity cuts to non-essential recurrent spending (per diems, foreign trips).</text>
    <text x="605" y="180" font-family="system-ui, sans-serif" font-size="10" fill="#6EE7B7">✓ Most sustainable long-term solution.</text>
  </g>
</svg>"""
