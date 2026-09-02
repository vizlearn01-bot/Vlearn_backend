"""
VLearn CBC Grade 10 History — Topic 7: Human Developments in Africa
Authoritative High-Quality SVG Visual Assets
"""

# =============================================================================
# SVG 1: The Human Development Capabilities Wheel (Lesson 1)
# =============================================================================
SVG_HUMAN_DEVELOPMENT_WHEEL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="hdHeaderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="centerHubGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="50%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="gradHealth" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="gradEdu" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#5b21b6"/>
    </linearGradient>
    <linearGradient id="gradLive" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradDignity" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradVoice" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <linearGradient id="gradEco" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14b8a6"/>
      <stop offset="100%" stop-color="#0f766e"/>
    </linearGradient>
    <filter id="glowShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#hdHeaderGrad)" stroke="#334155" stroke-width="1.5" filter="url(#glowShadow)"/>

  <!-- Title Header -->
  <rect x="35" y="28" width="890" height="54" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="52" fill="#f8fafc" font-size="18" font-weight="bold" text-anchor="middle" letter-spacing="0.5">THE HUMAN DEVELOPMENT CAPABILITIES WHEEL</text>
  <text x="480" y="70" fill="#94a3b8" font-size="12" text-anchor="middle">Expanding Human Freedoms, Agency, and Holistic Wellbeing Beyond Pure Economic Output (GDP)</text>

  <!-- Central Hub Circle -->
  <circle cx="480" cy="275" r="76" fill="url(#centerHubGrad)" stroke="#fde68a" stroke-width="3" filter="url(#glowShadow)"/>
  <text x="480" y="255" fill="#fef3c7" font-size="11" font-weight="600" text-anchor="middle" letter-spacing="1">CORE PARADIGM</text>
  <text x="480" y="275" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">HUMAN</text>
  <text x="480" y="293" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">DEVELOPMENT</text>
  <text x="480" y="310" fill="#fde68a" font-size="10" text-anchor="middle">Capabilities &amp; Freedoms</text>

  <!-- Connecting Spoke Lines -->
  <line x1="480" y1="199" x2="480" y2="155" stroke="#0284c7" stroke-width="3" stroke-dasharray="4 3"/>
  <line x1="545" y1="237" x2="650" y2="175" stroke="#7c3aed" stroke-width="3" stroke-dasharray="4 3"/>
  <line x1="545" y1="313" x2="650" y2="375" stroke="#059669" stroke-width="3" stroke-dasharray="4 3"/>
  <line x1="480" y1="351" x2="480" y2="400" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4 3"/>
  <line x1="415" y1="313" x2="310" y2="375" stroke="#ec4899" stroke-width="3" stroke-dasharray="4 3"/>
  <line x1="415" y1="237" x2="310" y2="175" stroke="#14b8a6" stroke-width="3" stroke-dasharray="4 3"/>

  <!-- Spoke Card 1: Health & Longevity (Top Center) -->
  <g transform="translate(365, 95)" filter="url(#glowShadow)">
    <rect x="0" y="0" width="230" height="75" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="22" rx="8" fill="url(#gradHealth)"/>
    <text x="115" y="15" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">1. HEALTH &amp; LONGEVITY</text>
    <text x="15" y="38" fill="#e2e8f0" font-size="10.5">• Freedom from disease &amp; hunger</text>
    <text x="15" y="52" fill="#e2e8f0" font-size="10.5">• Access to clean water &amp; nutrition</text>
    <text x="15" y="66" fill="#93c5fd" font-size="9.5">Life expectancy &amp; vitality</text>
  </g>

  <!-- Spoke Card 2: Knowledge & Education (Top Right) -->
  <g transform="translate(650, 140)" filter="url(#glowShadow)">
    <rect x="0" y="0" width="230" height="75" rx="8" fill="#1e293b" stroke="#7c3aed" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="22" rx="8" fill="url(#gradEdu)"/>
    <text x="115" y="15" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2. EDUCATION &amp; KNOWLEDGE</text>
    <text x="15" y="38" fill="#e2e8f0" font-size="10.5">• Critical thinking &amp; literacy</text>
    <text x="15" y="52" fill="#e2e8f0" font-size="10.5">• Indigenous ecological wisdom</text>
    <text x="15" y="66" fill="#c4b5fd" font-size="9.5">Lifelong capability expansion</text>
  </g>

  <!-- Spoke Card 3: Livelihood & Income (Bottom Right) -->
  <g transform="translate(650, 320)" filter="url(#glowShadow)">
    <rect x="0" y="0" width="230" height="75" rx="8" fill="#1e293b" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="22" rx="8" fill="url(#gradLive)"/>
    <text x="115" y="15" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. LIVELIHOOD &amp; INCOME</text>
    <text x="15" y="38" fill="#e2e8f0" font-size="10.5">• Decent standard of living</text>
    <text x="15" y="52" fill="#e2e8f0" font-size="10.5">• Productive agricultural/herding assets</text>
    <text x="15" y="66" fill="#6ee7b7" font-size="9.5">Material means for flourishing</text>
  </g>

  <!-- Spoke Card 4: Dignity & Security (Bottom Center) -->
  <g transform="translate(365, 385)" filter="url(#glowShadow)">
    <rect x="0" y="0" width="230" height="75" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="22" rx="8" fill="url(#gradDignity)"/>
    <text x="115" y="15" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">4. DIGNITY &amp; SECURITY</text>
    <text x="15" y="38" fill="#e2e8f0" font-size="10.5">• Freedom from violence &amp; fear</text>
    <text x="15" y="52" fill="#e2e8f0" font-size="10.5">• Cultural respect &amp; human rights</text>
    <text x="15" y="66" fill="#fcd34d" font-size="9.5">Safe, cohesive communities</text>
  </g>

  <!-- Spoke Card 5: Participation & Voice (Bottom Left) -->
  <g transform="translate(80, 320)" filter="url(#glowShadow)">
    <rect x="0" y="0" width="230" height="75" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="22" rx="8" fill="url(#gradVoice)"/>
    <text x="115" y="15" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">5. PARTICIPATION &amp; EQUALITY</text>
    <text x="15" y="38" fill="#e2e8f0" font-size="10.5">• Civic voice in community decisions</text>
    <text x="15" y="52" fill="#e2e8f0" font-size="10.5">• Gender equity &amp; inclusion</text>
    <text x="15" y="66" fill="#f472b6" font-size="9.5">Democratic governance &amp; agency</text>
  </g>

  <!-- Spoke Card 6: Ecological Harmony (Top Left) -->
  <g transform="translate(80, 140)" filter="url(#glowShadow)">
    <rect x="0" y="0" width="230" height="75" rx="8" fill="#1e293b" stroke="#14b8a6" stroke-width="2"/>
    <rect x="0" y="0" width="230" height="22" rx="8" fill="url(#gradEco)"/>
    <text x="115" y="15" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">6. ECOLOGICAL HARMONY</text>
    <text x="15" y="38" fill="#e2e8f0" font-size="10.5">• Sustainable resource stewardship</text>
    <text x="15" y="52" fill="#e2e8f0" font-size="10.5">• Climate resilience &amp; biodiversity</text>
    <text x="15" y="66" fill="#5eead4" font-size="9.5">Intergenerational planetary care</text>
  </g>

  <!-- Bottom Contrast Banner: GDP vs Human Development -->
  <g transform="translate(45, 485)">
    <rect x="0" y="0" width="870" height="95" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <!-- Left: GDP Narrow View -->
    <rect x="15" y="12" width="410" height="70" rx="6" fill="#0f172a" stroke="#dc2626" stroke-width="1"/>
    <text x="25" y="32" fill="#f87171" font-size="12" font-weight="bold">❌ NARROW ECONOMIC LENS (GDP ONLY)</text>
    <text x="25" y="50" fill="#94a3b8" font-size="11">• Measures total money flow &amp; production output</text>
    <text x="25" y="68" fill="#94a3b8" font-size="11">• Ignores wealth inequality, health, environmental degradation &amp; freedom</text>

    <!-- Right: Holistic Capabilities Approach -->
    <rect x="445" y="12" width="410" height="70" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="455" y="32" fill="#34d399" font-size="12" font-weight="bold">✔ HOLISTIC CAPABILITIES APPROACH (HUMAN DEVELOPMENT)</text>
    <text x="455" y="50" fill="#cbd5e1" font-size="11">• Evaluates what people can actually DO and BE in their lives</text>
    <text x="455" y="68" fill="#cbd5e1" font-size="11">• Economic growth is merely a means; human capability is the ultimate end</text>
  </g>
</svg>'''


# =============================================================================
# SVG 2: Neolithic Innovations & Socio-Economic Transformation Flowchart (Lesson 2)
# =============================================================================
SVG_NEOLITHIC_TRANSFORMATION_FLOWCHART = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="neoHeadGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="neoCol1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="neoCol2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="neoCol3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="neoCol4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="neoShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Outer Container -->
  <rect x="15" y="15" width="930" height="570" rx="16" fill="url(#neoHeadGrad)" stroke="#334155" stroke-width="1.5" filter="url(#neoShadow)"/>

  <!-- Title Header -->
  <rect x="35" y="28" width="890" height="56" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="52" fill="#f8fafc" font-size="18" font-weight="bold" text-anchor="middle" letter-spacing="0.5">THE NEOLITHIC REVOLUTION IN AFRICA: INNOVATION TO COMPLEX SOCIETIES</text>
  <text x="480" y="72" fill="#94a3b8" font-size="12" text-anchor="middle">How Indigenous Agricultural &amp; Material Discoveries Catalyzed Social Specialization and Civilizations</text>

  <!-- Step 1: Core Indigenous Innovations -->
  <g transform="translate(35, 105)" filter="url(#neoShadow)">
    <rect x="0" y="0" width="195" height="425" rx="10" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="195" height="36" rx="10" fill="url(#neoCol1)"/>
    <text x="97" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">1. CORE INNOVATIONS</text>
    
    <!-- Item 1: Crops -->
    <rect x="10" y="48" width="175" height="80" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="18" y="66" fill="#38bdf8" font-size="11" font-weight="bold">🌾 Indigenous Crops</text>
    <text x="18" y="82" fill="#cbd5e1" font-size="9.5">• Sorghum &amp; Pearl Millet</text>
    <text x="18" y="96" fill="#cbd5e1" font-size="9.5">• African Rice (O. glaberrima)</text>
    <text x="18" y="110" fill="#cbd5e1" font-size="9.5">• Yams &amp; Teff</text>

    <!-- Item 2: Animals -->
    <rect x="10" y="138" width="175" height="80" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="18" y="156" fill="#38bdf8" font-size="11" font-weight="bold">🐂 Livestock Taming</text>
    <text x="18" y="172" fill="#cbd5e1" font-size="9.5">• Humped Zebu Cattle</text>
    <text x="18" y="186" fill="#cbd5e1" font-size="9.5">• Longhorn cattle, Goats</text>
    <text x="18" y="200" fill="#cbd5e1" font-size="9.5">• Sheep &amp; Donkeys (traction)</text>

    <!-- Item 3: Material Tech -->
    <rect x="10" y="228" width="175" height="95" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="18" y="246" fill="#38bdf8" font-size="11" font-weight="bold">🏺 Material Tools</text>
    <text x="18" y="262" fill="#cbd5e1" font-size="9.5">• Polished ground stone axes</text>
    <text x="18" y="276" fill="#cbd5e1" font-size="9.5">• Microlith harvesting sickles</text>
    <text x="18" y="290" fill="#cbd5e1" font-size="9.5">• Ceramic pottery (Ounjougou,</text>
    <text x="18" y="304" fill="#cbd5e1" font-size="9.5">   Mali c. 9400 BCE)</text>

    <!-- Item 4: Knowledge -->
    <rect x="10" y="333" width="175" height="80" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="18" y="351" fill="#38bdf8" font-size="11" font-weight="bold">🧠 Botanical Wisdom</text>
    <text x="18" y="367" fill="#cbd5e1" font-size="9.5">• Seasonal cycle tracking</text>
    <text x="18" y="381" fill="#cbd5e1" font-size="9.5">• Seed selection &amp; breeding</text>
    <text x="18" y="395" fill="#cbd5e1" font-size="9.5">• Soil &amp; water observation</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 233 315 L 267 315" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <polygon points="267,310 277,315 267,320" fill="#38bdf8"/>

  <!-- Step 2: The Sedentary Shift -->
  <g transform="translate(270, 105)" filter="url(#neoShadow)">
    <rect x="0" y="0" width="195" height="425" rx="10" fill="#1e293b" stroke="#d97706" stroke-width="2"/>
    <rect x="0" y="0" width="195" height="36" rx="10" fill="url(#neoCol2)"/>
    <text x="97" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. SEDENTARY SHIFT</text>

    <rect x="10" y="48" width="175" height="110" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="0.8"/>
    <text x="18" y="68" fill="#fbbf24" font-size="11" font-weight="bold">🏠 Permanent Villages</text>
    <text x="18" y="86" fill="#cbd5e1" font-size="9.5">• Mud-brick &amp; thatch huts</text>
    <text x="18" y="100" fill="#cbd5e1" font-size="9.5">• Protective enclosure walls</text>
    <text x="18" y="114" fill="#cbd5e1" font-size="9.5">• Stable communal living</text>
    <text x="18" y="128" fill="#cbd5e1" font-size="9.5">• Safe living environments</text>

    <rect x="10" y="168" width="175" height="115" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="0.8"/>
    <text x="18" y="188" fill="#fbbf24" font-size="11" font-weight="bold">📦 Predictable Surplus</text>
    <text x="18" y="206" fill="#cbd5e1" font-size="9.5">• Grain silos &amp; clay granaries</text>
    <text x="18" y="220" fill="#cbd5e1" font-size="9.5">• Drought food buffers</text>
    <text x="18" y="234" fill="#cbd5e1" font-size="9.5">• Freedom from daily</text>
    <text x="18" y="248" fill="#cbd5e1" font-size="9.5">   foraging anxieties</text>

    <rect x="10" y="293" width="175" height="120" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="0.8"/>
    <text x="18" y="313" fill="#fbbf24" font-size="11" font-weight="bold">📈 Demographic Growth</text>
    <text x="18" y="331" fill="#cbd5e1" font-size="9.5">• Shorter weaning intervals</text>
    <text x="18" y="345" fill="#cbd5e1" font-size="9.5">• Lower infant mortality</text>
    <text x="18" y="359" fill="#cbd5e1" font-size="9.5">• Population density surges</text>
    <text x="18" y="373" fill="#cbd5e1" font-size="9.5">• Expanded workforce</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 468 315 L 502 315" stroke="#fbbf24" stroke-width="3" fill="none"/>
  <polygon points="502,310 512,315 502,320" fill="#fbbf24"/>

  <!-- Step 3: Division of Labor & Specialization -->
  <g transform="translate(505, 105)" filter="url(#neoShadow)">
    <rect x="0" y="0" width="195" height="425" rx="10" fill="#1e293b" stroke="#7c3aed" stroke-width="2"/>
    <rect x="0" y="0" width="195" height="36" rx="10" fill="url(#neoCol3)"/>
    <text x="97" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. DIVISION OF LABOR</text>

    <rect x="10" y="48" width="175" height="110" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="0.8"/>
    <text x="18" y="68" fill="#a78bfa" font-size="11" font-weight="bold">🛠 Specialized Vocations</text>
    <text x="18" y="86" fill="#cbd5e1" font-size="9.5">• Master potters &amp; weavers</text>
    <text x="18" y="100" fill="#cbd5e1" font-size="9.5">• Stone masons &amp; builders</text>
    <text x="18" y="114" fill="#cbd5e1" font-size="9.5">• Early metallurgists</text>
    <text x="18" y="128" fill="#cbd5e1" font-size="9.5">• Herbalists &amp; spiritual leaders</text>

    <rect x="10" y="168" width="175" height="115" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="0.8"/>
    <text x="18" y="188" fill="#a78bfa" font-size="11" font-weight="bold">⚖ Social Organization</text>
    <text x="18" y="206" fill="#cbd5e1" font-size="9.5">• Customary legal rules</text>
    <text x="18" y="220" fill="#cbd5e1" font-size="9.5">• Council of Elders</text>
    <text x="18" y="234" fill="#cbd5e1" font-size="9.5">• Age-set institutions</text>
    <text x="18" y="248" fill="#cbd5e1" font-size="9.5">• Property &amp; land norms</text>

    <rect x="10" y="293" width="175" height="120" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="0.8"/>
    <text x="18" y="313" fill="#a78bfa" font-size="11" font-weight="bold">🤝 Inter-Ecological Trade</text>
    <text x="18" y="331" fill="#cbd5e1" font-size="9.5">• Dried fish exchanged for</text>
    <text x="18" y="345" fill="#cbd5e1" font-size="9.5">   savannah grains</text>
    <text x="18" y="359" fill="#cbd5e1" font-size="9.5">• Salt, pottery &amp; stone tools</text>
    <text x="18" y="373" fill="#cbd5e1" font-size="9.5">• Regional barter networks</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 703 315 L 737 315" stroke="#a78bfa" stroke-width="3" fill="none"/>
  <polygon points="737,310 747,315 737,320" fill="#a78bfa"/>

  <!-- Step 4: Civilizational Foundations -->
  <g transform="translate(740, 105)" filter="url(#neoShadow)">
    <rect x="0" y="0" width="185" height="425" rx="10" fill="#1e293b" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="185" height="36" rx="10" fill="url(#neoCol4)"/>
    <text x="92" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">4. CIVILIZATION BASES</text>

    <rect x="8" y="48" width="169" height="110" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="16" y="68" fill="#34d399" font-size="11" font-weight="bold">🏛 Complex States</text>
    <text x="16" y="86" fill="#cbd5e1" font-size="9.5">• Centralized chiefdoms</text>
    <text x="16" y="100" fill="#cbd5e1" font-size="9.5">• Urban proto-cities</text>
    <text x="16" y="114" fill="#cbd5e1" font-size="9.5">• Defensive engineering</text>
    <text x="16" y="128" fill="#cbd5e1" font-size="9.5">• Complex tax/tribute</text>

    <rect x="8" y="168" width="169" height="115" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="16" y="188" fill="#34d399" font-size="11" font-weight="bold">📐 Sciences &amp; Arts</text>
    <text x="16" y="206" fill="#cbd5e1" font-size="9.5">• Solar &amp; lunar calendars</text>
    <text x="16" y="220" fill="#cbd5e1" font-size="9.5">• Field measurement (math)</text>
    <text x="16" y="234" fill="#cbd5e1" font-size="9.5">• Sahara rock paintings</text>
    <text x="16" y="248" fill="#cbd5e1" font-size="9.5">• Ceramic aesthetics</text>

    <rect x="8" y="293" width="169" height="120" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="16" y="313" fill="#34d399" font-size="11" font-weight="bold">🌍 Modern Legacy</text>
    <text x="16" y="331" fill="#cbd5e1" font-size="9.5">• Indigenous crop lineages</text>
    <text x="16" y="345" fill="#cbd5e1" font-size="9.5">   feeding billions today</text>
    <text x="16" y="359" fill="#cbd5e1" font-size="9.5">• Foundations of modern</text>
    <text x="16" y="373" fill="#cbd5e1" font-size="9.5">   agriculture &amp; architecture</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <rect x="35" y="540" width="890" height="32" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="480" y="561" fill="#cbd5e1" font-size="11.5" text-anchor="middle">
    <tspan fill="#38bdf8" font-weight="bold">Takeaway:</tspan> Agriculture created surplus food → Surplus enabled division of labor → Division of labor created modern technological and social institutions.
  </text>
</svg>'''


# =============================================================================
# SVG 3: Transhumance & Pastoralist Adaptive Strategy (Lesson 3)
# =============================================================================
SVG_TRANSHUMANCE_ADAPTIVE_CYCLE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 580" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="pastHeadGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="wetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="dryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <linearGradient id="instGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="pastShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Main Container -->
  <rect x="15" y="15" width="930" height="550" rx="16" fill="url(#pastHeadGrad)" stroke="#334155" stroke-width="1.5" filter="url(#pastShadow)"/>

  <!-- Title Header -->
  <rect x="35" y="28" width="890" height="56" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="52" fill="#f8fafc" font-size="18" font-weight="bold" text-anchor="middle" letter-spacing="0.5">PASTORALISM: ADAPTIVE TRANSHUMANCE &amp; RESOURCE GOVERNANCE IN ASALs</text>
  <text x="480" y="72" fill="#94a3b8" font-size="12" text-anchor="middle">How African Pastoralist Communities Convert Arid Grasslands into Resilient Livelihoods</text>

  <!-- Left Column: The Ecological Energy Bridge -->
  <g transform="translate(35, 100)" filter="url(#pastShadow)">
    <rect x="0" y="0" width="270" height="445" rx="12" fill="#1e293b" stroke="#0284c7" stroke-width="2"/>
    <rect x="0" y="0" width="270" height="34" rx="12" fill="url(#wetGrad)"/>
    <text x="135" y="22" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">1. ECOLOGICAL ENERGY BRIDGE</text>

    <!-- Sub-card 1 -->
    <rect x="12" y="46" width="246" height="82" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="22" y="66" fill="#38bdf8" font-size="11.5" font-weight="bold">🌿 Sparse Arid Grasslands</text>
    <text x="22" y="84" fill="#cbd5e1" font-size="10">• Rainfall &lt; 400mm/year (ASALs)</text>
    <text x="22" y="99" fill="#cbd5e1" font-size="10">• Inedible to humans; farming fails</text>
    <text x="22" y="114" fill="#93c5fd" font-size="9.5">Fragile, highly variable ecosystems</text>

    <!-- Sub-card 2 -->
    <rect x="12" y="138" width="246" height="90" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="22" y="158" fill="#38bdf8" font-size="11.5" font-weight="bold">🐄 Ruminant Livestock Digestion</text>
    <text x="22" y="176" fill="#cbd5e1" font-size="10">• Zebu cattle, goats, camels &amp; sheep</text>
    <text x="22" y="191" fill="#cbd5e1" font-size="10">• Multi-chamber stomachs digest scrub</text>
    <text x="22" y="206" fill="#cbd5e1" font-size="10">• Living transformers of sun &amp; grass</text>
    <text x="22" y="221" fill="#93c5fd" font-size="9.5">Mobile, renewable bio-wealth</text>

    <!-- Sub-card 3 -->
    <rect x="12" y="238" width="246" height="90" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="22" y="258" fill="#38bdf8" font-size="11.5" font-weight="bold">🥛 Nutrient-Rich Human Sustenance</text>
    <text x="22" y="276" fill="#cbd5e1" font-size="10">• Fresh &amp; fermented milk, blood, meat</text>
    <text x="22" y="291" fill="#cbd5e1" font-size="10">• Hides, skins, wool &amp; animal traction</text>
    <text x="22" y="306" fill="#cbd5e1" font-size="10">• Sustains millions in dry landscapes</text>
    <text x="22" y="321" fill="#93c5fd" font-size="9.5">High biological conversion efficiency</text>

    <!-- Sub-card 4: Ethno-veterinary -->
    <rect x="12" y="338" width="246" height="92" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="0.8"/>
    <text x="22" y="358" fill="#38bdf8" font-size="11.5" font-weight="bold">🔬 Ethno-Veterinary Science</text>
    <text x="22" y="376" fill="#cbd5e1" font-size="10">• Herbal vaccines &amp; tick management</text>
    <text x="22" y="391" fill="#cbd5e1" font-size="10">• Selective breeding for heat tolerance</text>
    <text x="22" y="406" fill="#cbd5e1" font-size="10">• Deep botanical and pasture memory</text>
    <text x="22" y="421" fill="#93c5fd" font-size="9.5">Indigenous science across generations</text>
  </g>

  <!-- Center Column: Seasonal Transhumance Cycle -->
  <g transform="translate(325, 100)" filter="url(#pastShadow)">
    <rect x="0" y="0" width="310" height="445" rx="12" fill="#1e293b" stroke="#d97706" stroke-width="2"/>
    <rect x="0" y="0" width="310" height="34" rx="12" fill="url(#dryGrad)"/>
    <text x="155" y="22" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. TRANSHUMANCE MOBILITY CYCLE</text>

    <!-- Wet Season Box -->
    <rect x="12" y="46" width="286" height="110" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="24" y="68" fill="#38bdf8" font-size="12" font-weight="bold">🌧 WET-SEASON DISPERSAL</text>
    <text x="24" y="88" fill="#cbd5e1" font-size="10.5">• Herds graze ephemeral wet plains</text>
    <text x="24" y="104" fill="#cbd5e1" font-size="10.5">• Drink from temporary pans &amp; pools</text>
    <text x="24" y="120" fill="#cbd5e1" font-size="10.5">• Dry-season reserves rest &amp; regrow</text>
    <text x="24" y="136" fill="#38bdf8" font-size="10">High milk yield, community festivities</text>

    <!-- Cycle Arrows -->
    <g transform="translate(155, 175)">
      <circle cx="0" cy="0" r="16" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
      <text x="0" y="5" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">⇅</text>
    </g>

    <!-- Dry Season Box -->
    <rect x="12" y="195" width="286" height="120" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1"/>
    <text x="24" y="217" fill="#fbbf24" font-size="12" font-weight="bold">☀️ DRY-SEASON RETREAT (ORONKEI)</text>
    <text x="24" y="237" fill="#cbd5e1" font-size="10.5">• Herds converge on perennial water</text>
    <text x="24" y="253" fill="#cbd5e1" font-size="10.5">• Deep wells (Tula wells) &amp; highland pastures</text>
    <text x="24" y="269" fill="#cbd5e1" font-size="10.5">• Controlled water turns by elder council</text>
    <text x="24" y="285" fill="#cbd5e1" font-size="10.5">• Prevents rangeland exhaustion</text>
    <text x="24" y="301" fill="#fcd34d" font-size="10">Strict rationing &amp; collective discipline</text>

    <!-- Bottom summary box -->
    <rect x="12" y="325" width="286" height="105" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="24" y="347" fill="#f8fafc" font-size="11.5" font-weight="bold">🎯 Strategic Principle:</text>
    <text x="24" y="367" fill="#94a3b8" font-size="10">• Mobility matches variable rainfall</text>
    <text x="24" y="383" fill="#94a3b8" font-size="10">• Avoids stationary overgrazing</text>
    <text x="24" y="399" fill="#94a3b8" font-size="10">• Not aimless wandering: structured, calculated</text>
    <text x="24" y="415" fill="#34d399" font-size="10" font-weight="600">Highest sustainable land-use efficiency</text>
  </g>

  <!-- Right Column: Customary Governance & Codes -->
  <g transform="translate(655, 100)" filter="url(#pastShadow)">
    <rect x="0" y="0" width="270" height="445" rx="12" fill="#1e293b" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="270" height="34" rx="12" fill="url(#instGrad)"/>
    <text x="135" y="22" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. SOCIAL GOVERNANCE</text>

    <!-- Maasai Age-set -->
    <rect x="12" y="46" width="246" height="92" rx="8" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="22" y="66" fill="#34d399" font-size="11.5" font-weight="bold">👑 Maasai Age-Set System (Rika)</text>
    <text x="22" y="84" fill="#cbd5e1" font-size="10">• Morans (warriors): herd defense &amp; treks</text>
    <text x="22" y="99" fill="#cbd5e1" font-size="10">• Elders: judicial authority &amp; peace</text>
    <text x="22" y="114" fill="#cbd5e1" font-size="10">• Communal land tenure (no private plots)</text>
    <text x="22" y="129" fill="#6ee7b7" font-size="9.5">Generational leadership continuity</text>

    <!-- Fulani Pulaaku -->
    <rect x="12" y="148" width="246" height="95" rx="8" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="22" y="168" fill="#34d399" font-size="11.5" font-weight="bold">🌟 Fulani Moral Code (Pulaaku)</text>
    <text x="22" y="186" fill="#cbd5e1" font-size="10">• Munyal (Patience &amp; self-control)</text>
    <text x="22" y="201" fill="#cbd5e1" font-size="10">• Gacce (Modesty &amp; dignity)</text>
    <text x="22" y="216" fill="#cbd5e1" font-size="10">• Hakkille (Mental discipline &amp; wisdom)</text>
    <text x="22" y="231" fill="#6ee7b7" font-size="9.5">Ethical guidelines for peaceful mobility</text>

    <!-- Deep Water Well Customary Rules -->
    <rect x="12" y="253" width="246" height="85" rx="8" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="22" y="273" fill="#34d399" font-size="11.5" font-weight="bold">💧 Deep Well Water Treaties</text>
    <text x="22" y="291" fill="#cbd5e1" font-size="10">• Borana / Maasai well masters</text>
    <text x="22" y="306" fill="#cbd5e1" font-size="10">• Water shared with visiting clans</text>
    <text x="22" y="321" fill="#6ee7b7" font-size="9.5">Prevents water-conflict during droughts</text>

    <!-- Social Cohesion -->
    <rect x="12" y="348" width="246" height="82" rx="8" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="22" y="368" fill="#34d399" font-size="11.5" font-weight="bold">🤝 Reciprocal Safety Nets</text>
    <text x="22" y="386" fill="#cbd5e1" font-size="10">• Herd gifting to restock ruined families</text>
    <text x="22" y="401" fill="#cbd5e1" font-size="10">• Collective disaster insurance</text>
    <text x="22" y="416" fill="#6ee7b7" font-size="9.5">Centuries of communal solidarity</text>
  </g>
</svg>'''


# =============================================================================
# SVG 4: Contemporary Challenges to Pastoralism Problem Tree (Lesson 4)
# =============================================================================
SVG_PASTORALISM_CHALLENGES_PROBLEM_TREE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="ptHeadGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="ptTrunkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="50%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
    <linearGradient id="ptRootGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="ptBranchGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#5b21b6"/>
    </linearGradient>
    <linearGradient id="ptSolGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <filter id="ptShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="610" rx="16" fill="url(#ptHeadGrad)" stroke="#334155" stroke-width="1.5" filter="url(#ptShadow)"/>

  <!-- Title Header -->
  <rect x="35" y="25" width="890" height="52" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="48" fill="#f8fafc" font-size="17" font-weight="bold" text-anchor="middle" letter-spacing="0.5">CONTEMPORARY CHALLENGES TO PASTORALISM: PROBLEM TREE &amp; SOLUTIONS</text>
  <text x="480" y="66" fill="#94a3b8" font-size="11.5" text-anchor="middle">Analyzing Root Causes, Systemic Impacts, and African Agency-Driven Policy Frameworks</text>

  <!-- Top Layer: Consequences / Effects (Branches) -->
  <g transform="translate(35, 88)">
    <text x="480" y="14" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">VISIBLE CONSEQUENCES &amp; SYMPTOMS (BRANCHES)</text>
    
    <!-- Impact 1: Conflicts -->
    <rect x="0" y="24" width="205" height="82" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="12" y="44" fill="#f87171" font-size="11" font-weight="bold">💥 Resource Conflicts</text>
    <text x="12" y="60" fill="#cbd5e1" font-size="9.5">• Grazing clashes &amp; cattle raids</text>
    <text x="12" y="74" fill="#cbd5e1" font-size="9.5">• Proliferation of small arms</text>
    <text x="12" y="88" fill="#fca5a5" font-size="9">Insecurity in border areas</text>

    <!-- Impact 2: Herd Starvation -->
    <rect x="225" y="24" width="205" height="82" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="237" y="44" fill="#f87171" font-size="11" font-weight="bold">☠ Herd Mortality</text>
    <text x="237" y="60" fill="#cbd5e1" font-size="9.5">• Millions of livestock perish</text>
    <text x="237" y="74" fill="#cbd5e1" font-size="9.5">• Loss of core family wealth</text>
    <text x="237" y="88" fill="#fca5a5" font-size="9">Acute nutritional crises</text>

    <!-- Impact 3: Poverty & Destitution -->
    <rect x="450" y="24" width="205" height="82" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="462" y="44" fill="#f87171" font-size="11" font-weight="bold">📉 Food Insecurity</text>
    <text x="462" y="60" fill="#cbd5e1" font-size="9.5">• Dependency on food aid</text>
    <text x="462" y="74" fill="#cbd5e1" font-size="9.5">• Displacement into relief camps</text>
    <text x="462" y="88" fill="#fca5a5" font-size="9">Compromised human dignity</text>

    <!-- Impact 4: Cultural Loss -->
    <rect x="675" y="24" width="215" height="82" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="687" y="44" fill="#f87171" font-size="11" font-weight="bold">🏚 Cultural Erosion</text>
    <text x="687" y="60" fill="#cbd5e1" font-size="9.5">• Youth drift to urban slums</text>
    <text x="687" y="74" fill="#cbd5e1" font-size="9.5">• Loss of botanical knowledge</text>
    <text x="687" y="88" fill="#fca5a5" font-size="9">Weakening of elder authority</text>
  </g>

  <!-- Central Connecting Branches (Lines) -->
  <path d="M 137 195 L 480 235" stroke="#ef4444" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
  <path d="M 327 195 L 480 235" stroke="#ef4444" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
  <path d="M 552 195 L 480 235" stroke="#ef4444" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
  <path d="M 782 195 L 480 235" stroke="#ef4444" stroke-width="2" fill="none" stroke-dasharray="3 3"/>

  <!-- Center: Core Problem Trunk -->
  <g transform="translate(180, 215)" filter="url(#ptShadow)">
    <rect x="0" y="0" width="600" height="74" rx="12" fill="url(#ptTrunkGrad)" stroke="#fca5a5" stroke-width="2"/>
    <text x="300" y="26" fill="#fef2f2" font-size="12" font-weight="600" text-anchor="middle" letter-spacing="1">CORE SYSTEMIC CRISIS (THE TRUNK)</text>
    <text x="300" y="48" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">ACUTE VULNERABILITY OF PASTORALIST LIVELIHOODS &amp; FREEDOMS</text>
    <text x="300" y="64" fill="#fed7aa" font-size="11" text-anchor="middle">Loss of Spatial Mobility, Resource Access, and Customary Adaptive Resilience</text>
  </g>

  <!-- Connecting Lines from Roots to Trunk -->
  <path d="M 140 340 L 480 290" stroke="#f59e0b" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
  <path d="M 330 340 L 480 290" stroke="#f59e0b" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
  <path d="M 630 340 L 480 290" stroke="#f59e0b" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
  <path d="M 820 340 L 480 290" stroke="#f59e0b" stroke-width="2" fill="none" stroke-dasharray="3 3"/>

  <!-- Bottom Layer: Root Causes (Roots) -->
  <g transform="translate(35, 310)">
    <text x="480" y="14" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">STRUCTURAL ROOT CAUSES (THE ROOTS)</text>

    <!-- Cause 1: Climate Change -->
    <rect x="0" y="24" width="205" height="92" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="12" y="44" fill="#fbbf24" font-size="11" font-weight="bold">🌡 Climate Extremes</text>
    <text x="12" y="60" fill="#cbd5e1" font-size="9.5">• Drought every 2 yrs (was 10)</text>
    <text x="12" y="74" fill="#cbd5e1" font-size="9.5">• Water pans drying rapidly</text>
    <text x="12" y="88" fill="#cbd5e1" font-size="9.5">• Unpredictable flash floods</text>
    <text x="12" y="103" fill="#fde68a" font-size="9">Ecosystem stress</text>

    <!-- Cause 2: Land Fencing -->
    <rect x="225" y="24" width="205" height="92" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="237" y="44" fill="#fbbf24" font-size="11" font-weight="bold">🚧 Land Fencing &amp; Subdiv.</text>
    <text x="237" y="60" fill="#cbd5e1" font-size="9.5">• Communal rangeland sold</text>
    <text x="237" y="74" fill="#cbd5e1" font-size="9.5">• Migration corridors blocked</text>
    <text x="237" y="88" fill="#cbd5e1" font-size="9.5">• Wildlife park expansions</text>
    <text x="237" y="103" fill="#fde68a" font-size="9">Trapped livestock herds</text>

    <!-- Cause 3: Inadequate Services -->
    <rect x="450" y="24" width="205" height="92" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="462" y="44" fill="#fbbf24" font-size="11" font-weight="bold">🏥 Stationary Services Deficit</text>
    <text x="462" y="60" fill="#cbd5e1" font-size="9.5">• Fixed schools fail migrants</text>
    <text x="462" y="74" fill="#cbd5e1" font-size="9.5">• Severe lack of vet clinics</text>
    <text x="462" y="88" fill="#cbd5e1" font-size="9.5">• Poor road &amp; water infrastructure</text>
    <text x="462" y="103" fill="#fde68a" font-size="9">High illiteracy &amp; disease</text>

    <!-- Cause 4: Marginalization -->
    <rect x="675" y="24" width="215" height="92" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" filter="url(#ptShadow)"/>
    <text x="687" y="44" fill="#fbbf24" font-size="11" font-weight="bold">🏛 Political Marginalization</text>
    <text x="687" y="60" fill="#cbd5e1" font-size="9.5">• ASALs underfunded in budgets</text>
    <text x="687" y="74" fill="#cbd5e1" font-size="9.5">• Disregard of customary tenure</text>
    <text x="687" y="88" fill="#cbd5e1" font-size="9.5">• Paternalistic policy bias</text>
    <text x="687" y="103" fill="#fde68a" font-size="9">Lack of policy voice</text>
  </g>

  <!-- Bottom Crown: Agency-Driven Policy Solutions (Green Canopy) -->
  <g transform="translate(35, 455)" filter="url(#ptShadow)">
    <rect x="0" y="0" width="890" height="155" rx="12" fill="#1e293b" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="890" height="28" rx="12" fill="url(#ptSolGrad)"/>
    <text x="445" y="19" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">✔ STRATEGIC POLICY SOLUTIONS &amp; AFRICAN AGENCY (TRANSFORMATIVE CANOPY)</text>

    <!-- Solution 1: Conservancies -->
    <rect x="15" y="38" width="160" height="105" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="23" y="56" fill="#34d399" font-size="10.5" font-weight="bold">🗺 Communal Conservancies</text>
    <text x="23" y="72" fill="#cbd5e1" font-size="9">• GPS pasture mapping</text>
    <text x="23" y="86" fill="#cbd5e1" font-size="9">• Rotational zoning</text>
    <text x="23" y="100" fill="#cbd5e1" font-size="9">• Elder rangeland rules</text>
    <text x="23" y="114" fill="#cbd5e1" font-size="9">• Grass restoration</text>
    <text x="23" y="130" fill="#6ee7b7" font-size="8.5">N. Kenya model</text>

    <!-- Solution 2: Mobile Services -->
    <rect x="188" y="38" width="160" height="105" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="196" y="56" fill="#34d399" font-size="10.5" font-weight="bold">🐪 Mobile Basic Services</text>
    <text x="196" y="72" fill="#cbd5e1" font-size="9">• Camel-back schools</text>
    <text x="196" y="86" fill="#cbd5e1" font-size="9">• Tent classrooms on treks</text>
    <text x="196" y="100" fill="#cbd5e1" font-size="9">• Mobile vaccine units</text>
    <text x="196" y="114" fill="#cbd5e1" font-size="9">• Solar power clinics</text>
    <text x="196" y="130" fill="#6ee7b7" font-size="8.5">Education on the move</text>

    <!-- Solution 3: Livelihood Diversification -->
    <rect x="361" y="38" width="160" height="105" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="369" y="56" fill="#34d399" font-size="10.5" font-weight="bold">🍯 Livelihood Diversity</text>
    <text x="369" y="72" fill="#cbd5e1" font-size="9">• Beekeeping &amp; honey</text>
    <text x="369" y="86" fill="#cbd5e1" font-size="9">• Women artisan co-ops</text>
    <text x="369" y="100" fill="#cbd5e1" font-size="9">• Eco-tourism guiding</text>
    <text x="369" y="114" fill="#cbd5e1" font-size="9">• Gum arabic harvesting</text>
    <text x="369" y="130" fill="#6ee7b7" font-size="8.5">Non-livestock income</text>

    <!-- Solution 4: Peace Treaties -->
    <rect x="534" y="38" width="165" height="105" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="542" y="56" fill="#34d399" font-size="10.5" font-weight="bold">🕊 Peace Caravans</text>
    <text x="542" y="72" fill="#cbd5e1" font-size="9">• Youth &amp; elder emissaries</text>
    <text x="542" y="86" fill="#cbd5e1" font-size="9">• Advance grazing pacts</text>
    <text x="542" y="100" fill="#cbd5e1" font-size="9">• Joint water committees</text>
    <text x="542" y="114" fill="#cbd5e1" font-size="9">• Cross-border treaties</text>
    <text x="542" y="130" fill="#6ee7b7" font-size="8.5">Traditional diplomacy</text>

    <!-- Solution 5: Legal Advocacy -->
    <rect x="712" y="38" width="163" height="105" rx="6" fill="#0f172a" stroke="#059669" stroke-width="0.8"/>
    <text x="720" y="56" fill="#34d399" font-size="10.5" font-weight="bold">⚖ Legal Empowerment</text>
    <text x="720" y="72" fill="#cbd5e1" font-size="9">• Communal Land Acts</text>
    <text x="720" y="86" fill="#cbd5e1" font-size="9">• ASAL budget allocation</text>
    <text x="720" y="100" fill="#cbd5e1" font-size="9">• Legal title to corridors</text>
    <text x="720" y="114" fill="#cbd5e1" font-size="9">• Parliamentary caucuses</text>
    <text x="720" y="130" fill="#6ee7b7" font-size="8.5">Structural protection</text>
  </g>
</svg>'''
