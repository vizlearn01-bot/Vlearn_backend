"""
VLearn Form 4 Business Studies — Topic 2 SVG Vector Graphics
Authoritative dark-mode high-contrast educational diagrams for Population and Employment.
"""

SVG_DEMOGRAPHIC_BALANCE_FLOW = """<svg viewBox="0 0 840 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="popCenter" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <marker id="dGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
    </marker>
    <marker id="dRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">The Demographic Balance Equation</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">How Inflows (Births + Immigration) and Outflows (Deaths + Emigration) Drive Population Size</text>

  <!-- Center Hub: TOTAL POPULATION SIZE -->
  <circle cx="420" cy="220" r="85" fill="url(#popCenter)" stroke="#38bdf8" stroke-width="3" />
  <text x="420" y="205" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle">TOTAL</text>
  <text x="420" y="225" fill="#38bdf8" font-size="16" font-weight="800" text-anchor="middle">POPULATION</text>
  <text x="420" y="245" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle">SIZE</text>

  <!-- Inflow 1: Births (+) -->
  <rect x="40" y="110" width="200" height="65" rx="12" fill="#064e3b" stroke="#34d399" stroke-width="2" />
  <text x="140" y="135" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">BIRTHS (+)</text>
  <text x="140" y="155" fill="#d1fae5" font-size="11" text-anchor="middle">Live births per 1,000 (CBR)</text>
  <path d="M 240 145 L 335 190" fill="none" stroke="#34d399" stroke-width="3" marker-end="url(#dGreen)" />

  <!-- Inflow 2: Immigration (+) -->
  <rect x="40" y="265" width="200" height="65" rx="12" fill="#064e3b" stroke="#34d399" stroke-width="2" />
  <text x="140" y="290" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">IMMIGRATION (+)</text>
  <text x="140" y="310" fill="#d1fae5" font-size="11" text-anchor="middle">Incoming settlers entering</text>
  <path d="M 240 295 L 335 250" fill="none" stroke="#34d399" stroke-width="3" marker-end="url(#dGreen)" />

  <!-- Outflow 1: Deaths (-) -->
  <rect x="600" y="110" width="200" height="65" rx="12" fill="#1e1b4b" stroke="#f43f5e" stroke-width="2" />
  <text x="700" y="135" fill="#f43f5e" font-size="14" font-weight="700" text-anchor="middle">DEATHS (-)</text>
  <text x="700" y="155" fill="#fecdd3" font-size="11" text-anchor="middle">Mortality rate per 1,000 (CDR)</text>
  <path d="M 505 190 L 600 145" fill="none" stroke="#f43f5e" stroke-width="3" marker-end="url(#dRed)" />

  <!-- Outflow 2: Emigration (-) -->
  <rect x="600" y="265" width="200" height="65" rx="12" fill="#1e1b4b" stroke="#f43f5e" stroke-width="2" />
  <text x="700" y="290" fill="#f43f5e" font-size="14" font-weight="700" text-anchor="middle">EMIGRATION (-)</text>
  <text x="700" y="310" fill="#fecdd3" font-size="11" text-anchor="middle">Departing citizens exiting</text>
  <path d="M 505 250 L 600 295" fill="none" stroke="#f43f5e" stroke-width="3" marker-end="url(#dRed)" />

  <!-- Formula Banner -->
  <rect x="100" y="360" width="640" height="42" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
  <text x="420" y="386" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="monospace">Population Change = (Births - Deaths) + (Immigration - Emigration)</text>
</svg>"""

SVG_OPTIMUM_POPULATION_CURVE = """<svg viewBox="0 0 840 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="optGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#34d399" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">The Optimum Population Curve</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Relationship Between Population Size and Output per Capita (Standard of Living)</text>

  <!-- Coordinate Axes -->
  <line x1="100" y1="360" x2="760" y2="360" stroke="#64748b" stroke-width="2.5" />
  <line x1="100" y1="360" x2="100" y2="80" stroke="#64748b" stroke-width="2.5" />

  <!-- Axis Labels -->
  <text x="430" y="395" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">Population Size (Millions) →</text>
  <text x="40" y="210" fill="#cbd5e1" font-size="13" font-weight="600" transform="rotate(-90 40 210)" text-anchor="middle">Standard of Living (Income Per Capita) →</text>

  <!-- Inverted U Curve -->
  <path d="M 120 340 Q 420 80 720 340" fill="none" stroke="url(#optGrad)" stroke-width="4.5" />

  <!-- Optimum Peak Marker -->
  <circle cx="420" cy="145" r="8" fill="#34d399" stroke="#ffffff" stroke-width="2.5" />
  <line x1="420" y1="145" x2="420" y2="360" stroke="#34d399" stroke-width="2" stroke-dasharray="5 3" />
  <rect x="340" y="90" width="160" height="34" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="420" y="112" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">OPTIMUM (Peak Output)</text>
  <text x="420" y="378" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Optimum Size (Po)</text>

  <!-- Under-population Zone (Left) -->
  <rect x="130" y="200" width="180" height="85" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
  <text x="220" y="225" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">UNDER-POPULATION</text>
  <text x="220" y="245" fill="#94a3b8" font-size="11" text-anchor="middle">• Resources underutilized</text>
  <text x="220" y="262" fill="#94a3b8" font-size="11" text-anchor="middle">• Inadequate labor supply</text>
  <text x="220" y="278" fill="#38bdf8" font-size="10" font-weight="600" text-anchor="middle">Increasing Returns Phase</text>

  <!-- Over-population Zone (Right) -->
  <rect x="530" y="200" width="180" height="85" rx="10" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="620" y="225" fill="#f43f5e" font-size="13" font-weight="700" text-anchor="middle">OVER-POPULATION</text>
  <text x="620" y="245" fill="#fecdd3" font-size="11" text-anchor="middle">• Amenities overstretched</text>
  <text x="620" y="262" fill="#fecdd3" font-size="11" text-anchor="middle">• High dependency &amp; poverty</text>
  <text x="620" y="278" fill="#f43f5e" font-size="10" font-weight="600" text-anchor="middle">Diminishing Returns Phase</text>
</svg>"""

SVG_POPULATION_PYRAMID_STRUCTURE = """<svg viewBox="0 0 840 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Comparative Age Structures: Young vs Ageing Populations</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Broad-Based Developing Structure (Kenya) vs Narrow-Based Developed Structure</text>

  <!-- Left: Young Population (Kenya / Developing) -->
  <rect x="40" y="80" width="360" height="320" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
  <text x="220" y="110" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">YOUNG POPULATION (Developing)</text>
  <text x="220" y="128" fill="#94a3b8" font-size="11" text-anchor="middle">High Birth Rate • Heavy Youth Dependency</text>

  <!-- Pyramid Bars (Young) -->
  <!-- 65+ Elderly (Narrow) -->
  <rect x="180" y="150" width="80" height="24" rx="4" fill="#a855f7" />
  <text x="220" y="167" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">65+ Years (5%)</text>

  <!-- 15-64 Working Age (Medium) -->
  <rect x="120" y="185" width="200" height="45" rx="6" fill="#0284c7" />
  <text x="220" y="212" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">15–64 Working Age (45%)</text>

  <!-- 0-14 Children (Broad Base) -->
  <rect x="65" y="240" width="310" height="60" rx="8" fill="#059669" />
  <text x="220" y="275" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">0–14 Children &amp; Youth (50%)</text>

  <text x="220" y="325" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Dependency Ratio &gt; 100%</text>
  <text x="220" y="345" fill="#94a3b8" font-size="10" text-anchor="middle">High government spending on schools &amp; clinics</text>
  <text x="220" y="362" fill="#34d399" font-size="10" text-anchor="middle">Future demographic dividend / abundant labor</text>

  <!-- Right: Ageing Population (Developed Nations) -->
  <rect x="440" y="80" width="360" height="320" rx="14" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5" />
  <text x="620" y="110" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">AGEING POPULATION (Developed)</text>
  <text x="620" y="128" fill="#94a3b8" font-size="11" text-anchor="middle">Low Birth Rate • High Life Expectancy</text>

  <!-- Pyramid Bars (Ageing) -->
  <!-- 65+ Elderly (Broad Top) -->
  <rect x="490" y="150" width="260" height="45" rx="6" fill="#a855f7" />
  <text x="620" y="177" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">65+ Elderly Retirees (28%)</text>

  <!-- 15-64 Working Age (Medium) -->
  <rect x="520" y="205" width="200" height="45" rx="6" fill="#0284c7" />
  <text x="620" y="232" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">15–64 Working Age (55%)</text>

  <!-- 0-14 Children (Narrow Base) -->
  <rect x="555" y="260" width="130" height="40" rx="6" fill="#059669" />
  <text x="620" y="285" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">0–14 Children (17%)</text>

  <text x="620" y="325" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Manpower Scarcity &amp; Pension Burden</text>
  <text x="620" y="345" fill="#94a3b8" font-size="10" text-anchor="middle">Heavy pension and geriatric care expenditure</text>
  <text x="620" y="362" fill="#f43f5e" font-size="10" text-anchor="middle">Shrinking future workforce &amp; labor mobility deficit</text>
</svg>"""

SVG_LABOR_FORCE_CLASSIFICATION_TREE = """<svg viewBox="0 0 860 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <marker id="trArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="430" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">The Structural Classification of National Labor Resources</text>
  <text x="430" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">From Total Population to Employed and Involuntarily Unemployed</text>

  <!-- Level 1: TOTAL POPULATION -->
  <rect x="310" y="80" width="240" height="45" rx="10" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
  <text x="430" y="108" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">TOTAL POPULATION</text>

  <path d="M 360 125 L 200 160" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#trArrow)" />
  <path d="M 500 125 L 660 160" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#trArrow)" />

  <!-- Level 2 Left: Dependents -->
  <rect x="90" y="160" width="220" height="50" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5" />
  <text x="200" y="182" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">DEPENDENTS</text>
  <text x="200" y="200" fill="#94a3b8" font-size="10" text-anchor="middle">0–14 Yrs • 65+ Retirees • Sick</text>

  <!-- Level 2 Right: Working-Age Population -->
  <rect x="550" y="160" width="220" height="50" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
  <text x="660" y="182" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">WORKING-AGE (15–64)</text>
  <text x="660" y="200" fill="#e0f2fe" font-size="10" text-anchor="middle">Physically Fit Population</text>

  <path d="M 600 210 L 480 250" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#trArrow)" />
  <path d="M 720 210 L 750 250" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#trArrow)" />

  <!-- Level 3 Left: Out of Labor Force -->
  <rect x="360" y="250" width="210" height="50" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5" />
  <text x="465" y="272" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">OUT OF LABOR FORCE</text>
  <text x="465" y="290" fill="#94a3b8" font-size="10" text-anchor="middle">Full-time Students • Non-seekers</text>

  <!-- Level 3 Right: LABOR FORCE -->
  <rect x="630" y="250" width="210" height="50" rx="8" fill="#059669" stroke="#34d399" stroke-width="2" />
  <text x="735" y="272" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">LABOR FORCE (Active)</text>
  <text x="735" y="290" fill="#d1fae5" font-size="10" text-anchor="middle">Employed + Active Seekers</text>

  <path d="M 690 300 L 610 345" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#trArrow)" />
  <path d="M 780 300 L 780 345" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#trArrow)" />

  <!-- Level 4 Left: Employed -->
  <rect x="500" y="345" width="200" height="60" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="600" y="368" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">EMPLOYED</text>
  <text x="600" y="386" fill="#ffffff" font-size="10" text-anchor="middle">• Full-time Formal/Informal</text>
  <text x="600" y="398" fill="#a7f3d0" font-size="9" text-anchor="middle">• Underemployed (Time/Skills)</text>

  <!-- Level 4 Right: Unemployed -->
  <rect x="710" y="345" width="135" height="60" rx="8" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="777" y="368" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">UNEMPLOYED</text>
  <text x="777" y="386" fill="#fecdd3" font-size="10" text-anchor="middle">Actively seeking</text>
  <text x="777" y="398" fill="#fecdd3" font-size="9" text-anchor="middle">work at market wage</text>
</svg>"""

SVG_UNEMPLOYMENT_POLICY_MATRIX = """<svg viewBox="0 0 840 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <marker id="uArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Cause-to-Solution Policy Alignment for Unemployment</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Targeted State Interventions Addressing Root Labor Market Distortions</text>

  <!-- Row 1: Structural -->
  <rect x="40" y="90" width="320" height="60" rx="10" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="200" y="115" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Skills Mismatch &amp; Theory-Based Syllabus</text>
  <text x="200" y="135" fill="#fecdd3" font-size="10" text-anchor="middle">(Structural Unemployment)</text>

  <line x1="360" y1="120" x2="470" y2="120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#uArrow)" />

  <rect x="480" y="90" width="320" height="60" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="640" y="115" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Curriculum Reform (TVET &amp; CBC)</text>
  <text x="640" y="135" fill="#d1fae5" font-size="10" text-anchor="middle">Practical vocational &amp; technical training</text>

  <!-- Row 2: Capital Shortage -->
  <rect x="40" y="170" width="320" height="60" rx="10" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="200" y="195" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Inadequate Business Capital for Youth</text>
  <text x="200" y="215" fill="#fecdd3" font-size="10" text-anchor="middle">(Job-Seekers vs Job-Creators)</text>

  <line x1="360" y1="200" x2="470" y2="200" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#uArrow)" />

  <rect x="480" y="170" width="320" height="60" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="640" y="195" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Youth &amp; SME Enterprise Funds</text>
  <text x="640" y="215" fill="#d1fae5" font-size="10" text-anchor="middle">Low-interest credit (YEDF, WEF, Uwezo)</text>

  <!-- Row 3: Rural-Urban Migration -->
  <rect x="40" y="250" width="320" height="60" rx="10" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="200" y="275" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Rural-Urban Migration &amp; City Flooding</text>
  <text x="200" y="295" fill="#fecdd3" font-size="10" text-anchor="middle">(Urban Slum Unemployment)</text>

  <line x1="360" y1="280" x2="470" y2="280" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#uArrow)" />

  <rect x="480" y="250" width="320" height="60" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="640" y="275" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Rural Delocalization &amp; Electrification</text>
  <text x="640" y="295" fill="#d1fae5" font-size="10" text-anchor="middle">Decentralizing roads &amp; rural industry hubs</text>

  <!-- Row 4: Seasonal Agricultural Lull -->
  <rect x="40" y="330" width="320" height="60" rx="10" fill="#1e1b4b" stroke="#f43f5e" stroke-width="1.5" />
  <text x="200" y="355" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Off-Season Agricultural Inactivity</text>
  <text x="200" y="375" fill="#fecdd3" font-size="10" text-anchor="middle">(Seasonal Unemployment)</text>

  <line x1="360" y1="360" x2="470" y2="360" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#uArrow)" />

  <rect x="480" y="330" width="320" height="60" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="1.5" />
  <text x="640" y="355" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Agro-Processing &amp; Diversification</text>
  <text x="640" y="375" fill="#d1fae5" font-size="10" text-anchor="middle">Adding value to create year-round factory jobs</text>

  <text x="420" y="420" fill="#94a3b8" font-size="11" text-anchor="middle">A holistic national strategy combines quantitative job creation with qualitative skill matching.</text>
</svg>"""
