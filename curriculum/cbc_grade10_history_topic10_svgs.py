"""
VLearn CBC Grade 10 History — Topic 10: Great Revolutions — The French Revolution
Authoritative High-Quality SVG Visual Assets and Historical Cartography / Diagrams
"""

# =============================================================================
# SVG 1: The Three Estates Social Pyramid (Lesson 1)
# =============================================================================
SVG_THREE_ESTATES_PYRAMID = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderEstates" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradFirstEstate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <linearGradient id="gradSecondEstate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="gradThirdEstate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="gradCardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <filter id="shadowPyramid" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderEstates)" stroke="#334155" stroke-width="1.5" filter="url(#shadowPyramid)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="19" font-weight="bold" text-anchor="middle" letter-spacing="0.5">THE THREE ESTATES OF THE ANCIEN RÉGIME (PRE-1789)</text>
  <text x="480" y="77" fill="#94a3b8" font-size="12" text-anchor="middle">Systemic Social Inequality, Land Monopoly, and Asymmetric Tax Distribution in Pre-Revolutionary France</text>

  <!-- Left Side: Visual Social Pyramid -->
  <!-- Top Tier: First Estate (Clergy) -->
  <polygon points="260,110 200,210 320,210" fill="url(#gradFirstEstate)" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="260" y="170" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">FIRST ESTATE</text>
  <text x="260" y="190" fill="#fee2e2" font-size="10.5" font-weight="bold" text-anchor="middle">Clergy (1%)</text>

  <!-- Middle Tier: Second Estate (Nobility) -->
  <polygon points="200,215 320,215 385,325 135,325" fill="url(#gradSecondEstate)" stroke="#d8b4fe" stroke-width="1.5"/>
  <text x="260" y="260" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">SECOND ESTATE</text>
  <text x="260" y="280" fill="#f3e8ff" font-size="11" font-weight="bold" text-anchor="middle">Nobility (2%)</text>
  <text x="260" y="300" fill="#e9d5ff" font-size="9.5" text-anchor="middle">Aristocracy, Landlords, High Command</text>

  <!-- Bottom Tier: Third Estate (Commoners) -->
  <polygon points="135,330 385,330 460,490 60,490" fill="url(#gradThirdEstate)" stroke="#7dd3fc" stroke-width="1.5"/>
  <text x="260" y="375" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">THIRD ESTATE (COMMONERS)</text>
  <text x="260" y="398" fill="#e0f2fe" font-size="12.5" font-weight="bold" text-anchor="middle">97% of Total Population (~26 Million)</text>
  
  <!-- Subdivisions inside Third Estate -->
  <line x1="100" y1="415" x2="420" y2="415" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="260" y="435" fill="#bae6fd" font-size="11" text-anchor="middle">Bourgeoisie (Merchants, Lawyers, Doctors, Bankers)</text>
  <text x="260" y="455" fill="#bae6fd" font-size="11" text-anchor="middle">Urban Artisans &amp; Wage Workers</text>
  <text x="260" y="475" fill="#bae6fd" font-size="11" text-anchor="middle">Peasant Farmers (80%+ of population)</text>

  <!-- Base Label -->
  <rect x="60" y="505" width="400" height="30" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="260" y="525" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">⚠ Carried 100% of Direct State Taxes &amp; Tithes</text>

  <!-- Right Side: Detailed Comparative Cards -->
  <!-- Card 1: First Estate -->
  <rect x="490" y="110" width="435" height="110" rx="10" fill="url(#gradCardBg)" stroke="#ef4444" stroke-width="1.5"/>
  <rect x="505" y="120" width="145" height="24" rx="5" fill="#ef4444"/>
  <text x="577" y="136" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">FIRST ESTATE: CLERGY</text>
  <text x="660" y="136" fill="#fca5a5" font-size="11" font-weight="bold">1% of Pop. | ~130,000</text>
  <text x="505" y="165" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#f8fafc">Land Monopoly:</tspan> Owned 10% of all fertile land in France</text>
  <text x="505" y="185" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#f87171">Tax Status:</tspan> Exempt from direct taxes (<tspan font-style="italic">Taille</tspan>); paid voluntary gift (<tspan font-style="italic">Don gratuit</tspan>)</text>
  <text x="505" y="205" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#38bdf8">Privileges:</tspan> Collected 10% religious tax (<tspan font-style="italic">Tithe</tspan>) from all Third Estate crops</text>

  <!-- Card 2: Second Estate -->
  <rect x="490" y="235" width="435" height="115" rx="10" fill="url(#gradCardBg)" stroke="#8b5cf6" stroke-width="1.5"/>
  <rect x="505" y="245" width="155" height="24" rx="5" fill="#8b5cf6"/>
  <text x="582" y="261" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">SECOND ESTATE: NOBILITY</text>
  <text x="670" y="261" fill="#d8b4fe" font-size="11" font-weight="bold">2% of Pop. | ~350,000</text>
  <text x="505" y="290" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#f8fafc">Land Monopoly:</tspan> Owned 25–30% of all agricultural land</text>
  <text x="505" y="310" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#f87171">Tax Status:</tspan> Completely exempt from the <tspan font-style="italic">Taille</tspan> and labor corvées</text>
  <text x="505" y="330" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#38bdf8">Monopolies:</tspan> Held all top government, judicial (<tspan font-style="italic">Parlements</tspan>), and military posts</text>

  <!-- Card 3: Third Estate -->
  <rect x="490" y="365" width="435" height="170" rx="10" fill="url(#gradCardBg)" stroke="#0284c7" stroke-width="1.5"/>
  <rect x="505" y="375" width="175" height="24" rx="5" fill="#0284c7"/>
  <text x="592" y="391" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">THIRD ESTATE: COMMONERS</text>
  <text x="690" y="391" fill="#7dd3fc" font-size="11" font-weight="bold">97% of Pop. | ~26,000,000</text>
  <text x="505" y="420" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#38bdf8">Bourgeoisie:</tspan> Wealthy and educated, but barred from noble titles and power</text>
  <text x="505" y="440" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#facc15">Urban Workers:</tspan> Vulnerable to bread inflation, high rents, and starvation</text>
  <text x="505" y="460" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#f87171">Peasantry:</tspan> Subject to forced labor (<tspan font-style="italic">Corvée</tspan>), feudal lord dues, royal taxes (<tspan font-style="italic">Gabelle</tspan>)</text>
  <text x="505" y="480" fill="#cbd5e1" font-size="11">• <tspan font-weight="bold" fill="#f8fafc">Tax Inequity:</tspan> Bore over 80% of personal income in combined tax extractions</text>
  <text x="505" y="500" fill="#f87171" font-size="10.5" font-style="italic">• Zero voting power under traditional Estates-General one-vote-per-estate system</text>

  <!-- Bottom Summary Banner -->
  <rect x="35" y="545" width="890" height="42" rx="8" fill="#111827" stroke="#334155" stroke-width="1"/>
  <text x="480" y="571" fill="#facc15" font-size="11.5" font-weight="bold" text-anchor="middle">⚡ Key Takeaway: The 3% privileged elite paid no taxes and controlled government, while the 97% productive base had zero voice.</text>
</svg>'''

# =============================================================================
# SVG 2: Timeline of Key Revolutionary Turning Points (Lesson 2)
# =============================================================================
SVG_REVOLUTIONARY_TIMELINE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderTimeline" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradModerate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="gradRadical" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#991b1b"/>
    </linearGradient>
    <linearGradient id="gradReaction" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <filter id="shadowTimeline" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderTimeline)" stroke="#334155" stroke-width="1.5" filter="url(#shadowTimeline)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="19" font-weight="bold" text-anchor="middle" letter-spacing="0.5">CHRONOLOGY &amp; TURNING POINTS OF THE FRENCH REVOLUTION (1789–1799)</text>
  <text x="480" y="77" fill="#94a3b8" font-size="12" text-anchor="middle">From the Constitutional Breakaway at Versailles to the Reign of Terror and the Rise of Napoleon</text>

  <!-- Phase Dividers & Labels -->
  <!-- Phase 1: Moderate Phase -->
  <rect x="40" y="105" width="370" height="26" rx="6" fill="#0369a1" opacity="0.4" stroke="#0284c7" stroke-width="1"/>
  <text x="225" y="122" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">PHASE 1: MODERATE &amp; CONSTITUTIONAL REFORM (1789–1792)</text>

  <!-- Phase 2: Radical Phase -->
  <rect x="420" y="105" width="290" height="26" rx="6" fill="#991b1b" opacity="0.4" stroke="#ef4444" stroke-width="1"/>
  <text x="565" y="122" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">PHASE 2: RADICAL TERROR (1792–1794)</text>

  <!-- Phase 3: Directory & Consulate -->
  <rect x="720" y="105" width="200" height="26" rx="6" fill="#6d28d9" opacity="0.4" stroke="#8b5cf6" stroke-width="1"/>
  <text x="820" y="122" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">PHASE 3: REACTION (1795–1799)</text>

  <!-- Central Horizontal Timeline Spine -->
  <line x1="60" y1="300" x2="900" y2="300" stroke="#475569" stroke-width="4"/>

  <!-- Milestone 1: May 1789 - Estates-General -->
  <line x1="90" y1="300" x2="90" y2="175" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="90" cy="300" r="7" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
  <rect x="40" y="145" width="115" height="90" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.2"/>
  <text x="97" y="162" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">MAY 5, 1789</text>
  <text x="97" y="177" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Estates-General</text>
  <text x="97" y="193" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Louis XVI convenes</text>
  <text x="97" y="206" fill="#cbd5e1" font-size="8.5" text-anchor="middle">assembly; dispute over</text>
  <text x="97" y="219" fill="#cbd5e1" font-size="8.5" text-anchor="middle">block voting rules</text>

  <!-- Milestone 2: June 1789 - Tennis Court Oath -->
  <line x1="205" y1="300" x2="205" y2="425" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="205" cy="300" r="7" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
  <rect x="150" y="340" width="125" height="95" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="1.2"/>
  <text x="212" y="358" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">JUNE 20, 1789</text>
  <text x="212" y="373" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Tennis Court Oath</text>
  <text x="212" y="389" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Third Estate forms</text>
  <text x="212" y="402" fill="#cbd5e1" font-size="8.5" text-anchor="middle">National Assembly;</text>
  <text x="212" y="415" fill="#cbd5e1" font-size="8.5" text-anchor="middle">vows a constitution</text>

  <!-- Milestone 3: July 14, 1789 - Storming of the Bastille -->
  <line x1="320" y1="300" x2="320" y2="175" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="320" cy="300" r="9" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
  <rect x="260" y="145" width="125" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="322" y="162" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">JULY 14, 1789</text>
  <text x="322" y="177" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Bastille Stormed</text>
  <text x="322" y="193" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Parisians seize prison</text>
  <text x="322" y="206" fill="#cbd5e1" font-size="8.5" text-anchor="middle">fortress &amp; gunpowder;</text>
  <text x="322" y="219" fill="#cbd5e1" font-size="8.5" text-anchor="middle">shatters royal power</text>

  <!-- Milestone 4: August 1789 - Declaration of Rights -->
  <line x1="435" y1="300" x2="435" y2="425" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="435" cy="300" r="7" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
  <rect x="375" y="340" width="125" height="95" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
  <text x="437" y="358" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">AUG 26, 1789</text>
  <text x="437" y="373" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Rights of Man</text>
  <text x="437" y="389" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Feudalism abolished;</text>
  <text x="437" y="402" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Liberty, Equality &amp;</text>
  <text x="437" y="415" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Popular Sovereignty</text>

  <!-- Milestone 5: Jan 1793 - Execution of Louis XVI -->
  <line x1="550" y1="300" x2="550" y2="175" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="550" cy="300" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
  <rect x="490" y="145" width="125" height="90" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.2"/>
  <text x="552" y="162" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">JAN 21, 1793</text>
  <text x="552" y="177" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">King Executed</text>
  <text x="552" y="193" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Louis XVI guillotined</text>
  <text x="552" y="206" fill="#cbd5e1" font-size="8.5" text-anchor="middle">for treason; European</text>
  <text x="552" y="219" fill="#cbd5e1" font-size="8.5" text-anchor="middle">powers invade France</text>

  <!-- Milestone 6: 1793-1794 - Reign of Terror -->
  <line x1="660" y1="300" x2="660" y2="425" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="660" cy="300" r="8" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
  <rect x="600" y="340" width="125" height="95" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="662" y="358" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">1793–1794</text>
  <text x="662" y="373" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Reign of Terror</text>
  <text x="662" y="389" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Robespierre &amp; Jacobins;</text>
  <text x="662" y="402" fill="#cbd5e1" font-size="8.5" text-anchor="middle">40,000+ executed;</text>
  <text x="662" y="415" fill="#cbd5e1" font-size="8.5" text-anchor="middle">ends July 1794</text>

  <!-- Milestone 7: 1799 - Coup of 18 Brumaire (Napoleon) -->
  <line x1="790" y1="300" x2="790" y2="175" stroke="#8b5cf6" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="790" cy="300" r="8" fill="#8b5cf6" stroke="#ffffff" stroke-width="2"/>
  <rect x="730" y="145" width="125" height="90" rx="8" fill="#1e293b" stroke="#8b5cf6" stroke-width="1.2"/>
  <text x="792" y="162" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">NOV 9, 1799</text>
  <text x="792" y="177" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Rise of Napoleon</text>
  <text x="792" y="193" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Napoleon Bonaparte</text>
  <text x="792" y="206" fill="#cbd5e1" font-size="8.5" text-anchor="middle">overthrows Directory;</text>
  <text x="792" y="219" fill="#cbd5e1" font-size="8.5" text-anchor="middle">establishes Consulate</text>

  <!-- Bottom Explanatory Strip -->
  <rect x="35" y="480" width="890" height="105" rx="10" fill="#111827" stroke="#334155" stroke-width="1"/>
  <text x="55" y="505" fill="#38bdf8" font-size="12" font-weight="bold">HISTORICAL PATTERN OF THE REVOLUTION:</text>
  <text x="55" y="528" fill="#cbd5e1" font-size="11">1. <tspan font-weight="bold" fill="#f8fafc">Constitutional Mobilization (1789):</tspan> Moderate Bourgeoisie seek constitutional monarchy and individual liberties.</text>
  <text x="55" y="548" fill="#cbd5e1" font-size="11">2. <tspan font-weight="bold" fill="#f87171">Foreign War &amp; Radical Terror (1792–1794):</tspan> External monarchical invasion causes paranoia, civil war, and suspension of rights.</text>
  <text x="55" y="568" fill="#cbd5e1" font-size="11">3. <tspan font-weight="bold" fill="#c084fc">Military Consolidation (1799):</tspan> Exhaustion from instability leads to military dictatorship while preserving key legal reforms.</text>
</svg>'''

# =============================================================================
# SVG 3: Global Ripples of 1789 Flow Diagram (Lesson 3)
# =============================================================================
SVG_GLOBAL_RIPPLES_1789 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderRipples" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradCoreFrance" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="gradHaiti" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradLatin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradEurope" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="gradModern" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899"/>
      <stop offset="100%" stop-color="#be185d"/>
    </linearGradient>
    <filter id="shadowRipples" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderRipples)" stroke="#334155" stroke-width="1.5" filter="url(#shadowRipples)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="19" font-weight="bold" text-anchor="middle" letter-spacing="0.5">GLOBAL RIPPLES OF 1789: CAUSE-AND-EFFECT FLOW</text>
  <text x="480" y="77" fill="#94a3b8" font-size="12" text-anchor="middle">How the French Revolution Catalyzed Global Anti-Slavery Revolts, Latin American Independence, and Nationalism</text>

  <!-- Central Origin Box: France 1789 -->
  <rect x="330" y="110" width="300" height="115" rx="12" fill="url(#gradCoreFrance)" stroke="#38bdf8" stroke-width="2"/>
  <text x="480" y="135" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">1. THE EPICENTER: FRANCE (1789)</text>
  <text x="480" y="155" fill="#e0f2fe" font-size="11" text-anchor="middle">• Collapse of Absolute Divine-Right Monarchy</text>
  <text x="480" y="173" fill="#e0f2fe" font-size="11" text-anchor="middle">• Declaration of the Rights of Man: "All Men Born Free"</text>
  <text x="480" y="191" fill="#e0f2fe" font-size="11" text-anchor="middle">• Abolition of Feudal Privileges &amp; Metric System</text>
  <text x="480" y="209" fill="#facc15" font-size="10.5" font-weight="bold" text-anchor="middle">Motto: "Liberté, Égalité, Fraternité"</text>

  <!-- Arrow Left Down: Caribbean / Haiti -->
  <path d="M 360,225 L 200,285" fill="none" stroke="#10b981" stroke-width="3"/>
  <polygon points="195,290 205,280 207,292" fill="#10b981"/>

  <!-- Arrow Middle Down: Europe / Nationalism -->
  <path d="M 480,225 L 480,285" fill="none" stroke="#8b5cf6" stroke-width="3"/>
  <polygon points="480,292 474,280 486,280" fill="#8b5cf6"/>

  <!-- Arrow Right Down: Latin America -->
  <path d="M 600,225 L 760,285" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="765,290 753,292 755,280" fill="#f59e0b"/>

  <!-- Branch 1: Haitian Revolution -->
  <rect x="40" y="295" width="275" height="150" rx="10" fill="url(#gradHaiti)" stroke="#34d399" stroke-width="1.5"/>
  <text x="177" y="320" fill="#ffffff" font-size="12.5" font-weight="bold" text-anchor="middle">2. HAITIAN REVOLUTION (1791–1804)</text>
  <text x="55" y="345" fill="#d1fae5" font-size="10.5">• <tspan font-weight="bold">Leader:</tspan> Toussaint Louverture</text>
  <text x="55" y="365" fill="#d1fae5" font-size="10.5">• Enslaved Africans applied "all men are free"</text>
  <text x="55" y="385" fill="#d1fae5" font-size="10.5">• Defeated French, British &amp; Spanish armies</text>
  <text x="55" y="405" fill="#d1fae5" font-size="10.5">• Created 1st free Black Republic in history</text>
  <text x="55" y="425" fill="#facc15" font-size="10" font-weight="bold">★ Benchmark of Universal Human Freedom</text>

  <!-- Branch 2: European Nationalism & Napoleonic Wars -->
  <rect x="345" y="295" width="270" height="150" rx="10" fill="url(#gradEurope)" stroke="#c084fc" stroke-width="1.5"/>
  <text x="480" y="320" fill="#ffffff" font-size="12.5" font-weight="bold" text-anchor="middle">3. EUROPEAN NATIONALISM</text>
  <text x="360" y="345" fill="#ede9fe" font-size="10.5">• <tspan font-weight="bold">Levée en Masse:</tspan> Mass citizen military draft</text>
  <text x="360" y="365" fill="#ede9fe" font-size="10.5">• Napoleonic Code exported legal equality</text>
  <text x="360" y="385" fill="#ede9fe" font-size="10.5">• Sparked anti-Napoleonic patriotism in</text>
  <text x="360" y="403" fill="#ede9fe" font-size="10.5">  Germany, Italy, and Spain</text>
  <text x="360" y="425" fill="#facc15" font-size="10" font-weight="bold">★ Birthed the Modern Nation-State Concept</text>

  <!-- Branch 3: Latin American Wars of Independence -->
  <rect x="645" y="295" width="275" height="150" rx="10" fill="url(#gradLatin)" stroke="#fcd34d" stroke-width="1.5"/>
  <text x="782" y="320" fill="#ffffff" font-size="12.5" font-weight="bold" text-anchor="middle">4. LATIN AMERICAN LIBERATION</text>
  <text x="660" y="345" fill="#fef3c7" font-size="10.5">• <tspan font-weight="bold">Leaders:</tspan> Simón Bolívar &amp; San Martín</text>
  <text x="660" y="365" fill="#fef3c7" font-size="10.5">• Napoleon's invasion of Spain (1808) broke</text>
  <text x="660" y="383" fill="#fef3c7" font-size="10.5">  Spanish colonial control in the Americas</text>
  <text x="660" y="403" fill="#fef3c7" font-size="10.5">• Creole leaders declared sovereign republics</text>
  <text x="660" y="425" fill="#facc15" font-size="10" font-weight="bold">★ Dismantled the Spanish Empire</text>

  <!-- Final Synthesis Banner: 20th/21st Century Human Rights & Kenya -->
  <rect x="35" y="465" width="890" height="120" rx="10" fill="#111827" stroke="#ec4899" stroke-width="1.5"/>
  <text x="480" y="490" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">5. ENDURING 21ST CENTURY CONSTITUTIONAL LEGACY</text>
  
  <rect x="55" y="505" width="405" height="68" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="257" y="525" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">UN Universal Declaration of Human Rights (1948)</text>
  <text x="70" y="545" fill="#cbd5e1" font-size="10">• Direct successor to 1789 Declaration of the Rights of Man</text>
  <text x="70" y="562" fill="#cbd5e1" font-size="10">• Established universal, indivisible rights across all nations</text>

  <rect x="495" y="505" width="415" height="68" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="702" y="525" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Constitution of Kenya (2010) — Bill of Rights</text>
  <text x="510" y="545" fill="#cbd5e1" font-size="10">• Article 1: "All sovereign power belongs to the people"</text>
  <text x="510" y="562" fill="#cbd5e1" font-size="10">• Article 27: Absolute equality and non-discrimination</text>
</svg>'''

# =============================================================================
# SVG 4: The Pillars of Civic Stewardship / Democratic Society (Lesson 4)
# =============================================================================
SVG_PILLARS_CIVIC_STEWARDSHIP = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background-color:#0f172a; font-family:'Segoe UI',system-ui,-apple-system,sans-serif;">
  <defs>
    <linearGradient id="gradHeaderPillars" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradDome" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="gradPillar1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="gradPillar2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="gradPillar3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradPillar4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#b91c1c"/>
    </linearGradient>
    <filter id="shadowPillars" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect x="15" y="15" width="930" height="590" rx="16" fill="url(#gradHeaderPillars)" stroke="#334155" stroke-width="1.5" filter="url(#shadowPillars)"/>

  <!-- Title Header -->
  <rect x="35" y="30" width="890" height="55" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="480" y="55" fill="#f8fafc" font-size="18" font-weight="bold" text-anchor="middle" letter-spacing="0.5">THE FOUR PILLARS OF CIVIC STEWARDSHIP &amp; DEMOCRATIC GOVERNANCE</text>
  <text x="480" y="74" fill="#94a3b8" font-size="11.5" text-anchor="middle">Synthesizing 1789 Revolutionary Principles with Kenya Constitution 2010 Democratic Values</text>

  <!-- Classical Architectural Pediment / Roof Structure -->
  <!-- Top Roof Triangle -->
  <polygon points="480,100 120,165 840,165" fill="url(#gradDome)" stroke="#bae6fd" stroke-width="2"/>
  <text x="480" y="142" fill="#ffffff" font-size="18" font-weight="bold" text-anchor="middle" letter-spacing="1">DEMOCRATIC SOCIETY &amp; POPULAR SOVEREIGNTY</text>
  <text x="480" y="157" fill="#e0f2fe" font-size="10.5" text-anchor="middle">"All sovereign power belongs to the people" (Art. 1, Constitution of Kenya / Art. 3, 1789 Declaration)</text>

  <!-- Architrave Beam -->
  <rect x="100" y="165" width="760" height="24" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <text x="480" y="181" fill="#facc15" font-size="11.5" font-weight="bold" text-anchor="middle">CONSTITUTIONAL BILL OF RIGHTS &amp; SEPARATION OF POWERS</text>

  <!-- 4 Classical Pillars -->
  <!-- Pillar 1: Universal Equality -->
  <rect x="110" y="195" width="170" height="295" rx="8" fill="url(#gradPillar1)" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="120" y="205" width="150" height="28" rx="4" fill="#0369a1"/>
  <text x="195" y="223" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">1. UNIVERSAL EQUALITY</text>
  <text x="125" y="255" fill="#e0f2fe" font-size="10">• <tspan font-weight="bold">Abolition of Privilege:</tspan></text>
  <text x="135" y="272" fill="#cbd5e1" font-size="9.5">No hereditary nobility,</text>
  <text x="135" y="287" fill="#cbd5e1" font-size="9.5">caste, or tax immunity.</text>
  <text x="125" y="312" fill="#e0f2fe" font-size="10">• <tspan font-weight="bold">Equality Before Law:</tspan></text>
  <text x="135" y="329" fill="#cbd5e1" font-size="9.5">Equal justice regardless</text>
  <text x="135" y="344" fill="#cbd5e1" font-size="9.5">of social standing.</text>
  <text x="125" y="369" fill="#e0f2fe" font-size="10">• <tspan font-weight="bold">Fair Taxation:</tspan></text>
  <text x="135" y="386" fill="#cbd5e1" font-size="9.5">Equitable revenue sharing</text>
  <text x="135" y="401" fill="#cbd5e1" font-size="9.5">and resource access.</text>
  <rect x="120" y="440" width="150" height="40" rx="4" fill="#0f172a" opacity="0.8"/>
  <text x="195" y="456" fill="#7dd3fc" font-size="9" font-weight="bold" text-anchor="middle">Kenya Const. Art. 27</text>
  <text x="195" y="470" fill="#94a3b8" font-size="8" text-anchor="middle">Equality &amp; Freedom from Bias</text>

  <!-- Pillar 2: Individual Liberty -->
  <rect x="300" y="195" width="170" height="295" rx="8" fill="url(#gradPillar2)" stroke="#34d399" stroke-width="1.5"/>
  <rect x="310" y="205" width="150" height="28" rx="4" fill="#047857"/>
  <text x="385" y="223" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle">2. INDIVIDUAL LIBERTY</text>
  <text x="315" y="255" fill="#d1fae5" font-size="10">• <tspan font-weight="bold">Core Freedoms:</tspan></text>
  <text x="325" y="272" fill="#cbd5e1" font-size="9.5">Speech, assembly,</text>
  <text x="325" y="287" fill="#cbd5e1" font-size="9.5">press, and religion.</text>
  <text x="315" y="312" fill="#d1fae5" font-size="10">• <tspan font-weight="bold">Bodily Security:</tspan></text>
  <text x="325" y="329" fill="#cbd5e1" font-size="9.5">Protection from arbitrary</text>
  <text x="325" y="344" fill="#cbd5e1" font-size="9.5">arrest without trial.</text>
  <text x="315" y="369" fill="#d1fae5" font-size="10">• <tspan font-weight="bold">Human Dignity:</tspan></text>
  <text x="325" y="386" fill="#cbd5e1" font-size="9.5">Universal rights inherent</text>
  <text x="325" y="401" fill="#cbd5e1" font-size="9.5">to every human being.</text>
  <rect x="310" y="440" width="150" height="40" rx="4" fill="#0f172a" opacity="0.8"/>
  <text x="385" y="456" fill="#6ee7b7" font-size="9" font-weight="bold" text-anchor="middle">Kenya Const. Art. 33–37</text>
  <text x="385" y="470" fill="#94a3b8" font-size="8" text-anchor="middle">Expression, Assembly &amp; Media</text>

  <!-- Pillar 3: Active Civic Participation -->
  <rect x="490" y="195" width="170" height="295" rx="8" fill="url(#gradPillar3)" stroke="#fcd34d" stroke-width="1.5"/>
  <rect x="500" y="205" width="150" height="28" rx="4" fill="#d97706"/>
  <text x="575" y="223" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. CIVIC PARTICIPATION</text>
  <text x="505" y="255" fill="#fef3c7" font-size="10">• <tspan font-weight="bold">Citizen Engagement:</tspan></text>
  <text x="515" y="272" fill="#cbd5e1" font-size="9.5">Voting, public forums,</text>
  <text x="515" y="287" fill="#cbd5e1" font-size="9.5">and budget hearings.</text>
  <text x="505" y="312" fill="#fef3c7" font-size="10">• <tspan font-weight="bold">Peaceful Advocacy:</tspan></text>
  <text x="515" y="329" fill="#cbd5e1" font-size="9.5">Constructive petitions</text>
  <text x="515" y="344" fill="#cbd5e1" font-size="9.5">and civic oversight.</text>
  <text x="505" y="369" fill="#fef3c7" font-size="10">• <tspan font-weight="bold">Shared Ownership:</tspan></text>
  <text x="515" y="386" fill="#cbd5e1" font-size="9.5">Democracy requires</text>
  <text x="515" y="401" fill="#cbd5e1" font-size="9.5">active, informed voters.</text>
  <rect x="500" y="440" width="150" height="40" rx="4" fill="#0f172a" opacity="0.8"/>
  <text x="575" y="456" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Kenya Const. Art. 10 &amp; 38</text>
  <text x="575" y="470" fill="#94a3b8" font-size="8" text-anchor="middle">National Values &amp; Political Rights</text>

  <!-- Pillar 4: Accountability of Power -->
  <rect x="680" y="195" width="170" height="295" rx="8" fill="url(#gradPillar4)" stroke="#f87171" stroke-width="1.5"/>
  <rect x="690" y="205" width="150" height="28" rx="4" fill="#b91c1c"/>
  <text x="765" y="223" fill="#ffffff" font-size="10.5" font-weight="bold" text-anchor="middle">4. ACCOUNTABILITY</text>
  <text x="695" y="255" fill="#fee2e2" font-size="10">• <tspan font-weight="bold">Rule of Law:</tspan></text>
  <text x="705" y="272" fill="#cbd5e1" font-size="9.5">No leader or party</text>
  <text x="705" y="287" fill="#cbd5e1" font-size="9.5">is above the law.</text>
  <text x="695" y="312" fill="#fee2e2" font-size="10">• <tspan font-weight="bold">Terror Warning:</tspan></text>
  <text x="705" y="329" fill="#cbd5e1" font-size="9.5">Unchecked power leads</text>
  <text x="705" y="344" fill="#cbd5e1" font-size="9.5">to tyranny and fear.</text>
  <text x="695" y="369" fill="#fee2e2" font-size="10">• <tspan font-weight="bold">Judicial Checks:</tspan></text>
  <text x="705" y="386" fill="#cbd5e1" font-size="9.5">Independent courts</text>
  <text x="705" y="401" fill="#cbd5e1" font-size="9.5">safeguard citizens.</text>
  <rect x="690" y="440" width="150" height="40" rx="4" fill="#0f172a" opacity="0.8"/>
  <text x="765" y="456" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Kenya Const. Chapter 6</text>
  <text x="765" y="470" fill="#94a3b8" font-size="8" text-anchor="middle">Leadership &amp; Integrity</text>

  <!-- Classical Base / Foundation -->
  <rect x="80" y="495" width="800" height="25" rx="4" fill="#334155" stroke="#475569" stroke-width="1"/>
  <text x="480" y="512" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">FOUNDATION: RULE OF LAW, INDEPENDENT JUDICIARY &amp; PUBLIC INTEGRITY</text>

  <!-- Bottom Synthesis Banner -->
  <rect x="35" y="530" width="890" height="55" rx="8" fill="#111827" stroke="#334155" stroke-width="1"/>
  <text x="480" y="552" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle">⚡ Core Synthesis for Grade 10 Learners:</text>
  <text x="480" y="571" fill="#cbd5e1" font-size="10.5" text-anchor="middle">Liberty without equality is privilege; equality without liberty is tyranny; both require active civic participation to survive.</text>
</svg>'''
