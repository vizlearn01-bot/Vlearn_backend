"""
VLearn Form 4 Business Studies — Topic 6: Economic Development and Planning
Educational Dark-Mode SVG Vector Graphics
"""

SVG_GROWTH_VS_DEVELOPMENT_CONCENTRIC = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">ECONOMIC GROWTH VS. ECONOMIC DEVELOPMENT</text>
  
  <!-- Outer Circle: Economic Development -->
  <circle cx="450" cy="245" r="180" fill="#1e293b" stroke="#34d399" stroke-width="3" stroke-dasharray="6,3"/>
  <text x="450" y="85" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">ECONOMIC DEVELOPMENT (Qualitative &amp; Structural Transformation)</text>

  <!-- Development Elements Surrounding Inner Circle -->
  <text x="320" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Poverty Reduction</text>
  <text x="580" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Fair Wealth Distribution</text>

  <text x="210" y="210" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Sectoral Shift (Agri → Mfg)</text>
  <text x="690" y="210" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Literacy &amp; Skills Expansion</text>

  <text x="210" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Improved Healthcare</text>
  <text x="690" y="280" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Institutional Strengthening</text>

  <text x="320" y="380" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Basic Needs Provision</text>
  <text x="580" y="380" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Opportunity Creation</text>

  <!-- Inner Circle: Economic Growth -->
  <circle cx="450" cy="245" r="95" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="450" y="225" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ECONOMIC GROWTH</text>
  <text x="450" y="248" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">(Quantitative Output)</text>
  <text x="450" y="270" fill="#e0f2fe" font-family="sans-serif" font-size="11" text-anchor="middle">GDP / GNP / National Income</text>
  <text x="450" y="285" fill="#e0f2fe" font-family="sans-serif" font-size="10" text-anchor="middle">"Making the cake bigger"</text>

  <!-- Summary Footer -->
  <rect x="180" y="405" width="540" height="35" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
  <text x="450" y="427" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Growth is necessary for development, but growth can occur without development!</text>
</svg>"""

SVG_VICIOUS_CYCLE_OF_POVERTY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">THE VICIOUS CYCLE OF POVERTY IN UNDER-DEVELOPMENT</text>
  
  <!-- Step 1: Low Income -->
  <g transform="translate(360, 60)">
    <rect x="0" y="0" width="180" height="70" rx="12" fill="#be123c"/>
    <text x="90" y="28" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">1. Low Per-Capita</text>
    <text x="90" y="48" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Income</text>
  </g>

  <path d="M 540 95 C 650 95, 750 150, 750 200" stroke="#f87171" stroke-width="3" fill="none" marker-end="url(#arrow)"/>

  <!-- Step 2: Low Savings -->
  <g transform="translate(660, 200)">
    <rect x="0" y="0" width="180" height="70" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="90" y="28" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">2. Low Savings Rate</text>
    <text x="90" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">(All income spent on food)</text>
  </g>

  <path d="M 750 270 C 750 340, 650 390, 540 390" stroke="#f87171" stroke-width="3" fill="none"/>

  <!-- Step 3: Low Investment -->
  <g transform="translate(360, 355)">
    <rect x="0" y="0" width="180" height="70" rx="12" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="90" y="28" fill="#f43f5e" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">3. Low Investment &amp;</text>
    <text x="90" y="48" fill="#f43f5e" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Capital Accumulation</text>
  </g>

  <path d="M 360 390 C 250 390, 150 340, 150 270" stroke="#f87171" stroke-width="3" fill="none"/>

  <!-- Step 4: Low Productivity -->
  <g transform="translate(60, 200)">
    <rect x="0" y="0" width="180" height="70" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="28" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">4. Low Productivity &amp;</text>
    <text x="90" y="48" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Manual Tech Use</text>
  </g>

  <path d="M 150 200 C 150 150, 250 95, 360 95" stroke="#f87171" stroke-width="3" fill="none"/>

  <!-- Center External Pressure Box -->
  <g transform="translate(340, 180)">
    <rect x="0" y="0" width="220" height="110" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="110" y="25" fill="#ef4444" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">External Accelerators</text>
    <text x="15" y="50" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Rapid Population Explosion</text>
    <text x="15" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="11">• High Dependency Ratio</text>
    <text x="15" y="90" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Dominance of Subsistence</text>
  </g>
</svg>"""

SVG_DEVELOPMENT_OBSTACLES_BARRIERS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">FIVE STRUCTURAL OBSTACLES TO ECONOMIC DEVELOPMENT</text>
  
  <g transform="translate(40, 70)">
    <!-- Obstacle 1 -->
    <rect x="0" y="0" width="150" height="340" rx="12" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect x="0" y="0" width="150" height="40" rx="12" fill="#be123c"/>
    <text x="75" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">1. Capital Deficit</text>
    <text x="10" y="70" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold">• Inadequate Capital</text>
    <text x="10" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Lack of machinery,</text>
    <text x="10" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="11">factories, power</text>
    <text x="10" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="11">grids, &amp; railways.</text>
    <text x="10" y="180" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Prevents manufacturing</text>
    <text x="10" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="11">and industrial</text>
    <text x="10" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="11">take-off.</text>

    <!-- Obstacle 2 -->
    <rect x="170" y="0" width="150" height="340" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect x="170" y="0" width="150" height="40" rx="12" fill="#d97706"/>
    <text x="245" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">2. Backward Tech</text>
    <text x="180" y="70" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">• Poor Technology</text>
    <text x="180" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Inefficient manual</text>
    <text x="180" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="11">production methods.</text>
    <text x="180" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="11">• High waste and low</text>
    <text x="180" y="180" fill="#cbd5e1" font-family="sans-serif" font-size="11">product quality.</text>
    <text x="180" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Uncompetitive in</text>
    <text x="180" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="11">global markets.</text>

    <!-- Obstacle 3 -->
    <rect x="340" y="0" width="150" height="340" rx="12" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
    <rect x="340" y="0" width="150" height="40" rx="12" fill="#6d28d9"/>
    <text x="415" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">3. Skill Shortage</text>
    <text x="350" y="70" fill="#a78bfa" font-family="sans-serif" font-size="12" font-weight="bold">• Human Resource</text>
    <text x="350" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Shortage of local</text>
    <text x="350" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="11">engineers, managers,</text>
    <text x="350" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="11">&amp; entrepreneurs.</text>
    <text x="350" y="180" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Cannot process</text>
    <text x="350" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="11">or manage domestic</text>
    <text x="350" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="11">mineral wealth.</text>

    <!-- Obstacle 4 -->
    <rect x="510" y="0" width="150" height="340" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <rect x="510" y="0" width="150" height="40" rx="12" fill="#b91c1c"/>
    <text x="585" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">4. Unfavorable Climate</text>
    <text x="520" y="70" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold">• Poor Domestic Env</text>
    <text x="520" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Political instability</text>
    <text x="520" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="11">&amp; corruption.</text>
    <text x="520" y="160" fill="#cbd5e1" font-family="sans-serif" font-size="11">• High insecurity &amp;</text>
    <text x="520" y="180" fill="#cbd5e1" font-family="sans-serif" font-size="11">burdensome laws.</text>
    <text x="520" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Scares local &amp;</text>
    <text x="520" y="240" fill="#cbd5e1" font-family="sans-serif" font-size="11">foreign investors.</text>

    <!-- Obstacle 5 -->
    <rect x="680" y="0" width="140" height="340" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="680" y="0" width="140" height="40" rx="12" fill="#0284c7"/>
    <text x="750" y="25" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">5. Resource Deficit</text>
    <text x="690" y="70" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">• Low Natural Env</text>
    <text x="690" y="100" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Lack of fertile soil,</text>
    <text x="690" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="11">erratic rainfall,</text>
    <text x="690" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="11">or minerals.</text>
    <text x="690" y="180" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Natural baseline</text>
    <text x="690" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="11">disadvantages for</text>
    <text x="690" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="11">take-off.</text>
  </g>
</svg>"""

SVG_DEVELOPMENT_PLANNING_PIPELINE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 440" width="100%" height="100%">
  <rect width="900" height="440" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">DEVELOPMENT PLANNING PIPELINE &amp; BALANCED REGIONAL EXECUTION</text>

  <!-- Top: National Goals -->
  <g transform="translate(250, 60)">
    <rect x="0" y="0" width="400" height="65" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="28" fill="#38bdf8" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">1. NATIONAL LONG-RUN POLICY OBJECTIVES</text>
    <text x="200" y="50" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Eradicate Illiteracy • Improve Health • Eliminate Poverty • Reduce Foreign Reliance</text>
  </g>

  <path d="M 450 125 L 450 160" stroke="#38bdf8" stroke-width="2.5" fill="none"/>

  <!-- Middle: Development Plan -->
  <g transform="translate(200, 160)">
    <rect x="0" y="0" width="500" height="75" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="250" y="28" fill="#fbbf24" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">2. STRATEGIC DEVELOPMENT PLAN (5-Year Blueprint)</text>
    <text x="250" y="50" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">Appropriate Resource Allocation • Donor Bargaining • Industrial Coordination</text>
  </g>

  <path d="M 450 235 L 200 280" stroke="#fbbf24" stroke-width="2" fill="none"/>
  <path d="M 450 235 L 450 280" stroke="#fbbf24" stroke-width="2" fill="none"/>
  <path d="M 450 235 L 700 280" stroke="#fbbf24" stroke-width="2" fill="none"/>

  <!-- Bottom: Balanced Regional Projects -->
  <g transform="translate(40, 280)">
    <rect x="0" y="0" width="250" height="110" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="125" y="28" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Region A Execution</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Constructing TVET Colleges</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Rural Electrification Grid</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Agro-processing Plants</text>
  </g>

  <g transform="translate(325, 280)">
    <rect x="0" y="0" width="250" height="110" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="125" y="28" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Region B Execution</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Public Level-5 Hospital</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Irrigation Dam Construction</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Local Market Infrastructure</text>
  </g>

  <g transform="translate(610, 280)">
    <rect x="0" y="0" width="250" height="110" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="125" y="28" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Region C Execution</text>
    <text x="15" y="55" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Tarmac Highway Links</text>
    <text x="15" y="75" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Water Treatment Facility</text>
    <text x="15" y="95" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Industrial Park Licensing</text>
  </g>
</svg>"""

SVG_FORMULATION_VS_IMPLEMENTATION_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">PLANNING CHALLENGES: FORMULATION VS. IMPLEMENTATION STAGES</text>
  
  <!-- Left Side: Formulation Stage -->
  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="390" height="380" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="45" rx="14" fill="#0284c7"/>
    <text x="195" y="28" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">STAGE 1: PLAN FORMULATION</text>

    <text x="195" y="70" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">(Drafting, Data Gathering, Blueprint Design)</text>

    <text x="20" y="100" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">1. Lack of Accurate Data:</text>
    <text x="20" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="12">Inaccurate statistics leads to guesswork in planning.</text>

    <text x="20" y="155" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">2. Large Subsistence Sector:</text>
    <text x="20" y="175" fill="#cbd5e1" font-family="sans-serif" font-size="12">Non-monetized production hard to measure or value.</text>

    <text x="20" y="210" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">3. Lack of Qualified Personnel:</text>
    <text x="20" y="230" fill="#cbd5e1" font-family="sans-serif" font-size="12">Shortage of local economists &amp; statisticians.</text>

    <text x="20" y="265" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">4. Transfer of Inappropriate Plans:</text>
    <text x="20" y="285" fill="#cbd5e1" font-family="sans-serif" font-size="12">Copy-pasting foreign plans unsuitable for local context.</text>

    <rect x="20" y="320" width="350" height="40" rx="8" fill="#0284c7" fill-opacity="0.3"/>
    <text x="195" y="345" fill="#e0f2fe" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Focus: Failures during the WRITING of the plan.</text>
  </g>

  <!-- Right Side: Implementation Stage -->
  <g transform="translate(470, 65)">
    <rect x="0" y="0" width="390" height="380" rx="14" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="45" rx="14" fill="#be123c"/>
    <text x="195" y="28" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">STAGE 2: PLAN IMPLEMENTATION</text>

    <text x="195" y="70" fill="#f43f5e" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">(Execution, Funding, Construction, Real World)</text>

    <text x="20" y="100" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">1. Over-Reliance on Foreign Aid:</text>
    <text x="20" y="120" fill="#cbd5e1" font-family="sans-serif" font-size="12">Donor delays or political conditionality stalls projects.</text>

    <text x="20" y="150" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">2. Natural Calamities &amp; Emergencies:</text>
    <text x="20" y="170" fill="#cbd5e1" font-family="sans-serif" font-size="12">Droughts &amp; floods force emergency money diversion.</text>

    <text x="20" y="200" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">3. Severe Price Inflation:</text>
    <text x="20" y="220" fill="#cbd5e1" font-family="sans-serif" font-size="12">Raw material cost spikes make allocations insufficient.</text>

    <text x="20" y="250" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold">4. Lack of Political Will &amp; Beneficiary Exclusion:</text>
    <text x="20" y="270" fill="#cbd5e1" font-family="sans-serif" font-size="12">Lack of leadership commitment &amp; top-down exclusion.</text>

    <rect x="20" y="320" width="350" height="40" rx="8" fill="#be123c" fill-opacity="0.3"/>
    <text x="195" y="345" fill="#fca5a5" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Focus: Failures during the DOING of the projects.</text>
  </g>
</svg>"""
