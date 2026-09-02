"""
VLearn CBC Grade 10 History — Topic 8: African Civilisations up to the 19th Century
Authoritative High-Quality SVG Visual Assets and Historical Cartography
"""

# =============================================================================
# SVG 1: Map of Great Lakes Civilisations and Kingdoms (Lesson 1)
# =============================================================================
SVG_MAP_GREAT_LAKES_CIVILISATIONS = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderMap1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradLake" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="gradOcean" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#082f49"/>
    </linearGradient>
    <linearGradient id="gradBuganda" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="gradWanga" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradNyamwezi" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadowMap1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderMap1)" stroke="#334155" stroke-width="1.5" filter="url(#shadowMap1)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="62" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="19" font-weight="bold" text-anchor="middle" letter-spacing="0.5">GREAT LAKES CIVILISATIONS &amp; REGIONAL GEOGRAPHY (PRE-19TH CENTURY)</text>
  <text x="480" y="77" fill="#94a3b8" font-size="12" text-anchor="middle">Comparative Geopolitical Locations: Buganda Kingdom, Wanga Kingdom, and Nyamwezi Territory</text>

  <!-- Map Canvas -->
  <rect x="40" y="105" width="570" height="480" rx="12" fill="#1a2234" stroke="#334155" stroke-width="1"/>

  <!-- Grid lines (Latitude / Longitude) -->
  <line x1="40" y1="210" x2="610" y2="210" stroke="#334155" stroke-width="0.75" stroke-dasharray="4,4"/>
  <text x="45" y="206" fill="#64748b" font-size="10">Equator (0°)</text>
  <line x1="40" y1="360" x2="610" y2="360" stroke="#334155" stroke-width="0.75" stroke-dasharray="4,4"/>
  <text x="45" y="356" fill="#64748b" font-size="10">5° S</text>
  <line x1="280" y1="105" x2="280" y2="585" stroke="#334155" stroke-width="0.75" stroke-dasharray="4,4"/>
  <text x="285" y="120" fill="#64748b" font-size="10">34° E</text>

  <!-- Indian Ocean (East) -->
  <path d="M 520,105 Q 550,250 510,380 T 540,585 L 610,585 L 610,105 Z" fill="url(#gradOcean)" opacity="0.85"/>
  <text x="565" y="280" fill="#38bdf8" font-size="12" font-weight="bold" transform="rotate(90, 565, 280)" letter-spacing="2">INDIAN OCEAN</text>

  <!-- Coastal Ports -->
  <circle cx="522" cy="270" r="4.5" fill="#f8fafc" stroke="#dc2626" stroke-width="1.5"/>
  <text x="512" y="265" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="end">Mombasa</text>

  <circle cx="515" cy="380" r="4.5" fill="#f8fafc" stroke="#dc2626" stroke-width="1.5"/>
  <text x="505" y="376" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="end">Bagamoyo</text>

  <!-- Zanzibar Island -->
  <ellipse cx="538" cy="370" rx="6" ry="14" fill="#38bdf8" stroke="#f8fafc" stroke-width="1"/>
  <text x="550" y="374" fill="#38bdf8" font-size="9" font-weight="bold">Zanzibar</text>

  <!-- Lake Victoria (Lake Nalubaale) -->
  <path d="M 210,195 C 240,180 280,185 300,210 C 315,230 310,265 295,290 C 275,315 235,320 210,300 C 190,280 185,250 195,220 Z" fill="url(#gradLake)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="250" y="250" fill="#e0f2fe" font-size="11" font-weight="bold" text-anchor="middle">LAKE VICTORIA</text>
  <text x="250" y="264" fill="#bae6fd" font-size="9" font-style="italic" text-anchor="middle">(Lake Nalubaale)</text>

  <!-- Lake Albert (Northwest) -->
  <ellipse cx="145" cy="155" rx="14" ry="32" transform="rotate(-30, 145, 155)" fill="url(#gradLake)" stroke="#38bdf8" stroke-width="1"/>
  <text x="115" y="145" fill="#93c5fd" font-size="8">L. Albert</text>

  <!-- Lake Tanganyika (West) -->
  <ellipse cx="115" cy="390" rx="15" ry="75" transform="rotate(-15, 115, 390)" fill="url(#gradLake)" stroke="#38bdf8" stroke-width="1"/>
  <text x="75" y="380" fill="#93c5fd" font-size="9" font-weight="bold">L. Tanganyika</text>
  <circle cx="120" cy="345" r="3.5" fill="#f59e0b" stroke="#fff" stroke-width="1"/>
  <text x="130" y="348" fill="#fde68a" font-size="8" font-weight="bold">Ujiji</text>

  <!-- Lake Turkana (Northeast) -->
  <ellipse cx="365" cy="140" rx="10" ry="28" transform="rotate(10, 365, 140)" fill="url(#gradLake)" stroke="#38bdf8" stroke-width="1"/>
  <text x="382" y="145" fill="#93c5fd" font-size="8">L. Turkana</text>

  <!-- 1. BUGANDA KINGDOM (North-West shores of Lake Victoria) -->
  <path d="M 185,170 C 215,160 250,175 255,200 C 235,215 200,210 185,190 Z" fill="url(#gradBuganda)" opacity="0.85" stroke="#c084fc" stroke-width="2"/>
  <circle cx="215" cy="188" r="5" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
  <text x="215" y="162" fill="#e9d5ff" font-size="11" font-weight="bold" text-anchor="middle">BUGANDA KINGDOM</text>
  <text x="215" y="174" fill="#d8b4fe" font-size="8.5" text-anchor="middle">(Capital: Mengo / Rubaga)</text>

  <!-- Bunyoro-Kitara (Neighbor) -->
  <path d="M 155,165 Q 180,145 200,160 Q 175,185 155,165 Z" fill="#475569" opacity="0.6" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="175" y="152" fill="#cbd5e1" font-size="8">Bunyoro</text>

  <!-- 2. THE WANGA KINGDOM (Northeast of Lake Victoria, Western Kenya) -->
  <!-- Nzoia River Basin -->
  <path d="M 340,200 Q 315,210 295,215" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="345" y="196" fill="#38bdf8" font-size="8">Nzoia R.</text>
  <ellipse cx="305" cy="220" rx="28" ry="20" fill="url(#gradWanga)" opacity="0.85" stroke="#34d399" stroke-width="2"/>
  <circle cx="305" cy="220" r="5" fill="#ffffff" stroke="#059669" stroke-width="2"/>
  <text x="338" y="222" fill="#a7f3d0" font-size="11" font-weight="bold">WANGA KINGDOM</text>
  <text x="338" y="234" fill="#6ee7b7" font-size="8.5">(Mumia's / Elureko)</text>

  <!-- Mt. Kenya / Mt. Elgon Cues -->
  <polygon points="305,180 312,192 298,192" fill="#64748b"/>
  <text x="315" y="188" fill="#94a3b8" font-size="7.5">Mt. Elgon</text>

  <polygon points="410,240 420,256 400,256" fill="#64748b"/>
  <text x="424" y="252" fill="#94a3b8" font-size="7.5">Mt. Kenya</text>

  <!-- 3. NYAMWEZI TERRITORY (Central Western Tanzania) -->
  <path d="M 160,330 C 230,310 290,325 310,380 C 290,440 200,450 160,400 Z" fill="url(#gradNyamwezi)" opacity="0.8" stroke="#fbbf24" stroke-width="2"/>
  <circle cx="230" cy="370" r="5.5" fill="#ffffff" stroke="#d97706" stroke-width="2"/>
  <text x="230" y="360" fill="#fef3c7" font-size="12" font-weight="bold" text-anchor="middle">NYAMWEZI CHIEFDOMS</text>
  <text x="230" y="388" fill="#fde68a" font-size="9" font-weight="bold" text-anchor="middle">Tabora (Kazeh)</text>
  <text x="230" y="400" fill="#fde047" font-size="8" text-anchor="middle">("People of the Moon")</text>

  <!-- Trade route arrow from Tabora to Bagamoyo -->
  <path d="M 240,375 Q 370,400 510,380" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6,4"/>
  <polygon points="508,375 518,380 508,385" fill="#f59e0b"/>
  <text x="380" y="382" fill="#fef08a" font-size="9" font-weight="bold" transform="rotate(-4, 380, 382)">Central Trade Route</text>

  <!-- Trade route from Wanga to Coast -->
  <path d="M 315,235 Q 430,270 518,272" fill="none" stroke="#34d399" stroke-width="1.8" stroke-dasharray="5,4"/>
  <polygon points="515,268 524,272 515,276" fill="#34d399"/>

  <!-- Compass Rose (Top Left of Map) -->
  <g transform="translate(70, 135)">
    <circle cx="0" cy="0" r="18" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <polygon points="0,-15 4,-3 0,0 -4,-3" fill="#ef4444"/>
    <polygon points="0,15 4,3 0,0 -4,3" fill="#94a3b8"/>
    <polygon points="15,0 3,4 0,0 3,-4" fill="#94a3b8"/>
    <polygon points="-15,0 -3,4 0,0 -3,-4" fill="#94a3b8"/>
    <text x="0" y="-18" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">N</text>
  </g>

  <!-- Right Column: Case Study Cards & Comparative Legend -->
  <!-- Card 1: Buganda -->
  <rect x="625" y="105" width="295" height="150" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5"/>
  <rect x="625" y="105" width="295" height="28" rx="10" fill="url(#gradBuganda)"/>
  <text x="772" y="124" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">1. BUGANDA KINGDOM (UGANDA)</text>
  <text x="637" y="148" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#c084fc">Environment:</tspan> High-rainfall, fertile lake shores</text>
  <text x="637" y="166" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#c084fc">Economy:</tspan> Intensive perennial banana farming</text>
  <text x="637" y="184" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#c084fc">Structure:</tspan> Highly centralized state (Kabaka)</text>
  <text x="637" y="202" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#c084fc">Strategic Power:</tspan> Lake Victoria canoe navy</text>
  <text x="637" y="220" fill="#94a3b8" font-size="10" font-style="italic">Supported dense population &amp; standing civil service.</text>

  <!-- Card 2: Wanga -->
  <rect x="625" y="265" width="295" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <rect x="625" y="265" width="295" height="28" rx="10" fill="url(#gradWanga)"/>
  <text x="772" y="284" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. WANGA KINGDOM (KENYA)</text>
  <text x="637" y="308" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Environment:</tspan> Fertile Nzoia River valley basin</text>
  <text x="637" y="326" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Economy:</tspan> Grain surplus &amp; iron metallurgy guilds</text>
  <text x="637" y="344" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Structure:</tspan> Centralized monarch (Nabongo/Mwami)</text>
  <text x="637" y="362" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Governance:</tspan> Checked by Eshihanya (Elders Council)</text>
  <text x="637" y="380" fill="#94a3b8" font-size="10" font-style="italic">Only centralized pre-colonial state in Kenya.</text>

  <!-- Card 3: Nyamwezi -->
  <rect x="625" y="425" width="295" height="160" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="625" y="425" width="295" height="28" rx="10" fill="url(#gradNyamwezi)"/>
  <text x="772" y="444" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. NYAMWEZI CHIEFDOMS (TANZANIA)</text>
  <text x="637" y="468" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#fde047">Environment:</tspan> Drier central savannah plateau</text>
  <text x="637" y="486" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#fde047">Economy:</tspan> Long-distance trade caravan pioneers</text>
  <text x="637" y="504" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#fde047">Structure:</tspan> Decentralized autonomous chiefdoms</text>
  <text x="637" y="522" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#fde047">Leadership:</tspan> Ruled by Ntemi &amp; Wanyampala council</text>
  <text x="637" y="540" fill="#94a3b8" font-size="10" font-style="italic">United in 1870s under Mirambo's military reform.</text>
</svg>'''

# =============================================================================
# SVG 2: Buganda Kingdom Political Hierarchy (Lesson 2)
# =============================================================================
SVG_BUGANDA_POLITICAL_HIERARCHY = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderHierarchy" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradKabaka" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradKatikiro" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#7e22ce"/>
    </linearGradient>
    <linearGradient id="gradSaza" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="gradGombolola" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>
    <linearGradient id="gradBataka" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadowHierarchy" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderHierarchy)" stroke="#334155" stroke-width="1.5" filter="url(#shadowHierarchy)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="20" font-weight="bold" text-anchor="middle" letter-spacing="0.5">BUGANDA KINGDOM: CENTRALISED POLITICAL PYRAMID &amp; ADMINISTRATION</text>
  <text x="480" y="76" fill="#94a3b8" font-size="12" text-anchor="middle">Hierarchical Command Structure from the Kabaka down to Clan Lineages (*Ebika*)</text>

  <!-- Pyramid Tiers (Left/Center area: x: 40 to 620) -->

  <!-- Tier 1: Kabaka -->
  <polygon points="330,110 200,195 460,195" fill="url(#gradKabaka)" stroke="#fef08a" stroke-width="2" filter="url(#shadowHierarchy)"/>
  <text x="330" y="150" fill="#451a03" font-size="15" font-weight="bold" text-anchor="middle">THE KABAKA</text>
  <text x="330" y="168" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle">(Supreme Monarch &amp; Commander-in-Chief)</text>
  <text x="330" y="184" fill="#78350f" font-size="9" text-anchor="middle">Appoints all civil &amp; military governors</text>

  <!-- Tier 2: Katikkiro & Lukiiko -->
  <polygon points="200,200 460,200 510,285 150,285" fill="url(#gradKatikiro)" stroke="#c084fc" stroke-width="2" filter="url(#shadowHierarchy)"/>
  <text x="330" y="235" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">KATIKKIRO (Prime Minister) &amp; LUKIIKO (Parliament)</text>
  <text x="330" y="255" fill="#f3e8ff" font-size="10.5" text-anchor="middle">• Katikkiro: Chief Executive Officer &amp; Royal Court Administrator</text>
  <text x="330" y="272" fill="#f3e8ff" font-size="10.5" text-anchor="middle">• Lukiiko: Great Council of Saza Chiefs, Dignitaries &amp; Senior Clan Heads</text>

  <!-- Tier 3: Saza Chiefs -->
  <polygon points="150,290 510,290 560,375 100,375" fill="url(#gradSaza)" stroke="#60a5fa" stroke-width="2" filter="url(#shadowHierarchy)"/>
  <text x="330" y="322" fill="#ffffff" font-size="13.5" font-weight="bold" text-anchor="middle">SAZA CHIEFS (20 County Governors)</text>
  <text x="330" y="342" fill="#dbeafe" font-size="10.5" text-anchor="middle">• Appointed directly by the Kabaka (Merit-based loyalty, non-hereditary)</text>
  <text x="330" y="360" fill="#dbeafe" font-size="10.5" text-anchor="middle">• Responsible for provincial tax collection, law enforcement &amp; troop levies</text>

  <!-- Tier 4: Gombolola & Batongole Chiefs -->
  <polygon points="100,380 560,380 610,470 50,470" fill="url(#gradGombolola)" stroke="#22d3ee" stroke-width="2" filter="url(#shadowHierarchy)"/>
  <text x="330" y="412" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">GOMBOLOLA (Sub-County) &amp; BATONGOLE (Parish) CHIEFS</text>
  <text x="330" y="432" fill="#cffafe" font-size="10" text-anchor="middle">• Administer local districts, maintain royal road networks (*Enguudo*)</text>
  <text x="330" y="450" fill="#cffafe" font-size="10" text-anchor="middle">• Mobilize communal labor (*Bulungi Bwansi*) &amp; maintain banana agriculture</text>

  <!-- Tier 5: Bataka & Ebika -->
  <polygon points="50,475 610,475 650,575 10,575" fill="url(#gradBataka)" stroke="#34d399" stroke-width="2" filter="url(#shadowHierarchy)"/>
  <text x="330" y="508" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">BATAKA (Clan Heads) &amp; EBIKA (52 Hereditary Clans)</text>
  <text x="330" y="530" fill="#d1fae5" font-size="10" text-anchor="middle">• Custodians of ancestral burial grounds (*Butaka*), cultural heritage &amp; land rights</text>
  <text x="330" y="548" fill="#d1fae5" font-size="10" text-anchor="middle">• Each clan performed specific sacred functions in the Kabaka’s court</text>
  <text x="330" y="565" fill="#a7f3d0" font-size="9" text-anchor="middle">• General Population: Farmers, Artisans, Bark-Cloth Makers, Fishermen, Canoe Navy</text>

  <!-- Right Column: Institutional Features & Analytical Cards (x: 640 to 920) -->

  <!-- Card 1: Key Strength: Meritocratic Civil Service -->
  <rect x="635" y="110" width="290" height="150" rx="10" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
  <rect x="635" y="110" width="290" height="26" rx="10" fill="#d97706"/>
  <text x="780" y="128" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">KEY STRENGTH: NON-HEREDITARY CHIEFS</text>
  <text x="647" y="152" fill="#e2e8f0" font-size="10.5">• Unlike feudal systems where chiefs inherited</text>
  <text x="647" y="168" fill="#e2e8f0" font-size="10.5">  titles, the <tspan font-weight="bold" fill="#fde047">Kabaka personally appointed</tspan></text>
  <text x="647" y="184" fill="#e2e8f0" font-size="10.5">  and removed Saza and Batongole chiefs.</text>
  <text x="647" y="206" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold" fill="#fde047">Impact:</tspan> Guaranteed unquestioned loyalty,</text>
  <text x="647" y="222" fill="#e2e8f0" font-size="10.5">  prevented regional warlordism, and built</text>
  <text x="647" y="238" fill="#e2e8f0" font-size="10.5">  a highly disciplined state administration.</text>

  <!-- Card 2: Checks & Clan Balance -->
  <rect x="635" y="270" width="290" height="150" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <rect x="635" y="270" width="290" height="26" rx="10" fill="#7e22ce"/>
  <text x="780" y="288" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">CHECKS &amp; CULTURAL DUALITY</text>
  <text x="647" y="312" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold" fill="#d8b4fe">Bakungu (Appointed)</tspan> vs <tspan font-weight="bold" fill="#a7f3d0">Bataka (Hereditary):</tspan></text>
  <text x="647" y="328" fill="#e2e8f0" font-size="10.5">  A dynamic tension between royal civil servants</text>
  <text x="647" y="344" fill="#e2e8f0" font-size="10.5">  and traditional clan custodians.</text>
  <text x="647" y="366" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold" fill="#d8b4fe">The Lukiiko:</tspan> Served as both parliament</text>
  <text x="647" y="382" fill="#e2e8f0" font-size="10.5">  and appellate court, debating policies</text>
  <text x="647" y="398" fill="#e2e8f0" font-size="10.5">  and advising the Kabaka on state affairs.</text>

  <!-- Card 3: Civic Duty (Bulungi Bwansi) -->
  <rect x="635" y="430" width="290" height="150" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <rect x="635" y="430" width="290" height="26" rx="10" fill="#047857"/>
  <text x="780" y="448" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">CIVIC DUTY: "BULUNGI BWANSI"</text>
  <text x="647" y="472" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold" fill="#6ee7b7">"For the Good of the Nation":</tspan></text>
  <text x="647" y="488" fill="#e2e8f0" font-size="10.5">  Communal labor system where all citizens</text>
  <text x="647" y="504" fill="#e2e8f0" font-size="10.5">  participated in maintaining public roads,</text>
  <text x="647" y="520" fill="#e2e8f0" font-size="10.5">  drainage channels, and royal palace halls.</text>
  <text x="647" y="542" fill="#94a3b8" font-size="10" font-style="italic">• Predecessor of modern community service</text>
  <text x="647" y="558" fill="#94a3b8" font-size="10" font-style="italic">  and grassroots participatory governance.</text>
</svg>'''

# =============================================================================
# SVG 3: Map of 19th-Century Long-Distance Caravan Trade Routes (Lesson 3)
# =============================================================================
SVG_MAP_TRADE_ROUTES_EAST_AFRICA = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderTradeMap" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradTradeCentral" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradTradeNorth" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradTradeSouth" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <filter id="shadowTradeMap" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderTradeMap)" stroke="#334155" stroke-width="1.5" filter="url(#shadowTradeMap)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="20" font-weight="bold" text-anchor="middle" letter-spacing="0.5">19TH-CENTURY LONG-DISTANCE TRADE CARAVAN NETWORKS IN EAST AFRICA</text>
  <text x="480" y="76" fill="#94a3b8" font-size="12" text-anchor="middle">Strategic Commercial Corridors: Central Route (Nyamwezi), Northern Route (Wanga/Kamba), and Southern Route (Yao)</text>

  <!-- Map Canvas (x: 40 to 610) -->
  <rect x="40" y="105" width="570" height="480" rx="12" fill="#161f30" stroke="#334155" stroke-width="1"/>

  <!-- Ocean Area -->
  <path d="M 500,105 Q 545,240 500,370 T 530,585 L 610,585 L 610,105 Z" fill="#0c4a6e" opacity="0.8"/>
  <text x="565" y="270" fill="#38bdf8" font-size="12" font-weight="bold" transform="rotate(90, 565, 270)" letter-spacing="2">INDIAN OCEAN</text>

  <!-- Lakes -->
  <!-- Lake Victoria -->
  <ellipse cx="260" cy="240" rx="48" ry="42" fill="#0284c7" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="260" y="244" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">L. Victoria</text>

  <!-- Lake Tanganyika -->
  <ellipse cx="120" cy="380" rx="14" ry="70" transform="rotate(-15, 120, 380)" fill="#0284c7" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="80" y="375" fill="#93c5fd" font-size="9" font-weight="bold">L. Tanganyika</text>

  <!-- Lake Nyasa / Malawi (South) -->
  <ellipse cx="230" cy="540" rx="12" ry="40" transform="rotate(-20, 230, 540)" fill="#0284c7" stroke="#38bdf8" stroke-width="1"/>
  <text x="200" y="545" fill="#93c5fd" font-size="8">L. Nyasa</text>

  <!-- ==================== TRADE ROUTES ==================== -->

  <!-- 1. CENTRAL ROUTE (Nyamwezi Core) - GOLD / AMBER -->
  <!-- Ujiji -> Tabora -> Mpwapwa -> Bagamoyo -> Zanzibar -->
  <path d="M 125,340 L 230,360 L 350,380 L 440,375 L 500,370" fill="none" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
  <!-- Branch to Buganda / Karagwe -->
  <path d="M 230,360 L 220,270 L 240,210" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5,4"/>

  <!-- 2. NORTHERN ROUTE (Kamba / Swahili / Wanga Gateway) - GREEN -->
  <!-- Mombasa -> Tsavo -> Machakos -> Naivasha -> Mumias (Wanga) -> Mt Elgon -->
  <path d="M 505,260 L 440,250 L 380,240 L 330,225 L 305,210" fill="none" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>

  <!-- 3. SOUTHERN ROUTE (Yao / Ngoni / Arabs) - RED -->
  <!-- Lake Nyasa -> Songea -> Kilwa Kivinje -->
  <path d="M 235,530 L 340,510 L 440,490 L 515,480" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Major Nodes / Hubs -->
  <!-- Tabora (Kazeh) -->
  <circle cx="230" cy="360" r="7" fill="#fbbf24" stroke="#78350f" stroke-width="2.5"/>
  <rect x="175" y="375" width="110" height="28" rx="5" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
  <text x="230" y="388" fill="#fde68a" font-size="9.5" font-weight="bold" text-anchor="middle">TABORA (Kazeh)</text>
  <text x="230" y="399" fill="#fef08a" font-size="8" text-anchor="middle">Nyamwezi Super-Hub</text>

  <!-- Ujiji -->
  <circle cx="125" cy="340" r="5" fill="#fbbf24" stroke="#78350f" stroke-width="1.5"/>
  <text x="135" y="338" fill="#fde68a" font-size="9" font-weight="bold">Ujiji</text>

  <!-- Mumias (Wanga Kingdom) -->
  <circle cx="305" cy="210" r="6" fill="#34d399" stroke="#064e3b" stroke-width="2"/>
  <text x="315" y="206" fill="#a7f3d0" font-size="9" font-weight="bold">Mumias (Wanga)</text>
  <text x="315" y="217" fill="#6ee7b7" font-size="7.5">Caravan Food Depot</text>

  <!-- Buganda Capital -->
  <circle cx="240" cy="205" r="5.5" fill="#c084fc" stroke="#581c87" stroke-width="1.5"/>
  <text x="230" y="196" fill="#e9d5ff" font-size="9" font-weight="bold" text-anchor="middle">Mengo (Buganda)</text>

  <!-- Coastal Ports -->
  <circle cx="505" cy="260" r="6" fill="#f8fafc" stroke="#10b981" stroke-width="2"/>
  <text x="495" y="255" fill="#ffffff" font-size="9.5" font-weight="bold" text-anchor="end">Mombasa</text>

  <circle cx="500" cy="370" r="6.5" fill="#f8fafc" stroke="#f59e0b" stroke-width="2"/>
  <text x="490" y="365" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="end">Bagamoyo</text>

  <ellipse cx="528" cy="360" rx="6" ry="14" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>
  <text x="540" y="364" fill="#38bdf8" font-size="9" font-weight="bold">Zanzibar</text>

  <circle cx="515" cy="480" r="5.5" fill="#f8fafc" stroke="#ef4444" stroke-width="1.5"/>
  <text x="505" y="475" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="end">Kilwa</text>

  <!-- Legend Inside Map Canvas -->
  <g transform="translate(50, 485)">
    <rect x="0" y="0" width="180" height="90" rx="8" fill="#0f172a" opacity="0.92" stroke="#334155" stroke-width="1"/>
    <text x="10" y="16" fill="#f8fafc" font-size="9.5" font-weight="bold">CARAVAN CORRIDORS</text>
    <line x1="10" y1="28" x2="35" y2="28" stroke="#f59e0b" stroke-width="3"/>
    <text x="42" y="31" fill="#e2e8f0" font-size="8.5">Central Route (Nyamwezi)</text>
    <line x1="10" y1="46" x2="35" y2="46" stroke="#10b981" stroke-width="3"/>
    <text x="42" y="49" fill="#e2e8f0" font-size="8.5">Northern Route (Wanga/Kamba)</text>
    <line x1="10" y1="64" x2="35" y2="64" stroke="#ef4444" stroke-width="3"/>
    <text x="42" y="67" fill="#e2e8f0" font-size="8.5">Southern Route (Yao/Kilwa)</text>
    <circle cx="20" cy="78" r="4" fill="#fbbf24"/>
    <text x="42" y="81" fill="#94a3b8" font-size="8">Major Inland Caravan Hub</text>
  </g>

  <!-- Right Column: Commodities & Historical Dynamics (x: 625 to 920) -->

  <!-- Box 1: Commodities Traded -->
  <rect x="625" y="105" width="295" height="175" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="625" y="105" width="295" height="28" rx="10" fill="url(#gradTradeCentral)"/>
  <text x="772" y="124" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">CARAVAN COMMODITY FLOWS</text>

  <text x="637" y="150" fill="#fbbf24" font-size="11" font-weight="bold">Interior to Coast Exports:</text>
  <text x="637" y="167" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold">Ivory:</tspan> Highly prized for luxury carving in Europe/Asia</text>
  <text x="637" y="183" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold">Copper &amp; Salt:</tspan> Smelted ingots from Katanga &amp; Uvinza</text>
  <text x="637" y="199" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold">Grain &amp; Iron Hoes:</tspan> Wanga food surpluses for caravans</text>

  <text x="637" y="222" fill="#38bdf8" font-size="11" font-weight="bold">Coast to Interior Imports:</text>
  <text x="637" y="239" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold">Cotton Cloth (*Kaniki/Merikani*):</tspan> Standard currency</text>
  <text x="637" y="255" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold">Firearms (*Guns/Powder*):</tspan> Transformed warfare</text>
  <text x="637" y="271" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold">Glass Beads, Brass Wire, &amp; Cowrie Shells</tspan></text>

  <!-- Box 2: Porters & Logistics -->
  <rect x="625" y="290" width="295" height="145" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <rect x="625" y="290" width="295" height="28" rx="10" fill="url(#gradTradeNorth)"/>
  <text x="772" y="309" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">NYAMWEZI PORTERS &amp; LOGISTICS</text>
  <text x="637" y="334" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold" fill="#6ee7b7">"Pagazi" (Professional Porters):</tspan> Highly skilled</text>
  <text x="637" y="350" fill="#e2e8f0" font-size="10.5">  caravan guides who marched 1,000+ km carrying</text>
  <text x="637" y="366" fill="#e2e8f0" font-size="10.5">  loads of up to 30 kg over demanding terrain.</text>
  <text x="637" y="388" fill="#e2e8f0" font-size="10.5">• <tspan font-weight="bold" fill="#6ee7b7">Guild Organization:</tspan> Established strict codes of</text>
  <text x="637" y="404" fill="#e2e8f0" font-size="10.5">  discipline, wage negotiations, and pathfinding.</text>
  <text x="637" y="424" fill="#94a3b8" font-size="9.5" font-style="italic">Foundation of East African regional mobility.</text>

  <!-- Box 3: Slave Trade Tragedy & Ethical Realities -->
  <rect x="625" y="445" width="295" height="140" rx="10" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <rect x="625" y="445" width="295" height="28" rx="10" fill="url(#gradTradeSouth)"/>
  <text x="772" y="464" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">TRAGIC CONTEXT: THE SLAVE TRADE</text>
  <text x="637" y="488" fill="#e2e8f0" font-size="10.5">• Coastal traders (e.g., Tippu Tip) expanded armed</text>
  <text x="637" y="504" fill="#e2e8f0" font-size="10.5">  slaving caravans alongside ivory procurement.</text>
  <text x="637" y="524" fill="#e2e8f0" font-size="10.5">• Caused severe depopulation and social trauma,</text>
  <text x="637" y="540" fill="#e2e8f0" font-size="10.5">  forcing communities to fortify or build standing armies.</text>
  <text x="637" y="562" fill="#fca5a5" font-size="9.5" font-style="italic">• A sobering reminder of the complex ethics of 19th C trade.</text>
</svg>'''

# =============================================================================
# SVG 4: Dynamic Transformation Model (Mirambo's Innovations) (Lesson 4)
# =============================================================================
SVG_DYNAMIC_TRANSFORMATION_MODEL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 580" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderTransform" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradForces" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="gradAdapt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradOutcomes" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="shadowTransform" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="550" rx="16" fill="url(#gradHeaderTransform)" stroke="#334155" stroke-width="1.5" filter="url(#shadowTransform)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="20" font-weight="bold" text-anchor="middle" letter-spacing="0.5">DYNAMIC HISTORICAL TRANSFORMATION: CHIEF MIRAMBO &amp; NYAMWEZI STATECRAFT</text>
  <text x="480" y="76" fill="#94a3b8" font-size="12" text-anchor="middle">How External 19th-Century Catalysts Drove Internal Military, Political, and Economic Revolution</text>

  <!-- 3-Column Flow Layout -->

  <!-- Column 1: External Catalysts / Forces of Change -->
  <rect x="35" y="110" width="265" height="425" rx="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" filter="url(#shadowTransform)"/>
  <rect x="35" y="110" width="265" height="38" rx="12" fill="url(#gradForces)"/>
  <text x="167" y="134" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">1. FORCES OF CHANGE</text>
  <text x="167" y="162" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">External 19th-Century Catalysts</text>

  <!-- Sub-card 1: Influx of Firearms -->
  <rect x="47" y="175" width="241" height="95" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="57" y="195" fill="#f87171" font-size="11.5" font-weight="bold">Influx of Muzzle-Loading Guns</text>
  <text x="57" y="214" fill="#e2e8f0" font-size="10.5">• Trade of ivory for guns (*bunduki*)</text>
  <text x="57" y="230" fill="#e2e8f0" font-size="10.5">• Revolutionized warfare &amp; defense</text>
  <text x="57" y="246" fill="#e2e8f0" font-size="10.5">• Traditional spears became obsolete</text>

  <!-- Sub-card 2: Caravan Trade Expansion -->
  <rect x="47" y="280" width="241" height="105" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="57" y="300" fill="#f87171" font-size="11.5" font-weight="bold">Coastal Commercial Incursion</text>
  <text x="57" y="319" fill="#e2e8f0" font-size="10.5">• Swahili-Arab merchants (e.g. Tabora)</text>
  <text x="57" y="335" fill="#e2e8f0" font-size="10.5">• High-stakes taxation (*Hongo* tolls)</text>
  <text x="57" y="351" fill="#e2e8f0" font-size="10.5">• Threat of merchant cartel monopoly</text>
  <text x="57" y="367" fill="#e2e8f0" font-size="10.5">• Destructive slave raid warfare</text>

  <!-- Sub-card 3: European Imperial Inquiries -->
  <rect x="47" y="395" width="241" height="105" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="57" y="415" fill="#f87171" font-size="11.5" font-weight="bold">Early European Envoys</text>
  <text x="57" y="434" fill="#e2e8f0" font-size="10.5">• Explorers (Burton, Speke, Stanley)</text>
  <text x="57" y="450" fill="#e2e8f0" font-size="10.5">• Christian missionary societies</text>
  <text x="57" y="466" fill="#e2e8f0" font-size="10.5">• Early imperial reconnaissance</text>
  <text x="57" y="482" fill="#e2e8f0" font-size="10.5">• Growing diplomatic complexity</text>

  <!-- Flow Arrow 1 -> 2 -->
  <path d="M 305,320 L 338,320" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="336,314 346,320 336,326" fill="#f59e0b"/>

  <!-- Column 2: Internal Adaptations (Mirambo's Statecraft) -->
  <rect x="348" y="110" width="265" height="425" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadowTransform)"/>
  <rect x="348" y="110" width="265" height="38" rx="12" fill="url(#gradAdapt)"/>
  <text x="480" y="134" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">2. INTERNAL ADAPTATIONS</text>
  <text x="480" y="162" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Mirambo's Strategic Statecraft</text>

  <!-- Sub-card 1: The Ruga-Ruga Army -->
  <rect x="360" y="175" width="241" height="105" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="370" y="195" fill="#fbbf24" font-size="11.5" font-weight="bold">The Professional "Ruga-Ruga"</text>
  <text x="370" y="214" fill="#e2e8f0" font-size="10.5">• Young, full-time professional army</text>
  <text x="370" y="230" fill="#e2e8f0" font-size="10.5">• Rigorous military discipline &amp; muskets</text>
  <text x="370" y="246" fill="#e2e8f0" font-size="10.5">• Replaced part-time seasonal warriors</text>
  <text x="370" y="262" fill="#e2e8f0" font-size="10.5">• Swift night marching tactics</text>

  <!-- Sub-card 2: Political Unification -->
  <rect x="360" y="290" width="241" height="100" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="370" y="310" fill="#fbbf24" font-size="11.5" font-weight="bold">Unification of 40+ Chiefdoms</text>
  <text x="370" y="329" fill="#e2e8f0" font-size="10.5">• Overcame decentralized fragmentation</text>
  <text x="370" y="345" fill="#e2e8f0" font-size="10.5">• Subjugated Uyowa, Ulyankhulu &amp; beyond</text>
  <text x="370" y="361" fill="#e2e8f0" font-size="10.5">• Built centralized administrative capital</text>
  <text x="370" y="377" fill="#e2e8f0" font-size="10.5">  at Isevike</text>

  <!-- Sub-card 3: Commercial Toll Control -->
  <rect x="360" y="400" width="241" height="100" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="370" y="420" fill="#fbbf24" font-size="11.5" font-weight="bold">Strategic Toll Enforcement</text>
  <text x="370" y="439" fill="#e2e8f0" font-size="10.5">• Controlled central trade corridor</text>
  <text x="370" y="455" fill="#e2e8f0" font-size="10.5">• Forced Arab merchants to pay *hongo*</text>
  <text x="370" y="471" fill="#e2e8f0" font-size="10.5">• Forged alliances with Kabaka Mutesa I</text>
  <text x="370" y="487" fill="#e2e8f0" font-size="10.5">  of Buganda</text>

  <!-- Flow Arrow 2 -> 3 -->
  <path d="M 618,320 L 651,320" fill="none" stroke="#10b981" stroke-width="3"/>
  <polygon points="649,314 659,320 649,326" fill="#10b981"/>

  <!-- Column 3: New Historical Realities / Outcomes -->
  <rect x="660" y="110" width="265" height="425" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5" filter="url(#shadowTransform)"/>
  <rect x="660" y="110" width="265" height="38" rx="12" fill="url(#gradOutcomes)"/>
  <text x="792" y="134" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">3. NEW HISTORICAL REALITIES</text>
  <text x="792" y="162" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Political &amp; Strategic Transformation</text>

  <!-- Sub-card 1: Centralized Empire -->
  <rect x="672" y="175" width="241" height="95" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="682" y="195" fill="#34d399" font-size="11.5" font-weight="bold">Rise of a Unified Empire</text>
  <text x="682" y="214" fill="#e2e8f0" font-size="10.5">• Nyamwezi transformed from loose</text>
  <text x="682" y="230" fill="#e2e8f0" font-size="10.5">  chiefdoms into formidable state</text>
  <text x="682" y="246" fill="#e2e8f0" font-size="10.5">• Demonstrated rapid political agility</text>

  <!-- Sub-card 2: Sovereignty & Diplomacy -->
  <rect x="672" y="280" width="241" height="105" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="682" y="300" fill="#34d399" font-size="11.5" font-weight="bold">African Diplomatic Agency</text>
  <text x="682" y="319" fill="#e2e8f0" font-size="10.5">• Negotiated as an equal with Sultan</text>
  <text x="682" y="335" fill="#e2e8f0" font-size="10.5">  Barghash of Zanzibar &amp; British</text>
  <text x="682" y="351" fill="#e2e8f0" font-size="10.5">• Called the "Napoleon of Central Africa"</text>
  <text x="682" y="367" fill="#e2e8f0" font-size="10.5">  by European travelers</text>

  <!-- Sub-card 3: Debunking Static Myths -->
  <rect x="672" y="395" width="241" height="110" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="682" y="415" fill="#34d399" font-size="11.5" font-weight="bold">Dynamic View of History</text>
  <text x="682" y="434" fill="#e2e8f0" font-size="10.5">• Shattered the racist colonial myth</text>
  <text x="682" y="450" fill="#e2e8f0" font-size="10.5">  that Africa was "stagnant &amp; unchanging"</text>
  <text x="682" y="466" fill="#e2e8f0" font-size="10.5">• Proved internal innovation, rapid</text>
  <text x="682" y="482" fill="#e2e8f0" font-size="10.5">  adaptation, and statecraft mastery</text>
</svg>'''

# =============================================================================
# SVG 5: Comparison: Traditional Court vs Modern Parliament (Lesson 5)
# =============================================================================
SVG_TRADITIONAL_VS_MODERN_GOVERNANCE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderCompare" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradTradCourt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <linearGradient id="gradModParl" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <filter id="shadowCompare" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderCompare)" stroke="#334155" stroke-width="1.5" filter="url(#shadowCompare)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="20" font-weight="bold" text-anchor="middle" letter-spacing="0.5">TRADITIONAL AFRICAN COUNCILS VS. MODERN DEMOCRATIC PARLIAMENTS</text>
  <text x="480" y="76" fill="#94a3b8" font-size="12" text-anchor="middle">Comparative Governance Analysis: Principles, Representation, Checks &amp; Balances, and Civic Synthesis</text>

  <!-- Side-by-Side Panels -->

  <!-- Left Panel: Traditional Court (Lukiiko / Eshihanya / Wanyampala) -->
  <rect x="35" y="105" width="430" height="375" rx="12" fill="#1e293b" stroke="#d97706" stroke-width="1.5" filter="url(#shadowCompare)"/>
  <rect x="35" y="105" width="430" height="36" rx="12" fill="url(#gradTradCourt)"/>
  <text x="250" y="129" fill="#ffffff" font-size="13.5" font-weight="bold" text-anchor="middle">TRADITIONAL AFRICAN ROYAL COURT &amp; ELDERS</text>

  <!-- Feature 1 -->
  <rect x="47" y="152" width="406" height="50" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="57" y="171" fill="#fbbf24" font-size="11" font-weight="bold">Basis of Authority:</text>
  <text x="57" y="189" fill="#e2e8f0" font-size="10.5">• Hereditary royal lineage (Kabaka/Nabongo), spiritual mandate &amp; ancestors</text>

  <!-- Feature 2 -->
  <rect x="47" y="210" width="406" height="62" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="57" y="228" fill="#fbbf24" font-size="11" font-weight="bold">Deliberation &amp; Law-Making:</text>
  <text x="57" y="246" fill="#e2e8f0" font-size="10.5">• Council of Elders (*Lukiiko / Eshihanya*) debating through consensus (*Palaver*)</text>
  <text x="57" y="262" fill="#e2e8f0" font-size="10.5">• Clan heads represent bloodlines, age-grades, and sacred guilds</text>

  <!-- Feature 3 -->
  <rect x="47" y="280" width="406" height="62" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="57" y="298" fill="#fbbf24" font-size="11" font-weight="bold">Checks and Balances:</text>
  <text x="57" y="316" fill="#e2e8f0" font-size="10.5">• Unwritten customary laws, moral taboos, and council vetos</text>
  <text x="57" y="332" fill="#e2e8f0" font-size="10.5">• Tyrannical rulers faced destooling, council rebellion, or mass emigration</text>

  <!-- Feature 4 -->
  <rect x="47" y="350" width="406" height="55" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="57" y="368" fill="#fbbf24" font-size="11" font-weight="bold">Civic Participation &amp; Duty:</text>
  <text x="57" y="386" fill="#e2e8f0" font-size="10.5">• Communitarian identity; communal labor (*Bulungi Bwansi*); clan loyalty</text>

  <!-- Feature 5 -->
  <rect x="47" y="413" width="406" height="55" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="57" y="431" fill="#fbbf24" font-size="11" font-weight="bold">Tenure of Office:</text>
  <text x="57" y="449" fill="#e2e8f0" font-size="10.5">• Life tenure (unless deposed, incapacitated, or ritually removed)</text>

  <!-- Right Panel: Modern Democratic Parliament (National Assembly) -->
  <rect x="495" y="105" width="430" height="375" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="1.5" filter="url(#shadowCompare)"/>
  <rect x="495" y="105" width="430" height="36" rx="12" fill="url(#gradModParl)"/>
  <text x="710" y="129" fill="#ffffff" font-size="13.5" font-weight="bold" text-anchor="middle">MODERN DEMOCRATIC NATIONAL ASSEMBLY</text>

  <!-- Feature 1 -->
  <rect x="507" y="152" width="406" height="50" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="517" y="171" fill="#38bdf8" font-size="11" font-weight="bold">Basis of Authority:</text>
  <text x="517" y="189" fill="#e2e8f0" font-size="10.5">• Popular sovereignty, supreme written Constitution, and universal adult suffrage</text>

  <!-- Feature 2 -->
  <rect x="507" y="210" width="406" height="62" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="517" y="228" fill="#38bdf8" font-size="11" font-weight="bold">Deliberation &amp; Law-Making:</text>
  <text x="517" y="246" fill="#e2e8f0" font-size="10.5">• Elected Members of Parliament (MPs/Senators) debating bills and voting</text>
  <text x="517" y="262" fill="#e2e8f0" font-size="10.5">• Formal Parliamentary Standing Orders, majority votes &amp; committee hearings</text>

  <!-- Feature 3 -->
  <rect x="507" y="280" width="406" height="62" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="517" y="298" fill="#38bdf8" font-size="11" font-weight="bold">Checks and Balances:</text>
  <text x="517" y="316" fill="#e2e8f0" font-size="10.5">• Separation of powers: Executive, Legislature, and Independent Judiciary</text>
  <text x="517" y="332" fill="#e2e8f0" font-size="10.5">• Impeachment proceedings, judicial constitutional review &amp; public ombudsmen</text>

  <!-- Feature 4 -->
  <rect x="507" y="350" width="406" height="55" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="517" y="368" fill="#38bdf8" font-size="11" font-weight="bold">Civic Participation &amp; Duty:</text>
  <text x="517" y="386" fill="#e2e8f0" font-size="10.5">• Universal Bill of Rights, public participation hearings, devolution to counties</text>

  <!-- Feature 5 -->
  <rect x="507" y="413" width="406" height="55" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="517" y="431" fill="#38bdf8" font-size="11" font-weight="bold">Tenure of Office:</text>
  <text x="517" y="449" fill="#e2e8f0" font-size="10.5">• Fixed, regular constitutional election cycles (e.g. 5-year terms)</text>

  <!-- Bottom Synthesis Banner: Shared Principles & Modern Synthesis (x: 35 to 925) -->
  <rect x="35" y="490" width="890" height="95" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
  <text x="480" y="512" fill="#34d399" font-size="12.5" font-weight="bold" text-anchor="middle">SYNTHESIS: COMBINING INDIGENOUS AFRICAN WISDOM WITH MODERN CONSTITUTIONAL DEMOCRACY</text>
  <text x="50" y="534" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Inclusive Consensus (*Palaver*):</tspan> Integrating traditional public dialogue into public participation hearings ensures marginalized voices are heard.</text>
  <text x="50" y="552" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Merit-Based Public Service:</tspan> Emulating Buganda’s professional civil service (*Bakungu*) combats modern tribalism and corruption.</text>
  <text x="50" y="570" fill="#e2e8f0" font-size="11">• <tspan font-weight="bold" fill="#6ee7b7">Cross-Border Integration:</tspan> Nyamwezi caravan diplomacy serves as the historical forerunner for East African Community (EAC) free trade.</text>
</svg>'''

# =============================================================================
# SVG 6: Comprehensive Comparative Matrix of East African Civilisations
# =============================================================================
SVG_WANGA_BUGANDA_NYAMWEZI_MATRIX = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderMatrix" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradWangaCol" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradBugandaCol" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="gradNyamweziCol" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="shadowMatrix" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderMatrix)" stroke="#334155" stroke-width="1.5" filter="url(#shadowMatrix)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="20" font-weight="bold" text-anchor="middle" letter-spacing="0.5">COMPARATIVE MATRIX: THREE PROMINENT EAST AFRICAN CIVILISATIONS</text>
  <text x="480" y="76" fill="#94a3b8" font-size="12" text-anchor="middle">Systematic Comparison Across Geography, Governance, Economy, Military, and Modern Historical Legacies</text>

  <!-- Column 1: Wanga Kingdom (Kenya) -->
  <rect x="35" y="105" width="285" height="480" rx="12" fill="#1e293b" stroke="#10b981" stroke-width="1.5" filter="url(#shadowMatrix)"/>
  <rect x="35" y="105" width="285" height="38" rx="12" fill="url(#gradWangaCol)"/>
  <text x="177" y="130" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">WANGA KINGDOM (KENYA)</text>

  <!-- Geography -->
  <rect x="45" y="150" width="265" height="65" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="55" y="167" fill="#6ee7b7" font-size="11" font-weight="bold">Location &amp; Geography:</text>
  <text x="55" y="184" fill="#e2e8f0" font-size="10">• Nzoia River basin, Western Kenya</text>
  <text x="55" y="200" fill="#e2e8f0" font-size="10">• Fertile agricultural plains &amp; riverine soils</text>

  <!-- Political Structure -->
  <rect x="45" y="222" width="265" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="55" y="239" fill="#6ee7b7" font-size="11" font-weight="bold">Governance Structure:</text>
  <text x="55" y="256" fill="#e2e8f0" font-size="10">• Centralized monarchy (Mwami / Nabongo)</text>
  <text x="55" y="272" fill="#e2e8f0" font-size="10">• Eshihanya (Council of Elders) checks</text>
  <text x="55" y="288" fill="#e2e8f0" font-size="10">• Clan head integration &amp; customary law</text>

  <!-- Economy & Technology -->
  <rect x="45" y="304" width="265" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="55" y="321" fill="#6ee7b7" font-size="11" font-weight="bold">Economy &amp; Technology:</text>
  <text x="55" y="338" fill="#e2e8f0" font-size="10">• Grain surplus (millet, sorghum, potato)</text>
  <text x="55" y="354" fill="#e2e8f0" font-size="10">• Advanced iron smelting guilds (jembes)</text>
  <text x="55" y="370" fill="#e2e8f0" font-size="10">• Essential food supply hub for caravans</text>

  <!-- Military & External Relations -->
  <rect x="45" y="386" width="265" height="65" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="55" y="403" fill="#6ee7b7" font-size="11" font-weight="bold">Military &amp; Diplomacy:</text>
  <text x="55" y="420" fill="#e2e8f0" font-size="10">• Clan warriors &amp; Maasai mercenary pacts</text>
  <text x="55" y="436" fill="#e2e8f0" font-size="10">• Nabongo Mumia diplomacy with British</text>

  <!-- Modern Legacy -->
  <rect x="45" y="458" width="265" height="115" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
  <text x="55" y="475" fill="#a7f3d0" font-size="11" font-weight="bold">Modern Legacy &amp; Lessons:</text>
  <text x="55" y="492" fill="#e2e8f0" font-size="10">• Inclusive multi-clan assimilation</text>
  <text x="55" y="508" fill="#e2e8f0" font-size="10">• Strategic diplomatic negotiation</text>
  <text x="55" y="524" fill="#e2e8f0" font-size="10">• Agricultural surplus as geopolitical</text>
  <text x="55" y="540" fill="#e2e8f0" font-size="10">  and commercial leverage</text>

  <!-- Column 2: Buganda Kingdom (Uganda) -->
  <rect x="338" y="105" width="285" height="480" rx="12" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.5" filter="url(#shadowMatrix)"/>
  <rect x="338" y="105" width="285" height="38" rx="12" fill="url(#gradBugandaCol)"/>
  <text x="480" y="130" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">BUGANDA KINGDOM (UGANDA)</text>

  <!-- Geography -->
  <rect x="348" y="150" width="265" height="65" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="358" y="167" fill="#c084fc" font-size="11" font-weight="bold">Location &amp; Geography:</text>
  <text x="358" y="184" fill="#e2e8f0" font-size="10">• Northern shores of Lake Victoria</text>
  <text x="358" y="200" fill="#e2e8f0" font-size="10">• High-rainfall tropical rainforest belt</text>

  <!-- Political Structure -->
  <rect x="348" y="222" width="265" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="358" y="239" fill="#c084fc" font-size="11" font-weight="bold">Governance Structure:</text>
  <text x="358" y="256" fill="#e2e8f0" font-size="10">• Absolute monarch (Kabaka)</text>
  <text x="358" y="272" fill="#e2e8f0" font-size="10">• Katikkiro (PM) &amp; Lukiiko (Parliament)</text>
  <text x="358" y="288" fill="#e2e8f0" font-size="10">• Appointed Saza &amp; Batongole chiefs</text>

  <!-- Economy & Technology -->
  <rect x="348" y="304" width="265" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="358" y="321" fill="#c084fc" font-size="11" font-weight="bold">Economy &amp; Technology:</text>
  <text x="358" y="338" fill="#e2e8f0" font-size="10">• Perennial Matooke (banana) plantations</text>
  <text x="358" y="354" fill="#e2e8f0" font-size="10">• Bark-cloth production &amp; pottery</text>
  <text x="358" y="370" fill="#e2e8f0" font-size="10">• High population density &amp; urbanization</text>

  <!-- Military & External Relations -->
  <rect x="348" y="386" width="265" height="65" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="358" y="403" fill="#c084fc" font-size="11" font-weight="bold">Military &amp; Diplomacy:</text>
  <text x="358" y="420" fill="#e2e8f0" font-size="10">• Lake Victoria plank-built war canoe navy</text>
  <text x="358" y="436" fill="#e2e8f0" font-size="10">• Standing infantry regiments &amp; firearms</text>

  <!-- Modern Legacy -->
  <rect x="348" y="458" width="265" height="115" rx="6" fill="#0f172a" stroke="#8b5cf6" stroke-width="1"/>
  <text x="358" y="475" fill="#d8b4fe" font-size="11" font-weight="bold">Modern Legacy &amp; Lessons:</text>
  <text x="358" y="492" fill="#e2e8f0" font-size="10">• Non-hereditary meritocratic civil service</text>
  <text x="358" y="508" fill="#e2e8f0" font-size="10">• Bulungi Bwansi (communal service)</text>
  <text x="358" y="524" fill="#e2e8f0" font-size="10">• Ecological food security via perennial</text>
  <text x="358" y="540" fill="#e2e8f0" font-size="10">  banana agroforestry systems</text>

  <!-- Column 3: Nyamwezi Chiefdoms (Tanzania) -->
  <rect x="640" y="105" width="285" height="480" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadowMatrix)"/>
  <rect x="640" y="105" width="285" height="38" rx="12" fill="url(#gradNyamweziCol)"/>
  <text x="782" y="130" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">NYAMWEZI CHIEFDOMS (TANZANIA)</text>

  <!-- Geography -->
  <rect x="650" y="150" width="265" height="65" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="660" y="167" fill="#fbbf24" font-size="11" font-weight="bold">Location &amp; Geography:</text>
  <text x="660" y="184" fill="#e2e8f0" font-size="10">• Central-western Tanzanian plateau</text>
  <text x="660" y="200" fill="#e2e8f0" font-size="10">• Drier miombo savannah &amp; open woodland</text>

  <!-- Political Structure -->
  <rect x="650" y="222" width="265" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="660" y="239" fill="#fbbf24" font-size="11" font-weight="bold">Governance Structure:</text>
  <text x="660" y="256" fill="#e2e8f0" font-size="10">• Decentralized independent chiefdoms</text>
  <text x="660" y="272" fill="#e2e8f0" font-size="10">• Ruled by Ntemi &amp; Wanyampala council</text>
  <text x="660" y="288" fill="#e2e8f0" font-size="10">• United under Mirambo in 1870s</text>

  <!-- Economy & Technology -->
  <rect x="650" y="304" width="265" height="75" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="660" y="321" fill="#fbbf24" font-size="11" font-weight="bold">Economy &amp; Technology:</text>
  <text x="660" y="338" fill="#e2e8f0" font-size="10">• Long-distance caravan trade pioneers</text>
  <text x="660" y="354" fill="#e2e8f0" font-size="10">• Ivory, copper, cloth, beads, firearms</text>
  <text x="660" y="370" fill="#e2e8f0" font-size="10">• Highly organized porter guilds (Pagazi)</text>

  <!-- Military & External Relations -->
  <rect x="650" y="386" width="265" height="65" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="660" y="403" fill="#fbbf24" font-size="11" font-weight="bold">Military &amp; Diplomacy:</text>
  <text x="660" y="420" fill="#e2e8f0" font-size="10">• Professional standing army (Ruga-Ruga)</text>
  <text x="660" y="436" fill="#e2e8f0" font-size="10">• Mirambo's firearm-based empire</text>

  <!-- Modern Legacy -->
  <rect x="650" y="458" width="265" height="115" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
  <text x="660" y="475" fill="#fde68a" font-size="11" font-weight="bold">Modern Legacy &amp; Lessons:</text>
  <text x="660" y="492" fill="#e2e8f0" font-size="10">• Regional economic integration (EAC forerunner)</text>
  <text x="660" y="508" fill="#e2e8f0" font-size="10">• Logistical prowess &amp; commercial grit</text>
  <text x="660" y="524" fill="#e2e8f0" font-size="10">• Consensus governance &amp; accountability</text>
  <text x="660" y="540" fill="#e2e8f0" font-size="10">  against tyrannical leadership</text>
</svg>'''
