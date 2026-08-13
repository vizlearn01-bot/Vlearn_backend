"""
VLearn Form 4 Business Studies — Topic 1 SVG Vector Graphics
Authoritative dark-mode high-contrast educational diagrams.
"""

SVG_NATIONAL_INCOME_HIERARCHY = """<svg viewBox="0 0 800 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="gdpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="gnpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="netGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="nnpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#6d28d9" />
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
    <marker id="arrowEmerald" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="400" y="40" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">National Income Aggregates &amp; Formula Transitions</text>
  <text x="400" y="65" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Interrelationships between Domestic, National, Gross, and Net Aggregates</text>

  <!-- GDP Block -->
  <rect x="80" y="100" width="260" height="90" rx="14" fill="url(#gdpGrad)" stroke="#38bdf8" stroke-width="2" />
  <text x="210" y="130" fill="#ffffff" font-size="16" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Gross Domestic Product (GDP)</text>
  <text x="210" y="152" fill="#e0f2fe" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Output produced geographically inside Kenya</text>
  <text x="210" y="172" fill="#bae6fd" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">(Includes Depreciation | Domestic Border)</text>

  <!-- Horizontal Transition: GDP -> GNP -->
  <path d="M 340 145 L 450 145" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrow)" />
  <rect x="355" y="115" width="80" height="26" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
  <text x="395" y="132" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle" font-family="monospace">+ (X - M)</text>
  <text x="395" y="160" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">+ Net Factor Income</text>

  <!-- GNP Block -->
  <rect x="460" y="100" width="260" height="90" rx="14" fill="url(#gnpGrad)" stroke="#34d399" stroke-width="2" />
  <text x="590" y="130" fill="#ffffff" font-size="16" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Gross National Product (GNP)</text>
  <text x="590" y="152" fill="#d1fae5" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Output produced by Kenyan citizens anywhere</text>
  <text x="590" y="172" fill="#a7f3d0" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">GNP = GDP + Net Factor Income</text>

  <!-- Vertical Transition: GDP -> NDP -->
  <path d="M 210 190 L 210 270" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowAmber)" />
  <rect x="155" y="215" width="110" height="26" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1" />
  <text x="210" y="232" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle" font-family="monospace">- Depreciation</text>

  <!-- NDP Block -->
  <rect x="80" y="275" width="260" height="90" rx="14" fill="url(#netGrad)" stroke="#fbbf24" stroke-width="2" />
  <text x="210" y="305" fill="#ffffff" font-size="16" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Net Domestic Product (NDP)</text>
  <text x="210" y="327" fill="#fef3c7" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Domestic output less capital wear and tear</text>
  <text x="210" y="347" fill="#fde68a" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">NDP = GDP - Depreciation</text>

  <!-- Vertical Transition: GNP -> NNP -->
  <path d="M 590 190 L 590 270" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowAmber)" />
  <rect x="535" y="215" width="110" height="26" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1" />
  <text x="590" y="232" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle" font-family="monospace">- Depreciation</text>

  <!-- NNP Block -->
  <rect x="460" y="275" width="260" height="90" rx="14" fill="url(#nnpGrad)" stroke="#c084fc" stroke-width="2" />
  <text x="590" y="305" fill="#ffffff" font-size="16" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Net National Product (NNP)</text>
  <text x="590" y="327" fill="#f3e8ff" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">True National Income of the Country</text>
  <text x="590" y="347" fill="#e9d5ff" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">NNP = GNP - Depreciation</text>

  <!-- Horizontal Transition: NDP -> NNP -->
  <path d="M 340 320 L 450 320" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrowEmerald)" />
  <text x="395" y="312" fill="#34d399" font-size="10" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">+ Net Factor Income</text>

  <!-- Per Capita Callout -->
  <rect x="230" y="380" width="340" height="30" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1" />
  <text x="400" y="400" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Per Capita Income = National Income (NNP) ÷ Total Population</text>
</svg>"""

SVG_CIRCULAR_FLOW_MODEL = """<svg viewBox="0 0 840 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="houseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="firmGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <marker id="cArrowBlue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#60a5fa" />
    </marker>
    <marker id="cArrowEmerald" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
    </marker>
    <marker id="cArrowRose" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
    </marker>
    <marker id="cArrowAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">The Circular Flow of Income (Open Economy)</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Real Flow vs Money Flow with Injections &amp; Leakages</text>

  <!-- Households Node -->
  <rect x="50" y="160" width="180" height="150" rx="16" fill="url(#houseGrad)" stroke="#60a5fa" stroke-width="2" />
  <text x="140" y="195" fill="#ffffff" font-size="18" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">HOUSEHOLDS</text>
  <text x="140" y="220" fill="#bfdbfe" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Own Factors of Prod.</text>
  <text x="140" y="238" fill="#bfdbfe" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Earn Factor Incomes</text>
  <text x="140" y="256" fill="#bfdbfe" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Buy Consumer Goods</text>
  <text x="140" y="280" fill="#93c5fd" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">(Land, Labour, Capital)</text>

  <!-- Firms Node -->
  <rect x="610" y="160" width="180" height="150" rx="16" fill="url(#firmGrad)" stroke="#34d399" stroke-width="2" />
  <text x="700" y="195" fill="#ffffff" font-size="18" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">BUSINESS FIRMS</text>
  <text x="700" y="220" fill="#a7f3d0" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Produce Final Goods</text>
  <text x="700" y="238" fill="#a7f3d0" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Hire Factor Services</text>
  <text x="700" y="256" fill="#a7f3d0" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Pay Factor Rewards</text>
  <text x="700" y="280" fill="#6ee7b7" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">(Rent, Wages, Profits)</text>

  <!-- Top Curve: Money Flow (Consumption Spending from Households to Firms) -->
  <path d="M 230 180 Q 420 100 610 180" fill="none" stroke="#60a5fa" stroke-width="3" marker-end="url(#cArrowBlue)" />
  <rect x="310" y="90" width="220" height="28" rx="8" fill="#0f172a" stroke="#60a5fa" stroke-width="1" />
  <text x="420" y="108" fill="#60a5fa" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Consumption Spending (C) →</text>

  <!-- Top Inner Curve: Real Flow (Goods & Services from Firms to Households) -->
  <path d="M 610 210 Q 420 150 230 210" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#cArrowBlue)" />
  <text x="420" y="165" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">← Flow of Final Goods &amp; Services (Real Flow)</text>

  <!-- Bottom Curve: Money Flow (Factor Incomes from Firms to Households) -->
  <path d="M 610 290 Q 420 370 230 290" fill="none" stroke="#34d399" stroke-width="3" marker-end="url(#cArrowEmerald)" />
  <rect x="300" y="340" width="240" height="28" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1" />
  <text x="420" y="358" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">← Factor Incomes (Wages, Rent, Profit)</text>

  <!-- Bottom Inner Curve: Real Flow (Factor Services from Households to Firms) -->
  <path d="M 230 260 Q 420 320 610 260" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#cArrowEmerald)" />
  <text x="420" y="305" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">Flow of Factor Services (Labour, Land, Capital) →</text>

  <!-- Leakages (Withdrawals) Box -->
  <rect x="50" y="390" width="240" height="75" rx="12" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="170" y="412" fill="#f43f5e" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">LEAKAGES / WITHDRAWALS (W)</text>
  <text x="170" y="432" fill="#fecdd3" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Savings (S) in financial banks</text>
  <text x="170" y="448" fill="#fecdd3" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Taxation (T) &amp; Imports (M)</text>
  <path d="M 140 310 L 140 390" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#cArrowRose)" />

  <!-- Injections Box -->
  <rect x="550" y="390" width="240" height="75" rx="12" fill="#064e3b" stroke="#fbbf24" stroke-width="1.5" />
  <text x="670" y="412" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">INJECTIONS (J)</text>
  <text x="670" y="432" fill="#fef3c7" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Investment (I) by business firms</text>
  <text x="670" y="448" fill="#fef3c7" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">• Government Spending (G) &amp; Exports (X)</text>
  <path d="M 670 390 L 670 310" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#cArrowAmber)" />
</svg>"""

SVG_EQUILIBRIUM_SCALE = """<svg viewBox="0 0 800 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="leakPan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#be123c" />
      <stop offset="100%" stop-color="#881337" />
    </linearGradient>
    <linearGradient id="injPan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#047857" />
      <stop offset="100%" stop-color="#064e3b" />
    </linearGradient>
  </defs>

  <!-- Title -->
  <text x="400" y="40" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Macroeconomic Equilibrium: The Balance Condition</text>
  <text x="400" y="65" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Withdrawals (Leakages) Must Exactly Equal Injections</text>

  <!-- Center Fulcrum & Beam -->
  <polygon points="400,120 375,320 425,320" fill="#334155" stroke="#64748b" stroke-width="2" />
  <circle cx="400" cy="120" r="14" fill="#38bdf8" stroke="#0284c7" stroke-width="3" />
  <line x1="160" y1="120" x2="640" y2="120" stroke="#94a3b8" stroke-width="8" stroke-linecap="round" />

  <!-- Left Scale Pan: Leakages -->
  <line x1="160" y1="120" x2="100" y2="200" stroke="#64748b" stroke-width="2" />
  <line x1="160" y1="120" x2="220" y2="200" stroke="#64748b" stroke-width="2" />
  <ellipse cx="160" cy="205" rx="70" ry="16" fill="url(#leakPan)" stroke="#f43f5e" stroke-width="2" />
  <rect x="90" y="215" width="140" height="90" rx="10" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="160" y="240" fill="#f43f5e" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">LEAKAGES (W)</text>
  <text x="160" y="262" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">S + T + M</text>
  <text x="160" y="282" fill="#fecdd3" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">Savings + Taxes + Imports</text>

  <!-- Right Scale Pan: Injections -->
  <line x1="640" y1="120" x2="580" y2="200" stroke="#64748b" stroke-width="2" />
  <line x1="640" y1="120" x2="700" y2="200" stroke="#64748b" stroke-width="2" />
  <ellipse cx="640" cy="205" rx="70" ry="16" fill="url(#injPan)" stroke="#34d399" stroke-width="2" />
  <rect x="570" y="215" width="140" height="90" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="640" y="240" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">INJECTIONS (J)</text>
  <text x="640" y="262" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">I + G + X</text>
  <text x="640" y="282" fill="#a7f3d0" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">Invest + Govt + Exports</text>

  <!-- Bottom Equilibrium States -->
  <rect x="180" y="340" width="440" height="42" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
  <text x="400" y="366" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="monospace">Equilibrium Condition: S + T + M = I + G + X</text>
</svg>"""

SVG_VALUE_ADDED_CHAIN = """<svg viewBox="0 0 860 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="vStage1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#15803d" />
      <stop offset="100%" stop-color="#166534" />
    </linearGradient>
    <linearGradient id="vStage2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="vStage3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="vStage4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#6d28d9" />
    </linearGradient>
    <marker id="vArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="430" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Value-Added Production Chain: Avoiding Double Counting</text>
  <text x="430" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Example: Multi-Stage Bread Production (Wheat → Flour → Bakery → Consumer)</text>

  <!-- Stage 1: Wheat Farmer -->
  <rect x="30" y="90" width="170" height="150" rx="14" fill="url(#vStage1)" stroke="#4ade80" stroke-width="2" />
  <text x="115" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">STAGE 1: FARMER</text>
  <text x="115" y="145" fill="#dcfce7" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Grows raw wheat</text>
  <text x="115" y="170" fill="#ffffff" font-size="12" text-anchor="middle" font-family="monospace">Input Cost = Sh. 0</text>
  <text x="115" y="190" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle" font-family="monospace">Sale Price = Sh. 10</text>
  <rect x="45" y="205" width="140" height="24" rx="6" fill="#0f172a" />
  <text x="115" y="222" fill="#4ade80" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Value Added: +Sh. 10</text>

  <!-- Arrow 1 -> 2 -->
  <line x1="200" y1="165" x2="235" y2="165" stroke="#38bdf8" stroke-width="3" marker-end="url(#vArrow)" />

  <!-- Stage 2: Flour Miller -->
  <rect x="240" y="90" width="170" height="150" rx="14" fill="url(#vStage2)" stroke="#38bdf8" stroke-width="2" />
  <text x="325" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">STAGE 2: MILLER</text>
  <text x="325" y="145" fill="#e0f2fe" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Grinds wheat to flour</text>
  <text x="325" y="170" fill="#ffffff" font-size="12" text-anchor="middle" font-family="monospace">Input Cost = Sh. 10</text>
  <text x="325" y="190" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle" font-family="monospace">Sale Price = Sh. 18</text>
  <rect x="255" y="205" width="140" height="24" rx="6" fill="#0f172a" />
  <text x="325" y="222" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Value Added: +Sh. 8</text>

  <!-- Arrow 2 -> 3 -->
  <line x1="410" y1="165" x2="445" y2="165" stroke="#38bdf8" stroke-width="3" marker-end="url(#vArrow)" />

  <!-- Stage 3: Baker -->
  <rect x="450" y="90" width="170" height="150" rx="14" fill="url(#vStage3)" stroke="#fbbf24" stroke-width="2" />
  <text x="535" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">STAGE 3: BAKER</text>
  <text x="535" y="145" fill="#fef3c7" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Bakes flour into bread</text>
  <text x="535" y="170" fill="#ffffff" font-size="12" text-anchor="middle" font-family="monospace">Input Cost = Sh. 18</text>
  <text x="535" y="190" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle" font-family="monospace">Sale Price = Sh. 25</text>
  <rect x="465" y="205" width="140" height="24" rx="6" fill="#0f172a" />
  <text x="535" y="222" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Value Added: +Sh. 7</text>

  <!-- Arrow 3 -> 4 -->
  <line x1="620" y1="165" x2="655" y2="165" stroke="#38bdf8" stroke-width="3" marker-end="url(#vArrow)" />

  <!-- Stage 4: Retailer -->
  <rect x="660" y="90" width="170" height="150" rx="14" fill="url(#vStage4)" stroke="#c084fc" stroke-width="2" />
  <text x="745" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">STAGE 4: RETAILER</text>
  <text x="745" y="145" fill="#f3e8ff" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Sells loaf to consumer</text>
  <text x="745" y="170" fill="#ffffff" font-size="12" text-anchor="middle" font-family="monospace">Input Cost = Sh. 25</text>
  <text x="745" y="190" fill="#ffffff" font-size="12" font-weight="600" text-anchor="middle" font-family="monospace">Sale Price = Sh. 30</text>
  <rect x="675" y="205" width="140" height="24" rx="6" fill="#0f172a" />
  <text x="745" y="222" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Value Added: +Sh. 5</text>

  <!-- Summary Box at Bottom -->
  <rect x="60" y="270" width="740" height="85" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
  <text x="430" y="298" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Sum of Value Added = Sh. 10 + Sh. 8 + Sh. 7 + Sh. 5 = Sh. 30</text>
  <text x="430" y="322" fill="#ffffff" font-size="13" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">Final Consumer Selling Price = Sh. 30 (Gross output double counting: 10 + 18 + 25 + 30 = Sh. 83)</text>
  <text x="430" y="342" fill="#94a3b8" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Counting only Value Added (Sh. 30) prevents artificial economic inflation of Sh. 53!</text>
</svg>"""

SVG_FACTORS_INFLUENCING_NI = """<svg viewBox="0 0 800 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <marker id="fArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="400" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Determinants of National Income Level</text>
  <text x="400" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">How Resource Endowments, Technology &amp; Institutions Drive National Output</text>

  <!-- Center Target: LEVEL OF NATIONAL INCOME -->
  <circle cx="400" cy="250" r="85" fill="url(#centerGrad)" stroke="#38bdf8" stroke-width="3" />
  <text x="400" y="235" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">LEVEL OF</text>
  <text x="400" y="255" fill="#38bdf8" font-size="16" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">NATIONAL</text>
  <text x="400" y="275" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">INCOME</text>

  <!-- 1. Labour Supply & Skills (Top Left) -->
  <rect x="60" y="90" width="180" height="60" rx="10" fill="#1e293b" stroke="#60a5fa" stroke-width="1.5" />
  <text x="150" y="115" fill="#60a5fa" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">1. Labour Supply &amp; Skills</text>
  <text x="150" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Education, health &amp; workforce</text>
  <line x1="240" y1="135" x2="330" y2="205" stroke="#60a5fa" stroke-width="2" marker-end="url(#fArrow)" />

  <!-- 2. Capital & Technology (Top Center) -->
  <rect x="310" y="80" width="180" height="60" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
  <text x="400" y="105" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">2. Capital &amp; Equipment</text>
  <text x="400" y="125" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Machinery, tools &amp; factories</text>
  <line x1="400" y1="140" x2="400" y2="165" stroke="#34d399" stroke-width="2" marker-end="url(#fArrow)" />

  <!-- 3. Entrepreneurship (Top Right) -->
  <rect x="560" y="90" width="180" height="60" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
  <text x="650" y="115" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">3. Entrepreneurship</text>
  <text x="650" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Organization &amp; risk-taking</text>
  <line x1="560" y1="135" x2="470" y2="205" stroke="#fbbf24" stroke-width="2" marker-end="url(#fArrow)" />

  <!-- 4. Natural Resources (Mid Left) -->
  <rect x="30" y="220" width="170" height="60" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5" />
  <text x="115" y="245" fill="#a78bfa" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">4. Natural Resources</text>
  <text x="115" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Arable land, water &amp; minerals</text>
  <line x1="200" y1="250" x2="310" y2="250" stroke="#a78bfa" stroke-width="2" marker-end="url(#fArrow)" />

  <!-- 5. Technology Level (Mid Right) -->
  <rect x="600" y="220" width="170" height="60" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="685" y="245" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">5. Level of Technology</text>
  <text x="685" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Modern production methods</text>
  <line x1="600" y1="250" x2="490" y2="250" stroke="#f43f5e" stroke-width="2" marker-end="url(#fArrow)" />

  <!-- 6. Political Stability (Bottom Left) -->
  <rect x="90" y="360" width="190" height="60" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
  <text x="185" y="385" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">6. Political Stability</text>
  <text x="185" y="405" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Peace, rule of law &amp; security</text>
  <line x1="250" y1="360" x2="335" y2="300" stroke="#38bdf8" stroke-width="2" marker-end="url(#fArrow)" />

  <!-- 7. Attitude to Work (Bottom Right) -->
  <rect x="520" y="360" width="190" height="60" rx="10" fill="#1e293b" stroke="#2dd4bf" stroke-width="1.5" />
  <text x="615" y="385" fill="#2dd4bf" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">7. Attitude to Work</text>
  <text x="615" y="405" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Discipline, diligence &amp; integrity</text>
  <line x1="550" y1="360" x2="465" y2="300" stroke="#2dd4bf" stroke-width="2" marker-end="url(#fArrow)" />
</svg>"""
